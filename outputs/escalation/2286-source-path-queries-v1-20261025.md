# #2286 prototype step 3: the DB query for each source path, designed in advance

Date: 2026-10-25. Escalation #2286 v7. Every query was run read-only on live iba.db, on one sample
each, and timed. Nothing was built or written. The test script is in the session scratchpad and is
not part of the app.

## 0. The paths as the researcher set them (v7, verbatim)

> a) a cluster must become a subgroup must become a thread must become a verse collection - the entry
> point can pick up on any of these stages b) word is treated as a or a collection of Strongs that
> becomes a verse collection c) verses relates to similar verses to become a collection d) a narrative
> chapter or block have citations which becomes a verse collection e) a claim have citations that
> becomes a verse collection f) an observation is related to a verse that follows c) path.

## 1. Shared pieces

Two steps are common to every path that passes through Strong's codes (a and b).

**S1. Codes to occurring codes** (B:113, bare code decomposed). A given code is kept if it occurs in
`verse_lexical`. A bare code that does not occur stands for its lettered derivatives that do.

```sql
WITH given(code) AS (SELECT value FROM json_each(:codes)),
occ AS (SELECT DISTINCT strong FROM verse_lexical WHERE deleted=0)
SELECT DISTINCT o.strong FROM given g JOIN occ o
  ON o.strong = g.code
  OR (o.strong GLOB g.code || '[A-Za-z]*' AND NOT EXISTS (SELECT 1 FROM occ x WHERE x.strong = g.code))
```

**S2. Codes to verses.** One set-based query (B:71), with no loop over verses:

```sql
SELECT DISTINCT verse_id FROM verse_lexical
WHERE deleted=0 AND strong IN (SELECT value FROM json_each(:codes))
```

## 2. The paths

### a) Cluster, then subgroup, then thread, then verses

| stage | query | sample result |
|---|---|---|
| a1 cluster to its codes | `SELECT DISTINCT strong FROM cluster_strong WHERE cluster_code=:cluster AND deleted=0`, then S1 and S2 | M49 (thanksgiving): 5 codes, 193 verses, 0.18 s |
| a1 cluster to its subgroups | `SELECT subgroup_code, label FROM cluster_subgroup WHERE cluster_code=:cluster AND coalesce(delete_flagged,0)=0 ORDER BY sort_order` | M49: 5 subgroups |
| a2 subgroup to its codes | `cluster_subgroup_strong` joined to `cluster_subgroup` on the subgroup code, live rows only, then S1 and S2 | A_thanksgiving_act (the verbal act of giving thanks): 1 code (G2168), 38 verses |
| a3 cluster to its open thread items | `escalation_thread_item` joined to `escalation`, `status='open'`, where `target_cluster=:cluster` or the item is a cluster item naming it | M49: OT-97.41 and OT-103.65, both scope items |
| a4 thread to verses | the open items of the thread joined to `escalation_thread_item_verse` (live rows) | OT-103: 536 verses, under 0.01 s |

**What the data shows about this chain:**

- **a-i. Subgroups exist for only 3 of the 80 live M clusters:** M49 (thanksgiving), M67 (diligence
  and idleness) and M83 (seeking). There are 13 subgroups and 21 subgroup-to-code links in all. For
  the other 77 clusters the stage "a cluster must become a subgroup" has no data.
- **a-ii. A thread is not a child of a subgroup in the data.** Thread items carry `target_cluster`
  but no subgroup. Open thread items are almost all cross-cluster pairings: 296 of the 305 open items
  are of kind `scope`, worded like `M49: H2534+H0599+H0639G x H3034 (2 verses)`. Their verses are
  already held in `escalation_thread_item_verse`; every open scope item has verse rows. So today the
  link from a subgroup to a thread can't be queried, only the link from a cluster to a thread.
- **a-iii. The resolver as built misses scope items.** `versescope.py` `_item` (lines 300 to 311)
  resolves item kinds verse, cluster, strong, chapter and strand. Any other kind is listed as "names
  no verse", so `-Thread` and `-Item` drop the 296 open scope items. Query a4 reads their verses
  directly. This is recorded as its own open item, #2287.
- **a-iv. The strands are over.** All 4 rows in `reading_strand` are `superseded`, so the strand
  selector has nothing live to read.

### b) Word, as one or more Strong's codes, then verses

| stage | query | sample result |
|---|---|---|
| word to codes | `SELECT ws.strong FROM word_registry w JOIN word_strong ws ON ws.word_id=w.id AND ws.deleted=0 WHERE w.word=:word AND w.deleted=0` | conscience: 3 codes (G4893, G4894, H3629) |
| codes to verses | S1 and S2 | 58 verses, 0.13 s |

`word_registry` holds 180 live words and `word_strong` holds 4,621 links. A word that isn't in the
registry can't take this path; it has to be given as Strong's codes.

### c) Verse, then similar verses

The tables give no single meaning of "similar". I found four relations that can be queried. Each was
run on Psa 51:10 ("Create in me a clean heart, O God, and renew a right spirit within me"):

| relation | query | Psa 51:10 |
|---|---|---|
| c1 same passage | `verse_passage` joined to itself on `passage_id` | 0: only 42 passages (777 verses) are defined, and Psa 51 is not one |
| c2 same M-coded word | each word of the verse that has an M cluster (`cluster_strong`, `cluster_code LIKE 'M%'`), then every verse holding that same lettered code | 829 verses, 0.16 s |
| c3 related word | as c2, but through `strong_related` to the related codes | 2,338 verses, 0.30 s |
| c4 neighbours | the verses within 2 of it in the same book and chapter (`verse_meta.chapter`, `verse_num`) | 5 verses: Psa 51:8 to 12 |

Why c2 is so wide: the verse's five M-coded words are H2889 (clean, M61, 87 verses), H3820A (heart,
M47, 550), H2318 (renew, M45, 10), H3559K (right, M23, 12) and H7307G (spirit, M47, 194). The two
inner-seat words, heart and spirit, bring in almost everything.

### d) Chapter or block, then its citations, then verses

```sql
SELECT DISTINCT verse_id FROM narrative_citation
WHERE last_version IS NULL AND section_id=:section AND verse_id IS NOT NULL
```

A chapter is the same query over all of its current blocks. Citations that don't resolve are listed
by `verse_id IS NULL`: 37 of the 7,477 live citations. Sample: block 10.5 "The tongue, the lips and
the eyes devise" gave 5 verses, none unresolved.

### e) Claim, then its sources, then verses

```sql
SELECT s.source_kind, s.verse_id, s.observation_id, s.ref_as_written
FROM narrative_claim_source s JOIN narrative_claim c ON c.id=s.claim_id WHERE c.claim_ref=:claim
```

Sources come in four kinds:

| kind | count | becomes |
|---|---|---|
| verse | 2,096 (1 with no verse) | `verse_id` |
| observation | 87 | path f, through `observation_id` (the resolver as built lists these as "not a verse") |
| study file | 40 | no verse: listed |
| lexical | 5 | no verse: listed |

Sample: claim C-88 has 19 sources, verse and observation together.

### f) Observation, then its verse, then path c

```sql
SELECT DISTINCT v.id FROM ib_node n JOIN verse v ON v.osisId=n.verse_reference AND v.deleted=0
WHERE n.observation_id=:obs
```

All 16,901 nodes resolve to a verse. Sample: observation 204 is on 3 verses. From there the path is
c, so it shares c's open question.

## 3. What is open for the researcher

| # | question | the facts behind it | your answer |
|---|---|---|---|
| Q1 | **Path a, the subgroup stage:** 77 of the 80 M clusters have no subgroups. Is making the subgroups part of the work unit step (RM-03, the overview that segments a cluster), or do they have to exist before a cluster can be a source? | a-i | |
| Q2 | **Path a, subgroup to thread:** threads are cross-cluster pairings, not children of a subgroup. What links a subgroup to a thread in your chain: the subgroup's codes appearing in a thread item's terms, or a link still to be made? | a-ii | |
| Q3 | **Path c, "similar":** which relation, or which mix of them, makes a verse similar: same passage, same word, related word, neighbours, or something else? c2 and c3 run to hundreds or thousands of verses because of the seat words. Should the seat words (M47) be left out of the similarity? | section c | |
| Q4 | **Path e:** do a claim's observation sources go on through path f, and so through c? | section e | |
