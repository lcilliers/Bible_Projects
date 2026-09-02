# Verse-lexical enrichment — scope reconciliation and open decisions (v1)

**Filename:** verse-lexical-enrichment-scope-v1-20260902.md
**Escalation:** #1379 (Verse_lexical rework: intrinsic contextual enrichment)
**Purpose:** Before writing any code, reconcile what #1379 is actually asking against what already
exists — a live mechanized layer, a drafted-but-unbuilt design, and a separate downstream table —
and lay out the decisions that have to be made before a build can start. Nothing here is decided;
it is the ground to react to, per the standing "investigate, present facts, ask a real question"
protocol (`docs/interaction-preferences.md`).

## 1. What #1379 actually asks

Escalation #1379 grew directly out of the Dan 1:8 worked example
(`Workflow/Catalogue/lexical-to-finding-worked-example-v1-20260901.md`, escalation #1378). Its own
v1 comment states the researcher's direction verbatim: *"verse-lexical must work harder to put the
context of the word... understanding the word in relation to its usage and articulating it for
digestion when human being analysis use the lexical."* Its v2 addendum names a concrete extension:
tag each word for its HIB value at the point of the read — *"primary characteristic, chain
characteristic, actor... other party... etc."*

The worked example, done entirely by hand against one real verse (Dan 1:8), independently arrived
at a rich set of specific gaps in the current `verse_lexical` data — summarised in §3 below.

## 2. What's actually live right now

`iba.db`'s `verse` → `span` → `verse_lexical` chain, built by `lib/lexical.py`
(`lexical.build_for_range` / `build_for_verse`), registered as work package `verse-lexical`,
step `lexical.build`. This is a **mechanical, never-interpreted** engine — by explicit design,
per its own docstring — that for every Strong's code in a span:

- classifies `role` (`content` vs `function` — real lexical item vs. bound grammatical formative);
- selects the **stem/voice-narrowed sense** from `strong_meaning_parsed` via `morph_code` (not the
  whole gloss stack, not a guess — the specific branch the morphology names);
- flags (never resolves) the sibling/base-fallback ambiguity case into `ambiguity_note`.

`verse_lexical` columns, live: `id, span_id, verse_id, code_ordinal, strong, morph_code, role,
status, resolved_sense, ambiguity_note, created_at, deleted`. That's it — no genre, no language,
no relational/chain/polarity field, no per-verse theme, nothing beyond one resolved sense per code.

This is explicitly called **T1–T3** of a nine-step technique (see §3) — the module docstring says
outright it "runs independent of T4-T9."

## 3. What's designed but never built — the canonical technique doc already specifies most of this

`iba/docs/WA-verse-reading-technique-v4-2026-08-05.md` is the **live canonical instruction** for
verse reading (draft status, researcher-authored 2026-08-05, not superseded by anything newer).
It already lays out T1–T9, in two phases:

- **T1–T3 (lexical meaning)** — read from the row not the gloss; pull the full lexical range before
  assigning a sense; let morph decide voice/person/aspect. **This is exactly what `lexical.build`
  mechanizes today.**
- **T4–T5 (still lexical-layer, not yet mechanized)** — T4: enumerate every grammatically live
  referent reading for an ambiguous pronoun/party, adopt one explicitly, keep the rest on record.
  T5: record genre-conventional elements of the verse/passage as an observation, including elements
  *expected but textually absent*.
- **T6–T9 (inner-being relevance — preliminary stamps, not full analysis)** — T6: stamp every word
  that explicitly points to a human being as `IB`. T7: stamp the noun causing the action as `Agent`
  (an `IB` can be an `Agent` for another `IB`). T8: stamp every word relating to any `IB` in the
  verse as `Process` (includes state/condition/faculty words tied to an IB). T9: stamp every action
  word (verb) as `Action`. A word can carry multiple stamps; stamps are indicative/preliminary, not
  a movement/relationship analysis (that's explicitly a later step, out of scope for T6-T9 itself).

**None of T4–T9 has ever been written to the database.** The doc's own sample JSON output block
says so directly: `"status": "test-draft, not written to DB (destination tables not yet defined
per researcher Q7)"`. This is not a gap #1379 discovered — it's a gap the technique doc already
named and left open.

## 4. The separate downstream layer — `phenomenon`

`iba.db` has a `phenomenon` table (`passage_id, verse_id, hib_id, description, textual_warrant,
status, ordinal`) — free-text discovery notes, tied to a specific HIB (per
`feedback_iba_phenomenon_set_hib_first_lexical_verified`: *"phenomenon.set worked HIB-by-HIB,
every call checked against the lexical row; process still settling"*). It has **no
`cfg_work_package`/registered utility** — it isn't a mechanized step, it's a manually-driven
capture mechanism. This is closer to what the worked example calls "Phase 2" (discovery, requiring
judgment) than to T4-T9's "preliminary stamp" layer, and it does not carry the structured,
per-span fields (relational target, chain link, polarity, declared-vs-structural) the worked
example produced — it's prose per HIB, not structured per-code data.

## 5. Reconciling the worked example against the T4–T9 spec

The Dan 1:8 dissection was done from scratch, without reference to the v4 technique doc's T4-T9
stamps (the document doesn't cite it). Read side by side, they overlap substantially but are not
identical:

| Worked-example finding | Maps to v4's T4-T9? |
|---|---|
| Combined-span idiom test (heart hiding inside "resolved") | Not named in T1-T5 explicitly, but it's the kind of thing T2 ("pull the full lexical range") gestures at — arguably a T1-T3 refinement, not a T4-T9 concern |
| Outward-enactment test (`asked` — inner act producing outward behaviour) | Overlaps T9 (`Action` stamp) but the worked example's point is sharper: it's specifically an act *of the same IB*, continuing the same finding — T9 alone doesn't capture "continuation of the same act," just "this is a verb" |
| Relational test (`king`, `chief of the eunuchs` as the other party) | Directly = T7 (`Agent`) and the "other party" the researcher named in #1379 v2 — but T7 as written is about *causing* action; the worked example's "relational target" is the *addressee*, a different role T7 doesn't obviously cover as worded |
| Polarity test (`not` as its own structured field) | **Not named anywhere in T1-T9.** A genuine gap in the existing spec, not just an unbuilt part of it |
| Sequencing/chain test (waw-consecutive → resolve→ask chain) | **Not named anywhere in T1-T9.** Also a genuine gap — T4-T9 has no "operation chain" concept at all |
| Declared-vs-structural distinction (Phase 1 must preserve, not demote, undeclared-but-expected content) | This is closer to a **principle governing how T4-T9 stamps get recorded** than a new stamp itself — but the current T6-T9 wording ("indicative... preliminary... not conclusive") doesn't obviously protect against the demotion failure mode the researcher corrected twice in the worked example |
| Genre as verse-level field | = T5 ("genre-conventional elements... may be elements expected but textually absent") — T5 is about *applying* genre-awareness, but doesn't itself specify *where the genre tag comes from*. `bible_research.db.verse.genre` exists but is book-level, confirmed too coarse on Dan 1:8's own tag, and was never ported to `iba.db` |
| Language/testament as explicit field | Not named in T1-T9 at all — `strong.language` exists but is one join away from `verse_lexical`, never denormalized onto it |
| Related-word enrichment (`strong_related` + `lemma_key`, sorted same-concept/genuine-relative/coincidental) | Not named in T1-T9 at all. Also the one area where the worked example's own mechanical test (`lemma_key` match = related) **failed its own control case** and had to be retracted — flagged there as real analytical work, not a safe mechanical rule |
| Primary-operation/theme field (which term is the verse's entry point) | Not named in T1-T9 at all — a genuinely new field the worked example proposes |

**Bottom line:** #1379 is not asking for something adjacent to the existing design — it is asking to
finish and, on above evidence, meaningfully extend a spec (T4-T9) that was drafted a month ago and
never implemented, using a real worked case that surfaced gaps the original spec didn't anticipate
(polarity, chain, related-word enrichment, an explicit primary-operation field). Building only what
T4-T9 already says, or building only what the worked example found, would each miss things the other
one caught.

## 6. Open decisions — before any build starts

These are genuine judgement calls, not something to default on:

**A. Scope of the merge.** Update `WA-verse-reading-technique-v4` in place to fold in the worked
example's additions (polarity, chain, related-word discipline, primary-operation field, the
declared/structural distinction) before building anything — one reconciled spec, not two competing
ones? Or build straight from the worked example and treat v4's T4-T9 as superseded?

**B. Where the enrichment lives.** New columns directly on `verse_lexical` (per-code, matching its
current grain), or a new linked table (since several roles — relational target, chain link,
theme/primary-operation — are naturally per-*span* or per-*verse*, not per-code)? `verse_lexical`'s
whole current design is one row per code; several of the worked example's fields don't fit that
grain cleanly.

**C. Automation vs. manual capture.** `lexical.build` (T1-T3) is fully mechanical — no interpretive
judgement, run at scale across a book/chapter range. T6-T9 stamps and the worked example's richer
taxonomy involve real judgement calls (the "asked" miss, the two "stakes/scaffolding" corrections,
the retracted `lemma_key` test) that took *the researcher's own correction, twice*, to get right
even on one verse. This is the single biggest open question: is the ask to (i) build T4-T9 as a
**mechanized step** in `lexical.build`, run automatically at scale the way T1-T3 is; or (ii) build
the **schema/capture structure** for these fields, populated **one verse at a time**, by hand or in
a chat-driven pass (the way `phenomenon` already works), leaving the judgement to a human/live pass
rather than an algorithm? The researcher's own closing reflection in #1379 v1 — *"this type of
analysis is not going to come out of a repetitive cookie-cutter process... take it one by one"* —
points toward (ii), but that's inference from one remark, not a stated decision; worth confirming
directly, because it changes the entire build.

**D. Genre.** Port `bible_research.db.verse.genre` into `iba.db` as-is (known, on this verse's own
test, to be book-level and too coarse), re-derive at verse grain from scratch, or leave genre out of
this round and flag it as its own follow-on item?

**E. Language/testament.** Denormalize `strong.language` onto `verse_lexical` directly (one column,
trivial to backfill, removes the implicit join) — any reason not to just do this regardless of how
A-D land, since it's cheap and uncontroversial?

**F. Related-word enrichment.** Given the worked example's own `lemma_key` test failed its control
case, this doesn't look like a safe mechanical rule yet. Hold it out of any automated build and
leave it as a manual/Phase-2 pull for now, or attempt a corrected mechanical version anyway?

**G. Hebrew/Greek asymmetry on the chain test.** The waw-consecutive sequencing test is confirmed
Hebrew-specific and has no built Greek equivalent. Build Hebrew-only now and flag Greek verses as
"chain test not yet supported for this language," or hold the whole chain field until both are
ready?

## 7. Correction (2026-09-02, same day) — T4 and T6-T9's ground is more built than §3 claimed

§3 above said flatly that "none of T4-9 has ever been written to the database." That was based on
an incomplete search — checking `cfg_work_package` by name (`lexical`/`verse`) and the `phenomenon`
table in isolation, not a full read of `cfg_method_rule`. A full read of `cfg_method_rule` (35
rows, all steps) corrects the picture:

- **T4 is explicitly, literally folded into a live config rule.** `cfg_method_rule` step=`hib.set`,
  `rule_key=referent-crux-resolution`, `source_doc='debate-analytic-process-digest-20260805.md
  Step 1 (T4 folded in)'`, `enforced_by='schema: hib_referent_option'`. The `hib_referent_option`
  table (`hib_id, reading_text, textual_grounds, adopted, ordinal`) is a real, structured
  implementation of T4's own four sub-steps (enumerate live readings, textual grounds per reading,
  adopt one explicitly, keep rejected alternatives on record) — not a stub, not a draft.
- **A whole registered, gated pipeline already covers ground close to T6-T9**, under its own
  vocabulary, not the v4 doc's stamp names — work package `operations-ingest`
  (`iba/app/ps/Operations-Ingest.ps1`), live (`inactive=0`), three steps:
  - `hib.set` — the HIB register itself (`hib`, `verse_hib`) — the human-inner-being identification
    T6 names, plus typing (`hib.kind` — named/unnamed × individual/collection, six-type scheme).
  - `phenomenon.set` — phenomena register, phase-gated on `hib.set` completing for the whole
    passage first (`passage.phenomena_complete_at`), one row per HIB×verse (`phenomenon` table,
    already inspected in §4), with a real control-total check (every HIB×verse pair must produce a
    register entry, including explicit "silent" ones).
  - `operation.set` — `operation` (`process`, `action_type`, `decision`, `observation_text`) +
    `operation_party` (`role`, `kind`, `hib_id`, `enablement_only`) — this is where T7 (Agent), T8
    (Process), and T9 (Action) actually land: `operation.process` ≈ T8, `operation.action_type` ≈
    T9, `operation_party` (with `role`/`kind`/`hib_id`) ≈ T7's Agent/other-party structure, done
    with considerably more structure than a flat stamp (a `four-parts` rule requires every
    operation to carry process + source + target + action-type; `hib-can-be-party-in-another-hibs-
    operation` explicitly handles one HIB acting on another).
  - A fourth step, `closing.set` (work package not yet located in this pass — flagged, not
    chased down further here), adds linkages (`passage_linkage`), an insufficiencies register
    (`passage_insufficiency`), and an emergent-questions log (`passage_emergent_question`).

  Full text search for literal `T1`-`T9` tokens across every `cfg_method_rule` row found exactly
  two hits: `T4` (above) and `T2` (a `phenomenon.set` rule citing T2's "pull the full lexical
  range" discipline). **No rule anywhere cites T5, T6, T7, T8, or T9 by name.** So this pipeline is
  not a labelled implementation of v4's T6-T9 — it was built independently (dated rules span
  2026-08-02 through 2026-08-07, alongside and partly overlapping v4's own 2026-08-05 date), using
  its own terms (HIB/phenomenon/operation/party), and it covers closely related ground without
  ever being reconciled against the v4 doc's T6-T9 wording.

**What this changes about §6's open decisions:** Decision A (does T4-T9 need building fresh, or
folded/reconciled against something that already exists) has a real answer now for T4 and
substantially-overlapping ground for T6-T9 — **not** "build from nothing," but "reconcile the v4
technique doc's T4-T9 language against the already-live `operations-ingest` pipeline's own
vocabulary and schema, and decide whether they're the same mechanism under two names or genuinely
different work." That reconciliation hasn't been done — this correction surfaces that it's needed,
it doesn't do it.

**Genre (T5) — status confirmed, marked CRITICAL, must resolve before build.** Genre has **no**
config-anchored home anywhere in this pipeline either. Worse than absent: the one directly-adjacent
rule, `phenomenon.set`/`not-literary-pattern`, explicitly routes genre-like observations *away*
from structured capture — *"A genuine literary/structural/genre observation is not a phenomenon —
log it once as an emergent question... never built into the phenomena register."* So the existing
live pipeline's own design decision was to treat genre as unstructured free text, not a queryable
field — the opposite of what T5 and the worked example both call for. Per researcher instruction
(2026-09-02, this chat): **genre is critical and must be marked up for resolution before any
T4-T9-adjacent build proceeds** — not deferred as one open item among several. This needs its own
resolution: (a) where does a per-verse genre tag come from (`iba.db` has none at all today); (b)
what's it checked against (no genre-convention catalogue exists in either DB); (c) does resolving
it change the `not-literary-pattern` rule's own routing decision in the live pipeline.

## 8. What this document is not

Not a design proposal, not a schema, not code. It's the reconciliation needed so the next document
— an actual design — starts from one merged picture instead of two independently-produced ones.
