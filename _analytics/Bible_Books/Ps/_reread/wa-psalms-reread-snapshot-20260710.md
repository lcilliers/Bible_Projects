# Psalms — re-read gate SNAPSHOT (delta vs baseline), 2026-07-10

> Book-wide gate assessment at **51 / 150 psalms re-read** under the corrected method (Screen 0 / verse-span depth / genre-aware ledger). Measures the whole Psalter as it now stands and deltas against the "before" in [`wa-psalms-reread-baseline-20260709.md`](wa-psalms-reread-baseline-20260709.md).
> **Runner:** `python scripts/_check_reread_measures_v3_20260709.py --book Psalms` (read-only). **Unit model = passage** (poetic/chapter-driven). Interpretation guidance: [`../_reports/wa-reread-measures-interpretation-guidance-and-crossbook-baseline-20260709.md`](../_reports/wa-reread-measures-interpretation-guidance-and-crossbook-baseline-20260709.md).

## Structure — before → now
| metric | 2026-07-09 baseline | 2026-07-10 snapshot | Δ |
|---|--:|--:|--:|
| verses | 2,461 | 2,461 | — |
| candidate char-spans | 4,768 | 4,768 | — |
| characteristics | 3,810 | 3,700 | −110 † |
| active lexical rows | 76,321 | 83,892 | **+7,571** |
| per-span `ve_nr` present | …no 103, no 116 | **+103 (source), +116 (locus)** | 2 dims now live |

† Characteristics fell because corrected-method re-reads **re-roled God-content spans** that the old `role-reassess-2026` pass had mis-called characteristics down to **qualifier/standalone** (Screen 0). Fewer, truer characteristics — not lost coverage.

## Gate results — delta
*failing now = items to correct; status ❌ if >0, ✅ if 0, ⏸ if not measurable.*

| gate | measure | 2026-07-09 | 2026-07-10 | Δ | status |
|---|---|--:|--:|--:|:--:|
| **G0** | passages > 12 char-spans | 150 | 159 | +9 | ❌† |
| **G1** | undecided spans / verses unprocessed | 0 / 0 | 0 / 0 | — | ✅ |
| **G2** | chars with no operation(106) | 1,847 | **1,160** | **−687** | ❌ (improving) |
| **G3** | ungrounded pairs / over-calls | 0 / 0 | 0 / 0 | — | ✅ |
| **G4** | recurring terms read identically | 4 | **2** | **−2** | ❌ (improving) |
| **G5** | cohesive units read in isolation | N/A‡ | N/A‡ | — | ⏸ |
| **G6** | candidate verses with no discovery | 976 | **654** | **−322** | ❌ (improving) |
| **G7** | content items with null value | 0 | 0 | — | ✅ |
| **G9** | (b) malformed pairs | 0 | **0** | — | ✅ (see fix) |
| **G10** | chars missing ≥1 mandatory dim | 3,810 (all) | **2,451** | **−1,359** | ❌ (improving) |
| **G10** | mandatory dims with ZERO rows | none | none | — | ✅ |

**Read:** every completeness/integrity gate is moving the right way. The re-read portion (51/150) now carries **full genre-aware ledgers** (drove G10 down 1,359, no-operation down 687, no-discovery down 322, and flattened-term reuse down to 2). The residual debt (2,451 incomplete ledgers · 1,160 no-operation · 654 no-discovery) is the **~99 not-yet-re-read psalms** under the old pass. G1/G3/G7 stay clean; source(103) and locus(116) are now populated where re-read.

## Pair-integrity fix applied this run (G9b)
The first run of this snapshot showed **G9b malformed pairs jump 0 → 5,219**, entirely from `reread-psalms-2026`. Root cause: the apply script (`_apply_reread_lexical_v1`) tagged **every** `k:'pair'` dim as `pair_kind='pair'`, including `res='none'` absent-dimension flags and `res='inferred'` single-anchor annotations — which have no second endpoint. The DB convention reserves `pair_kind='pair'` for `res='span'` two-endpoint relations (a *flag* kind already exists for noted-but-unresolved dims).

**Fixed (both the tool and the data):**
1. **Reusable script** — `_apply_reread_lexical_v1_20260709.py` now derives `pair_kind` from resolution: `res='span'` + both endpoints → `pair`; the owner span supplies a missing endpoint; `res` none/inferred → `flag`. Prevents recurrence on psalms 52–150.
2. **Data repair** (reread rows): 117 genuine span-pairs missing a `from` endpoint → owner span supplied; **5,102** none/inferred rows re-tagged `pair` → `flag`; 5 stray null-`pair_kind` discovery notes → `note`.

Result: `pair_kind='pair'` now holds only 1,343 genuine `res='span'` pairs; **G9b = 0**.

‡ **G5 / G9(a,c) still N/A** — the encoding guard samples pair endpoints book-wide and still hits the old `role-reassess` Strong's-encoded endpoints; these gates become measurable once enough of the book is re-read with span-id endpoints.
† **G0 genre caveat** unchanged — a "passage" is a whole psalm; whole-chapter poetic reading exceeds the 12-span budget by design, not a true failure.

## Success trajectory
On track against the baseline's success criteria: G2, G6, G10 trending → 0 as re-reading proceeds; G4 nearly clear; source(103)/locus(116) populated; G9b clean; G1/G3/G7 held. Next re-measure at the Book II close (Ps 72).

*Filed 2026-07-10, Psalms folder. Read-only snapshot (the pair-fix section records a one-time tool+data correction, committed to git).*
