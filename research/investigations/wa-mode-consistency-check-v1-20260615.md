# Mode (#4) — database consistency check

> Researcher request (2026-06-15): *"check from the database that each verse has a value for mode and that it is consistent."* Scope = active term-occurrences in the analytical (clustered) scope: `wa_verse_records` joined to `mti_terms` with `cluster_code`, `delete_flagged=0`. Mode source = `morph_code` (+ `stem` = the Hebrew binyan). Read-only.

## Verdict: mode is present and consistent. Two tiny, understood residues — no actual inconsistency.

## 1. Coverage — essentially complete

| scope | total | with mode | missing |
|---|---|---|---|
| clustered active (incl T2) | 58,830 | 58,654 | **176 (0.3%)** |
| clustered active **excl T2** | 34,548 | 34,542 | **6 (0.02%)** |

The 176 without a value = **6 content terms** STEP returned no morph for (specific un-parseable verses) + **170 T2 particles** (function words — *not*, *from*, pronouns — which carry no morphology; correctly blank). Excluding the T2 function-word layer, coverage is **100% bar 6 occurrences**.

## 2. Consistency — clean

- **0** (term, verse) pairs with conflicting morph codes (each term-in-verse has exactly one mode).
- **0** stem ↔ morph contradictions: every Hebrew verb carries its stem; **no** non-verb carries a stem; every `stem` agrees with the binyan letter in its `morph_code`.

## 3. A false alarm I caught (worth recording)

The first pass flagged **1,293 "unparseable" morph codes** (e.g. `A-NSM`, `ANcfsa`, `AVqcc`). Investigation showed **most are not a data problem — my checker didn't know two valid patterns**:
- **`A-` Greek codes = adjectives** (Robinson scheme: `A-NSM` = Adjective Nominative Singular Masculine). 1,640 occurrences — *beloved* (G0027), *holy* (G0040), *gentle* (G4239), *godly* (G2318). **Correct and consistent.**
- **non-hyphenated `A…` codes = Aramaic** (`AVqp3ms`, `ANcfsa`) in Daniel / Ezra / Jer 10:11. **Correct morphology.**

So the "inconsistency" was in the verification parser, not the stored data. Logged here so it isn't re-raised.

## 4. Two genuine residues — mode *incomplete*, not inconsistent

1. **Aramaic verb stems not extracted (~210 occurrences).** Aramaic verbs (Dan/Ezr) carry a valid `morph_code` but `stem` is NULL, because the backfill's stem map (`_apply_morph_backfill.py` `HEB_STEM`) only fires on `H`-prefix codes. Their mode is present but missing the binyan refinement. **Fixable:** extend the stem map to the `A`-prefix (Aramaic) binyanim and re-derive `stem` for those 210 rows (no re-fetch needed — the morph_code is already stored).
2. **One Hebrew verb with an unmapped binyan letter:** Pro 27:15 `HVDp3ms` → `stem='?D'`. The `D` binyan isn't in the map. One occurrence; confirm what `D` denotes and add it.

## Recommendation
Coverage and consistency pass. The only action worth taking is the **Aramaic stem back-derivation** (210 rows, in-place from existing morph codes) + the single `D`-binyan lookup — small completeness fixes, not corrections. Optional and low priority; mode is sound for Hebrew + Greek (the bulk).
