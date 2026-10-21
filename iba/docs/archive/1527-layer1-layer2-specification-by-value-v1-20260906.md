# Layer 1 / Layer 2 — itemized specification, by value produced

- **filename:** 1527-layer1-layer2-specification-by-value-v1-20260906.md
- **date:** 2026-09-06
- **escalation:** #1527
- **status:** Extracted from the actual design-decision documents (not the code, not live data) —
  `1383-verse-lexical-window1-method-and-drift-mitigation-v1-20260903.md` (the origin of the
  Layer 1/Layer 2 split itself), `1383-verse-lexical-window1-capture-design-vs-study-purpose-
  v1-20260903.md` (checked against Window 2's actual needs), `1383-verse-lexical-window1-full-
  build-specification-v1-20260904.md` (the operationalized final spec), and `1451-window1-layer2-
  verse-scoped-redesign-v1-20260905.md` (the most recent correction to Layer 2's own reach). Each
  item below is sourced to the document it comes from. Where the design changed between the
  original proposal and the final build, both are shown — that movement is itself part of the
  record, not smoothed over.

---

## The governing principle — Layer 2 reads Layer 1, and only Layer 1 (plus itself)

Stated most precisely in the method-and-drift-mitigation doc (§2): *"Layer 1's output is the input
to this layer, not something re-derived by hand each time... there is no 'row I didn't get to,'
only 'row I looked at and made a call on.'"*

**Corrected and sharpened later, #1451 (2026-09-05):** Layer 2 may read **adjacent verses' own
Layer 1 data** when a single verse's own Layer 1 can't settle something (a pronoun's referent, a
chain's continuation) — but this is a **targeted, one-verse-at-a-time read**, never a passage-wide
build, and it must **never** touch a Window 2 object (`passage`, `hib`, `phenomenon`, `operation`)
— *"Window 1 categorically does not consider or determine inner-being value... requiring any
Window-2 object as a prerequisite for a Window-1 write... is a category error."* If even a
targeted adjacent-verse read can't resolve something, that is recorded explicitly as
`resolution_status='unresolved'` — never guessed, never silently left ambiguous.

So: **Layer 2's read boundary = Layer 1 (this verse, or an adjacent verse's Layer 1 if genuinely
needed) — never Window 2, never a passage-scoped structure.** The original full-build-spec's
`passage`-gated version of Layer 2 (§C.2 of the 2026-09-04 spec) is **superseded** by this
correction, made one day later.

---

## Layer 1 — mechanical facts, one value per code, computed unconditionally

### As originally conceived (method-and-drift-mitigation doc, §2, 2026-09-03) — 5 items

| # | Value produced | Deterministic from |
|---|---|---|
| 1 | Same-code, different-gloss data-quality flag | `strong`, compare glosses within the verse |
| 2 | Hebrew narrative-morph flag (wayyiqtol) | `morph_code` pattern |
| 3 | Negator flag | a small, explicit, evidence-built code lexicon |
| 4 | Connective type (causal / coordinating / purpose) | a small, explicit, evidence-built code lexicon |
| 5 | Related-words, full pull | `strong_related`, every content-role code |

### As it landed in the operationalized build spec (2026-09-04) — the actual final column set

| # | Value produced (`verse_lexical` column) | What changed from the original 5 |
|---|---|---|
| 1 | `role` (content / function) | present from the original T1-T3 baseline, not new to this round |
| 2 | `resolved_sense` (stem/voice-narrowed sense) | baseline T1-T3, not new — **but see the open flag below** |
| 3 | `ambiguity_note` | baseline T1-T3, not new |
| 4 | `gloss_consistent_in_verse` | = original item 1, promoted to a real column |
| 5 | `narrative_morph` | = original item 2, promoted to a real column |
| 6 | `is_negator` | = original item 3, promoted to a real column |
| 7 | `party_kind` (divine/human/non_human) | **new** — not in the original 5 at all |
| 8 | `position`/`surface`/`language`/`testament` (denormalized) | **new** — not in the original 5; came from the separate `capture-design-vs-study-purpose` doc's language/testament ask and general denormalization convenience |
| — | ~~Connective type~~ | **moved to Layer 2** — the final spec makes `connective` a `verse_lexical_note` note_type (judgement-bearing: "value_text must be one of the three connective classes, or UNCLASSIFIED"), not a Layer 1 column, contrary to the original proposal listing it as mechanical |
| — | ~~Related-words, full pull~~ | **moved to Layer 2** — the final spec makes `related_word` a `verse_lexical_note` note_type ("every content-role code gets a full, unconditional strong_related pull as note_type='related_word' rows... the pull is mechanical/total; same-concept-vs-coincidental sorting is Layer 2"), i.e. the *pull* stayed mechanical in spirit but the *storage* is a Layer 2 note row, and the *sorting* of its results is explicitly judgement |

**A live open question flagged in the design phase and, as far as this document trail shows, never
followed up before the build proceeded** (`capture-design-vs-study-purpose`, §5, §8 item 3,
2026-09-03): across a 19-verse validation sample, *"every single `resolved_sense` value was the
flat `stepGloss:` fallback form — not one narrowed sense was observed."* The document explicitly
asks whether this is sample coincidence or a systemic failure, and lists it as an open item needing
"a dedicated live check before build." No later document in this trail records that check having
been done. (Separately, and consistent with this: escalation #1527, raised today, found the same
fallback pattern live and corpus-wide.)

---

## Layer 2 — judgement-bearing calls, per code, structured but never mechanized

### As originally conceived (method-and-drift-mitigation doc, §2, 2026-09-03) — 5 items

| # | Value produced | Nature |
|---|---|---|
| 1 | Idiom sense-selection | judgement |
| 2 | Related-word sorting (same-concept vs. coincidental) | judgement, over Layer 1's mechanical pull |
| 3 | Pronoun/entity resolution | judgement |
| 4 | Structural-pattern naming | judgement |
| 5 | Genre determination | judgement |

### As it landed in the operationalized build spec (2026-09-04 + 2026-09-04 addendum) — the final `note_type` enum, 13 values

| # | `note_type` | What it captures | Traceable to the original 5? |
|---|---|---|---|
| 1 | `idiom` | = original item 1 | direct |
| 2 | `pronoun_resolution` | = original item 3 | direct |
| 3 | `noun_relational` | **new** — not named in the original 5 (per `capture-design-vs-study-purpose` §1, supplies Window 2's "source vs. target of an operation" need) | new |
| 4 | `noun_severity` | **new** — not named in the original 5 | new |
| 5 | `chain` | **new** — sequencing/waw-consecutive chain, not named as a Layer 2 item originally (it appears as a Layer 1 *mechanical* signal, narrative_morph, feeding a Layer 2 *chain* judgement) | new as a distinct note_type |
| 6 | `connective` | **moved here** from the original Layer 1 list (see above) | moved, not new content |
| 7 | `related_word` | = original item 2 (sorting), with the underlying pull itself mechanical | direct, split mechanics/judgement |
| 8 | `polarity` | **new** — negation-as-a-structured-finding, beyond the mechanical `is_negator` flag | new |
| 9 | `entity_link` | = original item 3 (entity resolution, the non-pronoun case) | direct |
| 10 | `inert` | **new** — the explicit "checked, nothing to say" marker for function-role codes, part of the completeness discipline (§2's "fill in the judgement column or mark it not-applicable") | new, structural not analytical |
| 11 | `structural_pattern` | = original item 4 | direct |
| 12 | `recurrence_role_shift` | **new**, added in a later addendum (§B.18, 2026-09-04, per `1446`'s own gap analysis) — same code recurring in a verse with a genuine rhetorical role shift | new |
| 13 | `cross_lemma_shared_gloss` | **new**, same addendum — two different codes sharing an English gloss, confirmed as a real coincidence not a data error | new |

**Genre** — original item 5 — did **not** become a `note_type` at all. It landed as `passage.genre`,
a field on the (Window 2) `passage` table, set as "this read's own first move" before any
`verse_lexical_note` row is written (`one-integrated-read-genre-first` rule). **This is now itself
an open question** following #1451's verse-scoping correction: if Layer 2 no longer depends on a
`passage` row at all, `passage.genre`'s role as Layer 2's genre-capture mechanism has no clear home
— named as unresolved by #1451 itself ("`verse_lexical_note.passage_id`... needs a decision: drop
it, or repurpose it... not designed here").

---

## What this itemization does not include

Purely the specification, as the design documents state it — no live data, no code-vs-spec
comparison beyond what the source documents themselves already flagged as open (the `resolved_sense`
fallback question). The full column-by-column code-vs-rule comparison is the separate document
already filed: `1527-layer1-verse-lexical-definition-reference-v1-20260906.md`.
