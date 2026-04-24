# Obslog — VC_Review

**File:** wa-global-vc_review-obslog-v1_0-20260424.md
**Opened:** 2026-04-24
**Session topic:** Re-evaluation of Verse Context instruction — hypothesis that VC should run from term perspective, not registry perspective
**Governance:** Global rules v2.11 (per extract wa-global-rules-extract-20260421.json, 36 rules)
**Session reference:** VC_Review
**Prior output reference:** wa-versecontext-instruction-v2_9-20260424.md (instruction under review)

---

## Entry 001 — 2026-04-24 — Session opening, GR-TEMPO-001 failure corrected

**Researcher message (verbatim):**
> this session is about thinking and re-evaluating an instruction.  Verse Context is currently being approached from a registry entry perspective.  It takes the owner terms of a word, read all the associated verses, interpret the verses and consolidate the context of the verses into verse groups.  The main aim of verse context is the consolidate verses that all say the same thing into one group, and to designate a anchor verse that represents the verse group best.  My hypothesis is that there is no reason to run this from a registry perspective.  We simply need to run it from a term perspective. Verse context is not registry related.   This session is governed by the global rules.  Pay special attention to the descipline of the obslog.  Compliance is not an option.  The obslog reference is VC_Review

**Compliance failure — recorded:**
On session opening, Claude AI produced a chat response acknowledging the global rules were uploaded but did not read them before responding. Researcher challenged: "did you actually read to global rules?" This is a direct GR-TEMPO-001 failure — recognition-plus-continued-conversation replaced recognition-plus-action. Specifically: GR-LOAD-001 step (1) requires the rules to be read in full before any substantive work; Claude AI proceeded to clarifying questions without the read.

**Correction actions taken:**
1. Read wa-global-rules-extract-20260421.json in full (36 rules across 13 categories).
2. Opened this obslog as GR-LOAD-001 step (2).
3. Will state GR-CAD-001 activation as step (3) in chat.

**Files read this session so far:**
- wa-global-rules-extract-20260421.json (in full)

**Files NOT yet read but present:**
- wa-versecontext-instruction-v2_9-20260424.md (the instruction under review — primary subject)
- wa-programme-prose-extract-20260424.json (programme context)

---

## Entry 002 — 2026-04-24 — Next actions queued

Before engaging with the researcher's hypothesis, the following must happen:
1. Read wa-versecontext-instruction-v2_9-20260424.md in full (no skim, no sampling — per GR-LOAD-001 familiarisation semantics).
2. Read wa-programme-prose-extract-20260424.json in full for programme context.
3. Then engage with the hypothesis step by step.

This is the correct sequence; the earlier clarifying-question-first approach was wrong because it produced chat output before the source materials were read.

Note on the earlier clarifying questions: they remain open but secondary. They will be resolved as part of reading the instruction (the version question) and by noting that the obslog is newly opened in this session (the obslog-existence question).

---

## Entry 003 — 2026-04-24 — Readings completed

Files read in full:
- wa-global-rules-extract-20260421.json (all 36 rules, 13 categories)
- wa-versecontext-instruction-v2_9-20260424.md (the instruction under review, 1710 lines)
- wa-programme-prose-extract-20260424.json — targeted reads of:
  - `prog_instr_session_a` (section 52)
  - `prog_instr_verse_context` (section 46)
  - `prog_instr_dimension_review` (section 47)
  - `prog_data_terms` (section 24)
  - `prog_xref_architecture` (section 25)
  - `prog_data_verses` (section 26)
  - `prog_anchor_verse` (section 27)

## Entry 004 — 2026-04-24 — Observations relevant to the hypothesis (pre-response)

**The hypothesis (verbatim from researcher):**
> My hypothesis is that there is no reason to run this from a registry perspective. We simply need to run it from a term perspective. Verse context is not registry related.

**Observations from the data and documents read (pure observation, not interpretation):**

OBS-1 — Database architecture is already term-keyed, not registry-keyed
- `verse_context.mti_term_id` is FK to `mti_terms.id` (v2.9 §2.2)
- `verse_context_group.mti_term_id` is FK to `mti_terms.id` (v2.9 §2.1)
- Neither classification table has a `registry_id` or `registry_fk` field
- v2.9 §2.2 explicit: *"Programme-wide key: mti_term_id is the same integer regardless of which registry views the term. OWNER and XREF registries query the same verse_context records via this key."*
- prog_data_verses §26 explicit: *"The classification is attached to the term, not to the registry-view of the term."*

OBS-2 — The OWNER/XREF architecture already makes classification term-centric at the data level
- prog_xref_architecture §25: *"one term, one owning registry — and a companion mechanism that records the term's relevance to other registries without duplicating its classification"*
- *"A finding raised in the OWNER registry's Session B is the finding for that term across the programme; registries that reference the term as XREF inherit the finding through the shared mti_term_id path rather than producing a separate one."*
- v2.9 §0.2: XREF terms are NOT separately classified. Their verse_context is the OWNER term's verse_context, inherited via mti_term_id.

OBS-3 — Where "registry" currently appears in the VC instruction
Registry concerns in v2.9 currently drive:
(a) Batch construction ordering (§5.2): *"ordered by mti_terms.owning_registry_fk ascending (keeps terms from the same registry together where possible)"* — a soft preference, not a requirement
(b) Registry split across batches (§5.2): expected behaviour, not a constraint
(c) XREF coverage check (§0.2, §13.2): determines whether a *registry* can advance to Complete — but the check itself is a term-coverage check wearing a registry hat
(d) Registry completion check (§13.1): "are all this registry's OWNER terms classified?"
(e) Registry status advancement (§13.3): `verse_context_status` on `word_registry` — this is the gate for DataPrep
(f) Re-export per registry (§13.3): produces fresh full-word JSON
(g) Processing order (§6.1 step 7): *"Terms are processed in registry sequence, ascending by registry number"*
(h) Classification input framing (§6.1 step 1, v2.9 change): per-registry Session A .md is now the "primary" input, batch JSON is "legacy"

OBS-4 — The actual analytical unit in §6.2 is already the term
- §6.2 Step 1: "Read all verses" — for the term
- §6.2 Step 2: "Apply the relevance filter" — for each verse of the term
- §6.2 Step 3: "Group relevant verses" — for the term
- §6.2 Step 4: "Designate anchors" — per group, per term
- §6.2 Step 5: "Identify dual-context verses" — per term
- §6.2 Step 6: "Per-term classification summary" — per term
- Every step is scoped to a single term. Registry is not present in the analytical loop itself.

OBS-5 — What genuinely binds VC to registry (if anything)
From the readings, the remaining registry-coupled points are:
(i) `verse_context_status` is a field on `word_registry`, not on `mti_terms`. Therefore the "completion" signal is by registry.
(ii) DataPrep gate (v2.9 §13.3): *"This re-export is what opens the DataPrep gate"* — DataPrep is triggered per registry.
(iii) Re-export produces per-registry JSON.
(iv) Session B DataPrep reads the registry-level file.
(v) Session A's per-word (i.e. per-registry) .md is now named as primary classification input in v2.9 §6.1 step 3.

These are all downstream/upstream interface points, not core VC classification logic. They are the ways the registry envelope is observed at the boundary of VC, not within it.

**Preliminary interpretation (to be tested with researcher):**

The hypothesis appears consistent with the data architecture. The classification itself is already term-centric in the database and in §6.2's workflow. What the instruction labels as "registry perspective" looks like it is actually:
- Batch organisation convenience (soft — terms from one registry tend to cluster together, but this is batch assembly not classification)
- Registry-boundary reporting (the completion check, status advancement, re-export)
- Input document framing (the per-registry Session A .md is currently presented as primary input)

Whether removing the registry frame from VC would simplify the instruction, or whether the registry envelope serves a function that is not obvious from the text, is a question for the researcher.

**Questions that arise before I can reflect further:**

Q1 — When you say "run it from a term perspective," do you mean:
(a) The input document model changes — terms are processed as a programme-wide queue, grouped into batches by some term-level criterion (e.g. verse count, language, cluster), without per-registry Session A .md as the primary input?
(b) The workflow itself changes — §6.2's six steps are the same, but the batch and reporting envelopes are term-keyed instead of registry-keyed?
(c) Both?

Q2 — What happens to the completion signal that triggers DataPrep?
If VC stops tracking registries, something else has to advance `word_registry.verse_context_status` to Complete (or replace that mechanism) so DataPrep knows when to start. Is the proposal to:
(a) Keep the registry-level completion check but move it out of VC (so CC runs it as a derivative check from term-level classifications)?
(b) Replace the registry gate with a term-level gate (and DataPrep also becomes term-driven)?
(c) Something else?

Q3 — What about the re-export?
Currently VC produces a re-export of the full-word (per-registry) JSON as a trigger artifact. If VC is term-scoped, the re-export could be per-term or per-batch or removed entirely. Which reflects the intent?

These three questions are interpretive choices that affect the shape of any revised instruction. Per the session rules, I will pause here rather than speculate.

---

## Entry 005 — 2026-04-24 — Researcher's answers to Q1–Q3 (verbatim)

**Researcher message (verbatim):**
> Q1 - it is about both.  adding the registry into the process add noise, not value.
> q2 - it should exist on both. CC will update the registry when all the terms (owner and XREf) has gone through VC.
> q3 - there are approx 3000 owner terms.  Each terms will have its own input .md  depending on volume handling.  I can introduce multiple terms in a single sessions.  Each term is completed in its own right.

**Parsing the answers:**

A1 — Both input model AND workflow change. Registry frame is removed from both. Rationale: "adding the registry into the process add noise, not value."

A2 — Dual completion tracking. Term-level completion is primary; CC derives registry-level completion (verse_context_status = Complete) as a consequence of all terms (OWNER and XREF) in that registry having been classified.
- This preserves the DataPrep gate without putting registry into VC's core workflow.
- Registry becomes a CC-side aggregation, not a VC-side concern.

A3 — Scale and input unit:
- ~3000 OWNER terms in scope programme-wide (confirms the analytical unit count — this is the real workload of VC).
- Each term has its own input .md (per-term Session A .md, not per-registry).
- Multiple terms may be introduced in one session — session-level batching is at researcher's discretion, not driven by registry or batch id.
- Each term is completed in its own right — term is the atomic unit of completion, not registry and not batch.

---

## Entry 006 — 2026-04-24 — Consequences for the instruction (observation, pre-reflection)

The researcher's answers move the instruction's shape in a specific direction. Recording the observable consequences before reflecting.

C-1 — Input model
- Per-term Session A .md becomes the primary (and probably sole) classification input.
- The per-registry Session A .md model newly introduced in v2.9 §6.1 step 3 is displaced.
- The legacy batch JSON (VCB-{nnn}-extract-{date}.json) is also displaced — or, at least, no longer the organising unit.

C-2 — Workflow (§6.2)
- §6.2's six steps remain substantively unchanged (they were already term-scoped).
- What changes: the "processing order" in §6.1 step 7 ("Terms are processed in registry sequence, ascending by registry number") is removed or rewritten — terms are processed in whatever order the researcher introduces them into a session.
- Registry sequence is no longer a discipline of VC.

C-3 — Completion model
- The atomic completion unit is the term, not the batch and not the registry.
- Each term is completed when its verse_context and verse_context_group records are in place and R1–R4 hold for that term.
- Registry-level completion (word_registry.verse_context_status = Complete) is derived by CC once all OWNER and XREF terms for that registry have term-level completion.
- DataPrep gate is unchanged in mechanism (it still reads word_registry.verse_context_status) — but the signal is produced as a downstream consequence, not by VC itself.

C-4 — Re-export
- Per-registry re-export still happens (DataPrep reads the per-registry full-word JSON). But it is triggered by CC's derived registry-completion event, not by VC's own completion cycle.
- VC does not own the re-export step; it owns only the term-level classification.

C-5 — Batch concept
- The "batch" (VCB-{nnn}) as the organising unit is gone. Term is the unit.
- Sessions may carry one term or many — at researcher discretion.
- File-naming conventions (§6.4) built around {batch_id} need to be rebuilt around {term identifier}.
- Artefacts (observations file, session log, flags register, patch, Session B flags) either move to per-term scoping, or to per-session scoping with term identifiers inside.

C-6 — Flags register and Session B flags
- Currently end-of-batch artefacts. Need to be rethought. Options visible from the instruction's current shape:
  (a) Per-term — a small flags file per term when flags arise.
  (b) Per-session — one flags file per researcher session, covering whatever terms were processed.
  (c) Rolling programme-wide — one continuously-updated register.
- This is an interpretive choice for the researcher.

C-7 — Patch scope
- Currently one VERSECONTEXT patch per batch.
- Options: per-term, per-session, or batched-to-a-cadence.
- Per-term would produce many small patches; per-session would let several terms be written together. This is a workflow efficiency choice, not a correctness choice.

C-8 — XREF handling (§0.2)
- Largely unchanged in substance — XREF terms are still not separately classified; they still inherit via mti_term_id.
- But the registry-level XREF coverage check (§0.2, §13.2) becomes CC's responsibility as part of the derived registry-completion step, not VC's.

C-9 — Documents downstream of VC
- Dimension Review instruction — operates at cluster (registry-grouping) level. Its trigger is per-registry verse_context_status = Complete. Unaffected in mechanism, because the registry signal is preserved (just produced downstream of VC, not by VC).
- Session B Analysis Readiness — reads per-registry exports. Unaffected.
- Session B Analysis Output — reads per-registry exports. Unaffected.
- The registry envelope survives where it is needed (downstream stages); it is only removed from VC's own process.

C-10 — Programme prose
- prog_instr_verse_context (programme prose section 46) currently describes VC as operating "in batches — typically tens of registries at a time". This prose text will need revision to reflect the per-term model. This is a downstream programme-prose update, not a blocker.

---

## Entry 007 — 2026-04-24 — Open interpretive choices for the researcher

Before any drafting, three interpretive choices remain:

IC-1 — Scope of flags artefacts (per C-6 above): per-term, per-session, or programme-rolling?
IC-2 — Scope of patch artefacts (per C-7 above): per-term, per-session, or researcher-paced?
IC-3 — Observations log scope: currently per-batch (wa-vcb-{batch_id}-term-observations-...). With batch gone, does the obslog become per-session (dated), per-term, or programme-rolling?

These are authorship-adjacent choices that affect the shape of the revised instruction but not its analytical substance. Per GR-HF-001, they are candidates for specialist authorship within researcher direction — except that the researcher is the one with the visibility on what works best across multiple sessions. I will surface them and ask.

---

