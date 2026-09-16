# Analytic Event Inventory — Phase 4: Question → Event Crosswalk

**Escalation:** #1704 · **Phase:** 4 (Discovery → Match → Corrective Actions → **Crosswalk**) ·
**Date:** 2026-09-16

**Purpose, per researcher instruction, verbatim:** *"1704 should lead into a cross correlation of
the catalogue questions and the event that will lead to the surfacing of the data... not only a
broad indication (e.g. lexical) but the exact event or element of the stage that will lead to the
answer."* Every one of the 100 live catalogue questions (98 existing + `T2.11.1`/`T2.11.2`,
#1701), one row each, naming the **exact** mechanism — which column, which code path, which
`note_type`, which stage — not a category label. Nothing re-decided here; every row cites its
Phase 1c/Phase 2/Phase 3 finding, or today's corrections (Group D, #1701, #1665).

**Reading the "Surfaced by" column:** a specific table/column/function name = it exists and is
live; "not built" = the mechanism is designed (named in Phase 2/3) but not yet coded; "no
mechanism" = genuinely nothing surfaces this yet, pure LLM reading of already-available text is
the only current path; "no mechanism needed" = confirmed by Phase 1c as pure synthesis/
interpretation, correctly requiring none.

---

## T0 — Divine Image and Created Design

| Question | Event/mechanism | Surfaced by (exact) | Status |
|---|---|---|---|
| T0.1.1 | directional-party-frame | `verb_argument` (trigger/impact, `cfg_method_rule` id 63) × `party_kind` (`cluster_strong` T7/T8, `lib/lexical.py:load_code_classes`) | Ingredients live, combining event not built |
| T0.1.2a/2b | directional-party-frame (same as T0.1.1) | same | Unexercised — 0 findings, 2026-09-04 split pattern |
| T0.2.1 | purpose-clause-detection | Hebrew lə+infinitive / Greek hina/hopos telic markers — no column exists | No mechanism |
| T0.2.2/2.3 | none needed | direct LLM synthesis on already-surfaced T0.1/T0.2.1 data | No mechanism needed |
| T0.3.1/3.2/3.3 | none needed | derivative of T0.1+T0.2, answer-stage LLM synthesis | No mechanism needed |
| T0.4.1 | typological-link | none — needs an external OT-quotation/type-antitype cross-reference resource this project doesn't have | **DROPPED, 2026-09-16** — researcher: "not adding value to characteristic debate." Excluded from #1696's migration. |

## T1 — Definition

| Question | Event/mechanism | Surfaced by (exact) | Status |
|---|---|---|---|
| T1.1.1/1.2/1.3 | term-grain aggregation | `related_word`/`cross_lemma_shared_gloss` `note_type` pulls (`lib/lexicalenrich.py`), aggregated per-*term* — mechanism exists, grain is per-verse today | Grain fix needed, not new build |
| T1.2.1 | kind-classification | `verse_lexical.morph_code` (live) → part-of-speech derivation (verb→act, adjective→quality, noun→condition/disposition) | Column live, derivation not coded |
| T1.2.2 | `compound_unit` `note_type` | `verse_lexical_note.note_type='compound_unit'` — enum value exists, `cfg_method_rule` not registered | Group A, buildable |
| T1.3.1/3.2/3.3 | structural-opposite-term detection (= T7.1.5's demand) | `related_word`/`cross_lemma_shared_gloss`, formalized as one named event | Reuse existing mechanism, not built as named event |
| T1.4.1a | morph_code direct | `verse_lexical.morph_code` — no derivation needed, the question IS the column | Live |
| T1.4.1b/4.2/4.3 | morph_code-derived | `verse_lexical.morph_code` | Live, same mechanism as 4.1a |
| T1.5.1/5.2 | post-occurrence/characteristic-level sequence | none — new grain (across a family's verses, not within one) | No mechanism |
| T1.6.1/6.3 | post-occurrence/characteristic-level sequence (same, longitudinal) | none | No mechanism |
| T1.7.1/7.2/7.3 | `polarity` `note_type` + `party_kind`/T4/T9 (adversarial/angelic interference) | `verse_lexical_note.note_type='polarity'` (enum exists, rule not registered) + `cluster_strong` T4/T9 lookup (live, same mechanism as T4.6) | Group A, buildable |

## T2 — Constitutional Location and Boundaries (+ new `T2.11`)

| Question | Event/mechanism | Surfaced by (exact) | Status |
|---|---|---|---|
| T2.1.1/1.2 | cross-characteristic co-occurrence, filtered for M47 | **CORRECTED, 2026-09-16** — researcher: spirit/soul/heart/mind is `cluster M47` ("Inner Seat," verified live, 38 strongs), not a missing T-code. Same mechanism as T5.4/T6.1–6.3: `_assess_cross_cluster_cooccurrence.py` (#729, inactive), reactivated and filtered for M47 co-occurring with the verse's other M-code(s) | Kept live, "very relevant" (researcher) — reactivate the script, no new referent code needed |
| T2.7.1 | T14-body-part-surfacing | none — no `verse_lexical` column for T14 (unlike T4/T5/T7/T8/T9) | No mechanism, cheap to build (same shape as `is_negator`) |
| T2.9.1/9.2 | directional-party-frame | same as T0.1.1 — `verb_argument` × `party_kind` | Ingredients live, combining event not built |
| T2.10.1 | T14-body-part-surfacing + post-occurrence sequence | same T14 gap + the undesigned sequence event | No mechanism, two-part gap |
| **T2.11.1** (new, #1701) | faculty-engagement-reflection | a new `ib_observation` row at the end of a subgroup's read, per #1704 §5 decision 4 (b)(v) | Question authored 2026-09-16; reading-stage process spec not yet updated to actually produce it |
| **T2.11.2** (new, #1701) | faculty-engagement-reflection (pattern, cross-verse) | same, subgroup-level synthesis across the read | Same as above |

## T4 — Divine/Human Interfaces, Spiritual Beings

| Question | Event/mechanism | Surfaced by (exact) | Status |
|---|---|---|---|
| T4.1.1/1.2/1.3, T4.2.1/2.2/2.3, T4.3.1/3.2/3.3, T4.4.1/4.2/4.3, T4.5.1/5.2/5.3 (15 qs) | directional-party-frame | `verb_argument` (trigger=`target_verse_lexical_id`, impact=`related_verse_lexical_ids`) paired with `party_kind` (`cluster_strong` T7/T8) — direction falls out mechanically (trigger=divine/impact=human → T4.1, etc.) | Both ingredients live individually; the combining event and `verb_argument`'s own trigger logic (1 example ever) are the real gap |
| T4.6.1 | `party_kind` + T4/T9 lookup | `cluster_strong` T4 (adversarial)/T9 (angelic), `lib/lexical.py` | **Live and exercised** — real historical findings exist |
| T4.6.2a/2b, T4.6.3a/3b | same `party_kind`+T4/T9 mechanism | same | **Mechanism live, wiring not connected** — 0 findings ever. Cheapest fix on this entire list: wire the existing lookup to these 4 question codes directly |

## T5 — Formative and Developmental Dimension

| Question | Event/mechanism | Surfaced by (exact) | Status |
|---|---|---|---|
| T5.1.1/1.2 | T3-operation-surfacing | `cluster_strong.operation` flag — exists, confirmed dead, not read anywhere | Folds into #1701, not standalone |
| T5.2.1 | post-occurrence/characteristic-level sequence | none | No mechanism |
| T5.3.1/3.2 | T3-operation-surfacing (same as T5.1) | `cluster_strong.operation`, dead | Folds into #1701 |
| T5.4.1/4.2 | cross-characteristic co-occurrence | `_assess_cross_cluster_cooccurrence.py` — built once, confirmed inactive since 2026-08-18 (#729) | **DROPPED, 2026-09-16** — part of the T5.4/5.5/5.6 reframe (option C, #1704 item 6), replacement questions coming next round |
| T5.5.1 | post-occurrence/characteristic-level sequence | none | **DROPPED, 2026-09-16** — same reframe |
| T5.6.1 | future-orientation marker | `verse_lexical.morph_code` (tense/aspect) + `related_word`-shaped lexical markers ("last days" etc.) | **DROPPED, 2026-09-16** — same reframe. **Conflict, unresolved**: this was the mechanism's own primary consumer, approved for build the same turn it was dropped — researcher to confirm build-anyway vs. hold for the replacement questions |

## T6 — Structural Relationships

| Question | Event/mechanism | Surfaced by (exact) | Status |
|---|---|---|---|
| T6.1.1/1.2 | cross-characteristic co-occurrence | `_assess_cross_cluster_cooccurrence.py` (#729, inactive) | Reactivate |
| T6.2.1/2.2 | cross-characteristic co-occurrence + corpus-wide ordering | same script + an ordering extension | Reactivate + extend |
| T6.3.1/3.2/3.3 | cross-characteristic co-occurrence + causal-connective detection | same script + `is_connective` column (not built) + **`cluster_strong.rationale` sub-type text, already recorded for all 95 T6 rows** (checked live, 2026-09-16 — causal/coordinating/purpose/temporal/comparative/etc. per-strong) | Reactivate script; `is_connective` buildable now; sub-type data exists as free text, not structured |
| T6.4.1/4.2/4.3 | `related_word` + `cross_lemma_shared_gloss`, cross-characteristic aggregation | `lib/lexicalenrich.py` note_type pulls — building blocks exist, cross-characteristic aggregation step not built | Reuse + extend |
| T6.5.1/5.2/5.3 | none needed | synthesis of T6.1+T6.4, answer-stage LLM once those two are wired | No mechanism needed, depends on above landing first |

## T7 — Evidential and Methodological Foundation

| Question | Event/mechanism | Surfaced by (exact) | Status |
|---|---|---|---|
| T7.1.1/1.2/1.3/1.4, 1.6–1.10 (9 qs) | term-grain aggregation | `related_word`/`cross_lemma_shared_gloss`, same grain issue as T1.1 | Grain fix, not new build |
| T7.1.3 | term-grain aggregation, **plus `idiom` note_type** | `related_word`/`cross_lemma_shared_gloss` + `idiom` (Group A, buildable) | **Question text expanded, 2026-09-16** — researcher approved `idiom` matched here (option B), text revised to explicitly prompt idiom/analogy/implied meaning, see `1704-catalogue-content-decisions-v1-20260916.md` item 8 |
| T7.1.5 | structural-opposite-term detection (= T1.3's demand) | `related_word`/`cross_lemma_shared_gloss`, formalized as one named event | Reuse, not built as named event |
| T7.2.1 | `connective`/`chain` `note_type`, directly named in the question text | `verse_lexical_note.note_type` IN ('connective','chain') — enum values exist, `cfg_method_rule` not registered (Group D correction) | **Live and exercised historically** (146 answers, old `finding` corpus) — going forward, Group A buildable |
| T7.2.2a/2b | genre/contextual-setting classification | none — **no data source in `iba.db`** (`verse_meta.genre` dropped, #1607 D12/D13) | **RETIRED, 2026-09-16** — researcher: "genre cannot be determined from a verse reading," consistent with the standing #1608 ruling. Excluded from #1696's migration. |
| T7.2.3 | none needed (argument-structure) | direct LLM reading of `verse_text`, not Layer 1/2-surfaceable | No mechanism needed |
| T7.2.4 | genre/contextual-setting classification (interpretive half needs none) | same blocked data source as T7.2.2 | **RETIRED, 2026-09-16** — same researcher decision as T7.2.2a/2b. Excluded from #1696's migration. |
| T7.2.5/2.6 | anchor-verse ranking | `resolved_sense`-collapse/anchor-verse work already in progress at #1526 | **Already in progress**, not a fresh gap |
| T7.3.1/3.2/3.3/3.4 | none needed | external human-science interpretive lens applied to already-surfaced evidence | No mechanism needed |

---

## Summary — what this table makes visible that the component-level view didn't

- **20 of 100 question codes (T4.1–T4.5's 15 + T0.1.1/1.2a/1.2b + T2.9.1/9.2)** resolve to the
  exact same two-ingredient mechanism (`verb_argument` × `party_kind`) — the single highest-leverage
  build item in the whole catalogue, now visible as a literal count, not just "highest-value gap."
- **4 question codes (T4.6.2a/2b/3a/3b) have a fully live mechanism sitting completely
  unconnected** — the cheapest fix on this entire list, a wiring task with zero design work.
- **12 questions (T0.2.2/2.3, T0.3.1–3.3, T6.5.1–5.3, T7.2.3, T7.3.1–3.4)** are confirmed to need no
  mechanism at all — pure synthesis, already correctly served by direct LLM reading.
- **`T2.11`'s 2 new questions** are the only ones whose mechanism is a *stage design gap* (the
  reading-stage process spec doesn't yet implement step (b)(v)) rather than a missing column or
  script — worth keeping distinct from the script-reactivation group above.
- **CORRECTED, 2026-09-16, per researcher review of Phase 5**: 8 question codes retired from the
  live catalogue entirely (`T0.4.1`, `T5.4.1`, `T5.4.2`, `T5.5.1`, `T5.6.1`, `T7.2.2a`, `T7.2.2b`,
  `T7.2.4` — genre/contextual-setting and typological-link both judged not to add value; T5.4–5.6
  reframed, replacements coming); `T2.1` corrected from "no T-code covers this" to a real, live
  mechanism (`M47` + cross-cluster co-occurrence); `T7.1.3` gains `idiom` and an expanded question
  text. Full record: `1704-catalogue-content-decisions-v1-20260916.md`. Live question count is now
  **92**, not 100.

This table is now the authoritative per-question reference — Phase 2/3's own event-level groupings
(Group A/B/C/D) are still the right unit for *build sequencing*, this is the right unit for
*checking any one question's own readiness* before it's actually asked in a real answer-stage run.
