# #2491 — Collection rebuild: plan v1 for approval

Plan only. Nothing built, nothing changed in iba/app/db/iba.db. Counts are from read-only queries of 2026-11-12, each with its definition. The researcher's rulings are on #2491 v9 (not copied here, B:3).

## 1. The model the researcher has ruled

1. A surface in scope is a member of exactly one collection.
2. A collection is formed from like words; its members are surfaces. A base is only a tool for gathering like words.
3. A phrase is one concept; the concept is placed in a collection, not each of its words.
4. Collections whose members largely coincide are one collection and are combined.
5. An opposite sits in one collection: if it stands alone it goes where it is the opposite; if it has its own collection with other members it sits there.
6. The collection's name is formed from all its members as a concept covering them; it may or may not be a base.

## 2. Where the data stands (study groups: behaviour and inner_being_state)

- Surfaces with verses: 3,765. In exactly one collection (own row or base, member tiers): 2,096; in two or more: 1,487; in none: 182. On the stricter rule that the surface's own row carries the link, 815 have none (633 only through the base).
- Of the 1,436 in two or more (own-kind occurrences): 625 are phrases, 811 are words. 1,160 phrase surfaces are in the study groups: 72 in none, 422 in one, 666 in two or more.
- 276 collections have word members; 385 pairs share at least one word; in 55 pairs the shared words are half or more of the smaller collection; merging those 55 would join 86 collections into 32 groups (chaining joins different senses, so each merge is a judgement).
- Rows that depend on a collection's id: `ib_node.collection_id` (35,590 filled today by the old base rule), `surface_term.collection_state`, and the link table. How the engagement observations (stage engagement, 527) and the evidence report key their collection has not been read; it is read before any merge (step 1).

## 3. Method for every step

Class by class, never one sweeping run: a pilot of a few concepts by hand first; predicted counts; tried on a copy (`dbsnapshot.copy_db`); a named rollback snapshot; every config write through `apply_logged`; every data change kept in `surface_event` with its reason; nothing physically deleted (links are set deleted, superseded rows keep `superseded_by_id`); counts after equal the prediction or the run rolls back. Anything decided by meaning comes to the researcher as a workbook with the evidence, one batch at a time; nothing is decided by script. Any suggestion I make is labelled inferential (B:4).

## 4. Steps

0. **Settle the scope first.** The 182 surfaces with verses in no collection include ordinary words grouped by mistake (days 861, right 290, has, had). The workbook is with the researcher (`_analytics/surfaces/exports/study-surfaces-no-own-collection-link-v1-20261112.xlsx`). A surface that is not an inner-being word is regrouped, not forced into a collection. Also register the six rulings of section 1 as a config rule (B:31, after the researcher confirms the wording), and stop any new collection-build or phrase-attach run until the rebuild is done.
1. **Read the dependents.** How `engagement` observations, the evidence report, the members and surfaces exports and the node column read a collection; what a merge must move. Report before anything is merged.
2. **Combine collections.** Workbook of the 55 pairs (and the 27 more at one third or more): members of each, the shared words, example verses. The researcher rules merge or keep apart and names the merged concept. A merge moves the members to the kept collection (`collection.merged_into_id`, status merged), keeps the old link rows as history.
3. **One collection for each remaining overlapping word.** After step 2 the overlap is measured again. For a word still in two or more: a list with every collection, tier and example verses; the researcher names the one. The opposite rule of section 1 is applied as a proposal only where it is mechanical (a standalone opposite), the rest is the researcher's.
4. **Phrases.** One workbook: each phrase, its collections now, the matched words and the Strong's code, example verses; the researcher names the one collection (or none). The other phrase links are set deleted. The phrase rule (`attach_phrases`) is retired as it stands.
5. **Members are surfaces.** Each derived form gets its own link to the collection of its base once that base is in one collection (the 633), and the 182 are placed or regrouped from step 0. The base stays an instrument, no longer the member.
6. **Names.** Each collection's name is checked against its members; where the core word does not cover them, a name is proposed from the members for the researcher to accept.
7. **Recompute and verify.** `ib_node.collection_id` for the nodes, `surface_term.collection_state`, the exports and reports; then the check that matters: a list, not a percentage, of every in-scope surface not in exactly one collection (target none), and the verses reached by the collections.

## 5. What the researcher is asked to decide

1. Approve the order of section 4, or change it.
2. The name of a collection: is `collection.core_term_id` still required (a base as anchor), or is the name free text and the anchor optional (a schema change)?
3. A text that carries two real senses (one text, two Strong's codes): one collection for the text, or the unit becomes the text with its Strong's code. Not measured how often this occurs.
4. The non-member links (associated, possible opposite, set aside, 3,726 live rows): kept as history, since they break no rule, or retired with the rebuild.
5. The second pass over the 11,175 surface texts never grouped is out of this plan; when it is run, the surfaces it adds enter the same rules.

## 6. Limits

Counts depend on the definitions stated; the overlap between collections is measured on single-word core, synonym and opposite members only; "meaning" is not tested by any count here, which is why every merge and placement goes to the researcher.
