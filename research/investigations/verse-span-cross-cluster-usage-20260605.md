# Span as focal point — how a verse is "used" across the study

> Read-only investigation, 2026-06-05. Answers the researcher's intervention: the **span** (the term
> occurrence in the verse) is the focal point of meaning; verses with multiple spans may belong to other
> clusters; *how would we know if a verse is used in other parts of the study?*
> Script: `scripts/_exploratory_verse_cross_cluster_usage_v1_20260605.py`.

## The model (confirmed)

- A **span** = one term occurrence in a verse = one `wa_verse_records` row (`term_id`, `target_word` =
  the matched word, `mti_term_id` → `mti_terms.cluster_code`).
- A **verse** = `(book_id, chapter, verse_num)`. **62,753 active span-rows sit on only 23,642 distinct
  verses** — ~2.6 spans per verse; the densest carries **17** (Neh 9:17).
- So the *verse* is not the analytic unit — the **span is**. The same verse is read once per span, and
  different spans of one verse legitimately belong to different clusters.

## How we know a verse is used elsewhere (the answer)

Key the verse by `(book_id, chapter, verse_num)` and join **all** its span-rows → terms → `cluster_code`.
The set of distinct clusters across those spans is **where the verse is used**. No new structure is
required to ask the question — it is a group-by on the canonical verse key. (Whether to make it *easier*
to ask is the raw-data question below.)

```sql
SELECT TRIM(mt.cluster_code) AS cluster, wr.target_word AS span, wr.term_id
FROM wa_verse_records wr JOIN mti_terms mt ON mt.id = wr.mti_term_id
WHERE wr.book_id=? AND wr.chapter=? AND wr.verse_num=? AND COALESCE(wr.delete_flagged,0)=0
ORDER BY cluster;
```

## Evidence of scale

- **Study-wide:** of 23,261 verses with clustered spans, **59% appear in ≥2 clusters**, and **30%
  (7,190) in ≥2 *real* M-clusters** (excluding the T2/FLAG buckets). Average **2.03 clusters per verse**.
- **M01 (Fear):** of 834 analytic verses, **698 (84%) carry a span in ≥1 other cluster**. Top
  co-occurring real clusters: M23 Strength (61), M15 Wisdom (51), M22 Praise (50), M30 Obedience (44),
  M05 Love (36), M44 Relational (33), M41 Remembrance (32), M33 Peace (32), M10 Sin (31), M04 Joy (29).
- **Worked example — 2 Corinthians 7:11**, one verse, **8 clusters**, each via its own span:

  | span | Strong's | cluster |
  |------|----------|---------|
  | fear | G5401 | M01 Fear |
  | indignation | G0024 | M02 Anger |
  | grief | G3076 | M03 Grief |
  | innocent | G0053 | M12 Purity |
  | longing | G1972 | M18 Hope |
  | zeal | G2205 | M21 Prayer |
  | punishment | G1557 | M26 Righteousness |
  | earnestness | G4710 | M34 Perseverance |

  M01's Pass A reads this verse **through the `fear` span only** — and *should*; "fear" here is one note in
  Paul's catalogue of a repentant church's inner state. But the verse is simultaneously the analytic
  property of seven other clusters via its other spans.

## What this means for method

1. **Span is the focal point of meaning (Seven Principles augmentation).** The meaning is of the
   **term-occurrence in this verse**, with the *verse* supplying literary/historical/canonical context
   (Principles 3–6). The Seven Principles should be read **span-first**: establish the text → the span's
   sense *in use* here (Principle 2, no totality transfer) → the verse and its context frame it. The
   "meaning of the verse" is really "the meaning the span carries, read in the verse."
2. **Sibling-span awareness ≠ contamination.** The v3 contamination guard suppresses inherited *cluster
   structure* (group/VCG/sub-group/cluster labels) so the analyst doesn't anchor on prior groupings.
   Knowing the verse carries **other inner-being spans** is different — it is part of reading the verse
   (the literary context) and it flags multi-belonging. The per-verse brief classifier was *already*
   designed to see all sibling spans at once (`feedback_brief_classifier_pass`). So Pass A can be
   span-focal **and** sibling-aware without reintroducing structure contamination.
3. **Multi-belonging is recorded, not resolved** (`feedback_two_governing_principles` P2;
   `feedback_cross_cluster_co_occurrence`). When the target span's verse carries a sibling span that pulls
   toward another cluster, Pass A names it — it does not compress to the M01 frame, and it does not move
   the verse. Routing is by **span/term**, never by the whole verse (`project_pointer_lifecycle_model`).

## The raw-data-adjustment question (options — your call)

The query works today, but cross-cluster co-occurrence is **reconstructed** each time by grouping on the
verse key; nothing in the model makes a verse a first-class object or exposes a span's siblings directly.

- **Option 0 — leave as is.** Ask via the group-by when needed. Cheapest; no migration.
- **Option 1 — a co-occurrence view/index (light).** A `verse_span_cooccurrence` view (or a small
  materialised table) keyed by `(book,ch,verse)` listing every span + its cluster. Makes "is this verse
  used elsewhere, and where?" a single lookup; feeds Pass A sibling-awareness and the audit. No change to
  source data — reversible.
- **Option 2 — promote the verse to a first-class entity (heavier).** A `verse` table (canonical key +
  text) with `wa_verse_records` carrying a FK to it. Cleanest long-term (verse-level queries, dedup,
  cross-cluster joins become trivial), but a real migration touching ~63k rows and downstream code.

Recommended: **Option 1 now** (enables span-focal + sibling-aware Pass A and the cross-cluster audit
check immediately), consider **Option 2** later if verse-level work proliferates.

## Implications for the Pass A drafts (NOT changed yet — for your review)

- **DRAFT A meaning rubric** → make **span-focal explicit**: "record the meaning the *target span* carries
  in this verse; the verse and its other spans are context. Where a sibling span pulls toward another
  cluster, name it in the meaning — do not compress to this cluster's frame, do not move the verse."
- **DRAFT A input** → Pass A should see the **full verse + all sibling spans** (already the per-verse
  classifier shape), with inherited *structure* still suppressed.
- **DRAFT B audit** → add a surfacing check **PA-14 cross-cluster co-occurrence**: for each cluster verse,
  list the sibling spans and their cluster homes (from Option-1 view), so multi-belonging is visible and
  the analyst can confirm the target-span meaning didn't absorb a sibling's sense.
