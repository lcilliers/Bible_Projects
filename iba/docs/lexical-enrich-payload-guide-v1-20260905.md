# `lexical.enrich` payload — field-by-field guide

**2026-09-05.** Written because the ps-tools worksheet had one example row for `VerseLexical.ps1`,
it required a payload, and there was nowhere that said what a payload actually is. This is that
document — every field, every enum, a real worked example, and how to find the numbers a payload
needs. The worked example below is copied verbatim to
[`lexical-enrich-payload-example-rom-9-14-v1-20260905.json`](lexical-enrich-payload-example-rom-9-14-v1-20260905.json)
— point `-PayloadPath` at that file to run it as-is.

## What this payload is for

`-Step lexical.enrich` writes Window 1 **Layer 2** — judgement-bearing findings about the
mechanical Layer 1 reading (idioms, related-word families, connective classification, pronoun
resolution, and so on) — into `verse_lexical_note`. The analytical work (deciding what the finding
actually is) happens BEFORE this step, by a reading pass against the method docs; the payload is
that pass's decisions, structured so the step can validate and write them. It is not something the
script generates for you — you (or an AI reading pass) author it, then hand it to
`-PayloadPath`.

## Top level

```json
{
  "book": "Rom",
  "genre": "narrative",
  "notes": [ ... ],
  "remove": [ ... ]
}
```

- **`book`** — REQUIRED, must exactly match the `-Book` value the run is invoked with (a mismatch
  fails fast: `payload-mismatch`).
- **`genre`** — optional. As of the verse-scoped redesign (escalation #1451, 2026-09-05) there is
  no `passage` row to persist this against yet — supplying it does no harm but it is not saved
  anywhere; the run's own message says `(genre supplied but not persisted -- no per-verse home
  designed yet)` when you do. Fine to omit.
- **`notes`** — the actual findings, a list (shape below). At least one of `notes`/`remove` must be
  non-empty, or the whole payload is refused (`empty-payload`).
- **`remove`** — findings to retract, a list (shape below). Usually empty (`[]`) on a fresh pass.

## One `notes` entry

```json
{
  "verse": "Rom.9.14",
  "position": 3,
  "code_ordinal": 0,
  "note_type": "connective",
  "resolution_status": "resolved",
  "finding": "Part of the me genoito ('by no means') rhetorical-denial construction together with positions 7-8.",
  "evidence": "optional -- a supporting quote/citation, rarely needed",
  "target_verse": "Rom.9.14",
  "target_position": 8,
  "target_code_ordinal": 0,
  "related_codes": [
    { "verse": "Rom.9.14", "position": 7, "code_ordinal": 0 },
    { "verse": "Rom.9.14", "position": 8, "code_ordinal": 0 }
  ],
  "reconciliation_note": "only needed when this run is CORRECTING an existing note's content"
}
```

| field | required? | meaning |
|---|---|---|
| `verse` | always | OSIS reference of the word being annotated, e.g. `Rom.9.14`. |
| `position` | always | the word's position within the verse — see "finding position/code_ordinal" below. |
| `code_ordinal` | optional, default `0` | which code at that position, when a span carries more than one (rare — `0` covers the common single-code case). |
| `note_type` | always | one of the 15 live values below. |
| `resolution_status` | always | one of the 5 live values below. |
| `finding` | always in practice | the actual analytical text — what you found. Not schema-enforced as required, but a note with no finding text is not useful. |
| `evidence` | optional | a supporting citation/quote, when the finding needs one. |
| `target_verse`/`target_position`/`target_code_ordinal` | optional | names ONE other code this note is about — an idiom's other half, a pronoun's antecedent, etc. `target_code_ordinal` defaults to `0` like the source's own. |
| `related_codes` | optional | a LIST of `{verse, position, code_ordinal}` objects — for a note relating this code to several others (a connective's construction partners, a structural pattern's members). |
| `reconciliation_note` | required only when correcting | if this run changes what an EXISTING live note says (same verse/position/code_ordinal/note_type, different content), this field must explain why — the step refuses a content change with no note attached. |

### `note_type` — the 15 live values

`idiom` · `pronoun_resolution` · `noun_relational` · `noun_severity` · `chain` · `connective` ·
`related_word` · `polarity` · `entity_link` · `inert` · `structural_pattern` ·
`recurrence_role_shift` · `cross_lemma_shared_gloss` · `verb_argument` · `compound_unit` (newest,
escalation #1451 follow-up, 2026-09-05 — for a compound expression across multiple positions that
must be read as one integrated unit, not scored per-position).

### `resolution_status` — the 5 live values

`resolved` · `unresolved` · `unclassified` · `not_supported_this_language` · `checked_empty`
(the mandatory-pull-came-back-empty disposition, e.g. `related_word` found 0 genuine cognates).

## One `remove` entry

```json
{ "verse": "Rom.9.14", "position": 3, "code_ordinal": 0, "note_type": "connective", "reason": "why this note is being retracted" }
```

Same `verse`/`position`/`code_ordinal`/`note_type` addressing as a note, plus a required `reason`.
Retracts a currently-live note outright (soft-deletes it) rather than correcting its content.

## The reconciliation rule — every existing note must be addressed

This is the part that produces the most confusing error the first time: **every live note already
on the verse(s) being enriched must be accounted for by this exact payload** — repeated (unchanged
or corrected-with-`reconciliation_note`) in `notes`, or retracted in `remove`. A payload that's
silent about an existing note fails with `unreconciled` naming it. This is deliberate (§E.4 of the
original design spec) — it stops a partial/forgetful re-run from silently dropping prior findings.
If you're re-running enrich on a verse you already enriched before, start from the PREVIOUS
payload and add/adjust, don't write a fresh, shorter one.

## Finding `position`/`code_ordinal` for a verse

Run `-Step report.verse_lexical` (or `report.lexical_exceptions`) for the range first — it renders
every live Layer 1 code with its `position` and `surface` text, in order. That's what you're
annotating; `code_ordinal` is `0` unless the report shows more than one code sharing a position.

## The worked example

[`lexical-enrich-payload-example-rom-9-14-v1-20260905.json`](lexical-enrich-payload-example-rom-9-14-v1-20260905.json)
is the REAL payload used to enrich Rom.9.14 in this session's own 10-verse validation pass — not a
synthetic toy, already tested live and currently attached to that verse's actual `verse_lexical_note`
rows. It demonstrates: a plain `related_word` finding (position 0), an `unclassified` disposition
with the reason stated (position 2's `connective` — the 3-class connective lexicon has no
inferential class), a `checked_empty` disposition (position 3's `related_word`), a `related_codes`
cross-reference (position 3's `connective`, pointing at positions 7-8), and a `target_verse`/
`target_position` cross-reference (position 7's `idiom`, pointing at position 8). Run it with:

```powershell
.\iba\app\ps\VerseLexical.ps1 -Book Rom -Range 9:14 -Step lexical.enrich `
  -PayloadPath iba\docs\lexical-enrich-payload-example-rom-9-14-v1-20260905.json
```

(Already-live data — re-running it against the current DB should come back all-`unchanged`, not
`new`, since nothing about the verse has changed since it was written.)
