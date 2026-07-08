# WA — Session B: Analysis Output Instruction
**Framework B — Soul Word Analysis Programme
Analysis Output Instruction — Comprehensive Analysis, Second-Tier Q&A Partitioning, and Analytical Synthesis
Version 1_8 | 20260430 | Status: Active — Stage 2c rewritten as analytical synthesis pass (intra- and inter-tier); prose chapters replaced by structured synthesis entries; T0 excluded from Stage 2c; six CC schema/parser actions flagged**

| **Document** | **Value** |
|---|---|
| Filename | wa-sessionb-analysis-output-v1_8-20260430.md |
| Supersedes | wa-sessionb-analysis-output-v1_7-20260430.md (Stage 2c rewrite — see Change Log) |
| Companion documents | wa-global-rules-all [current] │ wa-reference [current] │ wa-claudecode-instruction [current] │ wa-directive-instruction [current] │ wa-sessionc-instruction [current] │ wa-sessionb-analysis-readiness [current] │ wa-sessiona-prose-instruction [current] │ db-capture-phase1-results-and-table-architecture-v1-20260427.md |
| Inputs | Registry data package `.md` (primary; second-tier catalogue embedded at §L) + Validation report `.md` (gate-passing audit + WARN list, per readiness §v2.R8) + Analytic Status `.md` (revision sessions only). |
| Outputs | **Two artefacts produced by AI:** comprehensive obslog `.md` and session log `.md`. CC's Phase 2 writer parses the obslog and writes every category to its DB target — no patches. Side-effects of the obslog parse: chapters in `prose_section`, findings in `wa_session_b_findings`, Q&A links in `wa_finding_catalogue_links`, entity links in `wa_finding_entity_links`, anchor analyses in `verse_context.analysis_note`, SD pointers / SB findings / RESEARCHER_DECISION in `wa_session_research_flags`, and `word_registry.session_b_status`. |
| Claude AI role | Comprehensive reading; observations recording; second-tier Q&A production; Stage 2c synthesis pass (intra- and inter-tier, T1–T7); citation discipline (§4); §N open-item resolution (§3); prose revision on review (§7) |
| Claude Code role | Phase 2 obslog-to-DB writer (parser + validator + writer); pre-write backup; post-write verification + anomaly raising |
| Prerequisite | Readiness validation report at **READY** verdict (per readiness `[current]` §v2.R8). If verdict is BLOCKED, Stage 2 cannot start until failures are resolved. |

---

## Architecture v2 — operational spec

**Source-of-truth:** [research/investigations/db-capture-phase1-results-and-table-architecture-v1-20260427.md](../../../research/investigations/db-capture-phase1-results-and-table-architecture-v1-20260427.md) Parts 10-12 (researcher-locked).

The mechanics below are the operative v2 spec. Sections §1 through §10 replace the v1.6 §v2.x addendum; the analytical discipline of Stages 2a / 2b / 2c later in this document is unchanged.

### §1 Inputs — `.md` artefacts only, no JSON extract

For initial analysis: **the registry data package `.md` plus its companion validation report `.md`**. The registry data package carries: §A registry overview · §B Stage 1 Completion Record (synthesised) · §C term inventory · §D lexical foundation · §E XREF · §F group landscape with dimensions · §G correlation signals · §H existing flags + findings · §I phase2 flags · §J verbatim verse text · §K legacy-VC notice · §L second-tier catalogue (T0–T7; see §10) · §M readiness verification · §N Open Session B Items.

The validation report `.md` records the 15-check verdict (READY / BLOCKED) with PASS/WARN/FAIL per check; the WARN list is the set of informational items AI should track during Stage 2a where they materially affect findings.

For **revision sessions:** also the **Analytic Status `.md`** — captures lifecycle summary, resolved Q&As, resolved SD pointers, not_relevant findings, prior chapters, anchor-verse analyses, open items.

### §2 Outputs — comprehensive obslog + session log

AI produces exactly **two artefacts**:

| Artefact | Filename pattern | Purpose |
|---|---|---|
| Comprehensive obslog | `wa-{NNN}-{word}-obslog-v{n}-{date}.md` | Carries all Stage 2a observations, Stage 2b Q&A, Stage 2c chapters, SD pointer accumulator, RESEARCHER_DECISION accumulator, anchor-verse analyses, status update. CC's parser walks this file and writes every category to its DB target. |
| Session log | `wa-{NNN}-{word}-sessionb-sessionlog-v{n}-{date}.md` | Handoff document — current position, open items, resume instructions, session-close summary. Not parsed by CC; informational. |

**There are no patches.** AI does not construct or submit Type (b) patches, Closing patches, or supplementary patches. Every database write is performed by CC's Phase 2 writer reading the obslog. CC's writer maps obslog content to DB targets:

| Obslog content | DB target |
|---|---|
| Stage 2a observations (`**OBS-{NNN}-{seq}:**` markers) | `wa_session_b_findings` (status='open', finding_type='OBSERVATION') |
| Stage 2b Q&A pairs (second-tier catalogue) | `wa_finding_catalogue_links` (with finding_id → source observation; coverage='full' / 'partial' / 'no_finding' / 'not_applicable') + lifecycle update on source observation to status='resolved_qa' |
| Stage 2c synthesis entries (`**SYN-INTRA-{NNN}-{seq}**` and `**SYN-INTER-{NNN}-{seq}**` markers) | `wa_session_b_findings` (finding_type='SYNTHESIS_INTRA_TIER' or 'SYNTHESIS_INTER_TIER') + `wa_finding_catalogue_links` rows linking each synthesis entry to its source Q&A entries |
| SD pointers (`**SP-{NNN}-{seq}**` accumulator entries) | `wa_session_research_flags` (flag_code='SD_POINTER') + lifecycle update on source observation to 'resolved_sd' |
| Anchor-verse readings (Unit 7) | `verse_context.analysis_note` per (verse_record_id, mti_term_id) |
| GAP + word-specific questions raised mid-session | `wa_obs_question_catalogue` inserts |
| Review notes on catalogue prompts | `wa_obs_question_catalogue.review_note` (append) |
| Inline chapter citations | `wa_prose_section_citations` (extracted from chapter prose) |
| Status update (`## Session Close` block) | `word_registry.session_b_status` |
| RESEARCHER_DECISION items | `wa_session_research_flags` (flag_code='RESEARCHER_DECISION') |

### §3 §N open items — non-negotiable resolution

Every item in §N of the registry data package is a Stage-2a observation OR a CC-raised anomaly carried forward as `wa_session_b_findings.status='open'`. **Each must reach one of these outcomes by session close:**

1. **Resolve via Q&A** — answer a second-tier catalogue prompt with this finding as source → `wa_finding_catalogue_links` row + lifecycle to `resolved_qa`
2. **Raise as new GAP question** — adds to `wa_obs_question_catalogue` + lifecycle to `resolved_qa`
3. **Convert to SD pointer** — `wa_session_research_flags` insert + lifecycle to `resolved_sd`
4. **Mark not_relevant** — with reason in `obsolete_reason` + lifecycle to `not_relevant`

A session that closes leaving §N items at `status='open'` has not closed cleanly. The obslog must explicitly record the chosen outcome path for each open item — CC's parser reads these closures.

### §4 Citation discipline (mandatory)

**Every Stage 2b Q&A answer must cite its source observation(s) as `OBS-{NNN}-{seq}` references inline.** Without this, CC's writer cannot link the answer to its source observation — the lifecycle stays `open`, and the audit trail breaks.

**Every Stage 2c synthesis entry with a D outcome must cite at least two Stage 2b Q&A entries** in the `Source Q&A:` field. F and N outcomes require at least one. Citations must use the `Q&A-{seq:03d}` token format so CC's parser can resolve the links to `wa_finding_catalogue_links` rows.

### §5 Catalogue completeness

For every prompt in the second-tier catalogue (T0–T7; see §10 for tier structure), Stage 2b must produce one of:

- `coverage='full'` (ANSWERED) — finding linked
- `coverage='partial'` (PARTIALLY ANSWERED) — finding linked, qualification noted
- `coverage='not_applicable'` (NOT APPLICABLE) — rationale recorded
- `coverage='no_finding'` (NOT ANSWERED — silent in data; backfill candidate)

No prompt may be silently skipped. CC's catalogue-completeness sweep fills `no_finding` rows after AI's session for any unaddressed prompt.

### §6 Stage discipline — what is preserved

Stages 2a / 2b / 2c, integrity rules SB-1..SB-28, and the Closure checklist below describe the **discipline** of the analytical work and **remain authoritative**. The discipline is unchanged from v1; the change in v2 was the delivery mechanism (obslog → CC → DB instead of obslog → AI patches → CC apply). v1.7 has cleaned the patch language out of the discipline so the two read consistently.

### §7 Prose revision on review (mandatory for revision sessions)

**Rule:** Whenever an analytic revision session closes, every Stage 2c chapter (`prose_section` row) whose content is affected by the revision **must be superseded** with an updated version that:

1. **Carries inline citations for every substantive claim** under §4 discipline, including newly resolved findings, new SD pointers, and new GAP questions raised in the revision session.
2. **Covers all findings** — both the prior session's resolved findings and the revision session's newly resolved §N items, new SD pointers (`SP-{NNN}-{seq}`), and new GAP questions (`GAP-N-{seq}`).
3. **Surfaces new citation tokens** for CC's writer to register in `wa_prose_section_citations`. Tokens use the full finding_id format from the §4 list so the FK resolves at write time.

**A chapter is "affected" if any of the following apply to it:**

- A finding cited in the chapter has changed lifecycle (e.g. `open` → `resolved_qa`).
- A new finding, SD pointer, or GAP question raised in the revision belongs in the chapter's analytical scope.
- A dimension review, group reclassification, or anchor-verse change in the revision touches the chapter's content.
- The original chapter pre-dates §4 citation discipline and the revision is the first opportunity to bring it into compliance.

**Obslog format for superseded chapters:**

Each affected chapter is rendered in the obslog under a heading of the form:

```
### SUPERSEDE: sb_s2c_ch{n} — {chapter title}

**registry_id:** {n}
**author:** claude_ai
**version:** supersedes prior sb_s2c_ch{n} for registry {n}
**source_file:** wa-{NNN}-{word}-obslog-v{n}-{date}.md

---

{chapter body with inline citations throughout}
```

CC's parser identifies `SUPERSEDE: sb_s2c_ch{n}` blocks, calls `supersede` on the corresponding `prose_section` row (preserving `registry_id` and `section_type_id` from the predecessor), inserts the new prose body with an incremented version stamp, and extracts citations into `wa_prose_section_citations`.

**Session-close audit (CC):** After writing supersedes, CC's audit must confirm that:

- Every revision-session finding (resolved_qa, resolved_sd, not_relevant) is cited in at least one superseded or unchanged chapter.
- Every chapter that was a candidate for supersede received one (no silently-skipped chapters).
- Unresolved citation tokens (FK not populated) are < 10% of total citations per chapter.

If any of these fail, CC raises an anomaly finding (`DATA_ANOMALY_CITATION_GAP` or similar) for the next session to address.

### §8 Obslog format markers (mandatory; CC's parser depends on these)

The obslog is parsed by CC's Phase 1 parser into a structured manifest. The parser uses **exact marker patterns** to identify each category of content. If a marker doesn't match, the content is silently skipped. This rule specifies the markers AI must use.

**Section headers:**

| Section | Heading |
|---|---|
| Stage 2a observations | (inline, no separate section — see Observation marker below) |
| Stage 2b Q&A log | `### Stage 2b Q&A Log` (under any H2) |
| Per-tier Q&A grouping | `#### Tier {N} — {tier title} — {N} prompts` |
| Stage 2c synthesis entries | `## Stage 2c — Synthesis Entries` (one H2 section; all SYN-INTRA and SYN-INTER markers within) |
| SD pointer accumulator | `## SD Pointer Accumulator — Final` (with bullet entries below) |
| RESEARCHER_DECISION accumulator | `## RESEARCHER_DECISION Accumulator — Final` (with bullet entries below) |
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
- Answer: {answer text — must include OBS-{NNN}-{seq} citations for ANSWERED/PARTIAL}
- Anchor verses: {comma-separated verse refs, e.g. Psa 34:18, Isa 53:5}
- Finding type: {THEOLOGICAL_NOTE | SOMATIC_EVIDENCE | SESSION_C_CORRECTION | VERSE_ANNOTATION | N/A}
- Stage 2b note: {optional qualifier}
[QUESTION REVIEW NOTE: {optional review of the catalogue prompt itself}]
```

- `{seq}` is the Q&A's sequential number in the obslog (e.g. `001`, `002`)
- **`{tier_prompt_code}`** is the prompt reference in the form **`T{n}.{component}.{prompt}`** (e.g. `T1.3.2`) — this is the `question_code` value in `wa_obs_question_catalogue` (catalogue v2). The pipe (`|`) between seq and tier_prompt_code is required by the parser.
- For `NOT APPLICABLE` disposition: use `Rationale:` instead of `Answer:` (parser falls back to Rationale when Answer is absent)
- **Status tag** maps directly to Disposition: A = ANSWERED, P = PARTIALLY ANSWERED, N = NOT APPLICABLE, S = NOT ANSWERED (silent in data)
- **Notation** may carry multiple tags separated by `/` (e.g. `New finding / Gap identified`)

**SD pointer marker** (within `## SD Pointer Accumulator — Final`):

```
**SP-{registry:03d}-{seq:03d}** — raised in Unit N, {YYYY-MM-DD}, {HIGH|MEDIUM|LOW}, Session D
- Target: R{NNN} ({word}) — or descriptive target if no specific registry
- Connecting term: {Strong's number or term description}
- Question: {the SD question being raised for Session D}
- Evidence basis: {OBS-NNN, OBS-NNN, ... — what observations grounded this pointer}
- Priority: {HIGH | MEDIUM | LOW}
```

**RESEARCHER_DECISION marker** (within `## RESEARCHER_DECISION Accumulator — Final`):

```
**RD-{registry:03d}-{seq:03d}** — raised {YYYY-MM-DD}, {HIGH|MEDIUM|LOW}
- Decision required: {the question or choice point requiring researcher input}
- Context: {what surfaced this — OBS-NNN refs, prompt component, etc.}
- Options considered: {short list if applicable}
- Recommendation (if any): {the AI's preferred resolution, or 'none — open question'}
```

**Status update** (in `## Session Close`):

```
session_b_status: 'Analysis Complete'
```

(Single quotes around the value; from controlled vocab: `Pre-Analysis Complete` | `Analysis Complete` | `Session B Complete` | `Verse Context Reset` | `Ready for Analysis` | `In Progress`.)

### §9 Synthesis entry citation discipline (mandatory; CC extracts source Q&A links)

**Stage 2c synthesis entries do not carry inline prose citations.** Citation in Stage 2c is via the structured `Source Q&A:` field in the obslog marker, not inline in prose. CC's parser reads the `Source Q&A:` field and writes `wa_finding_catalogue_links` rows linking the synthesis finding to the source Q&A entries.

**D-outcome entries:** `Source Q&A:` must cite minimum two `Q&A-{seq:03d}` tokens drawn from different prompts (for inter-tier) or from the tier being synthesised (for intra-tier).

**F-outcome entries:** `Source Q&A:` must cite minimum one `Q&A-{seq:03d}` token showing what evidence ground the further-research question.

**N-outcome entries:** `Source Q&A:` must cite minimum one `Q&A-{seq:03d}` token showing what was considered in determining not-applicable.

**Revision sessions — superseded chapters:** Where a prior session produced Stage 2c prose chapters (under the v1.7 model), and a revision session is required, those chapters are superseded using the SUPERSEDE block format from §7. The superseded chapter format, citation discipline, and CC audit rules in §7 continue to apply to any legacy chapter that requires revision. New sessions under v1.8 produce synthesis entries, not chapters.

**CC post-parse audit:** The count of `wa_finding_catalogue_links` rows written for Stage 2c synthesis entries for the registry must be > 0. Unresolved Q&A token references (FK not populated) per synthesis entry > 20% raises `DATA_ANOMALY_SYNTHESIS_CITATION_GAP`.


### §10 Second-tier catalogue as Stage 2b question set

**The second-tier catalogue (T0–T7) is the operative question set for Stage 2b.** It replaced the prior ~155-question generic catalogue on 2026-04-30 (catalogue migration v2).

**Catalogue source:** Embedded in §L of the registry data package. Applied in full for every registry. No separate catalogue file is required.

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

**Prior analysis as source material:** Where a registry has been previously analysed using the old catalogue, those Q&A results are treated as Stage 2a source material — they form part of the observations base that the second-tier prompts interrogate. The second-tier prompts are still applied in full regardless. Each prompt receives a fresh answer grounded in the registry data; prior findings are input, not output.

**Status codes and notation tags:** These are used within Stage 2b Q&A entries as qualifiers and are embedded in the Q&A marker (see §8):

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

---

## Change Log

**v1_8 (2026-04-30):** Stage 2c rewritten as analytical synthesis pass. Specific changes:

1. **Stage 2c — purpose and output rewritten.** Stage 2c is no longer a prose chapter-writing stage. It is a structured synthesis pass producing `SYNTHESIS_INTRA_TIER` and `SYNTHESIS_INTER_TIER` findings recorded in the obslog. Session C reads these findings from the database to produce the reader-facing word story.
2. **T0 excluded from Stage 2c.** T0 findings from Stage 2b are held in the database for Session D. Stage 2c covers T1–T7 only (7 intra-tier entries + 21 inter-tier entries = 28 mandatory entries).
3. **Three-outcome structure.** Every synthesis entry carries exactly one outcome: D (Described) / F (Further research required) / N (Not applicable). N requires a one-sentence rationale. F always produces an SD pointer.
4. **New obslog markers.** `**SYN-INTRA-{registry:03d}-{seq:03d}**` and `**SYN-INTER-{registry:03d}-{seq:03d}**` added to §8 markers table.
5. **§2 DB targets table updated.** Stage 2c row now references `SYNTHESIS_INTRA_TIER` and `SYNTHESIS_INTER_TIER` findings written to `wa_session_b_findings`; `prose_section` row for six chapters removed.
6. **§4 citation discipline updated.** Stage 2b Q&A citation requirement retained; Stage 2c chapter citation rule replaced with synthesis entry `Source Q&A:` field requirement.
7. **§9 rewritten.** Chapter citation discipline replaced with synthesis entry citation discipline and CC audit rule.
8. **Six CC actions flagged in Stage 2c.** New finding types, five new metadata fields, parser extensions for SYN markers, 28-entry completeness audit, Session D routing confirmation, extract builder update.
9. **Integrity rules SB-2, SB-27, SB-29 updated.** SB-2: closure gate now requires 28 synthesis entries. SB-27: rewritten — Stage 2c produces synthesis entries, not prose chapters. SB-29 (new): exhaustive mandatory pass, T0 excluded, three-outcome structure required.
10. **Domain B closure check updated.** Anchor-verse-in-chapter-3 check removed (no Chapter 3). SPIRIT_SOUL_BODY check retained as T2 substantive treatment.
11. **Domain F closure check updated.** Six-chapter check replaced with 28-entry synthesis completeness check.
12. **Status Update block updated.** `Stage 2c chapters: [6]` replaced with synthesis entry counts.
13. **Handoff Signal updated.** Stage 2c summary now references synthesis entries, not chapters.

**v1_7 (2026-04-30):** Cleanup pass; v2 mechanics integrated into body, legacy patch and analytic-output-file material removed, instruction–DB alignment corrected.

1. **Outputs row** — restated as "obslog + session log" only. Stage 2c chapters live inside the obslog; no separate analytic-word-output file.
2. **§v2.x addendum integrated** into a renamed top section "Architecture v2 — operational spec" (§§1–10). The body's discipline now reads consistently with §v2.
3. **Type (b) Patch Construction section deleted** (was v1.6 lines 985–1017). Stage 2b Q&A capture is via obslog markers, parsed by CC.
4. **Closing Patch section deleted** (was v1.6 lines 1322–1334). `session_b_status` is set via the `## Session Close` block per §8 markers.
5. **Handoff Signal** reduced from five mandatory outputs to two (obslog, session log).
6. **Naming Conventions** trimmed from seven rows to two. Patch and analytic-word-output rows removed; supplementary Type (a) row moved to the readiness instruction where it logically belongs.
7. **Pipeline Position diagram** updated — closing-patch language replaced with "Status update in obslog → CC writes session_b_status".
8. **Stage 2c output** — restated as obslog blocks under `## Stage 2c — Chapter N: {title}` markers. The separate `wa-{NNN}-{word}-sessionb-analytic-v1-{date}.md` file is retired.
9. **question_code format aligned with DB** — the v1.6 RESEARCHER_DECISION flagging the `T{n}.{component}.P{prompt}` proposal is removed; the operative form is `T{n}.{component}.{prompt}` (no `P`), which matches the catalogue v2 DB rows written 2026-04-30.
10. **Citation token list extended** — §4 and §9 now recognise `OBS-{NNN}-T2-{seq}`, `SP-{NNN}-T2-{seq}`, `SB-{NNN}-T2-{seq}`, and `RD-{NNN}-{seq}` alongside the v1 forms. These are the formats today's catalogue-v2 capture writes.
11. **Domain E status check removed** — the v1.6 check `wa_finding_catalogue_links.status IN ('suggested','validated')` is dropped. Under v2 the link's `coverage` field carries the analytic meaning; `status` is functionally deprecated.
12. **Schema readiness gate** — extended with a check that `wa_obs_question_catalogue` carries ≥ 189 v2 rows (`catalogue_version='v2-2026-04-29'` and not deleted) — guards against a stale v1 catalogue still being on disk.
13. **Integrity rules SB-14, SB-15, SB-16, SB-17 rewritten** in v2 terms. Patch references replaced with obslog-and-CC-parser references. SB-28 unchanged.
14. **§v2.6 reconciliation paragraph** ("body remains authoritative for discipline") deleted — v1.7 has integrated v2 mechanics into the body, so no separate addendum is needed.

**v1_6 (2026-04-30):** Second-tier catalogue replaces §L catalogue as Stage 2b question set. Tier structure table (T0–T7), status codes (A/P/S/N), notation tags, prior-analysis-as-source-material rule, closing summary format, tier-specific notes, gap and new finding protocol added. Standalone second-tier output file retired. Q&A marker format updated to include Tier / Component / Prompt / Status tag / Notation fields.

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
     ├── Stage 2a: Comprehensive analysis → Observations log (in obslog)
     ├── Stage 2b: Second-tier Q&A partitioning (T0–T7) → Q&A log (in obslog)
     ├── Stage 2c: Analytical synthesis → 28 synthesis entries (7 intra-tier + 21 inter-tier, T1–T7) in obslog
     └── Closure
          ├── Closure checklist
          ├── Corrective action loop
          ├── Status update via `## Session Close` block in obslog → CC writes session_b_status
          └── Handoff signal → Session C open; Session D notified
          │
          ▼
Session C  (word study production — reads from database: Stage 2a observations + Stage 2b Q&A + Stage 2c synthesis entries)
          │
          ▼
Session D  (cross-registry synthesis — reads from database + SD pointers)
```

---

## What to Attach at Session Start

**Two `.md` files are the entire session-start input for an initial analysis**. The second-tier catalogue is embedded in §L of the registry data package — there is no separate catalogue file.

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

**Stage 2c synthesis pass:** No additional file is required. Stage 2c reads from the Stage 2b Q&A log already in the obslog.

Do not load more data into the working session than the current stage requires.

---

## Governing Disciplines

These disciplines apply without exception across all stages, all sessions.

**Step-by-step.** Per GR-PROC-001. Each stage and each step within it is completed and confirmed before the next begins.

**Write on discovery.** Per GR-OBS-001 (non-waivable). Every observation, SD pointer, decision, and open question is written to the obslog at the moment it is determined. Nothing is accumulated in memory.

**All observations return to the database.** Per GR-OBS-006. Every analytical observation produced in Stage 2a must be addressed in Stage 2b and any that produce structured findings must be persisted before closure. Session C and Session D read from the database only.

**Data is authoritative.** Per GR-PROC-002. Work strictly from what is in the registry data package. Do not import general knowledge to fill gaps.

**Obslog is the single output, parsed by CC.** Per §2 above. No patches, no separate analytic-word-output file. All writes flow through CC's Phase 2 obslog parser.

**No DB state assumptions.** Per GR-DB-001. Claude AI never assumes the current state of the database.

**Cross-registry vision is always active.** Per GR-PROG-002. Every piece of data read in Stage 2a is read twice: once for what it says about this word, once for what it says about something beyond this word. SD pointers are raised continuously — not accumulated for a final pass. Per integrity rule SB-11.

**Characteristic-perspective grouping model.** Per GR-PROG-006. Every anchor verse is read with its group description as the interpretive lens. The group description names what the characteristic is that the verse is engaging. This is the reading frame — not the verse's general theme.

**Stage 2a is free-form. Stage 2b is structured.** Stage 2a produces observations without imposed structure. Stage 2b produces structured Q&A pairs governed by the second-tier catalogue. Do not attempt to structure Stage 2a observations as Q&A pairs during Stage 2a — this conflates two distinct stages and corrupts both.

**Researcher decision items.** Per GR-RD-001 through GR-RD-006. Last resort only. Before raising any item, exhaust analytical resources. Recorded in the obslog under `## RESEARCHER_DECISION Accumulator — Final` per §8 markers.

**Session logs at every breakpoint.** Per GR-PROC-006.

---

## Schema Readiness Gate

Before Stage 2a begins, confirm with CC that the following database conditions are met. If any condition fails, resolve before proceeding. This gate runs once per word — not at every session start.

| Condition | Check | Fail action |
|-----------|-------|------------|
| `wa_obs_question_catalogue` carries ≥ 189 v2 rows | `SELECT COUNT(*) FROM wa_obs_question_catalogue WHERE catalogue_version='v2-2026-04-29' AND (deleted=0 OR deleted IS NULL)` | If <189: catalogue v2 not loaded — raise with researcher |
| `wa_finding_catalogue_links` table exists | CC schema check | Raise CC directive — schema gap |
| `wa_session_b_findings.status` column exists | CC schema check | Raise CC directive — schema gap |
| `wa_session_b_findings.term_id` column exists | CC schema check | Raise CC directive — schema gap |
| Registry-specific catalogue questions present in §L | Count from second-tier catalogue section of data package | If 0: word-specific questions not yet indexed — raise with researcher |

Record in obslog: `Schema readiness gate: [n] conditions checked. All pass / [n] fail — [detail].`

---

## Stage 2a — Comprehensive Analysis

### Purpose

Stage 2a produces a comprehensive free-form narrative of everything the data says about this word. It is the analytical foundation for all subsequent work. It is not structured, not formatted for reading, and not organised by any external framework. It is the full working out of what the clean extract contains.

Stage 2a is complete when every element of the extract has been read, everything the data says has been recorded in the obslog, and the obslog's Stage 2a portion has been confirmed. After sign-off, the Stage 2a observations are fixed — they do not change in Stage 2b or 2c.

Stage 2a does not produce database writes directly. CC's writer parses Stage 2a observations from the obslog after the session closes (or at intermediate breakpoints if the session is paused).

---

### Stage 2a Tracking Sections

Open the obslog immediately and create these four named sections before reading any data:

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

**SD Pointer Accumulator format** — uses the §8 SD pointer marker.

**RESEARCHER_DECISION Accumulator format** — uses the §8 RD marker.

**Path 3 Resolution format — each entry:**
```
PATH 3 RESOLUTION [seq]: [date]
  Stage 1 Path 3 note: [original note reference]
  Field: [table.field on term/group]
  Stage 1 value: [what was recorded as provisional]
  Verse evidence: [verse reference and what it shows]
  Resolution: CONFIRMED [value] / CORRECTED TO [value] / REMAINS UNCERTAIN
  Correction required: YES — [correction] / NO
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
Read the Stage 2a Progress Record section of the obslog.

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

Record in obslog:
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

**SD pointer naming check:** Verify each existing SD pointer `flag_label` follows `[NNN]-SD[seq]` (or `SP-{NNN}-{seq}` for pre-T2 sources, `SP-{NNN}-T2-{seq}` for T2 sources) with zero-padded three-digit registry number. Any inconsistency: record as a RESEARCHER_DECISION item.

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
- Obslog Stage 2a portion confirmed — no in-memory observations remain unwritten

**Sign-off statement:**
```
STAGE 2A COMPLETE — Registry [NNN] ([word])
Date: [date]
Extract version: [version]
Reading units completed: 9 of 9
Obslog Stage 2a portion: confirmed
SD pointers accumulated: [n]
Path 3 notes resolved: [n of n]
Existing findings reviewed: [n]
Anchor verses read: [n] across [n] groups across [n] terms

Stage 2a observations are now fixed. Stage 2b may begin.
```

---

### Fallback Protocol — Stage 2a

**Session interrupted mid-unit:** Resume from the last group sign-off or the last unit sign-off recorded in Stage 2a Progress Record.

**Observation recorded but not fully developed:** Develop it before moving to the next item. Do not skip partial observations.

**Path 3 item requires correction:** Record the correction needed in the Path 3 Resolution Notes. Apply a supplementary Type (a) patch (per readiness instruction) before Stage 2b begins.

---

### Session Close Protocol — Stage 2a

**C1 — Complete the current group or reach a group boundary.**

**C2 — Verify the four tracking sections are current.**
SD Pointer Accumulator, RESEARCHER_DECISION Accumulator, Path 3 Resolution Notes, Stage 2a Progress Record — all updated.

**C3 — Produce the session log.**
Current position; units completed; outstanding units; SD pointers accumulated; Path 3 items resolved; exact resume instructions.

**C4 — Confirm obslog is up to date.**
All observations from this session written into the obslog. No observations remaining only in working memory.

---

## Stage 2b — Second-Tier Q&A Partitioning

### Purpose

Stage 2b applies the second-tier catalogue (T0–T7, embedded in §L of the registry data package) to the Stage 2a observations, producing a structured Q&A record for every prompt. The catalogue drives what is asked. Stage 2a provides the evidence. Stage 2b is the bridge between them.

The catalogue works tier by tier (T0 → T1 → T2 → T3 → T4 → T5 → T6 → T7). Each tier is completed in full before the next begins. Within a tier, each component is completed before moving to the next component.

Stage 2b output is recorded in the obslog under §8 markers. CC's writer parses these markers and writes the Q&A links and any new finding rows after session close.

Stage 2b is iterative and multi-session capable. Each session works through one or more tiers. Stage 2b is complete when all prompts across all eight tiers have a recorded disposition in the obslog Q&A log.

---

### Stage 2b Inputs

- Stage 2a observations (in obslog) — fixed, confirmed
- Second-tier catalogue from §L of the registry data package (T0–T7)
- Stage 1 Completion Record (for context — not modified)
- Prior analysis Q&A results where the registry has been previously analysed (treated as source material, not output)

**If any Path 3 corrections were identified in Stage 2a:** apply a supplementary Type (a) patch (per readiness instruction) to correct these fields before Stage 2b begins. Request a fresh extract after the patch is confirmed.

---

### Stage 2b Tracking Document Structure

The obslog carries the SD Pointer Accumulator, RD Accumulator, and Progress Record from Stage 2a. Stage 2b adds:

```
### Stage 2b Q&A Log
[Populated during Stage 2b — one entry per prompt, grouped by tier]

#### Stage 2b Progress Record
[Updated at each tier sign-off]
```

**Q&A Log entry format** (per §8 marker — reproduced for convenience):
```
**Q&A-{seq:03d} | {tier_prompt_code}**
- Tier: {T0|T1|...|T7} — {tier title}
- Component: {component code e.g. T1.3}
- Prompt: {N} — {full prompt text from catalogue}
- Disposition: ANSWERED | PARTIALLY ANSWERED | NOT APPLICABLE | NOT ANSWERED
- Status tag: A | P | N | S
- Notation: {tag(s) — see §10}
- Answer: {drawn directly from Stage 2a observations — OBS-NNN citations required for ANSWERED/PARTIAL}
- Anchor verses: {verse references}
- Finding type: {controlled vocabulary}
- Stage 2b note: {optional qualifier}
```

`{tier_prompt_code}` follows `T{n}.{component}.{prompt}` (e.g. `T1.3.2` — no `P` prefix).

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
Read through the Stage 2a observations. Identify all observations that bear on this prompt. Do not generate new analysis — draw only from what Stage 2a contains. Where prior analysis Q&A results exist for this registry, treat them as additional source material alongside Stage 2a observations.

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
One or more from: *Consistent with prior analysis* / *Adds structure* / *New finding* / *Gap identified*. See §10 for definitions.

**Step 5 — Write the Q&A entry:**
For ANSWERED and PARTIALLY ANSWERED: write the full answer in the obslog under the Q&A marker. Draw directly from Stage 2a. Cite observations as `OBS-{NNN}-{seq}`. Do not introduce new analysis.

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
| OBSERVATION | Generic — when none of the more specific types fits cleanly |

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
- If superseded: mark with a SUPERSEDE block in the obslog (CC's writer flips `delete_flag = 1` and sets `superseded_by_id`).
- If set-aside: mark with a SET_ASIDE block (CC's writer flips `delete_flag = 1` with `obsolete_reason`).

Format:
```
### SUPERSEDE: {finding_id}
**superseded_by:** {new finding_id}
**reason:** {short explanation}

### SET_ASIDE: {finding_id}
**obsolete_reason:** {reason from controlled vocabulary}
```

---

### Closing Summary

After all eight tiers are complete, append the Stage 2b closing summary (per §10):

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

CC's writer can read this summary to verify counts, but the source of truth is the per-prompt Q&A entries above.

---

### Stage 2b Sign-Off Checklist

| Item | Required state |
|------|---------------|
| All eight tiers (T0–T7) processed | Disposition recorded for every prompt in obslog |
| NOT ANSWERED (S) prompts | All Stage 2a reopening units complete and Stage 2b re-run for affected prompts |
| SD pointer review complete | All pointers confirmed, refined, or merged |
| Existing findings review complete | Supersessions/obsoletions marked in obslog |
| Closing summary produced | Status code totals, key gaps, new findings consolidated |
| Q&A Log section in obslog complete | Every prompt has a `**Q&A-{seq} | {tier_prompt_code}**` block |
| `evidential_status` set on all active OWNER terms | No NULLs (raised as RD if blocked) |

**Sign-off statement:**
```
STAGE 2B COMPLETE — Registry [NNN] ([word])
Date: [date]
Tiers processed: T0 through T7 (8 tiers)
Prompts: [n total]. Answered: [n]. Partially answered: [n]. Not applicable: [n]. Not answered (S): [n].
New findings recorded in obslog: [n]
Catalogue links recorded in obslog: [n]
SD pointers in accumulator: [n]
evidential_status set on all active OWNER terms: confirmed

Stage 2c may begin.
```

---

### Fallback Protocol — Stage 2b

**Session interrupted mid-tier:** Resume from the last Q&A entry in the Q&A Log within the current tier.

**NOT ANSWERED (S) prompt requires Stage 2a reopening:** Add a targeted unit to Stage 2a (Unit 10, 11, etc.). Return to Stage 2b after the unit sign-off.

**SD pointer count mismatch on CC's parse:** Treated as a CC-side anomaly (`DATA_ANOMALY_*`). AI re-checks the SD Pointer Accumulator markers conform to §8 format and re-submits the obslog if needed.

---

### Session Close Protocol — Stage 2b

**C1 — Complete the current tier or reach a tier boundary.**

**C2 — Verify tracking sections are current.**
Q&A Log, SD Pointer Accumulator, Progress Record all updated in obslog.

**C3 — Produce session log.**
Current tier position; tiers completed; outstanding tiers; SD pointer count.

**C4 — Confirm obslog is up to date.**

---



---

## Stage 2c — Analytical Synthesis

### Purpose

Stage 2c is a structured synthesis pass over the Stage 2b Q&A record. Its purpose is to examine what the T1–T7 findings reveal *in relation to each other* — patterns, dependencies, tensions, and structural connections that emerge from reading the tiers together, and that no single prompt answer states on its own.

Stage 2c produces **synthesis entries** recorded in the obslog and written to the database by CC's writer. These entries are the bridge between the analytical interrogation of Stage 2b and the reader-facing narrative of Session C.

**T0 is out of scope for Stage 2c.** T0 findings from Stage 2b are held in the database and drawn on directly by Session D for cross-registry synthesis. The per-word story (Session C) does not carry T0 content. Stage 2c does not process T0 at all.

**Stage 2c does not produce prose.** It produces structured synthesis entries. Session C reads from the database — Stage 2a observations, Stage 2b Q&A record, and Stage 2c synthesis entries — and writes the reader-facing word story from that complete record.

**No new analysis is introduced in Stage 2c.** Every synthesis entry must be grounded in named Stage 2b Q&A entries. A synthesis claim that cannot be traced to at least two Stage 2b Q&A entries is not a valid synthesis entry — it is new analysis and belongs in a Stage 2a reopening unit.

---

### Two Types of Synthesis Entry

**Intra-tier synthesis** — what emerges from reading one tier as a whole, across its component prompt answers, that no individual prompt answer states.

An intra-tier entry assembles the component answers within a single tier into a pattern or structural statement. It asks: what does this tier reveal about this characteristic as a whole?

**Inter-tier synthesis** — what emerges from reading two tiers together, identifying structural relationships, dependencies, or tensions between analytical domains.

An inter-tier entry names a connection between what one tier found and what another tier found — where the two findings taken together reveal something neither states alone.

---

### Scope and Coverage

The synthesis pass covers **T1 through T7 only**. T0 is excluded entirely.

**Intra-tier pass:** 7 entries — one per tier (T1, T2, T3, T4, T5, T6, T7). All 7 are mandatory.

**Inter-tier pass:** 21 entries — one per unique tier pair within T1–T7. All 21 are mandatory.

The 21 tier pairs are:

| Pair | | Pair | | Pair |
|---|---|---|---|---|
| T1 × T2 | | T2 × T5 | | T3 × T7 |
| T1 × T3 | | T2 × T6 | | T4 × T5 |
| T1 × T4 | | T2 × T7 | | T4 × T6 |
| T1 × T5 | | T3 × T4 | | T4 × T7 |
| T1 × T6 | | T3 × T5 | | T5 × T6 |
| T1 × T7 | | T3 × T6 | | T5 × T7 |
| T2 × T3 | | | | T6 × T7 |
| T2 × T4 | | | | |

**Total mandatory Stage 2c entries: 28** (7 intra + 21 inter). CC's parser verifies this count at post-parse audit. A count below 28 raises `DATA_ANOMALY_SYNTHESIS_INCOMPLETE`.

---

### Three Outcomes — Every Entry

Every synthesis entry — intra-tier and inter-tier — carries exactly one of three outcomes:

| Outcome | Code | Meaning |
|---|---|---|
| **Described** | D | A substantive synthesis finding is recorded — a pattern, dependency, tension, or structural connection that the tier(s) reveal in combination |
| **Further research required** | F | The data raises a question that cannot be resolved from current evidence — an SD pointer is written immediately |
| **Not applicable** | N | The tier or tier combination genuinely produces no structural relationship for this word — stated explicitly with a one-sentence rationale |

**Outcome N is a complete and valid finding.** It is not a default or a skip. A one-sentence rationale is required — "these tiers do not interact for this word because [reason]" is a finding about the characteristic's structure. An entry with no rationale for N is not valid.

**Outcome F always produces an SD pointer.** Write the SD pointer to the SD Pointer Accumulator immediately per GR-OBS-001. The synthesis entry cites the pointer.

---

### Obslog Markers for Stage 2c

Stage 2c entries are recorded in the obslog in a dedicated section, parsed by CC's writer.

**Section header:**
```
## Stage 2c — Synthesis Entries
```

**Intra-tier synthesis entry marker:**
```
**SYN-INTRA-{registry:03d}-{seq:03d}** | T{N} — {tier title}
- Entry type: SYNTHESIS_INTRA_TIER
- Tier: T{N}
- Components considered: {all component codes in this tier, e.g. T2.1, T2.3, T2.6, T2.8, T2.10}
- Source Q&A: {Q&A-seq, Q&A-seq, ... — for outcome D: minimum two entries; for F and N: one or more}
- Outcome: D | F | N
- Finding: {for D — the synthesis finding; for F — the research question; for N — the rationale}
- Session C chapter: {Ch1 | Ch2 | Ch3 | Ch4 | Ch5 | multiple: Ch2, Ch5 | N/A}
- SD pointer: {SP-{registry:03d}-{seq:03d} — for outcome F only; else NONE}
```

**Inter-tier synthesis entry marker:**
```
**SYN-INTER-{registry:03d}-{seq:03d}** | T{N} × T{N}
- Entry type: SYNTHESIS_INTER_TIER
- Tiers: T{N}, T{N}
- Source Q&A: {Q&A-seq, Q&A-seq, ... — for outcome D: minimum two entries from different tiers}
- Outcome: D | F | N
- Finding: {for D — the synthesis finding; for F — the research question; for N — the rationale}
- Structural relationship: {causal | enabling | sequential | constitutive | tension | parallel | N/A}
- Session C chapter: {Ch1 | Ch2 | Ch3 | Ch4 | Ch5 | multiple | N/A}
- SD pointer: {SP-{registry:03d}-{seq:03d} — for outcome F only; else NONE}
```

- `{seq}` is sequential across both intra- and inter-tier entries within a registry (001..NNN)
- For outcome D: `Source Q&A` must name at least two Q&A entries; for F and N: at least one
- For outcome D: `Structural relationship` names the type of connection found (inter-tier only)
- For outcome N: `Structural relationship` is `N/A`; `Session C chapter` is `N/A`
- `Session C chapter` guides CC's extract builder in surfacing findings for Session C

---

### Stage 2c Process

#### Step 1 — Intra-tier pass (T1 → T7)

Work through each tier in order: T1, T2, T3, T4, T5, T6, T7.

For each tier:

1. Read all Q&A entries for the tier in the obslog — every prompt answer across every component.
2. Consider the tier as a whole: what does it reveal about this characteristic that no individual prompt states? Is there a pattern, structural shape, movement, or tension across the components?
3. Assign an outcome (D, F, or N) and write the `SYN-INTRA` entry.
4. If outcome F: write the SD pointer immediately to the SD Pointer Accumulator.

**Do not skip any tier.** A tier with thin evidence or mostly N-status prompts in Stage 2b will typically produce an intra-tier outcome of N — but the entry must still be written with its rationale.

**Tier sign-off:**
```
T{N} intra-tier COMPLETE: [date]. Outcome: D | F | N.
```

After all seven tiers: `Intra-tier pass COMPLETE: [date]. D: [n]. F: [n]. N: [n]. Total: 7.`

---

#### Step 2 — Inter-tier pass (all 21 pairs)

Work through all 21 tier pairs in the order listed in the coverage table above (T1×T2 through T6×T7).

For each pair:

1. Read the intra-tier entries for both tiers, and the relevant Q&A entries underlying them.
2. Consider the two tiers in relation: does what one tier found interact with, depend on, qualify, or tension what the other tier found?
3. Assign an outcome (D, F, or N) and write the `SYN-INTER` entry.
4. If outcome F: write the SD pointer immediately.

**Do not skip any pair.** The 21-pair structure is exhaustive by design. An outcome of N with a one-sentence rationale is a complete and valid entry.

**Pair sign-off (after every five pairs or at natural session break):**
```
Inter-tier pairs complete to [T{N}×T{N}]: [date]. Running count: [n of 21].
```

After all 21 pairs: `Inter-tier pass COMPLETE: [date]. D: [n]. F: [n]. N: [n]. Total: 21.`

---

#### Step 3 — Synthesis review

After both passes are complete:

1. Read all 28 entries (7 intra + 21 inter) together.
2. Ask: does the set produce a coherent portrait of the characteristic? Are there structural contradictions between entries? Are there tensions that are themselves analytically significant?
3. Where a structural contradiction exists between a D outcome in one entry and a D outcome in another: record it explicitly — add a note to both entries and write a new `SYN-INTER` entry for the contradicting pair if one does not exist, with outcome D and `Structural relationship: tension`.
4. Where a Stage 2b gap (S-status prompt) has produced a synthesis gap: confirm an SD pointer has been raised. Do not write a D-outcome synthesis finding that papers over a Stage 2b gap.
5. Count: confirm 28 total entries (7 + 21). If short: identify the missing entry and complete it before close.

Record: `Synthesis review COMPLETE: [date]. Entries: [28]. D: [n]. F: [n]. N: [n]. Contradictions named: [n]. SD pointers raised in Stage 2c: [n]. Stage 2b gaps confirmed covered: [n].`

---

### What Stage 2c Does Not Do

- **Does not process T0.** T0 is Session D material. No SYN-INTRA entry for T0.
- **Does not write prose.** Session C writes the reader-facing narrative.
- **Does not introduce new analysis.** Every D-outcome entry traces to Stage 2b Q&A entries.
- **Does not resolve SD pointers.** Outcome F raises new ones. Existing SD pointers are not closed in Stage 2c.
- **Does not supersede Stage 2b findings.** A Stage 2b finding that appears wrong in light of synthesis requires a SUPERSEDE block in the obslog — not a synthesis entry that overrides it.
- **Does not skip entries.** All 28 are mandatory. Outcome N is not a skip — it is a finding.

---

### Session C Relevance Tagging

Every D-outcome synthesis entry carries a `Session C chapter` field. This guides CC's extract builder in surfacing the right findings for Session C's prose production.

| Chapter | Content | Primary synthesis input |
|---|---|---|
| Ch1 — What it is | Name, kind, boundary, semantic range | T1 intra; T1×T7 inter |
| Ch2 — How it works | Operations, faculties, constitutional location, relational axis, formative dimension | T2, T3, T4, T5 intra; T2×T3, T3×T5, T4×T5, T2×T4 inter |
| Ch3 — Verses | Anchor verse evidence | T7 intra (literary component); any inter entry with verse grounding |
| Ch4 — Language | Original language precision, somatic grounding, translation | T7 intra (lexical component); T2×T7, T1×T7 inter |
| Ch5 — Interrelationships | Cross-registry connections, structural relationships | T6 intra; T6×T2, T6×T4, T6×T5 inter |

A synthesis entry may be relevant to more than one chapter — list all that apply separated by commas. N-outcome entries carry `Session C chapter: N/A`.

---

### CC Actions Required — Stage 2c

The following database actions are required before Stage 2c is first applied. These are flagged for CC to implement.

**Action 1 — New finding types in `wa_session_b_findings`:**
Add two new controlled values to the `finding_type` field:
- `SYNTHESIS_INTRA_TIER`
- `SYNTHESIS_INTER_TIER`

**Action 2 — New fields on `wa_session_b_findings` (or linked metadata table):**
Synthesis entries carry metadata not currently held on findings. Required fields:
- `synthesis_outcome` — controlled vocabulary: `D | F | N`
- `tiers_engaged` — text; comma-separated tier codes (e.g. `T2` or `T2,T3`)
- `structural_relationship` — text; controlled vocabulary: `causal | enabling | sequential | constitutive | tension | parallel | N/A`
- `session_c_chapter` — text; comma-separated chapter references (e.g. `Ch2,Ch5`) or `N/A`
- `sd_pointer_ref` — text; `SP-{registry:03d}-{seq:03d}` for F-outcome entries; NULL otherwise

CC advises whether these are added as columns on `wa_session_b_findings` or as rows in a linked metadata table.

**Action 3 — Parser extension for `SYN-INTRA` and `SYN-INTER` markers:**
CC's obslog parser must recognise:
- `**SYN-INTRA-{registry:03d}-{seq:03d}**` — writes as `SYNTHESIS_INTRA_TIER` finding
- `**SYN-INTER-{registry:03d}-{seq:03d}**` — writes as `SYNTHESIS_INTER_TIER` finding

And must extract and write all bullet fields per Action 2, plus:
- `source_qa_links` from `Source Q&A:` — written as `wa_finding_catalogue_links` rows linking the synthesis finding to the source Q&A entries

**Action 4 — Completeness audit:**
CC's post-parse audit must verify:
- Intra-tier count = 7 (T1 through T7; T0 absent is correct)
- Inter-tier count = 21 (all pairs within T1–T7)
- Total = 28
- Any count below 28 raises `DATA_ANOMALY_SYNTHESIS_INCOMPLETE` for the registry

**Action 5 — Session D routing for F-outcome entries:**
All F-outcome synthesis entries have a corresponding SD pointer in `wa_session_research_flags`. CC confirms whether the `sd_pointer_ref` field on the synthesis finding is sufficient to link them, or whether an explicit FK column is required.

**Action 6 — Extract builder update (`build_complete_extract.py`):**
The `--scope=final` extract for Session C must include Stage 2c synthesis entries, organised as:
- Intra-tier D-outcome entries grouped by tier, with Session C chapter tag
- Inter-tier D-outcome entries grouped by primary tier combination, with Session C chapter tag
- F-outcome entries listed separately as open research questions (with SD pointer reference)
- N-outcome entries omitted from Session C extract (held in DB for programme record)
- T0 Q&A findings from Stage 2b surfaced separately for Session D extract

---

### Stage 2c Sign-Off Checklist

| Item | Required state |
|---|---|
| Intra-tier pass complete | 7 entries: T1 through T7. Count confirmed. |
| Inter-tier pass complete | 21 entries: all pairs within T1–T7. Count confirmed. |
| Total entries | 28. Any shortfall identified and resolved before sign-off. |
| Every entry has an outcome (D, F, or N) | No entries without outcome code |
| Every N-outcome entry has a one-sentence rationale | No bare N entries |
| Every D-outcome entry with inter-tier scope names structural relationship | No blank structural relationship on inter-tier D entries |
| Every F-outcome entry has an SD pointer in the accumulator | SD pointer written per GR-OBS-001 |
| Every D-outcome entry cites minimum two Stage 2b Q&A sources | No unsourced synthesis claims |
| T0 absent from intra-tier and inter-tier entries | No SYN-INTRA or SYN-INTER entry for T0 |
| Synthesis review complete | Contradictions named; 28-entry count confirmed |

**Sign-off statement:**
```
STAGE 2C COMPLETE — Registry [NNN] ([word])
Date: [date]
Intra-tier entries: 7 (T1–T7). D: [n]. F: [n]. N: [n].
Inter-tier entries: 21 (all T1–T7 pairs). D: [n]. F: [n]. N: [n].
Total: 28.
SD pointers raised in Stage 2c: [n]
Contradictions named: [n]
T0: excluded — Session D.

Closure may begin.
```

---

### Fallback Protocol — Stage 2c

**Session interrupted mid-pass:** Resume from the last completed sign-off. The intra-tier pass records tier-by-tier sign-offs; the inter-tier pass records running counts every five pairs. Identify the last recorded position and continue from the next entry.

**Synthesis finding cannot be sourced to two Stage 2b Q&A entries:** Do not write a D-outcome entry. If the pattern is analytically real, the source evidence is missing from Stage 2b — reopen Stage 2a for the relevant unit and extend Stage 2b accordingly before returning to Stage 2c.

**Inter-tier pair count does not reach 21:** Identify the missing pair(s) from the 21-pair table. Complete the missing entries before sign-off. Do not close Stage 2c short.

**T0 entry mistakenly written:** Remove it from the obslog before close. T0 content does not belong in Stage 2c.

---

---

## Closure

### Purpose

Closure verifies that the obslog is complete and correctly formatted, runs the closure checklist, and produces the formal handoff. CC's writer then parses the obslog and writes everything to the database.

---

### Closure Checklist

Run against the obslog at session close. Every item must pass. (Domains run within the obslog itself; CC's post-parse audit re-verifies the database state.)

**Domain A — Data completeness**

| Check | Pass condition | Fail action |
|-------|---------------|------------|
| All active OWNER terms have `evidential_status` set | No NULLs | Identify unset terms; address before close |
| All active OWNER terms have `mti_terms.status` set | No NULLs on active terms | Identify; address |
| `verse_context_status` | `Complete` | Investigate |
| All dimension index groups at `CLAUDE_AI` or `RESEARCHER` confidence | No AUTOMATED remaining | Run Dimension Review sub-process |
| `dominant_subject` set on all dimension index rows | No NULLs | Address correctable ones; RESEARCHER_DECISION for unclear |

**Domain B — Findings completeness**

| Check | Pass condition | Fail action |
|-------|---------------|------------|
| At least one active MEANING_OBSERVATION finding (or T1/T7.1 Q&A entry that supplies the equivalent) | Count > 0 | Stage 2a/2b gap — reopen |
| SPIRIT_SOUL_BODY treatment present | T2 tier substantively addressed in Stage 2b | Stage 2a/2b gap — reopen |
| No `thin_evidence = 1` findings unresolved | All thin findings dispositioned | Disposition in Stage 2b |
| No prior-phase findings with `delete_flag = 0` and disposition 'questioned' | All reviewed and actioned | Return to Stage 2b existing findings review |

**Domain C — Flag resolution**

| Check | Pass condition | Fail action |
|-------|---------------|------------|
| Zero `wa_session_research_flags` with `session_target = 'B'` and `resolved = 0` | Hard gate | Identify; resolve before closure |
| SD pointer accumulator count matches the per-tier raised totals | Hard gate | Re-check SD Pointer Accumulator |
| All `wa_term_phase2_flags` dispositioned | Confirmed, rejected, or irrelevant noted | Return to Stage 1 Step 1.3a |

**Domain D — Entity links**

| Check | Pass condition | Fail action |
|-------|---------------|------------|
| Every Stage 2b Q&A entry with status A or P cites at least one OBS reference | No orphan answers | Add OBS citation |
| Every SUPERSEDE block names the superseding finding | No dangling supersedes | Address before close |

**Domain E — Catalogue links (verified post-CC-parse)**

| Check | Pass condition | Fail action |
|-------|---------------|------------|
| Every active v2 finding has a `wa_finding_catalogue_links` row | No findings without catalogue link | CC's parser raises `DATA_ANOMALY_FINDING_UNCITED` — address in next session |

**Domain F — Stage 2c Synthesis**

| Check | Pass condition | Fail action |
|-------|---------------|------------|
| Intra-tier entries: 7 (T1–T7) | Count = 7; T0 absent | Identify missing tier; complete before close |
| Inter-tier entries: 21 (all T1–T7 pairs) | Count = 21 | Identify missing pair from 21-pair table; complete before close |
| Total synthesis entries | Count = 28 | Hard gate — must reach 28 before closure |
| Every entry has an outcome (D / F / N) | No entries without outcome code | Address before close |
| Every N-outcome entry has a one-sentence rationale | No bare N entries | Add rationale |
| Every F-outcome entry has SD pointer in accumulator | SD pointer written per GR-OBS-001 | Write missing pointer before close |
| Every D-outcome inter-tier entry names structural relationship | No blank structural relationship field | Add before close |

---

### Corrective Action Loop

If any domain fails:

1. Identify the specific gap.
2. Determine corrective action: obslog revision / supplementary observation / stage reopening / researcher decision.
3. Apply correction in the obslog.
4. Re-run only the failed domain check — not the full checklist.
5. If unresolvable within Analysis Output: raise a RESEARCHER_DECISION item per GR-RD-002. Record in the RESEARCHER_DECISION Accumulator until resolved.

---

### Status Update at Session Close

When the closure checklist is clean:

Add the `## Session Close` block to the obslog with the new status:

```markdown
## Session Close

session_b_status: 'Analysis Complete'

Final counts:
- Stage 2a observations: [n]
- Stage 2b Q&A entries: [n] (A: [n], P: [n], S: [n], N: [n])
- SD pointers raised: [n]
- RESEARCHER_DECISION items: [n]
- Stage 2c synthesis entries: [28] (Intra D: [n] F: [n] N: [n] / Inter D: [n] F: [n] N: [n])
```

CC's writer reads this block, updates `word_registry.session_b_status`, and runs its post-parse audit. If the audit raises anomalies, they appear as `DATA_ANOMALY_*` findings for the next session to address.

Record in obslog: `Session Close block added. session_b_status set to Analysis Complete. Registry [NNN] [word] Analysis Output complete pending CC parse.`

---

### Handoff Signal

After the `## Session Close` block is written:

```
ANALYSIS OUTPUT COMPLETE — Registry [NNN] ([word])
Date: [date]

Stage 2a: COMPLETE — observations recorded in obslog
Stage 2b: COMPLETE — [n] prompts across T0–T7; [n] new findings; [n] SD pointers raised
Stage 2c: COMPLETE — 28 synthesis entries (7 intra T1–T7 + 21 inter T1–T7 pairs); [n] SD pointers raised; [n] D-outcome findings

Closure: COMPLETE — all domains pass; Session Close block in obslog

Mandatory outputs confirmed:
  [ ] Comprehensive obslog: wa-{NNN}-{word}-obslog-v{n}-{date}.md
  [ ] Session log: wa-{NNN}-{word}-sessionb-sessionlog-v{n}-{date}.md

Session C: OPEN — pending CC's post-parse audit clean.
Session D: NOTIFIED — [n] SD pointers awaiting synthesis.
```

---

## Integrity Rules

| Rule | Status | Text |
|------|--------|------|
| SB-1 | From Analysis Readiness | Stage 2a does not begin until the Stage 1 Completion Record confirms all seven domains pass |
| SB-2 | v1.8 | Closure does not begin until Stage 2a is signed off, Stage 2b Q&A log is complete in the obslog, and Stage 2c synthesis pass is complete with 28 entries (7 intra-tier T1–T7 + 21 inter-tier T1–T7 pairs) recorded in the obslog |
| SB-7 | Retained — applies to legacy chapters and Session C output | Confirmed cross-registry connections must be supported by at least one correlation signal |
| SB-8 | Retained — applies to legacy chapters and Session C output | A connection supported by a correlation signal must not be omitted from the interrelationship account |
| SB-9 | Unchanged | Cross-word synthesis conclusions are not permitted in Analysis Output — questions only |
| SB-11 | Unchanged | SD pointers are raised throughout Stage 2a at the moment of discovery per GR-OBS-001 — not accumulated for a final stage |
| SB-12 | Unchanged | Every anchor verse is read with all five cross-registry vision questions applied (Stage 2a Unit 7) |
| SB-13 | Retired | Pass 6 SD pointer rule replaced by SB-11 |
| SB-14 | v1.7 rewrite | SD pointer persistence is the responsibility of CC's obslog parser. AI's responsibility is that every SD pointer raised in any unit appears under `## SD Pointer Accumulator — Final` per §8 markers before session close |
| SB-15 | v1.7 rewrite | SD Pointer Accumulator entries must be syntactically valid per §8. CC's parser counts and writes; AI does not perform a separate count-verification step |
| SB-16 | v1.7 rewrite | The `## Session Close` block in the obslog with `session_b_status:` is mandatory. Analysis Output does not close without this block in the obslog |
| SB-17 | v1.7 rewrite | Analysis Output does not close without both mandatory outputs: comprehensive obslog and session log |
| SB-18 | From Analysis Readiness | Zero open `wa_session_research_flags` with `session_target = 'B'` and `resolved = 0` — confirmed in Closure Domain C |
| SB-25 | Unchanged | Stage 2a observations are fixed after Stage 2a sign-off. Stage 2a reopening adds new units with sequential numbering — does not modify existing entries |
| SB-26 | Unchanged | Stage 2b draws only from Stage 2a. No new analysis introduced in Stage 2b. A Q&A answer not grounded in a named Stage 2a observation is not valid — Stage 2a must be reopened |
| SB-27 | v1.8 rewrite | Stage 2c draws only from Stage 2b Q&A pairs. It produces synthesis entries (SYNTHESIS_INTRA_TIER and SYNTHESIS_INTER_TIER findings), not prose chapters. No new analysis is introduced in Stage 2c. A synthesis entry that cannot be traced to at least two Stage 2b Q&A entries (for D-outcome) or at least one (for F and N outcomes) is not a valid Stage 2c entry |
| SB-28 | Unchanged | Stage 2b processes all eight second-tier tiers (T0–T7) in sequence. No tier may be skipped. A tier is complete only when every prompt within it has a recorded disposition |
| SB-29 | New v1.8 | Stage 2c is exhaustive and mandatory. All 7 intra-tier entries (T1–T7) and all 21 inter-tier entries (unique pairs within T1–T7) must be present in the obslog before Stage 2c sign-off. T0 is excluded from Stage 2c scope — T0 findings belong to Session D. Every entry carries exactly one of three outcomes: D (Described), F (Further research required), or N (Not applicable). Outcome N requires a one-sentence rationale. Outcome F requires an SD pointer entry in the SD Pointer Accumulator written immediately per GR-OBS-001 |

---

## Naming Conventions

| Output | Pattern | Example |
|--------|---------|---------|
| Comprehensive obslog | `wa-{NNN}-{word}-obslog-v{n}-{date}.md` | `wa-067-goodness-obslog-v3-20260426.md` |
| Session log | `wa-{NNN}-{word}-sessionb-sessionlog-v{n}-{date}.md` | `wa-062-fellowship-sessionb-sessionlog-v1-20260416.md` |

Type (a) supplementary patches for Stage 1 corrections (when needed under §3 Path 3 resolution) follow the readiness-instruction naming. They are not Session B Analysis Output deliverables.

---

*wa-sessionb-analysis-output-v1_8-20260430.md*
*Framework B — Soul Word Analysis Programme*
*Supersedes wa-sessionb-analysis-output-v1_7-20260430.md (Stage 2c rewritten as analytical synthesis pass)*
*Paired with wa-sessionb-analysis-readiness [current] (Stage 1)*
