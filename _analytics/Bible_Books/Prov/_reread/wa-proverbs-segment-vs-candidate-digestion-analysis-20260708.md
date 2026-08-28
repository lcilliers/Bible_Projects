# Proverbs — do the segments over-include non-char verses? (digestion analysis, 2026-07-08)

> Tests the hypothesis that Proverbs `segment_unit`s are too large (too many non-char verses) to digest the chars properly, forcing selective char analysis. Read-only; measured against the live `char_candidate` seed. **Verdict: the hypothesis about *non-char padding* is not borne out — but a real digestion problem exists, of a different kind.**

## 1. Non-char content in the segments — small
Active Proverbs segments: **251** (mapped via `segment_unit_verse`).
- Total verse-links: **932** · char-verses: **847** · **non-char verses: 85 = 9%**.
- Segment size: min 1, max 35, **mean 3.7, median 2**. Size buckets: `1`=72 · `2-4`=134 · `5-9`=29 · `10-19`=9 · `20+`=7.
- Non-char per segment: mean 0.3, max 9.

**So segments are mostly small and only 9% of their verses are non-char.** Non-char padding is not the driver. The two segments with real non-char padding are the *narratives* — `PRO-07-B` (adulteress, 18v / 9 non-char) and `PRO-31-noble-wife` (22v / 6 non-char).

## 2. The real digestion problem — char DENSITY, not padding
The load that matters for "digest the chars properly" is **char-spans per unit**, not verse count. Per segment: mean **9.3**, median 5, **max 129**. **16 of 251 segments carry ≥20 char-spans** — and the worst are the **F (frame/arena) segments in the sentence-collection chapters**, which are large because those chapters are wall-to-wall independent proverbs, each with chars:

| segment | type | verses | char-spans |
|---|---|--:|--:|
| PRO-14-F | F | 35 | **129** |
| PRO-15-F | F | 32 | **109** |
| PRO-10-F | F | 31 | 96 |
| PRO-11-F | F | 29 | 95 |
| PRO-12-F | F | 27 | 91 |
| PRO-13-F | F | 21 | 72 |
| PRO-01-D | D | 14 | 41 |
| PRO-02-A | D | 11 | 33 |
| PRO-31-noble-wife | D | 22 | 28 |

These F-frames are not *one inner-being movement* — they are collections of dozens of separate sayings. A 35-verse / 129-char-span unit **cannot** be digested char-by-char in one pass → that is exactly where selective char analysis creeps in. The problem is concentrated in **~6 F-frames + ~10 long discourses**, not the 251 segments broadly.

## 3. Would candidate-driven passages (rule v2) fix it? No — worse.
Building Proverbs as **candidate-driven passages** (maximal runs of consecutive candidate verses, within chapter): **104 passages**, size mean 7.7 / median 5, but **char-spans per passage mean 20.4, max 129, with 32 passages ≥20 char-spans** (largest: 129, 113, 101, 98…). Because Proverbs chapters are candidate-*dense*, merging consecutive candidate verses produces **bigger** char blobs than the semantic segments. So switching Proverbs from segmentation → candidate passages would **worsen** digestion, not improve it.

| model | units | median verses | char-spans/unit (mean) | units ≥20 char-spans |
|---|--:|--:|--:|--:|
| **segments (§15, current)** | 251 | 2 | 9.3 | 16 |
| candidate passages (rule v2) | 104 | 5 | 20.4 | 32 |

## 4. Implication
- The segmentation model is **already the finer, more digestible** of the two for Proverbs — median 2 verses. Keep it; do **not** move Proverbs to candidate-driven passages.
- The fix for "selective char analysis" is **granularity inside the dense units**, not a model swap: split the ~16 heavy segments (especially the 6 F-frames, 72–129 char-spans) into digestible reading sub-units — e.g. a **char-span budget per reading pass** (≤ ~10–12), or read the F-frame chapters **per-verse** (each verse's chars = one small digest). The unit of *work* in the cycle is already "one candidate char-lemma in one verse" (cycle §5); the F-frame just needs to be read in bounded batches rather than as one 35-verse block.

*Filed 2026-07-08. Read-only. No DB writes. Decision on the granularity fix + the segment-vs-passage model for Proverbs is the researcher's.*
