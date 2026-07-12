# Span-completeness pre-pass — feasibility + design (the term-list decided AHEAD)

- **File:** wa-span-completeness-prepass-v1-20260701.md · **2026-07-01 · Author:** Claude Code · **status: feasibility probe + DRAFT design.**
- **Researcher direction (2026-07-01):** the unit is the **SPAN**, not the term. **Verse → span → is it a primary term? → if not, should it be (missing primary or qualifier)? → confirm it must be pulled into the DB → the complete term-list for lexical analysis.** Do this **AHEAD** of lexical analysis (it's available from the master verse index), not during it.

## 1. Feasibility — CONFIRMED
- **The span layer already exists:** table **`verse_span_index`** (305,961 rows, built 2026-06-26) — one row per span: `verse_id · word_index · surface · pos · morph_code · stem · strongs · primary_strong` (canonical, zero-padded). `verse_morphology` holds the same. So "verse → spans" is a DB read, no rebuild.
- **The check is mechanical** against the known-term set (`mti_terms.strongs_number`, canonical), classified by `cluster_code`: **primary** (M-cluster) · **T2** (qualifier) · **FLAG** · **unclustered**.

## 2. What a run yields (probe: 2,000 analysed verses, 30,641 spans)
| span class | count | of which |
|---|--:|---|
| **primary-term span** | 5,962 | **4,946 already tagged · 1,016 UNTAGGED = missing-primary candidates** |
| **T2-qualifier span** | 6,623 | 1,075 tagged · **5,548 untagged** = qualifier candidates |
| other-term (FLAG/unclustered) | 5,936 | — |
| **unknown (not any known term)** | 12,120 | ordinary words + potential brand-new terms |

Extrapolated to all 19,171 analysed verses (~9.6×): on the order of **~10k missing-primary span-occurrences** and many more T2 — but **distinct lemmas are far fewer** (the same lemma recurs, e.g. `H1285` covenant, `H3027` hand). The real review burden is the **distinct candidate lemmas**, not the occurrences.

**Sample missing-primary candidates** (primary-term strongs, untagged at that verse): `H7592` consulted (*desire*) · `H0014` be-willing (*volition*) · `H3045` know (*knowledge*) · `H8334` minister (*worship*) · `H3027` hand (*strength*) · `H1285` covenant. Some are genuine IB misses; some are the same lemma used **non-IB here** — which is exactly why this is a candidate list, not an auto-decision.

## 3. The nuance — mechanical narrows, judgment decides
- **Context-dependent.** A lemma can be an IB term in one verse and ordinary in another (`H3027` hand = literal hand vs metaphor "strength"). So a span matching a primary lemma is a **candidate**, confirmed per occurrence — not an automatic term.
- **Three signal tiers** (decreasing mechanical confidence):
  1. **missing-primary** — span's lemma IS a known primary IB term, untagged here → *most likely a real miss* → review.
  2. **T2-qualifier** — span's lemma is a known T2 → pull as qualifier where it modifies a term.
  3. **unknown** — lemma is no known term → potential **new** primary/qualifier → hardest, pure judgment (bounded by IB relevance).
- This matches the standing rule that the registry/term set is an **index, not a census** (memory `feedback_term_coverage_cascade_is_index_not_census`) — the span sweep is the census check.

## 4. Proposed pre-pass (run AHEAD, review-gated)
For each verse (or cluster/passage batch), from `verse_span_index`:
1. classify every span → {tagged-term · missing-primary · T2-qualifier · unknown};
2. emit a **per-verse candidate sheet**: the tagged terms + the untagged missing-primary and qualifier candidates (+ gloss/morph), for researcher confirmation;
3. on confirmation → **pull the span into the DB as a term** (onboard) so it enters the term-list;
4. the confirmed term-list then drives lexical analysis — **no term-vs-not decisions left for analysis time.**

**Design choices to confirm before building:**
- **a. Scope of the first run** — all 19,171 analysed verses, or a pilot (one cluster / a book)?
- **b. Candidate tiers to include** — missing-primary only (cleanest), or also T2 and unknown?
- **c. Output** — a review `.md`/table per verse, or a DB staging table (`span_term_candidate`) the researcher marks up?
- **d. Confirm-to-onboard** — manual per candidate, or batch-approve a distinct lemma across all its occurrences?

## 5. Status
Feasibility proven; `verse_span_index` in place. Awaiting the §4 design choices before building the pre-pass. Related: memory `project_ve_lexical_is_verse_first`, `feedback_term_coverage_cascade_is_index_not_census`; earlier span tooling `_build_verse_span_lexical_index_v1_20260626.py`.
