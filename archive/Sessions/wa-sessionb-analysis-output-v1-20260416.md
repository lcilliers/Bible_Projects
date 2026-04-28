# WA — Session B: Analysis Output Instruction
**Framework B — Soul Word Analysis Programme
Analysis Output Instruction — Comprehensive Analysis, Q&A Partitioning, and Analytic Word Output
Version 1.0 | 20260416 | Status: Draft — change log removed; takes effect from v1.1**

| **Document** | **Value** |
|---|---|
| Filename | wa-sessionb-analysis-output-v1-20260416.md |
| Supersedes | wa-global-sessionb-instruction-v5_0-20260415.md (Stage 2 and Stage 3) |
| Companion documents | wa-global-general-rules-v[current].json │ wa-sessionb-cc-instructions-v[current].md │ wa-patch-specification-v[current].md │ wa-global-sessionc-prose-rule-v[current].md |
| Inputs | Stage 1 Completion Record; verified clean extract (version from Completion Record); master catalogue |
| Outputs | Observations log; Q&A log; Type (b) patches; SD pointer patch; analytic word output; closing patch; handoff signal |
| Claude AI role | Comprehensive reading; observations recording; Q&A production; analytic chapter writing; closure verification |
| Claude Code role | Type (b) patch application; SD pointer persistence; closing patch application; extract re-export |
| Prerequisite | wa-sessionb-analysis-readiness-v[current].md Stage 1 complete; Stage 1 Completion Record produced |

---

## Governing Rules

This instruction is governed by **wa-global-general-rules-v[current].json**.

Claude AI must confirm the global rules file has been loaded before beginning any work. State aloud: *"Global rules wa-global-general-rules-v[current].json loaded."*

---


## Pipeline Position

```
Analysis Readiness  (wa-sessionb-analysis-readiness-v[current].md)
     └── Stage 1 complete → Stage 1 Completion Record → Stage 2 Readiness Declaration
          │
          ▼
Analysis Output  (this instruction)
     ├── Schema readiness gate
     ├── Stage 2a: Comprehensive analysis → Observations log
     ├── Stage 2b: Q&A partitioning → Q&A log + Type (b) patches
     ├── Stage 2c: Analytic word output → Six chapters
     └── Closure
          ├── Closure checklist
          ├── Corrective action loop
          ├── Closing patch → session_b_status = Analysis Complete
          └── Handoff signal → Session C open; Session D notified
          │
          ▼
Session C  (word study production — reads from database + Stage 2c chapters)
          │
          ▼
Session D  (cross-registry synthesis — reads from database + SD pointers)
```

---

## What to Attach at Session Start

**Required at every session:**
- This instruction file
- Global rules file: `wa-global-general-rules-v[current].json`
- Stage 1 Completion Record — the final section of `wa-[nnn]-[word]-sessionb-observations-v[n]-[date].md` from the Analysis Readiness session. If the full observations log is not available, extract the Completion Record section. **If not present: stop — Stage 2a cannot begin without it.**
- The verified clean extract: `wa-[nnn]-[word]-complete-[date].json` (version confirmed in Stage 1 Completion Record)
- CC instructions: `wa-sessionb-cc-instructions-v[current].md`

**Required from Stage 2b onward:**
- Master catalogue: the `observation_question_catalogue` section of the extract, or the separate catalogue JSON
- Stage 2a observations log (fixed — confirmed complete)

**Required from Stage 2c onward:**
- Stage 2b Q&A log (confirmed complete)
- Session C prose rule: `wa-global-sessionc-prose-rule-v[current].md` — load and read before writing any chapter

Do not load more data into the working session than the current stage requires.

---

## Governing Disciplines

These disciplines apply without exception across all stages, all sessions.

**Step-by-step.** Per GR-PROC-001. Each stage and each step within it is completed and confirmed before the next begins.

**Write on discovery.** Per GR-OBS-001 (non-waivable). Every observation, SD pointer, decision, and open question is written to the observations log at the moment it is determined. Nothing is accumulated in memory.

**All observations return to the database.** Per GR-OBS-006. Every analytical observation produced in Stage 2a must be addressed in Stage 2b and any that produce structured findings must be persisted before closure. Session C and Session D read from the database only.

**Data is authoritative.** Per GR-PROC-002. Work strictly from what is in the clean extract. Do not import general knowledge to fill gaps.

**All changes through patches or directives.** Per GR-PROC-003. Type (b) patches record analytical findings. Both require researcher approval per GR-PROC-004.

**Two types of database writes.** Type (a) — data quality corrections (Stage 1 only). Type (b) — analytical findings (Stage 2b close). Neither substitutes for the other.

**No DB state assumptions.** Per GR-DB-001. Claude AI never assumes the current state of the database.

**Cross-registry vision is always active.** Per GR-PROG-002. Every piece of data read in Stage 2a is read twice: once for what it says about this word, once for what it says about something beyond this word. SD pointers are raised continuously — not accumulated for a final pass. Per integrity rule SB-11.

**Characteristic-perspective grouping model.** Per GR-PROG-006. Every anchor verse is read with its group description as the interpretive lens. The group description names what the characteristic is that the verse is engaging. This is the reading frame — not the verse's general theme.

**Stage 2a is free-form. Stage 2b is structured.** Stage 2a produces observations without imposed structure. Stage 2b produces structured Q&A pairs governed by the catalogue. Do not attempt to structure Stage 2a observations as Q&A pairs during Stage 2a — this conflates two distinct stages and corrupts both.

**Researcher decision items.** Per GR-RD-001 through GR-RD-006. Last resort only. Before raising any item, exhaust analytical resources.

**Session logs at every breakpoint.** Per GR-PROC-006.

---

## Schema Readiness Gate

Before Stage 2a begins, confirm with CC that the following database conditions are met. If any condition fails, resolve before proceeding. This gate runs once per word — not at every session start.

| Condition | Check | Fail action |
|-----------|-------|------------|
| `wa_obs_question_catalogue` has ≥ 194 rows | CC count query | Raise with researcher — catalogue may be stale |
| `wa_finding_catalogue_links` table exists | CC schema check | Raise CC directive — schema gap |
| `wa_session_b_findings.status` column exists | CC schema check | Raise CC directive — schema gap |
| `wa_session_b_findings.term_id` column exists | CC schema check | Raise CC directive — schema gap |
| Registry-specific catalogue questions present | Count from `observation_question_catalogue` section of extract | If 0: word-specific questions not yet indexed — raise with researcher |

Record in observations log: `Schema readiness gate: [n] conditions checked. All pass / [n] fail — [detail].`

---

## Stage 2a — Comprehensive Analysis

### Purpose

Stage 2a produces a comprehensive free-form narrative of everything the data says about this word. It is the analytical foundation for all subsequent work. It is not structured, not formatted for reading, and not organised by any external framework. It is the full working out of what the clean extract contains.

Stage 2a is complete when every element of the extract has been read, everything the data says has been recorded, and the observations log has been downloaded and confirmed. After sign-off, the observations log is fixed — it does not change in Stage 2b or 2c.

Stage 2a does not produce database writes. It does not produce Q&A pairs. It does not produce reader-facing prose. Those are Stage 2b and 2c.

---

### Stage 2a Outputs

| Output | Filename | When produced | Purpose |
|--------|----------|---------------|---------|
| Observations log | `wa-[nnn]-[word]-sessionb-observations-v[n]-[date].md` | Initiated at Stage 2a start; written continuously | Primary analytical record for this word. Fixed after Stage 2a sign-off. |
| Session log | `wa-[nnn]-[word]-sessionb-sessionlog-v[n]-[date].md` | At every breakpoint and session end | Handoff document — current position, open items, resume instructions |

---

### Stage 2a Tracking Document Structure

Open the observations log immediately and create these four named sections before reading any data:

```
#### SD Pointer Accumulator
[Empty at start — populated on discovery throughout Stage 2a]

#### RESEARCHER_DECISION Accumulator
[Empty at start — populated when Path 4 items are identified]

#### Path 3 Resolution Notes
[Empty at start — populated as Stage 1 Path 3 items are addressed in verse reading]

#### Stage 2a Progress Record
[Updated at each reading unit sign-off — this is the position marker register]
```

**SD Pointer Accumulator format — each entry:**
```
SD POINTER [seq]: [date]
  Raised during: [reading unit — term/group/verse reference]
  Target registry: [registry no and word, or 'pattern — no specific registry']
  Connecting term/verse: [strongs_number or verse reference]
  Question: [precisely stated cross-registry question]
  Evidence basis: [what in the extract triggers this pointer]
  Priority: HIGH / MEDIUM / LOW
```

**Path 3 Resolution format — each entry:**
```
PATH 3 RESOLUTION [seq]: [date]
  Stage 1 Path 3 note: [original note reference]
  Field: [table.field on term/group]
  Stage 1 value: [what was recorded as provisional]
  Verse evidence: [verse reference and what it shows]
  Resolution: CONFIRMED [value] / CORRECTED TO [value] / REMAINS UNCERTAIN
  Patch required: YES — [correction] / NO
```

**Stage 2a Progress Record format:**
```
[Reading unit] COMPLETE: [date]
  Units covered: [what was read]
  Observations written: [n entries in this session]
  SD pointers raised: [n]
  Path 3 items resolved: [n]
```

---

### Session Start Protocol

Apply at the start of every Stage 2a session.

**S1 — Confirm global rules loaded.**

**S2 — Read the Stage 1 Completion Record in full.**
If not attached or present: stop immediately. Stage 2a cannot begin without the Stage 1 Completion Record.
Extract and record:
- Extract version (authoritative reference for this word)
- All seven domain pass confirmations
- Path 3 notes count and list
- SD pointer count already in database

**S3 — Confirm extract currency from registry status.**
Read `registry.session_b_status` in the attached extract. If `session_b_status = 'Pre-Analysis Complete'`: Stage 1 is confirmed complete and this is the correct extract. Confirm `meta.export_version` matches the Stage 1 Completion Record. If it matches: PASS. If versions differ or status is not `Pre-Analysis Complete`: stop and raise with researcher.
No CC check needed — the status field written by Stage 1's closing patch is the authoritative confirmation.

**S4 — Establish position from Stage 2a Progress Record.**
Read the Stage 2a Progress Record section of the observations log.

| Last completed entry | Resume from |
|---------------------|-------------|
| No entries | Reading sequence Step 1 — registry overview |
| Correlation signals COMPLETE | Anchor verse reading — first unread group |
| [Group code] COMPLETE | Next group in sequence |
| All groups COMPLETE | Thin-evidence flags |
| Thin-evidence flags COMPLETE | Existing findings review |
| Existing findings COMPLETE | Stage 2a sign-off check |

**S5 — Check SD Pointer Accumulator.**
Note current count. Confirm no pointers were raised but not recorded.

**S6 — State resumption position:**
```
STAGE 2A SESSION: [date]
Resuming from: [reading unit]
Extract version confirmed: [version]
SD pointers accumulated so far: [n]
Path 3 items resolved so far: [n of n]
```

---

### Reading Sequence

Work through the reading units in the order below. Each unit is a defined reading task. Complete each unit fully and record a progress sign-off before moving to the next. Do not skip units. Do not reorder units.

**Unit 1 — Registry overview**

Read: `word_registry` fields — word, cluster, session_b_status, sb_classification, sb_classification_reasoning, description, dimensions, dim_review_version.

Record in observations log:
- The word's assigned cluster and what that cluster covers
- The existing sb_classification and its reasoning — note whether this looks well-founded or provisional
- The dimension(s) assigned — how many, which ones
- Anything in the description or notes field that signals prior analytical decisions worth examining

Stage 2a Progress Record sign-off: `Unit 1 COMPLETE: Registry overview read. [n] observations.`

---

**Unit 2 — XREF terms**

If `statistics.active_xref_term_count = 0`: record `Unit 2 COMPLETE: zero XREF terms.` and proceed immediately to Unit 3.

Otherwise read: all XREF terms in the extract. For each: owning registry, owning word, transliteration, gloss, occurrence count, related words.

Record:
- What vocabulary this registry borrows from other registries and why
- Whether any XREF term's semantic range is likely to complicate this word's own meaning boundary
- Whether any XREF term's owning registry is one with a known connection to this word (from correlation signals — noted but not yet read in detail)

Record in SD Pointer Accumulator if any XREF term raises a cross-registry observation immediately.

Stage 2a Progress Record sign-off: `Unit 2 COMPLETE: [n] XREF terms. [n] observations. [n] SD pointers.`

---

**Unit 3 — OWNER terms: lexical foundation**

Read: for each OWNER term — meaning (full parse), root family, related words, LSJ entry (Greek terms), short definition, transliteration, occurrence count, testament coverage.

Record for each OWNER term:
- Core meaning and semantic range — what does this word mean across its attested uses?
- Root family: what is the etymological grounding? Does the root carry a concrete physical or relational image?
- Related words: what cognates does this term have? Do they suggest a semantic family that is broader than the registry's scope?
- For Hebrew terms: is there a cognate in Aramaic or a cross-testament development?
- For Greek terms: is there a LXX/OT background that shapes NT usage? What does the LSJ record? **If `lsj_parse = NULL`: note as data gap; meaning work proceeds from `step_search_gloss`, `short_def_mounce`, and related words only.**
- Sense structure: how many distinct senses does this term carry? Is the meaning unified or does it span significantly different domains? **If `meaning_parse.senses` is empty AND `meaning` field is NULL: the term has no structured lexical data. Record from `step_search_gloss`, `word_analysis_gloss`, `short_def_mounce`, related words. Note as data gap and proceed — Stage 2a continues from gloss and verse evidence.**

Record Path 3 Resolution notes for any `evidential_status` items from Stage 1 that can be addressed from lexical data alone.

Stage 2a Progress Record sign-off: `Unit 3 COMPLETE: [n] OWNER terms. [n] observations. [n] SD pointers.`

---

**Unit 4 — Verse context groups: characteristic-perspective landscape**

Read: all verse context groups — group code, context description, dimension assignment, dimension confidence, dominant subject, anchor count, related count, set-aside count.

Do not read anchor verses yet. Read group descriptions only.

Record:
- The full landscape of inner-being characteristics this word engages across its corpus
- Whether the dimensions assigned are consistent with the group descriptions
- Whether any group description is ambiguous, overstated, or potentially miscategorised
- The distribution of dominant subjects (God / Human / Mixed / Community) — what pattern does this suggest?
- Any groups that stand out as analytically significant — the most dense, the most theologically loaded, the most unexpected
- Whether the group structure clusters naturally — are there two or three major axes that the groups fall along?

Note: group descriptions are the authoritative statement of what each characteristic is. Stage 2a takes these as given unless a group description is clearly inconsistent with the verse evidence (which will emerge in Unit 5).

Stage 2a Progress Record sign-off: `Unit 4 COMPLETE: [n] groups across [n] terms. [n] observations. [n] SD pointers.`

---

**Unit 5 — Correlation signals**

Read: all correlation signals in the extract — ranked pairs, xref sharing, verse co-occurrence, shared anchor verses.

If `correlation_signals.slice_counts.ranked_pairs = 0` and all other signal counts are 0: record `Unit 5 COMPLETE: zero ranked correlation signals. [n] shared anchor verses present. Cross-registry connections will be identified through verse evidence in Unit 7.` Proceed to Unit 6.

Otherwise record:
- The top-ranked connections and what drives their score (xref sharing, verse co-occurrence, shared anchors)
- Any connections that are surprising given the word's cluster assignment
- Any connections that are absent but expected given the word's meaning
- For each shared anchor verse pair: note which verses are shared with which registry — these are candidates for SD pointers

This unit is read before anchor verse reading so that the cross-registry lens is calibrated before the verse-by-verse work begins.

Stage 2a Progress Record sign-off: `Unit 5 COMPLETE: [n] correlation pairs reviewed. [n] observations. [n] SD pointers.`

---

**Unit 6 — Existing SD pointers and findings**

Read: all existing SD_POINTER records for this registry from `session_research_flags` section of extract. All existing `session_b_findings` for this registry.

For each existing SD pointer:
- Note the question, target registry, and priority
- Note whether it remains open or has been addressed by prior analysis
- Note whether Stage 2a anchor verse reading should investigate it further

For each existing finding:
- These are input material — prior-session hypotheses, not confirmed analytical facts
- Note the finding type, content, and whether it appears well-grounded or contestable
- These will be revisited during anchor verse reading

Do not accept or reject existing findings here. Record impressions only.

**SD pointer naming check:** Verify each existing SD pointer `flag_label` follows `[nnn]-SD[seq]` with zero-padded three-digit registry number (e.g. `062-SD001` not `62-SD001`). Any inconsistency: add to patch accumulator — update `wa_session_research_flags.flag_label`.

Stage 2a Progress Record sign-off: `Unit 6 COMPLETE: [n] existing SD pointers. [n] existing findings reviewed. [n] observations.`

---

**Unit 7 — Anchor verse reading**

This is the primary analytical unit. Read every anchor verse across all groups for all OWNER terms. Work group by group, term by term.

**For each group:**

1. Re-read the group description. Hold it as the interpretive lens for the anchor verses in this group.
2. Note the group's dimension and dominant subject — these shape what to look for.

**For each anchor verse within the group:**

Apply all five cross-registry vision questions:
1. Does this verse name or imply an inner-being characteristic that appears in another registry?
2. Does the term's behaviour here differ from its primary registry — suggesting a cross-registry boundary question?
3. Does the grammatical form (causative, reflexive, passive) create a causal or relational connection to another inner-being state?
4. Does the verse place two or more inner-being states in structural relationship (sequence, causation, contrast, parallel)?
5. Does the somatic expression here align with a somatic pattern in another registry?

A positive answer to any of these five questions triggers an SD pointer — written immediately to the SD Pointer Accumulator per GR-OBS-001.

Then record the verse observation: what does this verse contribute to understanding this inner-being characteristic that the group description alone does not capture? What does it show about how the characteristic operates, what it requires, what it produces, who it involves?

Address Path 3 notes from Stage 1 as they are encountered. When a verse addresses a `god_as_subject` or `somatic_link` Path 3 item, record the resolution in the Path 3 Resolution Notes section immediately.

**Group sign-off after all anchor verses are read:**
```
Group [code] COMPLETE: [date]
  Anchor verses read: [n]
  Key observation: [one sentence — what this group contributes to the word's portrait]
  SD pointers raised: [n]
  Path 3 items resolved in this group: [n]
```

**Terms with all verses set aside:** Before the set-aside review, check whether any active OWNER term has zero groups because all verses were set aside. Record `[strongs] — all [n] verses set aside ([reasons]). No groups formed. Term contributes root vocabulary context only.` This is the correct Verse Context outcome for physically-grounded vocabulary — not a data gap.

**Set-aside verses:** After the anchor verses for each group, review the set-aside verses. Confirm the set-aside reason is plausible. For verses with NULL set-aside reason (from Stage 1 IC-06 note): read the verse briefly and record whether the set-aside appears correct. Do not re-classify — record the observation.

**Stage 2a Progress Record sign-off at term close:**
`Term [strongs] anchor verse reading COMPLETE: [n] groups, [n] anchor verses. [n] SD pointers. [n] Path 3 resolutions.`

---

**Unit 8 — Thin-evidence phase2 flags**

Read: all phase2 flags carried forward with `thin_evidence` disposition from Stage 1 Step 1.3a. For each:
- Read the available verses for this term
- Record a disposition: confirmed by limited evidence / remains uncertain / clearly inapplicable
- If confirmed: note the evidence, however thin
- If remains uncertain: note what verse evidence would be needed to resolve it — this may become an SD pointer if it has cross-registry significance

Stage 2a Progress Record sign-off: `Unit 8 COMPLETE: [n] thin-evidence flags reviewed. [n] dispositioned. [n] SD pointers.`

---

**Unit 9 — Existing findings: input material review**

Review all existing findings noted in Unit 6. For each:
- Against the backdrop of everything read in Units 3–8: does this finding appear to be well-grounded, overstated, or in need of correction?
- Note the impression — confirmed / deepened / questioned / set-aside candidate
- Do not write corrected findings here. Stage 2b will handle finding dispositions.

Stage 2a Progress Record sign-off: `Unit 9 COMPLETE: [n] findings reviewed. Confirmed: [n]. Questioned: [n]. Set-aside candidate: [n].`

---

### Stage 2a Sign-Off Checklist

Before declaring Stage 2a complete, confirm all nine units have been completed:

| Unit | Subject | Status |
|------|---------|--------|
| 1 | Registry overview | COMPLETE / not complete |
| 2 | XREF terms | COMPLETE / not complete |
| 3 | OWNER terms: lexical foundation | COMPLETE / not complete |
| 4 | Verse context groups: landscape | COMPLETE / not complete |
| 5 | Correlation signals | COMPLETE / not complete |
| 6 | Existing SD pointers and findings | COMPLETE / not complete |
| 7 | Anchor verse reading — all groups all terms | COMPLETE / not complete |
| 8 | Thin-evidence phase2 flags | COMPLETE / not complete |
| 9 | Existing findings: input material review | COMPLETE / not complete |

All nine must be COMPLETE before the sign-off is recorded.

Additionally confirm:
- All Path 3 notes from Stage 1 have been addressed (count in Completion Record matches count resolved)
- SD Pointer Accumulator is complete — every pointer has all required fields
- Observations log downloaded and confirmed

**Sign-off statement:**
```
STAGE 2A COMPLETE — Registry [nnn] ([word])
Date: [date]
Extract version: [version]
Reading units completed: 9 of 9
Observations log: [filename] — downloaded and confirmed
SD pointers accumulated: [n]
Path 3 notes resolved: [n of n]
Existing findings reviewed: [n]
Anchor verses read: [n] across [n] groups across [n] terms

Observations log is now fixed. Stage 2b may begin.
```

---

### Fallback Protocol — Stage 2a

**Session interrupted mid-unit:** Resume from the last group sign-off or the last unit sign-off recorded in Stage 2a Progress Record. Do not re-read units that have a sign-off. Continue from where the sign-off ends.

**Observation recorded but not fully developed:** If the observations log contains a partial observation (a note with no conclusion), treat it as a starting point — develop it before moving to the next item. Do not skip partial observations.

**Stage 2a sign-off recorded but observations log not downloaded:** Re-download before proceeding to Stage 2b. The fixed observations log is the input to Stage 2b — if it is not confirmed present, Stage 2b cannot begin.

**Path 3 item requires correction:** If a Path 3 item resolves to a field correction (e.g. `god_as_subject` should be 1 but is 0), record the correction needed in the Path 3 Resolution Notes. These corrections are accumulated and applied in a supplementary Type (a) patch before Stage 2b begins — they are data corrections, not Stage 2b findings.

---

### Session Close Protocol — Stage 2a

**C1 — Complete the current group or reach a group boundary.**
Always end Stage 2a sessions at a group sign-off. Do not end a session mid-group if it can be avoided.

**C2 — Verify the four tracking sections are current.**
SD Pointer Accumulator, RESEARCHER_DECISION Accumulator, Path 3 Resolution Notes, Stage 2a Progress Record — all updated.

**C3 — Produce the session log.**
Current position; units completed; outstanding units; SD pointers accumulated; Path 3 items resolved; exact resume instructions.

**C4 — Produce downloads.**
Observations log and session log both available for download before the session closes.

---

## Stage 2b — Q&A Partitioning

### Purpose

Stage 2b converts the free-form observations of Stage 2a into structured Q&A pairs governed by the master catalogue. Each pair consists of a catalogue question and an answer drawn directly from the Stage 2a observations log. The catalogue drives what is asked. Stage 2a provides the evidence. Stage 2b is the bridge between them.

Stage 2b produces all Type (b) database writes for this word. Nothing from Stage 2a reaches the database until Stage 2b applies its patch.

Stage 2b is iterative and multi-session capable. Each session works through a defined batch of questions. Stage 2b is complete when all catalogue questions have a recorded disposition and the Type (b) patch is applied and confirmed.

---

### Stage 2b Inputs

- Stage 2a observations log — fixed, confirmed, downloaded
- Catalogue questions from the `observation_question_catalogue` section of the extract: both registry-specific questions (indexed for this word) and universal questions (scope = 'universal')
- Stage 1 Completion Record (for context — not modified)

**If any Path 3 corrections were identified in Stage 2a** (field corrections arising from verse reading — e.g. `god_as_subject` or `somatic_link`): apply a supplementary Type (a) patch to correct these fields before Stage 2b begins. Request a fresh extract after the patch is confirmed. Stage 2b reads from the corrected extract.

---

### Stage 2b Tracking Documents

The observations log already carries the SD Pointer Accumulator, RD Accumulator, and Progress Record from Stage 2a. Stage 2b adds:

```
#### Stage 2b Q&A Log
[Populated during Stage 2b — one entry per question]

#### Stage 2b Progress Record
[Updated at each question batch sign-off]
```

**Q&A Log entry format:**
```
Q&A [seq]: [date]
  Question code: [catalogue question_code e.g. U-001, L-003]
  Question text: [full question from catalogue]
  Scope: [universal / word-specific]
  Disposition: ANSWERED / PARTIALLY ANSWERED / NOT ANSWERED / NOT APPLICABLE
  Answer: [drawn directly from Stage 2a observations — cite observation by date/section if possible]
  Anchor verses cited: [verse references supporting the answer]
  Finding type: [controlled vocabulary — see below]
  SD pointer link: [SD pointer seq if this answer produces or confirms an SD pointer, else none]
  Stage 2b note: [any qualification on the answer — thin evidence, inferential, pending verification]
```

**Stage 2b Progress Record format:**
```
BATCH [n] COMPLETE: [date]
  Questions processed: [first code] through [last code]
  Answered: [n]. Partially answered: [n]. Not answered: [n]. Not applicable: [n].
  Findings to write: [n]
```

---

### Session Start Protocol — Stage 2b

**S1 — Confirm global rules loaded.**

**S2 — Confirm Stage 2a is signed off and observations log is fixed.**
Read the Stage 2a sign-off statement. If not present: Stage 2b cannot begin.

**S3 — Confirm supplementary Type (a) patch applied if required.**
Check Path 3 Resolution Notes in observations log. If any corrections were flagged: confirm the patch was applied and a fresh extract confirmed before proceeding.

**S4 — Establish position from Stage 2b Progress Record.**
Identify the last completed batch. Resume from the next question in sequence.

**S5 — State resumption position.**

---

### Question Processing

Work through catalogue questions in two passes.

**Pass A — Registry-specific questions (word-specific scope):**
These are questions indexed specifically for this word in `observation_question_catalogue` where `scope = 'word_specific'` or `source_registry_no = [nnn]`.

If `statistics.catalogue_questions_registry = 0`: no word-specific questions have been indexed for this word. Record `Pass A: zero registry-specific questions for registry [nnn].` and proceed directly to Pass B. This is not an error — words newly added to the programme may not yet have word-specific questions authored. Pass B (universal questions) remains fully applicable.

Otherwise process all registry-specific questions first.

**Pass B — Universal questions (universal scope):**
These are questions where `scope = 'universal'`. Process all of these after Pass A.

Within each pass, process questions in `obs_id` order (ascending).

---

**For each question:**

**Step 1 — Read the question:**
State the question code and full text.

**Step 2 — Search Stage 2a for relevant observations:**
Read through the Stage 2a observations log. Identify all observations that bear on this question. Do not generate new analysis — draw only from what Stage 2a contains.

**Step 3 — Assign a disposition:**

| Disposition | Meaning |
|-------------|---------|
| ANSWERED | Stage 2a contains sufficient evidence to give a direct answer. The answer is grounded in named verses or terms. |
| PARTIALLY ANSWERED | Stage 2a contains relevant observations but they are incomplete or contain thin evidence. The answer is qualified. |
| NOT ANSWERED | Stage 2a is silent on this question despite the data being available. Stage 2a must be reopened for this specific item. |
| NOT APPLICABLE | The question does not apply to this word. The data provides no engagement with this question's domain, and it is not an omission — the characteristic simply does not manifest in this way. |

**Critical distinction — NOT ANSWERED vs NOT APPLICABLE:**
NOT ANSWERED means Stage 2a should have addressed this and did not. NOT APPLICABLE means the characteristic genuinely does not engage with this question's domain. Assign NOT APPLICABLE conservatively — default to NOT ANSWERED if uncertain. NOT ANSWERED triggers Stage 2a reopening; NOT APPLICABLE does not.

**Step 4 — Write the Q&A entry:**
For ANSWERED and PARTIALLY ANSWERED: write the full answer in the Q&A Log entry. Draw directly from Stage 2a. Cite anchor verses and observations. Do not introduce new analysis.

For NOT ANSWERED: record in Stage 2b Q&A Log as NOT ANSWERED. Reopen Stage 2a for this specific question — add one targeted reading unit to Stage 2a (Unit 10+, sequentially numbered). Return to Stage 2b after the unit is complete.

For NOT APPLICABLE: record in Q&A Log as NOT APPLICABLE with a one-sentence rationale.

**Step 5 — Assign a finding type:**
Every ANSWERED or PARTIALLY ANSWERED question that produces a new observation (not already in an existing finding) must be assigned a finding type for the Type (b) patch.

| Finding type | Use |
|---|---|
| MEANING_OBSERVATION | Semantic range, sense structure, core meaning |
| ETYMOLOGY | Root etymology, word origin, cognate patterns |
| ROOT_FINDING | Root family observation with cross-registry significance |
| THEOLOGICAL_NOTE | Divine dimension — God as subject, theological depth, covenantal grounding |
| VERSE_ANNOTATION | Per-verse observation — what this verse contributes beyond the group description |
| VERSE_PATTERN | Pattern across multiple verses — structural relationship, repeated motif |
| SOMATIC_EVIDENCE | Bodily part or process named; direction of somatic connection |
| SPIRIT_SOUL_BODY | Spirit-soul-body classification with reasoning |
| SESSION_C_CORRECTION | Language correction to a prior finding or group description |
| CROSS_REGISTRY | Confirmed cross-registry connection with evidence |
| SD_POINTER_LINK | Not a finding type — this is a link to an existing SD pointer, not a new finding |

**Step 6 — Note SD pointer links:**
If the answer confirms, deepens, or resolves an existing SD pointer: note the link in the Q&A entry. If the answer raises a new SD pointer that was not identified in Stage 2a: record it in the SD Pointer Accumulator and note in the Q&A entry.

---

### SD Pointer Review

After all catalogue questions are processed: review the full SD Pointer Accumulator.

For each SD pointer:
1. Is the question precisely stated? If not, refine the wording.
2. Is the target registry identified where possible? If not, note 'pattern — no specific registry.'
3. Is the evidence basis stated? It must reference named observations from Stage 2a.
4. Is the priority appropriate (HIGH / MEDIUM / LOW)? Review against the analytical significance of the question.
5. Is this pointer a duplicate of an existing SD_POINTER record in the database (from prior work)? If so, note the existing record ID — do not duplicate.

Record in Stage 2b Q&A Log: `SD Pointer review complete. [n] pointers confirmed. [n] refined. [n] merged with existing records. [n] new.`

---

### Existing Findings Review

Review all existing findings from `session_b_findings` that were identified in Stage 2a Unit 9 as questioned or set-aside candidates.

For each:
- Against the Stage 2b Q&A pairs: does the existing finding remain accurate?
- If accurate: leave in place. No action.
- If superseded by a more precise Stage 2b finding: mark `delete_flag = 1` on the existing finding; set `superseded_by_id` to the new finding; record in patch accumulator.
- If factually incorrect: same supersession procedure.
- If set-aside (not wrong, but no longer analytically relevant): mark `delete_flag = 1` with `obsolete_reason` in patch.

---

### Type (b) Patch Construction

After all questions are processed and all existing findings reviewed:

**Step 1 — Compile patch operations from Q&A Log.**
For each ANSWERED or PARTIALLY ANSWERED Q&A entry that produces a new finding:
- One `wa_session_b_findings` INSERT per finding
- One `wa_finding_catalogue_links` INSERT per finding-question pair
- One `wa_finding_entity_links` INSERT per finding-term/verse/group link

For each superseded or obsoleted existing finding:
- One `wa_session_b_findings` UPDATE per affected row

For each SD pointer in the SD Pointer Accumulator (new, not in database):
- One `wa_session_research_flags` INSERT per pointer

For each `evidential_status` determination made during Stage 2a and confirmed in Stage 2b:
- One `wa_term_inventory` UPDATE per term

For each supplementary Type (a) correction from Path 3 resolutions (if not already patched):
- Included here if not yet applied

**Step 2 — List all operations in observations log before constructing patch JSON.**
State each operation: table, operation type, identifies row, field(s), value(s).

**Step 3 — Construct the patch.**
Per patch specification. Patch name: `PATCH-[YYYYMMDD]-[nnn]-SESSIONB-V1.json`

**Step 4 — Present for researcher approval.**
Do not submit to CC without explicit researcher approval.

**Step 5 — CC applies patch. Review confirmation.**
For each operation: confirm expected value is now in the database.

**Step 6 — SD pointer count verification.**
Request from CC: return count of `SD_POINTER` rows in `wa_session_research_flags` for registry [nnn].
Compare against SD Pointer Accumulator count.
- Match → record `SD pointer count verified: [n] in database = [n] in accumulator.`
- Mismatch → STOP. Identify missing pointers. Produce supplementary patch.

---

### Stage 2b Sign-Off Checklist

| Item | Required state |
|------|---------------|
| All registry-specific catalogue questions processed | Disposition recorded for each |
| All universal catalogue questions processed | Disposition recorded for each |
| NOT ANSWERED questions | All Stage 2a reopening units complete and Stage 2b re-run for affected questions |
| SD pointer review complete | All pointers confirmed, refined, or merged |
| Existing findings review complete | Supersessions/obsoletions identified and patched |
| Type (b) patch applied and confirmed by CC | Confirmation reviewed |
| SD pointer count in database = accumulator count | Hard gate |
| `evidential_status` set on all active OWNER terms | No NULLs |
| Q&A Log downloaded | Confirmed |

**Sign-off statement:**
```
STAGE 2B COMPLETE — Registry [nnn] ([word])
Date: [date]
Questions processed: [n] registry-specific + [n] universal = [n] total
  Answered: [n]. Partially answered: [n]. Not applicable: [n]. Stage 2a reopened: [n].
New findings written to database: [n]
Catalogue links written: [n]
SD pointers in database: [n] (verified against accumulator)
evidential_status set on all active OWNER terms: confirmed
Type (b) patch: [filename] — applied and confirmed

Stage 2c may begin.
```

---

### Fallback Protocol — Stage 2b

**Session interrupted mid-batch:** Resume from the last Q&A entry in the Q&A Log. The next question in `obs_id` order is the resumption point.

**NOT ANSWERED question requires Stage 2a reopening:** Add a targeted unit to Stage 2a (Unit 10, 11, etc.). Return to Stage 2b after the unit sign-off. Stage 2b does not advance past this question until the unit is complete.

**Type (b) patch partially applied:** Same procedure as Analysis Readiness — do not retry the full patch. Identify failed operations, produce a targeted corrective patch for those operations only.

**SD pointer count mismatch:** Do not proceed to Stage 2c. Identify which pointers are missing from the database. Produce a supplementary SD pointer patch. Re-verify count before Stage 2c.

---

### Session Close Protocol — Stage 2b

**C1 — Complete the current question batch or reach a question boundary.**
Always end Stage 2b sessions at a question sign-off in the Q&A Log.

**C2 — Verify tracking sections are current.**
Q&A Log, SD Pointer Accumulator, Progress Record all updated.

**C3 — Produce session log.**
Current question position; batch completed; outstanding questions; patch status; SD pointer count.

**C4 — Produce downloads.**
Q&A Log (as embedded in observations log) and session log available for download.

---

## Stage 2c — Analytic Word Output

### Purpose

Stage 2c produces the Analytic Word Output — a six-chapter document written for reading and reference. It is the primary reader-facing output of Analysis Output, and serves two downstream functions: it is the foundation for Session C word study production, and it provides the structured SD pointer summary for Session D.

Stage 2c is written from Stage 2b. Every statement in every chapter must be grounded in a Q&A pair from Stage 2b or in an SD pointer from the accumulator. No new analysis is introduced in Stage 2c.

Before writing any chapter, read and load the Session C prose rule: `wa-global-sessionc-prose-rule-v[current].md`. The prose rule governs sentence structure, citation practice, the boundary between observation and interpretation, and the treatment of Hebrew/Greek terms in English prose. It must be loaded and followed — it is not optional.

---

### Stage 2c Output

| Output | Filename | Purpose |
|--------|----------|---------|
| Analytic Word Output | `wa-[nnn]-[word]-sessionb-analytic-v1-[date].md` | Six-chapter document; primary Stage 2 deliverable |

---

### The Six Chapters

#### Chapter 1 — Meaning

**Content:** The word's semantic range: what it means, what sense structure it carries, how its meaning varies across terms, testament, and corpus.

**Must cover:**
- Core meaning and primary sense — what the Hebrew/Greek term(s) most fundamentally express
- Semantic range — the breadth from the most concrete to the most abstract usage
- Sense structure — where the term carries multiple distinct senses, distinguish them clearly; do not compress into a single gloss
- Cross-testament development — where OT and NT vocabulary diverge in emphasis or usage, name the development
- Root etymology — where the etymological grounding is analytically significant, include it; where it is speculative or tangential, omit it
- XREF vocabulary — briefly note what neighbouring vocabulary this registry draws on and why

**Must not contain:**
- How the word operates in inner-being terms (that is Chapter 2)
- Verse citations as the primary vehicle — verses support meaning claims, they do not constitute them
- Theological claims not grounded in lexical evidence

**Source:** MEANING_OBSERVATION, ETYMOLOGY, ROOT_FINDING findings from Stage 2b.

---

#### Chapter 2 — How It Works

**Content:** The inner-being operations of this characteristic — how it functions in the person, what it produces, what it requires, how it relates to other inner-being states.

**Must cover:**
- The characteristic's mode of operation: is it a disposition (stable orientation), an act (discrete event), a capacity (potential for action), or a state (condition that obtains)?
- What produces or triggers this characteristic — what causes it to arise or intensify
- What this characteristic produces — what it leads to, enables, or transforms
- The volitional dimension — is this characteristic chosen, received, cultivated, or spontaneous?
- The divine-human axis — how God's involvement shapes the characteristic's operation for humans
- The corporate dimension — does this characteristic operate in community in a distinctive way beyond its operation in individuals?

**Must not contain:**
- Semantic definitions (that is Chapter 1)
- Verse-by-verse commentary (that is Chapter 3)
- Cross-registry connection claims not supported by Stage 2b (that is Chapter 5)

**Source:** THEOLOGICAL_NOTE, SOMATIC_EVIDENCE, SPIRIT_SOUL_BODY findings from Stage 2b; operations-related Q&A pairs.

---

#### Chapter 3 — Verses

**Content:** All anchor verses for this word, with full ESV text and the Q&A pair(s) from Stage 2b that address each verse.

**Format for each verse:**

```
[Book Chapter:Verse] — [Group code: context description]

[Full verse text — ESV]

[Q&A pair(s) applicable to this verse, drawn directly from Stage 2b]
[If no Q&A pair directly addresses this verse: a single observation sentence from Stage 2a]
```

**Ordering:** Group by term (OWNER terms only). Within each term, order groups by `obs_id` or natural reading order. Within each group, order anchor verses canonically (book order).

**Coverage:** Every anchor verse must appear. No anchor verse may be omitted. If an anchor verse has no Q&A pair in Stage 2b, it receives a one-sentence observation from Stage 2a. If Stage 2a is also silent on a specific verse — this is a gap that must be resolved by reopening Stage 2a for that verse before Chapter 3 is written.

**Source:** VERSE_ANNOTATION findings; Stage 2b Q&A pairs linked to anchor verses via `wa_finding_entity_links`.

---

#### Chapter 4 — Language

**Content:** The precision of Hebrew and Greek usage; what the English translation obscures; the somatic dimension; what interpretation requires knowing about the term's original language.

**Must cover:**
- Where English glosses compress distinct sense or blend terms: name the compression and what it costs
- The somatic grounding: where the term is rooted in bodily experience, organ, or sensation — state this directly
- Translation notes: where ESV (or major translations) make choices that affect understanding — note the alternatives and their significance
- Grammatical forms: where causative, reflexive, or passive forms carry analytical weight — include them
- What a reader cannot access without knowing the Hebrew or Greek — the losses

**Must not contain:**
- Detailed lexical or grammatical exposition that belongs in an academic commentary
- Claims about textual variants unless directly relevant to the word's meaning

**Source:** SESSION_C_CORRECTION findings; language-accuracy Q&A pairs from Stage 2b.

---

#### Chapter 5 — Interrelationships

**Content:** This word's confirmed cross-registry connections, with evidence. Inferential connections labelled explicitly. SD pointers that raise connection questions.

**Structure:**

**Confirmed connections** (supported by at least one correlation signal — per integrity rule SB-7):
For each confirmed connection:
- Name the connected registry
- State the connection type (shared term / verse co-occurrence / shared anchor / shared root / semantic overlap)
- Characterise the nature of the connection: what specifically does this word share with that word, and what does the connection reveal about either or both?
- Note the open question for Session D

**Inferential connections** (analytically plausible but not confirmed by correlation signal):
For each inferential connection:
- Name the connected registry
- State the basis for the inference (shared semantic domain, complementary operations, structural relationship)
- Label explicitly: `Inferential — no correlation signal. Confirmation would require: [what signal would establish this].`

**Must not contain:**
- Cross-registry synthesis conclusions (those are Session D)
- Connections supported only by general theological association

**Source:** CROSS_REGISTRY findings from Stage 2b; correlation signal review from Stage 2a.

**Per integrity rules SB-7 and SB-8:** Chapter 5 must not contain a confirmed connection without correlation signal support. Chapter 5 must not omit a connection supported by a correlation signal. Before finalising Chapter 5: confirm against the correlation signals section of the extract that all strong signals are represented.

---

#### Chapter 6 — Open Questions

**Content:** All SD pointers for this registry, in full. This chapter is the Session D input from this word.

**Format for each SD pointer:**
```
[flag_label] — [priority: HIGH / MEDIUM / LOW]
Target: [registry no] [word] (if specific) / Pattern question (if no specific registry)
Connecting term/verse: [strongs_number or verse reference]

Question: [full question text as recorded in SD Pointer Accumulator]

Evidence basis: [what in the data triggers this question — named terms, verses, patterns]
```

**Coverage:** Every SD_POINTER record for this registry must appear. Ordering: HIGH priority first, then MEDIUM, then LOW. Within each priority level, order by `flag_label` sequentially.

**Must not contain:**
- Answers to the questions (those are Session D)
- Synthesis claims

**Source:** All SD_POINTER records for registry [nnn] from `wa_session_research_flags` — confirmed against database count from Stage 2b.

---

### Stage 2c Production Protocol

**Before writing:**
1. Load and read `wa-global-sessionc-prose-rule-v[current].md` in full.
2. Confirm Stage 2b Type (b) patch is confirmed applied.
3. Confirm SD pointer count in database matches Stage 2b accumulator.
4. Request a fresh extract from CC — this is the authoritative source for all data cited in Stage 2c.

**Writing order:** Chapter 1 → Chapter 2 → Chapter 3 → Chapter 4 → Chapter 5 → Chapter 6.

**After each chapter:** Download the chapter draft. Record chapter complete in Stage 2a Progress Record.

**After Chapter 5:** Run the SB-7/SB-8 check — confirm every strong correlation signal is represented and no unconfirmed connection is stated as confirmed.

**After Chapter 6:** Confirm SD pointer count in Chapter 6 matches database count.

---

## Closure

### Purpose

Closure verifies that the database is complete and ready for Session C, applies the closing patch, and produces the formal handoff. It mirrors the structure of Stage 1 completion.

---

### Fresh Extract for Closure

Request from CC: re-export the complete word data for registry [nnn] and return the new version identifier.
Record: `Closure extract confirmed: [filename] — version [n] — exported [date].`

---

### Closure Checklist

Run against the fresh closure extract. Every item must pass.

**Domain A — Data completeness**

| Check | Pass condition | Fail action |
|-------|---------------|------------|
| All active OWNER terms have `evidential_status` set | No NULLs | Identify unset terms; produce patch |
| All active OWNER terms have `mti_terms.status` set | No NULLs on active terms | Identify; produce patch |
| `verse_context_status` | `Complete` | Should not fail at this stage — if it does: investigate |
| All dimension index groups at `CLAUDE_AI` or `RESEARCHER` confidence | No AUTOMATED remaining | Run Dimension Review sub-process for affected groups |
| `dominant_subject` set on all dimension index rows | No NULLs | Patch correctable ones; RESEARCHER_DECISION for unclear |

**Domain B — Findings completeness**

| Check | Pass condition | Fail action |
|-------|---------------|------------|
| At least one active MEANING_OBSERVATION finding | Count > 0 | Stage 2a/2b gap — reopen |
| SPIRIT_SOUL_BODY finding present | Count = 1 | Stage 2a/2b gap — reopen |
| All anchor verses covered in Stage 2c Chapter 3 | Count of anchor verses = count of verse entries in Chapter 3 | Identify missing; add to Chapter 3 |
| No `thin_evidence = 1` findings unresolved | All thin findings dispositioned | Disposition in Stage 2b |
| No prior-phase findings with `delete_flag = 0` and disposition 'questioned' from Stage 2a Unit 9 | All findings reviewed and actioned | Return to Stage 2b existing findings review |

**Domain C — Flag resolution**

| Check | Pass condition | Fail action |
|-------|---------------|------------|
| Zero `wa_session_research_flags` with `session_target = 'B'` and `resolved = 0` | Hard gate | Identify; resolve before closure |
| SD pointer count in database matches Stage 2b accumulator | Hard gate | Supplementary SD pointer patch |
| All `wa_term_phase2_flags` dispositioned | Confirmed, rejected, or irrelevant noted for every flag | Return to Stage 1 Step 1.3a disposition records |

**Domain D — Entity links**

| Check | Pass condition | Fail action |
|-------|---------------|------------|
| Every active finding in `wa_session_b_findings` has at least one `wa_finding_entity_links` row | No orphan findings | Add entity links via supplementary patch |

**Domain E — Catalogue links**

| Check | Pass condition | Fail action |
|-------|---------------|------------|
| Every active finding has a `wa_finding_catalogue_links` row with `status IN ('suggested','validated')` | No findings without catalogue link | Return to Stage 2b; assign links |

**Domain F — Analytic Word Output**

| Check | Pass condition | Fail action |
|-------|---------------|------------|
| All six chapters produced and downloaded | Six files exist | Complete missing chapters |
| Chapter 5 confirmed against SB-7 and SB-8 | No unconfirmed confirmed connections; no missing signal-supported connections | Revise Chapter 5 |
| Chapter 6 SD pointer count matches database count | Counts match | Revise Chapter 6 |

---

### Corrective Action Loop

If any domain fails:

1. Identify the specific gap.
2. Determine corrective action: field patch / supplementary finding / stage reopening / researcher decision.
3. Apply correction and confirm via CC.
4. Re-run only the failed domain check — not the full checklist.
5. If the corrective action cannot be resolved within Analysis Output: raise a RESEARCHER_DECISION item per GR-RD-002. Record the open item in Stage 2c Chapter 6 as an open item until resolved.

Repeat until checklist is clean.

---

### Closing Patch

When the closure checklist is clean:

Construct the closing patch:
- `word_registry.session_b_status = 'Analysis Complete'`

Patch name: `PATCH-[YYYYMMDD]-[nnn]-ANALYSIS-V1.json`

Present for researcher approval. Submit to CC. Wait for confirmation.

Record: `Closing patch confirmed. session_b_status = Analysis Complete. Registry [nnn] [word] Analysis Output complete.`

---

### Handoff Signal

After the closing patch is confirmed, state the formal handoff:

```
ANALYSIS OUTPUT COMPLETE — Registry [nnn] ([word])
Date: [date]
Closure extract version: [version]

Stage 2a: COMPLETE — Observations log [filename] (fixed)
Stage 2b: COMPLETE — [n] Q&A pairs; [n] findings written; [n] SD pointers persisted
Stage 2c: COMPLETE — Six chapters produced
Closure: COMPLETE — All domains pass; closing patch applied

Mandatory outputs confirmed:
  [ ] Observations log: wa-[nnn]-[word]-sessionb-observations-v[n]-[date].md
  [ ] Session log: wa-[nnn]-[word]-sessionb-sessionlog-v[n]-[date].md
  [ ] Analytic Word Output: wa-[nnn]-[word]-sessionb-analytic-v1-[date].md
  [ ] Type (b) patch: PATCH-[YYYYMMDD]-[nnn]-SESSIONB-V1.json (applied)
  [ ] Closing patch: PATCH-[YYYYMMDD]-[nnn]-ANALYSIS-V1.json (applied)

Session C: OPEN — database and analytic output ready.
Session D: NOTIFIED — [n] SD pointers awaiting synthesis.
```

---

## Integrity Rules

The following rules govern Analysis Output. Rules SB-2 through SB-17 are updated from v5.0.

| Rule | Status | Text |
|------|--------|------|
| SB-1 | From Analysis Readiness | Stage 2a does not begin until the Stage 1 Completion Record confirms all seven domains pass |
| SB-2 | Updated | Closure does not begin until Stage 2a is signed off (observations log fixed), Stage 2b Type (b) patch is applied and confirmed, and Stage 2c all six chapters are complete |
| SB-7 | Updated | Chapter 5 must not contain a confirmed connection not supported by at least one correlation signal |
| SB-8 | Updated | Chapter 5 must not omit a connection supported by a correlation signal |
| SB-9 | Unchanged | Cross-word synthesis conclusions are not permitted in Analysis Output — questions only |
| SB-11 | Updated | SD pointers are raised throughout Stage 2a at the moment of discovery per GR-OBS-001 — not accumulated for a final stage |
| SB-12 | Updated | Every anchor verse is read with all five cross-registry vision questions applied (Stage 2a Unit 7) |
| SB-13 | Retired | Pass 6 SD pointer rule replaced by SB-11 (Stage 2a continuous SD pointer requirement) |
| SB-14 | Updated | SD pointer persistence is part of the Stage 2b Type (b) patch — mandatory; Closure does not begin without SD pointer count verified |
| SB-15 | Updated | SD pointer count in database must match Stage 2b accumulator count before Closure begins — hard gate in Stage 2b sign-off and Closure Domain C |
| SB-16 | Unchanged | The closing patch is a mandatory final output — Analysis Output does not close without it confirmed by CC |
| SB-17 | Updated | Analysis Output does not close without all five mandatory outputs confirmed: observations log, session log, analytic word output, Type (b) patch (applied), closing patch (applied) |
| SB-18 | From Analysis Readiness | Zero open `wa_session_research_flags` with `session_target = 'B'` and `resolved = 0` — confirmed in Closure Domain C |
| SB-25 (new) | New | Stage 2a observations log is fixed after Stage 2a sign-off. No further writing to the Stage 2a sections is permitted after sign-off. Stage 2a reopening (triggered by NOT ANSWERED questions in Stage 2b) adds new units to the log with sequential numbering — it does not modify existing entries |
| SB-26 (new) | New | Stage 2b draws only from Stage 2a. No new analysis is introduced in Stage 2b. A Q&A answer that cannot be grounded in a named Stage 2a observation is not a valid Stage 2b answer — the question is NOT ANSWERED and Stage 2a must be reopened |
| SB-27 (new) | New | Stage 2c draws only from Stage 2b Q&A pairs and the SD pointer accumulator. No new analysis is introduced in Stage 2c. A claim in Stage 2c that cannot be traced to a Q&A pair or SD pointer is a Stage 2c integrity violation |

---

## Naming Conventions

| Output | Pattern | Example |
|--------|---------|---------|
| Observations log | `wa-[nnn]-[word]-sessionb-observations-v[n]-[date].md` | `wa-062-fellowship-sessionb-observations-v1-20260416.md` |
| Session log | `wa-[nnn]-[word]-sessionb-sessionlog-v[n]-[date].md` | `wa-062-fellowship-sessionb-sessionlog-v1-20260416.md` |
| Analytic word output | `wa-[nnn]-[word]-sessionb-analytic-v1-[date].md` | `wa-062-fellowship-sessionb-analytic-v1-20260416.md` |
| Type (b) patch | `PATCH-[YYYYMMDD]-[nnn]-SESSIONB-V[n].json` | `PATCH-20260416-062-SESSIONB-V1.json` |
| Supplementary patch | `PATCH-[YYYYMMDD]-[nnn]-SESSIONB-SUPP-V[n].json` | `PATCH-20260416-062-SESSIONB-SUPP-V1.json` |
| Closing patch | `PATCH-[YYYYMMDD]-[nnn]-ANALYSIS-V1.json` | `PATCH-20260416-062-ANALYSIS-V1.json` |
| Type (a) supplementary patch | `PATCH-[YYYYMMDD]-[nnn]-PREANALYSIS-SUPP-V[n].json` | `PATCH-20260416-062-PREANALYSIS-SUPP-V1.json` |

---

*wa-sessionb-analysis-output-v1-20260416.md*
*Framework B — Soul Word Analysis Programme*
*Supersedes wa-global-sessionb-instruction-v5_0-20260415.md (Stage 2 and Stage 3)*
*Paired with wa-sessionb-analysis-readiness-v[current].md (Stage 1)*
