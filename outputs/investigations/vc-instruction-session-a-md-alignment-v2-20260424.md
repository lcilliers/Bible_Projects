# VC Instruction Alignment with Session A `.md` Input — Analysis (v2)

**Date:** 2026-04-24 (revision v2)
**Supersedes:** `vc-instruction-session-a-md-alignment-v1-20260424.md` (preserved in `outputs/investigations/archive/`)
**Revision reason:** v1 surfaced three asks (a/b/c). Ask (a) landed in VC instruction v2_9 (commit `5d5ba4a`). This v2 extends Ask (b) with the re-evaluation and orphan-group discipline the researcher raised on 2026-04-24 after v1 was produced, and rewrites the Ask (b) processing-section recommendations to carry it. Ask (c) is unchanged from v1.
**Status of asks:**
- **(a)** DONE — v2_9 of the VC instruction carries the programme-prose read-at-startup rule.
- **(b)** PENDING — 8 original conflict points + 6 re-evaluation / orphan-group additions. Lands as v3_0 of the VC instruction.
- **(c)** PENDING — rework of `prog_instr_verse_context` (212-word v1 → ~420-word v2, drafted in this analysis). Lands as a PROSE supersede.

---

## 1. Method (unchanged from v1)

The VC instruction is the authoritative specification of what the AI must do. The content of the Session A `.md` is derived from it by asking: **what does the AI do**, and **what does the instruction say the AI does NOT do**. The analysis sections below answer those questions, identify conflicts with the `.md`-primary input model, and propose the concrete edits that bring the instruction and the script into alignment.

---

## 2. Ask (a) — VC instruction must read Phase A programme-prose at start-up

**Status: DONE in v2_9 (2026-04-24).**

VC instruction §6.1 Startup was rewritten to require two mandatory reads before the classifier opens any input:

1. Load `prog_instr_session_a` from the latest programme-prose extract; state aloud *"Session A content boundary understood: Session A carries STEP-sourced data only; no downstream-stage content is read from it or written into it."*
2. Load `prog_instr_verse_context` from the same extract; state aloud *"Verse Context's role understood — classify verses by term-level inner-being engagement; produce anchors; defer all interpretation to Session B."*

The §6.1 opener also acknowledges two valid input forms (Session A `.md` per-registry; legacy batch JSON for split-registry). The deeper input-form restructuring is Ask (b).

v2_8 is archived to `data/imports/WA/Workflow/Framework_B/archive/`. See commit `5d5ba4a`.

---

## 3. Ask (b) — conflicts with the `.md`-primary input model

**Eight original conflict points (from v1) retained, then six new items (B.9–B.14) added for re-evaluation discipline and orphan-group handling.**

### Original conflict points (unchanged from v1; summarised)

| # | Location | Problem | Resolution |
|---|---|---|---|
| B.1 | Header Inputs row | Names batch JSON as classifier input | Update to name Session A `.md` as primary; batch JSON as fallback |
| B.2 | §0.1 Pipeline Entry Point | Paragraph assumes batch JSON is input | Rewrite to lead with `.md`; retain batch JSON for split-registry |
| B.3 | §5 (entire section) | "Batch JSON Construction" with full schema | Rename to "Input Preparation"; retain schema as Annexure C |
| B.4 | §6.1 step 2 | "Load and parse the batch JSON" | Replace with input-form-aware wording (done in v2_9 already) |
| B.5 | §6.4 Session discipline | References batch JSON | Straight replace "batch JSON" → "Session A `.md`" where it is the classifier's input |
| B.6 | File naming | `wa-vcb-{batch_id}-...` assumes batch | Accept both schemes; `wa-{NNN}-{word}-vc-...` for per-registry |
| B.7 | §7.2 `_patch_meta.batch_id` | Required field | Make optional; `registry` field added for per-registry |
| B.8 | §5.2 "never split a term" | Phrased around batches | Rephrase: "Never split a term across input documents" |

Full wording for each is in v1 (archived copy).

---

### NEW: Re-evaluation discipline and orphan-group handling

This extends Ask (b) with the class of issues raised on 2026-04-24 about how prior verse_context content enters the VC session and how the classifier must handle it. The gap: the current instruction (and the batch JSON that preceded the `.md`) surface prior content but do not mandate explicit disposition. A classifier reading a term with prior records can drift between "review and confirm", "revise one or two", and "silently pass through" with no numerical check. Pre-existing groups whose verses all get reassigned in a re-evaluation become orphans with no disposition.

The additions below close the gap. They apply to **both** input forms (`.md` and batch JSON) — they are about classifier discipline, not about the input medium.

#### B.9 — Existing verse_context groups in the Session A `.md` (confirmation)

**Current state of the `.md`:** `scripts/build_session_a_prose.py` already renders prior VC content for every OWNER term. Specifically, in the Verses section per term:

- **Existing verse_context groups for this term** — a table of every `verse_context_group` row for the term's `mti_term_id`, including `delete_flagged = 1` dissolved rows, with columns `group_code`, `description`, `state` (active / dissolved). This ensures the AI sees dissolved groups and does not unknowingly recreate their meaning as a new group.
- **Prior classification** — per verse, below the verse text: `is_relevant` / `is_anchor` / `is_related` / `group_code` / `set_aside_reason` / notes / deleted-row marker. A verse with no prior `verse_context` row has no "Prior classification" line — its absence tells the AI this verse is unclassified.

**Verdict:** data is present. No change to the script is needed on this front.

**Confirmed in the Session A `.md` header, proposed addition (B.14 below):** a posture line stating fresh-start vs re-evaluation based on the count of active prior groups across all OWNER terms.

#### B.10 — Prior-state posture declaration at start-up (new §6.1 step)

**Problem:** today the instruction does not ask the AI to declare whether it is doing a fresh classification or a re-evaluation. The distinction matters: re-evaluation carries obligations (review every prior record, account for every pre-existing group) that fresh classification does not.

**Proposed: new mandatory step after existing §6.1 steps, before processing:**

> After loading the input, and before processing the first term, state the **prior-state posture** for this session based on the existing verse_context content surfaced in the input. Use one of the two templates below; state verbatim so the posture is visible in the session transcript.
>
> **FRESH posture** (no prior records across any OWNER term in the input):
>
> > *"Prior-state posture: FRESH. No verse_context records exist for any term in this input. All classifications are first-time. No orphan-group disposition required at term close."*
>
> **RE-EVALUATION posture** (any prior records exist for any OWNER term):
>
> > *"Prior-state posture: RE-EVALUATION. Verse_context records exist for {n} of {total} OWNER terms; {m} active verse_context_group rows and {d} dissolved rows are present. Every prior classification will be reviewed against the current filter and grouping model. Every pre-existing active group will be accounted for at term close — either retained with verses, dissolved, or carried without verses with a documented reason. No silent pass-through."*
>
> The counts `n / total / m / d` are derived from the input and must match the numbers visible in the input document. If they do not match, stop and flag — the input may be mis-rendered.

The researcher's `prog_instr_verse_context` programme-prose read (done at step 2 under the new §6.1 from v2_9) anchors the role-of-VC framing. This new posture step anchors the relationship to prior work.

#### B.11 — Per-term re-evaluation self-check (new §6.2 Step 6 subsection)

**Problem:** §6.2 Step 6 currently requires a per-term classification summary (Annexure B). It does not require an arithmetic self-check when prior records exist.

**Proposed: extend §6.2 Step 6 — "Per-term classification summary and observations file write":**

> **Re-evaluation self-check — mandatory for every term that had prior verse_context records.**
>
> Before writing the Classification block to the observations file, state the self-check:
>
> > *"Re-evaluation self-check for {strongs} ({transliteration}) mti_id={n}:*
> > *- Active verses: N*
> > *- Prior classifications reviewed: N (every active verse — mandatory)*
> > *- Confirmed unchanged (is_relevant + group + is_anchor all unchanged): X*
> > *- Revised is_relevant: Y*
> > *- Revised group assignment: Z*
> > *- Promoted to anchor: P*
> > *- Demoted from anchor: D*
> > *- Check: X + Y + Z = N? {yes/no}"*
>
> If the arithmetic does not balance, every active verse was not accounted for. Stop and correct before proceeding. The balance-check is the numerical proof that "review every prior record" was performed.
>
> **For terms with no prior records:** this self-check is not required. The standard per-term summary (Annexure B) is sufficient.

This makes the re-evaluation obligation explicit and numerically verifiable.

#### B.12 — Orphan-group check at term close (new §6.2 Step 6 subsection)

**Problem:** when a re-evaluation moves all verses out of a pre-existing active group, the group becomes an orphan. There is no current rule requiring explicit disposition. The patch would then carry a group with no active verses, and the applicator would not detect it.

**Proposed: extend §6.2 Step 6 — "Orphan-group check":**

> **Orphan-group check — mandatory for every term that had prior verse_context_group records.**
>
> For every pre-existing active `verse_context_group` for this term (from the Existing verse_context groups table in the input), after re-classification:
>
> 1. Count the active verses (`is_relevant = 1`, `delete_flagged = 0`) now assigned to the group.
> 2. If the count is zero, the group is an orphan.
> 3. Dispose of each orphan explicitly in the patch:
>    - **Dissolve** — include an `update` operation on the group setting `delete_flagged = 1` and `notes = "dissolved — all verses reassigned in re-evaluation"` (or a more specific reason). This is the default action.
>    - **Retain** — only where the group is structurally meaningful and expected to carry verses from future work. Include a note in the observations file explaining retention. Patch emits no operation for the group; the group remains `delete_flagged = 0` with zero active verses.
>
> State the check in the observations file immediately after the re-evaluation self-check:
>
> > *"Orphan-group check for {strongs} mti_id={n}:*
> > *- Pre-existing active groups: G*
> > *- Active verse counts per group after re-classification: {group_code: count, ...}*
> > *- Orphan groups (0 active verses): [list of group_codes] or NONE*
> > *- Disposition per orphan: {group_code}: dissolved | retained ({reason})"*
>
> No orphan may be left undisposed. Silent orphans are a validation failure.

#### B.13 — Patch pre-submission validation: orphan-group check (new §7.7 bullet)

**Problem:** §7.7 Pre-submission validation enforces coverage per verse but does not check orphan groups.

**Proposed: add to §7.7:**

> **Orphan-group validation.** For every pre-existing active `verse_context_group` for every term in the input:
>
> - Count the distinct `verse_context` operations in this patch that reference the group and leave it with at least one active verse (operations where `is_relevant = 1`, `delete_flagged = 0`). If the count is ≥ 1, the group is validated.
> - If the count is 0, the patch must include an `update` operation on `verse_context_group` setting `delete_flagged = 1` for this group. Absence of such an operation is a validation failure.
>
> This is programmatically verifiable: compute, for each pre-existing active group, the net active-verse count after patch application; flag any group reaching zero with no dissolve operation.

Extend the programmatic pre-submission validation for large batches (Section 6.4, deferred-patch path) to include this check as well.

#### B.14 — Session A `.md` header posture line (script update)

**Problem:** today the `.md` surfaces prior content inside each term's Verses section, but the "About this document" header does not state the overall posture. A classifier opening the `.md` has to scan to determine "is this a fresh run or a re-evaluation?". The posture should be in the header.

**Proposed: edit `scripts/build_session_a_prose.py` to compute and render a one-line posture statement in the About section:**

> *This registry has {n_active_groups} active prior verse_context groups across its OWNER terms ({n_dissolved} dissolved). {If n_active_groups == 0:} **Approach this as a FRESH classification.** {If n_active_groups > 0:} **Approach this as a RE-EVALUATION** — every prior active group must be retained (with verses), dissolved, or documented-retained at term close. No silent pass-through.*

Script change: one function that computes `n_active_groups` and `n_dissolved` across all OWNER terms of the registry, and one line inserted into `render_header()`. Approximately 10 lines of Python.

---

### Consolidated B.1–B.14 → v3_0 of the VC instruction

| # | Section touched | Change type |
|---|---|---|
| B.1 | Header Inputs row | Reword |
| B.2 | §0.1 Pipeline Entry Point | Rewrite paragraph |
| B.3 | §5 (rename + §5.1–5.4 reword) | Structural + content |
| B.4 | §6.1 step 2 | Reword (already partly done in v2_9) |
| B.5 | §6.4 | Find/replace batch-JSON → Session A `.md` where classifier input |
| B.6 | File naming (various) | Add per-registry scheme alongside VCB |
| B.7 | §7.2 `_patch_meta` | Make `batch_id` optional; add `registry` |
| B.8 | §5.2 | Rephrase "never split a term" |
| B.9 | *(Session A `.md` already renders prior VC)* | No instruction change; existing §5.3 mapping confirms |
| **B.10** | **§6.1 (new step)** | **New: prior-state posture declaration** |
| **B.11** | **§6.2 Step 6 (new subsection)** | **New: per-term re-evaluation self-check** |
| **B.12** | **§6.2 Step 6 (new subsection)** | **New: orphan-group check at term close** |
| **B.13** | **§7.7 (new bullet)** | **New: orphan-group validation** |
| **B.14** | *(Session A script, not instruction)* | **Script edit: posture line in `.md` header** |

v3_0 is a substantive revision — probably 60–80 touched lines in the 1708-line document, plus four new subsections. Still an edit-in-place job, not a full rewrite. Existing structure carries; the logic is additive except where B.3 renames §5.

---

## 4. Ask (c) — rework `prog_instr_verse_context` (unchanged from v1)

Current `prog_instr_verse_context` (id=46, v1, 212 words, draft, Chapter 6 — Instruction corpus) mixes governance with operational mechanics. The drafted ~420-word v2 body (narrative, governance-scoped) is unchanged from v1 of this analysis and is reproduced in Appendix A below for reference.

### Relationship to Ask (b) B.10–B.13

The re-evaluation and orphan-group additions are **instruction content** (they belong in the VC instruction v3_0), not programme-prose content. Programme prose says what VC IS and why; it does not specify self-check templates or arithmetic checks. So Ask (c)'s rework does not need to absorb B.10–B.13 — those are purely instruction-level.

One line of programme prose does benefit from a small amendment: the v2 body's paragraph about completion should gesture at re-evaluation as a normal, expected operation (the programme re-runs VC on reset registries). Proposed one-sentence addition to the v2 body:

> (appended to the completion paragraph) *Because a registry may be reset (for example, when a downstream change obsoletes prior classifications or when the filter and grouping model have evolved), Verse Context runs are re-runnable: the stage's record is the current classification, and every prior classification is subject to review when the work is re-opened.*

This keeps Ask (c) governance-level but acknowledges what the v3_0 instruction will operationalise.

---

## 5. Decisions to confirm before execution

1. **Accept the B.9–B.14 additions to Ask (b)?** They extend the scope of v3_0 but fit thematically. Approving as a bundle means v3_0 is the single VC instruction version that addresses both input-form restructuring AND re-evaluation discipline.
2. **Script update for B.14 (posture line in `.md` header) — land with v3_0 or sooner?** My recommendation: sooner. It's a small isolated change (~10 lines); doing it now means the 5 BANKED `.md`s can be regenerated with the posture line before any VC session is attempted on them.
3. **The one-sentence amendment to the Ask (c) v2 body (completion paragraph, re-runnability)** — keep or drop?
4. **Ask (c) overall — voice and scope of the ~420-word draft** (unchanged from v1) — does it land right for programme prose?
5. **File-naming (B.6)** — accept both `wa-vcb-{batch_id}-...` and `wa-{NNN}-{word}-vc-...` in parallel, or pick one?

---

## 6. Execution plan (on approval)

1. **B.14 now** — update `scripts/build_session_a_prose.py` with the posture-line logic. Regenerate the 5 BANKED `.md`s. Commit. (Low-risk; isolated.)
2. **Ask (c) supersede** — PROSE patch on `prog_instr_verse_context` (v1 → v2) using the existing draft (optionally with the completion-paragraph amendment). Apply, regen extract, commit. (Low-risk; supersede-only, v1 retained.)
3. **VC instruction v3_0** — produce `wa-versecontext-instruction-v3_0-{YYYYMMDD}.md` incorporating B.1–B.13. Archive v2_9. Commit. (Higher-touch; ~60–80 lines changed, four new subsections added. Single-file edit; structure unchanged.)

Each step is a separate commit so each is reviewable independently.

---

## Appendix A — Ask (c) proposed v2 body (unchanged from v1)

*(Included verbatim so this v2 analysis is self-contained; the v1 archived copy carries the same text.)*

**Heading: Programme — Verse Context**

> Verse Context is the stage at which the programme turns the verse corpus into classified evidence. For every active Hebrew or Greek term the programme investigates — every OWNER term in the registry — a reader passes through all of the verses in which that term occurs in the ESV and asks a single question about each verse: does this verse, through the use of this term, say something about the inner being? The verses that answer yes are grouped by the inner-being characteristic they engage; one or two verses in each group are designated as anchors — verses that make the group's meaning evident without requiring surrounding context. The verses that answer no are set aside with a controlled reason (purely physical, purely spatial, purely narrative, or wrong-face — the verse carries inner-being content but through a different term). Classification is uniform across the programme; every OWNER term is treated identically regardless of its registry.
>
> Verse Context is explicitly not the interpretive stage. It does not analyse the term in depth, does not draw conclusions about the word being studied, does not assign evidential weight, and does not place terms on dimensions or into cross-registry syntheses. All of that is downstream work, and downstream work reads from the classifications Verse Context produces — the groups, the group descriptions, the anchors, the set-asides. What Verse Context produces is the evidential substrate on which Session B, Session C, and Session D all rest.
>
> Two disciplines make Verse Context trustworthy as evidence. The first is that the filter operates at term level, not at verse level: a verse about covenant renewal may use a given term in a purely legal sense with no inner-being engagement through that specific term — the verse's overall theme does not admit the term to the registry if the term itself does not carry inner-being content there. The second is that groups are formed from the perspective of the inner-being characteristic the verse cluster is primarily about, not from what the term does — so a property term that serves different characteristics across its corpus is grouped by the characteristic it serves in each cluster, not by the term's grammatical or syntactic behaviour. Both disciplines trace directly to the evidence-first principle: the programme's findings are the programme's findings only if the verses, read at term level, under characteristic-perspective grouping, support them.
>
> A registry's Verse Context work is complete when every one of its OWNER terms has been classified and every one of its XREF terms has an OWNER whose classification is complete. At that point the registry's evidential substrate is intact and the programme moves the word into Dimension Review and then into the interpretive stages. Without Verse Context complete, no interpretive claim about a word can be grounded; that is the reason Verse Context precedes everything downstream.

### Optional one-sentence amendment (new in v2)

Appended to the last paragraph:

> *Because a registry may be reset (for example, when a downstream change obsoletes prior classifications or when the filter and grouping model have evolved), Verse Context runs are re-runnable: the stage's record is the current classification, and every prior classification is subject to review when the work is re-opened.*

---

*Analysis v2 produced 2026-04-24 after the researcher's 2026-04-24 question on how existing verse_context content is surfaced to the classifier and what self-check mechanisms ensure re-evaluation integrity. Supersedes v1 (preserved in archive) — v1 captured Asks (a)/(b)/(c); v2 marks (a) complete and extends (b) with six new items (B.9–B.14) on re-evaluation discipline and orphan-group handling.*
