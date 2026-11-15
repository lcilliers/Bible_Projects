# #2448 The study plan as the researcher recorded it, and where each step stands in config and code (v1, 2026-11-15)

Status: read from the written record only (session logs of 2026-11-09 to 2026-11-14, #2448 history v1 to v15, #2463, #2486, #2491, #2498, #2495, #2505, #2507). Nothing changed. Where the record is silent it says so. This file exists because the plan was held in about forty comments and fourteen session logs and in no single place; it is a map of them, not a new design.

## 1. The plan as recorded: the chain from the base data to the narrative

| # | Step (the researcher's words or the escalation's title) | Source | State |
|---|---|---|---|
| 1 | Surfaces, base forms, families, then collections of surfaces by likeness of meaning | #2360 (superseded), #2361 completed | Done. 169 collections after the rebuild; each of 3,371 study surfaces in exactly one (#2491 completed; rule B:129) |
| 2 | Engagement: what each surface of a collection does for the inner being, per verse | #2406 completed | Built. #2412 (run it on all collections) was withdrawn on 2026-11-11: "engagement will in future be part of the end-to-end study of each collection" (log 20261111, engagement planning) |
| 3 | The collection on the node; cluster and subgroup retired from nodes and observations | #2484, #2487, #2495 completed; rules B:130 and B:131 | Done in code and rules for nodes and observations |
| 4 | Prior study documents re-read into the observations, read only for the verses in scope, folded into the collection reading | #2498 completed (pilot of two documents); requirement carried on #2448 v11 and v12 | The pilot is done; the general method is not built (it is a requirement of #2448) |
| 5 | The evidence of a collection, base data to narrative | #2464, #2477, #2502 | Built; reports exist for thought |
| 6 | Layered claim reading: layer 1 groups and Strong's enrichment, layer 2 pairings, then the claims; lexical work and claims readings never run together; layer 2 has a lexical-structural set and an inner-being set | #2463 v16 to v36, #2503, #2505, #2507 | Layer 1 and layer 2 machinery built (#2505, completed). The lexical-structural observations by collection have no process (#2507 open). No collection has groups yet |
| 7 | Claims cross-linked to collections; what a claim is and does; claim work-up and binding | #2486 re-assigned, with the researcher | Design drafts and a trial on a copy; nothing in live config |
| 8 | The final reading, and the narrative, based on collections not clusters; chapter 10 one sub-chapter per collection; a step between collections and narration | #2448 (on hold), #2376 (on hold), #2406 | #2448 design C1 to C7 approved on 2026-11-10 (v4, v7); the change list and test plan (v8) was never answered; put on hold "until #2412 is completed" (v9) |

## 2. What #2448 already holds (and I treated as parked work, not as the plan's last link)

- **Approved design (C1 to C7, 2026-11-10):** a reading opens on one collection (new column `reading.collection_id`), its members' verses, the engagement observations per verse with the verse read first, a gap is a member surface with no engagement assessment in a verse of the scope, output folder per collection, a pilot on one collection first, existing cluster readings kept as history.
- **Requirements added since:** the Observe sheet carries the lines of the indexed documents that name each verse, with a word-match gap list (v11); the reading Record sets the collection on a new node by the own-row rule (open point D5 of #2484, found again in the pilot) and accounts for each document line (v11); the classes the node checker still lists, to be worked as each collection is read (v12); the node validation flag of ruling N14 (v12); retire behaviour rules 119 and 120 and method rules RO13, RM-03 and RO8 **in the same unit of work as the code** of the collection Open (v13).
- **The hold is stale.** Its condition was #2412, which was withdrawn and replaced by "engagement is part of the end-to-end study of each collection". #2448 has been acknowledged at every Stop-hook check and not started.

## 3. Where the old processes still stand (from outputs/escalation/2507-legacy-scan-v1-20261115.md)

- `Reading.ps1 -Step Open` still takes exactly one subgroup as its home; `reading.home_cluster` is NOT NULL; the reading folder is the home cluster's; `Verse-Scope.ps1` and `Verse-Collate.ps1` still take Cluster, Subgroup and Strand.
- 77 active method rules on the reading steps; one names a collection or layer. RG-01 to RG-25 and RS-01 to RS-10 still describe one pass in which the lexical reading and the inner-being reading are done together.
- Seven active `verse-lexical` steps, all naming cluster, passage or book; `lexical.meaning` and `lexical.relational` are active and cluster-based; `lexical.enrich` and `lexical.run` were retired on 2026-09-07 (#1549) because they were built on books and passages, and nothing replaced them by collection.
- Cluster rules not touched: B:94, B:116, rules 55 to 100 that name clusters, and settings in the report, cluster and validation modules.

## 4. Where I broke the recorded sequence

#2448 v12 and v13 and my own note on 2026-11-13 say: rules 119 and 120 and RO13 retire when the collection Open exists, in the same unit of work as its code. On 2026-11-15, under #2505, I reworded B:119 and B:120 for collections and retired RO13 without the code. The rules now say the collection is the work unit while `Reading.ps1 -Step Open` still opens a subgroup. That is a stored rule and an enforcing code that disagree.

## 5. What is not recorded and has to come from the researcher

- Whether the lexical-structural observations (not inner-being aware) are produced by the engagement step, by a new step, or by an adapted `lexical.meaning` and `lexical.relational`. The record names the need (#2463 v22, #2507) and not the process.
- The answers to the #2448 v8 questions (the table migration of `reading`, standard mode) and to the #2486 open decisions.
- Which of the stages and kinds of observation made before 2026-10-31 stay as history and which are re-read into the layers.
