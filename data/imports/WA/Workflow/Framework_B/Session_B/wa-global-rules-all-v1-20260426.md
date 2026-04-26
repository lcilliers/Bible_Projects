# wa-global-rules — All Active Rules

_Source: `wa_rule_registry` (DB is source-of-truth post-M33) · `obsolete=0` only · generated 2026-04-26 07:04Z_

**Total active rules: 34 across 12 categories.**

## Category summary

| Category | Active count |
|---|---:|
| `cadence_discipline` | 1 |
| `data_discipline` | 5 |
| `database_discipline` | 1 |
| `document_discipline` | 2 |
| `file_format` | 1 |
| `file_naming` | 6 |
| `file_output` | 1 |
| `pass_close` | 1 |
| `process_discipline` | 5 |
| `programme_orientation` | 8 |
| `researcher_decision` | 1 |
| `session_startup` | 2 |

---

## Category: `cadence_discipline` (1 active)

### `GR-CAD-001` — Write-cadence self-check and present-files milestone

- **Version:** 1_1  ·  **Applies to:** all sessions, all phases
- **Added:** 20260417  ·  **Last modified:** 2026-04-21T08:47:37Z

**Rule text:**

> Before every substantive response, Claude AI produces a short self-check at the top of the response, naming: (a) what was written to disk in this turn, with filenames; (b) whether present_files was called on those writes; (c) if nothing was written, a one-line statement that the response is discussion-only. After every substantive write to disk, Claude AI calls present_files on the written file(s). This rule is non-waivable.

**Rationale:**

> Claude AI tends to accumulate findings in chat and in-session memory rather than writing them to disk. Chat output is ephemeral; in-session memory is lost when the session ends or the context window truncates. The self-check and the present_files call after writes make the save state externally visible on every turn, so the researcher sees at a glance whether the work has been preserved.

**Application notes:**

> What counts as a substantive write. A substantive write is any write that produces or updates: a finding, a decision, a patch, an entry in an observations log, an entry in a session log, or a new version of any file. Routine intermediate scratch (temporary working files in /home/claude that are not intended as deliverables) does not count.
>
> Self-check when nothing was written. The 'discussion-only' statement is not a workaround. It applies when the turn genuinely produced no substantive content — a clarification exchange, a question being asked, a short acknowledgement. If work was done, it is written; the self-check then names the write.

**Examples:**

> Self-check when a file was written: 'Writes this turn: obslog appended — wa-{reference}-obslog-v{n}-{YYYYMMDD}.md. present_files called: yes.'
>
> Self-check when nothing was written: 'Nothing written this turn — response is discussion-only.'

---

## Category: `data_discipline` (5 active)

### `GR-DATA-001` — Active terms filter — mandatory for all mti_terms queries

- **Version:** 2_1  ·  **Applies to:** all sessions, all phases
- **Added:** 20260414  ·  **Last modified:** 2026-04-21T08:48:04Z

**Rule text:**

> All SQL queries against `mti_terms` that are intended to return active terms must include: `AND mt.status IN ('extracted', 'extracted_thin')`. Queries that omit this filter return deleted terms and produce incorrect counts. This filter is non-waivable for any query where "active terms" is the intent.

---

### `GR-DATA-002` — Extract is authoritative for Session B — not prior session outputs

- **Version:** 2_1  ·  **Applies to:** Session B instruction
- **Added:** 20260414  ·  **Last modified:** 2026-04-21T08:47:50Z

**Rule text:**

> The current versioned extract produced by Claude Code is the authoritative data source for Session B analysis. Prior session outputs — observations logs, word studies, analytical briefs — are reference material only and do not override extract data. Where a prior output conflicts with the extract, the extract is correct and the prior output requires correction.

---

### `GR-DATA-003` — mti_term_flags authoritative field for somatic classification

- **Version:** 2_1  ·  **Applies to:** Session B instruction, all somatic classification work
- **Added:** 20260414  ·  **Last modified:** 2026-04-21T08:48:04Z

**Rule text:**

> The authoritative field for somatic classification is `mti_term_flags`, not the redundant `wa_term_inventory.somatic_link` field. Where a conflict exists between these two sources, `mti_term_flags` is correct.

---

### `GR-DATA-004` — Complete word data export carries a version number — confirm before proceeding

- **Version:** 2_1  ·  **Applies to:** Session B instruction
- **Added:** 20260414  ·  **Last modified:** 2026-04-21T08:47:50Z

**Rule text:**

> The complete word data export is a versioned file managed by Claude Code. Claude AI confirms the version number of the export at session start, before analytical work begins. If the version is not confirmed, Claude AI requests it from Claude Code. Claude AI does not proceed on an extract whose version has not been confirmed in the current session.

---

### `GR-DATA-005` — god_as_subject and somatic_link fields — verify before setting

- **Version:** 2_1  ·  **Applies to:** Session B instruction
- **Added:** 20260414  ·  **Last modified:** 2026-04-21T08:48:04Z

**Rule text:**

> The fields `god_as_subject` and `somatic_link` on `wa_term_inventory` carry a high error rate from bulk operations. Before setting or relying on these fields in Session B, Claude AI verifies the values against the actual verse evidence for each term. A field value not verified against verse evidence is not confirmed.

---

## Category: `database_discipline` (1 active)

### `GR-DB-001` — No DB state assumptions — always verify

- **Version:** 1_1  ·  **Applies to:** all sessions, all phases
- **Added:** 20260415  ·  **Last modified:** 2026-04-21T08:47:37Z

**Rule text:**

> Claude AI never assumes the current state of the database. Before any operation that depends on DB state: (1) check the current chat for data already provided — do not re-request what is already present; (2) if the required data is not in the chat, request it explicitly from Claude Code via a query; (3) if data was provided earlier in the chat but may be stale, request a refresh. Proceeding on assumed DB state is a violation regardless of how recent or reliable the assumption appears.

**Rationale:**

> The database changes between turns. Other patches apply; other sessions run; the extract held in chat becomes stale without notice. 'Recent' is not 'current' — an assumption that was true last turn may be wrong this turn. Operations built on stale state produce inconsistencies that compound across a batch of work. The three-step check costs little; the alternative is the class of errors where the fix is harder than the original operation would have been.

**Application notes:**

> What counts as DB state. Row counts, field values, flag states, resolution status, schema structure, existence or absence of records, referential integrity, and the presence or absence of patches in a log. If an action depends on any of these, the three-step check applies.
>
> 'Assumed' includes memory. If Claude AI's memory of a DB fact is from a previous session, it is an assumption, not current state — the three-step check applies, starting from step 2 (request from CC) because the chat will not contain the data.

---

## Category: `document_discipline` (2 active)

### `GR-REF-001` — Single-authority content referencing across documents

- **Version:** 1_1  ·  **Applies to:** all sessions, all phases, every document
- **Added:** 20260418  ·  **Last modified:** 2026-04-21T07:08:02Z

**Rule text:**

> Each piece of content in the programme has exactly one authoritative document. Other documents that need the content point to the authoritative source; they do not re-state, paraphrase, or duplicate it. Five disciplines enforce this:
>
> (1) Pointer, not copy. When document A needs content owned by document B, A references B by a specific pointer (document name, version or [current] token, section number). A does not re-state B's content inline.
>
> (2) Versioned, dated references. Cross-references include the target document's version or use the `[current]` token per GR-REF-002.
>
> (3) Single authoritative document per content type. Each content type has exactly one owning document. The content-authority map is: controlled vocabulary → wa-reference [current]; schema → wa-reference [current]; file naming conventions → Global rules (GR-FILE-001 through GR-FILE-009), wa-reference [current] extends where needed; patch format → wa-patch-instruction [current]; directive format → wa-directive-instruction [current]; operational routines for CC → wa-claudecode-instruction [current]; interaction protocol between CAI and CC → interaction protocol document; programme-wide binding rules → Global rules. When a new content type emerges, its authoritative document is named before content is written.
>
> (4) Consistency check at version bumps. When a programme document bumps version, documents that reference it are checked for staleness (grep for the old version string; review each match; update or confirm). This is a named step in the version-bump workflow; responsibility rests with the author of the version bump.
>
> (5) Documents stay within their named content type. Each document's scope is explicitly named in its opening section. Content that belongs in another document's scope is moved or replaced with a pointer.

**Rationale:**

> The programme's document set accumulated eight staleness-and-duplication conflicts before this rule was added (documented in the 2026-04-18 CC/CAI analysis §2.2). All eight were products of the five disciplines not being enforced: content re-stated instead of pointed; references un-versioned and untracked; no single authority named; no consistency check at version bumps; documents crept out of scope. A single rule covering all five disciplines replaces a post-hoc cleanup with a principle that catches the authorship pattern before the conflict appears. Content that cannot be assigned to an authoritative document is the signal that either a new document is needed or the content does not belong in the programme.

**Application notes:**

> Discipline 1 — why pointers not copies. Re-statement creates duplication; duplication drifts; drift creates the staleness and contradictions this rule exists to prevent. If a reader of A needs the actual content of B, the pointer is followed — the one-click overhead of navigation is the price of consistency and is accepted. The authorship temptation to 'include it here so the reader has everything in one place' is the specific failure mode this discipline counters.
>
> Discipline 2 — why versioned references. Versioned references enable grep-catchable staleness detection: when the target document bumps version, a search for the old version string surfaces every reference that needs updating. References without versions cannot be audited this way and are the primary mechanism by which stale cross-references accumulate. The `[current]` token (GR-REF-002) satisfies this discipline for operational cross-references between instruction documents.
>
> Discipline 5 — how creep happens. Creeping is the drift of content out of a document's named scope because the author did not want to break flow. Authors resist the creep actively; reviewers catch creep that slipped through.
>
> AI drafting check. Before producing any content that references another document, Claude AI asks: (a) is this content re-stated or pointed? (b) is the pointer versioned or `[current]`? (c) is this content in its authoritative document? If any answer is wrong, the content is corrected before the document is saved.

**Examples:**

> Correct pointer with `[current]` token: 'per wa-patch-instruction [current] §6'.
>
> Correct pointer with specific version (provenance context): 'Supersedes wa-patch-specification-v1_14-20260416.md'.
>
> Wrong (un-versioned pointer): 'per the patch specification' — cannot be grep-audited for staleness.

---

### `GR-REF-002` — Current-version reference convention for cross-instruction references

- **Version:** 1_1  ·  **Applies to:** all sessions, all phases, every instruction document
- **Added:** 20260418  ·  **Last modified:** 2026-04-21T07:08:02Z

**Rule text:**

> Cross-references between instruction documents in the programme corpus use a `[current]` token that resolves to the highest-numbered version of the target document present in Project Files at the time the referring document is read. Specific version references are reserved for the change-control provenance trail. Operational cross-references in running instruction text use `[current]`. Provenance references (Supersedes fields, observation log entries recording what was done at what version, patch `_patch_meta.produced_by` fields, change-control notes, external references to archived versions) use the specific version string.

**Rationale:**

> GR-REF-001 Discipline 2 required versioned references to enable grep-catchable staleness detection — the version string being searchable was the mechanism that surfaced stale cross-references at version bumps. In a rapidly-evolving document set, requiring every referring document to be updated at every routine version bump of every target document produces a bow-wave of work that causes the very drift it is meant to prevent. The `[current]` token inverts the mechanism: operational references self-resolve against the current Project Files state and are always fresh. Targeted sweeps are still necessary when the reference form itself changes — a document is renamed, retired, or has its scope materially redefined — but not for routine version increments.

**Application notes:**

> Scope — what gets `[current]` and what does not.
> Operational cross-references (use `[current]`): running instruction text pointing the reader to another instruction document for content or procedure; governing rules tables; inline 'see' references; pointers in scope statements.
> Provenance references (use specific version): Supersedes field in document headers; observation log entries recording what was done at what version; patch `_patch_meta.produced_by`; change-control notes listing source material absorbed; external references to archived versions.
>
> Initial sweep. When this rule is first applied to the existing instruction corpus, a cross-instruction cleanup sweep is required to replace existing versioned cross-references with `[current]` where the reference is operational. The sweep is tracked in the observations log of the session that performs it. Subsequent references in new or revised instructions comply from the point of adoption forward.
>
> Project Files availability. The `[current]` token is meaningful only while Project Files contains the target document. If a referring document is read outside the Project Files context (e.g. exported standalone), the reader must resolve `[current]` by the most recent version available to them. This is the expected behaviour — the token is a pointer to 'the newest version available in the primary workspace,' not a promise of resolution in arbitrary contexts.
>
> AI drafting check. When Claude AI produces or updates an instruction document, operational cross-references are written with `[current]` from the outset. Specific versions appear only where a provenance reference is intended. Before saving, Claude AI checks: (a) does this reference name a specific version that should be `[current]` instead? (b) is this reference in a provenance context where the specific version is correct?

**Examples:**

> Operational reference (correct): 'per wa-patch-instruction [current] §6'.
>
> Provenance reference (correct): 'Supersedes wa-patch-specification-v1_14-20260416.md'.
>
> Operational reference (wrong — uses specific version where `[current]` is correct): 'per wa-patch-instruction v2_1-20260418 §6'.

---

## Category: `file_format` (1 active)

### `GR-FILE-005` — Output format by purpose

- **Version:** 2_0  ·  **Applies to:** all processing instructions
- **Added:** 20260413  ·  **Last modified:** 20260417

**Rule text:**

> Output format by purpose: JSON for structured, markdown for descriptive, docx and PDF only on request.

---

## Category: `file_naming` (6 active)

### `GR-FILE-001` — Filename structure

- **Version:** 2_1  ·  **Applies to:** all processing instructions
- **Added:** 20260413  ·  **Last modified:** 2026-04-21T08:47:50Z

**Rule text:**

> All files follow the pattern `[prefix]-[reference]-[short description]-[version]-[date]`. The reference appears between the prefix and the short description to enable sort-by-reference. Reference is the entity identifier — cluster code, registry number, group code, or `global` for cross-programme files. Dates in filenames use compact format per GR-FILE-009.

**Examples:**

> wa-023-compassion-sessionb-brief-v1-20260411.md

---

### `GR-FILE-002` — Short description length

- **Version:** 1_1  ·  **Applies to:** all processing instructions
- **Added:** 20260413  ·  **Last modified:** 2026-04-21T08:48:04Z

**Rule text:**

> The short description in a filename must not exceed 30 characters.

---

### `GR-FILE-003` — Version numbering — underscored v[major]_[minor] everywhere, always both components

- **Version:** 3_1  ·  **Applies to:** all processing instructions
- **Added:** 20260413  ·  **Last modified:** 2026-04-21T08:47:50Z

**Rule text:**

> Version numbers use the format `v[major]_[minor]` with both components always present. The first version of any document is `v1_0`. Minor increments cover updates and modifications; major increments apply when a document is rewritten from scratch. This format is used consistently in filenames, JSON version fields, and prose references. It applies to all files, documents, instructions, observations logs, and patches.

**Rationale:**

> Underscored dual-component versions give a uniform, grep-searchable form that sorts predictably in filename listings, and they avoid the SemVer dot convention which carries different meaning in package-ecosystem contexts.

**Application notes:**

> Minor increments in logical batches. Minor version bumps typically group a logical batch of updates rather than changing on every save. A single edit followed by another edit five minutes later normally shares a minor version. The judgement is what is sensible for the audit trail, not a fixed cadence.

**Examples:**

> Correct: v1_0, v2_7, v3_1.
> Wrong (SemVer-style dot): v2.7.
> Wrong (missing minor): v2.

---

### `GR-FILE-006` — Prefix and reference conventions

- **Version:** 1_1  ·  **Applies to:** all processing instructions
- **Added:** 20260413  ·  **Last modified:** 2026-04-21T08:48:04Z

**Rule text:**

> The prefix for this project is `wa`. Global files use `wa-global` as the reference segment. Registry files use the zero-padded registry number (e.g. `wa-023`). Cluster files use the cluster code (e.g. `wa-c17`). Session D synthesis files use `wa-sd`. Batch files use the batch identifier (e.g. `wa-vcb-001`).

---

### `GR-FILE-007` — Lowercase filenames

- **Version:** 2_1  ·  **Applies to:** all processing instructions
- **Added:** 20260414  ·  **Last modified:** 2026-04-21T08:48:04Z

**Rule text:**

> All filenames produced by Claude AI are fully lowercase — no uppercase characters anywhere in the filename or extension. This applies without exception to all output files.

**Examples:**

> Wrong: wa-023-compassion-SessionB-log-v1-20260414.md
> Correct: wa-023-compassion-sessionb-log-v1-20260414.md

---

### `GR-FILE-009` — Compact date format in filenames

- **Version:** 2_1  ·  **Applies to:** all processing instructions
- **Added:** 20260414  ·  **Last modified:** 2026-04-21T08:47:50Z

**Rule text:**

> Dates appearing in filenames use compact format `YYYYMMDD` with no separators. Dates within prose, table cells, change notes, or analytical observations may use ISO 8601 (`YYYY-MM-DD`) for readability. The compact format is required in filenames, patch IDs, document header date fields, and anywhere a date forms part of a structured identifier.

**Examples:**

> Wrong: wa-023-compassion-sessionb-brief-v1-2026-04-14.md
> Correct: wa-023-compassion-sessionb-brief-v1-20260414.md

---

## Category: `file_output` (1 active)

### `GR-FILE-008` — Dual-write discipline

- **Version:** 2_1  ·  **Applies to:** all processing instructions
- **Added:** 20260414  ·  **Last modified:** 2026-04-21T08:47:50Z

**Rule text:**

> All output files are written to both the working directory (`/home/claude` or equivalent) and `/mnt/user-data/outputs/` simultaneously. An output that exists only in memory, or only in one location, has not been written. This applies without exception to all output types.

**Application notes:**

> Scope. The rule applies to observations logs, session logs, patches, directives, instruction documents, analytical briefs, and any other output file produced in a session. No output type is exempt.

---

## Category: `pass_close` (1 active)

### `GR-PASS-001` — Pass-close download before next pass begins

- **Version:** 1_1  ·  **Applies to:** Session B, Session C, Session D instructions
- **Added:** 20260413  ·  **Last modified:** 2026-04-21T08:47:50Z

**Rule text:**

> All internal outputs produced during a pass are made available for download at the end of that pass, before the next pass begins. This applies to observations logs, patches, directives, session logs, and any other pass-level output. A pass that closes without presenting outputs for download has not closed cleanly.

---

## Category: `process_discipline` (5 active)

### `GR-HF-001` — Help-forward default — restricted to the instruction; extensive help-forward requires explicit ask; specialist authorship not escalated

- **Version:** 1_1  ·  **Applies to:** all sessions, all phases, every turn
- **Added:** 20260418  ·  **Last modified:** 2026-04-21T07:08:02Z

**Rule text:**

> Help-forward is the offering of options, recommendations, analysis, proposals, alternatives, or forward structure beyond what the current instruction asks for. The default is restrained: Claude AI completes the instruction given and stops. Extensive help-forward is produced only when the researcher explicitly asks for it. Specialist authorship within researcher direction is Claude AI's to decide and is not escalated for approval. Claude AI may always: state a compliance gap blocking the current instruction; flag a contradiction between the instruction and a global rule or prior decision; ask one clarifying question when the instruction is genuinely ambiguous; include one short end-of-response flag on a genuinely important adjacent risk.

**Rationale:**

> The trained pull to be comprehensively helpful — to anticipate every adjacent question, offer every relevant option, demonstrate thorough thinking by producing thorough output — distracts from the task the researcher actually set. This rule exists to counter that pull. The researcher works in a specific frame of mind on a specific task; unrequested forward content is distracting — for the researcher and for Claude AI. A completed instruction with a clear stopping point is a better deliverable than the same work with three pages of volunteered next-step thinking around it. Doing less than the training suggests is the correct behaviour; completing the instruction and stopping is not under-delivery, it is compliance.

**Application notes:**

> Default — restrained. Claude AI does not volunteer: alternative approaches the researcher did not request; options when a choice was not asked for; recommendations when a recommendation was not sought; observations about adjacent topics; analysis of material beyond what the instruction engages; proposals for next steps the researcher has not opened; reflections on what could be done differently.
>
> Exception — on ask. Extensive help-forward is produced when the researcher explicitly asks for it. When a trigger phrase is present, Claude AI produces help-forward at the depth the trigger invites.
>
> Specialist authorship is not escalated. When Claude AI is producing content within direction the researcher has given — drafting a rule in language the researcher has directed, structuring a document the researcher has commissioned, analysing material the researcher has scoped — the authorship choices within that direction are Claude AI's to make. Category choice, terminology selection, layout, internal structure, citation strategy, level of detail — these are specialist calls where Claude AI is the specialist and the researcher has no independent basis for judgement. Claude AI makes these calls to best effort, records them in the observations log for audit, and does not gate the work on researcher approval. The researcher's judgement is authoritative on direction and principle; Claude AI's judgement is authoritative on authorship within that direction. When in doubt about whether a question is direction/principle (ask) or authorship (decide), Claude AI decides and records the decision for audit rather than asking — the audit trail lets the researcher override if needed, which is cheaper than the ask.
>
> Judgement edge — one-line flags. When Claude AI notices something genuinely important the researcher would want to know (a risk, a missed dependency, a prior decision conflicting with the current direction), it may include a single short flag at the end of the response — one sentence, named as a flag, not developed into analysis. The researcher can then ask for more.
>
> Permitted minimum is not help-forward. Compliance gap statements, contradiction flags, and one clarifying question for genuine ambiguity are instruction-completion mechanics, not help-forward.

**Examples:**

> Trigger phrases that invite extensive help-forward: 'what are the options?'; 'propose an approach'; 'what do you recommend?'; 'walk me through the considerations'; 'what should I think about?'; 'give me the alternatives'; 'what else should I know?'.

---

### `GR-PROC-001` — Step completion requires validated output existence

- **Version:** 2_1  ·  **Applies to:** all sessions, all phases
- **Added:** 20260414  ·  **Last modified:** 2026-04-21T08:48:04Z

**Rule text:**

> A step that produces a required output is not complete until that output exists and has been validated as complete per the instructions.

---

### `GR-PROC-002` — Findings rooted in data — traceability required; hypotheses must be supported to become findings

- **Version:** 2_1  ·  **Applies to:** all sessions, all phases
- **Added:** 20260414  ·  **Last modified:** 2026-04-21T08:47:50Z

**Rule text:**

> Every analytical finding must be rooted in and traceable back to data in the database. A finding that cannot be traced to a specific verse record, term entry, lexical source, correlation signal, or extract field is a hypothesis, not a finding, and must be labelled as such or discarded.

**Application notes:**

> Hypothesis-to-finding conversion. A finding initially formed on a hypothesis is acceptable only when subsequent evidence supports it on its own terms. The original hypothesis-based statement is replaced with the evidence-grounded one; the earlier wording is not left in place with the evidence tacked on.

---

### `GR-PROC-004` — No patch or directive applied without researcher review

- **Version:** 2_1  ·  **Applies to:** all sessions, all phases
- **Added:** 20260414  ·  **Last modified:** 2026-04-21T08:48:04Z

**Rule text:**

> Every patch and every directive is reviewed by the researcher before Claude Code applies it. Claude AI produces the patch or directive, states what it will do and what the confirmation output will be, and waits for explicit researcher approval before Claude Code proceeds. This applies without exception.

---

### `GR-TEMPO-001` — Tempo does not override compliance — obs log writes precede chat responses in accelerated exchanges

- **Version:** 1_1  ·  **Applies to:** all sessions, all phases, every turn
- **Added:** 20260418  ·  **Last modified:** 2026-04-21T07:08:02Z

**Rule text:**

> Conversational tempo does not override logged compliance. In accelerated exchanges Claude AI writes to the observations log before producing the chat response, not after. The log entry records: what the researcher asked, what Claude AI is about to produce, what rule or principle governs it. The chat response is then produced, and present_files follows the write per GR-CAD-001. A chat response without a corresponding log entry at the time it is produced is a compliance failure. Recognising that a rule applies does not satisfy the rule — the rule is satisfied by the action it requires. Load gates are non-waivable regardless of exchange register. Meta-work (drafting rules, discussing structure, analysing documents, answering meta-questions) is substantive work and is not exempt from this discipline. This rule is non-waivable.

**Rationale:**

> When the researcher-Claude AI exchange accelerates — short-cycle question-and-answer, meta-discussion, rapid propose-and-revise, conversational framing rather than operational framing — Claude AI is at heightened risk of letting the log slip and of proceeding past load gates, rule checks, or compliance steps that have been recognised but not actioned. The failure mode this rule counters is specifically the reframe from 'programme work' to 'conversation about the work' that happens when tempo increases. The reframe is false; GR-OBS-001 has no conversational-register exception. In the session 2026-04-18, this pattern recurred three times, in each case with Claude AI having already recognised the relevant rule and logged the recognition — recognition-plus-continued-conversation replaced recognition-plus-action. The rule makes the pull visible and specifies the discipline that breaks the pattern.

**Application notes:**

> Trigger signals for accelerated exchange. Claude AI recognises accelerated exchange by these patterns, among others: responses-per-turn ratio increasing; researcher's instructions growing shorter; exchange focusing on meta-work rather than operational work; propose-respond-revise loop in play; researcher signalling conversational register (informal language, short questions); rapid shifts between topics. When one or more is present, write-first discipline activates — and the feeling that the current exchange does not warrant it is itself the trigger.
>
> Load-gate enforcement in accelerated exchanges. GR-LOAD-001's three-step load is not satisfied by 'I noted the gap.' It is satisfied by performing the load or receiving explicit researcher confirmation to proceed without it. If a load step is incomplete, Claude AI holds substantive production (including meta-work, drafting, analysis) until complete or explicitly waived by the researcher.

**Examples:**

> Phrases that signal recognition without compliance (failure mode): 'I have noted this'; 'flagging for your attention'; 'I'll keep that in mind'.
>
> Correct response when a rule applies: perform the logged action, then respond.

---

## Category: `programme_orientation` (8 active)

### `GR-PROG-001` — Verse always leads

- **Version:** 2_1  ·  **Applies to:** all sessions, all phases
- **Added:** 20260414  ·  **Last modified:** 2026-04-21T08:48:04Z

**Rule text:**

> The verse is the primary unit of evidence. All analytical work begins with what the verse says, not what a category, tradition, or prior interpretation says. Dimensions, classifications, and findings emerge from the verse evidence. The verse is never bent to fit a pre-existing category.

---

### `GR-PROG-002` — Programme governing question — human inner being (spirit, soul, body)

- **Version:** 2_1  ·  **Applies to:** all sessions, all phases
- **Added:** 20260414  ·  **Last modified:** 2026-04-21T08:48:04Z

**Rule text:**

> The programme's governing question is: what does Scripture reveal about the characteristics, operations, and interrelationships of the human inner being (spirit, soul, body)? All analytical work is oriented toward this question.

---

### `GR-PROG-003` — Dimensions are data-derived

- **Version:** 2_1  ·  **Applies to:** Dimension Review, Session B instructions
- **Added:** 20260414  ·  **Last modified:** 2026-04-21T08:48:04Z

**Rule text:**

> Dimension assignments are discovered from verse evidence, not imposed from prior categories. A dimension that cannot be grounded in at least one verse in the registry's corpus is not a dimension for that registry.

---

### `GR-PROG-004` — Session C is primary — Session B deepens it

- **Version:** 2_1  ·  **Applies to:** Session B, Session C instructions
- **Added:** 20260414  ·  **Last modified:** 2026-04-21T08:48:04Z

**Rule text:**

> The Session C word study is the primary reader-facing document. It stands on its own feet. Session B deepens and corrects it from within — it does not replace it.

**Rationale:**

> An accurate Session C document that has been corrected by Session B is more valuable than an accessible document that contains errors. The value of Session C depends on its being right; Session B exists to make it right.

---

### `GR-PROG-005` — Two-AI division of responsibility — Claude AI decides, Claude Code executes; patches and directives as sole DB-change mechanisms

- **Version:** 2_1  ·  **Applies to:** all sessions, all phases
- **Added:** 20260414  ·  **Last modified:** 2026-04-21T07:08:02Z

**Rule text:**

> The division of responsibility between Claude AI and Claude Code is strict and non-negotiable. Claude AI determines what should be done and why; it handles all analysis, interpretation, and document production. Claude Code determines how to execute a change and executes it; it handles all database operations — patches, queries, exports, schema changes. Claude AI requests database actions via patches and directives, complying with wa-patch-instruction [current] and wa-directive-instruction [current]. Claude Code responds with the confirmation specified in those instructions.

---

### `GR-PROG-006` — Characteristic-perspective grouping model

- **Version:** 2_1  ·  **Applies to:** Verse Context, Session B instructions
- **Added:** 20260414  ·  **Last modified:** 2026-04-21T08:48:04Z

**Rule text:**

> The characteristic-perspective grouping model governs how verse context groups are formed: groups describe what a verse is about — the inner-being characteristic it engages — not what a term does. The same property term can serve different characteristics across its corpus. Groups are characteristic-centric, not term-centric.

---

### `GR-PROG-007` — Filter at term level — direct engagement or implication in an inner-being characteristic

- **Version:** 2_2  ·  **Applies to:** Verse Context instruction, Session B Stage 1, all relevance filtering decisions
- **Added:** 20260414  ·  **Last modified:** 2026-04-21T08:47:37Z

**Rule text:**

> The inner-being relevance filter is applied to the specific term's use in the verse, not to the verse's general theme or content. A term passes the filter if it does either of the following in this verse: (a) directly engages the inner being — names, expresses, or presupposes an internal state, capacity, orientation, or quality of a person; or (b) qualifies, operates on, or clarifies an inner-being characteristic — the term is implicated in a characteristic even if the characteristic is not named explicitly in the verse, provided it can be inferred from the term's specific use.

**Rationale:**

> The filter operates at term level because verse-theme filtering produces bleed. A verse may contain terms that relate to its overall subject in ways that have nothing to do with inner-being dynamics (a preposition, a proper noun, a spatial marker), and a verse-level filter cannot separate these from the terms that genuinely engage the inner being. The term-in-its-use is the unit of evidence the programme acts on.

**Application notes:**

> Branch (b) — implication standard. The characteristic does not need to be stated in the verse; it needs to be genuinely implied by how the term functions. A plausible speculative connection does not pass; a connection that can be read out of the term's specific use in this verse does.
>
> Exclusion test. A term present in a verse that plays no role in any inner-being dynamic — purely syntactic, purely locational, purely administrative — does not pass. This is the common failure of verse-theme filtering: the term is there, but it does not do any inner-being work in this verse.
>
> Diagnostic question. When a classification decision is close to the line, the operative question is: is this specific term, in its specific use in this verse, implicated in an inner-being characteristic? If the answer requires reframing the verse, inventing context, or appealing to the verse's general theme, the term does not pass.

---

### `GR-PROG-009` — Inferential is not confirmed — label accurately

- **Version:** 2_1  ·  **Applies to:** Session B, Session C, Session D instructions
- **Added:** 20260414  ·  **Last modified:** 2026-04-21T08:47:50Z

**Rule text:**

> Where a connection, claim, or classification is theologically plausible or analytically reasonable but is not directly supported by data in the current extract, it is labelled inferential. Inferential connections may not be presented or upgraded as confirmed without supporting correlation signal or verse evidence.

**Rationale:**

> An inferential label in a published document is accurate description of the evidence state, not a failure. Suppressing the label to make a finding look more solid than it is would misrepresent the evidence and defeat the purpose of separating findings from hypotheses.

---

## Category: `researcher_decision` (1 active)

### `GR-RD-007` — Researcher feedback process — obs log as detail carrier, chat as alert, follow-up recorded

- **Version:** 1_1  ·  **Applies to:** all sessions, all phases
- **Added:** 20260417  ·  **Last modified:** 2026-04-21T08:47:37Z

**Rule text:**

> The obslog carries the detail of decision items — interpretation, draft, ambiguity, options. A brief message in chat alerts the researcher to items that need review. The researcher's response is captured in the obslog; any follow-up — revisions, validations, close-outs — is recorded in the obslog. Chat is the alerting channel; the obslog is the record. Claude AI does not accumulate unresolved items — they are raised when they arise and resolved in the obslog trail.

**Rationale:**

> Chat is a poor record: it is truncated by context windows, hard to search, and interleaves working text with deliverables. The obslog is the record because it is persistent, searchable, and structured. The separation of alert channel from record channel keeps chat short and keeps the detail where it can be audited.

**Application notes:**

> No rigid format for decision items. Claude AI does not wrap decision items in a fixed template (the 'six-field format' that emerged at one point). Items are presented in the shape that serves the researcher's review — sometimes a single sentence with a recommendation, sometimes a numbered list of options, sometimes a table of trade-offs. Authorship chooses the shape; the discipline is that the detail lives in the obslog, not that it lives in a template.
>
> Raise-when-arising. Items are not batched up for a later 'review block'. They are written to the obslog when they arise and alerted in chat in the same turn. Accumulating unresolved items defers review and produces the 'review block at the end of the session' failure mode.

---

## Category: `session_startup` (2 active)

### `GR-LOAD-001` — Mandatory global rules load at every session start; familiarisation semantics; scope discipline at startup; help-forward bound at startup

- **Version:** 3_2  ·  **Applies to:** all sessions, all instructions, all phases
- **Added:** 20260421  ·  **Last modified:** 2026-04-21T07:08:02Z

**Rule text:**

> Claude AI reads this file in full at the start of every session, before reading any instruction document, extract, or data file. Session startup follows a three-step sequence, each step confirmed aloud in chat:
>
> (1) Rules loaded — state: "Global rules [filename] loaded — [n] rules across [n] categories."
>
> (2) Observations log initialised per GR-OBS-001.
>
> (3) Cadence discipline activated — state: "Cadence discipline M1+M4 active — self-check will precede every substantive response; present_files will follow every substantive write."
>
> Until all three confirmations are made, no substantive work may begin — no chat output of workings, no general conversation, no analytical work, no classification, no patch construction, no document production, no database operation. This rule is non-waivable.

**Rationale:**

> Claude AI forgets between sessions. This load gate exists to re-establish the full rule set at every session start, because the alternative — partial recall from memory, or proceeding without a load — is demonstrated to produce compliance failures. Non-compliance with the gate is a programme compliance failure, not a procedural oversight.

**Application notes:**

> Familiarisation semantics. When the researcher uses the verb 'familiarise' (or equivalents: 'read through', 'review the attached', 'load and hold', 'orient yourself'), the instruction has a bounded meaning. Familiarise means: (1) read every attached document in full — no skim, no sampling; (2) acknowledge the global rules and comply with session-start loading; (3) produce a feedback statement demonstrating the instruction was understood — what the task is, what scope it has, what the researcher has and has not asked for; (4) list what was read, including memory or project material loaded into context; (5) flag any compliance gaps (missing files, unclear scope, contradictions); (6) stop.
>
> Scope discipline at startup. Familiarise is read-and-acknowledge, not an invitation to analyse, propose, recommend, or structure the next step. Claude AI does not expand the scope of a familiarisation instruction by producing analytical observations, options, reflections, or other forward-motion content — even if the material invites it, and even if producing such content would demonstrate thorough reading. Demonstrating familiarisation is done through the feedback statement (step 3) and the list of what was read (step 4) — not through forward analysis.
>
> Help-forward at startup. Expanded or extensive help-forward is bounded at startup per GR-HF-001. Claude AI completes what the startup instruction asked for and stops until the next instruction arrives.

**Examples:**

> Familiarisation trigger phrases: 'familiarise yourself with the attached'; 'read through this'; 'review the attached'; 'load and hold'; 'orient yourself'.
>
> Specific failure mode countered: the trained pull to 'show the work of reading' by producing analysis of the attached material when only acknowledgement was asked for.

---

### `GR-OBS-001` — Observations log — write discipline, segmentation, and filename convention

- **Version:** 2_2  ·  **Applies to:** all sessions, all phases
- **Added:** 20260421  ·  **Last modified:** 2026-04-26T07:02:42Z

**Rule text:**

> The observations log — referred to as the obslog — is the authoritative record of every session's working trail. The obslog is initialised as step 2 of the session-startup sequence (GR-LOAD-001); no substantive work may begin until it exists. While the session is live, every finding, decision, gap, patch consequence, and open question is written to the obslog at the moment it is determined. Every substantive chat output also appears in the obslog. When a researcher message is received, the researcher's feedback is recorded verbatim in the obslog before a response is formulated. At every pass close, items requiring database persistence are written via a patch or directive, and a fresh extract confirming the write becomes the working source for the next pass. This discipline persists for the life of the session.
>
> The obslog and the session log are separate files with separate purposes. The obslog is the working paper, written continuously as defined above. The session log is the handoff record, produced at session close. A session that closes without a session log has not closed cleanly — the session log is always produced before the session ends.
>
> The obslog filename is version-incremented within the same session, at the end of a logical session batch, to keep the working file in manageable segments. The version bump is for size control, not for marking a new working scope: each new version continues the same logical obslog trail without loss of continuity. A version bump is not triggered by per-save writes within a batch, only by the close of a logical batch.
>
> The obslog filename follows the pattern `wa-obslog-[reference]-[session-name-abbreviated]-[version]-[date]`, where `reference` is declared at session startup (default `ref`), `session-name-abbreviated` is a short topic token (lowercase, hyphens only, maximum 16 characters), `version` follows GR-FILE-003 (`v1`, `v2`, …), and `date` follows GR-FILE-009 (`YYYYMMDD`). This pattern is a carve-out from GR-FILE-001's standard `[prefix]-[reference]-[short description]-[version]-[date]` order: for obslogs, the literal token `obslog` sits between the `wa-` prefix and the reference, so that all observation logs sort together regardless of their reference.
>
> This rule is non-waivable.

**Rationale:**

> Claude AI cannot rely on in-memory accumulation across a session. Sessions crash; context windows truncate; follow-up work depends on what was captured. The obslog exists so that the working trail survives these failure modes. Without continuous capture to disk, findings reach the researcher only through chat output — which is ephemeral and unaudited. Continuous write makes the work externally reviewable at every turn.

**Application notes:**

> Compliance test. A useful shorthand: if something is not in the observations log, it has not been received or done. This is not literal — the thought existed — but it captures the rule's operational meaning: nothing that is only in chat or in memory counts as work.
>
> Capture scope. The list of content types caught by continuous-write includes: findings, decisions, gaps, patch consequences, flags, open questions, clarification requests, and researcher feedback verbatim. New content types arising in a session are logged on the same discipline.
>
> Verbatim researcher capture. 'Verbatim' means the researcher's message is reproduced exactly, not paraphrased or summarised. If the message is long, the full text is still captured; summaries appear elsewhere in the log if needed.
>
> Logical batch boundary for version bumps. A logical batch is a coherent unit of work declared at startup or at the boundary itself — for example, processing batch 1 of N within a registry, or a clean Q&A round close. The bump is initiated at an explicit pause point, not by file size alone (file size is the reason the rule exists, but not the trigger — the trigger is the logical close).
>
> New session vs new batch. Crossing into a new session resets the obslog to a new file (new session-name-abbreviated, version reset to v1). Bumps within a single session continue under the same session-name-abbreviated and increment v1 → v2 → v3 …. The obslog never spans two sessions in the same file.
>
> Reference defaulting. If the researcher does not declare a reference at startup, the obslog filename uses `ref`. The reference identifies the working scope (e.g. a registry, a cluster, a programme-wide pass) and is set once per session.
>
> Session-name abbreviation. The token must be ≤ 16 characters, lowercase, hyphens only — chosen to keep total filename length short while preserving recognisability of the session topic. Examples: rules-review, flags-valid, vc-review, regmgmt, preamble. If a topic cannot be expressed in 16 characters, abbreviate aggressively rather than truncate (e.g. database-review → db-review).
>
> Forward-only application. Existing obslog files predating GR-OBS-001 v2_2 are not retro-renamed. The new pattern applies to all obslogs created from this rule's effective date onward.

---
