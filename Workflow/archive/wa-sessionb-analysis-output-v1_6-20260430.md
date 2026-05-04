# WA — Session B: Analysis Output Instruction
**Framework B — Soul Word Analysis Programme
Analysis Output Instruction — Comprehensive Analysis, Second-Tier Q&A Partitioning, and Analytic Word Output
Version 1_6 | 20260430 | Status: Active — Second-tier catalogue replaces §L catalogue as Stage 2b question set (v2.10)**

| **Document** | **Value** |
|---|---|
| Filename | wa-sessionb-analysis-output-v1_6-20260430.md |
| Supersedes | wa-sessionb-analysis-output-v1_5-20260428.md (replaces §L ~155-question catalogue with second-tier T0–T7 catalogue as Stage 2b question set; obslog remains the single output; standalone second-tier file retired) |
| Companion documents | wa-global-rules-all [current] │ wa-reference [current] │ wa-claudecode-instruction [current] │ wa-patch-instruction [current] │ wa-directive-instruction [current] │ wa-sessionc-instruction [current] │ wa-sessionb-analysis-readiness [current] │ wa-sessiona-prose-instruction [current] │ db-capture-phase1-results-and-table-architecture-v1-20260427.md |
| Inputs | **Registry data package `.md` (primary; second-tier catalogue embedded) + Validation report `.md` (gate-passing audit + WARN list, per readiness §v2.R8) + Analytic Status `.md` (revision sessions only).** No separate catalogue file is required — the second-tier catalogue is embedded in the registry data package. |
| Outputs | **Comprehensive obslog `.md` only.** CC parses obslog → DB writes (no patches). Side-effect: chapters in `prose_section`, findings + Q&A links + entity links + verse_context.analysis_note populated. **Revision sessions** must include superseded chapter blocks per v2.7 when prior prose is affected by the revision. |
| Claude AI role | Comprehensive reading; observations recording; second-tier Q&A production; analytic chapter writing; **citation discipline** (v2.4); **§N open-item resolution** (v2.3); **prose revision on review** (v2.7) |
| Claude Code role | **Phase 2 obslog-to-DB writer** (parser + validator + writer); pre-write backup; post-write verification + anomaly raising |
| Prerequisite | Readiness validation report at **READY** verdict (per readiness `[current]` §v2.R8). If verdict is BLOCKED, Stage 2 cannot start until failures are resolved. |

---

## Architecture v2 — addendum (effective 2026-04-27)

**Source-of-truth:** [research/investigations/db-capture-phase1-results-and-table-architecture-v1-20260427.md](../../../research/investigations/db-capture-phase1-results-and-table-architecture-v1-20260427.md) Parts 10-12 (researcher-locked).

The instruction body below describes the v1 patch-driven flow. **Under v2, these key shifts apply:**

### v2.1 Inputs — two `.md` artefacts replace the JSON extract

For initial analysis: **the registry data package `.md` plus its companion validation report `.md`**. The registry data package carries: §A registry overview · §B Stage 1 Completion Record (synthesised) · §C term inventory · §D lexical foundation · §E XREF · §F group landscape with dimensions · §G correlation signals · §H existing flags + findings · §I phase2 flags · §J verbatim verse text · §K legacy-VC notice · §L second-tier catalogue (T0–T7; see §v2.10 below) · §M readiness verification · **§N Open Session B Items**. The validation report `.md` records the 15-check verdict (READY / BLOCKED) with PASS/WARN/FAIL per check; the WARN list is the set of informational items AI should track during Stage 2a where they materially affect findings.

For **revision sessions:** also the **Analytic Status `.md`** — captures lifecycle summary, resolved Q&As, resolved SD pointers, not_relevant findings, prior chapters, anchor-verse analyses, open items.

### v2.2 Output — comprehensive obslog only

**No patches submitted by AI.** AI produces one comprehensive obslog `.md`. CC's Phase 2 writer parses the obslog and writes every category to its DB target:

| Obslog content | DB target |
|---|---|
| Stage 2a observations | `wa_session_b_findings` (status='open', finding_type='OBSERVATION') |
| Stage 2b Q&A pairs (second-tier catalogue) | `wa_finding_catalogue_links` (with finding_id → source observation; coverage='full' / 'partial' / 'not_applicable') + lifecycle update on source observation to status='resolved_qa' |
| Stage 2c chapters (5; chapter 6 IS the SD pointer compendium) | `prose_section` with section_type_id `sb_s2c_ch1`..`sb_s2c_ch5` |
| SD pointers | `wa_session_research_flags` (flag_code='SD_POINTER') + lifecycle update on source observation to 'resolved_sd' |
| Anchor-verse readings (Unit 7) | `verse_context.analysis_note` per (verse_record_id, mti_term_id) |
| GAP + word-specific questions | `wa_obs_question_catalogue` inserts |
| Review notes | `wa_obs_question_catalogue.review_note` (append) |
| Chapter citations | `wa_prose_section_citations` (extracted from chapter prose) |
| Status update | `word_registry.session_b_status` |

### v2.3 §N open items — non-negotiable resolution

Every item in §N of the registry data package is a Stage-2a observation OR a CC-raised anomaly carried forward as `wa_session_b_findings.status='open'`. **Each must reach one of these outcomes by session close:**

1. **Resolve via Q&A** — answer a second-tier catalogue prompt with this finding as source → `wa_finding_catalogue_links` row + lifecycle to `resolved_qa`
2. **Raise as new GAP question** — adds to `wa_obs_question_catalogue` + lifecycle to `resolved_qa`
3. **Convert to SD pointer** — `wa_session_research_flags` insert + lifecycle to `resolved_sd`
4. **Mark not_relevant** — with reason in `obsolete_reason` + lifecycle to `not_relevant`

A session that closes leaving §N items at `status='open'` has not closed cleanly. The obslog must explicitly record the chosen outcome path for each open item — CC's parser reads these closures.

### v2.4 Citation discipline (mandatory)

**Every Stage 2b Q&A answer must cite its source observation(s) as `OBS-NNN` references inline.** Without this, CC's writer cannot link the answer to its source observation — the lifecycle stays `open`, and the audit trail breaks.

**Every Stage 2c chapter substantive claim must cite at least one of:**

- `OBS-NNN` (a Stage 2a observation)
- `Q&A-NNN` or `Q###` (a catalogue question / Q&A pair)
- `SP-NNN` (an SD pointer)
- `DIM-NN-NNN` or other finding ID (an existing finding)

Citations are inline in chapter prose. CC's parser extracts them into `wa_prose_section_citations`. A chapter with substantive claims that lack citations fails the post-write coherence audit.

### v2.5 Catalogue completeness

For every prompt in the second-tier catalogue (T0–T7; see §v2.10 for tier structure), Stage 2b must produce one of:

- `coverage='full'` (ANSWERED) — finding linked
- `coverage='partial'` (PARTIALLY ANSWERED) — finding linked, qualification noted
- `coverage='not_applicable'` (NOT APPLICABLE) — rationale recorded
- `coverage='no_finding'` (CC-detected gap if AI didn't address) — backfill candidate

No prompt may be silently skipped. CC's catalogue-completeness sweep fills `no_finding` rows after AI's session for any unaddressed prompt.

### v2.6 Stage retirement / continuity

The body of this document (Stages 2a / 2b / 2c, integrity rules SB-1..SB-27, Closure checklist) describes the **discipline** of the analytical work and **remains authoritative**. What changes under v2 is the **delivery mechanism**: obslog → CC → DB instead of obslog → AI patches → CC apply.

The Closure section's "closing patch" is now the writer's `status_update` operation. The Stage 2b "Type (b) patch construction" is replaced by CC's `write_qa_findings` + `write_review_notes` + `write_new_questions` + `write_anchor_verse_analyses` + `write_chapters` writer logic.

### v2.7 Prose revision on review (mandatory for revision sessions)

**Rule:** Whenever an analytic revision session closes, every Stage 2c chapter (`prose_section` row) whose content is affected by the revision **must be superseded** with an updated version that:

1. **Carries inline citations for every substantive claim** under v2.4 discipline, including newly resolved findings, new SD pointers, and new GAP questions raised in the revision session.
2. **Covers all findings** — both the prior session's resolved findings and the revision session's newly resolved §N items, new SD pointers (`SP-NNN`), and new GAP questions (`GAP-N-NNN`).
3. **Surfaces new citation tokens** for CC's writer to register in `wa_prose_section_citations`. Tokens use the full finding_id format (`OBS-{registry:03d}-OBS-{seq:03d}`, `SP-{registry:03d}-{seq:03d}`, `Q&A-NNN`, `Q###`, `DIM-NN-NNN`) so the FK resolves at write time.

**A chapter is "affected" if any of the following apply to it:**

- A finding cited in the chapter has changed lifecycle (e.g. `open` → `resolved_qa`).
- A new finding, SD pointer, or GAP question raised in the revision belongs in the chapter's analytical scope.
- A dimension review, group reclassification, or anchor-verse change in the revision touches the chapter's content.
- The original chapter pre-dates v2.4 citation discipline and the revision is the first opportunity to bring it into compliance.

**Obslog format for superseded chapters:**

Each affected chapter is rendered in the obslog under a heading of the form:

```
### SUPERSEDE: sb_s2c_ch{n} — {chapter title}

**registry_id:** {n}
**author:** claude_ai
**version:** supersedes prior sb_s2c_ch{n} for registry {n}
**source_file:** wa-{nnn}-{word}-obslog-v{n}-{date}.md

---

{chapter body with inline citations throughout}
```

CC's parser identifies `SUPERSEDE: sb_s2c_ch{n}` blocks, calls `supersede` on the corresponding `prose_section` row (preserving `registry_id` and `section_type_id` from the predecessor), inserts the new prose body with an incremented version stamp, and extracts citations into `wa_prose_section_citations`.

**Session-close audit (CC):** After writing supersedes, CC's audit must confirm that:

- Every revision-session finding (resolved_qa, resolved_sd, not_relevant) is cited in at least one superseded or unchanged chapter.
- Every chapter that was a candidate for supersede received one (no silently-skipped chapters).
- Unresolved citation tokens (FK not populated) are < 10% of total citations per chapter.

If any of these fail, CC raises an anomaly finding (`DATA_ANOMALY_CITATION_GAP` or similar) for the next session to address.

### v2.8 Obslog format markers (mandatory; CC's parser depends on these)

The obslog is parsed by CC's Phase 1 parser into a structured manifest. The parser uses **exact marker patterns** to identify each category of content. If a marker doesn't match, the content is silently skipped. This rule specifies the markers AI must use.

**Section headers:**

| Section | Heading |
|---|---|
| Stage 2a observations | (inline, no separate section — see Observation marker below) |
| Stage 2b Q&A log | `### Stage 2b Q&A Log` (under any H2) |
| Per-tier Q&A grouping | `#### Tier {N} — {tier title} — {N} prompts` |
| Stage 2c chapters | `## Stage 2c — Chapter N: {title}` (one H2 per chapter) **OR** `## Stage 2c — Analytic Word Output` followed by `### Chapter N — {title}` (one H3 per chapter, both work) |
| SD pointer accumulator | `## SD Pointer Accumulator — Final` (with bullet entries below) |
| Session close + status | `## Session Close` containing `session_b_status: 'Analysis Complete'` (or other valid status from controlled vocab) |

**Observation marker** (Stage 2a — inline within reading-unit prose):

```
**OBS-{registry:03d}-{seq:03d}:** {full content of the observation}
```

- `{registry}` is zero-padded to 3 digits (e.g. `030`)
- `{seq}` is zero-padded to 3 digits, sequential 001..NNN per registry
- The content runs until the next OBS marker, the next H3, or two newlines followed by another marker

**Q&A marker** (Stage 2b — second-tier catalogue):

```
**Q&A-{seq:03d} | {tier_prompt_code}**
- Tier: {T0|T1|T2|T3|T4|T5|T6|T7} — {tier title}
- Component: {component code e.g. T1.3}
- Prompt: {N} — {full prompt text from catalogue}
- Disposition: ANSWERED | PARTIALLY ANSWERED | NOT APPLICABLE | NOT ANSWERED
- Status tag: A | P | N | S
- Notation: Consistent with prior analysis | Adds structure | New finding | Gap identified
- Answer: {answer text — must include OBS-{registry:03d}-{seq:03d} citations for ANSWERED/PARTIAL}
- Anchor verses: {comma-separated verse refs, e.g. Psa 34:18, Isa 53:5}
- Finding type: {THEOLOGICAL_NOTE | SOMATIC_EVIDENCE | SESSION_C_CORRECTION | VERSE_ANNOTATION | N/A}
- Stage 2b note: {optional qualifier}
[QUESTION REVIEW NOTE: {optional review of the catalogue prompt itself}]
```

- `{seq}` is the Q&A's sequential number in the obslog (e.g. `001`, `002`)
- `{tier_prompt_code}` is the prompt reference in the form `T{n}.{component}.P{prompt}` (e.g. `T1.3.P2`) — this becomes the `question_code` in `wa_obs_question_catalogue`
- The pipe (`|`) between seq and tier_prompt_code is required by the parser
- For `NOT APPLICABLE` disposition: use `Rationale:` instead of `Answer:` (parser falls back to Rationale when Answer is absent)
- **Status tag** maps directly to Disposition: A = ANSWERED, P = PARTIALLY ANSWERED, N = NOT APPLICABLE, S = NOT ANSWERED (silent in data)
- **Notation** may carry multiple tags separated by `/` (e.g. `New finding / Gap identified`)

**RESEARCHER_DECISION item on question_code format:** The `tier_prompt_code` format (`T{n}.{component}.P{prompt}`) is proposed as the `question_code` value for CC's parser. CC must confirm this resolves correctly against `wa_obs_question_catalogue.question_code` before first application, and advise if an alternative format is required. This does not block analytical work — AI uses the format above; CC adapts the parser if necessary.

**SD pointer marker** (within `## SD Pointer Accumulator — Final`):

```
**SP-{registry:03d}-{seq:03d}** — raised in Unit N, {YYYY-MM-DD}, {HIGH|MEDIUM|LOW}, Session D
- Target: R{NNN} ({word}) — or descriptive target if no specific registry
- Connecting term: {Strong's number or term description}
- Question: {the SD question being raised for Session D}
- Evidence basis: {OBS-NNN, OBS-NNN, ... — what observations grounded this pointer}
- Priority: {HIGH | MEDIUM | LOW}
```

**Status update** (in `## Session Close`):

```
session_b_status: 'Analysis Complete'
```

(Single quotes around the value; from controlled vocab: `Pre-Analysis Complete` | `Analysis Complete` | `Session B Complete` | `Verse Context Reset` | `Ready for Analysis` | `In Progress`.)

### v2.9 Chapter citation discipline (mandatory inline + CC extracts)

**Required:** every substantive claim in a Stage 2c chapter (Chapters 1–5 — Chapter 6 is the SD pointer compendium) must carry an inline citation in parentheses. Token formats:

```
{prose claim} (OBS-{registry:03d}-{seq:03d})
{prose claim} (Q&A-{seq:03d}, OBS-{registry:03d}-{seq:03d})
{prose claim} (SP-{registry:03d}-{seq:03d})
{prose claim} (DIM-{registry}-{seq:03d})
{prose claim} (GAP-N-{seq:03d}) — for GAP-N references
```

Multiple citations per claim are permitted: `(OBS-030-001, OBS-030-005, Q&A-024)`.

**CC behaviour on initial chapter write:** CC's `write_chapters()` extracts inline citations from the chapter prose and inserts rows into `wa_prose_section_citations`, resolving FKs to `wa_session_b_findings.id` (for OBS-NNN, DIM-NN-NNN, GAP-N-NNN tokens) and `wa_session_research_flags.id` (for SP-NNN tokens). Q&A-NNN tokens are stored with FK=null and the raw token in `citation_form`.

**Citation token resolution patterns:**

| Token | Match against | FK column |
|---|---|---|
| `OBS-{NNN}-{seq}` | `wa_session_b_findings.finding_id` | `cited_finding_id` |
| `SP-{NNN}-{seq}` | `wa_session_research_flags.flag_label` (where flag_code='SD_POINTER') | `cited_sd_pointer_id` |
| `DIM-{N}-{seq}` | `wa_session_b_findings.finding_id` | `cited_finding_id` |
| `GAP-N-{seq}` | `wa_obs_question_catalogue.question_code` | (no FK column; stored in `citation_form` only) |
| `Q&A-{NNN}` or `Q{NNN}` | (no FK column; stored as `citation_form`) | — |

**Audit on session close (CC):** the count of `wa_prose_section_citations` rows written for the registry must be > 0; unresolved-FK ratio per chapter < 10%. Failures raise `DATA_ANOMALY_CITATION_GAP` findings.

### v2.10 Second-tier catalogue as Stage 2b question set (effective 2026-04-30)

**The second-tier catalogue (T0–T7) replaces the prior ~155-question §L catalogue as the operative question set for Stage 2b.** This is the primary change introduced in v1_6.

**Catalogue source:** The second-tier catalogue is embedded in the registry data package at §L. It is applied in full for every registry. No separate catalogue file is required.

**Tier structure:** The catalogue spans eight tiers:

| Tier | Title | Focus |
|---|---|---|
| T0 | Divine Image and Created Design | Characteristic as reflecting divine nature; original design vs. fallen condition |
| T1 | Definition | Name, essence, boundary, immediate and sustained effect |
| T2 | Constitutional Location and Boundaries | Spirit, soul, heart, mind, body — where this characteristic operates |
| T3 | Inner Faculties | Engagement of all 11 inner faculties |
| T4 | Relational Interfaces | God-to-human, human-to-God, human-to-human directions |
| T5 | Formative and Developmental | Transformation, formation, reversibility, mechanism, eschatological trajectory |
| T6 | Structural Relationships | Co-occurrence, sequential, vocabulary/root sharing, distinctions, shared anchors |
| T7 | Evidential and Methodological Foundation | Lexical, verse and literary, human science frameworks |

**Tier sequence is fixed:** T0 → T1 → T2 → T3 → T4 → T5 → T6 → T7. Complete one full tier before moving to the next.

**Prior analysis as source material:** Where a registry has been previously analysed using the old §L catalogue, those Q&A results are treated as Stage 2a source material — they form part of the observations base that the second-tier prompts interrogate. The second-tier prompts are still applied in full regardless. Each prompt receives a fresh answer grounded in the registry data; prior findings are input, not output.

**Status codes and notation tags:** These are used within Stage 2b Q&A entries as qualifiers and are embedded in the Q&A marker (see §v2.8):

| Status code | Disposition | Meaning |
|---|---|---|
| A | ANSWERED | The data provides a direct and substantive response |
| P | PARTIALLY ANSWERED | The data addresses this prompt but incompletely; states what is evidenced and names what is missing |
| S | NOT ANSWERED | The data does not address this prompt; silence stated explicitly; Stage 2a reopening required if the gap should have been addressed |
| N | NOT APPLICABLE | The prompt's closing condition applies or the characteristic genuinely does not engage this domain |

**Notation tags** (one or more per Q&A entry):

| Tag | Meaning |
|---|---|
| *Consistent with prior analysis* | The prompt produces the same finding as existing programme work |
| *Adds structure* | The prompt organises or sharpens existing findings without changing substance |
| *New finding* | The prompt surfaces something not previously named or assembled in the data |
| *Gap identified* | The prompt reveals an area the existing analysis has not addressed |

**Closing summary (Stage 2b sign-off addendum):** After all tiers are complete, append to the Stage 2b Q&A log:

```markdown
## Stage 2b — Second-Tier Catalogue Summary

### Status Code Totals Across T0–T7
[Table: Tier | Total Prompts | A | P | S | N]

**Answered rate (A):** [n/total = %]
**Partial rate (P):** [n/total = %]
**Not answered rate (S):** [n/total = %]
**Not applicable rate (N):** [n/total = %]
**Coverage (A+P of applicable prompts):** [n/applicable = %]

### Key Gaps Consolidated
[Bulleted list of all S-status prompts by tier and component]

### New Findings Consolidated
[Numbered list of all *New finding* items across all tiers]
```

**Tier-specific notes** (apply during Stage 2b):

- **T0:** Theologically oriented but analytically grounded. Do not speculate beyond what verse evidence names. The closing condition "Where Scripture is silent about God's possession of this characteristic, note this explicitly" will be N for most characteristics. T0.2 Prompt 2 (original design vs. response to fallen condition) is frequently S — name the gap clearly.
- **T1:** T1.3 (Boundary) frequently produces partial answers — distinction from adjacent characteristics is often deferred to Session D. T1.5 (Immediate Response) and T1.6 (Sustained Effect) are distinct — keep them separate.
- **T2:** T2.8 (Body — Deposit) is the most speculative prompt — only affirm a deposit where verse evidence explicitly or strongly implies it. Flag the T5.7 dependency at T2.8. T2.10 (Constitutional Movement) is often the most structurally significant T2 output.
- **T3:** Work through all 11 faculty components. T3.5 (Creativity) is frequently S — name the silence. T3.3 (Memory) and T3.9 (Conscience) are often the richest new-finding sources. T3.11 (Relational Capacity) should distinguish characteristics that build/sustain connection from those that restore/repair it.
- **T4:** T4.3 (Giving) and T4.4 (Receiving) must be kept distinct. T4.4 Prompt 3 (person who encounters but does not receive) is frequently S — worth flagging. T4.6 (Spiritual Beings) is frequently S.
- **T5:** T5.1 Prompt 2 (reversibility) — attend carefully to whether the data distinguishes formal from genuine receipt. T5.7 (Deposit Consequence) depends on T2.8 — if T2.8 finds no constitutional body deposit, T5.7 closes formally and all three prompts receive N. State this explicitly at T5.7.
- **T6:** T6.1 (Co-occurrence) — always use quantitative data from the co-occurrence table. T6.4 (Vocabulary and Root Sharing) — zero XREF count does not mean no root-level connection. T6.5 (Distinctions) is frequently the weakest component — boundaries are commonly deferred to Session D.
- **T7:** T7.1 Prompts 8 (LXX) and 9 (NT coinage) are frequently S — the NO_WORD_ANALYSIS flag is the indicator. T7.3 (Human Science) is frequently undeveloped — identify the most relevant framework(s) from the characteristic's nature and name the gap. Do not introduce framework content not grounded in the data.

**Gap and new finding protocol:**

A **gap** is identified when: the prompt addresses a dimension the data has not examined; the verse evidence that would answer the prompt exists but has not been analysed; a structural question is implied by the data but no SD pointer captures it. When a gap is identified: (1) state it explicitly in the prompt response; (2) note whether it is covered by an existing SD pointer or is genuinely new; (3) assess whether further verse investigation in the current phase would address it, or whether it properly belongs to Session D.

A **new finding** is identified when: the prompt produces an answer that assembles existing observations in a way not previously done; the prompt reveals a structural relationship, sequence, or pattern implicit in the data but not named; the prompt synthesises across multiple observations into a single analytical statement. When a new finding is identified: (1) flag it with *New finding*; (2) state what the finding adds; (3) note implications for Session D or other registries.

**Standalone second-tier output file retired:** The `WA-R[nnn]-second-tier-analysis-v1-[date].md` format (from the previous standalone instruction) is retired. All second-tier analysis is written directly into the obslog. No separate second-tier file is produced.

---

## Change Log

**v1_6 (2026-04-30):** Second-tier catalogue replaces §L catalogue as Stage 2b question set. (1) Banner version, filename, Supersedes refreshed. (2) Inputs row: registry data package replaces readiness `.md` as primary input label (catalogue now at §L as second-tier T0–T7, not ~155 generic questions). (3) §v2.1 inputs: §L description updated — second-tier catalogue (T0–T7) replaces prior catalogue. (4) §v2.5 catalogue completeness: reworded to reference second-tier prompts rather than ~155 questions. (5) New §v2.10 — **Second-tier catalogue as Stage 2b question set**: full tier structure table (T0–T7), status codes (A/P/S/N) mapped to obslog disposition vocabulary (ANSWERED/PARTIALLY ANSWERED/NOT ANSWERED/NOT APPLICABLE), notation tags, prior-analysis-as-source-material rule, closing summary format, tier-specific notes, gap and new finding protocol, standalone output file retirement. (6) §v2.8 obslog format markers: per-tier Q&A grouping header updated from `#### Section N` to `#### Tier {N} — {tier title}`, Q&A marker updated to include `Tier`, `Component`, `Prompt`, `Status tag`, `Notation` fields; `{question_code}` replaced by `{tier_prompt_code}` in format `T{n}.{component}.P{prompt}`; RESEARCHER_DECISION item added on question_code format pending CC confirmation. (7) Claude AI role row: updated to reference second-tier Q&A production. (8) Standalone second-tier instruction (`WA-second-tier-analysis-instruction-v1-2026-04-30.md`) retired — methodology absorbed into this document.

**v1_5 (2026-04-28):** Obslog format markers + chapter citation discipline made explicit. New §v2.8 — obslog format markers (mandatory). New §v2.9 — chapter citation discipline. First application: R030 contrition retrofit.

**v1_4 (2026-04-27):** Session-start inputs aligned with readiness v1_9. Inputs row: explicit list. Prerequisite row: validation report READY verdict as gate. §v2.1 inputs: catalogue count corrected. §v2.5: count corrected. §What to Attach: full rewrite for Architecture v2. First application: R030 contrition.

**v1_3 (2026-04-27):** Added §v2.7 — prose revision on review rule. First application: R067 goodness obslog v3.

**v1_2 (2026-04-27):** Architecture v2 addendum applied. Inputs/Outputs/AI role rows updated. New Architecture v2 addendum section.

**v1_1 (2026-04-18):** GR-REF-002 sweep. Companion documents row updated. Governing Rules normalised. Stale examples replaced.

---

## Governing Rules

This instruction is governed by **wa-global-general-rules [current]**.

Claude AI must confirm the global rules file has been loaded before beginning any work per GR-LOAD-001.

---

## Pipeline Position

```
Analysis Readiness  (wa-sessionb-analysis-readiness [current])
     └── Stage 1 complete → Stage 1 Completion Record → Stage 2 Readiness Declaration
          │
          ▼
Analysis Output  (this instruction)
     ├── Schema readiness gate
     ├── Stage 2a: Comprehensive analysis → Observations log
     ├── Stage 2b: Second-tier Q&A partitioning (T0–T7) → Q&A log embedded in obslog
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

Under Architecture v2 (effective 2026-04-27), **two `.md` files are the entire session-start input for an initial analysis**. The second-tier catalogue is embedded in §L of the registry data package — there is no separate catalogue file.

**Required at session start (initial analysis):**

1. **This instruction file** — `wa-sessionb-analysis-output [current]`
2. **Global rules file** — `wa-global-rules-all [current]`
3. **Registry data package `.md`** — `Sessions/Session_B/07_Analysis_Readiness_Status/wa-{NNN}-{word}-readiness-output-v{n}-{date}.md`
   - The primary data input. Contains §A–§N including the embedded second-tier catalogue at §L.
   - **If absent: stop — Stage 2 cannot begin.**
4. **Validation report `.md`** — `Sessions/Session_B/07_Analysis_Readiness_Status/wa-{NNN}-{word}-readiness-validation-v1-{date}.md`
   - Records the 15-check verdict per readiness `[current]` §v2.R8.
   - **If verdict is BLOCKED: stop — Stage 2 cannot begin until the failures listed in the report are resolved.**
   - WARN list is the set of informational items AI should track during Stage 2a where they materially affect findings.
5. **CC instructions** — `wa-claudecode-instruction [current]`

**Additional input for revision sessions** (registry has been analysed before):

- **Analytic Status `.md`** — `Sessions/Session_B/07_Analysis_Readiness_Status/wa-{NNN}-{word}-analytic-status-v{n}-{date}.md`
   - Captures the prior analytical state: lifecycle summary, resolved Q&As, resolved SD pointers, not_relevant findings, prior chapters, anchor analyses, open items.

**No separate catalogue file is required** — the second-tier catalogue lives in §L of the registry data package (T0–T7; grows when GAP questions are added per `wa-obs-question-catalogue [current]`).

**No separate verbatim verse text file is required** — verbatim verse text is in §J of the registry data package.

**No separate observations or Q&A log is required at session start** — those are produced by AI **during** Stage 2a/2b within the comprehensive obslog (output, not input).

**Stage 2c chapter authoring:** the prose rule `wa-global-sessionc-prose-rule [current]` is loaded only when Stage 2c chapter writing begins, not at session start.

Do not load more data into the working session than the current stage requires.

---

## Governing Disciplines

These disciplines apply without exception across all stages, all sessions.

**Step-by-step.** Per GR-PROC-001. Each stage and each step within it is completed and confirmed before the next begins.

**Write on discovery.** Per GR-OBS-001 (non-waivable). Every observation, SD pointer, decision, and open question is written to the observations log at the moment it is determined. Nothing is accumulated in memory.

**All observations return to the database.** Per GR-OBS-006. Every analytical observation produced in Stage 2a must be addressed in Stage 2b and any that produce structured findings must be persisted before closure. Session C and Session D read from the database only.

**Data is authoritative.** Per GR-PROC-002. Work strictly from what is in the registry data package. Do not import general knowledge to fill gaps.

**All changes through patches or directives.** Per GR-PROC-003. Type (b) patches record analytical findings. Both require researcher approval per GR-PROC-004.

**Two types of database writes.** Type (a) — data quality corrections (Stage 1 only). Type (b) — analytical findings (Stage 2b close). Neither substitutes for the other.

**No DB state assumptions.** Per GR-DB-001. Claude AI never assumes the current state of the database.

**Cross-registry vision is always active.** Per GR-PROG-002. Every piece of data read in Stage 2a is read twice: once for what it says about this word, once for what it says about something beyond this word. SD pointers are raised continuously — not accumulated for a final pass. Per integrity rule SB-11.

**Characteristic-perspective grouping model.** Per GR-PROG-006. Every anchor verse is read with its group description as the interpretive lens. The group description names what the characteristic is that the verse is engaging. This is the reading frame — not the verse's general theme.

**Stage 2a is free-form. Stage 2b is structured.** Stage 2a produces observations without imposed structure. Stage 2b produces structured Q&A pairs governed by the second-tier catalogue. Do not attempt to structure Stage 2a observations as Q&A pairs during Stage 2a — this conflates two distinct stages and corrupts both.

**Researcher decision items.** Per GR-RD-001 through GR-RD-006. Last resort only. Before raising any item, exhaust analytical resources.

**Session logs at every breakpoint.** Per GR-PROC-006.

---

## Schema Readiness Gate

Before Stage 2a begins, confirm with CC that the following database conditions are met. If any condition fails, resolve before proceeding. This gate runs once per word — not at every session start.

| Condition | Check | Fail action |
|-----------|-------|------------|
| `wa_obs_question_catalogue` has rows for the second-tier T0–T7 catalogue | CC count query | Raise with researcher — catalogue may not be loaded |
| `wa_finding_catalogue_links` table exists | CC schema check | Raise CC directive — schema gap |
| `wa_session_b_findings.status` column exists | CC schema check | Raise CC directive — schema gap |
| `wa_session_b_findings.term_id` column exists | CC schema check | Raise CC directive — schema gap |
| Registry-specific catalogue questions present in §L | Count from second-tier catalogue section of data package | If 0: word-specific questions not yet indexed — raise with researcher |

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
Read `registry.session_b_status` in the attached data package. If `session_b_status = 'Pre-Analysis Complete'`: Stage 1 is confirmed complete and this is the correct extract. Confirm `meta.export_version` matches the Stage 1 Completion Record. If it matches: PASS. If versions differ or status is not `Pre-Analysis Complete`: stop and raise with researcher.

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
- Core meaning and semantic range
- Root family: etymological grounding
- Related words: cognates and their implications
- For Hebrew terms: Aramaic cognate or cross-testament development
- For Greek terms: LXX/OT background; LSJ record. **If `lsj_parse = NULL`: note as data gap; proceed from `step_search_gloss`, `short_def_mounce`, and related words only.**
- Sense structure: number of distinct senses. **If `meaning_parse.senses` is empty AND `meaning` field is NULL: record from `step_search_gloss`, `word_analysis_gloss`, `short_def_mounce`, related words. Note as data gap and proceed.**

Record Path 3 Resolution notes for any `evidential_status` items addressable from lexical data.

Stage 2a Progress Record sign-off: `Unit 3 COMPLETE: [n] OWNER terms. [n] observations. [n] SD pointers.`

---

**Unit 4 — Verse context groups: characteristic-perspective landscape**

Read: all verse context groups — group code, context description, dimension assignment, dimension confidence, dominant subject, anchor count, related count, set-aside count.

Do not read anchor verses yet. Read group descriptions only.

Record:
- The full landscape of inner-being characteristics this word engages across its corpus
- Whether the dimensions assigned are consistent with the group descriptions
- Whether any group description is ambiguous, overstated, or potentially miscategorised
- The distribution of dominant subjects — what pattern does this suggest?
- Any groups that stand out as analytically significant
- Whether the group structure clusters naturally

Stage 2a Progress Record sign-off: `Unit 4 COMPLETE: [n] groups across [n] terms. [n] observations. [n] SD pointers.`

---

**Unit 5 — Correlation signals**

Read: all correlation signals in the extract — ranked pairs, xref sharing, verse co-occurrence, shared anchor verses.

If all signal counts are 0: record `Unit 5 COMPLETE: zero ranked correlation signals. [n] shared anchor verses present.` Proceed to Unit 6.

Otherwise record:
- The top-ranked connections and what drives their score
- Any connections that are surprising given the word's cluster assignment
- Any connections that are absent but expected
- For each shared anchor verse pair: note which verses are shared with which registry — SD pointer candidates

Stage 2a Progress Record sign-off: `Unit 5 COMPLETE: [n] correlation pairs reviewed. [n] observations. [n] SD pointers.`

---

**Unit 6 — Existing SD pointers and findings**

Read: all existing SD_POINTER records for this registry. All existing `session_b_findings` for this registry.

For each existing SD pointer: note question, target registry, priority; whether it remains open; whether Stage 2a anchor verse reading should investigate it further.

For each existing finding: these are input material — prior-session hypotheses, not confirmed analytical facts. Note finding type, content, and whether it appears well-grounded or contestable.

Do not accept or reject existing findings here. Record impressions only.

**SD pointer naming check:** Verify each existing SD pointer `flag_label` follows `[nnn]-SD[seq]` with zero-padded three-digit registry number. Any inconsistency: add to patch accumulator.

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

Then record the verse observation: what does this verse contribute to understanding this inner-being characteristic that the group description alone does not capture?

Address Path 3 notes from Stage 1 as they are encountered.

**Group sign-off after all anchor verses are read:**
```
Group [code] COMPLETE: [date]
  Anchor verses read: [n]
  Key observation: [one sentence]
  SD pointers raised: [n]
  Path 3 items resolved in this group: [n]
```

**Terms with all verses set aside:** Record `[strongs] — all [n] verses set aside ([reasons]). No groups formed. Term contributes root vocabulary context only.`

**Set-aside verses:** After anchor verses for each group, review set-aside verses. Confirm set-aside reason is plausible. For NULL set-aside reason: read briefly and record whether set-aside appears correct. Do not re-classify.

**Stage 2a Progress Record sign-off at term close:**
`Term [strongs] anchor verse reading COMPLETE: [n] groups, [n] anchor verses. [n] SD pointers. [n] Path 3 resolutions.`

---

**Unit 8 — Thin-evidence phase2 flags**

Read: all phase2 flags carried forward with `thin_evidence` disposition from Stage 1 Step 1.3a. For each:
- Read the available verses for this term
- Record a disposition: confirmed by limited evidence / remains uncertain / clearly inapplicable
- If remains uncertain: note what verse evidence would be needed to resolve it

Stage 2a Progress Record sign-off: `Unit 8 COMPLETE: [n] thin-evidence flags reviewed. [n] dispositioned. [n] SD pointers.`

---

**Unit 9 — Existing findings: input material review**

Review all existing findings noted in Unit 6. For each:
- Against the backdrop of everything read in Units 3–8: does this finding appear well-grounded, overstated, or in need of correction?
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

**Session interrupted mid-unit:** Resume from the last group sign-off or the last unit sign-off recorded in Stage 2a Progress Record.

**Observation recorded but not fully developed:** Develop it before moving to the next item. Do not skip partial observations.

**Stage 2a sign-off recorded but observations log not downloaded:** Re-download before proceeding to Stage 2b.

**Path 3 item requires correction:** Record the correction needed in the Path 3 Resolution Notes. Apply a supplementary Type (a) patch before Stage 2b begins.

---

### Session Close Protocol — Stage 2a

**C1 — Complete the current group or reach a group boundary.**

**C2 — Verify the four tracking sections are current.**
SD Pointer Accumulator, RESEARCHER_DECISION Accumulator, Path 3 Resolution Notes, Stage 2a Progress Record — all updated.

**C3 — Produce the session log.**
Current position; units completed; outstanding units; SD pointers accumulated; Path 3 items resolved; exact resume instructions.

**C4 — Produce downloads.**
Observations log and session log both available for download before the session closes.

---

## Stage 2b — Second-Tier Q&A Partitioning

### Purpose

Stage 2b applies the second-tier catalogue (T0–T7, embedded in §L of the registry data package) to the Stage 2a observations log, producing a structured Q&A record for every prompt. The catalogue drives what is asked. Stage 2a provides the evidence. Stage 2b is the bridge between them.

The catalogue works tier by tier (T0 → T1 → T2 → T3 → T4 → T5 → T6 → T7). Each tier is completed in full before the next begins. Within a tier, each component is completed before moving to the next component.

Stage 2b produces all Type (b) database writes for this word. Nothing from Stage 2a reaches the database until Stage 2b applies its patch.

Stage 2b is iterative and multi-session capable. Each session works through one or more tiers. Stage 2b is complete when all prompts across all eight tiers have a recorded disposition and the Type (b) patch is applied and confirmed.

---

### Stage 2b Inputs

- Stage 2a observations log — fixed, confirmed, downloaded
- Second-tier catalogue from §L of the registry data package (T0–T7)
- Stage 1 Completion Record (for context — not modified)
- Prior analysis Q&A results where the registry has been previously analysed (treated as source material, not output)

**If any Path 3 corrections were identified in Stage 2a:** apply a supplementary Type (a) patch to correct these fields before Stage 2b begins. Request a fresh extract after the patch is confirmed.

---

### Stage 2b Tracking Documents

The observations log carries the SD Pointer Accumulator, RD Accumulator, and Progress Record from Stage 2a. Stage 2b adds:

```
### Stage 2b Q&A Log
[Populated during Stage 2b — one entry per prompt, grouped by tier]

#### Stage 2b Progress Record
[Updated at each tier sign-off]
```

**Q&A Log entry format** (per §v2.8 marker):
```
**Q&A-{seq:03d} | {tier_prompt_code}**
- Tier: {T0|T1|...|T7} — {tier title}
- Component: {component code e.g. T1.3}
- Prompt: {N} — {full prompt text from catalogue}
- Disposition: ANSWERED | PARTIALLY ANSWERED | NOT APPLICABLE | NOT ANSWERED
- Status tag: A | P | N | S
- Notation: {tag(s) — see §v2.10}
- Answer: {drawn directly from Stage 2a observations — OBS-NNN citations required for ANSWERED/PARTIAL}
- Anchor verses: {verse references}
- Finding type: {controlled vocabulary}
- Stage 2b note: {optional qualifier}
```

**Stage 2b Progress Record format:**
```
TIER [n] COMPLETE: [date]
  Tier: T[n] — [title]
  Prompts processed: [n]
  Answered: [n]. Partially answered: [n]. Not applicable: [n]. Not answered (S): [n].
  New findings identified: [n]
  SD pointers raised in this tier: [n]
```

---

### Session Start Protocol — Stage 2b

**S1 — Confirm global rules loaded.**

**S2 — Confirm Stage 2a is signed off and observations log is fixed.**
Read the Stage 2a sign-off statement. If not present: Stage 2b cannot begin.

**S3 — Confirm supplementary Type (a) patch applied if required.**
Check Path 3 Resolution Notes. If corrections were flagged: confirm patch applied and fresh extract confirmed.

**S4 — Establish position from Stage 2b Progress Record.**
Identify the last completed tier. Resume from the first prompt of the next tier.

**S5 — State resumption position.**

---

### Prompt Processing

Work through the second-tier catalogue tier by tier (T0 → T7). Within each tier, work component by component in the order given in the catalogue. Within each component, work prompt by prompt in sequence.

**For each prompt:**

**Step 1 — Read the prompt:**
State the tier, component, prompt number, and full text.

**Step 2 — Search Stage 2a for relevant observations:**
Read through the Stage 2a observations log. Identify all observations that bear on this prompt. Do not generate new analysis — draw only from what Stage 2a contains. Where prior analysis Q&A results exist for this registry, treat them as additional source material alongside Stage 2a observations.

**Step 3 — Assign a disposition and status tag:**

| Disposition | Status tag | Meaning |
|---|---|---|
| ANSWERED | A | Stage 2a contains sufficient evidence to give a direct and substantive response |
| PARTIALLY ANSWERED | P | Stage 2a addresses this prompt but incompletely; state what is evidenced and name what is missing |
| NOT ANSWERED | S | Stage 2a is silent on this prompt despite the data being available; Stage 2a must be reopened |
| NOT APPLICABLE | N | The prompt does not apply to this word, or the prompt's closing condition is met |

**Critical distinction — NOT ANSWERED (S) vs NOT APPLICABLE (N):**
NOT ANSWERED (S) means Stage 2a should have addressed this and did not — it triggers Stage 2a reopening. NOT APPLICABLE (N) means the characteristic genuinely does not engage with this prompt's domain, or the prompt's explicit closing condition is met. Assign N conservatively — default to S if uncertain.

**Step 4 — Assign a notation tag:**
One or more from: *Consistent with prior analysis* / *Adds structure* / *New finding* / *Gap identified*. See §v2.10 for definitions.

**Step 5 — Write the Q&A entry:**
For ANSWERED and PARTIALLY ANSWERED: write the full answer. Draw directly from Stage 2a. Cite observations as OBS-NNN. Do not introduce new analysis.

For NOT ANSWERED (S): record as NOT ANSWERED. Add *Gap identified* notation. Reopen Stage 2a for this specific prompt — add a targeted reading unit (Unit 10+, sequentially numbered). Return to Stage 2b after the unit is complete.

For NOT APPLICABLE (N): record with a one-sentence rationale. If the prompt's closing condition is met (e.g. T5.7 depends on T2.8 finding no body deposit), state this explicitly and note the dependency.

**Step 6 — Assign a finding type:**
Every ANSWERED or PARTIALLY ANSWERED entry that produces a new observation:

| Finding type | Use |
|---|---|
| MEANING_OBSERVATION | Semantic range, sense structure, core meaning |
| ETYMOLOGY | Root etymology, word origin, cognate patterns |
| ROOT_FINDING | Root family observation with cross-registry significance |
| THEOLOGICAL_NOTE | Divine dimension — God as subject, theological depth, covenantal grounding |
| VERSE_ANNOTATION | Per-verse observation |
| VERSE_PATTERN | Pattern across multiple verses |
| SOMATIC_EVIDENCE | Bodily part or process named |
| SPIRIT_SOUL_BODY | Spirit-soul-body classification with reasoning |
| SESSION_C_CORRECTION | Language correction to a prior finding or group description |
| CROSS_REGISTRY | Confirmed cross-registry connection with evidence |

**Step 7 — Note SD pointer links:**
If the answer confirms, deepens, or resolves an existing SD pointer: note the link. If the answer raises a new SD pointer: record it in the SD Pointer Accumulator.

**Tier sign-off after all prompts in a tier are complete:**
```
TIER T[n] COMPLETE — [tier title]
Date: [date]
Prompts: [n total]. A: [n]. P: [n]. S: [n]. N: [n].
New findings: [n]. SD pointers raised: [n].
```

---

### SD Pointer Review

After all eight tiers are processed: review the full SD Pointer Accumulator.

For each SD pointer:
1. Is the question precisely stated?
2. Is the target registry identified where possible?
3. Is the evidence basis stated with named OBS references?
4. Is the priority appropriate?
5. Is this a duplicate of an existing SD_POINTER record in the database? If so, note the existing record ID.

Record: `SD Pointer review complete. [n] pointers confirmed. [n] refined. [n] merged with existing records. [n] new.`

---

### Existing Findings Review

Review all existing findings from Stage 2a Unit 9 that were questioned or set-aside candidates.

For each:
- Against Stage 2b Q&A pairs: does the existing finding remain accurate?
- If accurate: leave in place.
- If superseded: mark `delete_flag = 1`, set `superseded_by_id`, record in patch accumulator.
- If set-aside: mark `delete_flag = 1` with `obsolete_reason`.

---

### Closing Summary

After all eight tiers are complete, append the Stage 2b closing summary (per §v2.10):

```markdown
## Stage 2b — Second-Tier Catalogue Summary

### Status Code Totals Across T0–T7
[Table: Tier | Total Prompts | A | P | S | N]

**Answered rate (A):** [n/total = %]
**Partial rate (P):** [n/total = %]
**Not answered rate (S):** [n/total = %]
**Not applicable rate (N):** [n/total = %]
**Coverage (A+P of applicable prompts):** [n/applicable = %]

### Key Gaps Consolidated
[Bulleted list of all S-status prompts by tier and component]

### New Findings Consolidated
[Numbered list of all *New finding* items across all tiers]
```

---

### Type (b) Patch Construction

After all tiers are processed, SD pointer review is complete, and existing findings are reviewed:

**Step 1 — Compile patch operations from Q&A Log.**
For each ANSWERED or PARTIALLY ANSWERED entry that produces a new finding:
- One `wa_session_b_findings` INSERT per finding
- One `wa_finding_catalogue_links` INSERT per finding-prompt pair
- One `wa_finding_entity_links` INSERT per finding-term/verse/group link

For each superseded or obsoleted existing finding:
- One `wa_session_b_findings` UPDATE per affected row

For each SD pointer in the SD Pointer Accumulator (new, not in database):
- One `wa_session_research_flags` INSERT per pointer

For each `evidential_status` determination made during Stage 2a and confirmed in Stage 2b:
- One `wa_term_inventory` UPDATE per term

**Step 2 — List all operations in observations log before constructing patch JSON.**

**Step 3 — Construct the patch.**
Per patch specification. Patch name: `PATCH-[YYYYMMDD]-[nnn]-SESSIONB-V1.json`

**Step 4 — Present for researcher approval.**

**Step 5 — CC applies patch. Review confirmation.**

**Step 6 — SD pointer count verification.**
Request from CC: count of `SD_POINTER` rows for registry [nnn]. Compare against accumulator count.
- Match → `SD pointer count verified: [n] in database = [n] in accumulator.`
- Mismatch → STOP. Produce supplementary patch.

---

### Stage 2b Sign-Off Checklist

| Item | Required state |
|------|---------------|
| All eight tiers (T0–T7) processed | Disposition recorded for every prompt |
| NOT ANSWERED (S) prompts | All Stage 2a reopening units complete and Stage 2b re-run for affected prompts |
| SD pointer review complete | All pointers confirmed, refined, or merged |
| Existing findings review complete | Supersessions/obsoletions identified and patched |
| Closing summary produced | Status code totals, key gaps, new findings consolidated |
| Type (b) patch applied and confirmed by CC | Confirmation reviewed |
| SD pointer count in database = accumulator count | Hard gate |
| `evidential_status` set on all active OWNER terms | No NULLs |
| Q&A Log downloaded | Confirmed |

**Sign-off statement:**
```
STAGE 2B COMPLETE — Registry [nnn] ([word])
Date: [date]
Tiers processed: T0 through T7 (8 tiers)
Prompts: [n total]. Answered: [n]. Partially answered: [n]. Not applicable: [n]. Not answered (S): [n].
New findings written to database: [n]
Catalogue links written: [n]
SD pointers in database: [n] (verified against accumulator)
evidential_status set on all active OWNER terms: confirmed
Type (b) patch: [filename] — applied and confirmed

Stage 2c may begin.
```

---

### Fallback Protocol — Stage 2b

**Session interrupted mid-tier:** Resume from the last Q&A entry in the Q&A Log within the current tier.

**NOT ANSWERED (S) prompt requires Stage 2a reopening:** Add a targeted unit to Stage 2a (Unit 10, 11, etc.). Return to Stage 2b after the unit sign-off.

**Type (b) patch partially applied:** Do not retry the full patch. Identify failed operations, produce a targeted corrective patch.

**SD pointer count mismatch:** Do not proceed to Stage 2c. Identify missing pointers. Produce supplementary patch. Re-verify before Stage 2c.

---

### Session Close Protocol — Stage 2b

**C1 — Complete the current tier or reach a tier boundary.**

**C2 — Verify tracking sections are current.**
Q&A Log, SD Pointer Accumulator, Progress Record all updated.

**C3 — Produce session log.**
Current tier position; tiers completed; outstanding tiers; patch status; SD pointer count.

**C4 — Produce downloads.**
Q&A Log (embedded in observations log) and session log available for download.

---

## Stage 2c — Analytic Word Output

### Purpose

Stage 2c produces the Analytic Word Output — a six-chapter document written for reading and reference. It is the primary reader-facing output of Analysis Output, and serves two downstream functions: it is the foundation for Session C word study production, and it provides the structured SD pointer summary for Session D.

Stage 2c is written from Stage 2b. Every statement in every chapter must be grounded in a Q&A pair from Stage 2b or in an SD pointer from the accumulator. No new analysis is introduced in Stage 2c.

Before writing any chapter, read and load the Session C prose rule: `wa-global-sessionc-prose-rule [current]`. The prose rule governs sentence structure, citation practice, the boundary between observation and interpretation, and the treatment of Hebrew/Greek terms in English prose. It must be loaded and followed.

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
- Core meaning and primary sense
- Semantic range — breadth from most concrete to most abstract usage
- Sense structure — where the term carries multiple distinct senses, distinguish them clearly
- Cross-testament development — where OT and NT vocabulary diverge in emphasis or usage
- Root etymology — where etymological grounding is analytically significant
- XREF vocabulary — briefly note what neighbouring vocabulary this registry draws on and why

**Must not contain:** How the word operates in inner-being terms (Chapter 2); verse citations as primary vehicle; theological claims not grounded in lexical evidence.

**Source:** MEANING_OBSERVATION, ETYMOLOGY, ROOT_FINDING findings from Stage 2b.

---

#### Chapter 2 — How It Works

**Content:** The inner-being operations of this characteristic — how it functions in the person, what it produces, what it requires, how it relates to other inner-being states.

**Must cover:**
- The characteristic's mode of operation: disposition, act, capacity, or state
- What produces or triggers this characteristic
- What this characteristic produces — what it leads to, enables, or transforms
- The volitional dimension
- The divine-human axis
- The corporate dimension

**Must not contain:** Semantic definitions (Chapter 1); verse-by-verse commentary (Chapter 3); cross-registry connection claims not supported by Stage 2b (Chapter 5).

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

**Ordering:** Group by term (OWNER terms only). Within each term, order groups by `obs_id` or natural reading order. Within each group, order anchor verses canonically.

**Coverage:** Every anchor verse must appear. If Stage 2a is silent on a specific verse — reopen Stage 2a for that verse before writing Chapter 3.

**Source:** VERSE_ANNOTATION findings; Stage 2b Q&A pairs linked to anchor verses.

---

#### Chapter 4 — Language

**Content:** The precision of Hebrew and Greek usage; what the English translation obscures; the somatic dimension; what interpretation requires knowing about the term's original language.

**Must cover:**
- Where English glosses compress distinct sense or blend terms
- The somatic grounding
- Translation notes — where ESV makes choices that affect understanding
- Grammatical forms where they carry analytical weight
- What a reader cannot access without knowing Hebrew or Greek

**Must not contain:** Detailed lexical or grammatical exposition belonging in academic commentary; claims about textual variants unless directly relevant.

**Source:** SESSION_C_CORRECTION findings; language-accuracy Q&A pairs from Stage 2b.

---

#### Chapter 5 — Interrelationships

**Content:** This word's confirmed cross-registry connections, with evidence. Inferential connections labelled explicitly. SD pointers that raise connection questions.

**Structure:**

**Confirmed connections** (supported by at least one correlation signal — per SB-7):
- Name the connected registry
- State the connection type
- Characterise the nature of the connection
- Note the open question for Session D

**Inferential connections** (analytically plausible but not confirmed by correlation signal):
- Name the connected registry
- State the basis for the inference
- Label explicitly: `Inferential — no correlation signal. Confirmation would require: [what signal would establish this].`

**Must not contain:** Cross-registry synthesis conclusions (Session D); connections supported only by general theological association.

**Source:** CROSS_REGISTRY findings from Stage 2b; correlation signal review from Stage 2a.

**Per SB-7 and SB-8:** Chapter 5 must not contain a confirmed connection without correlation signal support. Chapter 5 must not omit a connection supported by a correlation signal.

---

#### Chapter 6 — Open Questions

**Content:** All SD pointers for this registry, in full. This chapter is the Session D input from this word.

**Format for each SD pointer:**
```
[flag_label] — [priority: HIGH / MEDIUM / LOW]
Target: [registry no] [word] (if specific) / Pattern question (if no specific registry)
Connecting term/verse: [strongs_number or verse reference]

Question: [full question text as recorded in SD Pointer Accumulator]

Evidence basis: [what in the data triggers this question]
```

**Coverage:** Every SD_POINTER record for this registry must appear. Ordering: HIGH first, then MEDIUM, then LOW. Within each level, order by `flag_label` sequentially.

**Must not contain:** Answers to the questions (Session D); synthesis claims.

**Source:** All SD_POINTER records for registry [nnn] confirmed against database count from Stage 2b.

---

### Stage 2c Production Protocol

**Before writing:**
1. Load and read `wa-global-sessionc-prose-rule [current]` in full.
2. Confirm Stage 2b Type (b) patch is confirmed applied.
3. Confirm SD pointer count in database matches Stage 2b accumulator.
4. Request a fresh extract from CC.

**Writing order:** Chapter 1 → Chapter 2 → Chapter 3 → Chapter 4 → Chapter 5 → Chapter 6.

**After each chapter:** Download the chapter draft. Record chapter complete in Stage 2a Progress Record.

**After Chapter 5:** Run the SB-7/SB-8 check.

**After Chapter 6:** Confirm SD pointer count in Chapter 6 matches database count.

---

## Closure

### Purpose

Closure verifies that the database is complete and ready for Session C, applies the closing patch, and produces the formal handoff.

---

### Fresh Extract for Closure

Request from CC: re-export the complete word data for registry [nnn].
Record: `Closure extract confirmed: [filename] — version [n] — exported [date].`

---

### Closure Checklist

Run against the fresh closure extract. Every item must pass.

**Domain A — Data completeness**

| Check | Pass condition | Fail action |
|-------|---------------|------------|
| All active OWNER terms have `evidential_status` set | No NULLs | Identify unset terms; produce patch |
| All active OWNER terms have `mti_terms.status` set | No NULLs on active terms | Identify; produce patch |
| `verse_context_status` | `Complete` | Investigate |
| All dimension index groups at `CLAUDE_AI` or `RESEARCHER` confidence | No AUTOMATED remaining | Run Dimension Review sub-process |
| `dominant_subject` set on all dimension index rows | No NULLs | Patch correctable ones; RESEARCHER_DECISION for unclear |

**Domain B — Findings completeness**

| Check | Pass condition | Fail action |
|-------|---------------|------------|
| At least one active MEANING_OBSERVATION finding | Count > 0 | Stage 2a/2b gap — reopen |
| SPIRIT_SOUL_BODY finding present | Count = 1 | Stage 2a/2b gap — reopen |
| All anchor verses covered in Stage 2c Chapter 3 | Count of anchor verses = count of verse entries in Chapter 3 | Identify missing; add to Chapter 3 |
| No `thin_evidence = 1` findings unresolved | All thin findings dispositioned | Disposition in Stage 2b |
| No prior-phase findings with `delete_flag = 0` and disposition 'questioned' | All reviewed and actioned | Return to Stage 2b existing findings review |

**Domain C — Flag resolution**

| Check | Pass condition | Fail action |
|-------|---------------|------------|
| Zero `wa_session_research_flags` with `session_target = 'B'` and `resolved = 0` | Hard gate | Identify; resolve before closure |
| SD pointer count in database matches Stage 2b accumulator | Hard gate | Supplementary SD pointer patch |
| All `wa_term_phase2_flags` dispositioned | Confirmed, rejected, or irrelevant noted | Return to Stage 1 Step 1.3a |

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
5. If unresolvable within Analysis Output: raise a RESEARCHER_DECISION item per GR-RD-002. Record as open item in Chapter 6 until resolved.

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

After the closing patch is confirmed:

```
ANALYSIS OUTPUT COMPLETE — Registry [nnn] ([word])
Date: [date]
Closure extract version: [version]

Stage 2a: COMPLETE — Observations log [filename] (fixed)
Stage 2b: COMPLETE — [n] prompts across T0–T7; [n] findings written; [n] SD pointers persisted
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

| Rule | Status | Text |
|------|--------|------|
| SB-1 | From Analysis Readiness | Stage 2a does not begin until the Stage 1 Completion Record confirms all seven domains pass |
| SB-2 | Updated | Closure does not begin until Stage 2a is signed off, Stage 2b Type (b) patch is applied and confirmed, and Stage 2c all six chapters are complete |
| SB-7 | Updated | Chapter 5 must not contain a confirmed connection not supported by at least one correlation signal |
| SB-8 | Updated | Chapter 5 must not omit a connection supported by a correlation signal |
| SB-9 | Unchanged | Cross-word synthesis conclusions are not permitted in Analysis Output — questions only |
| SB-11 | Updated | SD pointers are raised throughout Stage 2a at the moment of discovery per GR-OBS-001 — not accumulated for a final stage |
| SB-12 | Updated | Every anchor verse is read with all five cross-registry vision questions applied (Stage 2a Unit 7) |
| SB-13 | Retired | Pass 6 SD pointer rule replaced by SB-11 |
| SB-14 | Updated | SD pointer persistence is part of the Stage 2b Type (b) patch — mandatory; Closure does not begin without SD pointer count verified |
| SB-15 | Updated | SD pointer count in database must match Stage 2b accumulator count before Closure begins — hard gate in Stage 2b sign-off and Closure Domain C |
| SB-16 | Unchanged | The closing patch is a mandatory final output — Analysis Output does not close without it confirmed by CC |
| SB-17 | Updated | Analysis Output does not close without all five mandatory outputs confirmed: observations log, session log, analytic word output, Type (b) patch (applied), closing patch (applied) |
| SB-18 | From Analysis Readiness | Zero open `wa_session_research_flags` with `session_target = 'B'` and `resolved = 0` — confirmed in Closure Domain C |
| SB-25 | Unchanged | Stage 2a observations log is fixed after Stage 2a sign-off. Stage 2a reopening adds new units with sequential numbering — does not modify existing entries |
| SB-26 | Unchanged | Stage 2b draws only from Stage 2a. No new analysis introduced in Stage 2b. A Q&A answer not grounded in a named Stage 2a observation is not valid — Stage 2a must be reopened |
| SB-27 | Unchanged | Stage 2c draws only from Stage 2b Q&A pairs and the SD pointer accumulator. No new analysis introduced in Stage 2c |
| SB-28 | New | Stage 2b processes all eight second-tier tiers (T0–T7) in sequence. No tier may be skipped. A tier is complete only when every prompt within it has a recorded disposition |

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

*wa-sessionb-analysis-output-v1_6-20260430.md*
*Framework B — Soul Word Analysis Programme*
*Supersedes wa-sessionb-analysis-output-v1_5-20260428.md (second-tier T0–T7 catalogue replaces §L catalogue as Stage 2b question set; standalone second-tier output file retired)*
*Paired with wa-sessionb-analysis-readiness [current] (Stage 1)*
