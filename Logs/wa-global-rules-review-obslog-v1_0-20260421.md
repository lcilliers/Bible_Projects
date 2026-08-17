# Observations Log — Global Rules Review Session

**Filename:** wa-global-rules-review-obslog-v1_0-20260421.md
**Date opened:** 2026-04-21
**Reference to prior output:** Prior turn in this chat was discussion-only, no file written.
**Scope:** Rules interpretation review, working toward clarifying the global rules. Session initiated under new global rules (schema 3.14.0, extract dated 2026-04-21).
**Session type:** Meta-work on the rules themselves (governance), not registry analysis.

---

## 1. Session-start compliance note

**Load sequence executed per GR-LOAD-001 v3_1 (three-step):**
- Step 1 — rules loaded: wa-global-rules-extract-20260421.json, 36 rules across 13 categories.
- Step 2 — obslog initialised: this file.
- Step 3 — cadence discipline activation: to be stated in the chat response containing this entry.

**Gap note — prior turn.** The first two turns of this chat (interpretation briefing + brief acknowledgement) were produced before the updated rules were supplied and before the load gate was executed. They were framed at the time as pre-session orientation. Under the new GR-LOAD-001 v3_1 this chat is now a live session from this turn forward. Prior-turn content is recaptured below per researcher instruction.

**Change observed vs prior extract (20260420):**
- Flags-file load step has been removed from the startup sequence. Prior GR-LOAD-001 required a four-confirmation load including flags file; new v3_1 has three steps only (rules → obslog → cadence). The flag I raised in the prior turn about an unloaded flags file is superseded — the new rule does not require it at startup.

---

## 2. Researcher turn — verbatim (turn 1, rules interpretation request)

> I have changed the way that you will consume global rules going forward. I have attached the rules. Can you tell me how you will interpret these rules, in sequence of events. what would you do first, what would you look out for, and how would you know that a rule applies.

Attachment at the time: wa-global-rules-extract-20260420.json (prior version, schema 3.13.0, 36 rules, 13 categories including a then-present `load_requirement` category and 22 addendum items across three groups).

## 3. Claude AI response — recaptured summary (turn 1)

Produced before the new rules were supplied. Seven-step interpretation sequence:

1. **Session start gate.** GR-LOAD-001 as entry gate; four confirmations at the time (rules → flags → obslog → cadence). Load bounded the meaning of "familiarise" to read-and-acknowledge.
2. **Cadence discipline active every turn after load.** GR-CAD-001 self-check at top of every response; GR-OBS-001 continuous write; GR-TEMPO-001 write-first in accelerated exchanges. Meta-work is substantive work.
3. **Help-forward bound every turn.** GR-HF-001: restrained default; extensive help-forward only on explicit ask; specialist authorship within researcher direction is Claude AI's to decide not escalate; one-line flags permitted for genuine risks; permitted minimum (compliance gaps, contradictions, one clarifying question) always allowed.
4. **Applies_to as the trigger lookup.** A mapping table produced showing which rules apply always vs Session B only vs Verse Context only etc., using the applies_to field as the operative check.
5. **Rule interaction and precedence.** GR-REF-001 complements GR-REF-002 (not conflict). Addendum items are not independent rules — they point back to main rule_ids. GR-DIR-* rules lived in addendum_patch_directive pending consolidation. GR-PROG-005 contained a TODO placeholder.
6. **Pre-output self-checks.** Four-check list before any output: filename (GR-FILE-001/002/003/006/007/009), format (GR-FILE-005), dual-write (GR-FILE-008), cadence (GR-CAD-001).
7. **Session close.** GR-OBS-003 session log mandatory; GR-PASS-001 pass outputs made available for download before next pass.

**Three one-line flags raised at the time:**
- Flag 1: Chat was meta-work falling under GR-TEMPO-001; strictly, obslog should have been updated before the response, but session had not formally started per GR-LOAD-001; judgement call flagged not asserted.
- Flag 2: GR-PROG-005 contained a [TODO: consolidated patch/directive instruction] placeholder.
- Flag 3: GR-DATA-001 applies_to said "all sessions, all phases" but ADD-REF-001 (addendum) observed it operationally applies only where mti_terms queries are issued.

**One clarifying question asked:** whether the chat should be treated as a live session and proceed to load the flags file and open the obslog, or an out-of-session orientation where the full load was deferred.

## 4. Researcher turn — verbatim (turn 2)

> this is helpful. we will get back to your feedback to reconsider it in a process of making the rules more clear.

## 5. Claude AI response — recaptured summary (turn 2)

Short acknowledgement. Held the three flags and the clarifying question for the later review cycle. Added one note that exchanges of the rule-interpretation kind outside a formal session may warrant their own handling convention, or GR-LOAD-001 might need to bind them the same way as working sessions.

## 6. Researcher turn — verbatim (turn 3, this turn)

> I am uploading a updated version of the global rules and the instructions to edit it. the edit instructions will help you to construct the output .md for any changes to the rules. global rules now apply to this session. Recapture your previous feedback into the obslog

Attachments: wa-global-rules-extract-20260421.json (new, schema 3.14.0); rules-update-protocol.md (new, describes post-M33 patch-based rules update workflow — DB canonical, JSON audit-trail only, three paths: conversational, markdown round-trip, direct file edit [discouraged]; operations insert/update/deprecate via RULES patch type).

## 7. Observations on the updated rules (observation only — no interpretation deepening unless invited)

Comparison 20260420 → 20260421:

- **New category `session_startup` (2 rules)** — groups GR-LOAD-001 and GR-OBS-001 together as the startup gate.
- **GR-LOAD-001 revised to v3_1.** Four-step load sequence replaced by three-step: (1) rules loaded, (2) obslog initialised, (3) cadence activated. **The flags-file load step is no longer in the rule.**
- **GR-OBS-001 revised to v2_0** with new specifics: obslog initialisation is now explicitly step (2) of startup; researcher feedback is to be captured verbatim in the obslog **before formulating a response**.
- **observation_discipline category** now holds only GR-OBS-003 and GR-OBS-004 (GR-OBS-001 moved to session_startup).
- **Addenda section empty** in the new extract — the addendum_instructions, addendum_patch_directive, and addendum_reference groups that were present on 20 April are not in the 21 April extract. (Unclear whether they were migrated, consolidated, or temporarily suppressed — to be confirmed with researcher if it becomes operationally relevant.)
- **Total rule count unchanged at 36 active.**

## 8. Implications for prior flags

- **Flag 1 (meta-work obslog timing):** Superseded for this session — GR-OBS-001 v2_0 now explicitly requires verbatim researcher feedback capture before response formulation. The rule now covers the case directly.
- **Flag 2 (GR-PROG-005 TODO placeholder):** Still present in the 20260421 extract — GR-PROG-005 text still contains "[TODO: consolidated patch/directive instruction — reference to be inserted when the document is produced]". Flag stands.
- **Flag 3 (GR-DATA-001 applies_to vs operational scope):** The addendum item that flagged this (ADD-REF-001) is no longer in the extract. The rule text itself is unchanged. Operational question remains open; audit note that was present is not.

## 9. Open items carried forward to rules-clarity review

1. How rule-interpretation exchanges (meta-work outside a registered session) should be handled under GR-LOAD-001 — whether such exchanges count as "sessions" requiring the full startup gate, or warrant a separate convention.
2. GR-PROG-005 TODO placeholder — the consolidated patch/directive instruction referenced has not yet been produced.
3. Whether the addenda content that was in the 20260420 extract has been migrated, retired, or is awaiting re-export. (The rules update protocol document describes wa_addendum_registry as a supported table for patches, so the schema retains addenda capability; the 21 April extract just contains none at present.)
4. (Researcher stated intent) Reconsider the prior feedback as part of a process to make the rules clearer — held.

---

---

## 10. Researcher turn — verbatim (turn 4)

> the addenda rules are now obsolete as they moved to a different instruction.
> I removed the Flag process. Can you scan the rules to see if any other rules need to be aligned

## 11. Confirmations recorded from the researcher statement

- **Addenda:** Migrated to a different instruction; now obsolete. Empty addenda section in the 20260421 extract is intentional, not an extract artefact. Resolves open item §9.3.
- **Flag process:** Removed. No separate flags file, no flags registry, no standing/open/resolved flag lifecycle. The word "flag" as a verb (to call attention to something in chat or in the obslog) is still ordinary language; the flag *process* as a programme artefact is retired.

## 12. Scan method

Scanned the rule_text and subject fields of all 36 active rules for:
- literal mentions of "flags file" or "global flags"
- mentions of "addendum" / "addenda"
- references to specific ADD- item identifiers
- flag-process language (e.g., "tracked in the flags", "the flag process", "standing flag", "open flag", "resolved flag")
- [TODO: ...] placeholders

## 13. Scan results — 3 rules contain language that needs realignment

### 13.1 GR-REF-001 (v1_0) — content-authority map references retired "Global flags"

**Location:** Discipline 3 paragraph, content-authority map.

**Current text (hit):**
> Operational routines for CC → CC instructions; Interaction protocol between CAI and CC → Interaction protocol document; Programme-wide binding rules → Global rules; **Open issues and flags → Global flags.** When a new content type emerges...

**Issue:** The content-authority map lists "Open issues and flags" as a content type owned by a document called "Global flags". Both are retired.

**Suggested realignment options (for researcher decision):**
- (a) Delete the "Open issues and flags → Global flags" entry from the map entirely (the content type no longer exists).
- (b) Replace with the new home, if open issues now live somewhere specific — e.g. in the obslog, or in a new open-items register. Unknown to me; requires researcher direction.

### 13.2 GR-REF-002 (v1_0) — sweep mechanism "tracked in the flags file"

**Location:** Sweep mechanism paragraph.

**Current text (hit):**
> Sweep mechanism. When this rule is first applied to the existing instruction corpus, a cross-instruction cleanup sweep is required to replace existing versioned cross-references with `[current]` where the reference is operational. **The sweep is tracked in the flags file.** Subsequent references in new or revised instructions are produced in compliance with this rule from the point of adoption forward.

**Issue:** The sentence prescribes tracking the sweep in the now-retired flags file.

**Suggested realignment options (for researcher decision):**
- (a) Replace with "tracked in the obslog of the session that performs the sweep" — consistent with GR-OBS-001 capture discipline.
- (b) Replace with tracking in a named successor register, if one exists.
- (c) Delete the tracking sentence if the sweep is a one-off historical action already completed — the rule would then stand on its forward-compliance clause only.

### 13.3 GR-PROG-005 (v2_0) — TODO placeholder for patch/directive instruction

**Location:** First paragraph, end of sentence about Claude AI requesting database changes.

**Current text (hit):**
> Claude AI requests actions related to the database via patches and directives, complying with **[TODO: consolidated patch/directive instruction — reference to be inserted when the document is produced]**. Claude Code responds with the specified feedback.

**Issue:** Unfilled TODO placeholder. The consolidated patch/directive instruction referenced has not been produced (or its name has not been recorded in the rule).

**Suggested realignment options (for researcher decision):**
- (a) Insert the actual instruction reference if the consolidated patch/directive instruction now exists — using `[current]` per GR-REF-002 if it is an instruction document in Project Files.
- (b) If the consolidated instruction has not been produced, soften the sentence to reference the current governing patch specification and leave directives to be bound when their instruction is written — e.g. "complying with the current wa-patch-specification".
- (c) Leave as-is and track the TODO in whatever successor register replaced the flags file, if applicable.

Note: the rules update protocol document (rules-update-protocol.md, 2026-04-20) describes the post-M33 patch workflow for rules themselves. That is a patch *operations* document. It is possible — but I cannot confirm without researcher direction — that the "consolidated patch/directive instruction" intended by GR-PROG-005 is either (i) this same protocol document, (ii) the patch specification already referenced elsewhere in the rules, or (iii) a distinct instruction yet to be written.

## 14. Scan results — clean

**No other rules contain references to:** flags file, global flags, flag process, addendum/addenda, or ADD- item identifiers, or unfilled TODO placeholders.

The remaining 33 rules in the active set are internally consistent with the retirement of the flag process and the migration of addenda.

## 15. Orthogonal observation — possibly adjacent

`GR-LOAD-001 v3_1` no longer references the flags file (correct — the removal is already reflected there). This was a substantive change in the 20260421 extract and is internally consistent with the retirement.

## 16. Held pending researcher decision

Three realignment points (§13.1, §13.2, §13.3) require your direction before patches can be drafted. The direction needed for each is either (a) the specific replacement wording or target, or (b) an instruction to delete the clause. Patches would then follow the rules-update-protocol.md §3 pattern — a single RULES patch with three UPDATE operations.

---

---

## 17. Researcher turn — verbatim (turn 5)

> 13.1: (a)
> 13.2 (a)
> 13.3 (a) wa-patch-instruction-[current] , wa-directive-instruction-[current]
> the patch instruction is uploaded to be used in conjunction with the global rule update instruction.
>
> I notice that the global rules are very wordy. Does not not add to confusion. Should it not be written in a more rules based style

## 18. Decisions recorded (for the RULES patch to be drafted)

- §13.1 → option (a): delete the `Open issues and flags → Global flags` entry from the content-authority map in GR-REF-001 Discipline 3.
- §13.2 → option (a): replace `The sweep is tracked in the flags file.` in GR-REF-002 with tracking in the session obslog (consistent with GR-OBS-001).
- §13.3 → option (a): replace the `[TODO: consolidated patch/directive instruction — reference to be inserted when the document is produced]` placeholder in GR-PROG-005 with `wa-patch-instruction [current] and wa-directive-instruction [current]`.

Patch will be drafted per rules-update-protocol.md §3 (RULES patch type, UPDATE operations against wa_rule_registry). Drafting deferred pending a separate researcher instruction; decisions are recorded here.

## 19. Patch instruction read

wa-patch-instruction-v2_1-20260418.md loaded. Relevant points carried into the review:
- Patch format: three top-level keys (`_patch_meta`, `operations`, `_patch_summary`). Confirms and extends the rules-update-protocol.md worked example (which did not show `_patch_summary`).
- `patch_id` uses uppercase (applicator convention); filename uses lowercase (GR-FILE-007).
- `patch_type` vocabulary in §3.3 does NOT yet include `RULES` — the rules-update-protocol.md (20260420) states that `RULES` was registered in `wa_patch_type_registry` with `session_b_status_exempt = 1`. The patch instruction (dated 20260418, two days earlier) predates this registration. Implication: either the patch instruction needs a minor update to add `RULES` to the §3.3 vocabulary and §3.4 table with `session_b_status: null`, or rules-update-protocol.md is understood to extend the patch instruction for the governance-domain patch type.
- `wa-directive-instruction [current]` is referenced in §1.2 and Appendix A.3 — confirms the document exists (or is planned) and the `[current]` form is the correct reference for GR-PROG-005's realignment.

## 20. Researcher question on rules style — captured, not answered in chat yet

Verbatim: *"I notice that the global rules are very wordy. Does not not add to confusion. Should it not be written in a more rules based style"*

This is a question about the form of the governing document. Substantive response drafted in chat (see §21 below for the structured answer recorded in the log).

## 21. Response on rules wordiness — recorded

### 21.1 Observation — the rules are indeed wordy

Measured in the 20260421 extract:
- 36 rules, average rule_text length ~850 characters, median ~350.
- Five rules are substantially longer than the rest: GR-LOAD-001 (~2,700 chars), GR-HF-001 (~3,100 chars), GR-TEMPO-001 (~3,000 chars), GR-REF-001 (~4,300 chars), GR-REF-002 (~3,300 chars). These five carry roughly 50% of the total word weight of the rule set.
- The remaining 31 rules are between one and four sentences and read as rules in the conventional sense.

### 21.2 Interpretation — two distinct content types are currently mixed

The wordy rules consistently contain four kinds of content intermixed:
1. **The rule itself** — the binding requirement (usually one to three sentences).
2. **Rationale / failure mode being countered** — explanation of why the rule exists.
3. **Application notes** — how the rule applies in specific situations, edge cases, trained-pull counter-pressure.
4. **Examples** — worked illustrations.

All four are useful. They are not all the same kind of content. In conventional rules drafting (legal, engineering, procedural), (1) lives in the rule body; (2)–(4) live in commentary, explanatory notes, or guidance documents that sit alongside the rule and are distinct from it.

### 21.3 Reflection — whether this adds to confusion

Two effects, pulling in opposite directions:

**Argument that current form helps comprehension:**
- An AI reading the rule at session start encounters rule + rationale + failure-mode + application in a single unit, no navigation needed.
- The failure-mode commentary is specifically calibrated against Claude AI's trained pulls (the "demonstrate thorough reading," "anticipate the next step" patterns). Separating the rule from the failure-mode explanation may weaken the counter-pressure these rules were written to exert.
- Pointer-not-copy (GR-REF-001) creates overhead if rationale sits in a separately versioned document — every rule lookup becomes two lookups.

**Argument that current form adds confusion:**
- At session start, a human or AI scanning for *what must I do* has to separate the normative content from the explanatory content in real time. For some rules this is easy (short). For the five long ones it is not.
- The binding requirement can be buried. GR-LOAD-001's three-step sequence is in the first paragraph, but the "non-waivability" reminder is four paragraphs later; the "familiarisation semantics" block is a separate rule-like clause that could stand alone.
- Version control is at the rule level. A clarification to a rationale paragraph bumps the rule version the same way a change to the binding text does — the diff between v3_0 and v3_1 of GR-LOAD-001 may or may not have touched the actual rule. A reader cannot tell without reading both versions.
- Rules that are partly rule and partly essay are harder to audit for compliance. "Did I comply with GR-HF-001?" is a single-sentence question if the rule is one sentence; it is a paragraph-reading exercise if the rule is five paragraphs.

### 21.4 Option space — three possible forms

A. **Keep current form.** No change. Accept the wordiness as the price of self-contained rules and the counter-pressure effect.

B. **Split rule_text into structured fields per rule.** Add `rule_text` (binding), `rationale` (why), `application_notes` (how/edge cases), `examples`. Schema change — adds fields to `wa_rule_registry`. Extract then shows the rule concisely by default with commentary in folded/sub-sections. AI session-start load can continue to show everything; readers can view the rule-only slice when auditing.

C. **Separate commentary document.** Rules stay short in `wa_rule_registry`; a parallel `wa_rule_commentary` table holds rationale, failure-mode notes, and examples. Extract joins them on display. Version control can decouple — a clarification to rationale bumps the commentary version without touching the rule.

### 21.5 Recommendation — deferred; this is direction/principle, not authorship

Per GR-HF-001, category choice and internal structure are specialist-authorship calls (mine to make); however, the question of whether to restructure the governance schema is direction/principle (the researcher's to decide). Three options are presented above without a recommendation.

One-line observation that may inform the decision: if option B or C is taken, it can be phased — the wordy five (GR-LOAD-001, GR-HF-001, GR-TEMPO-001, GR-REF-001, GR-REF-002) account for most of the weight and can be restructured first; the remaining 31 are already close to rules-form and would migrate cheaply.

## 22. Held pending researcher decision

1. Whether to restructure rule content into binding vs rationale vs application vs examples (options A / B / C above).
2. Whether to add `RULES` to the `patch_type` vocabulary in wa-patch-instruction [current] §3.3 and §3.4, aligning it with rules-update-protocol.md.
3. Whether the RULES patch carrying §13.1/13.2/13.3 should be drafted now or after the style question (§21) is decided — if the style changes, the three rules in question may want to be rewritten as part of that restructuring rather than patched twice.

---

---

## 23. Researcher turn — verbatim (turn 6)

> #1 - B structure the text of the rule to be explicit and clear.
> #2 - this is already done. you can assume the instruction is updated, and use it to guide your preparation of the patch.
> #3 proceed to prepare the patch for the three reallignment patches, and the wording changes for the long worded rules as per #1

## 24. Decisions recorded

- **Option B selected** — restructure rule_text into structured fields: concise binding text in `rule_text`, commentary in separate fields (`rationale`, `application_notes`, `examples`). Pattern 1 (three separate fields) adopted by Claude AI; flagged to researcher for override. See §21.4 of this log for the options considered.
- **Patch instruction assumed current** — wa-patch-instruction [current] treated as having `RULES` registered in §3.3 and §3.4 with `session_b_status: null`. Patch drafted on that assumption.
- **Single patch for all changes** — three realignment updates (§13.1/13.2/13.3 decisions) plus five rule-text restructures (GR-LOAD-001, GR-HF-001, GR-TEMPO-001, GR-REF-001, GR-REF-002) in one RULES patch.

## 25. Drafting plan

1. Draft rewrites for the five wordy rules: concise `rule_text` plus separated `rationale`, `application_notes`, `examples`. Produce as a review document (markdown) so the researcher can see the rewrites before the patch applies.
2. Draft the RULES patch containing:
   - 3 realignment updates (GR-REF-001, GR-REF-002, GR-PROG-005) — rule_text edits only.
   - 5 restructure updates (the wordy five) — rule_text replacement plus new field population.
3. Present both files for researcher review before patch application (per GR-PROC-004 — no patch is applied without researcher approval).

## 26. Authorship decisions recorded (specialist, per GR-HF-001)

- **Version bump policy for the five wordy rules:** minor increment (v1_0 → v1_1, v3_1 → v3_2) — the *binding requirement* is preserved; only structure changes. Major bump would be reserved for a rewrite from scratch that changes what the rule requires. The three realignment rules get minor bumps too (rule_text edits only, requirement unchanged).
- **`rule_text` field after restructure:** contains the binding requirement only, in the shortest form that preserves normative force. Every sentence is a "must/does/is" statement. No "why," no "trained pull," no example.
- **`rationale` field:** why the rule exists and what failure mode it counters.
- **`application_notes` field:** how the rule applies in edge cases; trained-pull counter-pressure; anything about "when in doubt, do X."
- **`examples` field:** worked illustrations, phrase lists, trigger signals.
- **Content preservation:** no content discarded. Every paragraph in the current rule_text maps to one of the four fields. Traceability is a first-class concern.
- **`last_modified` set to 20260421** on every updated rule.

## 27. Draft outputs produced — validation results

**Files written:**
- `wa-global-rules-rewrites-draft-v1_0-20260421.md` — rewrites for researcher review, including traceability matrix (Part C) and open checks (Part D).
- `wa-global-patch-rules-realign-v1-20260421.json` — RULES patch, 6 UPDATE operations.

**Pre-submission validation — all 11 checks PASS:**
- total_operations == len(operations): PASS
- All op_ids unique: PASS
- All touched rule_ids exist in current extract: PASS
- patch_type == RULES: PASS
- session_b_status is null: PASS
- All ops are update with match.rule_id + set: PASS
- No [TODO placeholders in new rule_text: PASS
- No retired flag-process language in any new field: PASS
- patch_id uppercase convention: PASS
- Filename fully lowercase (GR-FILE-007): PASS
- Filename uses .json: PASS

**rule_text length comparison (binding field only):**

| Rule | Old chars | New chars | Change |
|---|---:|---:|---:|
| GR-PROG-005 | 646 | 580 | −66 |
| GR-LOAD-001 | 3,347 | 799 | −2,548 |
| GR-HF-001 | 4,076 | 746 | −3,330 |
| GR-TEMPO-001 | 3,897 | 834 | −3,063 |
| GR-REF-001 | 4,766 | 1,820 | −2,946 |
| GR-REF-002 | 3,607 | 632 | −2,975 |
| **Total** | **20,339** | **5,411** | **−14,928 (~73% reduction)** |

The 14,928 characters of reduction from `rule_text` have been moved to `rationale`, `application_notes`, and `examples` — no content discarded.

## 28. Held for researcher approval before patch apply (GR-PROC-004)

The patch will NOT be applied until the researcher approves. Four review questions recorded in the draft document Part D:

1. Confirm Pattern 1 field split (three columns: `rationale`, `application_notes`, `examples`) is the chosen schema. Pattern 2 (single `commentary` column) is redraftable.
2. Confirm the schema change (three new nullable TEXT columns on `wa_rule_registry`) is in place or will be added before patch apply.
3. Review the traceability matrix in Part C of the draft — confirm no content has been tacitly cut.
4. Confirm minor version bump convention (v1_0 → v1_1, v3_1 → v3_2) is acceptable.

Once approved, CC applies the patch via the rules-update-protocol.md workflow and regenerates the rules extract.

---

---

## 29. Researcher turn — verbatim (turn 7)

> rules draft Part D:
> 1 - split is acceptable it adds clarity. consider updating the additional columns for the other rules also to improve consistency.
> 2 - prepare directive for schema change
> 3 - content must be evaluated for being appropriate and correct, rather than just preserve
> 4 - version bump - keep it simply, versions are maintain on individual rule basis

## 30. Decisions recorded

- **#1 confirmed:** Pattern 1 three-field split adopted. **Additional direction:** extend the restructure to the remaining 30 rules (31 minus GR-PROG-005 which is already in the patch) so the rule set is consistent — every rule has the same four fields, populated or NULL.
- **#2 confirmed:** Schema change to `wa_rule_registry` is to be prepared as a directive (not a patch), because the applicator may not cover schema DDL. CC inspects the database and executes the correct DDL.
- **#3 confirmed — significant reframe:** Content is to be **evaluated for being appropriate and correct**, not just preserved. This changes the nature of the work. The traceability matrix I produced earlier (§26 authorship decision: "no content discarded") is no longer the governing discipline. Content may now be revised, softened, tightened, or dropped where Claude AI judges it inappropriate or incorrect — provided the judgement is recorded and auditable.
- **#4 confirmed — simplification:** Version bumps are per-rule, not batched. Each rule's version increments based on what changed in that rule, using the simple convention already in the rules file (minor for clarifications/restructures that preserve the requirement; major for rewrites-from-scratch or changed requirements).

## 31. Reframe — what #3 changes

The earlier work assumed preservation was the governing constraint — every paragraph had to land somewhere. Under the new direction, content passes through an evaluation gate:

1. **Is this content still accurate?** (e.g., references to retired concepts; outdated session evidence; counter-pressure written against failure modes that may no longer be live)
2. **Is it appropriate for the field it will go in?** (e.g., is this really rationale, or is it prose that has outlived its use?)
3. **Is it correct in style for a rules document?** (e.g., is it specifying what must happen, or is it arguing with a reader?)

If content fails these checks, it is revised or dropped — with the decision recorded in the obslog for audit.

This is a bigger piece of work than the previous draft. The same 36 rules, but now each one goes through an evaluation pass.

## 32. Held — question to researcher before proceeding

The combined scope is now:
- Directive for schema change (3 new columns on `wa_rule_registry`) — small, can be drafted straight away.
- Restructure + evaluate all 36 rules into the four-field form, with content review applied to each one — substantially larger than the patch I just produced.

**Two ways to proceed. I am asking because #3 materially changed the nature of the work, and the right approach depends on how you want the review cycle to work:**

(a) **Produce the schema directive now; do the full 36-rule restructure+evaluation in a single next pass, present as one patch for review.** Clean, one review cycle for all content. Larger document to review at once.

(b) **Produce the schema directive now; restructure+evaluate in batches (e.g. 5–8 rules per batch), present each batch for review before moving to the next.** Slower, but each evaluation decision is reviewed close to when it was made, reducing rework risk.

The six rules already drafted in the earlier patch need re-evaluation too — the preservation discipline I used on them is no longer the governing rule. I would redo those under the new discipline as part of whichever option you choose.

---

---

## 33. Researcher turn — verbatim (turn 8)

> the database schema (before your suggested changes) and the update patch instruction is attached. kindly adjust you directive and patch accordingly.

**Attachments:**
- `database-schema-v3_14_0-20260421.json` — full DB schema, snapshot before the proposed changes.
- `wa-patch-instruction-v2_2-20260421.md` — patch instruction v2_2, now includes RULES patch type and §13 rules-update workflow.

## 34. Findings from the attachments

### 34.1 Schema — `wa_rule_registry` (16 columns, 59 rows)

Columns present: `id`, `rule_id` (UNIQUE), `category`, `subject`, `rule_text`, `example`, `applies_to`, `version`, `added_date`, `last_modified`, `obsolete`, `obsolete_reason`, `superseded_by`, `addendum_ref`, `source_document`, `created_at`.

**`rationale`, `application_notes`, `examples` are NOT present.** The directive must add them.

**Note on existing column `example` (singular):** the table already has an `example` column. The v2_2 worked example (§13.4.1) shows `example` as an optional field on insert. I propose the new field be named `examples` (plural) to carry a list/block of illustrations and the singular `example` column be retained as-is for back-compatibility. Researcher to confirm whether to (a) retain both, (b) rename singular `example` → plural `examples`, or (c) drop the singular in favour of the plural. Captured as a held item.

Row count of 59 > 36 active rules (extract filters `obsolete=0`). The patch only touches 36 active rule_ids, so no effect on the 23 obsolete rows.

### 34.2 Schema — `wa_addendum_registry` (15 columns, 22 rows)

All 22 prior addenda were marked obsolete post-M36 per v2_2 §13.4.4. The four-field restructure does not apply to addenda in this pass.

### 34.3 Patch instruction v2_2 — what changed vs v2_1

- RULES is now registered in §3.3 and §3.4 (session_b_status: null).
- §2.4 defines **programme-wide patch filename and patch_id patterns** — my v1 patch used a different convention and must be regenerated.
- New v2_2 pattern for RULES: filename `wa-rules-{subject}-{action}-v{n}-{YYYYMMDD}.json`, patch_id `PATCH-{YYYYMMDD}-RULES-{SUBJECT}-V{n}`.
- `registry_id` and `word` omitted from `_patch_meta` for programme-wide types.
- `researcher_approval: "PENDING"` convention for RULES patches in `_patch_meta`.
- `produced_at` field shown in ISO-8601 timestamp form in the §13.5 example — I will follow that.
- §13.4.2 confirms `update` op shape — `match: {rule_id: ...}`, `set: {...}`. Matches what I built.

### 34.4 Corrections required to the v1 patch

| Item | v1 (old) | v2 (corrected per v2_2) |
|---|---|---|
| Filename | `wa-global-patch-rules-realign-v1-20260421.json` | `wa-rules-wordy-restructure-update-v1-20260421.json` (scope-named per §2.4) |
| patch_id | `PATCH-20260421-GLOBAL-RULES-V1` | `PATCH-20260421-RULES-WORDY-RESTRUCTURE-V1` (§2.4 pattern) |
| `_patch_meta.registry_id` | `null` | **omit field** (programme-wide — §2.4) |
| `_patch_meta.word` | `"global"` | **omit field** (programme-wide — §2.4) |
| `_patch_meta.produced_by` | `"wa-global-rules-review-session-20260421"` | `"wa-patch-instruction-v2_2-20260421"` (governing instruction per §13.5 example) |
| `_patch_meta.produced_at` | not set | ISO-8601 timestamp (per §13.5 example) |
| `_patch_meta.researcher_approval` | not set | `"PENDING"` (§13.5 convention) |
| `_patch_meta.motivation` | field name `description` | v2_2 §13.5 example uses `motivation` alongside `description`; keeping both |

### 34.5 Held decision from turn 7 (§31 #3) — content evaluation vs preservation

The researcher directed that content be **evaluated for appropriateness and correctness**, not just preserved. This applies to the content inside the patch.

**What I will do now:** regenerate the v1 patch into v2 with the filename/meta corrections only — the content of `rule_text` / `rationale` / `application_notes` / `examples` from v1 is preserved as drafted, not re-evaluated yet.

**Why not re-evaluate now:** re-evaluation is the larger scope discussed in §32 (approach a vs b), and the researcher has not yet chosen the approach. The v2 regeneration corrects the mechanical errors against v2_2; the content evaluation pass still needs approach approval. v2 is therefore a mechanical correction of v1, still labelled as drafted under preservation discipline, and still subject to the evaluation pass before application.

This limits the scope of this turn to what the researcher asked for: adjust the patch (and prepare the directive) per v2_2 and the schema. The content evaluation question remains held from §32.

## 35. Drafting plan

1. Directive — schema change. Adds three nullable TEXT columns to `wa_rule_registry`: `rationale`, `application_notes`, `examples`. Plain-language directive per wa-directive-instruction [current]; CC determines the correct DDL (ALTER TABLE ... ADD COLUMN ...) and executes. Completion confirmation: `PRAGMA table_info(wa_rule_registry)` showing the three new columns present.

2. Patch v2 — regenerate v1 against v2_2 pattern. Mechanical corrections only (filename, patch_id, `_patch_meta` fields per v2_2 §2.4 and §13.5). Operations unchanged in content. v1 patch file left on disk with a note that it is superseded.

3. Update obslog with the two files produced and the validation results.

## 36. Outputs produced this turn

**Files written:**

| File | Purpose | Location |
|---|---|---|
| `wa-global-dir-001-rule-registry-columns-v1-20260421.md` | Schema-change directive adding `rationale`, `application_notes`, `examples` TEXT columns to `wa_rule_registry` | /home/claude + /mnt/user-data/outputs |
| `wa-rules-wordy-restructure-update-v1-20260421.json` | RULES patch per v2_2 §2.4 (programme-wide pattern), §13.4.2 format. Six UPDATE operations. | /home/claude + /mnt/user-data/outputs |
| `wa-global-patch-rules-realign-v1-20260421.json` | **Superseded** by the v2 patch above — kept on disk for provenance but no longer to be applied. Remains in outputs dir from prior turn. | /mnt/user-data/outputs |

## 37. Patch v2 validation — 17 checks, all PASS

1. Top-level keys exactly `{_patch_meta, operations, _patch_summary}` ✓
2. patch_id follows §2.4 pattern `PATCH-YYYYMMDD-RULES-{SUBJECT}-V{n}` ✓
3. Filename fully lowercase per GR-FILE-007 ✓
4. Filename uses §2.4 scope-named pattern `wa-rules-*` ✓
5. `registry_id` omitted (programme-wide per §2.4) ✓
6. `word` omitted (programme-wide per §2.4) ✓
7. All required `_patch_meta` fields present ✓
8. `patch_type == RULES` ✓
9. `session_b_status` is null (RULES is exempt per §3.4) ✓
10. `produced_by` names governing instruction with version ✓
11. `researcher_approval` is PENDING (§13.5 convention) ✓
12. `total_operations == len(operations)` ✓
13. All op_ids unique ✓
14. All ops are valid `wa_rule_registry` updates per §13.4.2 ✓
15. All touched rule_ids exist in current active extract ✓
16. No immutable fields (`id`, `rule_id`, `created_at`) in any `set` clause ✓
17. No `[TODO` placeholders / no retired flag-process language / every op writes at least one restructure-relevant field ✓

## 38. What this turn did NOT do

- **Did not re-evaluate content.** The `rule_text`/`rationale`/`application_notes`/`examples` strings inside the patch operations are the same as in v1, carried forward under the preservation discipline. The content-evaluation discipline from turn 7 (§31 #3) still needs approach approval before it begins. The patch as it now stands is mechanically correct against v2_2 but is still drafted under preservation — it should not be applied until the content pass is done.
- **Did not extend the restructure to the other 30 rules.** Consistency across all 36 rules was directed in turn 7 (§30 #1) — that is the larger scope described in §32 and still needs approach decision.
- **Did not resolve the `example` vs `examples` column naming question.** Held in the directive §7 for researcher decision before CC executes.

## 39. Held items for researcher — in order of what blocks what

1. **Blocks directive execution:** resolve `example` (singular) vs `examples` (plural) naming (directive §7). Three options presented.
2. **Blocks patch application:** directive must be approved and executed first (creates the three new columns that the patch writes into).
3. **Blocks full restructure work:** approach decision from §32 — single patch for all 36 rules, or batched. Plus the content-evaluation discipline from §31 #3 must be applied to the 6 rules already drafted before they are included in whatever final patch is built.

---

## 40. Researcher turn — verbatim (turn 9)

> Directive DIR-20260421-001 (schema): added 3 nullable TEXT columns to wa_rule_registry — rationale, application_notes, examples. Pre-check confirmed option (a) was correct: GR-FILE-001, GR-FILE-007, GR-FILE-009 already hold content in the singular example field that would have been lost under option (c). Table now has 19 columns, 59 rows unchanged. All three §6 confirmations passed.
> Patch PATCH-20260421-RULES-WORDY-RESTRUCTURE-V1: 6 rules updated — GR-PROG-005 (v2_1, TODO filled), GR-LOAD-001 (v3_2), GR-HF-001, GR-TEMPO-001, GR-REF-001, GR-REF-002 (all v1_1). Binding statement in rule_text; rationale / application_notes / examples populated where relevant.
>
> proceed to refine the wording and additional fields of all the rules. global rules updated with patch - attached.

**Attachment:** wa-global-rules-extract-20260421.json (regenerated after the patch applied, same filename as earlier but now contains the six updated rules in their restructured form).

## 41. Confirmations recorded

- Directive DIR-20260421-001 executed successfully. `wa_rule_registry` now has 19 columns, 59 rows. Three new nullable TEXT columns (`rationale`, `application_notes`, `examples`) present.
- Patch PATCH-20260421-RULES-WORDY-RESTRUCTURE-V1 applied. Six rules restructured (GR-PROG-005, GR-LOAD-001, GR-HF-001, GR-TEMPO-001, GR-REF-001, GR-REF-002).
- Naming decision vindicated: option (a) — keep both `example` and `examples` columns — was correct. GR-FILE-001, GR-FILE-007, GR-FILE-009 had content in the singular column that would have been lost under option (c).
- Scope direction: **refine wording and additional fields of all the rules** — this is the full-pass restructure referenced in §32 (approach question). The instruction does not specify batched vs single-pass, so I read "all the rules" as authorisation to work through all 30 remaining rules (36 total minus 6 already done), and I need to pick a batching approach.

## 42. Inventory from the attached extract

- 36 active rules total.
- **6 already restructured** (populated `rationale` / `application_notes` / `examples`): GR-REF-001, GR-REF-002, GR-HF-001, GR-TEMPO-001, GR-LOAD-001, GR-PROG-005.
- **30 remaining** for this pass.
- Singular `example` column populated on three rules already: GR-FILE-001, GR-FILE-007, GR-FILE-009. These contain correct-vs-wrong filename illustrations. Content-evaluation decision needed: move into new `examples` field, leave in `example`, or mirror into both. Captured as §46 held item.
- Length distribution of the 30 remaining: 5 long (648–1,329 chars), 10 medium (300–450 chars), 15 short (66–297 chars). The short rules — e.g. GR-FILE-002 at 66 chars, GR-FILE-005 at 102 — may not need any of the three new fields; NULL will be the correct state.

## 43. Reframe from §31 #3 — content evaluation, not preservation

From this pass onward, rule content is **evaluated for appropriateness and correctness**, not just mapped into fields. This means each rule goes through the following evaluation steps:

1. **Is the binding requirement in `rule_text` still accurate and necessary?** If the rule is wrong or obsolete, flag for the researcher rather than restructure.
2. **Is the style appropriate for the field?** `rule_text` is a prescription ("Claude AI must X"; "Y is non-waivable"). `rationale` is an explanation of the reason. `application_notes` describes edge cases and how the rule applies. `examples` is worked illustration. Content that does not suit any of these gets dropped.
3. **Is there enough content to justify populating the commentary fields?** NULL is the correct state for rules that are already one clean sentence.
4. **Cross-rule consistency:** if two rules restate the same idea, the weaker one points at the authoritative one rather than carrying duplicate content (GR-REF-001 Discipline 1).

Changes made in the evaluation pass are logged in the obslog so the researcher can audit the decisions.

## 44. Sizing observation

Content-evaluation for 30 rules, each producing `rule_text` edits plus potentially three new field populations, is a substantial pass. Based on the 6 already done (which used preservation discipline, a smaller task than evaluation), this pass is materially larger than one turn's worth of careful work if done in a single go.

## 45. Two approach choices — asking the researcher

(a) **Single-pass.** Produce one patch containing up to 30 UPDATE operations. Largest review burden for the researcher; one review cycle; fastest to completion if the work is clean. Risk: if I misjudge what "appropriate and correct" means on early rules, I have 30 rules to re-do.

(b) **Batched, by category.** Run in batches by rule category (e.g. `data_discipline` → `file_naming` → `programme_orientation` etc.), one patch per batch. Review cycles are smaller and the researcher can recalibrate my judgement on early batches before later ones start. 10–13 categories in play, but some are single-rule categories which would be batched with a neighbour. Realistic: 4–6 batches.

(c) **Batched, by length.** Start with the 5 longest remaining rules (likely genuinely four-field), move to the 10 medium, finish with the 15 short ones (most of which will be NULL on the three new fields). Review burden concentrates early where judgement is hardest. Realistic: 3 batches.

My specialist recommendation per GR-HF-001 (since batching is authorship-adjacent direction, researcher's call): **option (c)**. Content-evaluation is hardest on the long rules where rule + commentary are currently mixed; calibrating on those first gives the most useful feedback with the least per-batch volume. But this is a judgement and (b) is equally defensible.

## 46. Held items — naming collision revisited

The singular `example` column is populated on GR-FILE-001, GR-FILE-007, GR-FILE-009 with correct-vs-wrong filename illustrations. Three options for each rule during the evaluation pass:

- Leave the `example` content in place (singular column) and leave the new `examples` column NULL for these rules.
- Move the content into the new `examples` column and NULL the `example` column (but the `example` column stays in the schema for other uses).
- Populate both with the same content (duplication — not preferred, violates GR-REF-001 Discipline 1).

My specialist default: **move to `examples` and NULL the singular** — the new plural column is the one specified in the patch instruction §13.4.1 going forward, and the data is small enough that the move is safe. But this merits confirmation in case the DB tooling or the extractor reads the singular column specifically. Captured as §46 held item.

---

## 47. Researcher turn — verbatim (turn 10)

> #45 (c)
> #46 accept recommendation

## 48. Decisions recorded

- **§45 → (c)** — batch by length, longest first. Three batches:
  - **Batch 1 — Long** (5 rules, 648–1,329 chars): GR-OBS-001, GR-CAD-001, GR-PROG-007, GR-RD-007, GR-DB-001.
  - **Batch 2 — Medium** (10 rules, 300–450 chars): the file-naming rules without content in `example`, the programme_orientation mid-length rules, the data_discipline mid-length rules, GR-PROC-002, GR-PROC-004, GR-OBS-003, GR-PROG-009, GR-PASS-001, GR-FILE-008, GR-FILE-003.
  - **Batch 3 — Short** (15 rules, 66–297 chars): the short data_discipline, file_naming, programme_orientation, and process_discipline rules. Three of these (GR-FILE-001, GR-FILE-007, GR-FILE-009) carry singular `example` content and will also receive the §46 migration into `examples`.
- **§46 → accept recommendation** — during the rule's own turn in a batch, if the singular `example` is populated, move the content into the new `examples` column and NULL the singular. No duplication. For GR-FILE-001, GR-FILE-007, GR-FILE-009, this happens in Batch 3.

## 49. Batch 1 plan — the long rules

Rules in scope (ordered by `rule_text` length, longest first — the order of evaluation):

| # | rule_id | Current v | rule_text chars | Current subject |
|---|---|---|---|---|
| 1 | GR-OBS-001 | 2_0 | 1329 | Observations log — continuous write, log authoritative, pass-close persistence |
| 2 | GR-CAD-001 | 1_0 | 984 | Write-cadence self-check and present-files milestone |
| 3 | GR-PROG-007 | 2.1 | 980 | Filter at term level — direct engagement or implication in an inner-being characteristic |
| 4 | GR-RD-007 | 1_0 | 704 | Researcher feedback process — obs log as detail carrier, chat as alert, follow-up recorded |
| 5 | GR-DB-001 | 1.0 | 648 | No DB state assumptions — always verify |

Approach for each:

1. Read the full existing `rule_text`.
2. **Evaluate** per §43 — is the binding requirement still correct? is the style right for the field? is there enough to justify commentary fields?
3. **Rewrite** into concise `rule_text` (the binding statement) with commentary moved to `rationale` / `application_notes` / `examples` as appropriate. Fields stay NULL if no content belongs.
4. **Version bump per rule** per §30 #4 (simple, rule-by-rule). Minor bump (e.g. v2_0 → v2_1) since the binding requirement is preserved; major bump reserved for rewrites-from-scratch or changed requirements.
5. **Log the evaluation judgements** made per rule, so the researcher can audit.
6. **Draft review document** showing the rewrites before the patch applies (per the batch 1 review pattern used successfully on the first patch).
7. **Build the RULES patch** per wa-patch-instruction [current] §2.4 (programme-wide filename) and §13.4.2 (update on wa_rule_registry).

## 50. Evaluation judgements — recorded per rule before producing the draft

### GR-OBS-001 — rule_text v2_0 (1329 chars)

**Reading in full:** binding content is clear (obslog is authoritative, continuous write, capture researcher feedback verbatim before response, pass-close persistence, non-waivable). Explanatory content is mixed in, including the "If something is not in the observations log, it has not been received or done" line which is a useful slogan and partially binding.

**Judgement:**
- Binding statements (keep in `rule_text`): obslog authoritative; initialisation is step 2 of GR-LOAD-001 startup; continuous write at moment of determination; researcher feedback captured verbatim before response is formulated; chat content mirrored to log; pass-close via patch/directive + fresh extract; non-waivable.
- Rationale (move): why — nothing may be accumulated in memory; crash/loss protection.
- Application notes: the "received or done" clause — moved to `application_notes` with the interpretation that it is both a slogan and a compliance test.
- Examples: none suited here — the rule is procedural, not illustrative. NULL.
- Version bump: v2_0 → v2_1 (minor — requirement preserved).

### GR-CAD-001 — rule_text v1_0 (984 chars)

**Reading in full:** a long-ish single rule about the write-cadence self-check. The binding is the self-check format and the present_files follow-on. There is meaningful rationale ("prevent the recurring failure mode... prevent loss of session data") and a definition of "substantive write" that reads like application notes.

**Judgement:**
- Binding (rule_text): produce self-check at top of every response; state what was written and whether present_files was called; one-line statement if discussion-only; call present_files after every substantive write; non-waivable; externally auditable.
- Rationale: recurring failure mode of accumulating findings in chat/memory without disk write; crash/context-loss protection.
- Application notes: the **definition** of "substantive write" — finding, decision, patch, obslog entry, session log entry, new file version. This is application scope, not rationale.
- Examples: the three-state self-check (file written / no write this turn / explicit discussion-only). Can go either in application_notes or examples. Cleaner as an example.
- Version bump: v1_0 → v1_1.

### GR-PROG-007 — rule_text v2.1 (980 chars)

**Reading in full:** this is the inner-being relevance filter, which is genuinely technical and long because it has a two-branch test. I need to be careful here — this is an analytical rule operating on verse data, not a procedural rule. The binding is the two-condition filter (a) direct engagement and (b) qualifies/operates on an inner-being characteristic. The explanatory content is mostly the expansion of each branch.

**Judgement:**
- Binding (rule_text): the two-condition test — (a) directly engages the inner being (names, expresses, presupposes an internal state/capacity/orientation/quality); (b) qualifies or operates on an inner-being characteristic (characteristic need not be stated, but must be genuinely implied by how the term functions). Filter applies at term level in a verse, not verse-theme level.
- Rationale: why term-level, not verse-theme level — to prevent bleed from verses that happen to contain a term but do not engage inner-being dynamics.
- Application notes: the "purely syntactic, purely locational, purely administrative" exclusion test; the restatement of the central question ("is this specific term, in its specific use in this verse, implicated in an inner-being characteristic?").
- Examples: none in the current rule_text. NULL (or could be added later from real examples).
- Version bump: v2.1 → v2_2. **Notation normalisation:** the current version "2.1" uses a dot not underscore — GR-FILE-003 requires `v[major]_[minor]`. Correcting to `2_2` aligns the notation; this is a v2_2 correction and a minor bump in one step, which is the cleanest path. Recording the notation correction explicitly.
- **Correction alert:** three other rules in the extract also have dot-notation versions: GR-DATA-001 through GR-DATA-005 (all "2.0"), GR-DB-001 ("1.0"), GR-FILE-001/002/006/007/009 (various), GR-OBS-004 ("2.0"), GR-PASS-001 ("1.0"), GR-PROC-004 ("2.0"), GR-PROG-001/003/004/006/009 (all "2.0"). Per GR-FILE-003 these should all be underscored. **Recording this for the researcher as a programme-wide observation** — not fixing in batch 1 beyond the rules it touches (GR-DB-001 in this batch). All other dot-notation fixes happen naturally as each rule is restructured in its own batch.

### GR-RD-007 — rule_text v1_0 (704 chars)

**Reading in full:** the researcher-feedback process — obslog carries detail, chat is the alert channel, follow-up recorded, no rigid six-field format, no accumulation of unresolved items.

**Judgement:**
- Binding (rule_text): obslog carries interpretive detail of decision items; chat is the alerting channel; researcher's response and any follow-up are captured in the obslog; no rigid format — shape items in whatever way serves researcher review; no accumulation — raise when arising, resolve in the obslog trail.
- Rationale: why chat is alert-only (length discipline; obslog is the record); why no rigid format (authorship call, situation-appropriate).
- Application notes: the non-accumulation clause as a working practice.
- Examples: NULL — the rule is procedural.
- Version bump: v1_0 → v1_1.

### GR-DB-001 — rule_text v1.0 (648 chars)

**Reading in full:** no DB state assumptions — always verify. Includes the three-step check sequence (check chat for already-provided data; if not present, request from CC; if stale, refresh) and a strong enforcement clause.

**Judgement:**
- Binding (rule_text): Claude AI never assumes current DB state. Before any DB-dependent operation: (1) check chat for data already provided; (2) if absent, request explicitly from CC; (3) if stale, ask for refresh. Assumption is violation regardless of how recent the assumed state appears.
- Rationale: why — row counts/field values/flag states/resolution status/schema structure/existence can change between turns; assumption is the failure mode.
- Application notes: list of state types covered (row counts, field values, flag states, resolution status, schema structure, existence/absence of records) — this is scope and belongs in application_notes; the enforcement clause belongs in rule_text.
- Examples: NULL.
- Version bump: v1.0 → v1_1 (notation normalisation plus minor bump).

## 51. Two cross-cutting observations found during evaluation — flagged for researcher

1. **Dot-notation versions are non-compliant with GR-FILE-003.** Many rules (GR-DATA-001..005, GR-DB-001, GR-FILE-001/002/006/007/009, GR-OBS-004, GR-PASS-001, GR-PROC-004, GR-PROG-001/003/004/006/009) use `2.0`/`1.0` format rather than `2_0`/`1_0`. In this batch I normalise only the rules I touch (GR-DB-001, GR-PROG-007). Other rules will be normalised as they are touched in batches 2 and 3. **One-line flag per GR-HF-001.**

2. **GR-OBS-001 already carries post-patch restructured content without the new fields.** Per the extract, GR-OBS-001 v2_0 was updated in the last patch with new text about obslog-as-step-2-of-startup and verbatim researcher-feedback capture, but the restructure into four fields was not applied in the last patch. This rule is therefore doubly in-scope: it needs both the four-field split AND a consistency check that the newer binding content is preserved. **Doing both in this batch.**

## 52. Batch 1 — outputs produced

**Files written:**

| File | Purpose |
|---|---|
| `wa-global-rewrites-batch1-long-v1-20260421.md` | Review document with per-rule evaluation judgements and proposed field values |
| `wa-rules-batch1-long-update-v1-20260421.json` | RULES patch, 5 UPDATE operations |

**Validation — 18 checks, all PASS.**

**rule_text reduction (with commentary moved to three new fields, content preserved except one decorative preamble sentence in GR-RD-007):**

| Rule | Old chars | New rule_text chars | Reduction |
|---|---:|---:|---:|
| GR-OBS-001 | 1,329 | 848 | 36% |
| GR-CAD-001 | 984 | 428 | 57% |
| GR-PROG-007 | 980 | 584 | 40% |
| GR-RD-007 | 704 | 469 | 33% |
| GR-DB-001 | 648 | 489 | 25% |

**Version bumps (all minor, per §30 #4):**
- GR-OBS-001: 2_0 → 2_1
- GR-CAD-001: 1_0 → 1_1
- GR-PROG-007: 2.1 → 2_2 (plus notation normalisation per GR-FILE-003)
- GR-RD-007: 1_0 → 1_1
- GR-DB-001: 1.0 → 1_1 (plus notation normalisation)

**Evaluation discipline applied (not just preservation):**
- One decorative preamble sentence dropped from GR-RD-007 ("The researcher feedback process is interactive and recorded").
- Style tightened: "every chat working text" → "every substantive chat output" in GR-OBS-001.
- Vocabulary normalised: "obs log" → "obslog" in GR-RD-007 per GR-OBS-001 canonical form.
- Dot-notation versions corrected on two rules.

**Held for researcher approval before apply (per GR-PROC-004):**

1. Directional acceptance of the five rewrites. If any specific rule's rewrite needs revision, I will redo that rule only.
2. GR-PROG-007 `examples` left NULL (worked verse examples would need researcher approval of verse judgements). Confirm this approach.
3. Version-notation corrections on GR-PROG-007 and GR-DB-001 (dot → underscore, combined with minor bump).

**Cross-cutting flags raised (one-line each per GR-HF-001):**
1. Dot-notation versions remain on 17+ other rules; being fixed as touched in later batches.
2. GR-PROG-007 examples field is a future-enhancement candidate.
3. "Obslog" vs "observations log" vocabulary harmonisation is at the fine-tuning level; not driving changes in this batch.

---

## 53. Researcher turn — verbatim (turn 11)

> Open checks:
> 1 - reviewed assumptions, proceed as suggested
> 2 - noted - accepted
> 3 - consistency is key

## 54. Decisions recorded — Batch 1 approvals

- **#1 approved** — the five Batch 1 rewrites are accepted directionally; patch `PATCH-20260421-RULES-BATCH1-LONG-V1` proceeds to apply.
- **#2 approved** — GR-PROG-007 `examples` left NULL is the right call for now; worked verse examples deferred to a future enhancement (candidate items list in §52 flag 2).
- **#3 approved + elevated to principle** — "consistency is key". This applies to: version-notation normalisation, vocabulary (obslog not "obs log"; `[current]` token usage), rule_text form (binding-only sentence style), and cross-rule references. Consistency is now a governing criterion for the rest of the pass, not just a batch-1 correction.

## 55. Batch 2 — scope and plan

Batch 2 covers 10 medium-length rules (`rule_text` 300–450 chars). Two are shorter than the long batch but long enough to carry commentary; most are already fairly clean but carry dot-notation versions and mixed rationale-in-rule_text to differing degrees.

### 55.1 Scope — the 10 medium rules

| # | rule_id | v | chars | Subject |
|---|---|---|---:|---|
| 1 | GR-FILE-003 | 3_0 | 431 | Version numbering — underscored v[major]_[minor] everywhere |
| 2 | GR-PROG-009 | 2.0 | 422 | Inferential is not confirmed — label accurately |
| 3 | GR-PROC-002 | 2_0 | 407 | Findings rooted in data — traceability required |
| 4 | GR-OBS-003 | 2_0 | 406 | Observations log vs session log — mandatory at close |
| 5 | GR-FILE-009 | 2.0 | 376 | Compact date format in filenames (has singular `example` populated — migrate to `examples` per §48) |
| 6 | GR-DATA-002 | 2.0 | 364 | Extract is authoritative for Session B |
| 7 | GR-DATA-004 | 2.0 | 356 | Complete word data export carries a version number |
| 8 | GR-FILE-001 | 2.0 | 357 | Filename structure (has singular `example` populated — migrate) |
| 9 | GR-FILE-008 | 2.0 | 355 | Dual-write discipline |
| 10 | GR-PASS-001 | 1.0 | 335 | Pass-close download before next pass begins |

### 55.2 Version-notation normalisation — 8 of 10

Eight rules in this batch use dot notation and will be corrected per GR-FILE-003 (underscored form): GR-PROG-009, GR-FILE-009, GR-DATA-002, GR-DATA-004, GR-FILE-001, GR-FILE-008, GR-PASS-001, (GR-OBS-003 is already underscored; GR-FILE-003 and GR-PROC-002 are already underscored). All combined with minor bump.

### 55.3 `example` → `examples` migration — 2 of 10

Per §48, rules with content in singular `example` column have that content moved into the new plural `examples` column and the singular set to NULL. In this batch:

- **GR-FILE-001** — current `example` content: `"wa-023-compassion-sessionb-brief-v1-20260411.md"`. Single filename illustration; well-suited to the plural column too.
- **GR-FILE-009** — current `example` content: `"WRONG: wa-023-compassion-sessionb-brief-v1-2026-04-14.md — CORRECT: wa-023-compassion-sessionb-brief-v1-20260414.md"`. Wrong-vs-correct pair; clearly belongs in `examples`.

Each `set` in those operations will include `"example": null` alongside `"examples": <content>`. Note: GR-FILE-007 is a batch 3 rule (short) and will be handled there.

### 55.4 Evaluation approach — per §43 and §54

For each rule:
1. Read the full current `rule_text`.
2. Identify what is **binding** (stays in `rule_text`), what is **rationale** (moves), what is **application scope/edge case** (moves), what is **example** (moves).
3. Consistency pass — check the rewrite for: underscored versions in any reference; `[current]` token correctness; "obslog" vocabulary; sentence style matching GR-CAD-001/GR-OBS-001/GR-REF-001 rhythm (prescription, then conditions, then non-waivability where it applies).
4. Evaluate — is there anything **to drop** (decorative preamble, restatement of the subject line, content more appropriate elsewhere)?
5. Version bump per rule, minor, with notation correction folded in where needed.
6. Record evaluation judgements in the review document.

### 55.5 Anticipated characteristics of the medium batch

Unlike the long rules, these are **mostly already close to rules-form**. I expect:
- Most `rule_text` fields will shrink modestly (10–30%) rather than the 25–57% seen in Batch 1.
- Several rules may have NULL `rationale` if the rule is self-evident and no "why" has been written.
- `application_notes` will mostly be small: "what counts" definitions or edge-case clarifications.
- `examples` will mostly be NULL except the two that inherit from `example` (singular).

If this prediction turns out wrong during evaluation — e.g. a rule is hiding more content than expected, or a rule's binding is wrong and not just over-worded — I will stop at that rule, flag it in the obslog with the full issue, and ask before continuing. "Consistency is key" cuts both ways: I will not force a rule into a mould it does not fit.

## 56. One sizing check before drafting

Batch 1 was 5 rules. Batch 2 is 10 rules — double the volume. The review document will roughly double in length, the patch will have 10 operations, and the validation will take correspondingly longer.

Two sub-options within the approved approach:

- **(2a) Single batch 2 patch** — 10 operations in one pass. Matches the approved `(c)` approach (3 batches total). Larger review burden for the researcher but one cycle closes all 10 medium rules.
- **(2b) Split batch 2 into 2a (5 rules) + 2b (5 rules)** — more review cycles, smaller increments, opportunity to recalibrate mid-batch.

My specialist default is **(2a) — single patch** on the grounds that Batch 1 went through cleanly and the medium rules are simpler per-rule than the long ones. But if you prefer tighter review cycles, (2b) is available at no real cost.

---

## 57. Researcher turn — verbatim (turn 12)

> 2a

## 58. Decision recorded

- **§56 → (2a)** — single patch for all 10 medium rules. One review cycle.

## 59. Batch 2 evaluation judgements — per rule

Evaluation discipline per §43, consistency principle per §54.

### 1. GR-FILE-003 v3_0 — Version numbering (431 chars, already underscored)

**Rule is already close to rules-form.** Binding is clear (format + bump convention + scope).

- **Keep in rule_text:** format `v[major]_[minor]`; first version is `v1_0`; minor for updates, major for rewrites-from-scratch; applies in filenames, JSON version fields, prose references; applies to all files, documents, instructions, observations logs, patches.
- **Rationale:** none articulated; adding a single-sentence rationale — searchable/sortable form; underscore avoids conflict with SemVer dot meaning in JSON versioning contexts.
- **Application notes:** the "grouped in logical batches" qualifier on minor bumps is application guidance; move.
- **Examples:** add a simple correct/wrong pair — useful because this is a frequently-applied rule.
- **Version:** 3_0 → 3_1 (minor).
- **Content dropped:** none.

### 2. GR-PROG-009 v2.0 — Inferential is not confirmed (422 chars)

- **Keep in rule_text:** the two-sentence binding — plausibility without extract support = inferential; inferential labels cannot be upgraded to confirmed without correlation signal or verse evidence.
- **Rationale:** the third sentence ("An inferential label in a published document is accurate description of the evidence state, not a failure") is rationale — it tells the author why not to hide the label — move.
- **Application notes:** NULL — rule is clean without further expansion.
- **Examples:** NULL — the rule is about labelling discipline; no concrete example carries weight without verse context.
- **Version:** 2.0 → 2_1 (notation + minor).
- **Content dropped:** none.

### 3. GR-PROC-002 v2_0 — Findings rooted in data (407 chars, already underscored)

- **Keep in rule_text:** every finding must be traceable to DB data; a finding not traceable to a specific verse record / term entry / lexical source / correlation signal / extract field is a hypothesis and must be labelled or discarded.
- **Rationale:** NULL — the rule is self-evidently rooted in the programme's empirical discipline.
- **Application notes:** the third sentence ("A finding initially formed on a hypothesis is acceptable only when subsequent evidence supports it on its own terms") is application — move.
- **Examples:** NULL.
- **Version:** 2_0 → 2_1.
- **Content dropped:** none.

### 4. GR-OBS-003 v2_0 — Obslog vs session log (406 chars, already underscored)

- **Keep in rule_text:** two files, different purposes; session log is the handoff produced at close or at named batch boundary; session without a session log has not closed cleanly; always produced before session ends.
- **Rationale:** NULL — the separation is self-evident given GR-OBS-001.
- **Application notes:** the pointer clarifying "observations log is written continuously per GR-OBS-001" — keep the pointer in rule_text (it clarifies the authority); no additional application needed.
- **Examples:** NULL.
- **Version:** 2_0 → 2_1.
- **Vocabulary:** normalise "observations log" to "obslog" where the canonical form applies (first mention keeps "observations log" for full form; subsequent mentions use "obslog" consistent with GR-OBS-001 v2_1).
- **Content dropped:** none.

### 5. GR-FILE-009 v2.0 — Compact date format (376 chars; has `example` populated)

- **Keep in rule_text:** `YYYYMMDD` with no separators; permitted in prose as `YYYY-MM-DD` for readability; required in filenames, patch IDs, document header date fields, structured identifiers.
- **Rationale:** NULL — self-evident (parseability, sort order).
- **Application notes:** NULL — rule_text already covers scope.
- **Examples:** **move** the singular `example` content ("WRONG: ...2026-04-14.md — CORRECT: ...20260414.md") into the plural `examples` column; set singular `example` to NULL per §48.
- **Version:** 2.0 → 2_1.
- **Content dropped:** none; migration only.

### 6. GR-DATA-002 v2.0 — Extract is authoritative (364 chars)

- **Keep in rule_text:** current versioned CC-produced extract is authoritative for Session B; prior outputs are reference only; on conflict, extract is correct and prior output requires correction.
- **Rationale:** NULL — the programme's discipline that DB state is canonical makes this self-evident.
- **Application notes:** NULL.
- **Examples:** NULL.
- **Version:** 2.0 → 2_1.
- **Content dropped:** none; style tightening only.

### 7. GR-DATA-004 v2.0 — Export version confirmation (356 chars)

- **Keep in rule_text:** export is versioned (CC-managed); version must be confirmed at session start; if not confirmed, request from CC; no work proceeds on an extract whose version has not been confirmed in the current session.
- **Rationale:** NULL (the "why" here overlaps with GR-DB-001 rationale about stale state).
- **Application notes:** NULL — rule_text is complete.
- **Examples:** NULL.
- **Version:** 2.0 → 2_1.
- **Content dropped:** none; one minor style tighten ("at session start before any analytical work begins" → "at session start before analytical work begins").

### 8. GR-FILE-001 v2.0 — Filename structure (357 chars; has `example` populated)

- **Keep in rule_text:** pattern `[prefix]-[reference]-[short description]-[version]-[date]`; reference placement (sort-by-reference); reference is entity identifier (cluster code, registry number, group code, or 'global'); dates compact per GR-FILE-009.
- **Rationale:** NULL — self-evident. The "sort-by-reference" phrase is embedded in rule_text but functions as a micro-rationale; keep there.
- **Application notes:** NULL — the reference-identifier list is scope and sits naturally in rule_text.
- **Examples:** **move** the singular `example` content ("wa-023-compassion-sessionb-brief-v1-20260411.md") into the plural `examples` column; set singular to NULL.
- **Version:** 2.0 → 2_1.
- **Content dropped:** none; migration + style tighten.

### 9. GR-FILE-008 v2.0 — Dual-write discipline (355 chars)

- **Keep in rule_text:** writes go to both the working directory and `/mnt/user-data/outputs/` simultaneously; an output only in memory or only in one location has not been written; no exception; applies to all output types.
- **Rationale:** NULL — self-evident given GR-OBS-001 + GR-CAD-001 (persistence + downloadability).
- **Application notes:** the output-type list (observations logs, session logs, patches, instruction documents, analytical briefs) — move; it is scope illustration.
- **Examples:** NULL.
- **Version:** 2.0 → 2_1.
- **Content dropped:** none.

### 10. GR-PASS-001 v1.0 — Pass-close download (335 chars)

- **Keep in rule_text:** all internal outputs produced during a pass are made available for download at pass end, before the next pass begins; applies to obs logs, patch specifications, CC directives, session logs, any pass-level output; pass that closes without presenting outputs has not closed cleanly.
- **Rationale:** NULL — self-evident given GR-OBS-001 + GR-CAD-001.
- **Application notes:** NULL.
- **Examples:** NULL.
- **Version:** 1.0 → 1_1.
- **Content dropped:** none; "patch specifications" → "patches" for consistency (post-v2_0 the patch-specification document was absorbed into the patch instruction; the generic term is now "patches").

## 60. Batch 2 sizing observations

- **10 operations** will be in one patch.
- **2 rules** carry `example` → `examples` migrations.
- **8 rules** have dot-notation version corrections folded in.
- Expected `rule_text` reduction is smaller per-rule than batch 1 (these rules were already close to rules-form).
- Most `rationale` and `examples` fields will be NULL — this is correct per §43: NULL is the right state where nothing distinctive belongs.

## 61. Batch 2 — outputs produced

**Files written:**

| File | Purpose |
|---|---|
| `wa-global-rewrites-batch2-medium-v1-20260421.md` | Review document with per-rule evaluation judgements and proposed field values |
| `wa-rules-batch2-medium-update-v1-20260421.json` | RULES patch, 10 UPDATE operations |

**Validation — 19 checks, all PASS** (17 standard + version-notation + migration check).

**rule_text length change:**

| Rule | Old | New | Change |
|---|---:|---:|---:|
| GR-FILE-003 | 431 | 419 | −3% |
| GR-PROG-009 | 422 | 315 | −25% |
| GR-PROC-002 | 407 | 286 | −30% |
| GR-OBS-003 | 406 | 406 | ±0% |
| GR-FILE-009 | 376 | 345 | −8% |
| GR-DATA-002 | 364 | 363 | ~0% |
| GR-DATA-004 | 356 | 349 | −2% |
| GR-FILE-001 | 357 | 359 | +1% (formatting change) |
| GR-FILE-008 | 355 | 272 | −23% |
| GR-PASS-001 | 335 | 315 | −6% |

Modest reductions as predicted (§55.5). The value of this batch is less about shortening than consistency: version notation normalised on 8 rules, vocabulary harmonised, scope lists moved to application_notes where they were sitting in rule_text for convenience, two singular `example` → plural `examples` migrations executed.

**Version bumps (all minor):**
- GR-FILE-003: 3_0 → 3_1
- GR-PROG-009: 2.0 → 2_1 (notation normalised)
- GR-PROC-002: 2_0 → 2_1
- GR-OBS-003: 2_0 → 2_1
- GR-FILE-009: 2.0 → 2_1 (notation normalised)
- GR-DATA-002: 2.0 → 2_1 (notation normalised)
- GR-DATA-004: 2.0 → 2_1 (notation normalised)
- GR-FILE-001: 2.0 → 2_1 (notation normalised)
- GR-FILE-008: 2.0 → 2_1 (notation normalised)
- GR-PASS-001: 1.0 → 1_1 (notation normalised)

**Terminology updates:**
- "patch specifications" → "patches" in GR-PASS-001 (source doc was absorbed into wa-patch-instruction [current] in v2_0).
- "observations log" → "obslog" for subsequent mentions in GR-OBS-003 (first mention retains full form).

**Singular `example` → plural `examples` migrations (§48):**
- GR-FILE-001: content `"wa-023-compassion-sessionb-brief-v1-20260411.md"` moved to `examples`; singular set to NULL.
- GR-FILE-009: content (wrong-vs-correct pair) moved to `examples`; singular set to NULL.

**Held for researcher approval before apply (per GR-PROC-004):**

1. Directional acceptance of the ten rewrites. If any specific rule's rewrite needs revision, say which — I'll redo that rule only.
2. "patch specifications" → "patches" terminology update in GR-PASS-001 (authorship judgement).
3. Migrations in GR-FILE-001 and GR-FILE-009 clear the singular `example` column as agreed; confirm this remains the right approach.

After batch 2 applies, remaining scope is batch 3 (15 short rules, 66–297 chars), which includes the final `example` → `examples` migration for GR-FILE-007 and the remaining dot-notation normalisations on the short rules.

---

## 62. Researcher turn — verbatim (turn 13)

> open check:
> 1 - all reviewed and accepted as is.
> 2-accepted

## 63. Decisions recorded — Batch 2 approvals

- **#1 approved** — all ten batch 2 rewrites accepted; patch `PATCH-20260421-RULES-BATCH2-MEDIUM-V1` proceeds to apply.
- **#2 approved** — "patch specifications" → "patches" terminology update in GR-PASS-001 confirmed.
- **#3** — not explicitly restated by the researcher in this turn; reading the "all reviewed and accepted as is" as covering the `example` → `examples` migrations for GR-FILE-001 and GR-FILE-009. Proceeding on that reading; will correct if wrong.

## 64. Batch 3 — scope and evaluation judgements

Batch 3 covers 15 short rules (rule_text 66–326 chars). Per §55.5 prediction: most rule_text reductions will be near zero, most commentary fields will correctly remain NULL.

### 64.1 Scope — the 15 short rules (order: longest first)

| # | rule_id | v (current) | chars | Dot→underscore | `example` migrate |
|---|---|---|---:|:---:|:---:|
| 1 | GR-PROG-006 | 2.0 | 326 | ✓ | — |
| 2 | GR-DATA-005 | 2.0 | 315 | ✓ | — |
| 3 | GR-FILE-006 | 1.0 | 308 | ✓ | — |
| 4 | GR-PROC-004 | 2.0 | 307 | ✓ | — |
| 5 | GR-DATA-001 | 2.0 | 302 | ✓ | — |
| 6 | GR-PROG-004 | 2.0 | 297 | ✓ | — |
| 7 | GR-PROG-001 | 2.0 | 287 | ✓ | — |
| 8 | GR-OBS-004 | 2.0 | 236 | ✓ | — |
| 9 | GR-PROG-002 | 2_0 | 228 | — (already) | — |
| 10 | GR-PROG-003 | 2.0 | 213 | ✓ | — |
| 11 | GR-DATA-003 | 2.0 | 203 | ✓ | — |
| 12 | GR-FILE-007 | 2.0 | 172 | ✓ | ✓ (final migration) |
| 13 | GR-PROC-001 | 2_0 | 136 | — (already) | — |
| 14 | GR-FILE-005 | 2_0 | 102 | — (already) | — |
| 15 | GR-FILE-002 | 1.0 | 66 | ✓ | — |

**11 of 15** receive dot-to-underscore notation normalisation. **1 of 15** receives the final `example` → `examples` migration.

### 64.2 Per-rule evaluation judgements

**1. GR-PROG-006 — Characteristic-perspective grouping model (326 chars)**
- Binding: groups describe what a verse is about (inner-being characteristic), not what a term does; groups are characteristic-centric, not term-centric.
- Rationale: NULL — self-evident given programme orientation (GR-PROG-001, GR-PROG-002).
- Application notes: NULL — the sentence "the same property term can serve different characteristics across its corpus" is worth keeping in rule_text; it's the discriminating observation the rule rests on.
- Examples: NULL — verse examples would help but require researcher-approved judgements (same constraint as GR-PROG-007 in batch 1).
- Version: 2.0 → 2_1.
- Style: minor tighten; no content dropped.

**2. GR-DATA-005 — god_as_subject and somatic_link fields (315 chars)**
- Binding: the two fields carry high error rate from bulk ops; verify against verse evidence before setting or relying on them in Session B; unverified values are not confirmed.
- Rationale: NULL — "high error rate from bulk operations" is the rationale inline; keeping it in rule_text.
- Application notes: NULL.
- Examples: NULL.
- Version: 2.0 → 2_1.

**3. GR-FILE-006 — Prefix and reference conventions (308 chars)**
- Binding: prefix `wa`; global → `wa-global`; registry → `wa-023`; cluster → `wa-c17`; Session D → `wa-sd`; batch → `wa-vcb-001`.
- Rationale: NULL.
- Application notes: NULL — the reference-type list is scope but sits naturally in rule_text.
- Examples: the list in the current rule_text reads like examples. Lean toward keeping in rule_text for completeness because the rule's operative content *is* the list.
- Version: 1.0 → 1_1.

**4. GR-PROC-004 — No patch or directive applied without researcher review (307 chars)**
- Binding: every patch and every directive reviewed by researcher before CC applies; Claude AI produces, states intended action + confirmation output, waits for explicit approval; applies without exception.
- Rationale: NULL — self-evident as a governance rule.
- Application notes: NULL.
- Examples: NULL.
- Version: 2.0 → 2_1.

**5. GR-DATA-001 — Active terms filter (302 chars)**
- Binding: all mti_terms queries intended to return active terms include `AND mt.status IN ('extracted', 'extracted_thin')`; queries omitting the filter return deleted terms and produce incorrect counts; non-waivable.
- Rationale: "return deleted terms and produce incorrect counts" is the rationale inline — keep.
- Application notes: NULL.
- Examples: the SQL fragment itself is the example — it sits naturally in rule_text. No additional examples.
- Version: 2.0 → 2_1.

**6. GR-PROG-004 — Session C is primary — Session B deepens it (297 chars)**
- Binding: Session C word study is primary reader-facing; stands on its own; Session B deepens and corrects but does not replace.
- Rationale: "An accurate Session C document that has been corrected by Session B is more valuable than an accessible document that contains errors" — this is rationale. Move.
- Application notes: NULL.
- Examples: NULL.
- Version: 2.0 → 2_1.

**7. GR-PROG-001 — Verse always leads (287 chars)**
- Binding: verse is the primary unit of evidence; analytical work begins with what the verse says; dimensions/classifications/findings emerge from verse evidence; verse is never bent to fit a pre-existing category.
- Rationale: NULL — this is a foundational rule; its "why" is articulated in GR-PROG-002.
- Application notes: NULL.
- Examples: NULL.
- Version: 2.0 → 2_1.

**8. GR-OBS-004 — Obslog version increment at named boundaries (236 chars)**
- Binding: obslog filename is version-incremented when resuming work on same registry/cluster in a new session — not on every file save within the same session; named boundary = new session start, not a mid-session write.
- Rationale: NULL — the distinction between session boundary and mid-session save is self-explanatory given the discipline.
- Application notes: NULL.
- Examples: NULL.
- Version: 2.0 → 2_1.
- Vocabulary: "observations log" → "obslog" for the subject line; rule_text already uses "observations log"; first mention in rule_text keeps full form.

**9. GR-PROG-002 — Programme governing question (228 chars, already underscored)**
- Binding: the governing question is what Scripture reveals about the characteristics, operations, and interrelationships of the human inner being (spirit, soul, body); all analytical work is oriented toward this question.
- Rationale: NULL — the question is definitional.
- Application notes: NULL.
- Examples: NULL.
- Version: 2_0 → 2_1.

**10. GR-PROG-003 — Dimensions are data-derived (213 chars)**
- Binding: dimension assignments are discovered from verse evidence, not imposed; a dimension ungrounded in at least one verse in the registry's corpus is not a dimension for that registry.
- Rationale: NULL — self-evident given GR-PROG-001.
- Application notes: NULL.
- Examples: NULL.
- Version: 2.0 → 2_1.

**11. GR-DATA-003 — mti_term_flags authoritative for somatic classification (203 chars)**
- Binding: the authoritative field for somatic classification is `mti_term_flags` (not `wa_term_inventory.somatic_link`); on conflict, `mti_term_flags` is correct.
- Rationale: NULL — field authority statement is definitional.
- Application notes: NULL — "redundant wa_term_inventory.somatic_link" notes the alternative field; keeping in rule_text.
- Examples: NULL.
- Version: 2.0 → 2_1.

**12. GR-FILE-007 — Lowercase filenames (172 chars, has singular `example`)**
- Binding: all filenames produced by Claude AI are fully lowercase; no uppercase anywhere in filename or extension; no exception.
- Rationale: NULL — self-evident (portability, grep-consistency).
- Application notes: NULL.
- Examples: **migrate** singular `example` content ("WRONG: ...SessionB-log... CORRECT: ...sessionb-log...") into plural `examples`; set singular to NULL.
- Version: 2.0 → 2_1.

**13. GR-PROC-001 — Step completion requires validated output existence (136 chars)**
- Binding: a step producing a required output is not complete until that output exists and has been validated as complete per the instructions.
- Rationale: NULL.
- Application notes: NULL.
- Examples: NULL.
- Version: 2_0 → 2_1.
- **This is a clean one-sentence rule. No restructure beyond the version bump.**

**14. GR-FILE-005 — Output format by purpose (102 chars)**
- Binding: JSON for structured; markdown for descriptive; docx and PDF only on request.
- Rationale: NULL.
- Application notes: NULL.
- Examples: NULL.
- Version: 2_0 → 2_1.
- **Minor bump only. Nothing to restructure — the rule is already at the minimum form.**

Question for self: should I even bump the version if no content changes? — My read: a minor bump without content change is pointless churn. **Judgement call per GR-HF-001:** leave this rule untouched in batch 3. Flag this in the obslog and the review document.

**15. GR-FILE-002 — Short description length (66 chars)**
- Binding: the short description in a filename must not exceed 30 characters.
- Same analysis as GR-FILE-005 — the rule is already at minimum form. Only the dot-notation version `1.0` needs normalisation.
- My read: the notation correction is a genuine change and justifies a minor bump. **Include in batch 3.** v1.0 → v1_1.

### 64.3 Summary count

- **14 operations in the patch** (15 rules minus GR-FILE-005, which has no notation correction and no content change warranting a bump).
- **11 dot-to-underscore notation corrections** folded in.
- **1 `example` → `examples` migration** (GR-FILE-007 — the last one).
- **Almost all commentary fields stay NULL** — correct state for short rules already in rules-form.
- **Content moves**: one rationale extraction (GR-PROG-004, sentence about accurate-vs-accessible value).
- **No content dropped.**

## 65. Batch 3 — outputs produced

**Files written:**

| File | Purpose |
|---|---|
| `wa-global-rewrites-batch3-short-v1-20260421.md` | Review document with per-rule evaluation judgements |
| `wa-rules-batch3-short-update-v1-20260421.json` | RULES patch, 14 UPDATE operations (GR-FILE-005 intentionally excluded) |

**Validation — 19 checks, all PASS.**

**rule_text length change:**

| Rule | Old | New | Change |
|---|---:|---:|---:|
| GR-PROG-006 | 326 | 327 | ±0% |
| GR-DATA-005 | 315 | 318 | +1% |
| GR-FILE-006 | 308 | 308 | 0% |
| GR-PROC-004 | 307 | 304 | −1% |
| GR-DATA-001 | 302 | 301 | ~0% |
| GR-PROG-004 | 297 | 162 | −45% |
| GR-PROG-001 | 287 | 287 | 0% |
| GR-OBS-004 | 236 | 245 | +4% |
| GR-PROG-002 | 228 | 228 | 0% |
| GR-PROG-003 | 213 | 213 | 0% |
| GR-DATA-003 | 203 | 209 | +3% |
| GR-FILE-007 | 172 | 172 | 0% |
| GR-PROC-001 | 136 | 136 | 0% |
| GR-FILE-002 | 66 | 66 | 0% |

Only GR-PROG-004 showed a meaningful reduction (−45%, concluding sentence extracted to `rationale`). Everything else is consistency/notation work as predicted in §55.5.

**Version bumps (all minor):**
- 11 notation normalisations: GR-PROG-006, GR-DATA-005, GR-FILE-006, GR-PROC-004, GR-DATA-001, GR-PROG-004, GR-PROG-001, GR-OBS-004, GR-PROG-003, GR-DATA-003, GR-FILE-007, GR-FILE-002 (12 total when counting GR-FILE-002 which is v1.0 → v1_1 notation+minor).
- 3 minor bumps without notation change (already underscored): GR-PROG-002 (2_0 → 2_1), GR-PROC-001 (2_0 → 2_1).

Actually — recounting against the patch output: 14 operations total; 11 notation fixes (GR-PROG-006, GR-DATA-005, GR-FILE-006, GR-PROC-004, GR-DATA-001, GR-PROG-004, GR-PROG-001, GR-OBS-004, GR-PROG-003, GR-DATA-003, GR-FILE-007, GR-FILE-002 = 12; minus GR-PROG-002 and GR-PROC-001 which were already underscored = 11 notation fixes as recorded in `_patch_summary.version_notation_normalised`).

**Final `example` → `examples` migration:** GR-FILE-007 content moved to plural column; singular set to NULL.

**Rationale extracted:** GR-PROG-004 — concluding sentence about accurate-vs-accessible value moved to `rationale` field.

**Terminology touch:** GR-PROC-004 — "CC directive" → "directive" (aligns with wa-directive-instruction [current]).

**Intentionally untouched:** GR-FILE-005 — already at minimum form (one sentence, no notation issue); version bump would be pointless churn. Authorship call per GR-HF-001 recorded in `_patch_summary.intentionally_untouched`.

## 66. Full-pass cumulative summary (post batch 3)

After all three batches apply, the rule set will be in this state:

- **36 active rules**, all carrying the four-field structure (`rule_text` + `rationale` + `application_notes` + `examples`), populated or NULL per evaluation discipline.
- **All version numbers compliant with GR-FILE-003 underscored form**, with GR-FILE-005 as the one rule that was already compliant and carries its original v2_0.
- **All singular `example` content migrated** to the plural `examples` column (3 migrations: GR-FILE-001, GR-FILE-009, GR-FILE-007).
- **Retired flag-process references** (eliminated in the first restructure patch on GR-REF-001 and GR-REF-002) absent from all rule_text.
- **TODO placeholder** in GR-PROG-005 (filled in the first restructure patch) replaced with `wa-patch-instruction [current]` and `wa-directive-instruction [current]`.

**Patches produced across the pass:**

| Patch | Rules | Scope |
|---|---:|---|
| `PATCH-20260421-RULES-WORDY-RESTRUCTURE-V1` | 6 | Initial restructure (3 realignments + 5 restructures, GR-PROG-005 shared) |
| `PATCH-20260421-RULES-BATCH1-LONG-V1` | 5 | Batch 1 — long rules |
| `PATCH-20260421-RULES-BATCH2-MEDIUM-V1` | 10 | Batch 2 — medium rules |
| `PATCH-20260421-RULES-BATCH3-SHORT-V1` | 14 | Batch 3 — short rules |

Total rule_id coverage: 35 of 36 (GR-FILE-005 untouched by design). When the batch 3 patch applies, the remaining 30-rule scope from §54 is complete.

**Held for researcher approval before apply (per GR-PROC-004):**

1. Directional acceptance of the fourteen rewrites.
2. GR-FILE-005 intentionally untouched — confirm or override (if override, a single-operation patch can be produced).
3. "CC directive" → "directive" terminology touch in GR-PROC-004.

---

## 67. Researcher turn — verbatim (turn 14)

> open check: accepts all three

## 68. Decisions recorded — Batch 3 approvals

- **#1 approved** — all fourteen batch 3 rewrites accepted; patch `PATCH-20260421-RULES-BATCH3-SHORT-V1` proceeds to apply.
- **#2 approved** — GR-FILE-005 remains intentionally untouched (authorship call per GR-HF-001 stands).
- **#3 approved** — "CC directive" → "directive" terminology touch in GR-PROC-004 confirmed.

## 69. Full-pass rules restructure — complete

With batch 3 approved and queued for apply, the full-pass restructure of the global rules (initiated in turn 6 of this session) is content-complete. Nothing further is held on the restructure work.

**Pass summary:**

| Patch | Rules touched | Notes |
|---|---:|---|
| PATCH-20260421-RULES-WORDY-RESTRUCTURE-V1 | 6 | Initial restructure + 3 realignment edits |
| PATCH-20260421-RULES-BATCH1-LONG-V1 | 5 | Long rules (648–1,329 chars) |
| PATCH-20260421-RULES-BATCH2-MEDIUM-V1 | 10 | Medium rules (300–450 chars) |
| PATCH-20260421-RULES-BATCH3-SHORT-V1 | 14 | Short rules (66–326 chars); GR-FILE-005 intentionally excluded |
| **Total** | **35 of 36** | GR-FILE-005 untouched by design |

**Schema change applied:** DIR-20260421-001 added three nullable TEXT columns (`rationale`, `application_notes`, `examples`) to `wa_rule_registry`. Column count 16 → 19, row count 59 unchanged.

**Post-pass rule set state (on batch 3 apply):**
- All 36 active rules carry the four-field structure, populated or NULL per evaluation.
- All versions use GR-FILE-003 underscored form.
- Three singular `example` → plural `examples` migrations completed (GR-FILE-001, GR-FILE-009, GR-FILE-007).
- Retired flag-process references absent from all rule_text.
- GR-PROG-005 TODO placeholder filled with `wa-patch-instruction [current]` + `wa-directive-instruction [current]`.
- Version notation normalised across the rule set (1 exception: GR-FILE-005, already compliant).

**Items intentionally deferred:**
- GR-PROG-007 `examples` field — worked verse examples would need researcher-approved verse judgements (flagged in batch 1 §52, obslog §51 flag 2).

**Session state:**
- Session initiated 2026-04-21 under new rules extract schema 3.14.0.
- Obslog file at v1_0 — no version bump during the session per GR-OBS-004 (same-session mid-session writes).
- 9 files produced across the session (obslog, 3 review documents, 1 directive, 4 patches).

## 70. Next natural actions (not in scope this turn, but noted for planning)

After batch 3 applies and the extract is regenerated, the next actions in the natural order of work would be:

1. **Session log.** Per GR-OBS-003, a session that closes without a session log has not closed cleanly. When the researcher signals end of session, a session log will be produced summarising the trail.
2. **Return to the primary analytical work.** The userMemories indicate Registry 062 (fellowship) is the next queued word for Session B analysis, and Registry 213 (listen) requires Verse Context work. The rules-clarity work is complete; the analytical pipeline resumes where it left off.

Neither item is acted on in this turn — they are noted only so the decision remains in the researcher's hands about when to transition.

*End of turn 14 entry. Holding.*
