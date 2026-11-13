# Session log 2026-11-13 — the node cleanup and the rebuild of the collections (#2487, #2491)

Session id: 4809e505-4396-4642-9c53-39171b55d802 (Developer Mode; started 2026-11-12 13:31 UTC, continued after a compaction, closed 2026-11-13).

## 1. Scope

A Developer Mode session on the IBA app and its data. It began as the node cleanup (#2484 to #2488: out-of-scope nodes and observations withdrawn, the collection put on the node) and turned, when the researcher found that the collections were not a valid base (a surface such as despised in no collection, words in several), into the rebuild of the collections (#2491, plan v3, steps 0 to 7): 277 collections became 169, every one of the 3,371 study surfaces (words and phrases with a verse) is now in exactly one collection, generic words were regrouped to other, phrases placed one concept in one collection, derived forms given their own link, names checked, the researcher's rulings registered as `cfg_behaviour_rule` 129, the three readers of a collection's members made to follow the rule, USER-GUIDE.md revised, out-of-scope nodes withdrawn again. Every ruling is my reading by meaning (B:4) and reversible from the named snapshots.

## 2. Escalations

- #2491 (raised in this session: the collection rebuild): updated v1 to v27 and at close; plan v3 written and approved; handed to the Researcher as ready_for_approval (approval sought: the rebuild, plan v3 steps 0 to 7, is complete as verified, so it can close).
- #2487 (salvage of the nodes): updated (v10 to v19), on hold, ready_for_approval with the Researcher; the one-by-one validation is superseded by #2491 and is not planned.
- #2488 (validate the collections as the base for node work): completed in this session (679 group B surfaces linked at tier gathered; sign-off prepared).
- #2484 (add the collection to every observation node): updated (v6, v7); ready_for_approval with the Researcher; the column was built and filled, the node-writing path (D5) is not done.
- #2490 (group B links: unassessed items, 2479 test re-basing): raised and held; commented at close (v2).
- #2463, #2448, #2481, #2485: commented at close with the effect of the rebuild; left in their states (in-progress or on-hold), assigned to Claude, not started.
- #2486 and #2483: read, left untouched (raised items cannot take a comment without moving off raised).
- #2489: completed by an earlier step of the session (two unregistered migrations moved).

## 3. Files

- Code and config: `iba/app/lib/collectionexport.py`, `iba/app/lib/collectionevidence.py`, `iba/app/handlers/collectionbuild.py` (attach_phrases refuses a writing run), `iba/app/USER-GUIDE.md`, `iba/app/BUILD.md` (entries 495 to 513), `.gitignore`; `cfg_behaviour_rule` 129 with `cfg_rule_scope` B:129 and `cfg_utility` through `configmaint.apply_logged`; `ib_node.collection_id` (`cfg_column`).
- Migrations (all run, then archived), in `iba/app/migration/archive/`: `node_collection_2487_v1_20261112.py`, `withdraw_out_of_scope_nodes_2487_v1_20261112.py`, `withdraw_surfaceless_nodes_2487_v1_20261112.py`, `collection_merge_batch1_2491_v1_20261112.py`, `collection_merge_batch2_2491_v1_20261112.py`, `collection_regroup_step0_2491_v1_20261113.py`, `collection_one_place_step3_2491_v1_20261113.py`, `collection_phrases_step4_2491_v1_20261113.py`, `collection_phrases_step4b_2491_v1_20261113.py`, `collection_derived_step5_2491_v1_20261113.py`, `collection_derived_step5b_2491_v1_20261113.py`, `collection_names_step6_2491_v1_20261113.py`, `collection_longtail_2491_v1_20261113.py`, `collection_uncovered_2491_v1_20261113.py`, `collection_rules_2491_v1_20261113.py`, `collection_verify_fix_2491_v1_20261113.py`, `collection_twentythree_2491_v1_20261113.py`, `collection_nodes_recompute_2491_v1_20261113.py`, `withdraw_out_of_scope_nodes_2491_v1_20261113.py`.
- Plans, rulings and reports: `outputs/escalation/2491-collection-rebuild-plan-v3-20261112.md` (v1 and v2 in `outputs/escalation/archive/`), `outputs/escalation/2491-verification-step7-v2-20261113.md` (v1 archived), `outputs/escalation/2487-no-surface-nodes-collection-plan-v1-20261112.md`, the escalation histories `outputs/escalation/2484-escalation-history-v2-20261112.md`, `outputs/escalation/2487-escalation-history-v1-20261112.md`, `outputs/escalation/2488-escalation-history-v1-20261112.md`, the escalation list `outputs/escalation/escalation-list-v269-20261113.md`.
- Analytics (`_analytics/surfaces/exports/`): `collection-merge-proposals-pairs-v2-20261112.md`, `collection-merge-proposals-batch2-v1-20261112.md`, the workbooks `node-validation-v5-plan-v3-20261112.xlsx`, `node-several-collections-samples-v1-20261112.xlsx`, `study-surfaces-no-own-collection-link-v1-20261112.xlsx`, `study-surfaces-against-one-collection-rule-v1-20261112.xlsx` (older versions in `archive/`).
- Session records: `Logs/compliance/COMPLIANCE-20261112-4809e505.md`, this log, `iba/app/reports/session-close-v356-20261113.md` (and its successors).
- Named snapshots (`iba/app/db/snapshots/kept/`, not committed): one before each live run, from `...pre-2487-withdraw-nodes.db` to `iba-20261113T043607Z-pre-2491-nodes-recompute.db`.
- Left out of the commit and ignored: a stray `_analytics/surfaces/exports/.claude/` (hook state written when a command ran with that folder as the working directory); `.gitignore` now ignores `_analytics/**/.claude/`.

## 4. Decisions

- Researcher: the model of a collection (each in-scope surface in exactly one collection; built on surfaces, the base an instrument; a phrase one concept; an opposite sits once; close and small collections combined; names from all members; each a chapter of the narration, light evaluation only; generic words regrouped; Claude decides by meaning and comes only where it cannot). Recorded in `cfg_behaviour_rule` 129 and #2491 v27.
- Researcher: 'no need for a link table' (a node carries one collection; a surface in several collections means the verse decides). Recorded in `iba/app/BUILD.md` entry 497 and #2487 v19.
- Researcher: withdraw the out-of-scope nodes and their observations, at 2026-11-12 and again after the rebuild ('Yes, withdraw'). Recorded in `iba/app/BUILD.md` entries 495, 496 and 509 and #2487 v19.
- Researcher: apply the merge proposals (batch 1, batch 2, section D) and go ahead with each of steps 0 to 6, the long tail, the review of uncovered-words, step 7, the 23 surfaces and the documentation. Recorded in `iba/app/BUILD.md` entries 498 to 512 and #2491 v27.
- Researcher: refused a coverage ledger as a check ('it is bad idea'). Recorded in #2491 v27.
- Claude, self-correctable: the wrong early counts retracted; the union node rule replaced by the own-row rule after a check failed (I had started the live step before reading the copy's failing check); the list slips of steps 4, 4b and 10 placed; the readers made to follow the rule. Recorded in `iba/app/BUILD.md` entries 503, 510, 511 and 512.
- Claude, a decision I should have put to the researcher: the code fix of the three readers (BUILD 512) under the go-ahead to revise documentation. Recorded in `Logs/compliance/COMPLIANCE-20261112-4809e505.md` (conflicts) and #2491 v27.

## 5. Open items

- #2491 (Researcher): approval that the rebuild is complete as verified, so it can close.
- #2487, #2484 (Researcher): both already with the researcher as ready_for_approval from earlier in the session.
- #2477 (Researcher): the evidence report as built (from an earlier session, untouched).
- #2448, #2463, #2481, #2485, #2490 (Claude, held, not started): they depend on the rebuild, which is now finished; #2481 needs a fresh reading because phrases now sit in one collection.
- #2483, #2486 (Claude, raised, not started).
- #2492 (Claude, raised at the close): the loose ends of the rebuild that were in no item: the node-writing path of the reading step does not yet set the collection on a new node (D5 of #2484); the 11,175 never-grouped surface texts are outside the collections by the researcher's ruling and were not searched for behaviours or states; the test runs temp_2393 and temp_2479 of the exports were not re-run after BUILD 512, and the evidence report and engagement were not compared before and after.

## 6. Git

Branch: main. Commit 6b142c52b92eae5e69a68489d6490d3c94f9cf72 (session 20261113: node cleanup (#2487) and rebuild of the collections (#2491) ... 55 files, 5,356 insertions, 39 deletions). Push output: `To https://github.com/lcilliers/Bible_Projects.git   dd619bd9..6b142c52  main -> main`. Session-Close.ps1 exited 0 (0 open findings) before the commit, report `iba/app/reports/session-close-v357-20261113.md`. The named snapshots and the database are not committed.
