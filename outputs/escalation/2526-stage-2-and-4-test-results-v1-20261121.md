# #2526 / #2528 Stage 2 and stage 4 rebuilt: test results (v1, 2026-11-21)

Both stages were rebuilt on the researcher's answers on #2526 (Q1 to Q7). Tests ran on copies of `iba.db` carrying the configuration (never the live database); the live database received only the two configuration migrations, each after a named snapshot. Proposal: `2526-grouping-and-subgrouping-proposal-v1-20261121.md` (4.10, 5.1 to 5.3). Stage 4 design: `2528-stage-4-design-v2-20261121.md`. This file replaces `archive/2528-stage-4-test-results-v1-20261121.md` (the verse-first stage 4, 44 of 44, no longer the design).

## Stage 2 (`lib/collectiongroup.py`; test `iba/app/tools/temp_2509_grouping_test_run.py`): 28 of 28

| Group | Cases | What they check |
|---|---|---|
| Configuration | B1 to B3 | The lexical items carry no inner-being role or question; the alignment check is clean; the steps, grants and four method rules are registered |
| Pull | P1 to P4 | One row for each surface (not each code); each has its codes with counts and sense as a pointer, a spread of its verses with text, its family; no row is split by code; the codes shown sum to the occurrences counted independently from `verse_lexical` |
| Refusals | R1 to R9, R8b, R8c | A surface unanswered, a group not in the list, an empty group, a short definition, a set-aside without reason, an uncertain placement without what is open, a row answered twice, an answer by code, a row naming a code, a surface not in the index: each refuses the whole file; none writes |
| Write | W0 to W8 | Preview writes nothing; the record makes the group and places the surfaces; a second record changes nothing; a regroup moves one surface; the scrutiny report; the grouping gate; step 1.1 still refused until stage 1 closes |

**Acceptance on `thought` (on a copy only, not the study's record).** A pull of the 33 surfaces took 0.2 s and 97 KB. Recorded with the researcher's three groups (starting, weighing, kinds of thought) for the surfaces the researcher named, a fourth subgroup for `thought` and `thoughts` (Q4), and my placement of the rest flagged uncertain (regard, regarded, reason, suppose, supposing, weigh, weighing): 4 subgroups, 33 placed, 0 set aside; the report lists each. The agreement on the named surfaces is by construction; the test shows that the file carries the evidence for the judgement and that a collection of this size is recorded in one file. The study's grouping of `thought` is standard-mode work.

## Stage 4 (`lib/layerinner.py`; test `iba/app/tools/temp_2526_stage4_test_run.py`): 36 of 36

| Group | Cases | What they check |
|---|---|---|
| Configuration | C1 to C4 | Three observation-led items, the verse-first items gone; items use only items of `reading.observation_items`; rules IB-01 to IB-06 name the new rows; the alignment check is clean |
| Gates and rows | G1, G2, O1 to O4 | 3.1 refused until stage 3 is closed; one row for each subgroup with stage 3 observations (equal to an independent query), none for a verse; 3.2 after 3.1, one row for the collection; 3.3 rows only for partner collections |
| Pull | P1 to P3 | Each row lists the stage 3 observations to take up (equal to an independent query), the verses with text for a read-back, the uses, roles and a fill with traced nodes and read-back; no verse row; 3.2 lists every 3.1 observation |
| Refusals | R1 to R13 | No traced observation; resting on another subgroup's observation; an occurrence outside the observations with no read-back; a read-back of a verse not in the row; the take-up of every stage 3 observation; both rested on and declared; no reason in words; a restated verse; an item the row does not use; a 3.2 row with no behaviour; a 3.1 observation neither gathered nor declared; none writes anything |
| Write and check | W0, W1, K1 to K7 | Preview writes nothing; one observation per finding with stage layer-3, stable key, roles, traced nodes; LayerCheck validates and closes each step; tamper (traced nodes removed) fails the check and answering again repairs it; an occurrence outside the observations validates only while its read-back is on the record; the behaviour is a discovery flag gathering 3.1 observations; a none row with its reason |
| Leftovers | M1 | No ledger row, rule text or config of the verse-first design is left |

Not exercised on this data: a 3.3 row with findings (the test collection reaches the threshold for one partner collection, `sin`, and the row is answered as none); the 3.2 `not_gathered` path ran on the two-observation test data.

## Older tests on copies carrying both migrations

2502 19 of 19; 2503 16 of 16; 2505 47 of 47 (C1 now excludes the new item names); 2507 12 of 12; 2509 28 of 28; 2525 13 of 13. Live: `Config-Maintenance.ps1 -Step Validate`: no new findings.

## Not done

Steps 3.1 to 3.3 and the grouping have not been run on a real collection (study work, standard mode). Open: the N14 flag definition, the F9 content check, the decision to delete the retired cluster reading code and its 10 `reading` rows. The researcher's approval of #2526 and #2528 is pending.
