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
- **Q-4 (next move):** pursue **(ii) the faculty↔inward asymmetry** — the most testable structural-movement claim — but first apply the Ps-119 stratification and cross-check against Proverbs.

## Standing caveats carried forward

- `NONE` (assessed) ≠ `ABSENT` (unread) — unchanged, still the first rule.
- The three layers (lemma base_gloss / meaning-in-context / occurrence) — unchanged.
- `effect`/`intensity`/`specifier` are **derivation-grade**, not read-grade, until the Phase-2 effect read lands.
