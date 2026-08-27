# WA-SessionB-Instruction-v5.0-20260415

**Framework B — Soul Word Analysis Programme
Session B Instruction — Data Audit, Remediation, Analysis, and Database Completion
Version 5.0 | 20260415 | Status: Draft — for researcher review**

| **Document** | **Value** |
|---|---|
| Filename | wa-global-sessionb-instruction-v5.0-20260415.md |
| Supersedes | wa-sessionb-instruction-v4.8-20260414.md |
| Companion documents | wa-global-general-rules-v2.2-20260415.json │ wa-dimensionreview-instruction-v3.1-20260414.md │ wa-versecontext-instruction-v2.7-20260414.md │ wa-sessionb-cc-instructions-v3.3-20260414.md │ wa-patch-specification-v1.11-20260414.md │ wa-sessionc-instruction-[current] │ wa-sessiond-orientation-v3.0-20260412.md |
| Inputs | Complete word data export: wa-[nnn]-[word]-complete-[date].json |
| Outputs | See Section 5 — What This Session Produces |
| Claude AI role | Data audit, analytical passes, outcome recording, checklist verification, handoff |
| Claude Code role | Patch application, sub-process execution, extract production, integrity validation |

---

## Governing Rules

This instruction is governed by **wa-global-general-rules-v2.2-20260415.json**.

Claude AI must confirm the global rules file has been loaded before beginning any work in this session. State aloud: *"Global rules wa-global-general-rules-v2.2-20260415.json loaded."*

Rules stated in the global file are not repeated here. Where a section references a global rule, the rule ID is cited.

---

## Change Log

**v5.0 (20260415):** Complete redesign of the Session B–Session C relationship and closure architecture. Global rules reference updated to v2.2. Stage 1 fully specified including flag resolution loop, inherited flag review, and wa_term_phase2_flags term-by-term audit. Stage 2 six-pass structure fully specified with per-pass write requirements. SD Pointer Persistence, Stage 3 Closure Checklist, Analytical Brief, Integrity Rules, and Naming Conventions fully specified. RESEARCHER_DECISION item handling governed by GR-RD-001 through GR-RD-006 throughout.

Principal changes from v4.8:

1. **Pipeline corrected.** Session C no longer precedes Session B. Pipeline: Session A → Verse Context → Dimension Review → Session B → Session C → Session D.
2. **Stage 3 and Stage 3b removed.** Session B ends with a handoff signal. Session C writes the word study from the verified database.
3. **Analytical Brief redefined.** Dual-purpose handoff: Session C readiness confirmation + Session D SD pointer summary. Not a mini word study.
4. **All observations return to the database.** Observations log is working paper only. All findings must be persisted before Session B closes.
5. **Two types of database writes formalised.** Type (a): data quality. Type (b): analytical outcomes.
6. **Each pass closes with a confirmed database write.** Per GR-PASS-002.
7. **Session B Closure Checklist introduced.** Mandatory final output — Claude AI's accountability instrument.
8. **Corrective action loop formalised.** Checklist failures trigger a defined corrective loop.
9. **Flag resolution loop specified.** Stage 1 now includes a defined process for reviewing and closing all inherited flags before Stage 2 begins.
10. **wa_term_phase2_flags review specified.** Term-by-term advisory flag review incorporated into Stage 1 audit.
11. **RESEARCHER_DECISION format governed.** Per GR-RD-001 through GR-RD-006 — programme-wide standard.

*Prior version history (v1.0–v4.8): see wa-sessionb-instruction-v4.8-20260414.md.*

---

## 1. Purpose and Scope

Session B is the analytical quality gate for each word in the programme. It operates on a single word per run. It does not advance until the word is complete in three respects:

**1. Data complete and reliable.** Every field in the registry is correctly populated. Every data gap has been identified, patched, and confirmed. Verse context is sound. Dimension data has reached `CLAUDE_AI` confidence. Correlation signals can fire correctly from the clean data. No analytical work begins on unreliable data.

**2. Analysis complete and recorded.** A rigorous six-pass analysis has been conducted against the clean data. The findings from every pass — meaning synthesis, divine dimension pattern, verse annotations, somatic evidence, language accuracy, and correlation audit — are persisted to the database as structured records. The observations log is a working document only; it has no standing in Session C or Session D.

**3. Database complete and verified.** All analytical outcomes from the six passes are recorded in the appropriate database tables. SD pointers are in the database. All inherited Session B flags are resolved. The Closure Checklist has been run against a fresh extract and passed clean. The Analytical Brief confirms readiness for Session C and Session D.

**What Session B does:**
- Audits the complete word data and identifies all gaps
- Reviews and closes all inherited flags from prior phases
- Triggers and oversees Verse Context and Dimension Review sub-processes where required
- Conducts six analytical passes against the clean, complete data
- Persists all analytical outcomes to the database via Type (a) and Type (b) patches
- Raises and persists all Session D pointers
- Runs the Closure Checklist against the verified database
- Produces the Analytical Brief as handoff to Session C and Session D
- Advances `session_b_status` to `Analysis Complete`

**What Session B does not do:**
- Write the word study — that is Session C
- Draw cross-registry synthesis conclusions — that is Session D
- Leave analytical findings only in the observations log — all findings must reach the database
- Close until the Closure Checklist is clean

Session B is multi-session. A single session may cover only part of one stage. The session log is the continuous record across all sessions for this word.

---

## 2. Pipeline Position

```
Session A  (term extraction → complete JSON)
     │
     ▼
Verse Context  (verse relevance filtering, grouping, anchor designation)
     │
     ▼
Dimension Review  (dimension assignment → CLAUDE_AI confidence on all groups)
     │
     ▼
Session B  (this instruction — multi-session operation)
     ├── Stage 1: Data audit and remediation
     │     ├── Confirm extract version
     │     ├── Read complete JSON → identify all gaps
     │     ├── Inherited flag review (wa_session_research_flags, session_target = B)
     │     ├── wa_term_phase2_flags term-by-term audit
     │     ├── Type (a) patches: field-level corrections
     │     ├── Verse Context sub-process (if triggered)
     │     ├── Dimension Review sub-process (if triggered)
     │     ├── RESEARCHER_DECISION block (if items raised)
     │     └── Fresh extract: Claude Code re-exports clean JSON
     ├── Stage 2: Analytical passes (six passes against clean data)
     │     ├── Pass 1: Meaning and semantic range
     │     ├── Pass 2: Divine dimension
     │     ├── Pass 3: Verse annotations
     │     ├── Pass 4: Somatic evidence and spirit-soul-body classification
     │     ├── Pass 5: Language accuracy
     │     └── Pass 6: Correlation audit and connection verification
     │     [Each pass closes with confirmed Type (b) database write — per GR-PASS-002]
     ├── Section 2.1: Analytical Brief
     ├── Section 2.2: SD Pointer Persistence
     └── Stage 3: Closure
           ├── Fresh extract
           ├── Closure Checklist (all domains verified)
           ├── Corrective action loop (if checklist fails)
           ├── Closing patch → session_b_status = Analysis Complete
           └── Handoff signal → Session C and Session D
     │
     ▼
Session C  (word study production — reads from database only)
     │
     ▼
Session D  (cross-registry synthesis — reads from database + SD pointers)
```

---

## 3. What to Attach at Session Start

- This instruction file
- Global rules file: `wa-global-general-rules-v2.2-20260415.json`
- The complete word data export: `wa-[nnn]-[word]-complete-[date].json`
- CC instructions: `wa-sessionb-cc-instructions-v3.3-20260414.md`

Sub-process instruction documents are attached only when the sub-process is triggered:
- Verse Context sub-process: `wa-versecontext-instruction-v2.7-20260414.md`
- Dimension Review sub-process: `wa-dimensionreview-instruction-v3.1-20260414.md`

Do not load more data into the working session than the current step requires.

---

## 4. Governing Disciplines

These disciplines apply without exception across all stages, all passes, and all sessions. All are governed by the global rules file.

**Step-by-step.** Per GR-PROC-001. Each step is completed and confirmed before the next begins.

**Write on discovery.** Per GR-OBS-001 (non-waivable). Every finding, decision, gap, patch consequence, flag, and open question is written to the observations log at the moment it is determined.

**All observations return to the database.** Per GR-OBS-006. Every analytical finding must be persisted to the appropriate database table before the session closes. Session C and Session D read from the database only.

**Data is authoritative.** Per GR-PROC-002. Work strictly from what is in the JSON. Do not import general knowledge to fill gaps.

**All changes through patches or directives.** Per GR-PROC-003 and GR-DIR-001 through GR-DIR-005. Patches are used when field names, FK keys, and operations are certain. Directives are used when the outcome is known but execution path requires CC inspection. Both require researcher approval (GR-PROC-004) and a stated completion confirmation (GR-DIR-005).

**Two types of database writes.** Type (a) patches correct and complete the input data. Type (b) patches record analytical outcomes. Both are mandatory. Neither substitutes for the other.

**Pass-close database write.** Per GR-PASS-002. Every analytical pass ends with a patch or directive to persist its outcomes. A fresh extract is pulled confirming the write before the next pass begins.

**Pass-close download.** Per GR-PASS-001. All outputs produced during a pass are made available for download at pass close before the next pass begins.

**No DB state assumptions.** Per GR-DB-001. Claude AI never assumes the current state of the database. Check the chat first; request from CC if not present; ask for a refresh if currency is in doubt.

**Researcher decision items.** Per GR-RD-001 through GR-RD-006. A RESEARCHER_DECISION item is raised only after Claude AI has exhausted its own analytical resources. It is presented in a discrete numbered block — never embedded in analysis. It must contain: RD-ID, what was checked, why resolution was not possible, the question, options with consequences, and Claude AI's recommendation. The resolution produces a concrete outcome. The same question is never raised twice.

**Session logs at every breakpoint.** Per GR-PROC-006.

**Cross-registry vision is always active.** Every piece of data read in Stage 2 is read twice: once for what it says about this word, and once for what it says about something beyond this word. SD pointers are raised continuously throughout all passes — not accumulated for Pass 6. Per Section 2.0a.

---

## Section 2.0a — Cross-Registry Vision

Cross-registry vision is a continuous discipline active throughout all six analytical passes, not a Pass 6 task. While reading every verse, group description, sense structure, lexical entry, dimension assignment, somatic observation, and correlation signal, Claude AI holds the question: **what does this data tell me about something beyond this registry?**

Five standing questions applied to every anchor verse:
1. Does this verse name or imply an inner-being characteristic that appears in another registry?
2. Does the term's behaviour here differ from its primary registry — suggesting a cross-registry boundary question?
3. Does the grammatical form (causative, reflexive, passive) create a causal or relational connection to another inner-being state?
4. Does the verse place two or more inner-being states in structural relationship (sequence, causation, contrast, parallel)?
5. Does the somatic expression here align with a somatic pattern in another registry?

A positive answer to any of these five questions triggers an SD pointer — written immediately to the observations log, persisted to `wa_session_research_flags` at pass close.

Per integrity rule SB-13: Pass 6 must not be the only pass that generates SD pointers. If it is, Stage 2 must be repeated from Pass 1.

---

## 5. What This Session Produces

Two categories of database write are produced throughout Session B:

| Write type | Purpose | Stage |
|---|---|---|
| Type (a) patch | Data quality — correct, complete, and reliable input data | Stage 1 |
| Type (b) patch / directive | Analytical outcomes — structured records of what Session B found | Stage 2 passes |

The following documents are produced:

| Output | Stage | Type |
|---|---|---|
| Observations log | All stages | Working log — written continuously; all content must be persisted to database before session closes |
| Session log | All stages | Breakpoint summary — produced at every pause or end per GR-PROC-006 |
| Type (a) field-level patch(es) | Stage 1 | JSON patch(es) for data corrections |
| CC directive(s) | Stage 1 | Plain-language instructions for CC operations |
| Verse Context sub-process outputs | Stage 1 (if triggered) | Per VC instruction |
| Dimension Review sub-process outputs | Stage 1 (if triggered) | Per DR instruction |
| Clean complete JSON | Stage 1 end | Re-exported by CC after all Stage 1 patches confirmed |
| Type (b) pass outcome patches / directives | Stage 2 — per pass | Analytical findings persisted at each pass close |
| Analytical Brief | Stage 2 end | Dual handoff: Session C readiness + Session D SD pointer summary |
| SD pointer patch | Section 2.2 | SD_POINTER records in wa_session_research_flags |
| Closure Checklist | Stage 3 | Verified checklist against fresh extract |
| Closing patch | Stage 3 | session_b_status → Analysis Complete |
| Handoff signal | Stage 3 end | Opens Session C; notifies Session D queue |

---

## Stage 1 — Data Audit and Remediation

### Purpose

Stage 1 makes the data complete, correct, and reliable before any analytical work begins. No pass in Stage 2 begins until Stage 1 is fully complete and a fresh extract is confirmed. This is a hard gate — per integrity rule SB-1.

Stage 1 has six sequential steps:

```
Step 1.1 — Confirm extract version
Step 1.2 — Read and audit the complete JSON
Step 1.3 — Inherited flag review
Step 1.4 — wa_term_phase2_flags term-by-term audit
Step 1.5 — Type (a) patch construction and application
Step 1.6 — Sub-process triggers and fresh extract
```

RESEARCHER_DECISION items raised during any step are accumulated and presented as a discrete block at the end of Step 1.4 — before patch construction begins. Stage 2 does not begin until all RD items from Stage 1 are resolved.

---

### Step 1.1 — Confirm Extract Version

Per GR-DB-001 and GR-DATA-004. Before reading any data:

1. State the filename of the complete word data export attached to this session.
2. Request from CC: confirm this is the current version of the extract for registry [nnn] and return the version identifier and export date.
3. Wait for CC confirmation. If CC returns a different version as current — stop. The attached extract is stale. Request the current version before proceeding.
4. Record in observations log: `Extract confirmed: [filename] — version [n] — exported [date].`

Do not proceed until extract version is confirmed.

---

### Step 1.2 — Read and Audit the Complete JSON

Read the complete word data export in full. For each section of the JSON, work through a defined audit checklist. Record every gap, anomaly, or concern in the observations log at the moment of discovery — per GR-OBS-001.

**Audit checklist — registry fields:**

| Field | Check |
|-------|-------|
| `word`, `registry_no`, `cluster` | Present and correct |
| `session_b_status` | Should be at the expected stage entry point |
| `verse_context_status` | Must be `Complete` before Stage 1 can proceed |
| `dimensions` | Populated — at least one dimension present |
| `sb_classification` | May be NULL at this stage |
| `carry_forward` | Default 1 — note if 0 |

**Audit checklist — terms:**

For each term in the extract:

| Check | Action if gap found |
|-------|-------------------|
| `status` is populated | Note as gap — requires classification decision |
| `evidential_status` is populated | Note as gap — requires Stage 2 Pass 1 |
| `god_as_subject` value | Per GR-DATA-005: do not trust — verify against verses in Pass 2 |
| `somatic_link` value | Per GR-DATA-005: do not trust — verify against verses in Pass 4 |
| Verse count > 0 for OWNER terms | Zero-verse OWNER term is a data gap — flag |
| `strongs_number` format | Must be clean (no embedded spaces, correct prefix H/G) |

**Audit checklist — verse context groups:**

| Check | Action if gap found |
|-------|-------------------|
| All OWNER terms have at least one group | Missing groups trigger Verse Context sub-process |
| Each group has a description | Blank description is a gap — note |
| Each group has at least one anchor verse | No anchor is a gap — note |
| `dominant_subject` populated on all dimension index rows | Missing triggers Dimension Review sub-process consideration |

**Audit checklist — dimension assignments:**

| Check | Action if gap found |
|-------|-------------------|
| All groups have a dimension assignment | Unassigned group triggers Dimension Review sub-process |
| All assignments at `CLAUDE_AI` or `RESEARCHER` confidence | `AUTOMATED` confidence is a data gap — triggers Dimension Review sub-process |
| No dimension assignment contradicts the group description | Contradiction is a finding — note in observations log |

**Audit checklist — prior-phase findings:**

Retrieve all `wa_session_b_findings` rows for this registry where `delete_flag = 0`. For each finding:

| Check | Action |
|-------|--------|
| Finding type is in controlled vocabulary | Note anomaly if not |
| `pass_ref` populated | Note if NULL — may be a pre-v5.0 finding |
| Finding content matches the extract data | Note any contradiction — requires resolution in Stage 2 |

Record the count of prior-phase findings in the observations log: `Prior-phase findings for registry [nnn]: [n] active findings.`

These findings are not resolved in Stage 1. They are reviewed and dispositioned during the relevant Stage 2 pass.

---

### Step 1.3 — Inherited Flag Review

**Purpose:** Identify all flags from prior phases that target Session B for this registry and confirm they will be resolved before Stage 2 closes.

Per GR-DB-001: do not assume the current state of `wa_session_research_flags`. Request the data.

**Action:** Request from CC — return all rows from `wa_session_research_flags` where `registry_id = [nnn]` AND `session_target = 'B'` AND `resolved = 0`.

**If zero rows returned:** Record in observations log: `Inherited Session B flags: 0. No inherited flags to resolve.` Proceed to Step 1.4.

**If rows returned:** For each flag:

1. Record the flag in the observations log: flag_label, flag_code, priority, description.
2. Assess whether the flag can be resolved from the current extract data alone:
   - **Resolvable in Stage 1** (data error, missing field, extraction anomaly): note the correction required — this becomes a Type (a) patch item.
   - **Resolvable during Stage 2** (requires verse reading, analytical judgement, or pass-specific work): note which pass will encounter and resolve it. The flag is carried forward to that pass.
   - **Not resolvable within this registry** (requires cross-registry data): convert to SD_POINTER — the flag's description carries forward as the pointer content. Mark the original flag `resolved = 1` with `resolved_note = 'Converted to SD_POINTER [label]'` in the Stage 1 patch.
   - **Requires researcher input** (genuine decision required after exhausting analytical resources): raise as a RESEARCHER_DECISION item per GR-RD-002.

3. Record the disposition of each flag in the observations log.

**Hard gate:** All inherited Session B flags must reach a confirmed disposition before Stage 2 begins. A flag with no disposition is a Stage 1 incomplete.

---

### Step 1.4 — wa_term_phase2_flags Term-by-Term Audit

**Purpose:** Review existing phase2 analytical flags on the registry's terms against the verse evidence. These flags are advisory — prior-session hypotheses. They are not confirmed analytical facts. The assessment (confirmed / rejected / irrelevant) is made by reading the verses, not by accepting the flag.

Per GR-DB-001: request the data rather than assuming it.

**Action:** Request from CC — return all rows from `wa_term_phase2_flags` where `term_inv_id` is in the active term set for registry [nnn]. Include: term_inv_id, strongs_number, flag_code, description (if any).

**If zero rows returned:** Record in observations log: `wa_term_phase2_flags: 0 flags for this registry.` Proceed to RESEARCHER_DECISION block.

**If rows returned:** For each term that has phase2 flags:

1. Read the verses for that term in the extract.
2. For each flag on the term, assess against the verse evidence:

| Outcome | Condition | Action |
|---------|-----------|--------|
| **Confirmed** | Verse evidence supports the flag | Record in observations log: `[flag_code] on [strongs] — confirmed by [verse reference].` Flag stands — no patch needed. |
| **Rejected** | Verse evidence does not support the flag | Record in observations log: `[flag_code] on [strongs] — rejected. Reason: [specific reason].` Add to Type (a) patch: mark flag with `delete_flagged = 1` and `obsolete_reason`. Per GR-OBS-005 — no physical deletion. |
| **Irrelevant — term deleted** | The term has `status = delete` in `mti_terms` | Record in observations log: `[flag_code] on [strongs] — irrelevant, term deleted.` No patch needed — the term and its flags are already outside the analytical scope. |
| **Irrelevant — function word** | The term is a particle, preposition, conjunction, or pronoun with no inner-being content | Record in observations log: `[flag_code] on [strongs] — irrelevant, function word.` Add to Type (a) patch: mark flag with `delete_flagged = 1` and `obsolete_reason = 'Function word — no inner-being analytical content.'` |
| **Thin evidence** | Verse count is too low to confirm or reject confidently | Record in observations log: `[flag_code] on [strongs] — thin evidence. [n] verses available. Carrying forward to Pass [n] for deeper assessment.` Flag carries forward — resolved in the relevant Stage 2 pass. |

3. Where a flag's `description` field is NULL (99% of bulk-imported flags), the assessment is made entirely from the verse evidence. The absence of prior reasoning does not block assessment — it means the verses must carry the full evidential weight.

**Record in observations log at step close:** `wa_term_phase2_flags audit complete. Confirmed: [n]. Rejected: [n]. Irrelevant: [n]. Thin — carried to Stage 2: [n].`

---

### RESEARCHER_DECISION Block — Stage 1

After Steps 1.3 and 1.4 are complete, collect all items that could not be resolved analytically and present them as a numbered decision block before proceeding to patch construction.

Format per GR-RD-002: each item must contain RD-ID, what was checked, why resolution was not possible, the question, options with consequences, and Claude AI's recommendation.

If zero items: record `No RESEARCHER_DECISION items from Stage 1.` and proceed to Step 1.5.

If items present: present the block. Stage 1 patch construction does not begin until all items are resolved. The researcher responds by RD-ID number. Each response produces a concrete outcome — a correction noted, a patch item added, or a direction confirmed.

---

### Step 1.5 — Type (a) Patch Construction and Application

Compile all audit findings from Steps 1.2, 1.3, and 1.4 that require database correction. These are data quality corrections — not analytical findings.

**Items that generate Type (a) patches:**
- Missing or incorrect field values on `word_registry`, `wa_term_inventory`, or `mti_terms`
- Rejected `wa_term_phase2_flags` rows (mark `delete_flagged = 1`)
- Inherited flag dispositions where the flag is closed in Stage 1
- Verse context or dimension gaps that can be corrected by a field patch (as opposed to requiring a full sub-process)

**Construct the patch** per the patch specification. State the patch contents in the observations log before requesting researcher approval.

**Researcher approves → CC applies → CC returns confirmation.**

Review the confirmation against the expected outcomes. If confirmation reveals anomalies, raise a corrective directive before proceeding.

Record in observations log: `Stage 1 Type (a) patch applied and confirmed. [n] operations. Confirmation reviewed — [outcome].`

---

### Step 1.6 — Sub-Process Triggers and Fresh Extract

**Sub-process triggers:** If the audit in Step 1.2 identified gaps that require a full Verse Context or Dimension Review sub-process, those sub-processes run now — after the Type (a) patch is confirmed but before the fresh extract is pulled.

- **Verse Context sub-process:** Triggered if any OWNER term has zero verse context records, or if verse context groups are missing or malformed. Load `wa-versecontext-instruction-v2.7-20260414.md` and run the sub-process. Do not proceed until sub-process is complete and its own patch is confirmed.
- **Dimension Review sub-process:** Triggered if any group has `AUTOMATED` confidence dimension assignment, or if any group has no dimension assignment. Load `wa-dimensionreview-instruction-v3.1-20260414.md` and run the sub-process. Do not proceed until sub-process is complete and its own patch is confirmed.

**Fresh extract:** After all Stage 1 patches and sub-processes are confirmed, request from CC: re-export the complete word data for registry [nnn] and return the new version identifier.

Confirm the fresh extract version in the observations log: `Fresh extract confirmed: [filename] — version [n] — exported [date]. Stage 1 complete.`

**Stage 2 does not begin until the fresh extract is confirmed.** Per integrity rule SB-1.

---

## Stage 2 — Analytical Passes

### Purpose

Six analytical passes conducted against the clean, confirmed extract from Stage 1. Each pass has a defined scope, a defined set of database writes, and a defined close procedure. No pass begins until the previous pass's database write is confirmed.

Every pass is governed by the cross-registry vision discipline in Section 2.0a. SD pointers are raised throughout all passes — not accumulated for Pass 6.

---

### Pass 1 — Meaning and Semantic Range

**Scope:** The word's meaning, semantic range, sense structure, and etymological grounding. The range of what this word means across its corpus — not just its primary gloss.

**What to read:** All terms in the extract (OWNER and XREF). All verse context groups and their descriptions. All anchor verses per group. Lexical data where available in the extract.

**What to produce:**

For each meaningful semantic unit (typically per root family or per major sense cluster):

1. State the core meaning and semantic range — grounded in the verse evidence.
2. Note any terms whose meaning boundary raises a cross-registry question (→ SD pointer candidate).
3. Note any terms whose `evidential_status` is not yet set — this pass informs Pass 1's contribution to the evidential status decisions.
4. Prior-phase findings with `finding_type` in (MEANING_OBSERVATION, ETYMOLOGY, ROOT_FINDING, TERM_BEHAVIOUR): review each against the extract. Disposition (confirm / correct / deepen / convert to SD_POINTER / set aside) and record in observations log.

**Cross-registry vision questions for Pass 1:**
- Does this word's semantic range overlap with another registry's vocabulary in a way that requires cross-registry investigation?
- Does the root etymology reveal a connection to another inner-being characteristic?
- Does any sense cluster describe an inner-being dynamic that names or implies a word in another registry?

**Type (b) write at pass close:**

Write findings to `wa_session_b_findings`:
- `finding_type = MEANING_OBSERVATION` — one finding per major semantic unit or sense distinction
- `finding_type = ETYMOLOGY` — where root etymology adds analytical value
- `finding_type = ROOT_FINDING` — where a root family observation has cross-registry significance
- `pass_ref = 'Session B Pass 1'`
- `study_segment` — assign to the appropriate word study or brief segment per the controlled vocabulary
- Entity links via `wa_finding_entity_links` — link each finding to the relevant term(s), group(s), or root family

Update `evidential_status` on `wa_term_inventory` for terms where Pass 1 provides sufficient basis for a classification. Use the controlled vocabulary: confirmed / plausible / uncertain / instrumental / relational_only.

Write any SD pointers raised during this pass to the observations log (persisted in Section 2.2).

Request CC to apply the pass close patch. Confirm before proceeding to Pass 2.

---

### Pass 2 — Divine Dimension

**Scope:** The word's divine dimension — where God is subject, object, or participant. How God's involvement shapes or redefines the inner-being characteristic. The theological depth of the word.

**What to read:** All verses where `god_as_subject` may apply — do not rely on the field value (per GR-DATA-005); read the verses and assess directly. All verse context groups in the Theological/Divine-Human dimension (where assigned). Anchor verses for divine involvement patterns.

**What to produce:**

1. Assess each term's `god_as_subject` field value against the verse evidence. Correct the field where the current value is wrong — this is a Type (a) correction noted for the pass close patch.
2. Identify the divine involvement pattern: where God enacts, receives, or transforms this inner-being characteristic.
3. Note the theological depth: eschatological usage, wisdom literature concentration, covenantal dimension.
4. Prior-phase findings with `finding_type = THEOLOGICAL_NOTE`: review and disposition.

**Cross-registry vision questions for Pass 2:**
- Does God's involvement here parallel his involvement in another registry — suggesting a divine-human connection pattern?
- Does the eschatological usage create a link to another inner-being characteristic in eschatological contexts?
- Does the covenantal dimension of this word connect it structurally to another covenantal vocabulary registry?

**Type (b) write at pass close:**

Write findings to `wa_session_b_findings`:
- `finding_type = THEOLOGICAL_NOTE` — divine involvement pattern, eschatological dimension, covenantal grounding
- `pass_ref = 'Session B Pass 2'`
- `study_segment = 'brief_s3_divine_dimension'` or relevant word study segment
- Entity links to relevant terms, verses, groups

Update `god_as_subject` field corrections via Type (a) note in the patch (if any corrections identified).

Write SD pointers to observations log. Confirm pass close patch before Pass 3.

---

### Pass 3 — Verse Annotations

**Scope:** A structured analytical annotation for every anchor verse in the extract. Each annotation is 3–6 sentences stating what this verse contributes that a plain reading does not surface.

This pass is the primary pass for cross-registry observation. Every anchor verse is read against all five standing questions in Section 2.0a before the annotation is written.

**What to read:** Every anchor verse in the extract — one at a time. The group description for context. Relevant terms active in the verse.

**What to produce:**

For each anchor verse:
1. Read the verse against all five cross-registry vision questions.
2. Write a 3–6 sentence annotation: what this verse reveals about the inner-being characteristic, what it contributes beyond the group description, and any cross-registry observations.
3. If the verse raises an SD pointer — write it to the observations log immediately.

Prior-phase findings with `finding_type = VERSE_PATTERN` or `VERSE_ANNOTATION`: review against the current verse reading. Disposition and record.

**Type (b) write at pass close:**

Write findings to `wa_session_b_findings`:
- `finding_type = VERSE_ANNOTATION` — one finding per anchor verse
- `finding_type = VERSE_PATTERN` — where a pattern across multiple verses is identified
- `pass_ref = 'Session B Pass 3'`
- `study_segment = 'word_study_s3_verses'` for verse annotations; `'brief_s2_meaning_findings'` for patterns
- Entity links: each VERSE_ANNOTATION finding links via `entity_type = verse` to the `verse_context.id`

Confirm pass close patch before Pass 4.

---

### Pass 4 — Somatic Evidence and Spirit-Soul-Body Classification

**Scope:** The word's somatic signature — its connection to bodily organs, physical processes, and physical expressions of the inner state. The provisional spirit-soul-body classification.

**What to read:** All terms with `somatic_link` or SOMATIC_INNER_LINK flags — verify each against the verse evidence per GR-DATA-005. All verse context groups in the Somatic/Embodied dimension (where assigned). Anchor verses for bodily vocabulary.

**What to produce:**

1. For each somatic term or somatic verse: identify the bodily part or process named, what inner state it expresses or produces, and the direction of the connection (inner state → body, or body → inner state).
2. Assess the `somatic_link` field value on each term against the verse evidence. Correct where wrong — Type (a) note.
3. Produce the provisional spirit-soul-body classification for the registry: where does this characteristic primarily operate? Spirit / Soul / Body / Interface. State the evidence basis.
4. Prior-phase findings with `finding_type = SOMATIC_EVIDENCE` or `SPIRIT_SOUL_BODY`: review and disposition.

**Cross-registry vision questions for Pass 4:**
- Does the somatic signature of this word share body-part vocabulary with another registry?
- Does the spirit-soul-body classification position this word at an interface that another registry also occupies?
- Does the direction of somatic connection (inward vs outward expression) align with or contrast a pattern in another registry?

**Type (b) write at pass close:**

Write findings to `wa_session_b_findings`:
- `finding_type = SOMATIC_EVIDENCE` — per somatic term or somatic verse pattern
- `finding_type = SPIRIT_SOUL_BODY` — the provisional classification with reasoning
- `pass_ref = 'Session B Pass 4'`
- `study_segment = 'brief_s4_somatic_signature'` and `'brief_s5_spirit_soul_body'`
- Entity links to relevant terms, verses, groups

Update `somatic_link` field corrections via Type (a) note in the patch (if any). Update `evidential_status` for terms where Pass 4 resolves remaining uncertainty.

Confirm pass close patch before Pass 5.

---

### Pass 5 — Language Accuracy

**Scope:** Verification that the analytical language used in prior-phase findings and the extract accurately represents what the Hebrew and Greek terms actually say. This pass challenges imprecision, over-claim, and translation drift.

**What to read:** All active findings in `wa_session_b_findings` for this registry with `delete_flag = 0`. The group descriptions. The extract's lexical data.

**What to examine:**

1. **Overstated claims:** Does any finding assert more than the evidence supports? Note and correct.
2. **Translation dependency:** Does any finding depend on a specific English translation rather than the underlying term? If so, ground it in the term.
3. **Anachronistic framing:** Does any finding project modern psychological categories onto ancient vocabulary? Note and correct.
4. **Group description accuracy:** Does any group description use language that is more specific than the verse evidence warrants? Note — this may trigger a group description correction directive.
5. **Evidential status accuracy:** Does the `evidential_status` assigned in Passes 1–4 accurately reflect the evidence? Note any that require revision.

Prior-phase findings with `finding_type = SESSION_C_CORRECTION`: these are corrections raised against the word study. Review each against the current extract. Confirm, update, or set aside.

**Type (b) write at pass close:**

Language corrections produce supersession writes to `wa_session_b_findings`:
- Write a corrected finding with the accurate language
- Set `delete_flag = 1` on the original; set `superseded_by_id` to the new finding's id
- `pass_ref = 'Session B Pass 5'` on both the new finding and the obsolescence record

Group description corrections: produce a CC directive specifying the corrected description text for the `verse_context_group` row.

Confirm pass close patch before Pass 6.

---

### Pass 6 — Correlation Audit and Connection Verification

**Scope:** The word's confirmed cross-registry connections — verified against correlation signals. Every connection that Session C will name must be confirmed here. Every SD pointer from all prior passes is reviewed and finalised.

**What to read:** The correlation data section of the extract — all correlation signals for this registry. All SD pointers accumulated in the observations log across Passes 1–5.

**What to produce:**

1. For each correlation signal: identify the connected registry and the signal type. Assess whether the signal is strong enough to name as a confirmed connection. State the evidence.
2. For each confirmed connection: characterise its nature from the data — what specific data creates this connection, what the connection reveals, and what the open question is for Session D.
3. For each inferential connection (not confirmed by signal): label it explicitly as inferential. State what correlation signal would be needed to confirm it.
4. Review all SD pointers from the observations log. Confirm each is correctly scoped: does it describe a genuine cross-registry question, or has it been overtaken by the analysis? Refine wording where needed.

Per integrity rule SB-7: Section 5 of the word study must not contain a confirmed connection without correlation signal support. Per integrity rule SB-8: Section 5 must not omit a connection that is supported by a correlation signal. Pass 6 is the verification gate for both rules.

**Type (b) write at pass close:**

Write findings to `wa_session_b_findings`:
- `finding_type = CROSS_REGISTRY` — one finding per confirmed connection, characterising the nature and evidence
- `pass_ref = 'Session B Pass 6'`
- `study_segment = 'word_study_s5_connections'` or `'brief_s7_correlation_connections'`
- Entity links: `entity_type = cross_registry` pointing to the relevant `wa_session_research_flags.id` (the SD_POINTER row for this connection)

Update `evidential_status` for any remaining terms not yet classified.

SD pointers finalised in observations log — ready for Section 2.2 persistence.

Confirm pass close patch. Stage 2 is complete when all six pass-close patches are confirmed.

---

## Section 2.1 — Analytical Brief

The Analytical Brief is a structured internal document produced after all six passes are complete and all pass-close patches are confirmed. It is a dual-purpose handoff document:

**To Session C:** confirms that the database contains all required analytical content for word study production. Session C reads this brief to understand what the database contains, not to receive the analysis itself.

**To Session D:** provides the structured SD pointer summary — the cross-registry connections identified during this analysis, with their evidence basis and the questions they raise for synthesis.

**The Analytical Brief is not a mini word study.** It does not narrate the analysis. It confirms database readiness and summarises the forward-looking picture.

**Structure:**

| Section | Content |
|---------|---------|
| Brief Section 1: Registry state | Registry [nnn] word, session_b_status, extract version, date |
| Brief Section 2: Meaning findings | Count of active MEANING_OBSERVATION, ETYMOLOGY, ROOT_FINDING findings. Summary of primary sense structure in one paragraph. |
| Brief Section 3: Divine dimension | Count of THEOLOGICAL_NOTE findings. Summary of divine involvement pattern in two sentences. |
| Brief Section 4: Somatic signature | Count of SOMATIC_EVIDENCE findings. Somatic pattern summary. SPIRIT_SOUL_BODY classification confirmed. |
| Brief Section 5: Spirit-soul-body classification | Classification stated with evidence summary. |
| Brief Section 6: Verse annotations | Count of VERSE_ANNOTATION findings. Count of anchor verses covered. |
| Brief Section 7: Correlation connections | Count of confirmed connections. List: [registry] — [connection type] — [signal]. |
| Brief Section 8: Cross-word questions | SD pointer count. List of SD pointers with flag_label, target registry, and one-sentence summary of the question. |
| Brief Section 9: Open items | Any items that could not be resolved in Session B and are being carried to Session D. None is the expected state. |

**Filename:** `wa-[nnn]-[word]-sessionb-brief-v1-[date].md`

---

## Section 2.2 — SD Pointer Persistence

SD Pointer Persistence is a mandatory step between the Analytical Brief and Stage 3. Stage 3 does not begin until this step is confirmed complete. Per integrity rule SB-14.

**Purpose:** Persist all SD pointers raised during Stage 2 to `wa_session_research_flags` as `SD_POINTER` records. The SD pointers exist in the observations log; they do not exist in the database until this step executes.

**Procedure:**

1. Compile all SD pointers from the observations log. Count them. Record in observations log: `SD pointer count from observations log: [n].`
2. Construct the SD pointer patch — one `SD_POINTER` record per pointer:
   - `flag_code = 'SD_POINTER'`
   - `flag_label = '[nnn]-SD[seq]'` — sequential within this registry
   - `registry_id = [nnn]`
   - `cross_registry_id` — the target registry id where known; NULL if the pointer is about a pattern rather than a specific registry
   - `strongs_reference` — the connecting term(s) where specific
   - `priority` — HIGH / MEDIUM / LOW based on analytical significance
   - `session_target = 'D'`
   - `description` — the full text of the pointer as recorded in the observations log
   - `raised_date` — today's date
   - `resolved = 0`
3. Submit to CC as `PATCH-[YYYYMMDD]-[nnn]-SDPOINTERS-V1.json`. Wait for confirmation.
4. After confirmation, request from CC: return count of `SD_POINTER` rows in `wa_session_research_flags` for registry [nnn].
5. Compare database count against observations log count.
   - Match → record: `SD pointer count verified: [n] in database = [n] in observations log.` Proceed to Stage 3.
   - Mismatch → STOP. Identify missing pointers. Produce supplementary patch. Re-check before proceeding. Per integrity rule SB-15.

---

## Stage 3 — Closure

### Purpose

Stage 3 verifies that the database is complete, correct, and ready for Session C. It runs a structured Closure Checklist against a fresh extract, applies corrective action where needed, and produces the closing patch that advances `session_b_status` to `Analysis Complete`.

---

### Step 3.1 — Fresh Extract

Request from CC: re-export the complete word data for registry [nnn] and return the new version identifier. This extract is the source for the Closure Checklist — it must reflect all Stage 1 and Stage 2 patches.

Record: `Closure extract confirmed: [filename] — version [n] — exported [date].`

---

### Step 3.2 — Closure Checklist

Run the following checklist against the fresh extract. Every item must pass before the closing patch is produced. Record the result of each check in the observations log.

**Domain A — Data completeness**

| Check | Pass condition |
|-------|---------------|
| All OWNER terms have `evidential_status` set | No NULL values |
| All OWNER terms have `status` set in `mti_terms` | No NULL values on active terms |
| `session_b_status` is not yet `Analysis Complete` | It should still be at the pre-close state |
| `verse_context_status = Complete` | Required |
| All dimension index groups at `CLAUDE_AI` or `RESEARCHER` confidence | No `AUTOMATED` remaining |
| `dominant_subject` set on all dimension index rows | No NULL values |

**Domain B — Findings completeness**

| Check | Pass condition |
|-------|---------------|
| At least one active MEANING_OBSERVATION finding | Count > 0 |
| SPIRIT_SOUL_BODY finding present | Count = 1 for this registry |
| All anchor verses have a VERSE_ANNOTATION finding | Count of VERSE_ANNOTATION = count of anchor verses |
| No `thin_evidence = 1` findings unresolved | All thin findings have been dispositioned |
| No prior-phase findings with `delete_flag = 0` and no `pass_ref` | All prior-phase findings reviewed |

**Domain C — Flag resolution**

| Check | Pass condition |
|-------|---------------|
| Zero `wa_session_research_flags` rows for this registry with `session_target = 'B'` and `resolved = 0` | Hard gate — per integrity rule SB-18 |
| SD pointer count in database matches observations log count | Hard gate — per integrity rule SB-15 |
| All `wa_term_phase2_flags` disposition recorded in observations log | Confirmed, rejected, or irrelevant noted for every flag |

**Domain D — Entity links**

| Check | Pass condition |
|-------|---------------|
| Every active finding in `wa_session_b_findings` has at least one row in `wa_finding_entity_links` | No orphan findings |

**Domain E — Analytical Brief**

| Check | Pass condition |
|-------|---------------|
| Analytical Brief produced and available for download | File exists |
| SD pointer count in Brief Section 8 matches database count | Counts match |
| Section 5 connection count in Brief Section 7 is consistent with CROSS_REGISTRY findings | Counts consistent |

---

### Step 3.3 — Corrective Action Loop

If any checklist item fails:

1. Identify the specific gap.
2. Determine the corrective action: field patch, new finding, SD pointer supplementary patch, directive to CC.
3. Apply the correction. Confirm via CC.
4. Re-run only the failed checklist domain — not the full checklist.
5. If the corrective action cannot be resolved within Session B (e.g. it requires a full sub-process re-run, a new word registration, or a researcher decision): raise a RESEARCHER_DECISION item per GR-RD-002 and record the open item in the Analytical Brief Section 9.

The corrective action loop repeats until the checklist is clean or all remaining items are formally escalated as open items with researcher-approved dispositions.

---

### Step 3.4 — Closing Patch

When the Closure Checklist is clean:

Produce the closing patch:
- `session_b_status = 'Analysis Complete'`
- `registry_note` updated with date and brief close summary

Submit as `PATCH-[YYYYMMDD]-[nnn]-ANALYSIS-V1.json`. Wait for CC confirmation.

Record in observations log: `Closing patch confirmed. session_b_status = Analysis Complete. Registry [nnn] [word] Session B complete.`

---

### Step 3.5 — Handoff Signal

After the closing patch is confirmed:

State the following as the session's formal handoff:

```
SESSION B COMPLETE — Registry [nnn] ([word])
Date: [date]
Extract version at close: [version]
Stage 1: COMPLETE — [n] Type (a) patches applied
Stage 2: COMPLETE — 6 passes, [n] findings written, [n] SD pointers raised
Section 2.2: COMPLETE — [n] SD_POINTER records confirmed in database
Stage 3: COMPLETE — Closure Checklist clean; closing patch applied

Outputs confirmed:
  [ ] Observations log: wa-[nnn]-[word]-sessionb-observations-v[n]-[date].md
  [ ] Session log: wa-[nnn]-[word]-sessionb-sessionlog-v[n]-[date].md
  [ ] Analytical Brief: wa-[nnn]-[word]-sessionb-brief-v1-[date].md
  [ ] SD pointer patch: PATCH-[YYYYMMDD]-[nnn]-SDPOINTERS-V1.json (applied)
  [ ] Closing patch: PATCH-[YYYYMMDD]-[nnn]-ANALYSIS-V1.json (applied)

Session C: OPEN — database ready. Session C may proceed.
Session D: NOTIFIED — [n] SD pointers awaiting synthesis.
```

---

## Analytical Principles

**Cross-registry vision is always active.** Per Section 2.0a. Every analytical act in Stage 2 includes the question: what does this data tell me about something beyond this word? SD pointers are raised at the moment of discovery — not accumulated for Pass 6.

**The data is authoritative.** Per GR-PROC-002. Every finding must be traceable to a specific verse record, term entry, lexical source, or correlation signal in the extract.

**Emergence, not imposition.** Per GR-PROG-008. Classifications emerge from the evidence. No classification is assigned in advance.

**Inferential is not confirmed.** Per GR-PROG-009. Label inferential connections accurately. Do not upgrade them.

**Phase 2 flags are advisory, not evidential.** Review them against the verse evidence. Do not accept them without verification. Do not dismiss them without reading the verses.

**Somatic evidence is observational before it is interpretive.** Record what the verses say about bodily involvement before interpreting what it means.

**CLAUDE_AI confidence means critical thinking applied.** Not tick-box acceptance. Ask: is there a hidden story? Is there something this data does not say that it should? Is there a contradiction that has not been resolved?

**Session C documents are not sacred.** Session B exists to correct, deepen, and complete them. An accurate database that enables a corrected word study is more valuable than an accessible document that contains errors.

**Researcher decision items are a last resort.** Per GR-RD-001. Before raising any item, exhaust analytical resources: read the instruction, check the rules, request the data from CC, attempt a resolution. A question that could be answered by reading the instruction is not a researcher decision item.

---

## Integrity Rules

The following rules apply in addition to programme-wide rules in the global rules file.

| Rule | Requirement |
|------|-------------|
| SB-1 | Stage 2 does not begin until Stage 1 is fully complete and the fresh extract is confirmed |
| SB-2 | Stage 3 does not begin until Stage 2 is fully complete, the Analytical Brief is written, and Section 2.2 SD pointer persistence is confirmed |
| SB-4 | No dimension group may reach `CLAUDE_AI` confidence without the Dimension Review sub-process completing Phase B and Phase C for that group |
| SB-7 | Section 5 of the word study must not contain a confirmed connection that is not supported by at least one correlation signal |
| SB-8 | Section 5 must not omit a connection that is supported by a correlation signal |
| SB-9 | Cross-word synthesis conclusions are not permitted in Session B outputs — questions only |
| SB-10 | `dominant_subject` must be assigned for every dimension index group before Stage 2 begins |
| SB-11 | SD pointers are raised at the moment of discovery during any pass — not accumulated for Pass 6. Per GR-OBS-001 |
| SB-12 | Every anchor verse is read against all five standing questions in Section 2.0a before its pass closes |
| SB-13 | Pass 6 must not be the only pass that generates SD pointers — if it is, Stage 2 must be repeated from Pass 1 |
| SB-14 | The SD pointer patch (Section 2.2) is a mandatory output — Stage 3 does not begin without it confirmed by CC |
| SB-15 | Stage 3 does not begin without the SD pointer count check (Section 2.2) passing — database count must equal observations log count |
| SB-16 | The closing patch (Step 3.4) is a mandatory final output — the session does not close without it confirmed by CC |
| SB-17 | The session does not close without all five mandatory outputs confirmed: observations log, session log, analytical brief, SD pointer patch (applied), closing patch (applied) |
| SB-18 | Zero open `wa_session_research_flags` rows for this registry with `session_target = 'B'` and `resolved = 0` at session close — hard gate |
| SB-19 | No RESEARCHER_DECISION item may be raised without evidence that GR-RD-001 steps 1–6 have been completed. Items raised without this evidence are non-compliant and will be rejected |

---

## Naming Conventions

All filenames follow GR-FILE-001 through GR-FILE-009 (lowercase, compact date YYYYMMDD, version numbered).

| Output | Pattern | Example |
|--------|---------|---------|
| Observations log | `wa-[nnn]-[word]-sessionb-observations-v[n]-[date].md` | `wa-023-compassion-sessionb-observations-v1-20260415.md` |
| Session log | `wa-[nnn]-[word]-sessionb-sessionlog-v[n]-[date].md` | `wa-023-compassion-sessionb-sessionlog-v1-20260415.md` |
| Analytical Brief | `wa-[nnn]-[word]-sessionb-brief-v[n]-[date].md` | `wa-023-compassion-sessionb-brief-v1-20260415.md` |
| SD pointer patch | `PATCH-[YYYYMMDD]-[nnn]-SDPOINTERS-V1.json` | `PATCH-20260415-023-SDPOINTERS-V1.json` |
| Type (a) patch | `PATCH-[YYYYMMDD]-[nnn]-PREANALYSIS-V[n].json` | `PATCH-20260415-023-PREANALYSIS-V1.json` |
| Closing patch | `PATCH-[YYYYMMDD]-[nnn]-ANALYSIS-V1.json` | `PATCH-20260415-023-ANALYSIS-V1.json` |

---

*End of wa-global-sessionb-instruction-v5.0-20260415.md*
*Supersedes wa-sessionb-instruction-v4.8-20260414.md*
*Governed by wa-global-general-rules-v2.2-20260415.json*
