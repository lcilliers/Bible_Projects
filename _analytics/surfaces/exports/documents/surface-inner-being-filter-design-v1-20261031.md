# Surface allocations: filter the obvious, test the rest (#2344, design v1, 2026-10-31)

Researcher, verbatim: "there is a large percentage that is obvious, we really do not perform llm tests on them. they need to be assigned and filtered out of the population to subject advanced llm determination."

Nothing built. Counts are read-only from iba/app/db/iba.db (live rows of the concept query).

## What the population is
- 10,722 live (strong, surface) pairs = 2,625 distinct Strong's codes. 2,100 of the codes have all their pairs in one subgroup.
- A verdict on "is this word inner-being" belongs to the Strong's code (the lemma), not the inflection: abhor, abhorred, abhors are one judgement. Judging 2,625 codes in place of 10,722 pairs (or 4,884 English words) cuts the work by about 4 to 1 before any filter.
- Pairs by concept domain: Relational 2,958; Moral character 1,345; Knowing and thinking 1,104; Will and action 1,099; Feeling (4 domains) 2,122; Person and life 686; Speech and cry 440; Standing before others 405; God and community 265; Trust and faith 252; Other beings 46.

## Proposed tiers (a draft for you to change)
1. **Assigned inner: no LLM.** The Strong's code is on a lexicon of plain inner-being words (affect, thought, will, disposition, inner organs: for example fear, joy, grieve, know, desire, heart, soul). Verdict `inner`, tier `lexicon`. The lexicon is a file you review once.
2. **Assigned not-inner: no LLM.** The Strong's code is on a list of plain outward words (objects, places, ritual acts, kinship, proper names, numerals, particles), for example seats, purification, burnt offering. Verdict `outer`, tier `lexicon`.
3. **Advanced determination: the remainder.** Per Strong's code, with its stepGloss and meaning-tree senses, the stronger question set: does the word name something inside a person (state, feeling, thought, disposition), or an act that expresses one, or only an outward thing. Run by the engine you choose (Claude batches, or the local model).
4. Your four-question human test (be, do, experience, express, get) stays as a first screen on tier 3 only, as the trial showed it passes nearly every word and cannot sort by itself.

All verdicts are inferential (B:4) until you confirm them in the CSV.

## What you are asked to decide
1. Do tiers 1 and 2 stand as the filter?
2. Who builds the two lexicons: Claude drafts both from the 2,625 codes' stepGloss for your review (my recommendation), or you supply the seed words.
3. The engine for tier 3: Claude in batches (faster, more accurate, cloud) or the local model (about 12 s per call on this CPU).
