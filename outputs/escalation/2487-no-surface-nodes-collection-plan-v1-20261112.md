# #2487 — Nodes with a verse and no surface: collection from the verse (plan v1 for approval)

Plan only. Nothing built, nothing changed in iba/app/db/iba.db. Read-only counts, 2026-11-12, after the #2488 links.

## 1. Rules I hold (re-read from #2487 plan v3, #2484 v4 and the design files)

- A node has one surface; a node cannot exist without an observation; a finding is an observation plus its nodes (R1, R10).
- Every in-scope node carries the collection(s) of its surface (R2, R11); the collection replaces cluster and subgroup, which are history only (R13).
- Researcher, #2484 v4: every verse-related node should have a surface; every node without a surface needs the researcher's attention.
- Every write through apply_logged with a row in ib_observation_change, counts predicted, tried on a copy, named rollback snapshot, then live (plan v3 section 5). A class is proven by hand on a pilot before it runs in bulk.

## 2. What the data holds

All 10,225 live nodes with no surface are prior-capture draft nodes of 2026-10-26 on 3,445 observations (stage prior-capture, status draft). 10,179 have a verse (the workbook's 9,920 are the in-scope ones). None has a Strong's code or verse_lexical_id (strong set on 2, verse_lexical_id on 1); 5,989 have a role.

Collections reached through the verse (own-kind words of the verse that are surfaces of member bases; tiers core, synonym, opposite, gathered, phrase; own row or base):

| the verse reaches | nodes | observations |
|---|---|---|
| no collection | 259 | 226 |
| one collection | 663 | 497 |
| several, and the observation text names a surface of one collection | 970 | 609 |
| several, and the observation text names surfaces of several collections | 1,142 | 714 |
| several, and the observation text names none of them | 7,145 | 2,716 |

"Several" is the norm: the median verse reaches about four collections, the most 71. The text test is a word match of the observation text against the verse's collection surfaces (rough, inferential, B:4).

## 3. What stops a direct run

1. **Most of these observations do not name a word.** 7,145 nodes (70%) sit on observations written at cluster level ("Face A, felt before a threat or a person: trembled, trembling, afraid ..."): the text gives no way to tell which of the verse's several collections it is about. Picking one, or giving the node all of them, is a judgement made by a script (B:127, B:19). The same observation is on several verses, and its words differ verse to verse.
2. **Where to store the collection.** ib_node has no collection column. Splitting a node into one new node per captured word, each with one collection, needs a column (#2484 D2 option B). The link table (D2 option A) keeps several collections on one node. D1 to D5 of #2484 are still unapproved.
3. **A new node needs a surface and a verse_lexical_id** (R10; the general verse_lexical_id fill is #2485). The captured word gives the surface; its Strong's code and verse_lexical row come from the verse word, and a word that occurs twice in a verse needs a rule.

## 4. Proposal

Done in classes, one at a time, each predicted and tried on a copy, a pilot by hand first:

- **Class 1, one collection on the verse (663 nodes):** the node takes that collection. No judgement.
- **Class 2, several collections, the observation names the words (2,112 nodes; 970 resolve to one collection, 1,142 to several):** each captured word becomes a node (one surface, its collection, its Strong's code and verse_lexical_id from the verse); the original surfaceless node is withdrawn with a reason, or takes the first word. About 3,131 captured surfaces in all; exact rows from the pilot.
- **Class 3, no collection on the verse (259 nodes):** list for you (no collection means entity or other words only, or an inner-being word in none).
- **Class 4, several collections, no named word (7,145 nodes, 2,716 observations):** not touched by rule. A list per observation for you, grouped so you decide per observation (restate it, withdraw it, or name the collection and word), as #2487 R2 and "malformed observations" already provide. I draft the restatements.

## 5. What you are asked to decide

1. **Storage:** one collection per node as a column `ib_node.collection_id`, with a new node for each extra word (needed for your "create new nodes" instruction), or the link table with several collections on one node (#2484 D2 A).
2. **Class 4:** agree it is not decided by rule and comes to you per observation, or give the rule you want applied.
3. **Class 2:** the original surfaceless node withdrawn, or kept as the first word's node.
4. Approval of the classes and order in section 4, with a pilot on a few verses before any bulk write.

Limits: counts from one read-only pass; the word match is rough; scope by surface text is inferential (B:4).
