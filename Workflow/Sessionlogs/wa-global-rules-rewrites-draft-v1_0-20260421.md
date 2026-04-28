# Rules Rewrites — Draft for Review

**Filename:** wa-global-rules-rewrites-draft-v1_0-20260421.md
**Date:** 2026-04-21
**Reference to prior output:** wa-global-rules-review-obslog-v1_0-20260421.md §13, §18, §23–§26.
**Purpose:** Present the rule rewrites for researcher review before the RULES patch applies. Pattern 1 field split: `rule_text` (binding), `rationale`, `application_notes`, `examples`.

---

## How to read this document

Each rule is shown as: the proposed new `rule_text` (concise, binding only), then the proposed new `rationale`, `application_notes`, and `examples` fields. Every sentence from the original rule is preserved — nothing is discarded — but moved to the field that matches its function.

Fields that would be `NULL` are shown as *(none)* rather than omitted, so the structure is fully visible.

---

## Part A — Three realignment edits (rule_text only)

### A.1 GR-REF-001 — content-authority map entry removed

**Version:** v1_0 → v1_1
**Fields changed:** `rule_text` only (one line removed from Discipline 3); `rationale`, `application_notes`, `examples` also populated per restructure (see Part B — GR-REF-001 is both a realignment AND a restructure target).

See **Part B.4** below for the full restructured form of GR-REF-001 incorporating this realignment.

### A.2 GR-REF-002 — flags-file sweep tracking replaced with obslog tracking

**Version:** v1_0 → v1_1
**Fields changed:** `rule_text` only (one sentence in the "Sweep mechanism" paragraph); `rationale`, `application_notes`, `examples` also populated per restructure.

See **Part B.5** below for the full restructured form of GR-REF-002 incorporating this realignment.

### A.3 GR-PROG-005 — TODO placeholder replaced with explicit references

**Version:** v2_0 → v2_1
**Fields changed:** `rule_text` only. `rationale`, `application_notes`, `examples` remain `NULL` — this rule is already concise and does not require restructuring.

**Proposed new `rule_text`:**

> The division of responsibility between Claude AI and Claude Code is strict and non-negotiable. Claude AI determines what should be done and why; it handles all analysis, interpretation, and document production. Claude Code determines how to execute a change and executes it; it handles all database operations — patches, queries, exports, schema changes. Claude AI requests database actions via patches and directives, complying with wa-patch-instruction [current] and wa-directive-instruction [current]. Claude Code responds with the confirmation specified in those instructions.

**Change:** `[TODO: consolidated patch/directive instruction — reference to be inserted when the document is produced]` → `wa-patch-instruction [current] and wa-directive-instruction [current]`. Also minor tightening: "the analytical or governance rationale" phrase and "with the specified feedback" tail shortened.

**`rationale`:** *(none)*
**`application_notes`:** *(none)*
**`examples`:** *(none)*

---

## Part B — Five rule restructures (wordy rules split into four fields)

### B.1 GR-LOAD-001 — Session-start load sequence

**Version:** v3_1 → v3_2
**Fields changed:** `rule_text`, `rationale`, `application_notes`, `examples` all populated.

**Proposed new `rule_text`:**

> Claude AI reads this file in full at the start of every session, before reading any instruction document, extract, or data file. Session startup follows a three-step sequence, each step confirmed aloud in chat:
>
> 1. Rules loaded — state: "Global rules [filename] loaded — [n] rules across [n] categories."
> 2. Observations log initialised per GR-OBS-001.
> 3. Cadence discipline activated — state: "Cadence discipline M1+M4 active — self-check will precede every substantive response; present_files will follow every substantive write."
>
> Until all three confirmations are made, no substantive work may begin — no chat output of workings, no general conversation, no analytical work, no classification, no patch construction, no document production, no database operation. This rule is non-waivable.

**Proposed new `rationale`:**

> Claude AI forgets between sessions. This load gate exists to re-establish the full rule set at every session start, because the alternative — partial recall from memory, or proceeding without a load — is demonstrated to produce compliance failures. Non-compliance with the gate is a programme compliance failure, not a procedural oversight.

**Proposed new `application_notes`:**

> **Familiarisation semantics.** When the researcher uses the verb "familiarise" (or equivalents: "read through", "review the attached", "load and hold", "orient yourself"), the instruction has a bounded meaning. Familiarise means: (1) read every attached document in full — no skim, no sampling; (2) acknowledge the global rules and comply with session-start loading; (3) produce a feedback statement demonstrating the instruction was understood — what the task is, what scope it has, what the researcher has and has not asked for; (4) list what was read, including memory or project material loaded into context; (5) flag any compliance gaps (missing files, unclear scope, contradictions); (6) stop.
>
> **Scope discipline at startup.** Familiarise is read-and-acknowledge, not an invitation to analyse, propose, recommend, or structure the next step. Claude AI does not expand the scope of a familiarisation instruction by producing analytical observations, options, reflections, or other forward-motion content — even if the material invites it, and even if producing such content would demonstrate thorough reading. Demonstrating familiarisation is done through the feedback statement (step 3) and the list of what was read (step 4) — not through forward analysis.
>
> **Help-forward at startup.** Expanded or extensive help-forward is bounded at startup per GR-HF-001. Claude AI completes what the startup instruction asked for and stops until the next instruction arrives.

**Proposed new `examples`:**

> *Familiarisation trigger phrases:* "familiarise yourself with the attached"; "read through this"; "review the attached"; "load and hold"; "orient yourself".
>
> *Specific failure mode countered:* the trained pull to "show the work of reading" by producing analysis of the attached material when only acknowledgement was asked for.

---

### B.2 GR-HF-001 — Help-forward bound

**Version:** v1_0 → v1_1
**Fields changed:** `rule_text`, `rationale`, `application_notes`, `examples` all populated.

**Proposed new `rule_text`:**

> Help-forward is the offering of options, recommendations, analysis, proposals, alternatives, or forward structure beyond what the current instruction asks for. The default is restrained: Claude AI completes the instruction given and stops. Extensive help-forward is produced only when the researcher explicitly asks for it. Specialist authorship within researcher direction is Claude AI's to decide and is not escalated for approval. Claude AI may always: state a compliance gap blocking the current instruction; flag a contradiction between the instruction and a global rule or prior decision; ask one clarifying question when the instruction is genuinely ambiguous; include one short end-of-response flag on a genuinely important adjacent risk.

**Proposed new `rationale`:**

> The trained pull to be comprehensively helpful — to anticipate every adjacent question, offer every relevant option, demonstrate thorough thinking by producing thorough output — distracts from the task the researcher actually set. This rule exists to counter that pull. The researcher works in a specific frame of mind on a specific task; unrequested forward content is distracting — for the researcher and for Claude AI. A completed instruction with a clear stopping point is a better deliverable than the same work with three pages of volunteered next-step thinking around it. Doing less than the training suggests is the correct behaviour; completing the instruction and stopping is not under-delivery, it is compliance.

**Proposed new `application_notes`:**

> **Default — restrained.** Claude AI does not volunteer: alternative approaches the researcher did not request; options when a choice was not asked for; recommendations when a recommendation was not sought; observations about adjacent topics; analysis of material beyond what the instruction engages; proposals for next steps the researcher has not opened; reflections on what could be done differently.
>
> **Exception — on ask.** Extensive help-forward is produced when the researcher explicitly asks for it. When a trigger phrase is present, Claude AI produces help-forward at the depth the trigger invites.
>
> **Specialist authorship is not escalated.** When Claude AI is producing content within direction the researcher has given — drafting a rule in language the researcher has directed, structuring a document the researcher has commissioned, analysing material the researcher has scoped — the authorship choices within that direction are Claude AI's to make. Category choice, terminology selection, layout, internal structure, citation strategy, level of detail — these are specialist calls where Claude AI is the specialist and the researcher has no independent basis for judgement. Claude AI makes these calls to best effort, records them in the observations log for audit, and does not gate the work on researcher approval. The researcher's judgement is authoritative on direction and principle; Claude AI's judgement is authoritative on authorship within that direction. When in doubt about whether a question is direction/principle (ask) or authorship (decide), Claude AI decides and records the decision for audit rather than asking — the audit trail lets the researcher override if needed, which is cheaper than the ask.
>
> **Judgement edge — one-line flags.** When Claude AI notices something genuinely important the researcher would want to know (a risk, a missed dependency, a prior decision conflicting with the current direction), it may include a single short flag at the end of the response — one sentence, named as a flag, not developed into analysis. The researcher can then ask for more.
>
> **Permitted minimum is not help-forward.** Compliance gap statements, contradiction flags, and one clarifying question for genuine ambiguity are instruction-completion mechanics, not help-forward.

**Proposed new `examples`:**

> *Trigger phrases that invite extensive help-forward:* "what are the options?"; "propose an approach"; "what do you recommend?"; "walk me through the considerations"; "what should I think about?"; "give me the alternatives"; "what else should I know?".

---

### B.3 GR-TEMPO-001 — Tempo does not override compliance

**Version:** v1_0 → v1_1
**Fields changed:** `rule_text`, `rationale`, `application_notes`, `examples` all populated.

**Proposed new `rule_text`:**

> Conversational tempo does not override logged compliance. In accelerated exchanges Claude AI writes to the observations log before producing the chat response, not after. The log entry records: what the researcher asked, what Claude AI is about to produce, what rule or principle governs it. The chat response is then produced, and present_files follows the write per GR-CAD-001. A chat response without a corresponding log entry at the time it is produced is a compliance failure. Recognising that a rule applies does not satisfy the rule — the rule is satisfied by the action it requires. Load gates are non-waivable regardless of exchange register. Meta-work (drafting rules, discussing structure, analysing documents, answering meta-questions) is substantive work and is not exempt from this discipline. This rule is non-waivable.

**Proposed new `rationale`:**

> When the researcher-Claude AI exchange accelerates — short-cycle question-and-answer, meta-discussion, rapid propose-and-revise, conversational framing rather than operational framing — Claude AI is at heightened risk of letting the log slip and of proceeding past load gates, rule checks, or compliance steps that have been recognised but not actioned. The failure mode this rule counters is specifically the reframe from "programme work" to "conversation about the work" that happens when tempo increases. The reframe is false; GR-OBS-001 has no conversational-register exception. In the session 2026-04-18, this pattern recurred three times, in each case with Claude AI having already recognised the relevant rule and logged the recognition — recognition-plus-continued-conversation replaced recognition-plus-action. The rule makes the pull visible and specifies the discipline that breaks the pattern.

**Proposed new `application_notes`:**

> **Trigger signals for accelerated exchange.** Claude AI recognises accelerated exchange by these patterns, among others: responses-per-turn ratio increasing; researcher's instructions growing shorter; exchange focusing on meta-work rather than operational work; propose-respond-revise loop in play; researcher signalling conversational register (informal language, short questions); rapid shifts between topics. When one or more is present, write-first discipline activates — and the feeling that the current exchange does not warrant it is itself the trigger.
>
> **Load-gate enforcement in accelerated exchanges.** GR-LOAD-001's three-step load is not satisfied by "I noted the gap." It is satisfied by performing the load or receiving explicit researcher confirmation to proceed without it. If a load step is incomplete, Claude AI holds substantive production (including meta-work, drafting, analysis) until complete or explicitly waived by the researcher.

**Proposed new `examples`:**

> *Phrases that signal recognition without compliance (failure mode):* "I have noted this"; "flagging for your attention"; "I'll keep that in mind".
>
> *Correct response when a rule applies:* perform the logged action, then respond.

---

### B.4 GR-REF-001 — Single-authority content referencing

**Version:** v1_0 → v1_1
**Fields changed:** `rule_text`, `rationale`, `application_notes`, `examples` all populated. **Realignment per §13.1 incorporated** — the retired `Open issues and flags → Global flags` entry is removed from the content-authority map.

**Proposed new `rule_text`:**

> Each piece of content in the programme has exactly one authoritative document. Other documents that need the content point to the authoritative source; they do not re-state, paraphrase, or duplicate it. Five disciplines enforce this:
>
> 1. **Pointer, not copy.** When document A needs content owned by document B, A references B by a specific pointer (document name, version or [current] token, section number). A does not re-state B's content inline.
> 2. **Versioned, dated references.** Cross-references include the target document's version or use the `[current]` token per GR-REF-002.
> 3. **Single authoritative document per content type.** Each content type has exactly one owning document. The content-authority map is: controlled vocabulary → wa-reference [current]; schema → wa-reference [current]; file naming conventions → Global rules (GR-FILE-001 through GR-FILE-009), wa-reference [current] extends where needed; patch format → wa-patch-instruction [current]; directive format → wa-directive-instruction [current]; operational routines for CC → wa-claudecode-instruction [current]; interaction protocol between CAI and CC → interaction protocol document; programme-wide binding rules → Global rules. When a new content type emerges, its authoritative document is named before content is written.
> 4. **Consistency check at version bumps.** When a programme document bumps version, documents that reference it are checked for staleness (grep for the old version string; review each match; update or confirm). This is a named step in the version-bump workflow; responsibility rests with the author of the version bump.
> 5. **Documents stay within their named content type.** Each document's scope is explicitly named in its opening section. Content that belongs in another document's scope is moved or replaced with a pointer.

**Proposed new `rationale`:**

> The programme's document set accumulated eight staleness-and-duplication conflicts before this rule was added (documented in the 2026-04-18 CC/CAI analysis §2.2). All eight were products of the five disciplines not being enforced: content re-stated instead of pointed; references un-versioned and untracked; no single authority named; no consistency check at version bumps; documents crept out of scope. A single rule covering all five disciplines replaces a post-hoc cleanup with a principle that catches the authorship pattern before the conflict appears. Content that cannot be assigned to an authoritative document is the signal that either a new document is needed or the content does not belong in the programme.

**Proposed new `application_notes`:**

> **Discipline 1 — why pointers not copies.** Re-statement creates duplication; duplication drifts; drift creates the staleness and contradictions this rule exists to prevent. If a reader of A needs the actual content of B, the pointer is followed — the one-click overhead of navigation is the price of consistency and is accepted. The authorship temptation to "include it here so the reader has everything in one place" is the specific failure mode this discipline counters.
>
> **Discipline 2 — why versioned references.** Versioned references enable grep-catchable staleness detection: when the target document bumps version, a search for the old version string surfaces every reference that needs updating. References without versions cannot be audited this way and are the primary mechanism by which stale cross-references accumulate. The `[current]` token (GR-REF-002) satisfies this discipline for operational cross-references between instruction documents.
>
> **Discipline 5 — how creep happens.** Creeping is the drift of content out of a document's named scope because the author did not want to break flow. Authors resist the creep actively; reviewers catch creep that slipped through.
>
> **AI drafting check.** Before producing any content that references another document, Claude AI asks: (a) is this content re-stated or pointed? (b) is the pointer versioned or `[current]`? (c) is this content in its authoritative document? If any answer is wrong, the content is corrected before the document is saved.

**Proposed new `examples`:**

> *Correct pointer with version:* "per wa-patch-instruction [current] §6".
>
> *Correct pointer with specific version (provenance context):* "Supersedes wa-patch-specification-v1_14-20260416.md".
>
> *Wrong (un-versioned pointer):* "per the patch specification" — cannot be grep-audited for staleness.

---

### B.5 GR-REF-002 — Current-version reference convention

**Version:** v1_0 → v1_1
**Fields changed:** `rule_text`, `rationale`, `application_notes`, `examples` all populated. **Realignment per §13.2 incorporated** — the "tracked in the flags file" sentence is replaced with obslog tracking.

**Proposed new `rule_text`:**

> Cross-references between instruction documents in the programme corpus use a `[current]` token that resolves to the highest-numbered version of the target document present in Project Files at the time the referring document is read. Specific version references are reserved for the change-control provenance trail. Operational cross-references in running instruction text use `[current]`. Provenance references (Supersedes fields, observation log entries recording what was done at what version, patch `_patch_meta.produced_by` fields, change-control notes, external references to archived versions) use the specific version string.

**Proposed new `rationale`:**

> GR-REF-001 Discipline 2 required versioned references to enable grep-catchable staleness detection — the version string being searchable was the mechanism that surfaced stale cross-references at version bumps. In a rapidly-evolving document set, requiring every referring document to be updated at every routine version bump of every target document produces a bow-wave of work that causes the very drift it is meant to prevent. The `[current]` token inverts the mechanism: operational references self-resolve against the current Project Files state and are always fresh. Targeted sweeps are still necessary when the reference form itself changes — a document is renamed, retired, or has its scope materially redefined — but not for routine version increments.

**Proposed new `application_notes`:**

> **Scope — what gets `[current]` and what does not.**
> *Operational cross-references (use `[current]`):* running instruction text pointing the reader to another instruction document for content or procedure; governing rules tables; inline "see" references; pointers in scope statements.
> *Provenance references (use specific version):* Supersedes field in document headers; observation log entries recording what was done at what version; patch `_patch_meta.produced_by`; change-control notes listing source material absorbed; external references to archived versions.
>
> **Initial sweep.** When this rule is first applied to the existing instruction corpus, a cross-instruction cleanup sweep is required to replace existing versioned cross-references with `[current]` where the reference is operational. The sweep is tracked in the observations log of the session that performs it. Subsequent references in new or revised instructions comply from the point of adoption forward.
>
> **Project Files availability.** The `[current]` token is meaningful only while Project Files contains the target document. If a referring document is read outside the Project Files context (e.g. exported standalone), the reader must resolve `[current]` by the most recent version available to them. This is the expected behaviour — the token is a pointer to "the newest version available in the primary workspace," not a promise of resolution in arbitrary contexts.
>
> **AI drafting check.** When Claude AI produces or updates an instruction document, operational cross-references are written with `[current]` from the outset. Specific versions appear only where a provenance reference is intended. Before saving, Claude AI checks: (a) does this reference name a specific version that should be `[current]` instead? (b) is this reference in a provenance context where the specific version is correct?

**Proposed new `examples`:**

> *Operational reference (correct):* "per wa-patch-instruction [current] §6".
>
> *Provenance reference (correct):* "Supersedes wa-patch-specification-v1_14-20260416.md".
>
> *Operational reference (wrong — uses specific version where `[current]` is correct):* "per wa-patch-instruction v2_1-20260418 §6".

---

## Part C — Traceability matrix (content preservation audit)

Every paragraph in the original rule_text maps to exactly one field in the restructured form. No content is discarded.

### GR-LOAD-001 (paragraph counting from original v3_1 rule_text)

| Original paragraph | New field |
|---|---|
| P1 (three-step sequence + steps 1–3 statements) | `rule_text` |
| P2 (no-substantive-work-until) | `rule_text` |
| P3 (non-waivable) | `rule_text` (compressed) + `rationale` (full) |
| P4 (Familiarisation semantics) | `application_notes` |
| P5 (Scope discipline at startup) | `application_notes` |
| P6 (Help-forward bound) | `application_notes` (compressed — points to GR-HF-001) |
| P7 (Non-waivability) | `rationale` |

### GR-HF-001

| Original paragraph | New field |
|---|---|
| P1 (definition) | `rule_text` (compressed) |
| P2 (Default — restrained) | `rule_text` (one-liner) + `application_notes` (full list) |
| P3 (Exception — on ask) | `rule_text` (one-liner) + `application_notes` + `examples` (trigger phrases) |
| P4 (Specialist authorship) | `rule_text` (one-liner) + `application_notes` (full) |
| P5 (Permitted minimum) | `rule_text` + `application_notes` |
| P6 (Judgement edge — flags) | `rule_text` + `application_notes` |
| P7 (Failure mode) | `rationale` |

### GR-TEMPO-001

| Original paragraph | New field |
|---|---|
| P1 (statement + risk description) | `rule_text` (compressed) + `rationale` |
| P2 (Core discipline — write first) | `rule_text` (full) |
| P3 (Recognition is not compliance) | `rule_text` (one-liner) |
| P4 (Load gates) | `rule_text` (one-liner) + `application_notes` (full) |
| P5 (Meta-work) | `rule_text` (one-liner) |
| P6 (Trigger signals) | `application_notes` + `examples` |
| P7 (Session evidence) | `rationale` |
| P8 (Non-waivability) | `rule_text` |

### GR-REF-001

| Original paragraph | New field |
|---|---|
| P1 (principle statement) | `rule_text` |
| P2 (Discipline 1 — pointer, not copy) | `rule_text` (one-liner) + `application_notes` (full) |
| P3 (Discipline 2 — versioned references) | `rule_text` (one-liner) + `application_notes` (full) |
| P4 (Discipline 3 — single authority) | `rule_text` (compressed map) — **flags entry removed**; **`wa-reference [current]` and `[current]` pointers substituted for legacy document names** |
| P5 (Discipline 4 — consistency check) | `rule_text` (compressed) |
| P6 (Discipline 5 — stay in scope) | `rule_text` (compressed) + `application_notes` |
| P7 (Failure mode) | `rationale` |
| P8 (AI drafting considerations) | `application_notes` |

### GR-REF-002

| Original paragraph | New field |
|---|---|
| P1 (principle) | `rule_text` (compressed) |
| P2 (examples inline) | `examples` (moved to field) |
| P3 (relationship to GR-REF-001 Discipline 2) | `rationale` |
| P4 (Scope — what gets `[current]`) | `application_notes` |
| P5 (Sweep mechanism) | `application_notes` — **flags-file sentence replaced with obslog tracking** |
| P6 (Project Files availability) | `application_notes` |
| P7 (AI drafting) | `application_notes` |

### GR-PROG-005

No restructure — already concise. `rule_text` edit only (TODO placeholder replaced).

---

## Part D — Open checks for the researcher

Before the patch is applied, please confirm:

1. **Pattern 1 field split is acceptable** — three separate columns (`rationale`, `application_notes`, `examples`) on `wa_rule_registry`, all TEXT nullable. If Pattern 2 (single `commentary` column) is preferred, the patch is redraftable cheaply.
2. **Schema change** — adding three nullable columns to `wa_rule_registry` is a schema change; the patch assumes these columns exist. If they do not yet exist, a schema-migration patch (or directive) precedes this RULES patch.
3. **Content preservation** — every paragraph from each original rule is mapped to a new field per the traceability matrix in Part C. No content is discarded. Please review that nothing has been tacitly cut or softened.
4. **Version bump convention** — minor bump (e.g. v1_0 → v1_1) because the binding requirement is preserved; only structure and cross-references change. Major bump would be reserved for a rewrite-from-scratch that changes the requirement. Confirm this convention is acceptable.

---

*End of draft rewrites document.*
