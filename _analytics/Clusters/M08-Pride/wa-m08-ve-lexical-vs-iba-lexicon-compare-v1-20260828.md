# M08 — old ve-lexical extract vs current iba.db lexicon — compare — 2026-08-28

> Escalation #1005, continued. Compares `Data/wa-ve-lexical-extract-M08-20260621-b1of2/b2of2.json`
> (the source that fed the June-21 `findings/` characteristic distillation) against the current
> `iba.db` lexicon (`Data/wa-m08-lexicon-evidence-extract-v1-20260828.json`, built this session).
> Confirms the researcher's expectation directly: there's real drift, and it's not one thing —
> three separate, independent gaps stack on top of each other.

## 1. Coverage — the term inventory has grown ~89% since June 21, and it's mostly real content

The old extract's own meta: 253 verses, 292 focus occurrences, **46 distinct M08 (`focus_cluster`)
Strong's numbers** — matches its own obslog exactly ("253 verses; 292 focus occurrences; 46
distinct lemmas").

`iba.db`'s current `cluster_strong` table carries **87 strongs tagged M08** — and **all 46 of the
old set are a strict subset** (zero loss, zero drift on the original 46). The other **41 are new**,
added since June 21. Classified by gloss:

| group | terms | example glosses |
|---|---|---|
| **mockery family** | 10 | mock (×8 distinct Hebrew/Greek lemmas: `lits`, `la.ag`, `qa.las`, `ta.a`, `muq`, `a.lal`, `ha.tal`, `empaizō`, `katagelaō`, `muktērizō`), derision (×2) |
| **boasting-verb family** | 5 | `katakauchaomai`, `megalaucheō`, `enkauchaomai`, `perpereuomai`, `aucheō` |
| **height/majesty family** | 7 | `hupsos`, `megalōsunē`, `megaleiotēs`, `hupsōma`, `el.yon`, `sa.gav`, a second Strong's# for `rum` (H7314) |
| **other proud/arrogant/haughty/domineering adjectives** | 17 | `huperonkos`, `huperairō`, `a.taq`, `shal.lit`, `ya.hir`, `kenodoxos`, etc. |
| **likely mis-tagged (noise, not content)** | 2 | **H6965B `qum`** "to arise: rise" — the generic Hebrew verb for ordinary physical standing/rising, 376 occurrences, almost certainly too broad for a pride-specific tag on the strength of shared root-family with `rum`; **G1065/G4007 `ge`/`per`** — Greek emphatic particles ("indeed"), T2-grammatical function words the old extract's own conventions explicitly excluded ("T2-GRAMMATICAL... EXCLUDED from generation/this extract/reads") |

**So the June-21 corpus wasn't complete even on its own terms at the time** — a whole mockery
sub-family and several boasting/height variants existed in the text and were simply never brought
into that read at all, independent of anything about backfill or harvest status.

**Harvest-status split of the 41 new strongs** (same pattern found project-wide earlier this
session): 20 are `origin='word'` (properly registered, 13 with verse coverage already); 21 are
`origin='backfill'` (no `word_registry` link, **zero** verse coverage — including `hupsos`
"height," 111 occurrences, a genuinely core M08 term sitting entirely unharvested).

## 2. Depth — the old extract carries a real per-verse interpretive read; `iba.db` currently doesn't

The old extract's `lexical` block per occurrence: `sense`, `lemma_meaning`, `type`, `location`,
`faculty`, `object`, `object_type`, `experiencer`, `divine_involvement`, `compound` (co-occurring
terms in the same verse) — and per its own meta, **the interpretive fields (`cause`, `location`,
`divine_involvement`, `object_type`, `valence`) were RESOLVED verse-by-verse by a governed
verse-read API pass**, not mechanically derived: "batched-by-verse, circuit-breaker, cost-cap,
self-verified... 0 M-cluster residue" (i.e. every occurrence was actually read, none left
unresolved). The extract's own `engine_changes` log documents real engineering rigor behind it: a
foundational zero-pad matching bug found and fixed, a full corpus re-derivation (38,971
term-in-verse units) after that fix, a T2-noise filter pass, and a signal-list completeness audit.

**`iba.db`'s current `verse_lexical` (L4b) is deliberately mechanical-only** — by its own `cfg_table`
description: "the mechanical T1-T3 reading: role classification + stem/voice-selected sense +
named-not-resolved ambiguity... never by re-deriving from span/strong/strong_meaning_parsed
directly" (downstream T4+ work is meant to build on it later). Checked directly this session:
`resolved_sense` is constant per strong+stem (varies only with Hebrew binyan/Greek voice, not with
verse content) — confirmed there is **no `location`, `faculty`, `object`, `divine_involvement`, or
`compound` field anywhere in `iba.db`'s current lexicon layer**. The old extract's interpretive
depth has no live equivalent in `iba.db` today, for any of M08's 87 terms — old 46 or new 41 alike.

## 3. What this means — three independent gaps, not one

"Marrying the findings" turns out to mean reconciling three separate things, each with a different
fix:

1. **Two characteristic sets never reconciled** (already found: old May 5-way split vs. new June
   7-way split, both live in the DB, nothing marking either superseded).
2. **The June characteristic set's own term corpus is 47% short of the current M08 assignment** —
   41 strongs added since, ~95% of them genuinely relevant content (mockery, boasting, height
   families) never read at all, plus 2 likely mis-tags that should probably be reviewed for removal
   rather than harvested.
3. **The interpretive depth the June read achieved (verse-level sense/location/faculty/divine-
   involvement, not just dictionary gloss) doesn't exist in `iba.db` for any M08 term yet** — the
   current base layer stops at the mechanical stem-reading; the researcher's "big shift into span/
   verse context" rebuilt the mechanical foundation cleanly (§0 of the earlier stream-robustness
   assessment: ~100% verse/lexical coverage everywhere) but hasn't yet re-run the kind of governed
   verse-read pass that produced the old extract's richer fields.

None of this makes the June-21 work (or the May work) worthless — both are real, checkable
analysis, and gap 2's new terms are themselves evidence the underlying M08 vocabulary is coherent
(mockery and boasting are obviously pride-adjacent). But it does mean a straight "load the old
findings into the DB" harvest would be reconciling against a term inventory and a lexical depth
that have both already moved past what those findings were built on.
