# Morph backfill gap — programme-wide (not M47-only)

> Prompted by the M47 observation (mode assessment, 2026-06-14): *"Important observation that M47 morph backfill is missing. Are there others also."* Answer: **yes.** The gap is systemic and term-level, M47 is simply the largest and most recent slice. Every figure below is a live query against `database/bible_research.db`.

## The finding

**69 content terms across 14 clusters are fully un-morphed** — `wa_verse_records.morph_code`/`stem` NULL on **every** active occurrence (3,436 occurrences total). It is **term-level, not scattered**: only 6 other occurrences are partially missing. So it is a clean, bounded set — "these specific terms were never tagged," not "morph is patchy everywhere."

| measure | value |
|---|---|
| programme-wide clustered active term-occurrences | 58,830 |
| …with no morph_code | 27,724 (47.1%) |
| — of which **T2** (qualifier/function-word layer) | 24,282 (100% of T2 — separate question, see below) |
| — of which **M47** (Constitution seats) | 1,584 (100% of M47) |
| **content terms fully un-morphed** (non-T2) | **69 terms · 3,436 occurrences** |
| partially un-morphed content terms | 6 terms · 6 occurrences (negligible) |

### Which clusters (not just M47)
M47 holds 28 of the 69, but **13 other clusters** carry the rest:

`M47 ×28 · M26 ×11 · M25 ×5 · M22 ×5 · M44 ×4 · M23 ×4 · M03 ×3 · M05 ×2 · M04 ×2 · M30 ×1 · M28 ×1 · M27 ×1 · M34 ×1 · M39 ×1`

### These are real, high-frequency terms — not edge cases
H3820A *lev* (331) · H1285 *berith*/covenant (236) · H4941G *mishpat*/justice (208) · H3824 *levav* (207) · H1320 *basar*/flesh (205) · H8199 *shaphat*/judge (182) · H5315H *nephesh* (180) · G2588 *kardia*/heart (120) · H1431 *gadal* (114) · G2919 *krino*/judge (97) · G4561 *sarx*/flesh (85) · G4893 *suneidesis*/conscience (29) … Mix of **27 sub-entries (suffix-letter Strong's) + 42 base Strong's; 48 Hebrew + 21 Greek.**

## Root cause

`scripts/_apply_morph_backfill.py` ran in **four batches on 2026-06-08** (M01-live → batch4). The un-morphed terms were never in a batch:
- **M47 was created 2026-06-10** — *after* the last batch — so none of its seat-terms (heart/soul/flesh/conscience/nephesh) were ever offered to the backfill.
- The other 13 clusters' missing terms were likewise added to clusters, or split as sub-entries, outside the batched run.

**Not recoverable from inside the DB** — `wa_verse_term_links` has no morph/stem column; the original morph came from **STEP preview-HTML**. The fix must re-fetch from STEP (same source, same script).

## Why it matters (ties to the UNRESOLVED design)

Mode (#4) is bedrock *only where morph exists*. Under the new three-state model, every un-morphed occurrence resolves to **`UNRESOLVED`-mode** — "expected a mode, no morph available." This backfill is therefore the concrete worklist that moves **~3,436 content occurrences from `UNRESOLVED` → resolved mode**. It is the first real instance of the `UNRESOLVED`-as-backtrack-flag working as intended.

## Fix path (reusable, proven — no new script)

```
# dry-run first (reports STEP reference match-rate, the systemic-failure guard)
python scripts/_apply_morph_backfill.py \
  --clusters M47,M26,M25,M22,M44,M23,M03,M05,M04,M30,M28,M27,M34,M39 \
  --dry-run --out research/investigations/wa-morph-backfill-catchup-dryrun-v1-20260614.md
# then live
python scripts/_apply_morph_backfill.py --clusters M47,... --live --out <file>.md
```

The script is idempotent on already-morphed occurrences (same STEP morph), so re-touching the partially-covered clusters is safe.

## Open decision — T2 (24,282 occurrences)

All of T2 is un-morphed. T2 is the **qualifier/reference layer, never analysed standalone**, so mode matters less. But some T2 terms are **verb-like** (*na.vat* "to look", *ra.ah* "to see", *a.sah* "to do") and would carry a real morphology. **Decision for the researcher:** backfill T2 too (completeness, and the verb-like qualifiers gain a mode), or leave T2 `UNRESOLVED`-mode by design (it is not a standalone analytical unit). Recommend backfilling — it is the same one command (`--clusters ...,T2`) and removes a 24k-row blind spot.
