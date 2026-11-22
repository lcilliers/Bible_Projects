# Validation pilot, part 3: the actions applied on 1Chr.28.9

Escalation #2538, 2026-11-22. Plan: `2538-validation-step-plan-v9-20261122.md` (principles 13 and 14, section 8). Reading: `2538-validation-pilot-reading-1chr-28-9-v1-20261122.md`.
Everything was done on a **copy** of the live database, through the new library `iba/app/lib/validationactions.py`. The live database was not touched (it has no `nature` column and no change row of these runs). Results are reproducible: `python iba/app/tools/temp_2538_validation_apply_1chr28_9.py <scratch dir>`.

## What was built

One library module of 21 functions (set the marker; defer a finding to a named collection; annotate any observation, deleted or live; complete a node's role or collection, or record why a column stays empty; restate with the base-data check named; trace to evidence; create an observation or evidence observation; add, move or drop a node; consume an observation into the ones that carry it; delete an observation that is neither; record self-evidencing; report trace gaps). Each keeps its change and reason in `ib_observation_change`. 53 test cases on a copy of the live database, all PASS (list in BUILD.md §547). Not built yet: the entry point and registered step, the `cfg_method_rule` row IB-07, the migration of the live database, the USER-GUIDE entry, the amendment of B:132 and B:133.

## What was done to the 55 observations

| action | count | which |
|---|---|---|
| marked (evidence 32, inner being 18 among the 50 live) | 55 | all |
| deleted as neither (comment first, ruling of 2026-11-22) | 6 | #19613, #19915, #20029, #20345, #20414, #20427 |
| consumed into another and deleted | 3 | #7320 into #7319; #22524 into #22604; #22525 into #22608 (the traces of the survivors re-pointed to the sources of the consumed one; no live trace points at a deleted observation) |
| restated, each checked against the verse table | 17 | #5797, #7317, #7319, #12413, #12431, #17167, #20216, #20549; the outline numbers or marks of the earlier document taken out of #16318, #17012, #17057, #17271, #20019; #22623 (count and the omitted serve); #20455, #20498, #20489 (the claim carried elsewhere taken out) |
| created | 4 | three evidence observations (#22669 who knows thoughts; #22670 seek before find; #22671 knowing ahead, H3336) and one inner-being observation split off #5797 (#22672, the mirrored darash) |
| node roles completed | 38 | on #5793, #5797, #7091, #7303, #7317, #7319, #7320, #12412, #12413, #12431 |
| nodes with the collection still empty: reason recorded | 8 | surfaces that belong to no single live collection (Hab.2.18 creation, Ps.103.14 frame, Ps.73.21 soul, Lam.1.16 spirit, on #12412, #17270, #17271) |
| recorded self-evidencing | 5 | #19501, #20216, #20455, #20498, #20549 |
| traces added | 4 plus the evidence traces of the creations | #20019 to #12412, #17271 to #17270; #12431, #7319, #7303, #12413 to the created evidence |
| deferrals to a named collection | 25 rows | see below |
| notes on deleted observations with no recorded reason | 26 | the 26 the researcher named (found by the rule, not by id); they stay deleted |

Final state of the live set: **50 observations; 0 word nodes missing a required column; 0 live traces to a deleted observation; every inner-being observation traced to marked evidence or recorded self-evidencing, except 3 deferred to the search and the compound's collections, and 2 whose traces point at layer-2 observations outside this verse that are not yet marked (they are marked when thought's whole scope is validated).** All 154 nodes on the verse still match `verse_lexical`.

## What was deferred, and to whom (principle 14)

Only where another collection's validation will touch the observation (its nodes carry that collection):

- **search (156):** #5793, #5797, #7091, #7303, #7317, #7319 (consumption check; the sense of seek and searches against the meaning tree); #21752 (restate to the verses held as nodes, trace it); #21757 (the other 78 verses).
- **intend (78):** #12412, #12413, #20019, #20549 (do its observations carry the H3336 findings).
- **forsake (47):** #17167, #19508. **serve (24):** #16318, #19501. **desire (9):** #17012.
- **heart (102):** #17057, #17270 (split the parallels, one finding each), #17271.
- **#20489** (five claims left, one observation): design to skill (184), reckoning to count (201), inner speech to heart (102), the body and emotions to fear (2), the creaturely and passing to intend (78). Its sixth claim (fully open to God) is carried by #22669 and #12431.

Not deferred, done now: everything about God and Jesus knowing thoughts (#12431, #20455, #20489, #20498 and the evidence), the layer-3 pairs, the count, the false codes and quotations.

## New findings the actions turned up

1. **#17012 quoted 1Ch 28:9 wrongly:** "a willing [delighting] soul [nephesh]" where the ESV has "a willing mind" (the word is nephesh). The restatement quotes the ESV and says the word is nephesh. The ESV quote check inside `restate` found it; the structural pull could not.
2. **#20489 had a node on the wrong word:** on 1Chr.28.9 it held the first "know" (Solomon's knowing God) for a claim about God knowing thoughts. Dropped, the word kept where it belongs (#19501).
3. **#20455 and #17270 hold renderings in double quotes that are not ESV quotations** ("the things of a person", "heart / heartily / fainthearted"). #20455 was repaired (single quotes). #17270 keeps its number and text until the heart collection splits it, because restating the whole compound runs into this.
4. **Two nodes on #20489 ("know" of Ps.139.2 and Ps.139.23)** were not about thoughts and were carried by nobody: deleted as unrelated, with the reason recorded and 20489 keeping its other nodes.
5. **A per-collection node is not a duplicate:** the same occurrence under two collections is the design (checked on #20019 and #20489).

## Limits and what stays for you

- Copy only. Nothing here is in the live data. To apply it live needs: the migration of `nature` and its enum under a named snapshot, rule IB-07, the entry point, the test plan registered, and your reading of v9 as a whole.
- Only 1Chr.28.9 and its 55 observations. #21757's other 78 verses and the Hebrew sense claims were not read. The three created evidence observations passed the quote check against the verse table; their claim that they state what no node states is my reading.
- The marker of the two layer-3 observations #22594 and #22606 stands on traces to layer-2 observations outside this verse that are not yet marked.
