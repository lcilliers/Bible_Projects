# #2491 — Collection rebuild: plan v2 for approval

Plan only. Nothing built, nothing changed in iba/app/db/iba.db. Counts are from read-only queries of 2026-11-12, each with its definition. The researcher's rulings are on #2491 v9 and v11 (not copied here, B:3).

## 1. The model the researcher has ruled

1. A surface in scope is a member of exactly one collection.
2. A collection is formed from like words; its members are surfaces. A base is only a tool for gathering like words.
3. A phrase is one concept; the concept is placed in a collection, not each of its words.
4. Collections whose members largely coincide are one collection and are combined.
5. An opposite sits in one collection: if it stands alone it goes where it is the opposite; if it has its own collection with other members it sits there.
6. The collection's name is formed from all its members as a concept covering them; it may or may not be a base.
7. Collections that are close to each other are combined. A small separate collection is grouped with like-minded collections instead of standing apart.
8. Each collection becomes a chapter of the narration: it tells a story of how its words work in the inner being. The refinement is therefore not only the removal of surfaces in several collections. It evaluates every collection so that it makes sense, does not overlap another, tells a story and makes the narrative possible.

## 2. Where the data stands (study groups: behaviour and inner_being_state)

- Surfaces with verses: 3,765. In exactly one collection (own row or base, member tiers): 2,096; in two or more: 1,487; in none: 182. On the stricter rule that the surface's own row carries the link, 815 have none (633 only through the base).
- Of the 1,436 in two or more (own-kind occurrences): 625 are phrases, 811 are words. 1,160 phrase surfaces are in the study groups: 72 in none, 422 in one, 666 in two or more.
- 276 collections have word members; 385 pairs share at least one word; in 55 pairs the shared words are half or more of the smaller collection; merging those 55 would join 86 collections into 32 groups (chaining joins different senses, so each merge is a judgement).
- Size of the 277 collections (all confirmed, none merged): member surfaces counted as the linked terms plus the derived forms of each: median 17, smallest 1, largest 282; 23 have 3 or fewer, 43 have 5 or fewer, 82 have 10 or fewer, 158 have 20 or fewer. Counting only the linked words (core, synonym, opposite, gathered; no phrases, no derived forms): median 7; 64 have 3 or fewer, 113 have 5 or fewer. The narrative has 38 chapters today (`narrative_chapter`); chapter 10 is built by collection (B:127).
- Rows that depend on a collection's id: `ib_node.collection_id` (35,590 filled today by the old base rule), `surface_term.collection_state`, and the link table. How the engagement observations (stage engagement, 527) and the evidence report key their collection has not been read; it is read before any merge (step 1).

## 3. Method for every step

Class by class, never one sweeping run: a pilot of a few concepts by hand first; predicted counts; tried on a copy (`dbsnapshot.copy_db`); a named rollback snapshot; every config write through `apply_logged`; every data change kept in `surface_event` with its reason; nothing physically deleted (links are set deleted, superseded rows keep `superseded_by_id`); counts after equal the prediction or the run rolls back. Anything decided by meaning comes to the researcher as a workbook with the evidence, one batch at a time; nothing is decided by script. Any suggestion I make is labelled inferential (B:4).

## 4. Steps

0. **Settle the scope first.** The 182 surfaces with verses in no collection include ordinary words grouped by mistake (days 861, right 290, has, had). The workbook is with the researcher (`_analytics/surfaces/exports/study-surfaces-no-own-collection-link-v1-20261112.xlsx`). A surface that is not an inner-being word is regrouped, not forced into a collection. Also register the rulings of section 1 as a config rule (B:31, after the researcher confirms the wording), and stop any new collection-build or phrase-attach run until the rebuild is done.
1. **Read the dependents.** How `engagement` observations, the evidence report, the members and surfaces exports and the node column read a collection; what a merge must move. Report before anything is merged.
2. **Evaluate every collection as a chapter.** Not only the overlaps: all 277. One evidence sheet for each (in workbooks of a set number at a time): its members by tier with the derived forms, the verses it reaches with examples, the collections nearest to it (shared words, and the words of the other that read alike), and four plain questions for the researcher's ruling, one per ruling of section 1: does it make sense (do the members share one concept), does it overlap another, does it tell a story of how its words work in the inner being, can a chapter be written from it. The ruling for each collection is one of: keep; combine with a named collection; group a small collection with like-minded ones; split (it holds two stories); regroup members elsewhere. The 55 pairs with half or more shared words (and the 27 more at one third or more) come first, then the 82 collections with 10 or fewer member surfaces, then the rest. I may propose a combination or a name; the researcher rules. A combination moves the members to the kept collection (`collection.merged_into_id`, status merged) and keeps the old link rows as history; a split makes a new collection with its members moved.
3. **One collection for each remaining overlapping word.** After step 2 the overlap is measured again; the surfaces still in two or more collections should be few. For each: a list with every collection, tier and example verses; the researcher names the one. The opposite rule of section 1 is applied as a proposal only where it is mechanical (a standalone opposite), the rest is the researcher's.
4. **Phrases.** One workbook: each phrase, its collections now, the matched words and the Strong's code, example verses; the researcher names the one collection (or none). The other phrase links are set deleted. The phrase rule (`attach_phrases`) is retired as it stands.
5. **Members are surfaces.** Each derived form gets its own link to the collection of its base once that base is in one collection (the 633), and the 182 are placed or regrouped from step 0. The base stays an instrument, no longer the member.
6. **Names.** Each collection's name is checked against its members; where the core word does not cover them, a name is proposed from the members for the researcher to accept.
7. **Recompute and verify.** `ib_node.collection_id` for the nodes, `surface_term.collection_state`, the exports and reports; then the checks that matter, each a list, not a percentage: every in-scope surface not in exactly one collection (target none); every collection without a ruling from step 2 (target none); and the verses reached by the collections.

## 5. What the researcher is asked to decide

1. Approve the order of section 4, or change it.
2. The name of a collection: is `collection.core_term_id` still required (a base as anchor), or is the name free text and the anchor optional (a schema change)?
3. A text that carries two real senses (one text, two Strong's codes): one collection for the text, or the unit becomes the text with its Strong's code. Not measured how often this occurs.
4. The non-member links (associated, possible opposite, set aside, 3,726 live rows): kept as history, since they break no rule, or retired with the rebuild.
5. The second pass over the 11,175 surface texts never grouped is out of this plan; when it is run, the surfaces it adds enter the same rules.
6. How small is too small: is there a size below which a collection is always grouped with another, or is each small collection ruled on whether it can carry a chapter (23 have 3 or fewer member surfaces, 82 have 10 or fewer)?
7. The link to the narration: should the evaluation of a collection also record the chapter it will become (a chapter number or a working title), or is that left to the narrative step?

## 6. Limits

Counts depend on the definitions stated; the overlap between collections is measured on single-word core, synonym and opposite members only; "meaning" is not tested by any count here, which is why every merge and placement goes to the researcher.
