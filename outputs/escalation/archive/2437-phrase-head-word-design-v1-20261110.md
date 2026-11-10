# #2437 — Attach multi-word phrases to a collected head word: findings and options

Status: design for the researcher's decision (B:105, B:44). Nothing is built or changed. Every count below is from a read-only query on `iba/app/db/iba.db` on 2026-11-10. The word match used is rough (exact word, a small stop list, no stemming), so its counts are inferential (B:4).

## Tables read (B:123)
- `surface_term` (`cfg_table.use`): one row per surface text. `form` is word or phrase; a phrase "is not tested by the structure or base modules and is assigned to collections last (ruling D2)". `collection_state` is filled only for a term as a base.
- `collection_link` (`cfg_table.use`): where a base stands in a collection; tiers core, synonym and opposite are members.
- Code: `iba/app/lib/surfaceresolve.py` line 66 makes a phrase its own base (`phrase_not_tested`); nothing links it to a head word.

## Verified
| Check | Result |
|---|---|
| Phrases in collection a (behaviour 378, inner_being_state 788) | 1166 |
| Of those with collection_state `untouched` | 1166 (all) |
| Of those with any live `collection_link` | 0 |
| Phrases with a word placed or shared in a collection | 788 |
| Phrases with only listed_only or set_aside words | 234 |
| Phrases with only words that have no collection state (out of scope or other group) | 122 |
| Phrases with no word matching a surface | 22 |

## The head word is often ambiguous
Distinct collections reached through each phrase's words (members only):

| Collections reached | Phrases |
|---|---|
| 0 | 411 |
| 1 | 392 |
| 2 | 193 |
| 3 or more | 170 |

Only 392 phrases point to a single collection by word match alone. 363 reach two or more (for example "pay attention" holds both pay and attention), so "the head word" needs a stated rule, not a lookup. Inflected phrases ("cried out", "crying out", "gave thanks") miss their base ("cry out", "give thanks") unless inflection is handled, so the listed-only and no-state counts above are inflated by it.

## Decisions needed

**D1. How the head word is found.**
- A (recommended): the structure module's inflection result for each word of the phrase, then a fixed rule for the head (the verb of a phrasal verb, the last noun of a noun phrase), held in config so it is not re-asked.
- B: the model proposes the head word of each phrase and the judge confirms, as the collection judges do. Costlier, runs through Ollama.
- C: match a phrase to an existing phrase base first, then A.

**D2. Phrases whose head word reaches more than one collection (363).**
- A (recommended): attach to one collection by the D1 rule and record the other candidates as evidence, not links.
- B: attach to all of them as shared.
- C: leave for the researcher to choose, one by one.

**D3. Phrases whose head word is only listed_only or set_aside, or has no collection state.**
- A (recommended): not attached; recorded as "head word outside the collections" with the reason, so the researcher can read them.
- B: attach to the word's collection anyway, flagged.

**D4. After attaching: do phrases go through Engagement with that collection?**
- A (recommended): yes, in the same batches as the word bases (setting `engagement.batch_size`).
- B: attach only; engagement is a later decision.

## Not decided here
The schema (a new tier or a link column), the step name and the code follow your answers; none is proposed now.
