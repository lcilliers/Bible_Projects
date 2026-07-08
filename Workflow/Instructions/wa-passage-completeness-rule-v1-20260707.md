# Passage completeness rule (reading-unit repair) — REUSABLE per book (v1)

> **⚠ SUPERSEDED 2026-07-08 by `wa-passage-completeness-rule-v2-20260708.md`.** v1 scoped passages by **verse-record**; v2 scopes them by **candidate characteristic** (the seed on the master) and makes candidate-without-verse-record a **DB integrity violation to repair**. Retained for provenance only — do not use for new work.
>
> Deterministic rule for step (b) of the per-book corrective method (`wa-per-book-corrective-method-authoritative-v1-20260707.md`): confirm/rework the passage reading units so every IB-relevant verse is captured, with no semantic guessing. Approved by the researcher 2026-07-07 (proven on Proverbs). **Use this same rule for every book.**

## Principle
- A passage is a **reading unit**: it captures verses with **IB content**, read in the context of adjacent verses.
- **Every verse that has a verse-record must belong to a passage.** A verse-record exists only for a registered IB term occurrence, so a verse with a verse-record is IB-relevant and must sit inside a reading unit.
- **Verses with no verse-record stay excluded** — they carry no IB content and are correctly outside any passage. They are *not* gaps.

## Scope (per book)
Verses where **`passage_id IS NULL`** AND there exists at least one **active `wa_verse_records`** for that verse.

## Procedure
1. Take the scope verses; **group consecutive verses (within a chapter) into runs** (the natural reading unit — never split a consecutive run).
2. For each run, look at the verse immediately **before** its first verse and immediately **after** its last verse:
   - **Adjacent to exactly one existing passage** (the before-verse is in a passage XOR the after-verse is in a passage) → **merge the run into that passage** (extend its end, or prepend to its start).
     - On a **prepend**, the passage's anchor moves to the run's first verse (`is_passage_anchor`, `passage.anchor_verse_id`, `start_chapter`/`start_verse`, `ref`, `verse_count` all updated).
     - On an **extend**, update `end_chapter`/`end_verse`, `ref`, `verse_count`.
   - **Between two passages** (both neighbours in passages), **or isolated** (neither neighbour in a passage) → **create a new passage for the run** (its own single- or multi-verse reading unit; first verse is the anchor).
3. **Between-two default is "own passage" on purpose** — choosing which neighbour a between-run belongs to is a *reading* judgment (step c), so step (b) does not guess it; it gives the run its own unit and leaves any semantic merge to the reading.

## What gets written / what does not
- **Write:** `passage` table (extend/prepend existing rows; insert new rows with a `source` tag marking the reading-unit repair, e.g. `readingunit-fix-2026`); `verse.passage_id` for every scope verse; `verse.is_passage_anchor` for the anchor of each new/prepended passage.
- **Do NOT write:** `ve_lexical`, `wa_verse_records`, `verse_span_index` — the schema is **normalized**: none carry a passage column; they all track the passage via `verse.passage_id`, so they propagate automatically.

## Governance
- **Integrity-gated:** backup → `_check_integrity_controls --snapshot` pre → apply → snapshot post → `--compare` (expect only passage/verse.passage_id deltas; no new invariant breach).
- **Re-check:** after applying, **0** verse-record verses may remain with `passage_id IS NULL`.
- **Per book only.** No cross-book operation.

*Recorded 2026-07-07. Tool: `scripts/_apply_passage_completeness_v1_20260707.py --book N` (dry-run first).*
