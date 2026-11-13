# #2491 — Collection rebuild: plan v3 for approval

Plan only. Nothing built, nothing changed in iba/app/db/iba.db. Counts are from read-only queries of 2026-11-12, each with its definition. The researcher's rulings are on #2491 v9, v11 and v12 (not copied here, B:3). The first batch of rulings for step 2 is `_analytics/surfaces/exports/collection-merge-proposals-pairs-v2-20261112.md`.

## 1. The model the researcher has ruled

1. A surface in scope is a member of exactly one collection.
2. A collection is formed from like words; its members are surfaces. A base is only a tool for gathering like words.
3. A phrase is one concept; the concept is placed in a collection, not each of its words.
4. Collections whose members largely coincide are one collection and are combined.
5. An opposite sits in one collection: if it stands alone it goes where it is the opposite; if it has its own collection with other members it sits there.
6. The collection's name is formed from all its members as a concept covering them; it may or may not be a base.
7. Collections that are close to each other are combined. A small separate collection is grouped with like-minded collections instead of standing apart.
8. Each collection becomes a chapter of the narration: it tells a story of how its words work in the inner being. The refinement is therefore not only the removal of surfaces in several collections. It evaluates every collection so that it makes sense, does not overlap another, tells a story and makes the narrative possible.
9. The work is not purely linear: a later change can reopen an earlier decision. Each step therefore ends by measuring again what the earlier steps settled.
10. A collection is built on surfaces, and a Strong's code is not the unit: one Strong's code may appear in several collections when its surfaces have different meanings that sit in different collections. The chapter heading comes from the collection's name but need not equal it. Where the base is a suitable name it can be the name; where it is not representative the name is reconsidered.
11. Smallness is not a number. A small collection that is really unique and fits nothing else stays small; it is judged on context and likeness.
12. The evaluation of a collection is a light estimate of whether its words will tell a coherent story; it does not design the story, the chapter number or the title.
13. The non-member links (associated, possible opposite, set aside) that point to a surface are considered as surfaces; those that only support the judgement of membership stay as part of the logic of the members.
14. The never-grouped surface texts (11,175) are deliberately left out; the few among them that are behaviours or states are dealt with at that later stage.

## 2. Where the data stands (study groups: behaviour and inner_being_state)

- Surfaces with verses: 3,765. In exactly one collection (own row or base, member tiers): 2,096; in two or more: 1,487; in none: 182. On the stricter rule that the surface's own row carries the link, 815 have none (633 only through the base).
- Of the 1,436 in two or more (own-kind occurrences): 625 are phrases, 811 are words. 1,160 phrase surfaces are in the study groups: 72 in none, 422 in one, 666 in two or more.
- 276 collections have word members; 385 pairs share at least one word; in 55 pairs the shared words are half or more of the smaller collection; merging those 55 would join 86 collections into 32 groups (chaining joins different senses, so each merge is a judgement).
- Size of the 277 collections (all confirmed, none merged): member surfaces counted as the linked terms plus the derived forms of each: median 17, smallest 1, largest 282; 23 have 3 or fewer, 43 have 5 or fewer, 82 have 10 or fewer, 158 have 20 or fewer. Counting only the linked words (core, synonym, opposite, gathered; no phrases, no derived forms): median 7; 64 have 3 or fewer, 113 have 5 or fewer. The narrative has 38 chapters today (`narrative_chapter`); chapter 10 is built by collection (B:127).
- Rows that depend on a collection's id: `ib_node.collection_id` (35,590 filled today by the old base rule), `surface_term.collection_state`, and the link table. How the engagement observations (stage engagement, 527) and the evidence report key their collection has not been read; it is read before any merge (step 1).

## 3. Method for every step

Class by class, never one sweeping run: a pilot of a few concepts by hand first; predicted counts; tried on a copy (`dbsnapshot.copy_db`); a named rollback snapshot; every config write through `apply_logged`; every data change kept in `surface_event` with its reason; nothing physically deleted (links are set deleted, superseded rows keep `superseded_by_id`); counts after equal the prediction or the run rolls back. The researcher does not rule on long lists. I read the members and decide combinations, placements and names by what the words mean, and come to the researcher only for a case I cannot decide from meaning, with the evidence for that case alone. Where I can decide only by word matching I say so. Nothing is decided by script, and each batch is a reading of the members, not a bulk run (B:127). Every ruling of mine is inferential (B:4), and one I would not apply without reading the verses is marked "check" and the verses are read first.

## 4. Steps

0. **Settle the scope first.** Words such as days, right, has and had are neither a behaviour nor an inner-being state: they belong to another group and must not be in a collection, and the same holds for others of their nature, including any that are already in a collection (the 182 in none are a start, `_analytics/surfaces/exports/study-surfaces-no-own-collection-link-v1-20261112.xlsx`). I read the study-group surfaces by meaning, regroup those that are not behaviour or inner-being state through the group step with the reason recorded, and bring to the researcher only the doubtful ones. Also register the rulings of section 1 as a config rule (B:31), and stop any new collection-build or phrase-attach run until the rebuild is done.
1. **Read the dependents.** How `engagement` observations, the evidence report, the members and surfaces exports and the node column read a collection; what a merge must move. Report before anything is merged.
2. **Evaluate every collection as a chapter.** Not only the overlaps: all 277. For each I read its members by tier with the derived forms, the verses it reaches, and the collections nearest to it, and decide by meaning: does it make sense (do the members share one concept), does it overlap another, will it tell a coherent story of how its words work in the inner being. The ruling for each is one of: keep; combine with a named collection; group a small collection with like-minded ones; split (it holds two stories); regroup members elsewhere; remove a wrong opposite membership. The first batch is done: the 55 pairs with half or more shared words, in `_analytics/surfaces/exports/collection-merge-proposals-pairs-v2-20261112.md` (20 combinations I am confident of, 10 clean-ups of opposite membership, 10 medium-confidence matters to check against the verses, and the 6 referred matters, now ruled with the researcher's directions and the verses). Then the 27 more pairs at one third or more, the 82 collections with 10 or fewer member surfaces, and the rest. A combination moves the members to the kept collection (`collection.merged_into_id`, status merged) and keeps the old link rows as history; a split makes a new collection with its members moved. I come to the researcher only for a collection I cannot rule on from meaning.
3. **One collection for each remaining overlapping word.** After step 2 the overlap is measured again; the surfaces still in two or more collections should be few. For each I name the one collection from the senses of the word in its verses and the opposite rule of section 1; only a case I cannot settle from meaning goes to the researcher, with its verses.
4. **Phrases.** For each phrase I decide the one concept it carries (usually the action word with its feature) and place it in that collection by meaning, reading its verses where the sense is not plain; a phrase I cannot place goes to the researcher. The other phrase links are set deleted. The phrase rule (`attach_phrases`) is retired as it stands.
5. **Members are surfaces.** Each derived form gets its own link to the collection of its base once that base is in one collection (the 633), and the 182 are placed or regrouped from step 0. The base stays an instrument, no longer the member.
6. **Names.** Each collection's name is checked against its members: the base stays where it represents them; where it does not, I reconsider it and set a name that covers all the members. No chapter number or title is designed here.
7. **Recompute and verify.** `ib_node.collection_id` for the nodes, `surface_term.collection_state`, the exports and reports; then the checks that matter, each a list, not a percentage: every in-scope surface not in exactly one collection (target none); every collection without a ruling from step 2 (target none); and the verses reached by the collections.

## 5. Decided by the researcher (#2491 v12), and what is asked now

Decided: the order of section 4 is acceptable and may be revisited as later steps change earlier ones; the base is the name where it is suitable and is reconsidered where it is not, and the chapter heading is derived from the name but need not equal it; the unit is the surface, not the Strong's code; the non-member links stay as part of the logic of the members unless they point to a surface; the never-grouped surfaces are left out; smallness is judged on context and likeness; no chapter numbers or titles are designed.

Asked now: approve this plan (v3) and the way of working in section 3, and say whether I am to apply the combinations of the first batch that I marked as confident (section A of the batch file, 20 combinations, the opposite clean-ups of section B and the ruled matters of section D) in a small batch, tried on a copy and kept reversible, or hold until you have read the batch file.

## 6. Limits

Counts depend on the definitions stated; the overlap between collections is measured on single-word core, synonym and opposite members only. The rulings of the first batch were made from the member words, without reading verses, and are inferential (B:4); the story test is a light estimate. Where a ruling rests on a word's sense in its verses, it is marked "check" and the verses are read before it is applied.
