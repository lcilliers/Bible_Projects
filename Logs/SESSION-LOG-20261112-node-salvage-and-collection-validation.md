# Session log 2026-11-12 — node salvage (#2484, #2487) and validating the collections (#2488) (Developer Mode)

Session id: 8aa10d3c-e70b-4026-80d0-402cd5576939 (started 2026-11-12 04:16 UTC, closed 2026-11-12; the chat was continued once after a context summary).

## 1. Scope

Developer Mode session on the nodes. It began with #2484 (add the collection to every observation node), grew into the node salvage programme #2487 (validate every node, one by one), made the first corrective step (nodes on withdrawn observations withdrawn), and then found that the collections are not a validated base for the node work. The researcher ruled that validating the collections (#2488, raised this session) comes before the nodes cleanup. #2488 then traced how the surfaces, groups and collections were made, listed the surfaces that are not collection members, linked 637 of 679 group B surfaces to collections (tier gathered), and fixed the surfaces export so it counts a link on a derived surface's own row. The session closes with the node work on hold on #2487; the researcher asked for a close and a fresh Developer Mode session to continue the node fixes.

## 2. Escalations

- #2484: read, updated (v2 in progress, v3 design handed over, v4 revise, v5 re-assigned, v6 the researcher's words recorded at the close). Its scope is folded into #2487.
- #2487: raised (v1), updated v2 to v6 with plans v1 to v3, re-assigned for approval; v7 records the first corrective step; v8 puts it on hold behind #2488; v9 records the researcher's words. Plan v3 and the D3 reading are not yet approved.
- #2488: raised (v1) on the researcher's instruction; updated v2 to v14: the corrected counts (916 and 884 surfaces), the history of how the surface groups were made, the T-code finding, the check of the 623 T-only codes (2,226 now), the Part A list, the group B analysis, the links written, the export fix, and the researcher's words.
- #2489: a code-raised coherence finding (two run migrations left unregistered in migration/), resolved self_correctable (v2) after they were archived.
- #2448, #2463, #2481, #2483, #2485, #2486: read at each Stop-hook check, untouched (parked, waiting for the researcher, or behind #2487).
- #2354, #2359, #2361, #2382, #2286, #2292, #2293, #2344, #2372, #2392, #2411, #2366: read only, to trace how the surfaces, groups and collections were made.

## 3. Files

- `iba/app/db/iba.db`: 4,962 live nodes withdrawn (`ib_node.deleted=1`, rows in `ib_observation_change`); 536 new gathered links, 101 associated links superseded by gathered in `collection_link`, 637 `surface_term.collection_state` set to placed, 637 `surface_event` rows (set_tier). Rollback snapshots `iba/app/db/snapshots/kept/iba-20261112T084858Z-pre-2487-withdraw-nodes.db` and `iba/app/db/snapshots/kept/iba-20261112T130805Z-pre-2488-group-b-links.db`.
- `iba/app/migration/archive/withdraw_nodes_of_withdrawn_observations_2487_v1_20261112.py` and `iba/app/migration/archive/link_group_b_surfaces_to_collections_2488_v1_20261112.py`: the two run migrations (archived after the run).
- `iba/app/lib/collectionexport.py`: the surfaces export reads a link on a derived surface's own row (`own_link=True` for both views).
- `iba/app/tools/temp_2488_export_own_link_test_run.py`: the test, 8 of 8 on a copy.
- `iba/app/USER-GUIDE.md` (ExportSurfaces text) and `iba/app/BUILD.md` (entries 493 and 494).
- `outputs/escalation/2487-node-salvage-plan-v3-20261112.md` (v1 and v2 in `outputs/escalation/archive/`); `outputs/escalation/2484-add-collection-to-nodes-design-v1-20261112.md`, `2484-node-surface-vs-verse-lexical-surface-findings-v1-20261112.md`, `2484-node-consistency-checks-design-v1-20261112.md`, `2463-nodes-without-verse-lexical-id-findings-v1-20261112.md`; `outputs/escalation/2488-group-b-links-v1-20261112.tsv` (the per-surface log of the links); the generated escalation list and history reports.
- Read-only workbooks in `_analytics/surfaces/exports/`: `node-validation-v3-plan-v2-20261112.xlsx` (the node export of plan v3; its counts of nodes on withdrawn observations and in scope are now out of date), `t-only-strongs-reached-by-collections-v1-20261112.xlsx`, `study-surfaces-not-collection-members-v1-20261112.xlsx`, `study-surfaces-group-b-subgroup-fellows-v2-20261112.xlsx`; earlier versions in `_analytics/surfaces/exports/archive/`.
- `Logs/compliance/COMPLIANCE-20261112-8aa10d3c.md` and this log.

## 4. Decisions

The researcher's own decisions:
- The scope of the node work is the 277 collections, and rules R1 to R13 (R6 and R7 dropped, R3 relaxed, R12 for entity and other surfaces); recorded in #2487 v2 to v6 and `outputs/escalation/2487-node-salvage-plan-v3-20261112.md`.
- Nodes on a withdrawn observation are simply marked withdrawn; recorded in #2487 v7, BUILD 494 and `iba/app/migration/archive/withdraw_nodes_of_withdrawn_observations_2487_v1_20261112.py`.
- Validating the collections must be done before the nodes cleanup proceeds; recorded in #2488 v1 and #2487 v8.
- Group C (a surface whose own row carries a member-tier link) must be linked to a collection; group A is left (supportive words, pulled in by reading in context); group B is allocated to the collection where the fellow terms of its cluster subgroup landed; recorded in #2488 v8.
- The new links take the tier gathered, and every surface goes to its suggested collection as listed, the few without a suggestion to the unassigned collection (read as `uncovered-words`); recorded in #2488 v9 and v10.
- Leave "trouble" and "troubled" in both collections for now; the 42 held surfaces stay as they are; the 101 own-row links must be included in collections; recorded in #2488 v12.
- Build the export fix; recorded in #2488 v13 and BUILD 493.
- Not now to pulling and assessing the verse items of the 637 newly linked surfaces; recorded in #2488 v14.

Claude's fixes, closed without a decision: the two run migrations were archived to clear the coherence finding, recorded in #2489 v2 and BUILD 494; a wrong figure in a #2488 comment (8,614 for 8,715 live links) was corrected in #2488 v11.

## 5. Open items

For the researcher:
- #2487: plan v3 (the flag, the method, the order 0, A to E) and my reading of D3 (a node follows its observation; entity and other nodes take the collections of their observation's collection-surface nodes, else are held) are not approved.
- #2488: which link tiers make a verse in scope is not settled (member tiers only, all tiers adding 1,690 verses and 1,024 nodes, or associated and set_aside without possible_opposite); the verdict column of `t-only-strongs-reached-by-collections-v1-20261112.xlsx` (2,226 T-only codes, which are inner-being words); the 42 held surfaces (an earlier set_aside or possible_opposite link to the same collection); whether #2488 includes the second pass over the 12,090 surface texts with no group (T-coded, never in the cluster-derived list of 6,069), a sample check of the grouped surfaces (Part D), and the 56 unjudged rows; the 164 derived surfaces whose collection differs from their base's.
- Engagement of the 637 newly linked surfaces (new members of collections already through engagement; 381 unassessed items in `search` alone): the researcher said not now; carried in #2488.

For Claude:
- #2487 resumes after the restart: regenerate the node workbook on the changed collections and scope; then the next node classes in the order 0, A to E (duplicates 4,639 rows, nodes with no role 24,369, surfaceless nodes 9,596 for the researcher, observations that are malformed 1,240), each predicted, tried on a copy, with a rollback snapshot, one class at a time. Nothing beyond the withdrawn-observation step is done.
- The expected counts of `iba/app/tools/temp_2479_phrase_members_test_run.py` need re-basing (P1, P4, P5, P7 fail because of the new links, with or without the export fix); carried in #2488 v13.
- Held parked items: #2448, #2463, #2481, #2483, #2485, #2486.

## 6. Git

(To be written after the first commit.)
