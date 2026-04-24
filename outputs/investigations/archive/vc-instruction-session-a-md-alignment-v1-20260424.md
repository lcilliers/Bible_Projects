# VC Instruction Alignment with Session A `.md` Input — Analysis

**Date:** 2026-04-24
**Purpose:** address three researcher requests after the Session A `.md` pilot landed —
(a) update VC instruction to always read the programme-prose Session A section at start-up;
(b) find conflicts in the VC instruction that still assume the old batch JSON is the only input;
(c) review and rework `prog_instr_verse_context` in programme prose to fit programme-prose purpose (governance, not instructional mechanics).
**Status:** AWAITING APPROVAL. On approval I'll produce: a v2_9 supersede of the VC instruction, a PROSE supersede of `prog_instr_verse_context`, and (if needed) a small addition to the VC startup rules.

---

## Ask (a) — VC instruction must read the Phase A programme-prose section at start-up

### Current state

VC Instruction §6.1 Startup lists six start-up steps. It references "this instruction document" and the batch JSON. It does not reference programme prose.

### What the user asked for

Every VC classification session should load the Phase A programme-prose section before doing any work. The Phase A section is `prog_instr_session_a` (programme prose Chapter 6, just superseded to v2 in commit `fb69391`). That section now carries the content boundary (Session A is STEP-sourced only, no analytical leakage) and the three-artefact provenance (legacy JSONs → engine exports → `.md` renderer). That content belongs in the VC classifier's working context — it tells the classifier what the input it's receiving is and isn't.

### Proposed change to §6.1 Startup

Rewrite step 1 to explicitly require loading the programme-prose Phase A section:

> **Revised step 1:** Read this instruction document in full (or confirm it is already loaded for this session). Read the programme-prose section `prog_instr_session_a` from the most recent `data/exports/reference/wa-programme-prose-extract-{YYYYMMDD}.md` (or equivalent). State: "Session A content boundary understood: Session A carries STEP-sourced data only; no downstream-stage content is to be read from or written into it."

Add a new step before step 6 (processing order):

> **Read `prog_instr_verse_context`** from the same programme-prose extract. Confirm: "Verse Context's role understood — classify verses by term-level inner-being engagement; produce anchors; defer all interpretation to Session B."

Both changes are small additions; they anchor the classifier's mental model in the programme-prose narrative before it opens any input.

---

## Ask (b) — conflicts that require the old batch JSON to work

The VC instruction v2.8 was written entirely around the batch JSON model. Several sections assume the batch JSON is the input. They do not work unchanged if the Session A `.md` is the input. The list below identifies the conflict points and proposes how to resolve each.

### B.1 Header block — Inputs row (top of document)

**Current:**
> Inputs | Full word JSON exports — wa-{nnn}-{word}-extract-{date}.json (for batch construction) │ Verse Context batch JSON — wa-vcb-{batch_id}-extract-{date}.json (for Claude AI classification)

**Problem:** The AI now classifies from the Session A `.md`, not the batch JSON. The batch JSON remains useful for Claude Code internal operations (batching large registries), but it is no longer the classifier input.

**Proposed:**
> Inputs | Session A `.md` — wa-{nnn}-{word}-session_a-{YYYYMMDD}.md (produced by `scripts/build_session_a_prose.py`, the classifier's primary input) │ Engine `--export-word` JSON — wa-{nnn}-{word}-extract-{date}.json in `data/exports/STEP Extracts/` (Claude Code internal use; source for Session A `.md` render) │ Legacy batch JSON — wa-vcb-{batch_id}-extract-{date}.json (retained for large-registry splitting; optional for the classifier)

### B.2 §0.1 Pipeline Entry Point

**Current:** states that Claude Code uses the full word exports as the source for batch construction, and the batch JSON is what Claude AI classifies from.

**Problem:** entire paragraph assumes batch JSON is the classifier input.

**Proposed rewrite:** open with the `.md` as primary input. Retain the full word export as the data Claude Code reads to produce both the `.md` and (where needed) the batch JSON. Retain the SQL description of what Claude Code reads — it is still the same tables.

Key edit:
> ~~The batch JSON Claude Code produces is a structured subset of this data — formatted for Claude AI consumption.~~
>
> → The Session A `.md` Claude Code renders is a self-contained document — composed under the six Session A prose handles — read by Claude AI as the sole input for classification. A parallel batch JSON may be produced for very large registries where classification is split across multiple sessions; in that case the `.md` is still the primary document and the batch JSON supplies the verse slice for the current session.

### B.3 §5 Claude Code — Batch JSON Construction

**Current:** §5.1, §5.2, §5.3, §5.4 describe the batch JSON pipeline (trigger, criteria, schema, output file).

**Problem:** This entire section assumes batch JSON is the classifier input. Its detailed schema (§5.3, ~70 lines of JSON) is largely redundant if the classifier works from the `.md`.

**Proposed:**

- **Rename §5** to "Claude Code — Input Preparation".
- **§5.1 Trigger** — unchanged in substance, but wording moves from "constructs a new batch" to "prepares the input documents for a new classification session" (either a per-registry `.md`, a split `.md` for large registries, or a legacy batch JSON where retained).
- **§5.2 Input selection criteria** — keep the OWNER / active / verses-exist / unclassified rules. Drop the 2,000–2,500 verse target as the primary governing metric; replace with per-registry scope as the default and "split only when a registry exceeds {threshold}" as the escalation rule.
- **§5.3 Input document structure** — replace the batch JSON schema block with a pointer to `docs/prose-store-architecture.md` §5.2 and `scripts/build_session_a_prose.py` for the `.md` structure. Retain the batch JSON schema as Annexure C ("legacy batch JSON — retained for large-registry split scenarios").
- **§5.4 Output file** — two names: `data/exports/session_a/wa-{NNN}-{word}-session_a-{YYYYMMDD}.md` (primary), `data/exports/verse_context/wa-vcb-{batch_id}-extract-{YYYYMMDD}.json` (legacy, large-registry only).

### B.4 §6.1 Startup — step 2

**Current:** "Load and parse the batch JSON".

**Problem:** direct conflict.

**Proposed:** "Load the Session A `.md` for the target registry (typically `data/exports/session_a/wa-{NNN}-{word}-session_a-{YYYYMMDD}.md`). For split-registry work, load the corresponding `.md` slice or legacy batch JSON as directed by Claude Code's session hand-off."

### B.5 §6.4 — Session discipline, file writing

**Current:** references "batch JSON" in several places (observations file naming, session log naming, discipline about instruction-document size with a big batch JSON loaded).

**Problem:** the `.md` replaces the batch JSON as the large input document. Token-budget concerns are similar but the file is different.

**Proposed:** straight replace — "batch JSON" → "Session A `.md`" where the text refers to the classifier's input. Leave the discipline rules (dual-write, progressive observations, version increments) unchanged.

### B.6 File naming — `wa-vcb-{batch_id}-...` pattern

**Current:** Claude AI's output files (observations, session logs, flags register, patch) all use `wa-vcb-{batch_id}-...`.

**Problem:** the `batch_id` concept assumes multi-registry batches. For per-registry classification, `{batch_id}` as "VCB-{nnn}" is less natural.

**Proposed:** keep `wa-vcb-{batch_id}-...` for backwards compatibility where Claude Code still issues batch IDs. For per-registry classification, accept an alternative scheme: `wa-{NNN}-{word}-vc-{scope}-v{n}-{YYYYMMDD}.{ext}` (e.g. `wa-134-renewal-vc-term-observations-v1-20260424.md`). Document both; neither is wrong.

### B.7 §7.2 VERSECONTEXT patch — `_patch_meta.batch_id`

**Current:** patch metadata includes `batch_id` as a required field.

**Problem:** per-registry sessions may not have a `batch_id` in the VCB sense.

**Proposed:** make `batch_id` optional in the patch schema. When present, it carries the batch identifier. When absent, `_patch_meta.registry` (new optional field) carries the registry number and word. Both are human-readable provenance; neither affects the applicator.

### B.8 §5.2 "Never split a term" rule

**Current:** "Never split a term — all verses for a term must appear in one batch".

**Problem:** for per-registry `.md`, this rule is satisfied automatically (all of a registry's OWNER terms and all their verses are in one document). Still applies for split-registry cases.

**Proposed:** retain the rule; rephrase to "Never split a term across input documents".

---

## Ask (c) — rework `prog_instr_verse_context` to fit programme-prose purpose

### Current state (212 words, draft, Chapter 6 Instruction corpus)

The existing body has three concerns mixed together:

1. **What VC is** — stage between Session A and DimReview, reads every verse for every OWNER term — *this is programme prose appropriate.*
2. **What it does vs does not do** — classifies and groups, doesn't interpret — *programme prose appropriate.*
3. **Mechanical details** — batch JSON, "tens of registries at a time", observations log / flags register / session log / patch file, re-export trigger — *these belong in the instruction document, not in programme prose.*

### Why this needs reworking

Per `docs/prose-store-architecture.md` and the working-memory methodology, programme prose is the **governance and orientation layer** — it tells a reader what a stage IS in the programme and why, in a way that survives the detail of whichever version of the instruction is current. The existing `prog_instr_verse_context` reads more like a mini-instruction than programme prose. It names specific artefacts ("batch JSON", "observations log"), specific cadence ("tens of registries at a time"), and specific operational mechanics (patch application, status advance, re-export trigger) — all of which change with each instruction version and will leave this prose stale.

Programme prose about VC should say things that stay true even as the instruction evolves: VC is the stage that grounds every later analytical claim in a specific verse; it classifies through the inner-being filter; it produces anchor verses as the evidential foundation for Session B and downstream work. The *specific how* — batch JSON vs `.md`, observations log naming, patch format — lives in the instruction.

### Proposed v2 body (~420 words)

Heading: **Programme — Verse Context**

```
Verse Context is the stage at which the programme turns the verse corpus
into classified evidence. For every active Hebrew or Greek term the programme
investigates — every OWNER term in the registry — a reader passes through
all of the verses in which that term occurs in the ESV and asks a single
question about each verse: does this verse, through the use of this term,
say something about the inner being? The verses that answer yes are
grouped by the inner-being characteristic they engage; one or two verses in
each group are designated as anchors — verses that make the group's meaning
evident without requiring surrounding context. The verses that answer no
are set aside with a controlled reason (purely physical, purely spatial,
purely narrative, or wrong-face — the verse carries inner-being content but
through a different term). Classification is uniform across the programme;
every OWNER term is treated identically regardless of its registry.

Verse Context is explicitly not the interpretive stage. It does not analyse
the term in depth, does not draw conclusions about the word being studied,
does not assign evidential weight, and does not place terms on dimensions
or into cross-registry syntheses. All of that is downstream work, and
downstream work reads from the classifications Verse Context produces —
the groups, the group descriptions, the anchors, the set-asides. What Verse
Context produces is the evidential substrate on which Session B, Session C,
and Session D all rest.

Two disciplines make Verse Context trustworthy as evidence. The first is
that the filter operates at term level, not at verse level: a verse about
covenant renewal may use a given term in a purely legal sense with no
inner-being engagement through that specific term — the verse's overall
theme does not admit the term to the registry if the term itself does not
carry inner-being content there. The second is that groups are formed from
the perspective of the inner-being characteristic the verse cluster is
primarily about, not from what the term does — so a property term that
serves different characteristics across its corpus is grouped by the
characteristic it serves in each cluster, not by the term's grammatical or
syntactic behaviour. Both disciplines trace directly to the evidence-first
principle: the programme's findings are the programme's findings only if
the verses, read at term level, under characteristic-perspective grouping,
support them.

A registry's Verse Context work is complete when every one of its OWNER
terms has been classified and every one of its XREF terms has an OWNER
whose classification is complete. At that point the registry's evidential
substrate is intact and the programme moves the word into Dimension
Review and then into the interpretive stages. Without Verse Context
complete, no interpretive claim about a word can be grounded; that is the
reason Verse Context precedes everything downstream.
```

### What this version keeps and what it drops

**Keeps:**
- What VC is (the stage that turns verses into classified evidence).
- The governing question and the set-aside categories (though in narrative form, not as bullet points).
- The two disciplines that make it trustworthy (term-level filter, characteristic-perspective grouping).
- The completion criterion (OWNER complete + XREF inheritance).
- The role downstream (feeds Session B/C/D).
- The evidence-first principle linkage.

**Drops (moved to the instruction, not lost):**
- Specific artefacts (batch JSON, observations log, flags register, session log, patch).
- Cadence ("tens of registries at a time").
- Mechanical handoff (patch application, status advance, re-export).
- Tool names.

The result reads as governance narrative, not a mini-instruction. It stays true across VC instruction version changes.

---

## Execution plan (on approval)

1. **Programme prose** — one PROSE patch, one `supersede` op on `prose_section` for `prog_instr_verse_context`, filename `wa-prose-programme-instr-verse-context-supersede-v2-20260424.json`. Apply, regen extract, commit.

2. **VC instruction** — produce `wa-versecontext-instruction-v2_9-20260424.md` incorporating items B.1–B.8 and the (a) startup changes. Not a patch — this is a file edit in `data/imports/WA/Workflow/Framework_B/Session_B/`. Follow the existing instruction-archive pattern: move v2_8 to `Framework_B/archive/`, commit v2_9 as the current. Change list is targeted — I estimate ~40 edits across the 1708-line document, all mechanical once the design is approved.

3. **Session A prose** — an optional, small companion addition: add a similar "read `prog_instr_session_a` at start-up" requirement to the Session A script's `.md` output header so a classifier who only has the `.md` is pointed at the right programme prose. The current `.md` header already gestures at this; I can tighten it.

4. **Commit strategy** — one commit for the programme-prose supersede, one commit for the VC instruction rewrite, one commit for any Session A script tweak. Keeps the change set reviewable.

---

## Three decisions to confirm

1. **Does the proposed v2 body of `prog_instr_verse_context` carry the right voice and scope for programme prose?** Any content to add, remove, or rephrase? I've aimed for narrative (not bulleted lists) and governance-level statements that stay true across instruction versions.

2. **B.6 file-naming decision** — accept both the existing `wa-vcb-{batch_id}-...` and a new per-registry `wa-{NNN}-{word}-vc-...` scheme (document both, neither wrong), or standardise on one? My recommendation: accept both for now; pick one when per-registry VC becomes the default after the pilot.

3. **VC instruction edit approach** — produce v2_9 that edits-in-place (change list B.1–B.8 + ask (a)), or produce a more ambitious v3 that substantially rewrites §5 and §6 around the `.md`-primary flow? My recommendation: v2_9 (edit-in-place) — the existing structure works; the problem is the input description. A full rewrite risks losing proven content.

---

*Analysis produced 2026-04-24 after Session A `.md` pilot (commit 8dc7f2f) to propose the VC instruction and programme prose updates that align the written instruction with the renderer that now exists.*
