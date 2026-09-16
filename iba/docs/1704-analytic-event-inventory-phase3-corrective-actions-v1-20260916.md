# Analytic Event Inventory — Phase 3: Corrective Actions

**Escalation:** #1704 · **Phase:** 3 of 3 (Discovery → Match → Corrective Actions) · **Date:** 2026-09-16

Ordered by dependency and value, not by event number. Draws only on Phase 2's own findings — nothing
new asserted here.

## Group A — buildable now, no dependency, do first

1. **`is_connective` column** (feeds causal-connective detection, T6.3) — same shape as
   `is_negator`/`party_kind`: a cheap `cluster_strong`-sourced boolean on `verse_lexical`. Confirmed
   dead code path (#1702), confirmed real question demand (T6.2/T6.3, #1704 Phase 1b/1c).
2. **T14 lexicon-assist column** (feeds T14-body-part-surfacing, T2.7/T2.10) — identical shape and
   justification to item 1.
3. **Reactivate `_assess_cross_cluster_cooccurrence.py`** (feeds cross-characteristic co-occurrence,
   T5.4/T6.1/T6.2/T6.3-partial) — the code exists (#729), register it per
   `governance.new_utility_registration_timing` rather than building fresh.
4. **Define `compound_unit` and `polarity`** in `cfg_method_rule` (#1589's own gap) — purpose now
   confirmed by this phase (T1.2.2, T1.7 respectively) rather than abstract "undefined note_type."
5. **`kind-classification`** — direct `morph_code` derivation, feeds T1.2.1. Cheapest item on the
   whole list.
6. **`directional-party-frame`** — pair existing `verb_argument` + `party_kind` data. Not gated on
   #1711 (that's about the LLM-driving mechanism for the *new* pre-subgroup Layer 2 stage; this is a
   mechanical combination of two already-live signals, usable at the reading stage now once `role`'s
   redesign lands, #1706 Phase B). Feeds 18 questions — highest-value single item on this list.
7. **`structural-opposite-term` and `term-grain-aggregation`** — both reuse existing mechanisms
   (`related_word`/`cross_lemma_shared_gloss`), no new code, just formal naming + (for term-grain)
   an aggregation step that doesn't exist yet at term level.

**None of Group A gates or is gated by Layer 1/#1706's build sequence** — these are answer-stage/
reading-stage instruction and lexicon-assist additions, independent of the Layer 1 rebuild or
#1711's Layer 2 design. Could run in parallel with either.

## Group B — needs a real design decision first

8. **Post-occurrence/characteristic-level sequence** (4 consumers: T1.5, T1.6, T5.2, T5.5) — worth
   real design attention given the fan-out; not a quick column add.
9. **Purpose-clause-detection** (T0.2.1) and **future-orientation marker** (T5.6, T0.4-partial) —
   both lightweight once designed, single-question-consumer each, low priority relative to Group A.
10. **Genre/contextual-setting classification** (T7.2.2, T7.2.4) — blocked on `verse_meta.genre`
    (dropped, #1607 D12/D13) being rebuilt, not just a wiring problem. Real base-data decision:
    does `genre` come back as a `verse_meta` column, and if so, sourced how (mechanical
    literary-form lookup vs. LLM classification)? Not decided here.
11. **Typological-link** (T0.4) — lowest priority; likely needs an external cross-reference data
    source this project doesn't currently have. Flag and park, don't design speculatively.

## Group C — explicitly not standalone, folds into #1701's resumption

12. **T3-operation-surfacing** and **constitutional-level vocabulary detection** — both, per #1702's
    own recommendation, should NOT be designed in isolation here. Both are instances of the same
    "no T-code/referent-class exists for this because the old Inner-Faculties framing was retired as
    conceptually wrong" problem #1701 already owns. Building either as a standalone fix would risk
    reintroducing the exact category error #1598/#1701 diagnosed. **Action: carry both into #1701
    when it resumes, not before.**

## Group D — CORRECTION, 2026-09-16: 6 more note_types checked live, none previously accounted for

Researcher check, this chat turn: *"So you wont have any dangling config or code elements that
does not have a home in the pipeline."* Verified rather than assumed — and it wasn't clean.
**10 of the 15 live `note_type` values lack a registered `cfg_method_rule`, not the 6 `#1589`
originally scoped** (checked live: `related_word`, `structural_pattern`, `recurrence_role_shift`,
`cross_lemma_shared_gloss`, `verb_argument` are the only 5 with a dedicated rule). The other 5 of
#1589's original 6 (`compound_unit`, `polarity`, `noun_relational`, `noun_severity`) plus 6 more
Phase 2/3 never named at all — `idiom`, `pronoun_resolution`, `entity_link`, `chain`, `connective`,
`inert` — needed checking. Most have a documented purpose already, in `1446-verse-word-analytic-
methods-extract-v2-20260904.md` §2b (2026-09-04, predates this whole #1704 thread) — just never
promoted into a registered rule, and (for 3 of them) never matched to a catalogue purpose either:

- **`chain`, `connective`** — purpose confirmed: T7.2.1 names both directly in its own question
  text ("connective/chain edge"). **Add to Group A** — cfg_method_rule definition needed, purpose
  already established, no new design.
- **`entity_link`, `pronoun_resolution`** — NOT a standalone catalogue-question answer. Per #1446's
  own definitions (ties a verb/noun to its named subject; same-verse antecedent resolution), these
  are **supporting/infrastructure note_types** — their purpose is making `party_kind`/
  `directional-party-frame`'s party-identification accurate, not answering a T0–T7 question
  directly. Real purpose, correctly not in the question crosswalk — but still needs a
  `cfg_method_rule` row stating this supporting role explicitly, per
  `governance.rules_must_be_config_driven` (a rule can't live only in a 2026-09-04 doc). **Group A**
  — definition needed, purpose now stated.
- **`idiom`** — genuinely unmatched. #1446's definition (multi-code compound whose combined gloss
  diverges from a literal reading) doesn't map cleanly onto one T0–T7 question the way `chain`/
  `connective` do — plausibly feeds T7.1's lexical/semantic analysis broadly, but not confirmed.
  **Group B** — real open item, not resolved here.
- **`inert`** — a null-result bookkeeping device (confirms a function-word code needs no further
  note), not a catalogue-answering event by design. Its role is already implicit in the
  `completeness-by-code-count` rule's own principle ("a finding, or an explicit checked_empty/
  not_supported_this_language/unresolved"). Lowest priority: a one-line `cfg_method_rule` for
  governance completeness, not a real gap in coverage.

**Corrected bottom line:** the 15 live `note_type` values now all have an accounted-for status —
5 registered, 8 with a confirmed purpose awaiting registration (Group A, cheap), 1 genuinely open
(`idiom`, Group B), 1 low-priority governance formality (`inert`). Nothing is silently unaccounted
for any more — but this was NOT true before this correction, and I should not have implied it was
without checking.

## What this does NOT include — deliberately

- **#1526** (anchor-verse ranking) — already an active, on-hold escalation with its own evidence
  base; not re-opened here, just confirmed as the same event under a different name (Phase 2).
- **#1711** (Layer 2 pre-subgroup design) — not a Phase 3 item; it's a different-shaped design
  question (the LLM-driving mechanism), not a catalogue-event gap. Deliberately sequenced after
  Layer 1, per the researcher's own instruction.

## The catalogue cross-entry — `pattern_type`

The researcher's own framing this session: *"the event cross entry into the catalogue are all
defined (there are, or should be a column the catalogue for it)."* Confirmed: `wa_obs_question_
catalogue.pattern_type` (TEXT) already exists for exactly this — currently **100% NULL across all
98 live rows** (Phase 1 Vector A's own finding, re-confirmed live this session). **Phase 1c's own
per-component tables already amount to a complete question→event crosswalk** — every one of the 98
live questions was read and assigned an event (or confirmed to need none) in that document; this
phase doesn't re-derive it, just confirms it's ready to apply:

- Questions with a real event, Group A (buildable now): `directional-party-frame` (T0.1.1/1.2a/1.2b,
  T2.9.1/9.2, T4.1.1–4.5.3 = 18 questions), `term-grain-aggregation` (T1.1.1–1.3, T7.1.1–1.4/1.6–1.10),
  `structural-opposite-term-detection` (T1.3.1–3.3, T7.1.5), `kind-classification` (T1.2.1),
  `compound_unit`/`polarity` (T1.2.2, T1.7.1–7.3), `cross-characteristic-co-occurrence`
  (T5.4.1/4.2, T6.1.1/1.2, T6.2.1/2.2, T6.3.1–3.3 partial), `T14-body-part-surfacing`
  (T2.7.1, T2.10.1), `causal-connective-detection` (T6.3.1–3.3, shared with co-occurrence).
- Questions with a real event, Group B (needs design first): `post-occurrence-sequence` (T1.5.1/5.2,
  T1.6.1/6.3, T5.2.1, T5.5.1), `purpose-clause-detection` (T0.2.1), `future-orientation-marker`
  (T5.6.1), `genre-contextual-setting` (T7.2.2a/2b, T7.2.4), `typological-link` (T0.4.1).
- Questions folding into #1701 (Group C): `T3-operation-surfacing` (T5.1.1/1.2, T5.3.1/3.2),
  `constitutional-level-vocabulary` (T2.1.1/1.2).
- Questions already mechanically served, existing event, just naming it: `morph-code-direct`
  (T1.4.1a–4.3), `connective-chain-direct` (T7.2.1), `adversarial-angelic-party-kind` (T4.6.1–6.3,
  split codes unconnected per #1700/#1702, tracked separately as an execution task, not a design
  gap), `anchor-verse-ranking` (T7.2.5/2.6, #1526).
- Questions needing no event (pure synthesis/interpretation, confirmed by reading every one in
  Phase 1c): T0.2.2/2.3, T0.3.1–3.3, T7.2.3, T7.3.1–3.4, T6.5.1–5.3, T7.2.4's interpretive half.

**Not decided here — the one real open item on this piece:** *where and when* to write these 98
values. `wa_obs_question_catalogue` is mid-migration (#1696, `bible_research.db` → `iba.db`,
approved in principle, deliberately held pending #1706). Writing `pattern_type` now would mean
writing it twice (once in `bible_research.db`, again after the migration) or writing it directly
into the migration's own insert. **Recommend: fold this crosswalk into #1696's migration step as an
extra column value on the bulk insert**, rather than writing it into the soon-to-be-`inactive=1`
source table first — same effort, no double-write, and it lands in the authoritative table from day
one. Flagged for the researcher's confirmation before either #1696 or this crosswalk executes.
