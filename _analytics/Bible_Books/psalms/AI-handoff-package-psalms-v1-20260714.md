# AI handoff package — Psalms macro pass, round 2 (inputs)

**Date:** 2026-07-14 · **For:** the analyst continuing from `WA-session-log-psalms-macro-v1.0-2026-07-14.md`.
This package supplies everything the round-1 log requested (§7) and records the source-fixes made in response.

---

## What changed since round 1 (do not re-derive these)

- **DQ-01 fixed at source.** The coupling(112)/locus(116) transposition you found (span 268779 et al.) is corrected — **666 Psalms spans** swapped; `locus` is now a clean enum. Your in-analysis normalisation is no longer needed; re-pull the projection. **No `.json` patch for you to issue** — done.
- **Projection regenerated at v2.** Same four files **plus** `psalms_qualifiers.csv`, and the `reading_view` now carries **`linked_qualifiers`** (54 cols).

## Your four requests — supplied

1. **Qualifier / standalone rows** → `outputs/projections/psalms/psalms_qualifiers.csv` (7,295 rows). Each links to its char via `linked_char_spans`/`linked_char_refs` where an explicit pair exists (296 rows); otherwise associate by `verse_ref`. Also surfaced per-char in `reading_view.linked_qualifiers`.
2. **The verse universe** (the denominator you refused to assert — correctly; here it is from the data):

   | book | verses | chapters | verses with ≥1 characteristic | coverage |
   |---|---|---|---|---|
   | Psalms | **2,461** | 150 | 1,329 | **54.0%** |
   | Psalms **ex-119** | 2,285 | 149 | 1,190 | 52.1% |
   | Psalm 119 alone | 176 | 1 | 139 | 79.0% |
   | Proverbs (contrast) | 915 | 31 | 807 | 88.2% |

   Note: coverage is *verses carrying a characteristic*, not a quality claim. The Psalms/Proverbs gap (54% vs 88%) is itself an observation — Proverbs is denser in inner-being terms per verse.
3. **Companion spec** → `Workflow/methodology/WA-projection-schema-and-companion-spec-v1-20260714.md` (schema §C–§G, incl. base-vs-nuance §G and the NONE/ABSENT rule).
4. **Proverbs projection** (contrast control) → `outputs/projections/proverbs/` (v2, same five files).

## Psalm 119 control (your step 1)

Filter `chapter == 119` on any file (the `chapter` column is present throughout). Ex-119 denominators are in the table above. 119 is 176/2461 = 7.2% of verses but 244/2168 = 11.3% of readings — it *is* over-weight; stratify before trusting any unstratified figure.

## Researcher's answers to your Q-1…Q-4

- **Q-1 (`effect` 97.7% NONE):** treat as a **derived floor, not measured genre-silence**. `effect` (and to a lesser degree `intensity`/`specifier`) is derived from the reading prose, so `NONE` conflates true silence with under-reading. **`device` and `direction` are trustworthy; `effect` is not yet.** A real book-level `effect` read is scheduled (Phase-2). Use `linked_qualifiers` + `qualifiers.csv` to test any specific `effect=NONE` before building on it — 245 `effect=NONE` chars carry a linked qualifier and are now auditable.
- **Q-2 (transposition):** fixed at source (see above).
- **Q-3 (unit):** **readings** is the governing unit; characteristics/lemmas are roll-ups available on demand. Coverage now expressible against the verse universe.
- **Q-4 (next move):** ~~pursue (ii) the faculty↔inward asymmetry~~ — **superseded by round 2 (below)**.

## Round-2 corrections (2026-07-14) — after the analyst tested the target

The round-2 pass broke its own I-3 finding and exposed a reliability gap my first assessment missed. Recorded honestly:

- **I-3 (faculty↔inward) is RETRACTED.** It rested on `type(102)`, which the band-drift screen shows **records the reading order, not the text** (`type=faculty` only exists Ps 76+; `action` 0% in Ps 1–25). See `WA-dimension-reliability-register-v1-20260714.md`.
- **`type(102)` — do not use** for positional/cross-section/whole-book work. **`locus(116)` unreliable for Ps 1–25** (blanket 100% internal:ib-state early convention). Both now flagged in the preamble.
- **M-01 SURVIVES and is the real finding:** seat-words (leb/lebab/nephesh/ruach), grounded on **lemma** (not type), read `inward` ~27× above other lemmas and `static` far below, stable across all bands, non-tautological (God-ward seat-readings tag `toward-god`). This is the structural-movement claim to build on — it uses `direction` (stable) + `lemma` (invariant).
- **DQ-05:** Psa 86:12 vs 111:1 (identical heart/give-thanks/whole-heart) tag `inward` vs `toward-god` — ~20% direction inconsistency on that subset; bounds M-01, doesn't overturn it. Direction-consistency audit scheduled.
- **Qualifier-layer honesty:** only **4.1%** of qualifier rows (296/7,295) and **11.6%** of readings (251/2,168) carry an explicit char-link — a real audit trail for those; the rest is `verse_ref` inference, not a link.

## Standing caveats carried forward

- `NONE` (assessed) ≠ `ABSENT` (unread) — the first rule.
- The three layers (lemma base_gloss / meaning-in-context / occurrence) — unchanged.
- **Reliability is two-axis** (stability + provenance) — see the register. `direction`/`device` trustworthy; `effect`/`intensity`/`specifier` derivation-grade; `type` reader-drift; `locus`/`target` partial.
