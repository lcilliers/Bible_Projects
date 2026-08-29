# `finding` → verse/term: new direct index, staged plan

Responding to your correction: route straight to `iba.verse`/`iba.strong`, retire the old
incomplete index, add a text-mining pass for references embedded in the finding text itself.
`verse_context`/`wa_verse_records` are already `inactive=1` in `cfg_table` — confirmed, no action
needed there; they're used here only as a one-time READ source to backfill the new index, never as
an ongoing dependency.

## Term side — simpler than expected, mostly done in one query

`mti_terms.strongs_number` → `iba.strong.strongNumber` resolves **435,169 of 435,193** VERSE-level
`finding` rows (99.99%) — checked directly, not assumed. The text-mining fallback you asked for is
real but tiny: **~24 rows**, not a major undertaking. Plan: new column or link (your call on shape,
same question as before — I'd lean toward the same row as the verse link) populated from this
join for the 435,169; the 24 stragglers get the text-mining pass; then drop `finding.mti_term_id`.

## Verse side — new table, three backfill passes

**New table** (name TBD — suggest `finding_verse_index`, retiring `finding_verse_link` alongside
`verse_context`/`wa_verse_records`): `id`, `finding_id` → `finding.id`, `verse_id` → `iba.verse.id`,
`reference_text` (preserved, human-readable), `source` (`structural` | `finding_verse_link` |
`text_mined`), `created_at`. Proper M:N — no uniqueness constraint forcing one verse per finding or
vice versa, per your instruction.

**Pass 1 — structural** (the 435,193 VERSE-level findings' primary verse): resolve
`verse_context_id → verse_context.verse_record_id → wa_verse_records.id → wa_verse_records.
verse_id → iba.verse.id`, ONE TIME, writing the resolved `iba.verse.id` straight into the new
table. ~93% of `wa_verse_records` rows have `verse_id` populated, so this pass won't reach 100% —
the gap gets picked up by pass 3 if the finding text also happens to name its own verse (likely,
given the sample content).

**Pass 2 — migrate `finding_verse_link`'s existing 3,659 rows.** Its own `cfg_table.use` already
documents the real shape: 3,586 "anchor" rows carry only `reference` text (no usable id at all),
73 "support" rows have a `verse_record_id` that — checked live — doesn't reliably resolve anywhere
(2% match rate against `wa_verse_records`, and the handful matching `iba.verse.id` by coincidence
are confirmed wrong-verse matches). So this pass resolves via **`reference` TEXT**, not the numeric
column, for all 3,659 rows — same matching mechanism as Pass 3, just against already-flagged data.

**Pass 3 — text-mine every finding's own content** (all 458,096 rows, not just the ones lacking a
structural link — the sample content already shows findings naming several OTHER verses beyond
their own anchor, e.g. one finding citing "Psa 11:5", "Isa 1:14", "Hos 9:15", "Pro 8:13", "Psa
97:10", "Psa 139:21" — six references in one row). Needs:

- A verse-reference regex (book abbreviation + chapter:verse, comma-separated lists, ranges).
- Book-abbreviation normalisation — `book_code_variants` (112 variant codes → 66 books) already
  exists and is exactly this lookup, but it bridges into `bible_research.db`'s own `books` table,
  not `iba.verse` directly — one more hop needed to land on `iba.verse.reference`/`osisId`'s own
  book-prefix convention (confirmed live: `osisId` and `reference` don't even use the same
  abbreviation for the same book — e.g. `1Tim.1.5` vs `1Ti 1:5` — so the matching target itself
  needs picking, not just the source normalisation).
- A decision on ambiguous/malformed matches (a chapter:verse that doesn't exist, a book
  abbreviation that doesn't resolve) — log and skip, or flag for review?

This pass is the real engineering, and the one most likely to produce a large row count (multiple
references per finding × 458k findings) — worth a row-count estimate from a sample run before
committing to the full pass.

## Sequencing

1. Build the new table + Pass 1 (cheap, fully mechanical, verified chain).
2. Pass 2 (small, 3,659 rows, same matching mechanism Pass 3 needs — good place to prove the
   reference-matching logic works before running it at Pass 3's scale).
3. Design + sample-test Pass 3's regex/normalisation on a small slice, show you the match rate and
   some real examples, before running it against all 458k rows.
4. Term side: the 435,169-row join (fast), then the ~24-row text fallback.
5. Only once all of the above are verified: drop `finding.verse_context_id` and
   `finding.mti_term_id`; mark `finding_verse_link` inactive (not dropped).

**Not started yet** — this is the plan. Confirming before I build: the new table name/shape, and
whether you want Pass 3 built and sample-tested first (my recommendation) before committing to a
full run.
