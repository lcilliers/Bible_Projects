# #2486 Cross-link every claim to its collection: design v1 (2026-11-13)

Status: design for the researcher's decision. Nothing built or changed. Read-only queries on `iba/app/db/iba.db`.

Researcher instruction (2026-11-13, verbatim): "next is to work through claims and ensure that each claim is connected to its collection based on the surfaces".

## What I read (B:123)

`cfg_table`/`cfg_column` text for `narrative_claim` (393 rows), `narrative_claim_source`, `ib_node`, `collection`, `collection_link`.
- A claim's sources are mostly verses: 2,095 of 2,096 verse-kind rows carry only `verse_id`. There is no surface on a claim source.
- 87 source rows (66 claims) are kind `observation`, carrying `observation_id`; an observation's live nodes carry a surface and `collection_id` (#2484).
- Other kinds: 40 study file (40 claims), 5 lexical (5 claims).
- `narrative_claim` has no collection column and no link table. `main_chapter_id` exists, but chapters have no collection link (38 chapters).

## What the data shows

| Route | Claims reached | Collections per claim |
|---|---|---|
| Via the claim's verses (any live node in the verse) | 355 of 393 | median 6, max 32; 68 claims have more than 10 |
| Via the claim's observation sources (their live nodes) | 64 | median 2, max 7 |
| Neither | 38 (12 withdrawn, 13 current not in narrative, 8 current in narrative, 5 held) | none |

Of the 64 claims reached by both routes, the observation route is a subset of the verse route for 50; 14 differ.

The verse route is too wide to be "based on the surfaces": a verse carries every collection that has a surface in it, so a claim about one word would be linked to 6 to 32 collections. The claim's own sources never name the surface, so the surface has to come from somewhere else.

## Decisions needed (B:44, B:105)

1. **Form of the link.** Recommend a link table `narrative_claim_collection` (claim_id, collection_id, basis, surface, created_at, created_by, deleted), because a claim may bear on several collections. Alternative: one `main_collection_id` column on `narrative_claim`, which loses the several-collection case.
2. **Where the surface comes from.** Options:
   - (a) Observation route only: the surfaces of the live nodes of the claim's observation sources. Precise (median 2), covers 64 claims.
   - (b) For claims with verse sources only, the surfaces in the claim's verses that the claim text actually names or rests on. Needs a reading of each claim, by me with you, not a word match (B:127, B:129 say not to assign by pattern). Covers the other 291 claims reachable by verse.
   - (c) Verse route as is. Not recommended (fan-out above).
   Recommend (a) as the migration, then (b) claim by claim in your reading, each link stored with its basis (`observation` or `read`), so a link is traceable.
3. **Where the two routes differ** (14 claims): recommend the observation route decides and the difference is listed for you.
4. **Claims with no collection** (38): recommend they stay unlinked and are listed; the 12 withdrawn need none. The 8 current claims told in the narrative and the 13 current ones not told need a decision each.
5. **Chapters.** Recommend a chapter-to-collection link is a separate step after claim links exist (the narrative chapter is built by collection, B:127); not part of this item.
6. **Meaning in config.** New table and columns get `cfg_table`/`cfg_column` rows by the stated procedure in `iba/app/USER-GUIDE.md`, registered through `apply_logged`; trial on a copy under a named snapshot, counts predicted and checked; BUILD entry.

## Not decided here

Whether claim-level links come from reading each claim with you (b) or are limited to (a). Everything else above follows from your answer to 1 and 2.
