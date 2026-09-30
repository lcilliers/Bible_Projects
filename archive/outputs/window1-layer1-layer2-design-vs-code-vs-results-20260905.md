# Window 1 Layer 1/Layer 2 — design questions vs. actual code vs. the 10-verse results

> Source document for every "design question" below: [`1383-verse-lexical-window1-full-build-
> specification-v1-20260904.md`](../iba/docs/1383-verse-lexical-window1-full-build-specification-v1-20260904.md)
> §C.1/C.2 (the logic) and §D.1/D.2 (validation), plus §B.9/B.18 (the note_type catalogue).
> Every "actual code" cell below was re-read from the live file just now, not recalled. Every
> "result" cell is checked against the real rows from the 10-verse test (escalation #1451,
> `outputs/window1-layer2-10verse-test-20260905.md`), not asserted.
>
> **Two real gaps between the design and the code surfaced doing this exercise — flagged in their
> own section at the end, not buried in the tables.** This is exactly the kind of thing a
> side-by-side like this is for.

## Layer 1 — mechanical fields (`verse_lexical`, spec §C.1/D.1)

| Field | Design's rule (§C.1) | Actual code | Fired in the 10 verses? |
|---|---|---|---|
| `position` | straight copy of `span.position` | `_layer1_fields()`, `lib/lexical.py` | Yes, 100% of 144 rows (mechanical copy, cannot fail short of a `span` gap) |
| `surface` | straight copy of `span.surface` | same | Yes, 100% |
| `language` | straight copy of `strong.language` | same | Yes, 100% ("Hebrew" on the 8 OT verses, "Greek" on Mark/Rom) |
| `testament` | `cfg_book_order.ordinal <= 38` → `'OT'`, else `'NT'` | `_testament_for()` | Yes — correctly `OT` on all 8 OT verses, `NT` on Mark.11.21/Rom.9.14 |
| `is_negator` | 1 if `strong` is in the negator lexicon, else `NULL` | `_layer1_fields()` via `_code_classes_for()`, now sourced from `cluster_strong` T5 (escalation #1451, was `cfg_lexical_code_class`) | Fired correctly: `Lev.17.16` (2 negators), `Rom.9.14` (2 negators, the *me genoito* construction) |
| `narrative_morph` | Hebrew-only; wayyiqtol or az+imperfect pattern on `morph_code`, else `NULL` | `_narrative_morph_for()` | Fired on 2 of 10: `Gen.46.18` ("bore," `HVqw3fs`), `Ps.94.22` ("has become," `HVqw3ms`) — both genuine wayyiqtol forms, not exercised by anything I authored, just present in the mechanical layer already |
| `gloss_consistent_in_verse` | 1 unless the same `(strong, morph_code)` pair carries ≥2 distinct `resolved_sense` values in the verse | `_apply_gloss_consistency()` | **Never fires `0` in any of the 10 verses** — not a failure, just means none of these 10 happened to contain the specific data-quality collision this check exists to catch. Not exercised, not broken. |
| `party_kind` | `'divine'/'human'/'non_human'` when the code is itself a name in the party lexicon | `_layer1_fields()`, now sourced from `cluster_strong` T4/T7/T8/T9 (escalation #1451) | Fired 4 times, all `divine`: `Prov.31.30` (Lord), `Ps.94.22` (Lord + God), `Isa.4.5` (Lord), `Rom.9.14` (God). **No `human`/`non_human` case appears in any of the 10 verses** — none happened to name a human or angelic/adversarial party by the codes currently in T8/T9/T4. |

## Layer 2 — judgement note_types (`verse_lexical_note`, spec §B.9/§B.18/§D.2)

| note_type | Design's purpose (§B.9/§D.2) | Quality check the code actually enforces | Used in the 10-verse test? |
|---|---|---|---|
| `inert` | the "checked, nothing to report" disposition — closes out a code that needs no finding | none defined in the spec, none needed | **129 of 144 notes** — the large majority, by design: every code without a specific finding this pass |
| `entity_link` | same-verse (spec says; corrected to passage-scope in §B.18) referent resolution | none enforced in code | 7 uses, 2 of them genuinely cross-verse (`Eccl.5.14`→`5.13`, `Mark.11.21`→`11.13`) |
| `structural_pattern` | detection-only flag that a rhetorical relationship spans ≥2 codes | **enforced**: `related_verse_lexical_ids` must have ≥2 entries, checked in `_quality_problems_for_note()` | 3 uses (`Ps.94.22` 3-term synonym cluster, `Isa.4.5` theophany-imagery cluster, `Amos.8.4` indictment cluster), all compliant |
| `connective` | clause-linking finding | **spec says** (§D.2): `value_text` must be one of the 3 connective classes or `UNCLASSIFIED` — **checked the actual code: this is not implemented.** `_quality_problems_for_note()` has no branch for `connective` at all. | 3 uses (`Lev.17.16` conditional clitic, `Prov.31.30` adversative "but", `Rom.9.14` rhetorical-denial idiom) — none were checked against the 3-class lexicon, because nothing in the code does that check |
| `verb_argument` | trigger/impact fact for a verb (added escalation #1449, after this spec was written) | none enforced (post-dates the spec entirely) | 1 use (`Gen.46.18` "gave": Laban→Leah) |
| `polarity` | negation-scope confirmation | none enforced | 1 use (`Lev.17.16`, second negator extending the first's scope) |
| `chain` | narrative wayyiqtol sequencing | **enforced**: `resolved` only permitted when the source row's `narrative_morph` is non-NULL | **0 uses** — despite 2 of the 10 verses (`Gen.46.18`, `Ps.94.22`) having a live `narrative_morph` value that would have made a `chain` note legitimate. Not used because this pass didn't author one, not because it was unavailable. |
| `idiom` | binary found/absent idiom test | **enforced**: `resolution_status` must be `resolved` or `checked_empty`, nothing else | **0 uses** |
| `pronoun_resolution` | same-purpose sibling of `entity_link`, specifically for pronouns | none enforced | **0 uses** — every pronoun/referent finding in this pass was written as `entity_link` instead; the spec keeps these as two separate note_types and this pass didn't distinguish them |
| `noun_relational` | (not detailed further in this spec version) | none enforced | 0 uses |
| `noun_severity` | (not detailed further in this spec version) | none enforced | 0 uses |
| `related_word` | **§D.2/§B.14 (`related-word-pull-total-sorting-manual`): "every content-role code gets a full, unconditional `strong_related` pull as `note_type='related_word'` rows" — stated as mandatory, not optional** | **spec says** (§D.2): every row's target/related code must actually appear in `strong_related`. **Checked the actual code: not implemented.** No branch for `related_word` in `_quality_problems_for_note()`. | **0 uses — and this is the one real completeness gap worth naming plainly: the design spec requires this pull unconditionally for every content-role code, and this pass did not do it for any of the ~100 content-role codes across the 10 verses.** |
| `recurrence_role_shift` | same-code recurrence with a rhetorically significant role change (added §B.18) | **enforced**: target/related must share the source's own `(strong, morph_code)` pair | 0 uses |
| `cross_lemma_shared_gloss` | two *different* lemmas sharing a gloss (added §B.18) | **enforced**: source/target must have different `strong` and matching `resolved_sense` | **Attempted once, correctly rejected**: I first tried this for `Mark.11.21`'s "fig tree" → `Mark.11.13`'s "fig tree" — same `strong` code (G4808), so this is a same-lemma recurrence, not a cross-lemma coincidence. The quality check's logic (different design question) meant I switched it to `entity_link` before running — the gate did exactly its job. |

## The two real gaps found doing this exercise, stated plainly

1. **Completeness is checked much more loosely than the design specifies.** §D.2's own control-total
   is "(content-role codes × applicable note-types for that code's part-of-speech) + (function-role
   codes × 1)" — implying a code can need *several* notes (e.g. a verb might need both a
   `related_word` pull and a `verb_argument`/`chain` finding) before the block counts as complete.
   The actual `check_completeness()` (re-read just now, `lib/lexicalenrich.py`) only requires **≥1**
   live note per `verse_lexical` row, of *any* type. That's why 129 blanket `inert` notes were
   enough to satisfy "block complete" on all 10 verses — the code's own bar is lower than the design
   document sets.
2. **The mandatory `related_word` pull was never built, and this pass never did it.** The design
   names this as unconditional for every content-role code (~100 of the 144 rows across these 10
   verses). Neither the code nor this test run performed it. This is the single biggest gap between
   "the design as written" and "what actually happened" in the 10-verse test — worth deciding
   whether to build the enforcement, or to consciously scope it out, rather than leaving it silently
   unaddressed.

Six more note_types (`idiom`, `pronoun_resolution`, `noun_relational`, `noun_severity`, `chain`,
`recurrence_role_shift`) have real, working quality-gate code but **zero occurrences** in this
10-verse sample — not because anything is broken, but because this pass's own analytical depth was
deliberately modest (stated at the top of the 10-verse report) and didn't reach for them. `chain` in
particular had two live opportunities (`Gen.46.18`, `Ps.94.22`'s own `narrative_morph` hits) that
went unused.
