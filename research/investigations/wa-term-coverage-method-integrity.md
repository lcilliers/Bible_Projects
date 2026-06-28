# Term-coverage method integrity — does the registry→terms→related-terms cascade hold?

> **Doc version:** 1 · **Last updated:** 2026-06-28 · finding. Triggered by: why was cruelty/`perek` missed? (see `wa-ruthlessness-investigation.md` §2). **This validates the *method*, not the one item.**

## The question
We expected: **registry word (English) → STEP terms → STEP related-terms** to catch every IB-relevant term. `perek` (ruthlessness) was missed. Is the cascade structurally sound, or does our reliance on STEP's related-graph have a hole?

## The test (empirical, 2026-06-28)
| probe | result |
|---|---|
| Does `perek` H6531 appear as a recorded related-word of *any* studied term? | **0 rows** — total orphan |
| What does our studied "ruthless" term `arits` H6184 relate to (DB)? | `terror` H4637 · `dreadful` H6178 · `tremble` H6206 — **the dread family only** |
| STEP **live** related-words for `arits` | identical — terror / dreadful / tremble. **No cruelty terms.** |
| STEP **live** related-words for `perek` | **`paroketh` H6532 "curtain" — and nothing else.** A same-root **homonym**, not a semantic relative. |

## Root cause — three compounding structural facts
1. **No English seed for cruelty.** The ~215 registry words have no cruelty/ruthlessness/harshness entry. The English list is the **entry gate**; with no seed, the concept's whole sub-field can only be reached by spillover from adjacent concepts.
2. **STEP `relatedNos` is shallow, and sometimes morphological — not a semantic ontology.** It returns ~1–3 terms, one hop. For `perek` the only link is a spelling-homonym (`curtain`); for rare words it is near-empty. It associates; it does not map meaning.
3. **Contextual capture poisons cross-concept discovery.** `arits` is genuinely a cruelty word, but it was pulled under **dread**, and its relations point **back to dread** — not outward to its cruelty neighbours. A term captured under concept X carries X's relations, so it does **not** act as a seed for its own home concept. Cruelty therefore never gets seeded, even though a cruelty word is in the study.

## The integrity verdict
- The cascade is sound for **expanding a seeded concept** (take a registry word, pull its lexical family). That is what it is for, and it works.
- It is **not a discovery mechanism** for concepts the English list omitted, and **not a complete semantic graph.** STEP `relatedNos` has rare-word orphans, homonym links, and single-dimension/contextual linking.
- Therefore **term coverage = closure of (a human-curated ~215-word English list) under (a shallow, leaky association graph).** That set is strictly smaller than "all IB-relevant Hebrew/Greek terms." Blind spots are **guaranteed**, not accidental; `perek` is a proven one.
- **The binding constraint is the human curation of the English word list.** STEP cannot find what the list did not seed, and adjacent-concept spillover is unreliable (homonyms, contextual capture). So the cascade's completeness can never exceed the completeness of the English seed list — and we already know that list has gaps (cruelty; likely violence; possibly others).

## What this does NOT mean
- The cascade is not broken or useless — within a seeded concept it pulls the family well, and the digested cluster work (M01, M06, etc.) remains valuable.
- It means the cascade must be understood as an **index over the corpus, not a census of it.**

## Implication — why the verse-fanout method is necessary, not optional
The verse-fanout method enters from **the verse**, where *every term that occurs is present* — independent of the English seed list and the `relatedNos` graph. `perek` is invisible to the cascade but unmissable at the verse (Exo 1:13, Lev 25:43). So:
- the registry/STEP cascade is a **partial, leaky index**;
- the verse-fanout reads the **complete substrate** directly;
- they are complementary, and the verse-fanout is what **guarantees coverage** the cascade cannot.

## Recommendations (for researcher decision — not actioned)
1. **Re-frame the registry as a *seed list*, not a coverage boundary.** Expect gaps; do not treat "not in the registry" as "not IB-relevant."
2. **Use the verse-fanout as the coverage guarantor** — terms surface at the verse regardless of seed/relatedNos. Untracked-but-present terms (like `perek`) become the signal for registry gaps.
3. **Consider a coverage audit:** sweep the corpus morphology for high-frequency / clearly-IB terms that have **no study identity** (orphans like `perek`, `chamas`) — a finite, mechanical check that surfaces the blind spots the cascade left.
4. Do **not** rely on STEP `relatedNos` to deepen a concept's field — it is too shallow/leaky; deepen via the verse-fanout and the multi-contributor spiderweb instead.
