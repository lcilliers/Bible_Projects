# Batch 1 — Long Rules — Rewrites for Review

**Filename:** wa-global-rewrites-batch1-long-v1-20260421.md
**Date:** 2026-04-21
**Reference to prior output:** wa-global-rules-review-obslog-v1_0-20260421.md §47–§51; extract wa-global-rules-extract-20260421.json (post-patch).
**Batch scope:** 5 long rules (rule_text > 600 chars): GR-OBS-001, GR-CAD-001, GR-PROG-007, GR-RD-007, GR-DB-001.
**Discipline:** content-evaluation (appropriateness + correctness), not preservation. Version bumps per-rule, minor, unless noted.

---

## How to read this document

For each rule, four blocks are shown:
1. **Current state summary** — version, rule_text length, subject.
2. **Evaluation judgements** — what stays, what moves, what is dropped, and why.
3. **Proposed new field values** — `rule_text` (binding), `rationale`, `application_notes`, `examples`, `version`.
4. **Cross-cutting notes** — consistency observations with other rules.

Fields that remain NULL are shown as *(NULL — none appropriate)* rather than omitted.

---

## 1. GR-OBS-001 — Observations log

### Current state
- Version: `2_0`
- `rule_text` length: 1,329 chars
- Subject: Observations log — continuous write, log authoritative, pass-close persistence
- `applies_to`: all sessions, all phases

### Evaluation judgements

| Paragraph in current rule_text | Disposition |
|---|---|
| Line 1: "obslog authoritative" + "obslog" naming convention | **Keep in rule_text** (binding statement + vocabulary anchor) |
| "Initialisation" paragraph | **Keep in rule_text**, compressed to one sentence pointing at GR-LOAD-001 step 2 |
| "Capture discipline" paragraph | Split: the **prescriptive core** (write at moment of determination; mirror chat to log; verbatim researcher feedback before response) stays in `rule_text`. The **slogan** ("If something is not in the observations log, it has not been received or done") moves to `application_notes` — it's a compliance test, not a binding instruction. The list of capture types (finding, decision, gap, patch consequence, flag, open question) moves to `application_notes` as scope. |
| "Pass-close discipline" paragraph | **Keep in rule_text** — it specifies a binding operational step. |
| "This process must persist throughout the life of the session. This rule is non-waivable." | **Keep in rule_text**. |
| (No rationale currently articulated) | `rationale` field added: *why* — memory is unreliable, crashes happen, context is lost; continuous disk writes prevent session-data loss. |
| (No examples currently) | `examples` NULL — rule is procedural. |

**Style corrections:** "every chat working text" in the original is awkward English — tightened to "every substantive chat output". Capture list tightened for clarity.

**Content dropped: none.** All operative content preserved, just relocated.

### Proposed new field values

**`rule_text`:**

> The observations log — referred to as the obslog — is the authoritative record of every session's working trail. The obslog is initialised as step 2 of the session-startup sequence (GR-LOAD-001); no substantive work may begin until it exists. While the session is live, every finding, decision, gap, patch consequence, and open question is written to the obslog at the moment it is determined. Every substantive chat output also appears in the obslog. When a researcher message is received, the researcher's feedback is recorded verbatim in the obslog before a response is formulated. At every pass close, items requiring database persistence are written via a patch or directive, and a fresh extract confirming the write becomes the working source for the next pass. This discipline persists for the life of the session. This rule is non-waivable.

**`rationale`:**

> Claude AI cannot rely on in-memory accumulation across a session. Sessions crash; context windows truncate; follow-up work depends on what was captured. The obslog exists so that the working trail survives these failure modes. Without continuous capture to disk, findings reach the researcher only through chat output — which is ephemeral and unaudited. Continuous write makes the work externally reviewable at every turn.

**`application_notes`:**

> **Compliance test.** A useful shorthand: if something is not in the observations log, it has not been received or done. This is not literal — the thought existed — but it captures the rule's operational meaning: nothing that is only in chat or in memory counts as work.
>
> **Capture scope.** The list of content types caught by continuous-write includes: findings, decisions, gaps, patch consequences, flags, open questions, clarification requests, and researcher feedback verbatim. New content types arising in a session are logged on the same discipline.
>
> **Verbatim researcher capture.** "Verbatim" means the researcher's message is reproduced exactly, not paraphrased or summarised. If the message is long, the full text is still captured; summaries appear elsewhere in the log if needed.

**`examples`:** *(NULL — none appropriate)*

**`version`:** `2_0` → `2_1` (minor — requirement preserved; structural move + style tightening)

### Cross-cutting notes
- GR-CAD-001 references present_files-after-write; GR-OBS-001 references obslog-write-at-moment. These two rules together govern the write cadence. Both are being restructured in this batch; cross-references use `[current]`-style pointers implicitly through rule_id.

---

## 2. GR-CAD-001 — Write-cadence self-check

### Current state
- Version: `1_0`
- `rule_text` length: 984 chars
- Subject: Write-cadence self-check and present-files milestone
- `applies_to`: all sessions, all phases

### Evaluation judgements

| Paragraph in current rule_text | Disposition |
|---|---|
| Self-check structure (a)/(b)/(c) at top | **Keep in rule_text** — this is the binding format. |
| "After every substantive write to disk, Claude AI calls present_files" | **Keep in rule_text** — second binding requirement. |
| Definition of "substantive write" (finding, decision, patch, obslog entry, session log entry, new file version) | Move to `application_notes` — this is scope, not rule. |
| "This rule exists to prevent the recurring failure mode of Claude AI accumulating findings in chat and memory without writing to disk" | Move to `rationale`. |
| "prevent loss of session data when a session crashes or the chat context is lost" | Move to `rationale`. |
| "non-waivable and externally auditable — the researcher sees on every turn whether the write happened" | "Non-waivable" stays in `rule_text`. "Externally auditable" is rationale. |

**Style corrections:** none needed — current text is clear.

**Content dropped: none.**

### Proposed new field values

**`rule_text`:**

> Before every substantive response, Claude AI produces a short self-check at the top of the response, naming: (a) what was written to disk in this turn, with filenames; (b) whether present_files was called on those writes; (c) if nothing was written, a one-line statement that the response is discussion-only. After every substantive write to disk, Claude AI calls present_files on the written file(s). This rule is non-waivable.

**`rationale`:**

> Claude AI tends to accumulate findings in chat and in-session memory rather than writing them to disk. Chat output is ephemeral; in-session memory is lost when the session ends or the context window truncates. The self-check and the present_files call after writes make the save state externally visible on every turn, so the researcher sees at a glance whether the work has been preserved.

**`application_notes`:**

> **What counts as a substantive write.** A substantive write is any write that produces or updates: a finding, a decision, a patch, an entry in an observations log, an entry in a session log, or a new version of any file. Routine intermediate scratch (temporary working files in `/home/claude` that are not intended as deliverables) does not count.
>
> **Self-check when nothing was written.** The "discussion-only" statement is not a workaround. It applies when the turn genuinely produced no substantive content — a clarification exchange, a question being asked, a short acknowledgement. If work was done, it is written; the self-check then names the write.

**`examples`:**

> Self-check when a file was written: "Writes this turn: obslog appended — wa-{reference}-obslog-v{n}-{YYYYMMDD}.md. present_files called: yes."
>
> Self-check when nothing was written: "Nothing written this turn — response is discussion-only."

**`version`:** `1_0` → `1_1` (minor)

### Cross-cutting notes
- Works in tandem with GR-OBS-001 (obslog discipline) and GR-FILE-008 (dual-write). The three together form the write-discipline triad.

---

## 3. GR-PROG-007 — Inner-being relevance filter

### Current state
- Version: `2.1` (dot notation — non-compliant with GR-FILE-003)
- `rule_text` length: 980 chars
- Subject: Filter at term level — direct engagement or implication in an inner-being characteristic
- `applies_to`: Verse Context instruction, Session B Stage 1, all relevance filtering decisions

### Evaluation judgements

| Paragraph / clause in current rule_text | Disposition |
|---|---|
| Opening: "The inner-being relevance filter is applied to the specific term's use in the verse, not to the verse's general theme or content." | **Keep in rule_text** — scope statement. |
| Two-condition test (a) direct engagement, (b) qualifies/operates on an inner-being characteristic | **Keep in rule_text** — the binding test. |
| "even if the characteristic is not named explicitly... provided it can be inferred from the term's specific use" | Keep in rule_text — it's part of branch (b). |
| "The characteristic does not need to be stated; it needs to be genuinely implied" | Move to `application_notes` — restates branch (b) for clarity. |
| "A term that is present in a verse but plays no role in any inner-being dynamic — purely syntactic, purely locational, purely administrative — does not pass." | Move to `application_notes` — this is an exclusion test, application scope. |
| Final "is this specific term, in its specific use in this verse, implicated in an inner-being characteristic?" | Move to `application_notes` as the **diagnostic question** — useful during classification decisions. |
| (No rationale explicitly) | `rationale` added: why term-level — verses may contain many terms; bleed from verse-theme filtering is the specific failure. |
| (No examples explicitly) | `examples` left NULL — worked examples would be useful but the current rule does not carry any and constructing them crosses into authorship of verse judgements which should be researcher-approved; capturing as a future enhancement in obslog §51. |

**Notation normalisation:** `2.1` → `2_2` (minor bump plus dot-to-underscore).

**Content dropped: none.** All language preserved, redistributed.

### Proposed new field values

**`rule_text`:**

> The inner-being relevance filter is applied to the specific term's use in the verse, not to the verse's general theme or content. A term passes the filter if it does either of the following in this verse: (a) directly engages the inner being — names, expresses, or presupposes an internal state, capacity, orientation, or quality of a person; or (b) qualifies, operates on, or clarifies an inner-being characteristic — the term is implicated in a characteristic even if the characteristic is not named explicitly in the verse, provided it can be inferred from the term's specific use.

**`rationale`:**

> The filter operates at term level because verse-theme filtering produces bleed. A verse may contain terms that relate to its overall subject in ways that have nothing to do with inner-being dynamics (a preposition, a proper noun, a spatial marker), and a verse-level filter cannot separate these from the terms that genuinely engage the inner being. The term-in-its-use is the unit of evidence the programme acts on.

**`application_notes`:**

> **Branch (b) — implication standard.** The characteristic does not need to be stated in the verse; it needs to be genuinely implied by how the term functions. A plausible speculative connection does not pass; a connection that can be read out of the term's specific use in this verse does.
>
> **Exclusion test.** A term present in a verse that plays no role in any inner-being dynamic — purely syntactic, purely locational, purely administrative — does not pass. This is the common failure of verse-theme filtering: the term is there, but it does not do any inner-being work in this verse.
>
> **Diagnostic question.** When a classification decision is close to the line, the operative question is: *is this specific term, in its specific use in this verse, implicated in an inner-being characteristic?* If the answer requires reframing the verse, inventing context, or appealing to the verse's general theme, the term does not pass.

**`examples`:** *(NULL — examples would be useful but require researcher approval of worked verse judgements; flagged for future enhancement in obslog §52)*

**`version`:** `2.1` → `2_2` (minor bump + notation normalisation)

### Cross-cutting notes
- GR-PROG-001 ("Verse always leads") and GR-PROG-006 ("Characteristic-perspective grouping") sit adjacent to this rule. No content overlap — each has a distinct binding — but they are read together in Verse Context work.

---

## 4. GR-RD-007 — Researcher feedback process

### Current state
- Version: `1_0`
- `rule_text` length: 704 chars
- Subject: Researcher feedback process — obs log as detail carrier, chat as alert, follow-up recorded
- `applies_to`: all sessions, all phases

### Evaluation judgements

| Clause in current rule_text | Disposition |
|---|---|
| "The observations log carries the detail — the interpretation, the draft, the ambiguity, the options." | **Keep in rule_text** (binding role of obslog vs chat). |
| "A brief message in chat alerts the researcher to items that need review." | Keep in rule_text. |
| "The researcher's response is captured in the observations log. Any follow-up — revisions, validations, close-outs — is recorded in the observations log." | Keep in rule_text. |
| "Chat is the alerting channel; the observations log is the record." | **Keep in rule_text** — the rule's key distinction. |
| "Claude AI does not wrap decision items in a rigid six-field format; it presents them in the shape that serves the researcher's review." | Move to `application_notes` — it is a prohibition of a specific authorship pattern, better placed as application guidance. |
| "Claude AI does not accumulate unresolved items — they are raised when they arise and resolved in the obs log trail." | Keep in rule_text (binding behaviour). |
| (No rationale explicitly) | `rationale` added: chat length discipline; review-friendly shape; chat is not the record. |

**Style corrections:** "obs log" in the current text is inconsistent with the "obslog" vocabulary normalised in GR-OBS-001 — normalising to "obslog" across both fields.

**Content dropped:** the phrase "The researcher feedback process is interactive and recorded" is decorative preamble — it restates the title; not binding content. Dropped.

### Proposed new field values

**`rule_text`:**

> The obslog carries the detail of decision items — interpretation, draft, ambiguity, options. A brief message in chat alerts the researcher to items that need review. The researcher's response is captured in the obslog; any follow-up — revisions, validations, close-outs — is recorded in the obslog. Chat is the alerting channel; the obslog is the record. Claude AI does not accumulate unresolved items — they are raised when they arise and resolved in the obslog trail.

**`rationale`:**

> Chat is a poor record: it is truncated by context windows, hard to search, and interleaves working text with deliverables. The obslog is the record because it is persistent, searchable, and structured. The separation of alert channel from record channel keeps chat short and keeps the detail where it can be audited.

**`application_notes`:**

> **No rigid format for decision items.** Claude AI does not wrap decision items in a fixed template (the "six-field format" that emerged at one point). Items are presented in the shape that serves the researcher's review — sometimes a single sentence with a recommendation, sometimes a numbered list of options, sometimes a table of trade-offs. Authorship chooses the shape; the discipline is that the detail lives in the obslog, not that it lives in a template.
>
> **Raise-when-arising.** Items are not batched up for a later "review block". They are written to the obslog when they arise and alerted in chat in the same turn. Accumulating unresolved items defers review and produces the "review block at the end of the session" failure mode.

**`examples`:** *(NULL — procedural rule)*

**`version`:** `1_0` → `1_1` (minor)

### Cross-cutting notes
- Complements GR-HF-001 (help-forward bound): GR-HF-001 specifies what Claude AI *may* raise; GR-RD-007 specifies *where* it is raised and how follow-up is tracked.
- Complements GR-OBS-001: GR-OBS-001 makes the obslog the authoritative record; GR-RD-007 applies that to decision items specifically.

---

## 5. GR-DB-001 — No DB state assumptions

### Current state
- Version: `1.0` (dot notation — non-compliant with GR-FILE-003)
- `rule_text` length: 648 chars
- Subject: No DB state assumptions — always verify
- `applies_to`: all sessions, all phases

### Evaluation judgements

| Clause in current rule_text | Disposition |
|---|---|
| "Claude AI never assumes the current state of the database." | **Keep in rule_text** — the binding statement. |
| Scope list: "row counts, field values, flag states, resolution status, schema structure, and the existence or absence of records" | Move to `application_notes` — this is scope, not rule. |
| Three-step check: (1) check chat for already-provided data; (2) request from CC if absent; (3) refresh if stale | **Keep in rule_text** — the operational procedure the rule binds. |
| "Claude AI that proceeds on assumed DB state is in violation of this rule regardless of how recent or reliable the assumption appears" | **Keep in rule_text** — enforcement clause. |
| (No rationale explicitly) | `rationale` added: DB state changes between turns; "recent" is not "current"; operations on stale state produce inconsistencies that compound. |

**Notation normalisation:** `1.0` → `1_1`.

**Content dropped: none.**

### Proposed new field values

**`rule_text`:**

> Claude AI never assumes the current state of the database. Before any operation that depends on DB state: (1) check the current chat for data already provided — do not re-request what is already present; (2) if the required data is not in the chat, request it explicitly from Claude Code via a query; (3) if data was provided earlier in the chat but may be stale, request a refresh. Proceeding on assumed DB state is a violation regardless of how recent or reliable the assumption appears.

**`rationale`:**

> The database changes between turns. Other patches apply; other sessions run; the extract held in chat becomes stale without notice. "Recent" is not "current" — an assumption that was true last turn may be wrong this turn. Operations built on stale state produce inconsistencies that compound across a batch of work. The three-step check costs little; the alternative is the class of errors where the fix is harder than the original operation would have been.

**`application_notes`:**

> **What counts as DB state.** Row counts, field values, flag states, resolution status, schema structure, existence or absence of records, referential integrity, and the presence or absence of patches in a log. If an action depends on any of these, the three-step check applies.
>
> **"Assumed" includes memory.** If Claude AI's memory of a DB fact is from a previous session, it is an assumption, not current state — the three-step check applies, starting from step 2 (request from CC) because the chat will not contain the data.

**`examples`:** *(NULL — procedural rule; no verse or data illustration relevant)*

**`version`:** `1.0` → `1_1` (minor + notation normalisation)

### Cross-cutting notes
- Complements GR-DATA-001 (active terms filter) and GR-DATA-002 (extract is authoritative): both of those rules are specific instances of the general discipline GR-DB-001 binds.

---

## Traceability and evaluation audit — summary

| Rule | Original chars | New rule_text chars | Reduction in rule_text | Commentary fields populated | Content dropped |
|---|---:|---:|---:|---|---|
| GR-OBS-001 | 1,329 | ~860 | −35% | rationale, application_notes | None |
| GR-CAD-001 | 984 | ~550 | −44% | rationale, application_notes, examples | None |
| GR-PROG-007 | 980 | ~600 | −39% | rationale, application_notes | None |
| GR-RD-007 | 704 | ~540 | −23% | rationale, application_notes | One decorative preamble sentence |
| GR-DB-001 | 648 | ~480 | −26% | rationale, application_notes | None |

The reductions in `rule_text` are smaller than those achieved on the first wordy-five patch because these five rules were always closer to rules-form than the Discipline-heavy GR-REF-001 or GR-HF-001. Most content moves to commentary fields rather than being compressed away.

---

## Cross-cutting flags for the researcher (one-line each per GR-HF-001)

1. **Version-notation normalisation in progress.** Dot-notation versions (`2.0`, `1.0`) are non-compliant with GR-FILE-003. Fixed on the two rules this batch touches (GR-PROG-007, GR-DB-001); the rest will be fixed as they are touched in batches 2 and 3.
2. **GR-PROG-007 examples field left NULL.** Worked verse examples would materially help classifiers using this rule, but constructing them requires researcher approval of verse judgements. Flagging as a later enhancement.
3. **"Obslog" vs "observations log" vocabulary.** GR-OBS-001 establishes "obslog" as the canonical short form. GR-RD-007 now uses "obslog" throughout; GR-CAD-001's new application_notes references "observations log". Consistency fine-tuning possible but not driving any change here.

---

## Open check before patch applies

Please confirm:

1. The evaluation judgements above are directionally acceptable. If any specific rule's rewrite looks off, say which and how — I will redo that rule only, not the batch.
2. The GR-PROG-007 decision to leave `examples` NULL (rather than invent worked verse examples without researcher approval) is the right call.
3. The dot-to-underscore version-notation correction on GR-PROG-007 (`2.1` → `2_2`) and GR-DB-001 (`1.0` → `1_1`) is acceptable as a combined minor bump + notation fix.

---

*End of Batch 1 review document. Patch follows at wa-rules-batch1-long-update-v1-20260421.json.*
