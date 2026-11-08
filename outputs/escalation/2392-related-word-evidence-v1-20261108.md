# #2392 Word-keyed related-word evidence for grouping surfaces — exploration v1 (2026-11-08)

Read-only. Nothing was written to iba.db or built. All matching below is inferential (B:4): word-level matching on lower-cased text, with no sense or family check.

## What was asked

Researcher, verbatim (full text in #2392 v1): the related words STEP gives for each strong are a clue to words that relate to each other even when the words look nothing alike. An extract of all the related words from the meaning tables might be added to the AI thinking process to speed up the similarity question. The exploration was not to over-analyse words that do not matter: many related words never appear in the study, and many surfaces fall outside the scope of collections.

## Scope used (so nothing that does not matter is measured)

- Surfaces in scope: surface_term rows, live, one word, in the groups behaviour or inner_being_state: 2,686 words. Phrases (1,166 of the 3,852 in those groups) are not tested by the structure or base modules and come last (surface_term.form), so they are left out.
- The collection test uses the 58 live collections and their live links (collection_link): synonym 230, opposite 39, possible_opposite 162, associated 451, set_aside 95 (core rows excluded).
- Read first (B:123): cfg_table.use of surface_term, collection, collection_link, strong_related, strong_sense, strong_meaning_parsed; wa_term_related_words (bible_research.db) is not used (inactive for iba analysis; the researcher says it is likely incomplete).

## The evidence list built in memory

A bag of English words per source: for each strong, its sense head (strong_sense) plus the gloss of every related term (strong_related.related_gloss, 88,467 live rows, 15,455 source strongs); and, separately, for each lemma the parsed glosses (strong_meaning_parsed, 52,522 rows, 13,255 lemmas). A gloss is split on comma, semicolon, colon, slash and brackets, a leading to/a/an/the is dropped, and only one-word pieces are kept. Two words are co-listed when they share a bag.

## Coverage of what matters

| set | words | found in a related bag | found in a parsed-gloss bag | found in either |
|---|---|---|---|---|
| in-scope single words | 2,686 | 1,167 | 1,704 | 1,739 (65%) |
| bases among them (a base is the base_id of a live surface) | 1,105 | | | 1,031 (93%) |

The bases, which are what collections are built from, are almost all covered. The uncovered third of all in-scope words is mostly the long tail of surfaces (derived forms), which the base work already reduces.

## Signal: do co-listed words match what the judge decided

Pairs are core word and member, counting only pairs where both words appear in some bag.

| pair kind | pairs | both known | co-listed in a related bag | in a parsed bag | either | share |
|---|---|---|---|---|---|---|
| synonym | 230 | 204 | 36 | 100 | 117 | 57% |
| associated | 451 | 412 | 24 | 88 | 97 | 24% |
| set_aside (model listed, judge refused) | 95 | 91 | 8 | 29 | 29 | 32% |
| opposite | 39 | 39 | 3 | 1 | 4 | 10% |
| possible_opposite | 162 | 155 | 3 | 3 | 6 | 4% |
| random pairs of in-scope words (20,000, seed 1) | 20,000 | 20,000 | 76 | 162 | 224 | 1% |

Reading, each point inferential:

1. Accepted synonyms are co-listed 57% of the time against 1% for random pairs, so the lists carry real signal about likeness.
2. 43% of accepted synonyms are not co-listed (for example love and cherish, anger and enrage, pride and vanity). The lists cannot be the only source: they would miss many true pairs.
3. Opposites are almost never co-listed (4 of 39). The lists do not help find opposite poles; they help likeness only.
4. 32% of the pairs the judge set aside are co-listed, for example pride and arrogant, repent and regret, hope and expect. Either the lists are broader than the judge's test (family or sense overlap) or the judge was strict. That needs the researcher's eye on a sample; this file does not decide it.
5. The parsed glosses (lemma-keyed) carry more of the signal than strong_related (100 against 36 synonym pairs).
6. Examples that are co-listed: love and beloved, love and affection, fear and terror, fear and dread, deceive and deceit, deceive and lie. Not co-listed: love and cherish, anger and vexed, forgive and mercy.

## Limits

- Co-listing through a shared strong is sense-blind: a bag mixes every sense of the strong, which is the per-strong problem the researcher described. A direct pair (one word in the other's list) was not separated from a shared bag in this pass.
- Only words that are one word were matched. Multi-word glosses ("to love: lover" is split, but "give thanks" is not matched) are dropped.
- Counts are over the live data at this moment; the Ask run of #2388 is still writing collections in the other session, so collection counts will change.

## Correction to a figure given earlier in chat

I said 15,018 related strongs had no strong row. That came from a faulty query (the inner column name resolved to the outer table). The correct check: strong_related.related_strong holds 1,673 distinct codes with no row in strong (including one empty value); for 787 of them the base code (suffix letter removed) is present in strong, so part is a suffix-form mismatch and part is codes STEP names that were never onboarded. Not tested further; it does not touch the in-scope words.

## Options for the researcher (a decision, not yet designed)

- A. Hints in the collection prompt: when a core word is started, give the model the in-scope words that co-list with it (from the evidence list), labelled as STEP evidence and inferential. Cheapest; helps likeness; the model and judge still decide.
- B. Candidate finder: use the co-listed words as extra candidates the model did not list, then judge them as now. Widens recall (the 43% not found by the lists would still come from the model).
- C. Check only: leave the prompt alone and flag judged pairs with no co-listing at all, and refused pairs that are co-listed (point 4), for the researcher to look at.
- D. Not now.

Any of A to C needs a stored extract (a table or a file); that is a design and a build, which comes only after the researcher chooses (B:105).
