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
| 2 | **Layer 1 build** (`verse_lexical`) | mechanical, per-code columns: `role`, `is_negator`, `party_kind`, `surface`, etc. — no `resolved_sense`, dropped (see stage 5) | #1592/#1607, `1607-layer1-layer2-consolidated-column-spec-v1-20260910.md` | **Design closed.** Full rebuild, not incremental (researcher's own instruction, §3.3 below). |
| 3 | **cluster.status / cluster_subgroup.status readiness** | lifecycle gating columns | #1697 (cluster), #1690 §3a (subgroup) | Design closed except 5 small confirm-or-correct items (§7). |
| 4 | **Catalogue migration** | `wa_obs_question_catalogue` → `iba.db` | #1696 | Design closed, pending CSV review + pack sign-off. |
| 5 | **Layer 2 — lexical observations + lexical-question answers** | multi-source LLM reading of `vw_strong_meaning_raw` (all 3 sources), per strong — produces `ib_observation` row(s): general lexical observations AND slant-answers to the catalogue's term-scoped ("Word/term (lexical)") questions. This is where `resolved_sense`'s replacement lives — not a Layer 1 column | Researcher, verbatim, 2026-09-15 (§3 below) | **Genuinely new, undesigned.** Not in any prior spec. Needs: a stage name/value, scope grain (per-strong corpus-wide? per-cluster?), which catalogue question(s) it links to — none decided yet. |
| 6 | **Capture Layer 2 observations** | the recording pass (#1693) writes stage 5's LLM output into `ib_observation`/`ib_node` — same run-structure pattern already used for reading/answer/synthesis, made explicit here since it sits before subgroup, not after | #1693 §0 (pattern), extended | **New, explicit step** — not previously called out as its own stage; mechanism is #1693's existing same/broaden/new logic, applied to a new input. |
| 7 | **cluster-subgroup build** (process b) | consumes stage 6's captured Layer 2 observations as input; outputs: subgroups, membership, catalogue-driven `ib_observation` (`stage='subgroup'`) — its own, separate observations, not Layer 2's | #1690, #1691 §9 item 8 | Design closed except the stage-5/6 input wiring (new). |
| 8 | **reading stage** (process c) | per-subgroup LLM read; inputs = subgroup's own `ib_observation` rows + Layer 1/2 lexical for every verse in scope | #1682 process spec, #1691/#1692 (`ib_observation`/`ib_node`) | Design closed. **This is the fix for the #1607 v14 root-cause finding** (below). |
| 9 | **answer stage** (process d) | catalogue-question answering, multi-slant, per subgroup | #1682 §4A, #1691 | Design closed; needs stage 4 (catalogue in `iba.db`) landed for the real FK. |
| 10 | **synthesis/synergy stage** (process e) | cross-**cluster** (not just cross-family) comparative claims, append-only, `supersedes` chain | #1682 §4B, #1691 §9 item 9, #1695 | Design closed for the table; **gating precondition for a multi-cluster run is undesigned** (#1693 §0 open gap) — explicitly deferred by researcher until build+test through stage 9 is complete. |
| 11 | **faculty reflection** (new) | end-of-read, subgroup-level observation — "where in the being did this happen" | #1701 (resolved framing, this session) | **Framing resolved, nothing else designed.** A fresh catalogue question needs authoring. |

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

Recorded at #1704/#1705/#1701, **not yet incorporated into #1682's process spec or #1691's `tag`
design** — carried forward here as concrete build requirements on stages 7–10:

1. **The role-driven walk must be structurally forced, not advisory** (#1704 §5 decision 1). The
   reading-stage prompt/process design needs an explicit per-role checklist the LLM must work
   through and account for before synthesis — "silently ignore what it reads" is the exact failure
   mode already diagnosed once (§1 above). **Build item on stage 8's actual process design**, not
   yet written.
2. **Pointer observations are their own kind, always separate from relational** (#1704 §5 decision
   2) — out-of-scope-referencing, raw material for stage 10's synergy work. `ib_observation.tag`'s
   answer-stage taxonomy is explicitly "not concluded" (#1691 §5) — this is exactly the open slot
   this requirement fills. **Build item on #1691's still-open `tag` taxonomy.**
3. **`verb_argument` needs a real model expansion** (#1705, spun out this session) — graded
   significance (incidental → core inner-being driver) and relation to *multiple* M-codes at once,
   not a single agent/patient pair. **Undesigned. Confirmed gating, not parallel** (researcher,
   verbatim: *"cannot be postponed or parked"*) — a real precondition on stage 5/8's T3-operation
   handling, not a small fix folded into the Layer 1 column spec. Full context:
   `1705-verb-argument-what-exists-reference-v1-20260915.md`.
4. **Faculty is an end-of-read, subgroup-level reflection, not a per-strong tag** (#1701, resolved
   this session) — dissolves the old "conceptually wrong" Inner-Faculties objection. **A fresh
   catalogue question still needs authoring** — not drafted.

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
| `verb_argument` (D9) | See #1705 — spun out as its own model-expansion project, not a Layer 1/2 field decision. |

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
finalized mean" section (all dated 2026-09-14) tells a different, more current story:

| Escalation | Component | Its own latest verdict |
|---|---|---|
| #1690 | `cluster_subgroup`/`cluster_subgroup_strong` | ✅ **Design-complete**, approved 2026-09-13 |
| #1691 | `ib_observation` | ✅ **Design-complete** — "every §4 item now closed" except the synergy-stage input (§10, explicitly *not* a blocker) |
| #1692 | `ib_node` | ✅ **Design-complete** — "RESOLVED... every §4 item now closed... ready to register" |
| #1693 | the recording pass | ✅ **Design-complete** pending confirming its own proposed name ("the recording pass") — one word-choice, not a design gap |
| #1696 | catalogue migration | ✅ **Design-complete** — pending the researcher's CSV review (`1696-catalogue-migration-candidate-rows-v1-20260914.csv`) |
| #1697 | `iba.cluster.status` | ✅ **Design-complete, 2026-09-15** — all 5 items below resolved this session |

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
what's left is the researcher's actual sign-off nod across all six, and the build itself (§6).

---

## 5. This session's un-folded additions — real, but not yet spec-level

Unlike §3/§4 (existing designs this proposal grounds and sequences), these three are **new
requirements that don't yet have a spec to point to** — listed so they aren't lost, not so they
block the build below:

- **#1704** (role-driven-reading-sequence) — the forced-walk requirement (§2 item 1) needs to be
  written into #1682's process spec for stage 8; not done.
- **#1705** (`verb_argument` model expansion) — genuinely undesigned; significance grading +
  multi-M-code relation + referent-identity arguments. This is large enough that it should probably
  run as its own design escalation on its own timeline, in parallel with the build below, rather
  than gating it — **flagged for the researcher's call, not assumed**.
- **#1701** (faculty reflection) — framing resolved, catalogue question not authored, no schema
  impact identified yet beyond "an `ib_observation` row at the end of a subgroup's read."

---

## 6. The build action list

**Ordered by actual dependency, not by escalation number.** Each item names what it produces and
which escalation/spec it draws its design from. Nothing here executes without the researcher's
go-ahead — this is the proposal, not the build log.

### Phase A — base-data readiness (must run before Layer 1 rebuild)

1. Register lexical readiness (#1606) as a real, persisted `cfg_method_rule` check — three legs,
   per the researcher's own original wording, not just a description.
2. Researcher's call: run the T-code classification pass on Leg 3's 111 zero-allocation strongs
   (same by-hand method as T4/T5/T6/T7/T9/T15), or accept them as a known, tracked gap for now.

### Phase B — Layer 1 cutover + rebuild (`verse_lexical`)

**Researcher instruction, verbatim, 2026-09-15:** *"the current lexical records will all be dumped.
layer 1 has materially changed and the table schema changed. your proposal must include the steps
to desolve the old lexical configuration, and set the new configuration. layer 1 will be processed
in bulk to produce fresh results for the entire corpus. I am no longer interested to try and
reconcile old data, and the discrepancies in the old data is not going to be 'fixed'."* Confirms:
full corpus-wide bulk rebuild, no incremental/per-word processing; no effort spent reconciling or
repairing old data (the fresh rebuild **is** the fix); and — new requirement — the old Layer 1
*configuration* (not just the data) must be explicitly retired as its own step, not left to drift
alongside the new one. "Dumped" read as soft-delete (`deleted=1`), matching the project's standing
no-physical-delete convention (CLAUDE.md §3) and the already-confirmed "soft delete all current
lexicals before first actual run starts" instruction — flagged for confirmation if a literal hard
delete was actually meant.

3. Design the `role` pre-validator (empty-set-is-error gate) — not yet specified (#1607 §3).
4. Decide the `role` JSON's exact internal shape — bare array vs. array of objects (#1607 §3).
5. **Dissolve the old Layer 1 configuration** (new, explicit step, not previously listed): retire
   the `cfg_column` rows for the dropped columns (`ambiguity_note`, `language`) and any
   `cfg_method_rule` rows tied to the old `role`/`resolved_sense` mechanism (superseded, not
   deleted, matching the project's own governance convention); update `cfg_step.does` for whatever
   step builds `verse_lexical` to describe the new shape, not the old one.
6. **Set the new Layer 1 configuration**: register the redesigned `role` column's shape in
   `cfg_column`, the new `verse_meta` table (item 9) in `cfg_table`/`cfg_column`, and the bulk
   full-corpus rebuild routine itself in `cfg_utility`/`cfg_step`/`cfg_write_grant` if it doesn't
   already have a registered home.
7. Soft-delete every current `verse_lexical` row — the full-rebuild precondition.
8. Run the rebuild, corpus-wide, in bulk: drop `ambiguity_note` and `language` (re-pointing
   `_narrative_morph_for` to `verse_meta.language` in the same unit of work); populate the
   redesigned `role`; **drop `resolved_sense` from Layer 1 entirely** (see item 10 — the real
   synthesis work moves to a new Layer 2 stage, not a Layer 1 column).
9. Create the new verse-level `verse_meta` table (D13) — `language`, and whatever else is needed at
   that grain.
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
11. Post-build: run the surface-alignment validation heuristics against the fresh rows (replaces
    #1591's old-row repair, now moot — §3) — note: consistent with "not reconciling old data" above,
    since this validates the *new* rebuild's own output, not old rows.
12. Close #1590 (superseded) and #1597 (resolved by architecture) once confirmed by the researcher.

### Phase C — Layer 2: lexical observations + capture (genuinely undesigned — §1 stages 5–6)

Not a small addition to Phase B — two new steps in the pipeline (produce, then capture), needing
their own design pass before they can be built. Open, not decided here:
13. **Stage name/value.** `ib_observation.stage` currently has `subgroup`/`reading`/`answer`/
    `synthesis` — Layer 2 runs *before* `subgroup`, so it needs its own new value (candidate:
    `meaning` or `lexical`, not chosen here).
14. **Scope grain.** Per strong, corpus-wide in one pass? Per cluster (so it can run alongside/just
    ahead of that cluster's own process (b))? Not stated by the researcher's instruction, which
    describes the mechanism but not the batching.
15. **Which catalogue question(s) it links to.** "Linked to a question" — the lexical/term-scoped
    catalogue components (T1.1 Name/Naming, T7.1 Lexical/Semantic Analysis, etc. — the ones
    #1682 §4A's own `Word/term (lexical)` scope category already names) are the natural candidates,
    not confirmed. Determines what `question_code` actually gets populated with.
16. **RESOLVED, researcher, verbatim, 2026-09-15 — capture is its own explicit step, not folded
    into Layer 2's own LLM pass.** *"layer 1 -> layer 2 (produce lexical observations and answers
    to lexical questions) -> capture lexical observations -> subgroup"* — four steps, not three.
    Mechanism confirmed as the recording pass (#1693), same run-structure pattern as every other
    stage (§1 stage 6) — not a new mechanism, but its own visible pipeline step, not silently
    absorbed into Layer 2's own description the way earlier drafts of this doc had it.

### Phase D — cluster/subgroup readiness gates

17. Add `iba.cluster.status` (#1697) — **design fully resolved** (§4), `ALTER TABLE` + register the
    `cfg_enum`.
18. Add `cluster_subgroup.status` (#1690 §3a) as part of creating that table (Phase E).
19. Migrate `wa_obs_question_catalogue` into `iba.db` (#1696) — bulk-insert the 98 live rows, retarget
    every live routine in #1696 §2, flip `bible_research.db`'s copy `inactive=1`, restore the real FK
    on `ib_observation.question_code` (also needed for Phase C's `question_code` linkage above).

### Phase E — cluster-reading pipeline tables

20. Create `cluster_subgroup`/`cluster_subgroup_strong` in `iba.db` (#1690 §1 DDL), registered in
    `cfg_table`/`cfg_column`.
21. Create `ib_observation` in `iba.db` (#1691 §1 DDL), registered — extended for Phase C's new
    `stage` value once item 13 is settled.
22. Create `ib_node` in `iba.db` (#1692 §1 DDL), registered.
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

### Phase G — carried-forward, does NOT include #1705

**RESOLVED, researcher, verbatim, 2026-09-15:** *"verb_argument is fundamentally part of the
current pipeline and work, and cannot be postponed or parked."* **#1705 gates — moved out of this
phase.** It's a real precondition on Phase F's T3-operation handling (stage 8/reading, and likely
Phase C/stage 5's Layer 2 lexical-question-answering too, since T3 operation verbs are exactly what
`verb_argument` is meant to surface) — genuinely undesigned (reference doc:
`1705-verb-argument-what-exists-reference-v1-20260915.md`), not scheduled as its own build-list item
yet because the design itself doesn't exist. Design it, then it becomes a real, numbered
precondition on Phase F, not an item in this carried-forward phase.

30. #1701 (faculty reflection) — author the new catalogue question; no schema work identified yet.
32. #1589's remaining 6 undefined `note_type` values — folds into #1704 Phase 3 (corrective actions)
    once that phase runs.
33. #1594's `passage.genre`/`passage.lexical_complete_at` orphaned-column finding — real, unclosed,
    carried forward as its own small fix, independent of the phases above.

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
7. ~~Decide whether #1705 gates or runs in parallel~~ — **DONE, 2026-09-15.** Gates, confirmed.
   Reference doc filed (`1705-verb-argument-what-exists-reference-v1-20260915.md`); the actual
   redesign (significance grading, multi-M-code relation, referent-identity widening) is still
   undesigned and is the real remaining work, not the gating question.
8. **New, 2026-09-15 — design the pre-subgroup meaning-synthesis stage** (§1 stage 5, Phase C):
   name its `ib_observation.stage` value, decide its scope grain (per-strong corpus-wide vs.
   per-cluster), confirm which catalogue question(s) it links to, and confirm the recording pass
   (#1693) is the right write path for it.
9. Confirm "dumped" (Phase B banner) means soft-delete (`deleted=1`), matching the project's
   standing convention and the already-confirmed rebuild instruction — not a literal hard delete.

Nothing in this document is built. It is the single point of reference this session's request asked
for — ground the whole lexical-stack thread in what's decided, what's new, and what order it goes in.
