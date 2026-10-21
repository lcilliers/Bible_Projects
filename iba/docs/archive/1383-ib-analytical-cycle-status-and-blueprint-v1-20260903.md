# The IB analytical cycle — status and blueprint (v1)

**Filename:** 1383-ib-analytical-cycle-status-and-blueprint-v1-20260903.md
**Escalation:** #1383 (carries this for now; genuinely exceeds that escalation's original Window-1
scope — flagged in the open items, not pre-decided whether it splits out).
**What this is:** a forward statement of the whole cycle as it now stands, blueprint-shaped —
every layer, every stage, what it is, what it takes in, what it produces, and where it currently
stands. **Not a history document** — this session's own historical grounding (the RESET record,
the synthesis-B spec, this conversation's own convergence-check) lives in the prior chat and the
documents it cites; pull those separately if the history itself is needed again. This document
states where things are now and where the cycle goes next.

---

## 0. The shape of the whole cycle, in one line

**Base substrate → Level 1 (lexical, one passage-block) → Level 2 (behaviour/movement, one
characteristic-candidate, two passes) → Publishing.** Four stages. The first two are the ones this
session did real work on; the third is newly specified here; the fourth is named but not designed —
flagged as such, not filled in with invented detail.

Matches, and refines, the standing three-stage frame already recorded in config
(`governance.programme_stages`: Base_data → Analysis → Publishing) — Level 1 and Level 2 together
*are* "Analysis," now split because this session's work showed they need genuinely different input
shapes and different rules, not because the three-stage frame was wrong.

---

## 1. Governing principles — apply at every stage below, stated once here, not repeated per-stage

1. **Grain discipline.** No stage answers a question that depends on evidence a lower stage hasn't
   yet produced. A stage that finds itself "making something up" to answer a question is evidence
   the question was asked at the wrong stage, not a licence to guess.
2. **Boundaries won't hold; meaning lives on the edges.** Any partition used to make a stage
   tractable (a passage block, a characteristic-candidate grouping) is a **workspace**, never an
   analytical claim. The true relationships get recorded as explicit, traceable signals/edges
   between items, not by getting the partition itself right.
3. **Observe, don't impose.** A category (faculty, characteristic, movement) is only real if it
   varies per instance of evidence. A property that's constant across every occurrence of a term
   describes the term, not what any given verse shows — and doesn't belong in a per-verse or
   per-instance record.
4. **Mechanical vs. judgement, split explicitly, at every stage.** Anything a deterministic rule or
   query can answer must be built as one, run automatically, on every item, no selection. Judgement
   time is reserved for what's genuinely interpretive, and it sits on top of the mechanical layer's
   complete output — never re-derives what the mechanical layer already settled.
5. **Traceability.** Every finding, at every stage, walks down to the verses/evidence that grounds
   it. No stage's output is trusted further than its citation path.
6. **Config-governed anchoring.** Process rules that matter live in `cfg_*`, checked mechanically
   where possible (`configmaint.validate`), not held only in memory, a doc, or good intentions.
   This is the direct, structural answer to "it started well, then drifted" — the anchor is the
   config and the mechanical check, not remembering to be careful.
7. **Completeness by structure.** A stage's output format should make incompleteness visible by
   construction (every input item gets a row/entry, `n/a` where nothing applies) — never rely on a
   pass "remembering" to cover everything.

---

## 2. Stage 0 — Base substrate

**What it is.** The raw material every later stage reads: `verse`, `span`, `strong`,
`strong_related`, and the mechanical T1–T3 baseline (`verse_lexical.role`/`morph_code`/
`resolved_sense`/`status`, written by `lexical.build`).

**Status: built, but not yet fully trusted.** Three concrete, live defects found this session, not
yet fixed:
- `classify_role` misclassifies `H0853` (the Hebrew direct-object marker) as `content`; 5+ live
  instances confirmed in this session's own sample alone (10,521+ project-wide, per #1383's design
  doc). Fix already designed (§4 of the design doc), not yet built.
- 824 verses (13,621 `verse_lexical` rows) point at soft-deleted `span` rows via a stale
  foreign key — escalation #1441, not yet resolved.
- `resolved_sense` is built to draw a narrowed sense from `strong_meaning_parsed`, falling back to
  the flat `stepGloss` only on a miss — every sampled code across this session's whole 19-verse
  validation run hit the fallback. Not yet investigated whether this is representative or a sample
  artefact.

**Before Stage 1's output is treated as reliable at scale, this stage's own defects need a real
disposition** — not blocking every Stage-1 test run (this session's own test runs proceeded despite
them, correctly recording each as a live finding rather than silently working around it), but a
real gap before a production build.

---

## 3. Stage 1 — Level 1 (lexical), one passage-block

**Analytic unit.** A single, self-determining, sequential passage block (≤20 verses — the hard
cap decided in #1379 v7). Boundaries are found as part of the read itself, not pre-planned across
the whole corpus. Genre/language/testament are determined as that read's own first move.

**Scope, held strictly.** A verse's own words, from its own span/morph/lexicon data. Never HIB.
Never reaches into another verse outside the current block. Anything it can't resolve from the
block's own data is recorded `unresolved`, explicitly, never guessed and never resolved by
reaching outside the block.

**Process — two layers, this session's own drift-mitigation correction, load-bearing going
forward:**
- **Layer 1 (mechanical, automatic, complete, zero selection)**: same-code/different-gloss check;
  Hebrew narrative-morph (wayyiqtol / `az`+imperfect) flag; negator-code lexicon; connective-type
  lexicon (causal/coordinating/purpose — small, evidence-built, growable, `UNCLASSIFIED` rather
  than guessed for an unlisted code); full `strong_related` pull for every content-role code, no
  selection. Proven live this session (the Gal 5:16–17 demo script) — not aspirational.
- **Layer 2 (judgement, per-code, sitting on Layer 1's complete output)**: idiom/combined-span
  sense; pronoun/entity resolution (same-block only); noun relational-vs-severity classification;
  related-word sorting (same-concept vs. coincidental); genre; the manual capture that Layer 1
  can't mechanize. Cannot silently skip a code — Layer 1 already enumerated every one.

**Explicitly excluded from Stage 1's structured output, by direct precedent, not invention:**
verse-level rhetorical/structural patterns (merism, chiasm, antithetic parallelism, paired image) —
`phenomenon.set/not-literary-pattern` already routes this exact class of finding to an "emergent
question" log for Window 2, never the structured register; Stage 1 should do the same, not invent
a `note_type` for it.

**Output (proposed, not yet built).** `verse_lexical` extended with `position`/`surface`/
`language`/`testament` (mechanical, Layer 1); `passage.genre` (manual, Layer 2); a new
`verse_lexical_note` table (judgement-bearing findings — idiom/pronoun/noun-class/chain/
connective/related-word/polarity/entity-link/data-quality/inert). **Not yet built as schema.**

**Structural gap named this session, not yet fixed**: nothing links a Window-2 `phenomenon`/
`operation` record back to the specific `verse_lexical`/`verse_lexical_note` row that warranted it
— both currently carry only free text. Recommended: an FK, matching the precedent
`operation_party.hib_id` already set (a real link alongside the free text, not replacing it).

**Status: design mature, build not started, not yet approved.**
- Checklist prototyped and test-driven on 5 passages / 19 verses, both languages, multiple genres —
  real findings, not a clean pass (a second confirmed Hebrew narrative-chain case; the chain test's
  blind spot at genre pivots; two genuine Greek idioms; a live data-integrity bug found and
  escalated (#1441); one honest self-correction where an original framing didn't hold up).
- Measured against the observation-question catalogue in full (181 active questions, none
  skipped) — the coverage-and-grain-discipline analysis lives in a companion document (§8 below
  names it), not repeated here.
- Escalation #1383 (this thread) carries the open build decisions: the FK link timing, the
  literary-pattern disposition, the `resolved_sense` question.

---

## 4. Stage 2 — Level 2 (behaviour / movement), one characteristic-candidate, two passes

**This is the newest, least-settled piece of the blueprint — stated as clearly as the current
thinking supports, not padded to look more finished than it is.**

**Analytic unit — deliberately NOT the same as Stage 1's.** Stage 1 takes a sequential passage
block as input. Stage 2 takes an **assembled set of "like lexicals"** — every verse whose Stage-1
data relates to one characteristic-candidate — gathered across the whole corpus, not book-sequential.
This is the direct, confirmed answer to the "how did the old book-work and cluster-work each fail"
question from earlier this session: book-sequential work is right for generating the lexical
(Stage 1) and wrong for HIB work; characteristic-assembled work was closer to right for the
higher-order questions but failed at its own base because it tried to do lexical derivation and HIB
derivation in the same undifferentiated pass. **Stage 2 keeps the characteristic-assembled input
(gets the coherence gain) but does not let that collapse the sequencing discipline** — see Pass
2a/2b below.

**How the input gets assembled — the segmentation answer, adapted from the existing (stale, but
structurally sound) synthesis-B design, not invented fresh:**
- A characteristic-candidate's verse set is gathered using the **existing term→cluster linkage**
  (`mti_terms.cluster_code` or its current live equivalent) purely as a **candidate-gathering**
  step — cheap, mechanical, already built. **This partition carries no analytical weight of its
  own** — it is a starting neighbourhood for attention, exactly as the old synthesis-B spec's §2a
  already established for the old cluster mechanism ("a cluster is an operational partition, not an
  ontological claim... it gathers verses, it does not claim anything about them").
- **Membership stays provisional.** A verse's presence in a characteristic-candidate's assembled
  set is one fact about it; its own Stage-1/Stage-2 evidence can confirm, complicate, or overturn
  that membership during Pass 2a — matching the live precedent already set by
  `phenomenon.set/hib-still-warranted` ("review whether it still genuinely warrants being a HIB at
  all... before treating this HIB's phenomena as final").
- **The true cross-characteristic web is carried by explicit relation signals, not by the
  partition.** The old synthesis-B spec's D1 signal list (shared shape / co-occurring term /
  shared object-kind / pole-opposition / shared faculty-seat / cognate root / passage-adjacency) is
  the right shape of answer, but its concrete mechanics are written against the old schema and need
  re-grounding in `iba.db` — not yet done. This is the single largest piece of genuinely new design
  work Stage 2 still needs.
- **A pointer mechanism (re-surfacing a deferred cross-characteristic observation when its target
  next comes into focus) is needed, and does NOT already exist** — the old B+D pointer mechanism's
  literal DB shape (`from_id`/`related_activity`) was separately retired as unreliable (escalation
  #909); the *concept* (a deferred, traceable, focus-triggered re-surfacing) is sound and needed
  again, but has to be built fresh, not revived as-was.

**Pass 2a — Describe.** Per assembled characteristic-candidate, describe the behaviour/movement —
what makes up this piece of the inner being, grounded per-verse, from the evidence actually present
in each verse's own Stage-1 data (plus Window 2's existing `hib`/`phenomenon`/`operation` capture,
extended to draw on Stage 1's raw material directly rather than re-deriving it by eye). **No
per-verse-invariant property gets smuggled in as if freshly observed** — this is the exact,
named failure of the pre-reset cluster/faculty work (`faculty`/`type` as lemma-constants,
"relabelling fixed tags as per-verse discoveries") and it must not recur here.

**Pass 2b — Integrate.** Only after Pass 2a has run across the *whole* assembled set for a
characteristic-candidate: cross-segment deduction — what these described behaviours, together,
mean for the HIB as a whole. This is where the catalogue's **T0.2.1-class questions** (§7 of the
catalogue-coverage document, ~85 of 181 active questions — the largest single bucket in the whole
catalogue) actually get answered. **Never attempted before Pass 2a is complete for the relevant
set** — the same ordering discipline `phenomenon.set/phase-separation` already enforces at passage
scope ("must be completed for the WHOLE passage before any operation is written for ANY verse...
not interleaved... operation-writing momentum can bleed back into how the next verse's phenomenon
gets identified"), rescoped here from one passage to one characteristic-candidate's whole assembled
corpus.

**Status: principles agreed this session; no schema, no build, genuinely open design work
remaining** — named honestly as such, not overstated. What's settled: the two-pass split, the
provisional-partition segmentation approach, the phase-separation-style ordering rule, and the
explicit exclusion of T0.2.1-class questions from anything before Pass 2b. What's not settled: the
concrete `iba.db` mechanics for the relation signals and the pointer mechanism, and the schema (if
any) Pass 2a/2b's own findings get written to.

---

## 5. Stage 3 — Publishing

**Not designed in this document, or this session — named for completeness of the blueprint, not
filled in with invented detail.** `governance.programme_stages` already names it (essays and output
for the results, formerly "Session C"). Its own instruction docs (`wa-sessionc-cluster-overview`
etc.) predate every reset discussed this session and are not re-verified here. Flagged as a real
stage this blueprint deliberately leaves open, not silently assumed unchanged.

---

## 6. The catalogue's role, restated cleanly

`wa_obs_question_catalogue` is **not** a grid every characteristic must have every T-coded slot
filled in for — that exact framing (characteristic as a named, sortable unit with a fixed tier-grid
of questions) was explicitly set aside at the 2026-06-25 reset, and this session's own
catalogue-coverage check inherited that framing uncritically until the researcher caught it. Going
forward: the catalogue is **the areas-to-cover checklist** — a measure of whether the *cycle as a
whole* (Stage 1 + Stage 2's two passes) can, between them, get to every kind of question the study
actually needs answered, not a form to be filled in per named characteristic. Concretely, per this
session's full-catalogue check (companion document, §8):
- A minority of questions are single-verse and belong to Stage 1 or Window 2's existing per-verse
  capture.
- A real, sizeable set are pure lexical-aggregation questions, answerable once Stage 1's own
  related-words/testament/morph data is rolled up across a term's full occurrence set — no new
  capture needed, just a rollup layer.
- The largest single bucket (~85 of 181) is the T0.2.1 class — Stage 2 Pass 2b's job, not before.
- A real, named set (~30) have no owner anywhere in the current design — not blocking, but not
  silently dropped either.
- The catalogue's own wording needs revision for clarity, per the researcher's own observation this
  session — not undertaken here; a distinct, later piece of work.

---

## 7. Current status — one table, everything above in one place

| Stage | Design status | Build status | Owning document/escalation |
|---|---|---|---|
| Stage 0 (base substrate) | N/A — already exists | Built, 3 known live defects unresolved | #1441 (FK bug); design doc §2/§4 (role bug); capture-design doc §5 (`resolved_sense`) |
| Stage 1 (Level 1, lexical) | Mature, test-driven, not approved | Not started | #1383 — design/propose doc, checklist, calibration doc, method/drift-mitigation doc |
| Stage 2 (Level 2, behaviour, 2 passes) | Principles agreed this session; segmentation mechanics open | Not started | This document; #1383 (parked here for now) |
| Stage 3 (Publishing) | Pre-dates every reset discussed this session, not re-verified | Existing, unaudited | `wa-sessionc-cluster-overview` and its own instruction set — out of this document's scope |
| Catalogue (`wa_obs_question_catalogue`) | Coverage measured in full; wording revision flagged, not done | N/A | Catalogue-coverage companion document (§8) |
| Governance/config anchor layer | Live, in active use | Built and in use throughout this session | `iba/app/GOVERNANCE.md`, `cfg_behaviour_rule`, Developer Mode |

---

## 8. Companion documents this blueprint deliberately doesn't repeat

- `1383-verse-lexical-enrichment-design-propose-v1-20260903.md` — Stage 1's schema proposal.
- `1383-verse-lexical-enrichment-checklist-v1-20260902.md` — Stage 1's per-code item list.
- `1383-verse-lexical-window1-validation-test-plan-v1-20260903.md` /
  `...validation-applied-v1-20260903.md` / `...validation-calibration-v1-20260903.md` — Stage 1's
  test run and its own self-correction.
- `1383-verse-lexical-window1-method-and-drift-mitigation-v1-20260903.md` — the mechanical/
  judgement split, proven live.
- `1383-verse-lexical-window1-capture-design-vs-study-purpose-v1-20260903.md` — Stage 1 checked
  against Window 2's live schema; the FK-link and `resolved_sense` gaps first named here.
- `1383-verse-lexical-window1-catalogue-question-coverage-v1-20260903.md` — the full 181-question
  catalogue check, including the T0.2.1-class extraction (§7 there).
- `Workflow/methodology/wa-RESET-baseline-review-and-changeover-v1-20260625.md` — the historical
  record this blueprint deliberately doesn't re-derive.
- `Workflow/Instructions/wa-synthesis-B-spec-reset-v1-20260624.md` — the stale-but-structurally-
  sound design Stage 2's segmentation approach adapts from.

## 9. Confirmed next-step sequence (researcher, this session)

This blueprint accepted as the study's anchor. Confirmed sequence, in order: **(1) build the
lexical engine to finish Stage 1** — schema, `lexical.build` extension, `lexical.enrich` handler,
per the design/propose document; **(2) revisit Stage 0's discovered base-layer issues** (§2 above —
the `H0853` role bug, the orphaned-span FK bug #1441, the `resolved_sense` fallback question);
**(3) run Stage 1 through the passage system for the entire Bible.** Stage 2's own design (§4) is
understood to follow once Stage 1 is running at scale, not before.

**What "build the lexical engine" concretely still needs before it can start** — the accumulated
open decisions in #1383, not new analysis, just not yet explicitly closed:
- Schema sign-off: `verse_lexical` +4 columns, `passage.genre`, new `verse_lexical_note` table
  (design doc §5).
- The `H0853` classify_role fix (design doc §4) — designed, ready to build.
- The FK link from `phenomenon`/`operation` back to `verse_lexical_note` — build now, as part of
  this increment, or defer to when Stage 2 actually consumes it (capture-design doc §3/§8).
- `#1443`'s disposition (literary/structural findings → an emergent-question log, by
  `phenomenon.set` precedent) — confirm, so the schema doesn't carry a `note_type` for something
  that's been recommended to live elsewhere.
- The connective-type and negator lexicons — proven as a working prototype this session (drift-
  mitigation doc), needs promoting to real, registered code as part of this build, not re-prototyped.
- The `resolved_sense` fallback question (§2 above) — investigate before or alongside this build,
  since it bears on whether Stage 1's own baseline output is doing its stated job.

## 10. Open items for your decision

1. This document now covers ground well beyond #1383's original Window-1 scope — split it into its
   own escalation, or keep it parked here since #1383 is where this whole conversation has lived?
2. Stage 2's concrete build (the relation-signal mechanics, the pointer mechanism, whatever schema
   Pass 2a/2b write to) is real, substantial, not-yet-started design work — worth its own scoping
   pass once Stage 1 is further along, or is there value in designing them together now?
3. Stage 0's three known defects (§2) — a real disposition (fix now, fix as part of Stage-1 build,
   or something else) rather than left as three separately-tracked loose ends.
4. The catalogue's own wording revision (§6, your own observation) — scope it as its own piece of
   work, or fold into whichever stage ends up consuming it most.
