# Psalms base-source data note — coupling (112) / locus (116) transposition

> **Status:** open data-quality finding, filed 2026-07-12. Surfaced independently by 6+ narrative-generation agents during the Psalms narratives rollout (batch 5), then verified directly against the base sources. **Not fixed** — this needs a base-source/DB-level decision (see §4). The narratives are unaffected in substance (see §3).

## 1. The finding

In the Psalms family **base sources** (`verse-analysis/psalms/_base-sources/psalms__*.json`), dimension **112 (coupling)** and dimension **116 (locus)** carry each other's values in a large block of rows:

- **112 (coupling)** holds a *locus*-type token — `internal:ib-state`, `external:god`, `external:person`.
- **116 (locus)** holds a *coupling*-type phrase — `"paired with …"`.

The correct mapping (per `meta.dimension_frame` and the worked examples in `wa-narrative-style-instruction-v1-20260702.md`) is the reverse: coupling = the "paired with / welded to" binding; locus = the `internal:/external:` classification.

## 2. Extent (verified directly, not just agent-reported)

Scan of all 46 base sources, rows with both 112 and 116 present (2,168 rows):

- **666 rows show the transposition signature** (112 starts with `internal:`/`external:`).
- Psalm range of swapped rows: **Psa 89 – 138**. It **begins at Psa 89** — 652 of 666 are Psa ≥90; the remaining 14 are all Psa 89; **none below Psa 89**.
- It is **not** a clean "everything from Psa 89 is swapped": rows ≥90 split 652 swapped / 362 not. So from Psa 89 onward a *majority but not all* of rows are affected.
- It spans **all 46 families** (the block is reference-driven, not family-driven): e.g. praise 67, inner-seat 50, joy 33, blessing 32, thanksgiving 31, prayer 32, fear-of-god 24 … down to torah 1.

The reference-gated onset (starts exactly at Psa 89) points to a contiguous block of the reread coding, most likely written with the two columns swapped in the underlying `ve_lexical` rows for that block — or transposed by the export in `_produce_family_passage_base_source_v2_20260712.py`. **Root cause not yet isolated.**

## 3. Impact on the narratives (batch 5 + the 34 earlier families)

**Substantively low.** Every narrative-generation agent that hit the block detected it and read each field **by its semantic content** (treating an `internal:ib-state` value as the locus and a `"paired with …"` value as the coupling), rather than mislabelling. So the prose in `_narratives/*.md` and the `narrative`/`story` text is grounded correctly. The 34 families committed before this session share the same base-source quirk and were written the same way.

The residual risk is only if the transposition is ever consumed **programmatically** (e.g. a future patch that loads 112 as coupling and 116 as locus verbatim into the DB) — that path would ingest swapped values. Guard any such loader until §4 is resolved.

## 4. Recommended follow-up (needs researcher decision — do NOT auto-fix)

1. **Isolate root cause:** check whether `ve_lexical` rows for Psa 89+ hold 112/116 swapped in the DB, or whether the swap is introduced by the base-source generator. Query a few known rows (e.g. Psa 106:29, Psa 112:10) against `ve_lexical` directly.
2. If the DB is wrong: a targeted repair patch on the affected `ve_lexical` rows, then **regenerate the base sources** (`_produce_family_passage_base_source_v2_20260712.py --all`).
3. If only the generator is wrong: fix the field mapping and regenerate; DB untouched.
4. After regeneration, re-run the narrative verifier gate (`scripts/_check_family_narratives_20260712.py --all`) and spot-check that any narrative clause that leaned on 112/116 still reads correctly. Because the agents read by content, most narratives should need no change.

## 5. Provenance

- Reported by agents for: turning-repentance, worship-prostration-service, speech-mouth-tongue, walk-way-conduct, violence-cruelty, wisdom-folly-teaching, wickedness-ungodliness, sin-guilt-iniquity, trust-refuge-security (the sin-guilt agent gave the tightest bound: "Psa 94:23–130 except 119:11 & 119:133").
- Verified directly here: onset at Psa 89, 666/2,168 rows, all 46 families.
- Session: 2026-07-12 Psalms narratives rollout completion (see the session log of the same date).
