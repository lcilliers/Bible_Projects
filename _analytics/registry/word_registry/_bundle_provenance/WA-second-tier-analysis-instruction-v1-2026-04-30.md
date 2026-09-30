# WA Second-Tier Question Catalogue Analysis — Instruction

**File:** WA-second-tier-analysis-instruction-v1-2026-04-30.md
**Version:** v1.0
**Date:** 2026-04-30
**Status:** Active
**Prepared from:** WA-R064-second-tier-analysis-v1-2026-04-30.md (forgiveness, first application)
**Applies to:** All subsequent second-tier catalogue applications across the programme

---

## 1. Purpose

This instruction governs the application of the WA Second-Tier Observation Question Catalogue (`WA-obs-question-catalogue-v2`) to individual word registries. It captures the process, output structure, and progressive writing method used in the first application (R064 — forgiveness) so that subsequent analyses are consistent, complete, and reusable.

The document is written for CA (Claude AI) operating in analytical role. It is not a database instruction. CC (Claude Code) has no role in this task.

---

## 2. Inputs Required Before Starting

Before beginning any second-tier analysis, the following must be present in the session:

| Input | Description | Format |
|---|---|---|
| Registry data package | The complete data file for the word being analysed | `R[nnn]-[word]-data.md` |
| Question catalogue | `WA-obs-question-catalogue-v2-[date].json` | JSON |
| This instruction | The present document | MD |

**Pre-session checks:**
1. Read the registry data package in full before beginning. Do not proceed from partial reading.
2. Read the question catalogue in full. Note the tier structure (T0–T7) and all component codes.
3. Confirm the output file prefix with the researcher before producing any output. The current programme prefix is **WA**.

---

## 3. What the Task Is

The task is to apply each prompt in the second-tier catalogue to the registry data and produce a substantive answer for every prompt — including where the answer is silence or non-applicability. Silence and absence are complete and informative answers.

**This is not a summary of prior analysis.** Each prompt receives a fresh answer grounded in the registry data, even where the answer reproduces prior findings exactly.

**The prior Q&A answers in the registry data file are source material**, not the output. The second-tier catalogue prompts organise and interrogate that source material from a new structural angle.

---

## 4. Answer Status Codes

Every prompt receives exactly one status code:

| Code | Meaning |
|---|---|
| **A** | **Answered** — the data provides a direct and substantive response |
| **P** | **Partial** — the data addresses this prompt but incompletely; the response states what is evidenced and names what is missing |
| **S** | **Silent** — the data does not address this prompt; silence is stated explicitly |
| **N** | **Not applicable** — the prompt's closing condition applies (e.g., "if no X, note this explicitly" where X is present) |

The status code appears immediately after the prompt heading, before the answer text:

```
**Status: A** | *Consistent with prior analysis*
```

---

## 5. Notation Conventions

Every prompt response carries one notation tag alongside the status code:

| Tag | Meaning |
|---|---|
| *Consistent with prior analysis* | The prompt produces the same finding as existing programme work |
| *Adds structure* | The prompt organises or sharpens existing findings without changing substance |
| *New finding* | The prompt surfaces something not previously named or assembled in the data |
| *Gap identified* | The prompt reveals an area the existing analysis has not addressed |

A single response may carry more than one tag if warranted. State this plainly: `*New finding* / *Gap identified*`.

---

## 6. Output File Structure

### 6.1 File naming

Follow the programme naming convention:

```
WA-R[nnn]-second-tier-analysis-v1-[yyyy-mm-dd].md
```

Where `[nnn]` is the zero-padded registry number and `[word]` is not included in the filename (the registry number is sufficient). Version begins at v1. If the analysis is resumed across sessions, increment to v2 only if substantive content changes; use the same version within a single unbroken analysis session.

### 6.2 File header

Every output file opens with the following header block:

```markdown
# WA — R[nnn] [Word] — Second-Tier Question Catalogue Analysis

**File:** WA-R[nnn]-second-tier-analysis-v1-[date].md
**Date:** [date]
**Catalogue applied:** WA-obs-question-catalogue-v2-[date].json
**Data source:** R[nnn]-[word]-data.md
**Previous outputs:** [brief one-line reference to prior files in this registry's history]
**Status:** In progress — [tier last completed]
```

### 6.3 Tier sections

Each tier is a top-level section (`##`). Each component within a tier is a subsection (`###`). Each prompt within a component is its own sub-subsection identified by its prompt number (Prompt 1, Prompt 2, etc.).

Structure within each prompt response:

```markdown
**Prompt [N]:** [Exact prompt text from catalogue]

**Status: [Code]** | *[Notation tag]*

[Answer text — as long as required to be substantive. Minimum: one paragraph. No upper limit.]
```

### 6.4 Closing summary

After all tiers are complete, append a closing summary section:

```markdown
## Programme Summary — All Tiers

### Status Code Totals Across T0–T7
[Table: Tier | Total Prompts | A | P | S | N]

**Answered rate (A):** [n/total = %]
**Partial rate (P):** [n/total = %]
**Silent rate (S):** [n/total = %]
**Not applicable rate (N):** [n/total = %]
**Coverage (A+P of applicable prompts):** [n/applicable = %]

### Key Gaps Consolidated
[Bulleted list of all S-status prompts by location]

### New Findings Consolidated
[Numbered list of all *New finding* items across all tiers]
```

---

## 7. Progressive Writing Method

### 7.1 Work tier by tier

Complete one full tier before moving to the next. Do not write partial tiers.

The tier sequence is fixed: T0 → T1 → T2 → T3 → T4 → T5 → T6 → T7.

### 7.2 Write continuously to file

Use the bash tool to append each completed tier to the working file using a heredoc block. Do not hold content in context and write it all at once at the end — context loss will occur in long sessions.

The append command pattern:

```bash
cat >> /home/claude/[filename].md << 'TIER_LABEL'
[tier content]
TIER_LABEL
echo "Tier complete. Total lines: $(wc -l < /home/claude/[filename])"
```

### 7.3 Copy and present at each tier break

After each tier is appended to the working file:

1. Copy to the outputs directory:
```bash
cp /home/claude/[filename].md /mnt/user-data/outputs/[filename].md
```

2. Use `present_files` to make the file available to the researcher.

3. Report a brief tier summary to the researcher: prompt counts, status code distribution, key observations, new findings, and gaps identified.

4. Wait for researcher instruction before proceeding to the next tier.

### 7.4 Do not attempt all tiers in one memory session

The full catalogue contains 185+ prompts across 8 tiers. Attempting all tiers in one continuous write risks context loss and inconsistency. The tier-by-tier rhythm with file writes at each break is the structural protection against this.

---

## 8. Answer Quality Standards

### 8.1 Every prompt receives a substantive answer

Do not answer with "see above" or "as noted." Each prompt stands alone. If an answer reproduces an earlier finding, reproduce it in full rather than cross-referencing.

### 8.2 Ground every answer in the data

Every answer must be grounded in the registry data: specific verse references, observation IDs (OBS-064-xxx), finding IDs (DIM-064-xxx), SD pointer IDs, group IDs, term Strong's numbers, or Q&A responses. Do not introduce interpretations not supported by the data.

### 8.3 Name what is missing

When an answer is **P** (partial) or **S** (silent), name what is missing precisely:
- Which specific question is unanswered
- Whether further verse investigation would likely address it
- Whether it is a Session D question (already captured in an SD pointer) or a new gap

### 8.4 Distinguish observation, interpretation, and reflection

- **Observation:** What the data states directly
- **Interpretation:** What the data implies or suggests, stated as inference
- **New finding:** A synthesis or assembly not previously made in the data, clearly flagged

Do not present interpretation as observation, or new findings as established data.

### 8.5 Apply the closing condition correctly

Several prompts end with "If [X is absent/present], note this explicitly." These prompts become **N** (not applicable) when the condition named is met. Read the closing condition carefully before assigning N — do not assign N simply because the previous prompt was fully answered.

### 8.6 The T5.7 dependency

T5.7 (Deposit Consequence) depends on T2.8 (Body — Deposit). If T2.8 finds no constitutional body deposit, T5.7 closes formally and all three prompts receive **N**. State this explicitly at T5.7 and note any adjacent generational questions separately.

---

## 9. Tier-Specific Notes

### T0 — Divine Image and Created Design
- This tier is theologically oriented but analytically grounded. Do not speculate about divine nature beyond what the verse evidence names.
- The prompt "Where Scripture is silent about God's possession of this characteristic, note this explicitly" (T0.1 Prompt 3) will be **N** for most characteristics — forgiveness, grace, mercy, and similar are explicitly attributed to God. Apply the closing condition correctly.
- T0.2 Prompt 2 (original created design vs. response to fallen condition) will frequently be **S** — the data rarely addresses this distinction directly. Name the gap clearly.

### T1 — Definition
- T1.1 (Name and Naming) is usually fully answered from the registry description and term inventory.
- T1.3 (Boundary) frequently produces partial answers — the distinction from nearest adjacent characteristics is often deferred to Session D. Note all SD pointers that address boundary questions.
- T1.5 (Immediate Response) and T1.6 (Sustained Effect) are distinct: one names the first inner-being movement at encounter; the other names the constitutional state established over time. Keep them separate.

### T2 — Constitutional Location and Boundaries
- T2.1–T2.3 (Spirit, Soul, Heart) are usually well-evidenced for active registries. T2.4 (Mind) and T2.5 (Other Soul Subsets) are frequently partial.
- T2.6–T2.7 (Body) require careful reading of the verse evidence for somatic language. The four body-functions identified for forgiveness (mediating, expressive, indicative, functional) are a useful typology for other registries.
- T2.8 (Body — Deposit) is consistently the most speculative prompt. Only affirm a deposit where the verse evidence explicitly or strongly implies it. Flag the T5.7 dependency clearly at T2.8.
- T2.10 (Constitutional Movement) is often the most structurally significant output of T2 — assemble the full movement sequence if the data supports it.

### T3 — Inner Faculties
- Work through all 11 faculty components. T3.5 (Creativity) is frequently silent — name the silence explicitly.
- T3.3 (Memory) and T3.9 (Conscience) were the richest new-finding sources for forgiveness — pay close attention to these for other registries.
- T3.6 (Volition) and T3.7 (Motivation) are almost always engaged for active registries — the question is the direction and degree of engagement, not whether it is present.
- T3.11 (Relational Capacity) should distinguish between characteristics that build/sustain relational connection and those that restore/repair it. This is a productive analytical distinction.

### T4 — Relational Interfaces
- T4.1 (God to Human) is almost always the best-evidenced direction. T4.2 (Human to God) is usually well-evidenced for characteristics involving prayer, seeking, or worship.
- T4.3 (Giving) and T4.4 (Receiving) should be kept distinct — the conditions and inner-being states differ. T4.4 Prompt 3 (person who encounters but does not receive) is frequently silent and worth flagging.
- T4.6 (Spiritual Beings) is frequently silent — name the silence and note whether any SD pointers touch adversarial dimensions.

### T5 — Formative and Developmental
- T5.1 (Transformation): distinguish condition change from orientation change.
- T5.1 Prompt 2 (reversibility): attend carefully to whether the data distinguishes formal receipt from genuine receipt. The Mat 18:35 evidence is the primary reversibility data point.
- T5.3 (Mechanism): the four-mechanism typology (declarative encounter, cosmic atonement, cultic ritual, gradual formation) is a reusable analytical structure.
- T5.6 (Eschatological Trajectory): most registries will have partial evidence here — look for present-experience language that has a future-orientation quality (hope, waiting, anticipation).
- T5.7: handle the T2.8 dependency as noted above.

### T6 — Structural Relationships
- T6.1 (Co-occurrence): always use the quantitative data from the registry's co-occurrence table. Name the unexpected high signals separately from the expected ones.
- T6.2 (Sequential): distinguish causal, enabling, access-instrumental, and constitutive relationships precisely. These are different structural claims.
- T6.4 (Vocabulary and Root Sharing): check the `shared_term_count` and `term_sharing_ratio` fields. Zero XREF count does not mean no root-level connection — check the vocabulary for shared roots across registries.
- T6.5 (Distinctions): this is frequently the weakest component — boundaries between adjacent characteristics are commonly deferred to Session D. Name all relevant SD pointers.
- T6.6 (Shared Anchors): the shared anchor table in the registry data is definitive. Use it directly.

### T7 — Evidential and Methodological Foundation
- T7.1 (Lexical): work through all 10 prompts. The LXX prompt (Prompt 8) and NT coinage prompt (Prompt 9) are frequently silent — the NO_WORD_ANALYSIS flag is the indicator.
- T7.2 (Verse and Literary): usually fully answerable from the anchor verse analysis and group descriptions. The logical structure prompt (Prompt 3) is particularly productive — map the argument structure explicitly.
- T7.3 (Human Science): this is frequently undeveloped in the registry data. Identify the most relevant framework(s) from the characteristic's nature and name the gap explicitly. Do not introduce framework content not grounded in the data.

---

## 10. Gap and New Finding Protocol

### Gaps

A gap is identified when:
- The prompt addresses a dimension of the characteristic the data has not examined
- The verse evidence that would answer the prompt exists but has not been analysed
- A structural question is implied by the data but no SD pointer captures it

When a gap is identified:
1. State it explicitly in the prompt response
2. Note whether it is covered by an existing SD pointer (Session D target) or is genuinely new
3. Assess whether further verse investigation in the current programme phase would address it, or whether it properly belongs to Session D synthesis

### New findings

A new finding is identified when:
- The prompt produces an answer that assembles existing observations in a way not previously done
- The prompt reveals a structural relationship, sequence, or pattern implicit in the data but not named
- The prompt synthesises across multiple observations into a single analytical statement

When a new finding is identified:
1. Flag it clearly in the prompt response with *New finding*
2. State what the finding adds that was not previously assembled
3. Note whether it has implications for Session D synthesis or other registries

---

## 11. Session Log

A session log must be produced at natural breakpoints and at session close. The session log captures:
- The word and registry analysed
- The tiers completed in the session
- The key findings and gaps identified
- Any RESEARCHER_DECISION items raised
- Next steps

Session log naming:
```
WA-session-log-[description]-v1-[date].md
```

---

## 12. Worked Example — Prompt Format

The following illustrates the correct format for a prompt response drawn from the forgiveness analysis:

---

**Prompt 1:** What is this characteristic called in the programme — and what does the name itself signal about its essential nature?

**Status: A** | *Consistent with prior analysis*

The characteristic is named **forgiveness** in the programme (Registry 64, word field: "forgiveness"). The name signals three things about its essential nature immediately:

1. **Relational structure:** Forgiveness implies a prior injury and a relational claim. The name presupposes a two-party structure — an offender and an offended — and names the act or disposition of the offended party toward the claim. The name cannot be understood in isolation from the relationship it inhabits.

2. **Direction of movement:** Forgiveness is directional — it moves *from* the one holding a claim *toward* the one against whom the claim is held. The name encodes a one-way release: the forgiver initiates; the recipient receives. This distinguishes it from reconciliation (which is bilateral) or confession (which moves in the opposite direction).

3. **The cancelled debt:** The English word "forgiveness" carries the sense of releasing a liability. This aligns with the Hebrew and Greek vocabulary (sending away, releasing, covering over — as named in the registry description).

The registry description confirms: "Forgiveness is the release of a legitimate claim against someone who has wronged you — the decision not to hold the debt against them, to cancel the account of injury."

---

## 13. Checklist Before Starting Each Registry

- [ ] Registry data package read in full
- [ ] Question catalogue structure confirmed (T0–T7, all component codes)
- [ ] Output file created with correct header
- [ ] File written to `/home/claude/` working directory
- [ ] Outputs directory copy confirmed at: `/mnt/user-data/outputs/`
- [ ] Researcher has confirmed file prefix (WA)
- [ ] No content held back for end-of-session write — all tiers written progressively

---

## 14. Change Control

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-04-30 | Initial version — derived from R064 forgiveness first application |

*End of instruction document.*
