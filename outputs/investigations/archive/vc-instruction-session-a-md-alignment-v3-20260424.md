# VC Instruction Alignment with Session A `.md` Input — Analysis (v3)

**Date:** 2026-04-24 (revision v3)
**Supersedes:** `vc-instruction-session-a-md-alignment-v2-20260424.md` (preserved in `outputs/investigations/archive/`)
**Revision reason:** v2 surfaced and landed the per-registry `.md` input model. v3 adds a **workflow re-assessment** (new Section 7) raised by the researcher on 2026-04-24 after Asks (a)/(b)/(c) had landed: *would the VC entry point work better per-OWNER-term rather than per-registry?* This section thinks through the implications, argues the answer, and proposes a sequencing if the shift is adopted. It is an assessment, not a change — no new code or instruction edits until the researcher directs.
**Status of original asks (a/b/c):**

- **(a)** DONE — VC instruction v2_9 carries the programme-prose read-at-startup rule (commit `5d5ba4a`).
- **(b)** DONE — VC instruction v3_0 carries the `.md`-primary input model, re-evaluation discipline, and orphan-group handling (commit `ae079da`). Session A script carries the posture line (B.14, commit `9ad5060`).
- **(c)** DONE — `prog_instr_verse_context` v1 → v2 governance-narrative supersede (commit `1bbdd19`).
**New: Section 7 — per-OWNER-term input re-assessment. PENDING researcher decision.**

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

**v3 status update (2026-04-24 post-commit):** all three steps landed. B.14 in commit `9ad5060`, v3_0 of the instruction in `ae079da`, Ask (c) PROSE supersede in `1bbdd19`. The original asks are closed. The v3 re-assessment (Section 7 below) is a separate question raised after all the above landed.

---

## 7. Workflow re-assessment — per-OWNER-term input rather than per-registry

**Researcher question (2026-04-24, after Asks a/b/c landed):** if VC work is intrinsically term-level — the filter is applied term-by-term, grouping is term-level, anchors are term-level, XREF inheritance is term-level — would it work better to switch the Session A `.md` from **per-registry** (one `.md` covering all OWNER terms of a word) to **per-OWNER-term** (one `.md` per term, containing just that term's verses and prior state)?

This section thinks the question through to inform the decision. It argues the answer, surfaces concrete implications, and proposes sequencing if the shift is adopted. It proposes no new code or instruction edits until the researcher directs.

### 7.1 The atomic unit of VC is the term, not the registry

The entire VC mechanism keys on `mti_term_id`, not on registry:

- `verse_context_group.mti_term_id` — every group belongs to exactly one term.
- `verse_context.mti_term_id` — every classification is per-term.
- The filter (§3) is applied to *"the term's specific use in this verse, not … the verse's general theme"* (§3.2 ⚠ note).
- Grouping (§6.2 Step 3) is *"characteristic-perspective"* per term — "a property term that serves different characteristics across its corpus" is grouped per cluster within that one term.
- Anchor designation (§4) is per term — "every term must have at least one active anchor" (R4).
- XREF inheritance (§0.2) is per `mti_term_id` — an OWNER's classification is visible to any registry that borrows the term via that same key.
- The re-evaluation self-check and orphan-group check added in v3_0 (§6.2 Step 6) are both per-term calculations.

**The registry is a container of terms; the term is the unit of classification.** The per-registry `.md` bundles a container's worth of atomic units into one document for processing convenience. Bundling is not a methodological requirement; it is a transport choice.

### 7.2 Current per-registry `.md` — friction points

The per-registry `.md` pilot revealed (and this section adds) friction points that all trace to the same root — unit mismatch:

- **Heterogeneous sizes.** The 5 BANKED registries were intentionally chosen small (25–128 active verses each, 7–17 OWNER terms). At the programme scale that is atypical: 174 non-excluded registries average **21.3 OWNER terms** and some carry well over 100. Strength (187) has 186 OWNER terms and 3,540 active verses; desire (43) has 151 terms and 1,409 verses. A per-registry `.md` for those is impractical as a single classification input — it forces the split-registry fallback path every time.
- **Coarse re-run granularity.** Revise one term and the entire registry's `.md` must be re-rendered and re-classified. A term's re-run should affect that term only, not the 30+ terms beside it.
- **Posture is heterogeneous within a registry.** A registry's `.md` currently states a single posture (FRESH or RE-EVALUATION) based on any prior records. In practice the distribution is often mixed: some terms have prior records, others don't. The classifier then has to re-derive per-term posture from the per-term Prior classification state anyway.
- **Orphan-group scope is per-term but the `.md` view is per-registry.** The B.12 orphan-group check operates on pre-existing groups for a specific term. Surfacing "all groups for all terms in this registry" in one document doesn't help the check — the classifier still has to read the per-term Existing groups table and compute per-term.
- **Parallelism is awkward.** Two classifiers cannot work on the same registry's `.md` without coordination. Per-term would let independent sessions run concurrently on different terms with no coordination cost.
- **Batching logic collapses onto grouping logic.** §5.2's "never split a term across input documents" is the programme's only structural rule on input packaging, and it exists because the term is the unit. A per-term `.md` makes the rule vacuous — a term cannot be split because each `.md` is one term.

### 7.3 Implications — positive

Adopting per-term `.md` as the primary input:

1. **Atomic unit match.** Input scope = classification scope = output scope (per-term operations in the patch). No translation between container and unit.
2. **Uniform document size.** A term's `.md` carries that term's verses only. Most terms have a handful of verses; the largest terms (e.g. strength's `H2388` or similar) have tens to low hundreds. No `.md` blows past a working context budget.
3. **Trivially simple posture logic.** Per-term: either the term has prior records (RE-EVALUATION) or it doesn't (FRESH). No aggregation across terms; no mixed-posture registries.
4. **Orphan-group check reads naturally.** The pre-existing active groups in the `.md` are *this term's* groups. Count after re-classification, dispose, done.
5. **Targeted re-runs.** A term-level filter refinement, a term-level audit_word re-run, or a term-level researcher revision all re-render and re-classify exactly that term.
6. **Natural parallelism.** Multiple classifiers can work different terms concurrently. No coordination required (the terms share no state).
7. **Consistent treatment.** Every term gets the same document structure regardless of registry size. A term in strength looks identical in input shape to a term in renewal.
8. **Clean session sizing.** A session can hold one term (for large terms) or a group of small terms. Session scope becomes a deliberate assembly decision, not a constraint imposed by the registry's size.
9. **Re-evaluation alignment.** The v3_0 re-evaluation discipline is per-term. A per-term input aligns the document with the discipline it must support.

### 7.4 Implications — things to handle

1. **File count.** 174 non-excluded registries × ~21 OWNER terms = **~3,712 `.md` files** if rendered programme-wide. Manageable — well-structured filenames and a `data/exports/session_a/terms/` subfolder keep the active set browsable. Compare: `data/exports/STEP Extracts/` already holds ~186 active files with orderly naming.
2. **Registry-wide visibility.** A classifier working term-by-term doesn't see the other terms in the same registry. Argument against: losing registry context. Counter-argument: classification is explicitly term-level (see §7.1); registry context is not classifier input. Where registry-wide context matters (Dimension Review, Session B), those stages render their own registry-scoped extracts (the existing `build_complete_extract.py` etc.). VC does not need it.
3. **Cross-term wrong-face notes.** §3.6 wrong-face set-aside allows the notes field to point at the other term carrying the inner-being content ("wrong_face: inner-being content carried by lev (H3820A, Reg 183)"). The classifier needs to know terms exist; it does not need them in the current `.md`. Either: (a) the per-term `.md` lists the registry's other terms in a short "Other terms in this registry" section for reference; or (b) the classifier references a registry-scoped summary sidecar when wrong-face arises. Option (a) is simpler — keep a small pointer table.
4. **Registry completion check.** Currently checked per-registry (OWNER complete + XREF inheritance). With per-term sessions, the check is still registry-scoped — Claude Code aggregates term states after each patch and advances `verse_context_status` to Complete when all the registry's OWNER terms have active `verse_context` records. No semantic change; just timing (fires after each term patch rather than after a batch-wide patch).
5. **Session batching remains meaningful at the output layer.** A session can still produce one patch covering 1–N terms. The `wa-vcb-{batch_id}-...` file naming survives unchanged: `batch_id` identifies a session's output scope, which may be one term, several terms, or many terms. The `.md` input is per-term; the patch output can aggregate term-level operations. This keeps the existing patch-application and observations-file conventions intact.
6. **Processing order.** The v3_0 §6.1 step 8 rule ("terms processed in registry sequence ascending") presumed a multi-term input. With per-term input, order is session-assembly order — typically registry-ascending when Claude Code picks a batch of terms, but no longer enforced by the input document's structure.
7. **Registry-wide posture reporting.** Currently the `.md` header states posture for the whole registry. Per-term `.md`s state term-level posture. A registry-wide status report (e.g. "registry X has 7 FRESH terms, 5 RE-EVALUATION terms") becomes a separate reporting concern — a CLI flag on `build_session_a_prose.py` that summarises a registry's per-term posture is a small addition.
8. **Prose-store mapping.** The six seeded `sa_s1_d*` handles (Word Summary, Meaning, Verses, Terms, Pointers, Questions) are currently registry-scoped. If they were ever to be populated as `prose_section` rows, the registry-scoped framing would still make sense — the prose store is for registry-level governance, not per-term mechanical exports. A per-term `.md` can still be composed from the same underlying queries; the prose store's handles don't need to change.

### 7.5 Proposed per-term file organisation and naming

Suggested:

```text
data/exports/session_a/
├── wa-{NNN}-{word}-session_a-{YYYYMMDD}.md         # registry-scoped view (retained, optional)
└── terms/
    └── wa-{NNN}-{word}-{strongs}-session_a-{YYYYMMDD}.md
```

Per-term filename example: `wa-134-renewal-H2487-session_a-20260424.md`. The `NNN`-word prefix keeps a registry's terms sorted together in the directory; the Strong's keeps them unique; sort-order remains friendly.

Inside a per-term `.md`, the six seeded section structures carry over almost unchanged, but scoped to the one term:

- **Word Summary** — registry identity (so the classifier knows which word's term this is); OWNER/XREF term counts for the registry (so wrong-face pointers land in context); **this term's prior-state posture** (FRESH / RE-EVALUATION with this term's counts only).
- **Meaning** — this term's lexical layer only. One term, not a list.
- **Verses** — this term's verses only.
- **Terms** — a short "Other terms in this registry" table (pointer only — Strong's + gloss + OWNER/XREF marker). Lets the classifier reference wrong-face candidates without loading their data.
- **Pointers** — this term's cross-registry links (if any).
- **Questions** — catalogue questions linked to this term's flags.

The six handles in the prose store remain registry-scoped (as seeded); per-term `.md` uses the same conceptual section divisions but with term scope. No `prose_section_type` change required unless we later want to persist per-term Session A content in the DB (which we probably don't — the `.md` is enough as input; the DB already carries the underlying data).

### 7.6 Script changes (if adopted)

Modest. `scripts/build_session_a_prose.py` gains:

- `--term=<mti_term_id>` — render one per-term `.md`.
- `--registry=N --per-term` — render all per-term `.md`s for a registry.
- `--all-per-term` — programme-wide per-term render.
- Default behaviour (no flags) could remain per-registry for backwards compatibility, or flip to per-term as primary; researcher decides.
- Output naming convention per §7.5.

Re-use the existing per-term query helpers (the script already has `get_verses`, `get_meaning`, `get_lsj`, `get_prior_vc` etc. per-term — they're the atoms already). The registry-scoped header is rewritten for term scope; the rest of the rendering logic is already per-term.

### 7.7 Instruction changes (VC v3_1 post-adoption)

VC instruction v3_0 is designed around the `.md`-primary model without stipulating registry vs term scope. A small v3_1 would:

- **§0.1** — state that the default input is the **per-term Session A `.md`**; the per-registry view is retained for researcher review and Dimension Review hand-off.
- **§5.1 / §5.2** — input selection operates per-term; Claude Code composes a session from one or more per-term `.md`s.
- **§6.1** — posture declaration is per-term (simpler — one of two templates; no aggregation over terms).
- **§6.2 Step 6** — per-term self-check and orphan-group check unchanged; they already operate per-term.
- **§7.2 / §7.4** — patch scope unchanged (1–N terms per patch); processing order becomes session-assembly order.
- **File naming** — `wa-vcb-{batch_id}-...` unchanged for session outputs.

Not a structural rewrite. The v3_0 framework already treats the term as the atomic unit; v3_1 just names the term as the default scope of the input document.

### 7.8 Programme-prose implications

**`prog_instr_session_a` (Chapter 6, v2 just landed):** already describes Session A as "renders the per-word data into a self-contained form that the rest of the pipeline reads". The "per-word" phrase assumes the registry as the rendering unit. If we adopt per-term, this section's third paragraph needs a light touch to say the renderer can produce per-registry or per-term views from the same underlying data — both are faithful representations; the primary VC input is per-term. Supersede to v3; not a rewrite.

**`prog_instr_verse_context` (v2 just landed):** the governance narrative ("For every active Hebrew or Greek term the programme investigates — every OWNER term in the registry — a reader passes through all of the verses…") is already term-centric. No change needed; the narrative holds whether the input is delivered per-registry or per-term.

**`prog_data_terms` / `prog_data_verses` (Chapter 4):** already say the term is the unit. No change needed.

Overall programme-prose impact is one supersede of `prog_instr_session_a` (a short clarifying paragraph); nothing else. This is another sign that the per-term framing is already implicit in the programme's working model — only the *rendering unit of the input document* is shifting, not the underlying concepts.

### 7.9 Hybrid option — both views, composed from the same blocks

Rather than choosing one, the renderer can produce both:

- **Per-term `.md`** — the VC classifier's primary input. One term, its verses, its prior state.
- **Per-registry `.md`** — a human / Dimension Review / researcher-browse view. All the per-term `.md`s for a registry, concatenated with a registry-level header and the Terms/Pointers/Questions sections at the top.

Under this model the per-term `.md`s are the canonical output; the per-registry `.md` is generated by concatenation with a short registry-scope wrapper. No duplicate rendering logic; no lost functionality.

**My read: the hybrid is the right answer.** The per-term `.md` is the input; the per-registry view is a convenience for humans and downstream stages. Either can be produced from the same database queries with a modest renderer refactor.

### 7.10 Recommendation

**Adopt per-term `.md` as the primary VC input.** The evidence is strong:

- The method is term-level; the input should match the method.
- The re-evaluation and orphan-group disciplines introduced in v3_0 operate per-term; per-term input makes them trivial rather than contrived.
- The ~3,700-file count is unproblematic at the scale the programme operates.
- Large registries (16 with 51–100 terms, 4 with 100+) become tractable in a way they are not in the per-registry model.
- The v3_0 instruction framework accommodates the shift with minimal edits (v3_1 would be a light polish, not a rewrite).
- The programme prose `prog_instr_verse_context` is already term-centric in its narrative; nothing there needs to change.
- Retain the per-registry view as a secondary render (hybrid §7.9) for human and downstream use.

**Sequencing if adopted:**

1. **Add per-term render to `build_session_a_prose.py`.** Modify the script to produce per-term `.md`s (and retain per-registry as a secondary / convenience output). ~1 day of work. Commit; regenerate the 5 BANKED's per-term `.md`s as pilot; regenerate the per-registry view from the per-term blocks.
2. **Pilot one VC run on per-term `.md`.** Pick the smallest single term on renewal (registry 134, an OWNER term with ≤5 verses) and run a Claude AI VC session against that one `.md` alone. Compare output to the per-registry-input baseline.
3. **VC instruction v3_1.** Light supersede of v3_0 noting per-term as default; §6.1 posture logic simplified.
4. **`prog_instr_session_a` v3 supersede.** One-paragraph clarification on renderer scope.
5. **Programme-wide render.** Once pilot confirms, render all ~3,700 per-term `.md`s; re-run VC across the 180 registries at `Verse Context Reset` under the new input model.

### 7.11 Decision gate

Three questions for the researcher:

1. **Adopt per-term as primary VC input?** (my recommendation: yes, with the hybrid per-registry secondary render retained)
2. **Where should per-term `.md`s live?** `data/exports/session_a/terms/` is my suggestion — keeps them grouped but separates them from the per-registry secondary view.
3. **Pilot scope before full adoption?** My recommendation: one small term first, then one full small registry in per-term mode (renewal is the cleanest BANKED target; 14 OWNER terms; 44 active verses; already piloted under the per-registry model so baseline is known).

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

*Analysis v3 produced 2026-04-24 after the researcher's question on whether VC should take the OWNER term, rather than the registry, as its atomic input unit. Supersedes v2 (preserved in archive). v2 marked Asks (a)/(b)/(c) complete (commits `5d5ba4a`, `9ad5060`, `ae079da`, `1bbdd19`). v3 adds Section 7 — the per-term re-assessment — as a new pending decision. v2's Sections 1–6 and Appendix A are retained verbatim.*
