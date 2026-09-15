# `verb_argument` — what already exists in the system

**Escalation:** #1705 · **Purpose:** a single reference pulling together everything currently live,
decided, or found about `verb_argument` across #1449/#1606/#1607/#1704/#1705, so the redesign has a
grounded starting point instead of scattered escalation history. **Nothing new decided here** —
this is a consolidation, not a proposal.

**Researcher, verbatim, this chat turn:** *"verb_argument is fundamentally part of the current
pipeline and work, and cannot be postponed or parked."* Recorded as settled — this closes #1706 §7
item 7 (whether #1705 gates Phase F or runs in parallel): **it gates.**

---

## 1. Origin — why it exists at all

Raised as escalation **#1449** (*"No note_type for verb triggered-by/impacts"*), closed
2026-09-05. The gap it named: none of the existing `note_type` values could record **which code
triggers a given verb and which it impacts** as its own first-class fact —
`chain` is sequence/waw-consecutive only, `entity_link` is party/pronoun identity only, `connective`
is clause-linking only. `verb_argument` was designed to fill exactly that hole: a verb code's own
**trigger** (grammatical subject/agent) and **impact** (object/patient span(s)).

## 1a. Why T3 exists at all — the methodological history behind it (researcher, verbatim, 2026-09-15)

Context that explains why the current shape is thin, not just that it is: *"focussing on
actions/triggers/operations is not new in the study. One critical shortcoming in the past, was that
these concepts have been approached from the characteristic's perspective. The observation that the
inner being is more like a web of interactions, rather than distinct and separable characteristics
helped to realise that the connecting tissue between characteristics are as important as the actual
separate characteristics. The study progressively explored new ways to isolate the connections and
this lead to pulling out the action words or verbs from individual clusters into the T3 category. It
turns out that this step has improved the ability to focus on the verb/process operations in
relation to different M-codes."*

So T3 (Operations) is not an incidental referent-identity bucket alongside T4–T15 — it's the
project's own corrective move away from a characteristic-centric framing that couldn't see the
connective tissue between characteristics. Pulling verbs out of individual M-code clusters into
their own T3 category is *why* a T3-tagged verb can relate to several M-codes at once (§6 item 2)
— that's not a new requirement being bolted onto `verb_argument`, it's the entire reason T3 was
separated out in the first place. `verb_argument`'s multi-M-code gap (§6) is a direct, structural
consequence of this history, not an independent design ask.

## 2. What's actually configured, live, today

**`cfg_method_rule` id=63** (`verb-argument-trigger-impact`, step `lexical.enrich`, active):

> "A `verb_argument` note records a verb code's own trigger (grammatical subject/agent, via
> `target_verse_lexical_id`) and impact (object/patient span(s), via `related_verse_lexical_ids`)
> as a first-class fact — distinct from `chain` (sequence/waw-consecutive only), `entity_link`
> (party/pronoun identity only), and `connective` (clause-linking only)."

**`note_type` enum** — `verb_argument` is ordinal 13 of 15, live in `cfg_enum`.

**`cfg_column.use` text — corrected as of #1607/D9 (2026-09-10)**, now accurately describes the
live use rather than contradicting it (an earlier gap #1606/#1607 both found and flagged):
- `target_verse_lexical_id`: *"...Also used by `verb_argument` notes as the agent/trigger of a
  movement (e.g. note id 346, Gen H5414G 'gave': target=Laban, the giver) — a third, distinct use
  beyond the original pronoun/entity-link framing."*
- `related_verse_lexical_ids`: *"...PLUS `verb_argument`'s recipient/impact use (e.g. note id 346,
  Gen H5414G 'gave': related=Leah, the recipient) — a third, distinct use."*
- `note_type`: now lists all 15 live values including `verb_argument`/`compound_unit` (was missing
  both as of #1589's original finding — fixed).

**These three doc-fixes are the only part of the original #1606/#1607 "proposed scope for a real
fix" that's actually done.** The rest — trigger condition, T7–T14 wiring — is not.

## 3. The one live example — checked live, still exactly one, unchanged since 2026-09-05

```
verse_lexical_note id=346, created 2026-09-05T11:47:21Z
note_type: verb_argument
target_verse_lexical_id: 885443  (Laban — agent/trigger)
related_verse_lexical_ids: [885445]  (Leah — recipient/impact)
value_text: "'gave' (H5414G): trigger/agent is Laban (position 4), impact/recipient is Leah (position 6)."
evidence_text: NULL
```

This one row demonstrates the mechanism works when someone writes it by hand. Nothing has produced
a second one in the ten days since.

## 4. Confirmed unsupported, not just underused (checked live this session, unchanged from #1606/#1607)

1. **No trigger logic anywhere.** `lib/lexicalenrich.py:_quality_problems_for_note()` has dedicated
   quality checks for `chain`/`idiom`/`structural_pattern`/`recurrence_role_shift`/
   `cross_lemma_shared_gloss` — **none for `verb_argument`**. Nothing in code says "this T3
   operation-verb should get one attempted."
2. **The LLM prompt doesn't single it out either.** `lib/lexicalenrichgenerate.py:_instructions()`
   passes all 15 `note_type` values as a flat list — *"pick the relevant type"* is the only
   steering for `verb_argument`, same as every other type, no special prompting.
3. **No connection to T7–T14 in code anywhere.** The mechanism points at another `verse_lexical`
   row generically; nothing checks or leverages whether that row's own `cluster_strong` tag is a
   real party/place/object/natural-world referent — exactly the link that would make this
   project's whole T-code tagging effort pay off for Layer 2.
4. **Scale of the unaddressed pool:** 2,574 live `cluster_strong` rows carry `T3` (Operations) —
   candidate trigger-verbs, by the mechanism's own definition. One has ever gotten a note.

## 5. What's already been decided, not just found

- **D9 (#1607)**: *"the `verb_argument` would resolve in the same process"* — researcher confirmed
  scope: verb_argument's fix folds into the six-point column review, not a separate track.
- **D4 cross-reference (#1607)**: coverage for `verb_argument` (which T3 verbs get one attempted)
  is expected to be answered by `role`'s own completeness once built — `role`'s redesign (empty-set
  = error, gated by a pre-run validator) means every T3-tagged strong is now, by construction,
  discoverable — the trigger condition question becomes "does this T3 code's `role` membership
  alone justify an attempt," not a separate detection problem.
- **#1704 Phase 1b/1c — the consumption pattern**: `verb_argument` is the natural build for
  **`directional-party-frame`**, the single largest gap found in the whole catalogue (18
  questions across three components: T0.1, T2.9, T4.1–T4.5). Pairing each side's `party_kind`
  (already a live, working signal) with `verb_argument`'s trigger/impact shape lets the direction
  fall out mechanically: trigger=divine/impact=human → T4.1, trigger=human/impact=divine → T4.2,
  trigger=human/impact=human → T4.3/T4.4.

## 6. What #1705 itself adds — the genuinely new, undesigned part

Researcher, verbatim, raising #1705 (from the #1704 design-review conversation):

> *"verb-argument it is current definition fall far short. it must be expanded. verb operation is
> rich, extremely important for the study and not well understood. the same verb operates in
> relation to many different M-codes and its impact varies from incidental (nothing to discover or
> report) to actually be a core IB characteristic that drives a host of other activities and
> characteristics. at the moment verb-argument must carry this full load."*

Two requirements beyond anything in §5 above, neither designed:

1. **Significance grading** — incidental (nothing worth reporting) through core inner-being driver
   (a characteristic that drives a host of other activities). Currently binary: a note exists or it
   doesn't; no gradient.
2. **Multi-M-code relation** — the same verb can relate to several different M-clusters at once,
   not a single agent/patient pair scoped to one reading. Current shape (`target_verse_lexical_id` +
   `related_verse_lexical_ids`, both pointing at other `verse_lexical` rows) has no field for "this
   verb's relevance to cluster X vs. cluster Y differ."

Plus, carried from #1704 §2 (b)(iv), a third widening already flagged but not yet folded into a
formal ask: **referent-identity arguments** — `verb_argument` currently only naturally pairs with
`party_kind` (T4/T7/T8/T9); the role-driven-reading design wants it to also carry T10–T14 referent
arguments (a place, an object, a body-part) as the verb's target, not just a party.

## 7. `verb_argument`'s actual scope — researcher, verbatim, 2026-09-15

The clearest statement yet of what this is actually for, beyond §6's two named gaps:

> *"In my view, the verb_argument in its broadest sense is about harnessing the implications of T3
> in the context of the verse. When a word in the verse is assigned a T3 role it triggers all the
> related discovery questions. Where does it come from (party-kind, other object), what does it
> impact on (party-kind, other object), what does it do (meaning of T3), what M-code does it relate
> to, does the direction of travel matter, is there any transformational impact, does it cause
> blockage, what is the impact on the body (this list of questions is not exhaustive). Many of the
> answers is not going to be in a single verse — but looking at the same impact scenario across
> multiple verses may lead to answers."*

This reframes `verb_argument` from "a note_type that needed a code home" (§1's original #1449
framing) into **the trigger mechanism itself**: T3-role-assignment fires a whole discovery-question
set, not a single trigger/impact pair. Named questions (explicitly not exhaustive):

- **Source** — where does it come from (party-kind, or another referent-identity object)?
- **Target** — what does it impact on (party-kind, or another referent-identity object)?
- **Action** — what does it do (the T3 verb's own meaning)?
- **M-code relation** — which cluster(s) does it relate to? (§1a — the structural reason this is
  plural, not singular)
- **Direction** — does the direction of travel matter?
- **Transformation** — is there a transformational impact?
- **Blockage** — does it cause blockage?
- **Body** — what is the impact on the body?

**Directly matches, and gives full content to, #1704 §2 (b)(iv)** (the role-driven-reading-sequence
design, same session): *"then the focus move [to] the action words (T3) and its relation to each
party-kind and include discovery of movement, force, negatives, descriptive words and the role of
other key T-codes."* That was the shape; this is the actual question list filling it in — the two
are the same mechanism, not two separate requirements to reconcile.

**New, not previously named anywhere:** *"many of the answers is not going to be in a single verse —
but looking at the same impact scenario across multiple verses may lead to answers."* Some of these
questions are **cross-verse by nature**, not resolvable from one occurrence. The closest existing
infrastructure is process (c)'s own reading discipline (#1682: "scan every verse occurrence, no
sampling," `difference-inference`/`surface-gloss-divergence` tags already compare across
occurrences of one strong within a family) — but that discipline scans one *strong's* occurrences
for meaning-sense variation, not one *T3-role-and-scenario* pattern across potentially many
different strongs/verses sharing the same trigger/impact shape. Whether the existing per-family
reading scan already covers this or a distinct mechanism is needed is **not decided here** —
flagged as a real, concrete design question for whoever designs `verb_argument`'s actual mechanism.

## 8. Where this leaves #1705

Nothing in §6/§7 is designed. The escalation is a raised, `decision_required` placeholder naming the
requirement — genuinely a blank slate, not a proposal awaiting approval. What exists to build from:
a working single example (§3), a correct (if thin) config description (§2), a known consumption
pattern for the *party-pairing* half of the problem (§5's `directional-party-frame`), the
methodological reason it's structurally multi-M-code (§1a), and now a concrete, if
not-exhaustive, discovery-question list (§7) — but still zero design for how any of it is actually
triggered, scoped (single-verse vs. cross-verse), stored, or graded for significance.
