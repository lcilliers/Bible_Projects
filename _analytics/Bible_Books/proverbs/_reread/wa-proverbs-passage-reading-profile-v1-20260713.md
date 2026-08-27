# Proverbs — passage reading profile (v1, 2026-07-13)

> **SUPERSEDED 2026-07-13:** this profiles the *maximal-run* v2 passages (104), later found to be BUNDLES and replaced by the CHAR-CONTINUITY rebuild — **701 passages** (626 single-verse; mean 1.1 verses / 3.0 candidate chars; max 10 = fool cluster). See `wa-proverbs-passage-method-bundle-finding-v1` and `wa-passage-completeness-rule-v2` (2026-07-13 amendment). The distributions below are the OLD (bundled) shape, kept for provenance.

> Profile of the v2 candidate-driven passages that will go through the Stage-4 read. Read-only; from `passage` + `verse_span_index.char_candidate` (book_id=20). Source of passages: `passage-build-2026`.

## Passages that will go through reading: **104**

Every one is a maximal run of consecutive candidate-bearing verses (non-candidate verses are outside all passages and are not read).

## a) Verses per passage

Total verses read = **799** · min **1** · max **35** · mean **7.7** · median **5**.

| verses | passages |
|---|--:|
| 1 (single-verse) | 18 |
| 2–4 | 32 |
| 5–9 | 26 |
| 10–19 | 19 |
| 20–35 | 9 |

## b) Candidate characters per passage

Total candidate chars = **2,123** · min **1** · max **129** · mean **20.4** · median **11**.

| candidate chars | passages |
|---|--:|
| 1–5 | 37 |
| 6–10 | 14 |
| 11–20 | 24 |
| 21–50 | 18 |
| 51–100 | 8 |
| 101–200 | 3 |

## The heavy tail — the F-frames (candidate chars ≥ 40)

16 passages carry ≥40 candidate chars; the top 11 exceed 50. These are the sentence-collection chapters (Prov 10–29) where nearly every verse is an independent proverb with its own char — the digestion concern flagged at Stage 3 (read in **bounded char-span batches**, not one pass).

| passage | verses | candidate chars |
|---|--:|--:|
| Pro 14:1-35 | 35 | 129 |
| Pro 15:1-33 | 33 | 113 |
| Pro 11:1-31 | 31 | 101 |
| Pro 21:1-31 | 31 | 98 |
| Pro 12:1-28 | 28 | 97 |
| Pro 10:1-25 | 25 | 82 |
| Pro 28:1-28 | 28 | 78 |
| Pro 17:7-28 | 22 | 69 |
| Pro 19:1-23 | 23 | 59 |
| Pro 8:4-21 | 18 | 52 |
| Pro 13:12-25 | 14 | 52 |
| Pro 16:16-33 | 18 | 49 |
| Pro 1:18-33 | 16 | 43 |
| Pro 2:2-14 | 13 | 42 |
| Pro 20:1-19 | 19 | 41 |
| Pro 29:6-20 | 15 | 40 |

## Read-effort shape

- **~50% of passages are small** (55 of 104 have ≤10 candidate chars) — quick reads.
- **The load concentrates in the tail**: 11 passages (≥50 chars) hold **~1,000 of the 2,123 candidate chars** (~47%) — the F-frames. These are where a char-span budget (≤~10–12 per pass) or per-verse reading applies.
- 18 single-verse passages (isolated candidates).

*Filed 2026-07-13. Read-only profile. Passages = `passage-build-2026` (v2 candidate-driven).*
