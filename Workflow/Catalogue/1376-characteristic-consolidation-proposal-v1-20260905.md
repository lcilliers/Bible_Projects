# Characteristic-model consolidation — proposal

> Escalation #1376. Builds directly on
> [`1376-characteristic-tables-cross-db-inventory-v2-20260901.md`](1376-characteristic-tables-cross-db-inventory-v2-20260901.md)
> (the inventory — read that first for full detail on Models A–D; this document does not repeat it,
> only cites it). Your instruction (2026-09-05): *"proceed to review and propose how to consolidate
> all the different attempts to prepare a table of all characteristics using the results from the
> lexicals. This include retiring all the false positive characteristic type efforts."*
>
> **This is a proposal, not an executed decision.** Nothing below has been applied. Per
> `feedback_design_work_is_never_self_correctable`, a model-architecture call for the programme is
> yours to make — this document is the "genuine judgement call" filed for your review, per
> `docs/interaction-preferences.md`.

## The one fact that changes everything since the inventory was written

The inventory (2026-09-01) predates `verse_lexical` (built 2026-09-04, escalation #1383, Window 1
Layer 1/Layer 2 — 552,353 rows, full corpus). That is the first time this project has had a
**span-grounded, per-verse, mechanically-consistent** read of every occurrence — `role`,
`party_kind`, `is_negator`, `chain`/`entity_link`/`connective`/`structural_pattern` notes, morph —
built the same way everywhere, not hand-typed once per cluster or book. None of Models A/B/C had
this when they were built. That's the "results from the lexicals" your instruction points at: it's
new base data strong enough to finally ground a characteristic definition in verse evidence instead
of gloss lists (Model A), book-scoped meaning indexes (Model B), or free-text-only readings
(Model C).

## Recommendation, stated plainly

**Characteristics should be *derived bottom-up* from `verse_lexical` phenomena-in-context (Model
C's own conceptual break — "a HIB has phenomena that are characteristics in operation," not a
catalogue) — now finally buildable at full-corpus scale because `verse_lexical` exists. Models A
and B's *catalog* function (a hand-authored or book-scoped list of named characteristics) should be
retired as that function; their *data* is not all worthless and is disposed of differently below.**

The one thing every model agrees is still useful and costs nothing to keep: **`cluster`/
`cluster_code`** (the 49 M-code buckets). It's the one shared vocabulary across both databases,
already wired into `verse_lexical`, `cluster_strong`, and the live debate pipeline. Nothing here
touches it.

## Item-by-item disposition

| Table | Recommendation | Why |
|---|---|---|
| `cluster` (both DBs) | **Keep as-is.** | Shared vocabulary, live everywhere, coarse-grained enough to survive whatever finer model replaces `characteristic`. |
| `cluster_strong` (iba) | **Keep as-is.** | The Strong's→cluster assignment itself (Model A's HIGH/MEDIUM/LOW tiers) is a reasonable coarse filter; the problem is one level down, at `characteristic`, not here. |
| `characteristic` (277 rows) | **Retire as the catalog of record.** Freeze the existing rows (read-only, not deleted — they're 6 months of researcher naming/definition work and may still seed candidate names) but stop treating this table as "the" characteristic list going forward. | Self-admittedly "a convenience of arrangement, not a claim about the inner-being system" (the session log's own words) — gloss/frequency only, **zero verse-layer evidence**, only 35/49 clusters ever done. This is the clearest "false positive" in your framing: it looks like an analytical result but was built without ever reading a verse. |
| `characteristic_subgroup` / `cluster_subgroup` (146/175 rows) | **Retire the existing rows as stale; do not rebuild them as a table in this pass.** | Abandoned mid-way (17/49 clusters), lemma-based not span-based, and the inventory's own conclusion already says a rebuild would need full re-derivation against current lexicals, not re-labelling. That re-derivation is real, separate work — proposing it as an open follow-on (below), not doing it here. |
| `ib_characteristic` (1,634 rows) | **Do not delete. Re-scope, don't retire.** | Real depth (`stems`/`morph_codes`/`esv_words`/`key_span_id` — closer to actual lexical grounding than Model A ever got), just organised on the wrong axis (by book) and narrow (Psalms+Proverbs). Its `family` groupings are candidate material worth checking against `verse_lexical` phenomena before being thrown away — a cheap cross-check, not a rebuild. |
| `ib_characteristic_legacy` (29 rows) | **Retire outright (archive table, mark inactive in `cfg_table`).** | Explicitly a frozen backup of an already-superseded version of Model B. No live reference, no ambiguity — this is the one item in this whole inventory with no judgment call attached. |
| `hib` / `phenomenon` / `operation` / `operation_party` (iba, Model C) | **Keep and treat as the target shape.** Do not retire; this is what a `verse_lexical`-grounded characteristic model should look like once scaled past Daniel. | Richest design (per-HIB, per-verse, sourced/targeted), narrowest coverage (121 rows, one book) precisely because it was hand-read verse-by-verse without `verse_lexical` to lean on. That constraint is gone now. |
| `wa_dimension_index`, `ve_dimension_scoreboard`, `wa_dim_review_cluster_log`, `wa_session_b_dimensions`, `prose_section_dimension_link` (Model D, 5 tables) | **Retire outright (drop or archive-and-drop).** | Already universally marked retired in the inventory; `ve_dimension_scoreboard` records every one of its 18 dimensions as FAILED or IN-PROGRESS, never passed. Nothing here is a judgment call — it's dead weight the inventory already closed the book on. Only reason not already dropped: no one has proposed the physical cleanup until now. |

## What this proposal does NOT decide (flagged, not resolved here)

1. **How, mechanically, a `characteristic` gets derived from `verse_lexical` + `phenomenon` at
   scale** (clustering phenomena by some similarity measure? researcher-named groupings seeded from
   `ib_characteristic.family` and cross-checked against phenomena? something else?) — this is the
   real design work Models A/B/C each tried and didn't finish, and it deserves its own proposal
   once you've confirmed the disposition table above, not bundled into it.
2. **Whether `characteristic_subgroup`/`cluster_subgroup` gets rebuilt at all**, and if so, on what
   basis (span-level against `verse_lexical`, presumably) — named as a real follow-on above, not
   designed here.
3. **Timing** — none of this competes with or blocks the live Window 1/Window 2 lexical-build work;
   it's parked analysis, same as #1376 has been since 2026-09-01, until you decide otherwise.

## If approved, the mechanical retirement work (drop/archive the dead tables, freeze `characteristic`/`characteristic_subgroup`/`cluster_subgroup`, mark `ib_characteristic_legacy` inactive) is a small, low-risk follow-on migration script — not done here, pending your decision on the table above.

---

## Addendum, 2026-09-05 — your decision + the grouping/clustering question

**Your decision, recorded verbatim in escalation #1376's own history:** approve retiring
`characteristic`, `ib_characteristic_legacy`, and the 5 Model-D tables (config work only —
`cfg_table.inactive` flips, proposed as 6 individual `configmaint.propose` calls, escalations
#1493-#1498, all `ready_for_approval`, awaiting your approve/reject/revise); keep `cluster`/
`cluster_strong` **and** `characteristic_subgroup`/`cluster_subgroup` for now, no change to those;
no rebuild yet. Your new ask: *"propose the best way to proceed with grouping or clustering
phenomena. provide visibility on what is now available to work with from verse_lexical."*

### Visibility: what's actually there right now (checked live, 2026-09-05)

| Layer | Rows | Coverage | What it actually holds |
|---|---|---|---|
| `verse_lexical` (Layer 1, mechanical) | 975,451 | 29,754 / 29,759 verses — essentially the full corpus | Per-token: `role` (content 662,657 / function 312,794), `party_kind` (only `divine`, 13,476, populated so far — `human`/`non_human` wait on #1477/#1479-#1492's approval), `is_negator`, `morph_code`, `narrative_morph`, `resolved_sense`, `ambiguity_note`, `status` |
| `verse_lexical_note` (Layer 2, relational) | **0** | **none** | Built and wired (escalation #1383, 2026-09-04) — `chain`/`entity_link`/`connective`/`structural_pattern`/`recurrence_role_shift`/`cross_lemma_shared_gloss`/`verb_argument` (pending #1475/#1476) all exist as `note_type` values, but `lexical.enrich` (the tool that writes rows here) has never been run against real content — only a throwaway test fixture (John 1:1-5, created and fully deleted, escalation #1450) |
| `passage` | 18,558 | boundary rows only | Almost entirely auto-derived scope boundaries (`rule`, `source`, `verse_count`) with `genre` **NULL on every single row** — the one real content field group (`feasibility_note`/`debate_status`/`story_summary`) is populated on a handful of Daniel passages only, from the pre-`verse_lexical` manual debate method |
| `hib`/`phenomenon`/`operation` (Model C) | 63 / 177 / 177 | Daniel only | Unchanged since the inventory — richest design, built entirely by hand, predates `verse_lexical` |

**The one fact that has to shape any proposal here:** the layer a phenomenon-grouping method would
actually want to read from — `verse_lexical_note`, the relational "who triggers what, what refers
to what, what follows what" layer — is schema-complete but **data-empty**. `verse_lexical` itself
(the mechanical per-token layer) is at full corpus scale and genuinely new since the inventory, but
it answers "what kind of word, said by/about whom" — not yet "which verses describe the same
ongoing inner-being event." Designing a clustering algorithm against zero real relational rows
would be designing in the abstract, the same mistake Models A-C each made in their own way (Model
A: rules with no verse layer; Model B: real lexical grounding but wrong scoping axis) — Model C is
actually the one closest to the right idea (real per-verse relational reads), it just did it by
hand instead of building on this new base layer.

### Proposed approach — two tiers, not one algorithm

**Tier 0 — available today, zero new base-layer work, mechanical only.** A coarse phenomenon-
*candidate* index: for every verse, cross-tabulate `verse_lexical.party_kind` (once #1477/#1479-92
land: divine/human/angelic/adversarial) against the `cluster_code` of its content-role codes (via
`cluster_strong`) — "which party is associated with which cluster-topic, in which verse." This is
buildable now, corpus-wide, from data that already exists, and gives a first coarse answer to "where
does a given inner-being topic co-occur with a given kind of party" — but it is NOT yet "the same
phenomenon recurring," only "the same topic-vocabulary recurring." Worth building as a first-pass
visibility tool regardless of what Tier 1 becomes, since it costs nothing new.

**Tier 1 — the real grouping/clustering answer, but it needs real `verse_lexical_note` data first.**
Once `lexical.enrich` has actually been run over some real passages (not a test fixture): group
phenomena by shared `entity_link` (same referent HIB across verses = one ongoing thread), by
`verb_argument`'s target (same triggering HIB = a recurring behavioural pattern for that HIB), by
`chain` (a sequential unfolding read as one event), and by `structural_pattern`/
`recurrence_role_shift` (the same characteristic recurring under a changed role). This is
structurally close to what Model C already does by hand for Daniel (a phenomenon *is* a HIB's
state in one verse; an operation *is* its movement) — the difference is doing it FROM
`verse_lexical_note`'s mechanical relational facts instead of a free-text manual read, which is
what would let it scale past one book.

**Recommendation, concretely:** before committing to a clustering algorithm's exact shape, run
`lexical.enrich` for real over a small pilot (a handful of chapters — Daniel again, to stay
comparable against Model C's own existing hand-built phenomena as a validation check, or a fresh
short book) and see what `verse_lexical_note` actually looks like at real scale. Prototyping a
grouping method against genuine data beats designing one against an empty table — the same lesson
this whole document's Model A/B critique already draws. Not started here — this is the proposal,
not the pilot; your decision needed on whether to run it and on what scope.
