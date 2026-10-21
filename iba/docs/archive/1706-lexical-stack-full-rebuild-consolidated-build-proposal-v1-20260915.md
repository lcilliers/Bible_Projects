# Full lexical stack rebuild — consolidated build proposal

**Escalation:** #1706 · **Status:** design consolidation, decision_required, nothing built · **Date:** 2026-09-15

**Purpose, per researcher instruction verbatim:** *"consolidate all of these, there is a lot of
explorations through these, but has now all come together. we now need one coherent build proposal
that encapsulate the entire section, will ground it in what is already in existence and what is new
build, and then propose the full rebuild of the entire lexical stack."*

This document **consolidates as a tracking record** (not as content — nothing here overrides a
design decision already made) escalations **#1589, #1590, #1591, #1592, #1594, #1595, #1597, #1606,
#1607** (Layer 1/2 lexical core), folds in the already-designed **cluster-reading sign-off pack**
(#1690/#1691/#1692/#1693/#1696/#1697), and folds in **this session's own additions**
(#1704 role-driven-reading-sequence, #1705 verb_argument expansion, #1701 faculty resolution). It
does not re-decide anything already decided — every decision below cites the escalation/doc that
made it. Where something is genuinely still open, it's listed as such, not guessed.

**CORRECTION, 2026-09-16.** This document's first draft (2026-09-15) wrongly listed three Layer 1
items as open — the `role` pre-validator's design, the soft-delete-vs-hard-delete reading of
"dumped," and (by extension) §7 item 9 — when the researcher had already answered all three on
2026-09-09/10, in `1607-open-items-action-plan-v1-20260909.md` (D1), a document this draft's own
"governing design" citation (`1607-layer1-layer2-consolidated-column-spec-v1-20260910.md`) is built
from but which wasn't itself checked closely enough before those items were marked open. Fixed in
place at §6 items 3/4 and §7 item 9, not re-versioned — corrections to an in-review document land in
place. The remaining §6 item 4 (JSON internal shape) was resolved the same session, same-day
follow-up — **Layer 1's design is now fully closed, no open decisions remain.**

**CORRECTION 2, 2026-09-16 — Layer 2 section rewritten from a full re-read of the primary design
docs, not just this doc's own prior summary.** Per researcher instruction ("deeply and properly
review and assemble layer 2 work... decide what is outstanding... real information around the
decision-making points, not just churned"), §1/§2/§4/§5/§6/§7 below were rewritten against a full
read of `1682-cluster-reading-process-spec-v1-20260911.md`, `1682-cluster-reading-data-model-v1-
20260911.md`, `1690/1691/1692/1693/1696/1697-*.md` (every pack component, in full, not summaries),
and both `1704-*.md` docs — cross-checked live against `iba.db` (confirmed: **none of the pack's
five tables/columns exist yet — zero built, 100% design**). The single biggest correction: **#1705
closed 2026-09-15/16 with a reversal** (no `verb_argument` model expansion — direction is now
"guide the LLM with role data + questions, don't impose a resolution structure"), which invalidates
every reference below (and in the prior draft) to "#1705 gates Phase F" — replaced with #1711
throughout, a differently-shaped design question, not the same one under a new number.

---

## 1. Target architecture — the whole pipeline, stage by stage

**Corrected, 2026-09-15 — Layer 2 is its own stage, not folded into subgroup formation.** The
earlier framing (§1 as first written, and #1607 v15's own "layer 2... will be part of stage
cluster-subgroup" wording) blurred two different things together. Researcher, verbatim, this
session, laying out the actual chain: *"the process between lexical layer 1 -> layer 2 (produce
lexical observations and answers to lexical questions) -> capture lexical observations -> subgroup"*
— four distinct steps, not three. Layer 2 is the lexical-observation/lexical-question-answering
stage itself (what stage 5 below now names directly, not as a mysterious "new" addition); its
output gets **captured** (the recording pass, same #1693 §0 run-structure pattern already used for
reading/answer/synthesis: assemble → run the stage → record) as its own explicit step; only THEN
does subgroup formation (process b) run, consuming Layer 2's already-captured observations as
input — it does not perform Layer 2 judgement itself, as the table below previously (wrongly) said.

| # | Stage | What it is | Governing design | State |
|---|---|---|---|---|
| 0 | **Spine readiness** | verse→span→strong sync, extended-meaning-parse completeness | `governance.base_data_spine`, `Spine-Check.ps1` | **Live, enforced.** 0 FATAL findings this session. |
| 1 | **Lexical readiness check** | 3-leg check: every verse has ≥1 span (Leg1) · every span's strong resolves to a live `strong` row (Leg2) · every live strong has ≥1 `cluster_strong` allocation (Leg3) | #1606 | Leg1/Leg2 **PASS clean**. Leg3 **FAILS**: 111 strongs, zero allocation (H9xxx-dominated). Not yet a registered `cfg_method_rule` + persisted check, per the researcher's own #1606 instruction — **a real build item, not done yet.** |
| 2 | **Layer 1 build** (`verse_lexical`) | mechanical, per-code columns: `role`, `is_negator`, `party_kind`, `surface`, etc. — no `resolved_sense`, dropped (see stage 5) | #1592/#1607, `1607-layer1-layer2-consolidated-column-spec-v1-20260910.md` | **BUILT AND RUN, 2026-09-16.** 544,667 rows, 29,760 verses, corpus-wide, 0 errors. BUILD.md #267. |
| 3 | **cluster.status / cluster_subgroup.status readiness** | lifecycle gating columns | #1697 (cluster, v6), #1690 §3a (subgroup) | **BUILT, 2026-09-16.** Both columns live, 95/95 clusters backfilled, both enums registered. BUILD.md #267. |
| 4 | **Catalogue migration** | `wa_obs_question_catalogue` → `iba.db` | #1696 (v10) | **BUILT, 2026-09-16.** 92 rows live in `iba.db`, matching the Phase 5 content review exactly. `bible_research.db` copy flagged inactive. Real FK on `question_code` still deferred (needs a table rebuild once the write path exists). BUILD.md #267. |
| 5 | **`verse_meaning`** — Layer 2 lexical observations + lexical-question answers | multi-source LLM reading of the 3 meaning sources, per strong, **per cluster** — produces `ib_observation` row(s): general lexical observations AND slant-answers to T1.1 (Name/Naming, from surface + meaning-in-context) and T7.1 (Lexical/Semantic Analysis, from Layer 1 + Layer 2 jointly). This is where `resolved_sense`'s replacement lives — not a Layer 1 column | Researcher, verbatim, 2026-09-15 (§3 below) + 2026-09-16 (§4A, all 3 open items resolved) | **Design closed, 2026-09-16 — #1711 resolved.** Stage value `verse_meaning`, scope grain per-cluster, T1.1/T7.1 linkage both settled (§4A). Not built — Phase C (§6 items 13–16) still needs the actual config registration + build. |
| 6 | **Capture Layer 2 observations** | the recording pass (#1693) writes stage 5's LLM output into `ib_observation`/`ib_node` — same run-structure pattern already used for reading/answer/synthesis, made explicit here since it sits before subgroup, not after | #1693 §0 (pattern), extended | **New, explicit step** — not previously called out as its own stage; mechanism is #1693's existing same/broaden/new logic (fully specified), applied to a new input. Genuinely low-risk once stage 5 itself is designed — this is reuse, not a second design problem. |
| 7 | **cluster-subgroup build** (process b) | consumes stage 6's captured Layer 2 observations as input; outputs: subgroups, membership, catalogue-driven `ib_observation` (`stage='subgroup'`, #1691 §9 item 8) — its own, separate observations, not Layer 2's | #1690 (completed 2026-09-13) | **Design closed** except the stage-5/6 input wiring (new, depends on #1711). #1690 §7 item 4's "recommend a course of action on `strongs_reassigned`" routine deliberately left unbuilt — manual-only for now, researcher's own instruction. |
| 8 | **reading stage** (process c) | per-subgroup LLM read; inputs = subgroup's own `ib_observation` rows + Layer 1/2 lexical for every verse in scope, walked role-first (#1704 decision 1) | #1682 process spec §2, #1691/#1692 (`ib_observation`/`ib_node`, both completed) | **Design closed for the table shape.** Needs #1704's forced role-walk written into the process spec (§2 item 1 below) and #1691's `tag` taxonomy extended for the pointer/relational split (§2 item 2). **This is the fix for the #1607 v14 root-cause finding** (below). |
| 9 | **answer stage** (process d) | catalogue-question answering, multi-slant, per subgroup — adjacent-verse-context and cross-family/cluster flags are flagged, not resolved, this round (#1682 §4A) | #1682 §4A, #1691 (`tag`=`'slant'` placeholder still, direction confirmed §5 below) | Design closed for structure; needs stage 4 (catalogue in `iba.db`) landed for the real FK; catalogue-quality review (#1700/#1702, T3/T7 tiers still open) feeds directly into what this stage will actually be answering. |
| 10 | **synthesis/synergy stage** (process e) | cross-**cluster** (not just cross-subgroup) comparative claims, append-only, `supersedes` chain, `cluster_code` NULL (touched clusters recorded via `ib_node` rows instead) | #1682 §4B, #1691 §9 items 5/9, #1693 §0, #1695, **#1698 (still open)** | Table design closed. **Two real open gaps, both explicitly deferred by the researcher, correctly not urgent:** (a) the multi-cluster gating precondition (#1698 — a single-cluster `cluster.status='ready_for_synthesis'` check doesn't generalize); (b) the stage's own input JSON is undefined (#1691 §9 item 5, #1695) — needs more reading/answer-stage results first, by the researcher's own design. |
| 11 | **faculty reflection** (new) | end-of-read, subgroup-level observation — "where in the being did this happen," reframed as a reflection step, not a per-strong referent tag (#1704 decision 4, resolves #1701) | #1701 (v5, `ready_for_approval`), #1704 §5 decision 4, `1701-faculty-engagement-catalogue-addition-v1-20260916.md` | **DONE, 2026-09-16.** New catalogue component `T2.11` "Faculty Engagement" (2 questions, full field set), authored to close #1701 — not written to `bible_research.db`, folded into #1696's migration insert instead. No schema impact beyond an ordinary `ib_observation` row once built. |

**The recording pass** (#1693, formerly "load/reconcile") is the single write path into
`cluster_subgroup`/`cluster_subgroup_strong`/`ib_observation`/`ib_node` for every stage above — same/
broaden/new rules fully resolved (§4 below). **Hard constraint, all stages: `iba.db` only.** No step
anywhere in this pipeline reads or writes `bible_research.db` (DB fork, #737/#1682, 2026-09-13).

**Why stage 8 matters more than a normal design item:** the M10 prototype (#1682/#1690–1693's own
test data) confirmed live that the *previous* pipeline shape never passed `role`/`party_kind`/
`is_negator`/T-code data to the LLM at all — only plain verse text + surface/morph + dictionary
meaning. The LLM re-derived party identity from English prose instead of the live tags this whole
rebuild exists to get right (#1607 v14). Researcher's own diagnosis: *"we know that one of the
reasons why the original findings failed, was because it was based on simple verse reading...llm's
natural instinct of using the verse text, and effectively ignoring the enriched data that is
available happened again."* **This is the same root-cause failure that closed the original study
(2026-08-03)**, now confirmed reproduced once and fixed by construction in stage 8's design (the
subgroup's Layer 1/2 lexical is a mandatory input, not an optional enrichment).

---

## 2. This session's additions to the architecture (not yet folded into the specs above)

Recorded at #1704/#1701 (and formerly #1705, now closed and superseded — see item 3), **not yet
incorporated into #1682's process spec or #1691's `tag` design** — carried forward here as concrete
build requirements on stages 7–10:

1. **The role-driven walk must be structurally forced, not advisory** (#1704 §5 decision 1,
   confirmed). The reading-stage prompt/process design needs an explicit per-role checklist the LLM
   must work through and account for before synthesis — "silently ignore what it reads" is the
   exact failure mode already diagnosed once (§1 above, the #1607 v14 root-cause finding). #1704's
   own model gives the actual sequence to encode: (a) recognise the word's role → (b)(i) primary
   M-cluster = focal point → (b)(ii) other M-codes = relational + pointer observations → (b)(iii)
   sweep every party-kind word, per-party question sets → (b)(iv) walk T3 operation words against
   every nearby party-kind AND referent-identity (T10–T14) word → (b)(v) faculty reflection last
   (item 4 below). **Build item on stage 8's actual process design (#1682 §2)**, not yet written —
   the *sequence itself* is settled, encoding it as a structural checklist (not prompt wording) is
   the remaining work.
2. **Pointer observations are their own kind, always separate from relational** (#1704 §5 decision
   2, confirmed) — out-of-scope-referencing (queues discovery for a *different* verse/subgroup/
   cluster, never resolved inline), the raw material for stage 10's synergy work and #1698's
   cross-cluster gap. **Concretely, against what's actually live in #1691's `tag` design:** the
   reading stage already has a real, exercised 8-value taxonomy (`instance-meaning` 145,
   `verse-grouping` 110, `difference-inference` 39, `surface-gloss-divergence` 32, `no-human-context`
   23, `cross-family` 20, `data-error` 17, `alternative-meaning` 8 — M10 prototype counts) that
   already includes a `cross-family` tag; the answer stage has no real taxonomy yet, just a
   `'slant'` placeholder, though the *direction* is confirmed (a tag meaning "this answer raises
   something needing follow-up," folded flat rather than kept as separate arrays — #1691 §5).
   **Open, concretely:** does the relational/pointer split become two new reading-stage tag values
   (sharpening `cross-family` into two), two new answer-stage values, or both — not decided, because
   the actual tag vocabulary needs more real data first (#1691 §5's own stated position, unchanged).
   **Build item on #1691's still-open `tag` taxonomy**, informed by this split.
3. **`verb_argument` model expansion — SUPERSEDED 2026-09-16, replaced by #1711, not the same
   question.** #1705 (this item, as originally written) asked for a forced schema redesign —
   significance grading + multi-M-code relation as new fields on `verb_argument`. **Closed by the
   researcher, verbatim:** *"I am concerned that we are trying to over engineer the mechanical
   compilation of the verse, and then trying to induce it into analysis in relation the the verbs...
   it is not likely the right strategy to try and set a pattern in place to force it into a inner
   being role which it was never intended to be. I am now leaning toward guiding llm with the
   questions, rather than imposing T3 on the process."* The scenario-example digging that led to
   this (`1705-verb-argument-scenario-examples-v1-20260915.md`) showed the opposite of what a schema
   redesign would need: "almost every verse need different treatment," more digging producing more
   noise, not a consistent pattern. **What replaces it:** #1711 ("Design: Layer 2 lexical-observation
   process," deliberately sequenced by the researcher to start *after* Layer 1 closes) — same
   underlying need (T3/verb-operation surfacing matters, per #1704's own Phase 1b finding that T4.1–
   T4.5's 18 questions have zero mechanism), different shape: feed the LLM the role data + the
   catalogue questions and let it interpret the verse's context itself, not pre-impose a resolution
   structure it must satisfy. See §4A below for the full grounding this now needs.
4. **Faculty is an end-of-read, subgroup-level reflection, not a per-strong tag** (#1701's core
   question, resolved via #1704 §5 decision 4 this session) — dissolves the old "conceptually wrong"
   Inner-Faculties objection: asking "where did this happen" as a reflection made once at the end of
   a subgroup's read is a different kind of claim than tagging a strong with a fixed faculty referent
   at generation time. **A fresh catalogue question still needs authoring** — not drafted, and #1701
   itself is still open as an escalation (v4) despite its core question being answered.

---

## 3. Layer 1/2 lexical core — per-escalation disposition

### #1592 / #1607 — `verselexical.build` revisit + six-point column validation → **THE BUILD SPEC**

Researcher: *"this list of build actions will fundamentally set the verselexical build in motion."*
Confirmed: `1607-layer1-layer2-consolidated-column-spec-v1-20260910.md` **is** that list. Status,
column by column (✅ = decided, no further design needed; 🔧 = decided, schema/code change queued;
❓ = still open):

| Column | Disposition |
|---|---|
| `role` | 🔧 **Redesigned.** JSON array of every live `cluster_strong.cluster_code` per strong (not just the T4/5/7/8/9 subset). Empty set = ERROR, gated by a pre-run validator — **validator itself not yet designed** (§6 build item). |
| `ambiguity_note` | 🔧 **Drops.** Pairing moves to Layer 2 entirely; `role`'s completeness covers it. |
| `language` | 🔧 **Drops from `verse_lexical`.** Moves to a new verse-level `verse_meta` table (D13) — must re-point `_narrative_morph_for`'s language check in the same unit of work or Hebrew detection silently breaks. |
| `resolved_sense` | ❓ **On hold.** D2/D3 (source/truncation) assumed `strong_meaning_parsed` as source — that table is retired (#1668, meaning-distillation method under revision). **Genuine blocker on this one column only**, not the rebuild as a whole. |
| `surface`, `is_negator`, `party_kind`, `testament`, `gloss_consistent_in_verse`, `updated_at` | ✅ Unchanged mechanism, confirmed sound. |
| `verse_lexical_note.evidence_text` | See #1597 below — **superseded by design**, not a field-level fix. |
| `verb_argument` (D9) | **Superseded, 2026-09-16.** #1705's model-expansion project (significance grading, multi-M-code relation) closed without building — see §2 item 3. Not a Layer 1/2 field decision at all any more; whatever surfaces T3-operation data now happens through #1711's Layer 2 process design, not a `verb_argument` schema change. |

**Confirmed rebuild scope, researcher's own words:** *"the current 500k rows, plus the deleted rows
are all redundant... effectively all lexicals will be redone"* and *"soft delete all current
lexicals before first actual run starts."* **This is a full rebuild, not an incremental patch** —
every live `verse_lexical` row is superseded, not touched in place.

### #1589 — 6 of 15 `note_type` values undefined → **folded into the wider event-inventory work**

Researcher: *"folded into a much wider missing note-types list."* Confirmed: this is the same
underlying gap #1704's Phase 1 discovery generalizes (`note_type` = one instance of the broader
"analytic event" concept). #1589's own specific finding (idiom/pronoun_resolution/noun_relational/
noun_severity/polarity/compound_unit have zero `cfg_method_rule` definition) stays a real, unclosed
item — **not superseded, folded** — it becomes one line item in #1704's Phase 3 corrective-action
list once that phase runs, rather than a standalone decision here.

### #1590 — Greek/Hebrew role-tag bug → **SUPERSEDED, confirmed this session**

The bug lives entirely in `classify_role`/`_GREEK_FUNCTION_TAGS` — the morph-tag pattern-matching
mechanism that currently produces `verse_lexical.role`'s **old** `'content'`/`'function'` value. Per
#1592/#1607's confirmed redesign (above), `role` is being replaced wholesale with a
`cluster_strong.cluster_code` lookup — the same sourcing mechanism `is_negator`/`party_kind` already
use, not a morph-tag classifier at all. **The code path #1590 diagnoses is being deleted by this
rebuild, not fixed.** Recommend: close #1590 as superseded-by-design, no repair needed — confirm
before closing, since this is a disposition call, not a re-derivation of #1590's own evidence.

### #1591 — `surface` 192-row alignment defects → **moot; replaced by a post-build validation check**

Researcher, this chat turn: *"the new build instructions should be clear on how to determine
surface, old records are all set as deleted. research_db records are no longer relevant."* Combined
with the confirmed full-rebuild scope (above): the specific 192-row defect set belongs to data being
wholesale retired — there is no old-row list left to repair. **`surface`'s build rule is unchanged
and already clear** (denormalized from `span.surface`, #1607 spec item 14) — nothing new to design
there. What carries forward: a **post-rebuild data-quality check** (not a repair of old rows) —
re-run the same detection heuristics (multi-strong-same-position, empty-surface, ≥4-word spans)
against the *freshly built* rows once the rebuild completes, since the underlying interlinear
alignment behavior that caused the original defects is a property of the source data, not of the old
rows specifically, and could still surface in the rebuild. **Build item, not a design decision.**

### #1594 — verse-lexical enrich validated against the catalogue → **RESOLVED, both readings were partly right**

Researcher, earlier this chat turn: *"the verse-lexical enrich is now part of the stages as the
first step before subgroup."* Originally flagged as ambiguous between two readings (Layer 1 as the
true first step, vs. Layer 2 reverting to its own pre-pass). **Now resolved by the fuller
clarification later this session (§1 banner):** it's neither purely one nor the other — Layer 1
(stage 2) is still a hard precondition, genuinely first; but Layer 2 (stage 5) *also* runs as its
own explicit pre-subgroup pass, exactly the second reading that was flagged as the alternative. Both
were right, just not mutually exclusive as originally framed. #1594's own substantive finding (the
`passage.genre`/`passage.lexical_complete_at` Window-1→Window-2 handoff gaps, both orphaned by the
#1451 verse-scoping redesign) stays a real, separate finding — carried to §6's build list as its own
item (Phase G item 33).

### #1595 — `verse-lexical.note` structure/completeness → **folds into #1592/#1607's build spec**

Same disposition as #1592: this escalation's own findings (the `noun_relational`/`noun_severity`
pairing decision, still gated on #1593's lexicon-build scope) are real, open, and carried into §6 —
but the "one coherent build proposal" the researcher asked for **is** #1607's consolidated column
spec plus this document; #1595 is not a second, competing build target.

### #1597 — `verse_lexical_note.evidence_text` 100% unpopulated → **resolved by design, not by field-level decision**

Researcher, this chat turn: *"1701-1705 is all about this evidence."* Confirmed: the new
`ib_observation`/`ib_node` architecture (#1691/#1692) closes this gap **structurally**, not by
picking enforce-vs-merge on a field that's being superseded. `verse_lexical_note` (the old,
standalone Layer 2 pre-pass table) is retired in favor of `ib_observation`, whose grounding **is**
`ib_node` — and `ib_node`'s own CHECK constraint (at least one of
strong/verse_reference/cluster_subgroup_code/cluster_code/question_code/traced_observation_id must
be non-NULL) plus the **mandatory coverage self-check** (#1692 §2: every strong and verse in a
subgroup's membership must be grounded by ≥1 `ib_node` row, checked once by the LLM at generation
time and independently re-checked by the recording pass at load time) makes "no way to check any
finding's grounding" structurally impossible going forward — not a policy choice on one column. The
D8 enforce-vs-merge question (#1607) is **moot** for the same reason. **Recommend closing #1597 as
resolved-by-architecture**, confirm before closing.

### #1606 — 3-leg lexical readiness check → **confirms its place in the sequence, Leg 3 still open**

Researcher, this chat turn: *"lexical readiness is a precursor for the lexical reading stage, which
is a precursor for the sub group."* Confirmed as stage 1 in §1's table. Leg 1/2 pass; **Leg 3 still
fails (111 strongs, zero cluster allocation)** — genuinely the researcher's own call on timing (same
by-hand T-code classification work already done for T4/T5/T6/T7/T9/T15), not something to auto-apply
here. **Not yet built as a registered, persisted check** (`cfg_method_rule` + report), per the
researcher's own original #1606 instruction — a real, outstanding build item (§6).

---

## 4. Cluster-reading sign-off pack — status correction

**The pack tracker in `1682-cluster-reading-data-model-v1-20260911.md` is stale** (dated
2026-09-13, shows only #1690 as READY). Reading each component doc's own latest "what would
finalized mean" section (2026-09-14/15) plus the live escalation state (checked 2026-09-16) tells a
different, more current story — **design content is fully closed on all 6; escalation workflow
status is NOT uniformly closed; and none of the 5 tables/columns are built** (confirmed live:
`cluster_subgroup`, `cluster_subgroup_strong`, `ib_observation`, `ib_node`,
`wa_obs_question_catalogue` don't exist in `iba.db`; `cluster.status` column doesn't exist):

| Escalation | Component | Design content | Escalation workflow state (live, 2026-09-16) |
|---|---|---|---|
| #1690 | `cluster_subgroup`/`cluster_subgroup_strong` | ✅ Design-complete, approved 2026-09-13 | `completed` |
| #1691 | `ib_observation` | ✅ Design-complete — "every §4 item now closed" except the synergy-stage input (§10, explicitly *not* a blocker) | **v18, still `in-progress`/`review`** — content resolved but never formally closed, unlike its 3 siblings. Loose end, not a design gap. |
| #1692 | `ib_node` | ✅ Design-complete — "RESOLVED... every §4 item now closed... ready to register" | `completed` |
| #1693 | the recording pass | ✅ Design-complete, name settled ("the recording pass") | `completed` |
| #1696 | catalogue migration | ✅ Design-complete, CSV reviewed, "migration can proceed" | **v10, `re-assigned`/`ready_for_approval`** — deliberately held pending #1706 itself (researcher's own sequencing, this session) |
| #1697 | `iba.cluster.status` | ✅ Design-complete, 2026-09-15, all 5 items resolved | **v6, `re-assigned`/`ready_for_approval`** — awaiting sign-off |

**All 6 pack items are now design-complete.** #1697's 5 open items (its own §5), resolved this
session, item 1 confirmed last, researcher verbatim: *"confirmed, I do not see any spelling
issues."*
1. **RESOLVED.** Spellings confirmed as proposed, no corrections.

   | ordinal | your wording | proposed value |
   |---|---|---|
   | 1 | "strong assignment in progress" | `strong_assignment_in_progress` |
   | 2 | "T-cluster assignment completed" | `t_cluster_assignment_completed` |
   | 3 | "ready for subgroup allocation" | `ready_for_subgroup_allocation` |
   | 4 | "ready for reading" | `ready_for_reading` |
   | 5 | "ready for observations" | `ready_for_observations` |
   | 6 | "ready for synthesis" | `ready_for_synthesis` |
   | 7 | "completed" | `completed` |
   | 8 | "strongs re-assigned" | `strongs_reassigned` |

2. **RESOLVED, researcher, verbatim, 2026-09-15:** *"I assume this ordinal is the status on the
   cluster. as such 2 (T-cluster assignment) was a one off process, so it will not really be
   repeated. but it can stay. it has no real impact. stages 3-8 is real as [should] be built in the
   code for assigning the states."* Confirmed: this enum **is** `cluster.status`. Ordinals 1–2 are a
   **historical, one-off phase** (the T-code/M-code `cluster_strong` population work —
   #1606/#1598/#1694's own work) — real, but not an ongoing mechanism: no code needs to gate or
   transition between 1 and 2, they're kept in the enum for completeness/record, not actively
   checked. **Ordinals 3–8 are the real, active lifecycle** — the one that actually needs code built
   to assign/transition through it (per #1690 §3a/#1693/#1697 §3's own designs). Register the full
   1–8 enum in `cfg_enum`, but build gating/transition logic only for 3–8.

3. **RESOLVED, researcher, verbatim, 2026-09-15:** *"the ready_for_observations is set when the
   verse reading stage for all the subgroups in the cluster is completed."* Confirms the rollup
   reading exactly — `cluster_subgroup.status='ready_for_answer'` already means "reading complete for
   this subgroup" by its own §3a definition, so "every subgroup's reading stage completed" and
   "every subgroup at `ready_for_answer`" are the same condition stated two ways. Not a gate any code
   checks before running the answer stage — the cluster-level signal that it now can.

4. **RESOLVED, researcher, verbatim, 2026-09-15:** *"strongs_reassigned must trigger a warning to
   the chat. I do not see that the system can proceed with autoamted resetting, I want to control
   that process, for at lease a few rounds."* Picks option (a) — purely manual — and sharpens it:
   the visibility must be **active**, not passive. Landing in `strongs_reassigned` must **raise a
   real escalation** (decision_required, assigned to Researcher, naming the affected cluster and
   what changed) at the moment the transition fires, not just sit as a column value someone might
   notice later. **No automatic resubmission of process (b), and no automatic "recommend a course of
   action" routine** — that routine (#1690 §7 item 4's own floated idea) stays unbuilt for now;
   revisit automating any of this only after the researcher has run the manual process for a few
   rounds and knows what "control" should actually look like.

5. **RESOLVED, follows from #2.** Since ordinal 2 is a one-off, already-completed, no-real-impact
   phase (not a review-cleanliness gate — the 631-row/43-cluster `review_flag` split is NOT the
   criterion), the simple, consistent backfill is: **all 95 live `cluster` rows start at ordinal 2
   (`t_cluster_assignment_completed`)** — every one already has `cluster_strong` members, so every
   one is past ordinal 1 already. This is also the correct starting line for the real pipeline: once
   ordinals 3–8 are built, every cluster begins eligible to move to `ready_for_subgroup_allocation`.

**All 6 pack items are now design-complete — #1697's own 5 items, the last open ones in the whole
pack, are resolved as of this session.** No remaining Claude-side design work anywhere in the pack;
what's left is (a) the researcher's actual sign-off nod across all six, (b) tidying #1691's
escalation status to match its 3 completed siblings (content is equally resolved), and (c) the
build itself (§6) — all 5 tables/columns, confirmed live as not yet created.

**★ Post-approval addition, 2026-09-16 (#1526).** `cluster_subgroup` gains `anchor_verse_reference`
— one representative verse per subgroup, decided by process (b)'s own LLM session, written in the
same DB update as the rest of the subgroup row (#1693's recording pass), never a separate pass.
Supersedes #1526's original per-strong `resolved_sense`-keyed proposal (moot anyway — `resolved_sense`
is dropped from Layer 1, see Phase B item 10). Applied to both #1690 (`1690-...` §2A) and #1693
(`1693-...` write-mechanism table) even though both were already `completed` — a real post-approval
change, not new design. **Selection criterion RESOLVED, same day:** researcher, verbatim, *"the
verse that best describe the subgroup characteristic is selected by llm to serve as anchor"* —
process (b)'s own judgment call, added as governing-rule item (h) (#1690 §2). No open item remains
on this addition; exact prompt wording is a build detail for Phase F item 25 below, not a design gap.

**Not part of the pack, but immediately adjacent — #1698, still genuinely open.** Item (i) resolved
(`ib_observation.cluster_code` nullable for synthesis); item (ii) — #1697's `cluster.status=
'ready_for_synthesis'` precondition is a single-cluster check, and synthesis is confirmed
cross-cluster — doesn't generalize. **Correctly not urgent**: this only matters once synthesis
(stage 10) is reached, and the researcher has already deferred synthesis until build+test through
the answer stage (stage 9) is complete (§1 stage 10, #1693 §0). Nothing to resolve now.

---

## 4A. Grounding for #1711 — the pre-subgroup Layer 2 stage, what it inherits and what's genuinely new

**Purpose:** #1711 ("Design: Layer 2 lexical-observation process") is where stage 5/6 actually gets
designed — not here (§4A doesn't decide anything, it assembles what #1711 needs so that design
doesn't start from a blank page or re-litigate what the pack already settled).

**What this stage inherits from the pack, unmodified — it is not a new mechanism, it's a new input
to an existing one:**
- The same three-part run structure every other stage uses (#1693 §0): assemble input → run the
  LLM pass → the recording pass writes it. Nothing about stage 5 needs a different write mechanism.
- The same `ib_observation`/`ib_node` table shape (#1691/#1692, both design-complete) — a
  `stage`-scoped row, grounded via `ib_node` segments, same CHECK constraint, same coverage
  self-check pattern (#1692 §2's "every strong/verse in scope must be grounded by ≥1 node" — the
  same self-check the reading stage already requires, not invented for stage 5).
- The same same/broaden/new reconciliation logic (#1693 §3, fully resolved) for whether a new
  reading merges with, expands, or sits beside an existing observation on a re-run.
- The precedent for adding a genuinely new `stage` value: process (b) already got one this way
  (`subgroup`, #1691 §9 item 8) when live evidence showed it produced observations with no home —
  the same move (new enum value, same table, same write path) is what stage 5 needs, not a new
  table or a parallel mechanism.

**RESOLVED, 2026-09-16 — all 3 items, researcher verbatim this chat turn.** #1711 v11 closed the
design with no open decisions remaining:

1. **Stage name/value — `verse_meaning`.** Not `meaning` or `lexical` (the two candidates on
   record) — a new, more specific value naming what this pass produces, not just the layer it
   belongs to.
2. **Scope grain — per-cluster.** Not corpus-wide in one pass. Runs alongside/just ahead of each
   cluster's own process (b), matching process (a)/(c)'s own existing batching pattern (smaller
   runs, easier to re-run one cluster). The term-grain concern below (item 3, T1.1/T7.1 needing
   more than one cluster's slice of a strong's occurrences) is resolved by *how* those questions are
   answered, not by forcing corpus-wide scope.
3. **Catalogue question linkage — both T1.1 and T7.1, each with its own derivation.**
   **T1.1** (Name/Naming) is derived from reviewing the strong's `surface` + its meaning in context
   (Layer 1 surface data + the meaning sources, read per occurrence). **T7.1** (Lexical/Semantic
   Analysis) is derived from Layer 1 *and* Layer 2 jointly — it draws on this stage's own output,
   not just the raw meaning sources.

Full record: escalation #1711 v11. Not built — Phase C (§6 items 13–16) still needs the actual
config registration and the stage 5/6 mechanism itself built; nothing above changes that.

**Two more real items, found 2026-09-16 checking #1607's own Layer 2 spec against #1711 directly
(not carried over before now):**

- **D7 (`#1607`) — RESOLVED, researcher, verbatim, 2026-09-16: passage dropped as a reading unit
  entirely, replaced by an observation-level flag.** *"passage was dropped as a method and
  replaced by a observation rule to raise a requirement to read additional verses if needed.
  passages are no longer presented as a unit of reading."* `verse_lexical_note.passage_id` is
  confirmed **drop, not repurpose** — there's no unit left for it to anchor to. The replacement is
  already tracked, not new: `needs_adjacent_verse_context` (#1682 §4A item 1, confirmed direction
  at #1691 §5 as a `tag` value, empirically tracked at #1703). **Independently confirms #1703's own
  v2 finding** (researcher, that escalation, same principle in different words): the old
  `passage`/`verse_passage` structure was withdrawn as a candidate resolution mechanism because it
  was built for sequential book-reading, not subgroup-based (lexical-family-first, cross-book)
  reading — a related verse's *relevance*, not its *proximity*, is what matters now. **What's still
  genuinely open, per #1703's own unchanged finding:** the flag's *resolution* mechanism (what
  actually happens once `needs_adjacent_verse_context` is raised — a follow-up read? a permanent
  caveat?) and its real rate at scale — both still untested, #1711/#1703's own scope, not resolved
  by today's confirmation that passage-as-unit is gone.
- **`resolution_status` / the "unresolved, not guessed" principle — RESOLVED, researcher, verbatim,
  2026-09-16: this belongs at the design-principle level, not as a leftover column question.**
  *"these methods should be fundamentally part of the observation rules."* Confirmed: the
  discipline (never guess, record inability to resolve explicitly) is a governing rule for every
  `ib_observation`-writing stage, not a column to individually port over from `verse_lexical_note`.
  Concretely, it should surface as a `tag` value (matching how `data-error`/`no-human-context`
  already work) at whichever stage a genuine "couldn't resolve from available data" case arises —
  not designed further here, folded into the consolidated observation-rules checklist below.

**★ NEW, 2026-09-16 — consolidated observation-rules checklist, per researcher instruction:**
*"it worries me that you do not have an easy checklist for all the observation rules to check
against."* Built: `ib-observation-governing-rules-checklist-v1-20260916.md` — every rule
governing any `ib_observation`/`ib_node`-writing stage, pulled from #1682/#1690–1693/#1697/#1704/
#1607, organized so it can actually be checked against, not scattered across a dozen design docs.

**★ NEW, 2026-09-16 — a real governing rule for stage 5, not just a #1658 resolution.**
Researcher, verbatim: *"the important take away is to read meaning from all three tables because
they are complementary, rather than replacing each other."* Confirms #1658 doesn't block this
build (assembly reads `strong_meaning_tree`/`strong_lexicon` lsj/mounce directly, no view
registration needed) — but the substantive point is the design rule itself: stage 5 must read all
three meaning sources for every strong and treat them as complementary evidence, never as
redundant alternatives where one is picked and the others dropped. This is the exact same
discipline the reading stage (process c) already has as its own rule 2 (checklist §2 item 2:
*"Read all three meaning sources in full for every strong — never dump raw text unread, never
skip a source"*) — stage 5 inherits it, not a new principle invented for Layer 2. **Add to the
checklist's own stage-5 section once #1711 is designed** — not added there yet since stage 5 has
no section in the checklist until its design exists.

**The #1705 closure's direct bearing on #1711:** the same principle that closed #1705 applies here —
don't pre-impose a resolution structure (e.g. a rigid "answer these N questions in this order" walk)
on this stage's LLM pass; give it the role/T-code data plus the earmarked questions and let it
interpret the verse/term context itself, consistent with how #1704's role-driven sequence for stage
8 is a *discovery order*, not a forced answer format. Whether stage 5 needs its own version of the
"structurally forced, not advisory" walk from #1704 §2 item 1 — since that principle and this one
aren't actually in tension (forced *sequence*, free *interpretation*) — is itself part of #1711's
design, not decided here.

---

## 5. This session's un-folded additions — real, but not yet spec-level

Unlike §3/§4 (existing designs this proposal grounds and sequences), these are **requirements that
don't yet have a spec to point to** — listed so they aren't lost, not so they block the build below:

- **#1704** (role-driven-reading-sequence) — the forced-walk requirement and the pointer/relational
  split (§2 items 1–2) need writing into #1682's process spec for stage 8 and #1691's `tag` design
  respectively; not done. #1704 itself also still owes Phase 2 (match each candidate event against
  the 4-part name/config/code/purpose test) and Phase 3 (corrective actions) — Phase 1's discovery
  is complete (both docs read in full for this review), the follow-through phases haven't run yet.
- **#1711** (Design: Layer 2 lexical-observation process — replaces #1705) — genuinely undesigned;
  §4A above assembles what it inherits from the pack and the 3 real open items (stage name, scope
  grain, catalogue-question linkage) with actual substance, not just names. **Deliberately sequenced
  after Layer 1** by the researcher's own instruction this session — not gating anything right now.
- **#1701** (faculty reflection) — **DONE, 2026-09-16.** Framing resolved (§2 item 4), catalogue
  question authored (`T2.11` "Faculty Engagement"), folded into #1696's migration. No schema
  impact beyond an ordinary `ib_observation` row once built.
- **#1698** (synthesis cross-cluster gap) — real, correctly deferred until stage 9 is built and
  tested (§4 above) — not a current blocker, listed so it isn't lost when synthesis is actually
  reached.
- **#1700/#1702** (answer-stage catalogue-question quality) — in-progress systematic review; T0/T1/
  T2/T4/T5/T6 sections done, T3/T7 remain (#1700 v8). Directly feeds what the answer stage (stage 9)
  will actually be answering — worth finishing before that stage runs for real, not a hard gate on
  the build order above.

---

## 6. The build action list

**Ordered by actual dependency, not by escalation number.** Each item names what it produces and
which escalation/spec it draws its design from. Nothing here executes without the researcher's
go-ahead — this is the proposal, not the build log.

### Phase A — base-data readiness (must run before Layer 1 rebuild)

1. **DONE, 2026-09-16.** `lexical.readiness` built and registered (`handlers/lexical.py:readiness`,
   `cfg_step`/`cfg_method_rule`/`cfg_report`) — 3-leg check, run live: 0 FATAL findings, both before
   and after Phase B's rebuild. Full record: BUILD.md #267.
2. **DONE, 2026-09-15** (already recorded elsewhere in this doc) — all 111 classified.

### Phase B — Layer 1 cutover + rebuild (`verse_lexical`)

**Researcher instruction, verbatim, 2026-09-15:** *"the current lexical records will all be dumped.
layer 1 has materially changed and the table schema changed. your proposal must include the steps
to desolve the old lexical configuration, and set the new configuration. layer 1 will be processed
in bulk to produce fresh results for the entire corpus. I am no longer interested to try and
reconcile old data, and the discrepancies in the old data is not going to be 'fixed'."* Confirms:
full corpus-wide bulk rebuild, no incremental/per-word processing; no effort spent reconciling or
repairing old data (the fresh rebuild **is** the fix); and — new requirement — the old Layer 1
*configuration* (not just the data) must be explicitly retired as its own step, not left to drift
alongside the new one. **"Dumped" = soft-delete (`deleted=1`) — already explicitly instructed, not
just inferred** (corrected 2026-09-16, this document's first draft wrongly asked for reconfirmation):
researcher, verbatim, `1607-open-items-action-plan-v1-20260909.md` D1, 2026-09-09/10: *"soft delete
all current lexicals before first actual run starts."* The Sept-15 "dumped" wording is the same
instruction restated, not a new, unconfirmed one — no literal hard delete was ever on the table.

3. **DONE, 2026-09-16.** Built as `unready_codes_in_scope`/`NotReady` (`lib/lexical.py`) — fail-fast
   at run start, scoped to the run's own scope, wired into `build_for_range`/`build_for_verse_ids`
   and every handler call site. Full record: BUILD.md #267.
4. **DONE, 2026-09-16.** Bare JSON array of cluster codes, live: `load_role_codes`/`_role_for`
   (`lib/lexical.py`). **Layer 1's design is now fully closed** and built.
5. **DONE, 2026-09-16.** `rebuild_verse_lexical_layer1_v1_20260916.py` — dropped `cfg_column` rows
   for `ambiguity_note`/`language`/`resolved_sense`; `lexical.enrich` marked inactive (the old
   `role`/`resolved_sense`-adjacent mechanism). Full record: BUILD.md #267.
6. **DONE, 2026-09-16.** `role`'s new shape registered in `cfg_column`; `verse_meta` already had its
   own registration (#1608, item 9 below); the rebuild routine registered as `cfg_step
   verse-lexical/lexical.readiness` plus the existing `lexical.build`/`lexical.run` steps, no new
   `cfg_utility` needed (reuses the existing handler).
7. **DONE, 2026-09-16.** 544,590 live rows soft-deleted, same migration as item 5.
8. **DONE, 2026-09-16.** Corpus-wide rebuild run for real: 544,667 rows, 29,760 verses, 93 seconds,
   0 errors (`run_verse_lexical_layer1_rebuild_v1_20260916.py`). `ambiguity_note`/`language` dropped,
   `_narrative_morph_for` re-pointed, `role` redesigned, `resolved_sense` dropped from Layer 1
   entirely. Verified live: 0 NULL/empty-array role, 0 malformed JSON (5,000-row sample),
   `verse_meta.language` correctly recomputed via the fixed trigger (21,902 Hebrew + 7,858 Greek =
   29,760, 0 NULL). Full record: BUILD.md #267.
9. ~~Create the new verse-level `verse_meta` table (D13)~~ — **already done** (#1608, 2026-09-09;
   confirmed live, checked 2026-09-16: exists, registered in `cfg_table`, 29,760 rows, `language`
   column already present). Not an outstanding action — flagged as one in this document's own §6
   in error until this correction; §8's register already had it right.
10. **RESOLVED, researcher, verbatim, 2026-09-15, continuing the same instruction:** *"what is
    important is the new design of layer 1 is sound, and form the right base for the llm controlled
    layer 2. the new multi-source reading should be part of layer 2. it will be a observation
    (linked to a question) that will hit the DB before subgroup start, and would therefore be
    available as data when subgroups are formed."* Definitively resolves Phase B's old item 7
    (`resolved_sense`'s source/truncation): it doesn't move to a Layer 1 replacement at all (options
    (b)/(c) from the prior round are both out) — the multi-source reading of `vw_strong_meaning_raw`
    becomes a **new Layer 2 stage** (§1 stage 5), producing an `ib_observation` row per strong,
    linked to a catalogue question, written **before** process (b) (subgroup allocation) so its
    output is available input when subgroups are formed. This stage is genuinely new — see §1 stage
    5 and the open items below, not designed further in this document.
11. **Not done, 2026-09-16.** The surface-alignment post-build validation heuristics against the
    fresh rows were not re-run this session — a real, cheap follow-up, not forgotten, just not
    reached in this build round.
12. **Already applied earlier this session** — #1589/#1590/#1591/#1592/#1594/#1595/#1597 all closed
    (see BUILD.md #267's own scope note and this doc's SS8 register).

### Phase C — Layer 2: lexical observations + capture (genuinely undesigned — §1 stages 5–6)

Not a small addition to Phase B — two new steps in the pipeline (produce, then capture). Design
closed 2026-09-16 (#1711 v11, §4A) — build work remains, not decisions:
13. **Stage value DONE, 2026-09-16** — `verse_meaning` registered live in `ib_observation.stage`
    (`cfg_enum`, `create_cluster_reading_pipeline_tables_v1_20260916.py`). The actual assembly/
    LLM-calling mechanism that WRITES stage=`verse_meaning` rows is still not built (see BUILD.md
    #267's "Not done").
14. **Scope grain confirmed, not yet exercised** — no code runs per-cluster batches yet; the
    mechanism (`lexical.readiness`-style selector via `lexicalscope.py`) already exists for Layer 1
    and can likely be reused, not yet wired to the new stage.
15. **Catalogue linkage now buildable** — the FK's real target exists (`wa_obs_question_catalogue`
    live in `iba.db`, 92 rows, T1.1/T7.1 present), but `ib_observation.question_code`'s actual FK
    constraint is still un-enforced (SQLite FKs are declare-at-create-time; adding one needs a
    table rebuild, deferred to when the write path is built) and no code populates it yet.
16. **RESOLVED, researcher, verbatim, 2026-09-15 — capture is its own explicit step, not folded
    into Layer 2's own LLM pass.** *"layer 1 -> layer 2 (produce lexical observations and answers
    to lexical questions) -> capture lexical observations -> subgroup"* — four steps, not three.
    Mechanism confirmed as the recording pass (#1693), same run-structure pattern as every other
    stage (§1 stage 6) — not a new mechanism, but its own visible pipeline step, not silently
    absorbed into Layer 2's own description the way earlier drafts of this doc had it.

### Phase D — cluster/subgroup readiness gates

17. **DONE, 2026-09-16.** `iba.cluster.status`/`status_changed_at` added, `cfg_enum` registered (8
    values), all 95 live clusters backfilled to ordinal 2. Full record: BUILD.md #267.
18. **DONE, 2026-09-16.** `cluster_subgroup.status` created as part of the table (item 20), `cfg_enum`
    registered (6 values).
19. **DONE, 2026-09-16.** `wa_obs_question_catalogue` migrated into `iba.db` — **92 rows, exactly as
    expected**, `T2.11.1`/`T2.11.2` added, `T7.1.3` revised, 8 codes dropped per the Phase 5 review.
    `bible_research.db`'s copy flagged `inactive=1`. **Not done:** the real FK on
    `ib_observation.question_code`/`ib_node.question_code` — deferred to when those write paths are
    built (SQLite FKs are declare-at-create-time only). Full record: BUILD.md #267.

### Phase E — cluster-reading pipeline tables

20. **DONE, 2026-09-16.** `cluster_subgroup` (with `anchor_verse_reference`, the post-approval
    addition) and `cluster_subgroup_strong` created in `iba.db`, registered in `cfg_table`/
    `cfg_column`. Full record: BUILD.md #267.
21. **DONE, 2026-09-16.** `ib_observation` created, registered — `stage` enum includes the new
    `verse_meaning` value from item 13.
22. **DONE, 2026-09-16.** `ib_node` created, registered, CHECK constraint verified live (a synthetic
    all-NULL-grounding insert correctly rejected).
23. Build the recording pass (#1693) — same/broaden/new logic (fully specified), verse-reference
    resolution, denormalization, the two-level status check/advance (cluster + subgroup grain),
    the `placement_note`-promotion mechanism (mechanism itself still undesigned per #1693 §2, a
    real sub-item), and Phase C item 16's new write path.

### Phase F — pipeline execution, stage by stage

24. Run Layer 2 (Phase C) for real, corpus-wide or per-cluster per item 14's resolution — produce,
    then capture (stage 5 → stage 6) via the recording pass — its output must exist before process
    (b) runs.
25. Run process (b) (subgroup allocation) for real, against the rebuilt Layer 1 data and stage 24's
    captured Layer 2 observations — supersedes every prototype run to date (#1696 §4 item 4: prototype JSONs
    are not migrated or treated as real data).
26. Build stage 8's reading-stage process design update for the forced role-walk requirement
    (#1704) — a real spec change to #1682, not done yet.
27. Run process (c) (reading) per subgroup, with Layer 1/2 lexical genuinely reaching the LLM this
    time (the #1607 v14 fix, confirmed by construction in this design).
28. Run process (d) (answer) per subgroup, once #1696 lands (Phase D item 19) for the catalogue FK.
29. **Deferred, per researcher instruction:** process (e) (synthesis/synergy) waits until build+test
    through stage 28 is complete and its cross-cluster gating precondition (§1 stage 10) is designed.

### Phase G — carried-forward, not gated by anything above

**CORRECTED, 2026-09-16 — #1705 is closed, does not gate Phase F.** The prior draft (2026-09-15)
said `verb_argument`'s redesign gates stage 5/8's T3-operation handling. That's superseded: #1705
closed without a redesign (§2 item 3) — direction is now #1711 (§4A), deliberately sequenced by the
researcher to start *after* Layer 1, not a precondition blocking Phase F. Phase F's stage 5/8 work
does still need *some* T3/operation-surfacing mechanism (per #1704 Phase 1b's own finding that
T4.1–T4.5's 18 questions have zero live mechanism) — that need is real, but it's #1711's design
output that will supply it, not a `verb_argument` schema change gating this phase.

30. ~~#1701 (faculty reflection) — author the new catalogue question~~ — **DONE, 2026-09-16**
    (`T2.11`). Two other items still fold into #1701's own resumption per #1704 Phase 2/3: T3-
    operation-surfacing and constitutional-level vocabulary detection (T2.1's own, separate gap —
    not resolved by `T2.11`), both deliberately not designed standalone.
31. Close out #1691's escalation to match its 3 completed pack siblings — content is equally
    resolved (§4), this is workflow hygiene, not a design task.
32. **DONE, 2026-09-16 — #1704 Phase 2/3 complete, corrected same day.** Full event inventory: 8
    buildable now (Group A, incl. `directional-party-frame` — 18 questions, highest-value single
    item), 5 need design first (Group B), 2 fold into #1701 (Group C). **Correction (Group D),
    same day:** checked live rather than assumed — **10 of 15 `note_type` values lack a registered
    `cfg_method_rule`, not the 6 `#1589` originally scoped.** All 15 now accounted for: 5
    registered (`related_word`/`structural_pattern`/`recurrence_role_shift`/
    `cross_lemma_shared_gloss`/`verb_argument`); 8 have confirmed purpose, just need the config row
    (`compound_unit`→T1.2.2, `polarity`→T1.7, `chain`/`connective`→T7.2.1, `entity_link`/
    `pronoun_resolution`→ supporting role for `party_kind`/`directional-party-frame` accuracy, not
    a standalone catalogue answer); `idiom` genuinely still open (no confirmed question match);
    `inert` a low-priority governance formality (bookkeeping, purpose already implicit elsewhere).
    Docs: `1704-analytic-event-inventory-phase2-match-v1-20260916.md`, `-phase3-corrective-
    actions-v1-20260916.md` (Group D). Also tracked at escalation #1607 (Layer 1/2 column
    validation) — the parent venue for actually writing these `cfg_method_rule` rows.
    **Phase 4, same day**: full per-question crosswalk, all 100 live questions, the exact
    mechanism per question not just the event category — `1704-analytic-event-inventory-phase4-
    question-crosswalk-v1-20260916.md`. Surfaces at this granularity: 20 question codes share the
    single highest-leverage build item (`verb_argument`×`party_kind`); 4 (`T4.6.2a/2b/3a/3b`) have
    a fully live, unconnected mechanism — zero design work, pure wiring.
33. **DONE, 2026-09-16 — consolidated, then closed, not just carried forward.** #1594's
    `passage.genre`/`verse_meta.genre` orphaned-column finding is confirmed (Phase 2) to be the
    SAME root cause as T7.2.2a/2b's unexercised split (#1700's T7 review) and #1607 D12/D13's
    dropped `genre` column — one finding, not three. **Resolution, per Phase 5 researcher review**:
    not rebuilt — `T7.2.2a/2b`/`T7.2.4` are retired from the catalogue entirely (genre judged to add
    no real value for inner-being interpretation), consistent with the standing #1608 ruling.
    `verse_meta.genre` stays dropped, permanently, not a pending rebuild.
34. **DONE, 2026-09-16 — #1700/#1702 review complete.** All 98 (now 92 after researcher content
    review, item 32) live catalogue questions
    reviewed (T0–T7, confirmed no live non-tier material exists) — zero genericity found anywhere;
    every gap is coverage or connection, never quality. Directly feeds what Phase F item 28 (answer
    stage) will be answering. New open item from this work: `pattern_type` (the catalogue's own
    event-cross-reference column, 100% NULL) has a ready-to-apply crosswalk — sequencing question
    for the researcher (write now vs. fold into #1696's migration insert, recommended) at #1704
    Phase 3's own closing section.

---

## 7. What this proposal needs from the researcher to move to execution

1. ~~Confirm or correct §3's per-escalation dispositions~~ — **DONE, 2026-09-15.** Researcher closed
   #1589/#1590/#1591 directly (`supersede`, folded into #1704) and #1594/#1597 directly (`supersede`,
   confirming this doc's own readings) via direct escalation-tool action, outside chat.
2. ~~Confirm the reading of #1594's quote~~ — **DONE, 2026-09-15**, resolved: both readings were
   right, not mutually exclusive (§3).
3. ~~Answer #1697's 5 open items~~ — **DONE, 2026-09-15**, all 5 resolved (§4), #1697 `ready_for_approval`.
4. Sign off the pack (#1690/#1691/#1692/#1693/#1696/#1697) as a set, per the pack's own existing
   convention.
5. Decide Phase A item 2 (Leg 3's 111 strongs) — **DONE, 2026-09-15**, all 111 classified (#1606
   closed).
6. ~~Decide `resolved_sense`'s fate~~ — **DONE, 2026-09-15.** Dropped from Layer 1 entirely; the
   multi-source reading is Layer 2 itself — its own produce (§1 stage 5) + capture (§1 stage 6)
   pair, running before subgroup (§1 banner, Phase C items 13–16). Layer 2's own internal design is
   now the open item — see 8 below.
7. ~~Decide whether #1705 gates or runs in parallel~~ — **SUPERSEDED, 2026-09-15/16.** #1705 itself
   closed without a redesign — see §2 item 3. Replaced by item 8 below (#1711), which is not
   currently blocking anything (deliberately sequenced after Layer 1).
8. ~~Design #1711~~ (the pre-subgroup Layer 2 stage, §1 stage 5/6) — **DONE, 2026-09-16.** All 3
   items resolved (§4A): stage `verse_meaning`, per-cluster scope, T1.1+T7.1 linkage. #1711 v11
   closed, no open decisions remaining. What's left is build work (§6 Phase C), not design.
9. ~~Confirm "dumped" means soft-delete~~ — **DONE, already answered 2026-09-09/10, missed in this
   document's first draft, corrected 2026-09-16.** See Phase B banner.
10. ~~Sign off the pack as a set~~ (item 4 above) — all 6 components are design-complete; #1691's
    own workflow loose end **closed 2026-09-16 14:15** (v19, `ready_for_approval`, matching its 3
    siblings). **Still needed: your own actual approve/reject/revise nod across the set** — closing
    the workflow loose end is not the same as you signing off the pack.
11. **New, 2026-09-16 — no action needed, listed for completeness:** #1698 (synthesis cross-cluster
    gating) and #1691 §9 item 5/#1695 (synthesis input JSON) are both correctly deferred until
    stage 9 is built and tested — not decisions outstanding right now.

**UPDATED, 2026-09-16, same-day build session — Phases A/B/D/E done, not "nothing built."**
Researcher instruction, verbatim: *"you can now systemaitcally and in stages start the build of
1706... this include the entire build from lexical layer 1 write through to the end of
ib_observations."* Built and verified live this session: Phase A (`lexical.readiness`, 0 FATAL),
Phase B (Layer 1 fully redesigned and rebuilt corpus-wide — 544,667 rows, 29,760 verses, 93s, 0
errors), Phase D/E (all 5 pack tables/columns created + registered, catalogue migrated — 92 rows).
**Still not built:** Phase C's actual execution code (the `verse_meaning` LLM-calling mechanism),
the recording pass (#1693), and Phase F (no cluster has been run through any stage). Full build
record: BUILD.md #267. Full status/issues write-up: `outputs/1706-build-session-status-v1-
20260916.md`.

---

## 8. Escalation register — every escalation feeding this design, checked not assumed

**Purpose, per researcher instruction, 2026-09-16:** *"a register on all the escalations that
impact on the final design specified in 1706... irrespective if the escalations are marked
completed or not because you have a tendency to close escalations but not check that open items
have been resolved or taken into account."* This section exists so that never happens silently
again. Every row below was re-checked against its actual live `resolution`/content this session,
not assumed clean because its `state` says `completed`. Rows outside this design's actual content
(one-off `configmaint.propose` crashes, payload-processing errors, mechanical config-registration
steps with no design content of their own) are excluded — this is a design register, not a full
audit trail.

### ★ The one real finding from this check — RECONCILED, 2026-09-16

**#1660 (closed 2026-09-10) directly bore on stage 5's design and had not been checked against
it** — flagged here, then resolved the same day. Full analysis:
`1660-1711-layer2-volume-and-filter-reconciliation-v1-20260916.md`. Researcher's own framing:
*"1660 was trying to think through the volume impact... at that stage it was not yet conceptualised
to have layer 2 answering the questions... approach with new eyes, and think through volume and
filters."*

**Resolution:** #1660 and stage 5 are not the same question — #1660 rejected *undirected,
exhaustive lexical documentation for every word* as "overwhelming... just noise"; stage 5 is a
*directed, question-answering* pass (a specific catalogue question per strong), a different task
shape by construction. But #1660's cost concern was real and had never been checked against stage
5's actual volume — now it has, live:

| Scope | Distinct strongs | Characters (~tokens ÷ 4) |
|---|---:|---:|
| Corpus-wide (all `cluster_strong`-tagged) | 15,706 | 22,498,104 (~5.6M tokens) |
| **M-code strongs only** | **3,101** | **5,151,807 (~1.3M tokens)** |

**Scoping stage 5 to M-code strongs only — a 78% volume cut — is not a new decision, it's applying
an existing precedent**: #1527 (completed 2026-09-10) already restricts `resolved_sense`
computation to M-code cluster members for the identical reason (T-code-only strongs are
grammatical/referent-identity tags, not characteristic vocabulary). Additionally, of 2,961 M-code
strongs with real lexicon coverage, 2,098 (71%) carry genuine multi-sense ambiguity — the single-
sense minority (29%) is where the LLM's answer is expected to be short and settled, a depth
calibration already validated elsewhere in this catalogue (#1700's own finding that terse,
confident answers are calibration, not genericity), not a pre-filter that excludes real vocabulary.
**Three concrete design inputs now available for #1711**: M-code-only scope (matches #1527),
question-directed task shape (already true), depth calibrated by sense-count (not gated by it).

### The register

| ID | State | What it decided/covers | Checked 2026-09-16 |
|---|---|---|---|
| #1379 | completed | Verse-lexical rework: intrinsic contextual enrichment — early scope statement for Window 1 vs Window 2 | Historical, superseded in mechanism by #1592/#1607, principle (Window 1 = verse's own data only) still governs |
| #1443 | completed | Structural-pattern finding had no checklist slot → `structural_pattern` note_type born here | Content absorbed into live `note_type` enum, no residual open item |
| #1444 | completed | Mechanical/interpretive question-code splits (a/b pattern) | **Confirmed live still relevant**: 10 of these splits are 100% unexercised (#1700) — not a defect in #1444 itself, a downstream execution gap, tracked at #1704 |
| #1446/#1447 | completed | Full verse/word analytic-methods genealogy + T1-T3 three-scheme glossary disambiguation | Read in full this session (2026-09-16) — its own open items (D2/D5/D7/D8/D4 argument-structure derivation fixes, §3.4) are HISTORICAL (superseded VE-lexical model), not live; no residual live gap found beyond what #1704 already covers |
| #1449 | completed | `verb_argument` note_type born here (trigger/impact) | Superseded in ambition by #1705's closure — the *narrow* original definition stands, the *expansion* #1705 asked for does not |
| #1451 | completed | `passage.build` no-hibs gate — Window 1/2 boundary case | No residual open item found |
| #1524 | completed | Validate catalogue questions against Window 1 evidence | Was held pending #737's direction; #737 itself remains gated/open (see below) — worth confirming this doesn't need re-opening once #737 moves |
| #1526 | on-hold | Reading strategy vs. cluster size (anchor-verse-by-`resolved_sense`) | Correctly on-hold, researcher's own instruction; evidence stays on record |
| #1589 | superseded | 6 of 15 `note_type` values undefined | **Corrected scope this session** — actually 10 of 15, not 6 (§7 item 32) — folded into #1704 |
| #1590 | superseded | Greek/Hebrew role-tag bug | Confirmed: the code path is being deleted by Layer 1's redesign, not fixed — no residual action |
| #1591 | superseded | `surface` 192-row alignment defects | Confirmed moot — old rows retired wholesale; replaced by a post-rebuild validation check (§6 item 11) |
| #1592/#1595 | re-assigned/review | `verselexical.build` revisit; `verse-lexical.note` structure | Content fully folded into §3/§6 above; escalations themselves not formally closed — workflow loose end, not a content gap |
| #1691 | `ready_for_approval`, 2026-09-16 14:15 | `ib_observation` design | **Closed out to match its 3 completed pack siblings, as recommended below** — v19, resolution "ib_observation design complete per this escalation." No longer a workflow loose end. |
| #1547 | `ready_for_approval`, 2026-09-16 14:15 | "Prototype Window 2 analysis" placeholder | **Closed as superseded, as recommended below** — v2, resolution "Superseded in practice by #1682's real cluster-reading work." |
| #1702 | `ready_for_approval`, 2026-09-16 14:15 | Cluster T-codes / answer-stage coverage | **Closed, content fully absorbed into #1704** — v2, resolution "Fully absorbed into #1704 (Phase 1b/1c's T-code sweep)." |
| #1594 | superseded | Verse-lexical enrich vs. catalogue — Window handoff gaps | Resolved (§3); `passage.genre` finding consolidated with #1607 D12/D13 and #1700's T7.2.2a/2b finding into one root cause (§7 item 33) |
| #1597 | superseded | `verse_lexical_note.evidence_text` 100% unpopulated | Resolved by architecture (`ib_node` CHECK + coverage self-check) — confirmed structurally closed, not just asserted |
| #1598 | completed | Reallocation of M/T-code clusters; retired old T3 Inner-Faculties framing | Direct ancestor of #1701's resumption scope — still governs, no drift found |
| #1606 | completed | 3-leg lexical readiness check | Leg 3's 111 strongs classified; the check itself still not registered as a persisted `cfg_method_rule` (§6 Phase A item 1) — real, tracked |
| #1607 | in-progress | Layer 1/2 six-point column validation | The live parent venue — v17, still open, correctly so. **Checked 2026-09-16 for Layer 2 content not carried into #1711**: D7 (`passage_id`) and the `resolution_status`/"unresolved, not guessed" principle both found genuinely dropped, not just unresolved — see §4A above |
| #1608 | completed | New `verse_meta` table (D13) | **Re-verified this session**: fully built, verified (29,759/29,759, 0 orphans), no residual gap. Confirms today's earlier live-DB finding independently. |
| #1613 | completed | Base-data spine ruling + meaning-representation normalisation | Spine check re-run this session (step 4A of session start) — 0 FATAL, clean |
| #1658 | raised | `cfg_table` can't register a view safely | **RESOLVED for this pipeline, 2026-09-16** — researcher, verbatim: *"I don't think the view have to be registered. if you read the meaning in the lexical analysis you will in any case read directly from the tables, rather than the view."* Stage 5's assembly script queries `strong_meaning_tree`/`strong_lexicon` (lsj/mounce) directly, not via `vw_strong_meaning_raw` — no view registration needed, the gap simply doesn't bite this build. #1658 itself stays open as a general `cfg_table` capability question, unrelated to whether this pipeline needs it. |
| #1660 | closed | Bulk lexicon-join has no value for characteristic analysis | **RECONCILED, 2026-09-16** — see flagged finding above; resolved, not a residual conflict |
| #1665 | raised | `cfg_*` coherence advisory — **exactly 2 orphaned `cfg_enum` groups, both named here per researcher instruction 2026-09-16** | **`lexical_code_class`** — genuine retirement candidate. The mechanism it named (negator/connective/party classification) was already migrated onto the `cluster_strong` T4/T5/T7/T8/T9 code system (#1499–1502, completed 2026-09-05/06); `cfg_lexical_code_class` (the table) is already marked inactive; only the **`cfg_enum` group itself** (the value-list registration) is left as pure historical residue — recommend marking `inactive=1` to match. **The connective sub-type question is separately RESOLVED, 2026-09-16** — checked live, `cluster_strong.rationale` carries the causal/coordinating/purpose (and more) sub-typing for every T6 row, per #1499's own explicit decision ("sub-type recorded in rationale instead") — see #1704 Phase 2 event 5, corrected from ❓ to 🔧. **`party_kind`** — **NOT a retirement candidate** — this enum is live and essential (`verse_lexical.party_kind`, heavily used). Its "orphan" finding is narrower and different in kind: the code derives values from `cluster_strong` lookups directly, never actually calling `cfg.enum('party_kind')` to validate against the registered list — a validation-wiring gap (or an intentionally documentation-only registration), not dead code. Worth a decision (wire real validation, or mark the registration as reference-only) but not "retire." |
| #1668/#1675-1680 | completed | Retired `strong_meaning_parsed`/`lsj`/`mounce`; revised meaning-distillation method | Direct ancestor of stage 5's `vw_strong_meaning_raw` source — the method #1660 and this retirement produced is exactly what stage 5 needs to be checked against |
| #1682 | in-progress | Cluster-reading process spec (a/b/c/d/e) | Content fully absorbed into §1/§4A; escalation itself correctly still open (synergy-stage input undefined) |
| #1683 | re-assigned | M10's 32 legacy characteristic rows vs. Window 2 | Decoupled from the build by the DB fork — real, not blocking, own timeline |
| #1690/#1692/#1693 | completed | `cluster_subgroup`, `ib_node`, the recording pass — table/procedure designs | Design-complete, content re-verified this session against live DB (none built yet) |
| #1691 | in-progress | `ib_observation` design | Design-complete per its own §9/10; escalation itself not closed — workflow loose end (§7 item 10) |
| #1694 | closed, 2026-09-16 | 37 M-codes in `cluster_strong` have no `cluster` row | **MOOT — confirmed live.** Original finding compared `cluster_strong` (iba.db) against `bible_research.db.cluster` (the legacy table). Re-checked directly against `iba.db.cluster` (the correct, authoritative table for this build): 0 orphaned M-codes. Phase D/E's FK assumption is sound. |
| #1695 | in-progress | Design: synergy stage | Correctly deferred (§1 stage 10). **New directional input, 2026-09-16**: synergy's input JSON is expected to be the accumulated flag/pointer observations from reading+answer, not a fresh pull — see checklist §0 rule 5a |
| #1696 | re-assigned | Catalogue migration | Design-complete, deliberately held pending this document, per your own instruction |
| #1697 | re-assigned | `iba.cluster.status` lifecycle | Design-complete, all 5 items resolved |
| #1698 | in-progress | Synthesis cross-cluster gap | Correctly deferred (§4) |
| #1699 | raised | IB Node Web mockup | Parked pending real data, not a design gap |
| #1700/#1702 | in-progress/raised | Answer-stage catalogue-quality review; cluster T-code coverage | Both complete as of this session, fed directly into #1704 Phase 2/3 |
| #1701 | `ready_for_approval` | Inner-faculties framing | **DONE, 2026-09-16.** Core question resolved (#1704 decision 4); catalogue question authored — `T2.11` "Faculty Engagement" — folded into #1696's migration insert |
| #1703 | in-progress | Adjacent-verse-context flag-not-fetch | Untested at scale, relevant to stage 9, not blocking. **Resolution mechanism now confirmed in direction, 2026-09-16**: a later analytic run resolves it, expected to be synergy — see checklist §0 rule 5a. Rate question still stands, untested |
| #1704 | in-progress | Analytic event inventory | Phases 1-3 complete + corrected (Group D) this session |
| #1705 | closed | `verb_argument` model expansion | Closed without building — replaced by #1711, not the same question |
| #1711 | re-assigned | Layer 2 lexical-observation process design | The live open design gate — deliberately sequenced after Layer 1; **should also resolve the #1660 reconciliation above when it's picked up** |
| #737 | re-assigned | IBA debate-pipeline migration (gated) | Adjacent, not on this pipeline's critical path — #1524 above is the one place it still has a live dependency |
| #1547 | raised | "Prototype Window 2 analysis" placeholder | Superseded in practice by #1682's real work, never formally closed — recommend closing as superseded, not an open design question |

**What this register does NOT cover:** the large run of #1454-1670-range one-off `configmaint`
crashes, payload-processing errors, and mechanical config-registration steps (grant additions,
`cfg_column.use` text fixes, retirement of already-dead tables) — these are build/operational
history with no independent design content of their own; their effects are already reflected in
the live DB state this document checks against directly, not re-litigated here.
