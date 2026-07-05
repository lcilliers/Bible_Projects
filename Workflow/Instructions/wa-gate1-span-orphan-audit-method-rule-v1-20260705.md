# Method rule — Gate 1 (span-orphan audit) is STEP 1 of every book's span-depth work

> **Status:** authoritative method rule, added 2026-07-05 after the Torah Gate-1 oversight (Genesis/Exodus/Leviticus span-depth work was built from the curated `wa_verse_records` term-seed and so silently missed inner-being words that were never registered as terms — `ahev` LOVE, `gaal` REDEEM, `lachats` OPPRESS, `avaq` WRESTLE, and others). This rule closes that gap at source. It operationalises the standing principle [[feedback_term_coverage_cascade_is_index_not_census]] — **the registry is a SEED, not a census.**

---

## The rule

**Before** any span-depth reading, coding, or synthesis of a book (or before finalising one already done), run the **Gate-1 span-orphan audit**: diff the book's **full word index** (`verse_span_index`, every word of the text) against the **curated inner-being term-seed** (`wa_verse_records` for that book), and review the *un-registered* content-words for inner-being relevance. Any genuine inner-being term the seed missed must be **captured** (coded / read at span depth) and **onboarded** to `mti_terms` so it is registered for every book thereafter.

Gate 1 is **step 1**, not a post-hoc check. The seed tells you where the *known* terms are; the index tells you where the *unknown* ones hide. You cannot claim span-coverage of a passage's inner-being life from the seed alone.

## The tool

`scripts/_probe_gate1_span_orphans_v1_20260705.py --book <Name>` — read-only. Prints, per un-registered content-strong, gloss + frequency + first verse, gloss-filtered to surface inner-being candidates (`--all` for every un-registered word). Human review strips false positives (king, livestock, place-names, architectural terms). Output feeds the coding/reading.

Onboarding recovered terms: `scripts/_apply_gate1_term_onboard_v1_20260705.py` (pattern — assign each recovered strong to its cluster, insert into `mti_terms` with `anchor_note` documenting the recovery).

## Status by book (2026-07-05)

| Book(s) | Gate-1 status |
|---|---|
| Wisdom / Poetry / Prophets (Psalms, Proverbs, Job, Isaiah, Jeremiah, Ezekiel, the Twelve…) | **RAN** (`lexical-model-2026` index scan; the poetic/prophetic reading method queries `verse_span_index` directly — index-driven, sound) |
| Leviticus | **RAN + FIXED** (13 terms recovered incl. `ahev` 19:18, `deror` 25:10, `gaal`; coded into `ve_lexical`) |
| Genesis | **RAN 2026-07-05** — recovered vocab onboarded + folded into the 4 cycle syntheses; per-reading codas outstanding |
| Exodus | **RAN 2026-07-05** — recovered vocab onboarded + folded into the deliverance & sinai-covenant syntheses; per-reading codas outstanding |
| **Numbers, Deuteronomy** | **NOT RUN — run the scan FIRST when these books are reached** (they have no gate-1; do not read them from the seed) |

## Why this matters (the failure it prevents)

The Torah span-depth readings were built off `wa_verse_records`, which only contains *registered* terms. `gaal` "redeem," `ahev` "love," `lachats` "oppress," `avaq` "wrestle," and ~24 others were **never registered**, so they were invisible — the readings could gate-check as "complete" while missing the single most important inner-being word in a passage (love at the Aqedah; wrestle at Peniel; redeem in the exodus). The index-vs-seed diff is the only thing that surfaces a *word you don't know you're missing.* It is not optional.

*Filed 2026-07-05. Companion to the Gate-1 audit report (`verse-analysis/leviticus/_reports/wa-gate1-audit-and-scope-20260705.md`) and the Gen/Exod recovery work-list (`verse-analysis/_gate1-recovery/wa-gen-exod-gate1-recovery-20260705.md`).*
