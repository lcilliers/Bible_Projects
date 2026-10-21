# Verse-lexical enrichment — Window 1 checklist (v1, prototype)

**Filename:** 1379-verse-lexical-enrichment-checklist-v1-20260902.md
**Escalation:** #1379
**Status:** PROTOTYPE — being test-driven against Ps 25:2 and Hos 2:4
(`Workflow/Catalogue/1379-verse-lexical-enrichment-applied-ps25-2-hos2-4-v1-20260902.md`) before any
schema/code work starts. Expect this list to grow or be corrected as more verses are run through
it — not treated as closed.

**Naming note:** deliberately does NOT reuse `T1`-`T9` (already means something else in the
glossary — M-code cluster/tier labels, see `1379-verse-lexical-enrichment-scope-v1-20260902.md` §7) or
`Step 1`/`Step 3`/`Step 4-5` (already means the `operations-ingest` pipeline's own stages). Items
below are named descriptively, not numbered against either existing scheme.

## Scope — Window 1 only

This is **Window 1**: understanding the words in a single verse, everything derivable from its own
span/morph/lexicon data — full stop. It is NOT Window 2 (identifying HIBs, phenomena, operations —
`operations-ingest`'s job, which also reads adjacent verses). The one and only bridge between them:
where this checklist finds something it cannot resolve from the verse's own data, it records that
explicitly as **unresolved**, never guesses, and never reaches into another verse to settle it
itself.

**Standing discipline (from T1, still binding — the exact drift this checklist exists to prevent):**
work from the row, not the gloss; the English translation orients, it is not the evidence. Every
item below is answered from `strong`/`morph_code`/`span`/lexicon fields, never from reading the
English verse text and reasoning about what it "seems to mean."

## Process gate — before anything else

**Determine genre, language, and testament for the verse first; branch by genre.** Which items
below even apply differs by genre (confirmed live in the Ps 25:2 test — see the applied doc). This
is a hard prerequisite, not one more field alongside the others. **Genre currently has no DB source
in `iba.db`** (flagged CRITICAL in the scope doc) — for this prototype, genre is determined and
recorded manually per verse, not derived from any existing column; that does not resolve the
general sourcing question, it only unblocks testing.

## Baseline (already live — T1-T3, unchanged)

Per code, per span: `role` (content/function), morph-narrowed `resolved_sense`, `status`,
`ambiguity_note` (same-base sibling ambiguity). Not re-litigated here.

## New fields — cheap, mechanical, no judgement

- **position** — `span.position`, denormalized onto `verse_lexical` (currently only reconstructable
  via a join to `span`).
- **surface** — `span.surface`, denormalized the same way.
- **language** — `strong.language` (Hebrew/Greek/Aramaic), denormalized.
- **testament** — derived from `book` (fixed OT/NT split), denormalized.
- **genre** — per the gate above; CRITICAL, sourcing still open.

## Idiom / combined-span test

Is this span part of a multi-code compound whose surface gloss diverges from a literal
code-by-code reading? If so, which sense does the combination select, and on what evidence
(the combined-span grouping itself, cross-checked against the translators' own collapse into one
English surface word)? This is the single test that did the most work in the Dan 1:8 dissection
(found "heart" hiding inside "resolved") — first-class, not folded into the noun test below.

## Purposeful classification, by part of speech

- **Pronoun — who is it pointing to.** Attempt same-verse antecedent resolution only (does another
  word in *this verse's own data* agree in person/number/gender). If resolved, record it. **If not
  resolvable from this verse alone, record `unresolved` explicitly — never guess, never reach into
  adjacent verses to settle it.** (Genuine cross-verse cruxes are Window 2's job —
  `hib.set`/`hib_referent_option` already exists for that.)
- **Noun — what is it enhancing, what is it doing.** Is it bound (construct state) to another word,
  and what does that binding contribute? Two sub-cases, kept distinct (per the Dan 1:8 "stakes/
  scaffolding" correction):
  - **Relational/addressee marking** — does this noun name another party engaged in the verse's
    action (a target, source, or addressee, distinct from the primary actor)? Same-verse-resolve-
    or-mark-unresolved, same rule as the pronoun test.
  - **Severity/quality modifier** — does it sharpen the weight of an object or action without
    naming a party (e.g. "choice" delicacies, "children of whoredom")?
- **Verb — triggered by what, impacts what.** Triggered-by = the chain/sequencing test below.
  Impacts = the governed clause/object (what the verb's content actually is).

## Finding connections

- **Narrative chain/sequencing** — does the row's morphology carry a narrative-sequencing marker
  (Hebrew: waw-consecutive/wayyiqtol) linking it to another operation as "and then"? **Confirmed
  Hebrew-narrative-specific** — the Ps 25:2 test (poetic, no wayyiqtol forms present at all) shows
  this test simply does not fire outside narrative prose; this is itself the genre-gate mattering in
  practice, not a hypothetical. No Greek equivalent built yet (open).
- **Logical/causal connective** — NOT yet in the design before this test run; surfaced by Hos 2:4's
  own data (`H3588A`, "because," `HTc`). Distinct from narrative sequencing: this links two clauses
  by *reason*, not by *narrated order*. Candidate new item — see the applied doc for the concrete
  instance and whether it should be folded in permanently.

## Enhancing meaning — related words

Pull `strong_related` links for content-role codes, as data — mechanical, safe (this is STEP's own
curation). **Do not** auto-sort each link into same-concept/genuine-relative/coincidental — the one
mechanical rule tried for this (`lemma_key` match) failed its own control case in the Dan 1:8 pass.
Record the raw links; leave the sorting as a flagged judgement field, not an automated classifier,
unless a better rule is found.

## Polarity

Is this row a negation or modifier attached to a declared or structural operation? Its own
structured field — invisible to every vocabulary/gloss-based test by design (negation carries no
semantic content of its own), decisive for what kind of act is being recorded (refusal vs.
pursuit, granted vs. withheld). Confirmed to recur in both test verses (Ps 25:2 has two distinct
negation particles, `H0408` and would-be `H3808`; Hos 2:4 has `H3808`) — worth checking in the
applied doc whether the two Hebrew negators (`H0408` vs `H3808`) carry a functional difference
worth its own note.

## Entity-linking / subject-of-record

Confirms *whose* action/state this is — ties an operative verb or noun back to its named subject
(a possessive suffix, a proper name, a matching person/number on the verb itself). Same-verse-
resolve-or-mark-unresolved, same discipline as the pronoun test — this is really the same
mechanism applied to non-pronoun anchoring.

## Data-quality check — same code, different gloss

Re-scan the verse's own rows: does the same (Strong's, morph) pair carry two different English
surface glosses within this verse? (Caught `H0834A` in Dan 1:8.) Purely mechanical, verse-local.
Record as a **typed data-quality flag**, kept separate from any discovery-type flag — different
downstream owners (this is DB-integrity territory, not analytical).

## Inert / pure-grammar confirmation

For articles, conjunctions, bare prepositions, and any row that contributes nothing beyond
grammar: record "checked, contributes nothing" explicitly. Not a gap — a positive, deliberate
result, so a later reader can tell "not analysed" from "analysed and found empty."

## Correction (2026-09-02, same day) — one integrated read, not two layers

An earlier draft of this design (chat discussion, not previously written into this file) proposed
running verse-lexical in two separate passes — a light mechanical signal-pass to help find a
passage's boundary, then a full enrichment pass once the passage existed. **Researcher correction:
there is no such split.** There is **one integrated technical read** per verse/passage block —
genre/language determination is that read's own first move, not a separate prior pass. Still
strictly Window 1 (no HIB, no inner-being identification — pure contextual/lexical analysis).

**Boundaries are self-determining, sequentially, not pre-planned.** Dividing the whole Bible into
reading blocks upfront was considered and rejected as premature/likely infeasible at this project's
scale (consistent with the researcher's own v1 comment on this escalation: *"I don't have enough
years in my lifetime to finish the work... take it one by one"*). Instead: each read determines its
own extent as part of doing the read, and that determination hands off the starting point for the
next read — a sequential sweep through the text, not a batch pre-segmentation.

**Hard verse-count ceiling, decided:** **20 verses maximum per passage/reading-block.** If a block
would exceed that, it must be split. This is a genuinely new constraint, not something already
enforced: `passage.build`'s existing `scope-too-complex` refusal (`cfg_method_rule`
`feasibility-self-assessment`) is real and live, but it is a **qualitative self-assessment**
(`feasible`/`feasibility_note` supplied by whoever submits the payload) — checked directly against
`passage.py` and `cfg_setting`, no numeric ceiling exists anywhere in the current code or config.
The 20-verse hard bound is a new, explicit rule to build, not a rediscovery of an existing one.

## Passage-coverage build (proposed, not yet applied — no Developer Mode marker active this session)

Grounded in live FK/coverage investigation (escalation #1379 v6): `verse_lexical` currently FKs
only to `verse`+`span`, no `passage_id` anywhere — `phenomenon` (Window 2, already live) already
carries both `verse_id` and `passage_id` denormalized, an existing in-schema precedent this table
never got. T1-3 baseline already covers 99.98% of verses; passage registration is the real
bottleneck (2.6% of verses, 42 passages, 100% manual today). Proposed, for the Developer Mode
session:

1. Denormalize `passage_id` onto `verse_lexical`, matching `phenomenon`'s pattern.
2. A passage-scoped build — one integrated read across every verse in a passage via
   `verse_passage`, respecting the 20-verse hard bound.
3. A `passage.lexical_complete_at`-style completion marker, same shape as
   `passage.phenomena_complete_at`, so whole-passage coverage is checkable, not assumed.
4. A genre/chain-signal-based passage-boundary suggester — proposes a candidate block (respecting
   the 20-verse cap), researcher confirms/adjusts, `passage.build` registers it unchanged. Needed
   to move registration past today's 42 hand-built passages.

## Open items this checklist does not resolve

- Genre sourcing (CRITICAL, blocks the gate).
- Whether the logical/causal-connective item (surfaced by Hos 2:4) is a permanent addition.
- The `H0853`/direct-object-marker role-classification question (surfaced by Hos 2:4) — see the
  applied doc.
- Greek equivalents for the chain/sequencing test and the role-classification (H9xxx) heuristic —
  not tested here, both test verses are Hebrew/OT. Known NT coverage problem flagged separately
  by the researcher (2026-09-02), explicitly parked until this task completes.
