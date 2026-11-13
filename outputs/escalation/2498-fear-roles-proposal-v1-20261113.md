# Roles for the 29 live fear findings (proposal, #2498 decision Q5)

The 29 findings FE-47 to FE-85 that October recorded as live observations (stage `strand-reading`) carry **133 nodes, none with a role** (the 749 I quoted earlier is all the fear findings of the whole strand). Each role below was judged from the verse. Nothing is written yet. Load file: `outputs/escalation/2498-fear-roles-load-v1-20261113.json` (every node, its role and, for an exception, its reason).

## What is proposed

| Role | Nodes |
|---|---|
| characteristic | 127 |
| qualifier | 2 |
| object | 1 |
| standalone | 2 |
| no role (left alone, see below) | 1 |

**Why characteristic is the default.** Every node of these findings is the dread or trembling word the finding is about (the words of unit 2 and the fear words beside them), so in its verse it is what the finding observes. The five nodes that are not are the exceptions below, each read in its verse.

## The five exceptions

| Node | Verse | Word | Role | Why |
|---|---|---|---|---|
| 13367 | Job 3:25 "For the thing that I fear comes upon me, and what I dread befalls me." | *thing* | object | the thing feared: what the dread is directed at; *fear* and *dread* carry the characteristic |
| 13450 | Mic 7:17 "...they shall turn in dread to the Lord our God..." | *turn* | qualifier | the turning gives the direction of the trembling, toward God (face: coming to God in trembling) |
| 13452 | 2Kgs 4:13 "...you have taken all this trouble for us..." | *taken* | qualifier | the taking is the act that gives the trouble; *trouble* is the characteristic |
| 13457 | Lam 4:6 "...no hands were wrung for her." | *wrung* | standalone | a bodily wringing; the ledger says the English shows no fear. Recognised, no inner-being role |
| 13455 | Eccl 12:3 "...the keepers of the house tremble..." | *tremble* | standalone | **judgement call.** The body's trembling in age, placed with the flesh by the ledger. Characteristic is the alternative; say if you prefer it |

## One node left alone

Node 80340 (Mic 7:17, *come trembling*, observation 11786) is on the same occurrence as node 13449 (same observation, same word) with a different collection (`turn` against `fear`). It looks like a duplicate left by the salvage, so it belongs to the node cleanup; I gave it no role. 13449 takes characteristic.

## Rehearsal (on a copy; nothing live changed)

- 132 roles set; 29 observations touched; no text, kind, basis or node changed; a second run changes nothing; 132 `role` rows in `ib_observation_change`, each with its reason.
- Node checker on the 29 observations: nodes with no role 133 to 1; observations with no relevant-role node 29 to 0. Whole table: nodes with no role 14,133 to 14,001; observations with no relevant-role node 7,361 to 7,332.
- The loader was changed to let an existing node take its role even when no collection can carry it (two of these nodes have no collection); adding a node still needs one. The pilot load, re-checked after the change, still shows nothing to change.

## If you approve

A named snapshot, then `iba\app\ps\Draft-Apply.ps1 -Step Apply -File outputs\escalation\2498-fear-roles-load-v1-20261113.json`, the node checker, and a BUILD entry. To change the Eccl 12:3 call first, say so and I change the load file.
