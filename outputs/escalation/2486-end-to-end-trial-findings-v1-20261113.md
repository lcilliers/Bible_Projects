# #2486 End-to-end trial: what was built and what it found (v1, 2026-11-13)

Status: findings for the researcher. Built on a copy only; the live `iba/app/db/iba.db` has no trial table (checked). Plan: `outputs/escalation/2486-end-to-end-trial-plan-v1-20261113.md`. Basis: `outputs/escalation/2486-claim-objectives-and-definition-draft-v2-20261113.md`.

Researcher, verbatim (2026-11-13): "I think this work will lead us to surface my main concerns with the current work to day, which is great. so go ahead and a) build the forward and backward tracking, and b) determine the skeleton destinations (at the level of movement, chapter, sub chapter, section)".

Everything labelled as a level, a destination or a border reading below is my reading of the data (B:4), for the researcher to correct.

## 1. What was built (on the copy `iba/app/db/snapshots/trial-2486/iba-trial-2486.db`; rollback point: named snapshot `iba/app/db/snapshots/kept/iba-20261113T173200Z-pre-2486-claim-trial.db`)

| Object | Holds |
|---|---|
| `trial_skeleton` | the index: key, parent, level (movement, chapter, subchapter, section), title. 17 entries: the four movements of #2345 and, under II, three chapters, four sub chapters and six sections |
| `trial_claim_destination` | per claim: its skeleton key, its level (surface, interaction, across, meta) and where else it also fits |
| `trial_claim_node` | the backward link at node level: claim, observation, node, basis, and whether the node's verse is among the claim's own verse sources. 49 rows |
| `v_trial_claim_back` | claim to observation to node to surface, role and collection |
| `v_trial_claim_forward` | claim to its destination key to the blocks that tell it today and their chapters |

The collections of a claim are read from its nodes by query (C-359 reaches five). Nothing is stored on `narrative_claim`.

## 2. The six claims

| Claim | Said in brief | Level | Destination (movement / chapter / sub chapter / section) | Also fits | Told today in |
|---|---|---|---|---|---|
| C-367 | The heart is where thoughts and plans come from | interaction | II / Knowing and thinking / Thought and where it arises / Thoughts and plans come from the heart | III, the heart as seat | 10.4 "Where thoughts come from"; 4 "The heart thinks, attends and remembers" |
| C-338 | The choice is the chooser's own | surface | II / Will and action / Choosing / The choice is the chooser's own | | 10.7, three sections |
| C-362 | What the heart devises on its own: a rival worship, a false report, a god | across | II / Will and action / Planning and purpose / What the heart devises on its own | IV, idols taken inside | 10.7 "Planning"; 12 "Idols taken inside"; 10.4 "When thinking changes character" |
| C-364 | A purpose set ahead and held, kept and directed by God | interaction | II / Will and action / Planning and purpose / A purpose set ahead and held | | 10.7 "Planning" |
| C-359 | Looking ahead weighs ability and cost, plans under uncertainty | across | II / Will and action / Planning and purpose / Looking ahead | | 10.7 "Planning" |
| C-370 | A path from a thought arising to the deed | meta | II / How the behaviours connect / From a thought to a deed / The path in order | | 10.0 "From a thought to a deed" and 10.5 "The tongue, the lips and the eyes devise", both in full |

## 3. Backward tracking: what the checks show

| Claim | Named observations | Nodes | Role empty | No collection | Nodes on verses the claim does not list | Claim verses with no node | Other live observations on its verses |
|---|---|---|---|---|---|---|---|
| C-367 | 1 | 9 | 9 | 0 | 7 nodes on 6 verses | none | 29 |
| C-338 | 1 | 8 | 8 | 0 | 3 | none | 36 |
| C-362 | 2 | 5 | 5 | 2 | 2 | none | 13 |
| C-364 | 2 | 7 | 7 | 1 | 0 | none | 31 |
| C-359 | 1 | 8 | 8 | 2 | 0 | Luk 23:51, Dan 6:3 | 12 |
| C-370 | 1 | 12 | 12 | 0 | 6 nodes on 5 verses | none | 18 |

## 4. Findings

1. **The border is crossed at the source.** All six claims rest on observations of stage `strand-reading`, tag `key-statement`; so do 83 of the 87 observations named as a claim source in the whole register (the strand steps are retired, #2228). Their wording is already a statement about how the inner being works: "The heart is where thoughts come from" (12407); "The path: arising → lodging → reckoning → devising → expression → action" (12424); "The inclination can be kept, directed and stayed" (12434). The observation and the claim are the same statement; no observation under them says only what the verse says. This is your concern about observations having moved too far, found in the evidence of the claims themselves.
2. **The observations that do say what the verse says are not linked to the claims.** Each claim's verses carry 12 to 36 other live observations (mostly stage `prior-capture`, some `engagement` and `strand-reading`). A sample on Psa 140:2 and Pro 16:9 shows a mix: some state what the verse says ("The heart of man plans his way", 17053; 19999), and some are pointers to old documents and not about the verse ("Ch 12: the hidden trap and the deep heart", 18895; "EA §28: Context seats", 14484). Nothing records which, if any, a claim uses. I have not marked used or not used; that is the researcher's reading, claim by claim.
3. **The claim's verses and the observation's nodes do not agree, in both directions.** C-367 lists 2 verses; its observation applies 9 nodes, 7 of them on 6 verses the claim does not list (Mat 15:19, Mar 7:21 and others). C-370: 6 nodes on 5 unlisted verses. C-338: 3. C-359 lists Luk 23:51 and Dan 6:3, which no node of its observation touches. So the link is neither definitive back to the base data nor to the verses the claim cites.
4. **Roles are empty.** All 49 nodes have no role; across the whole database 14,065 of 68,406 live nodes have none, and B:130 requires a role on a node. Without a role the node cannot say how a word is used in the finding.
5. **Five of the 49 nodes carry no collection**: inventing, creation (C-362), aim in life (C-364), deliberate and planned (C-359). B:130 calls an in-scope node without a collection an error; whether these surfaces are in scope is not settled by the data.
6. **The forward link works but is not a destination.** Every claim is told in one to three blocks; none of the six has `main_chapter_id` or `main_section_id` set (331 of 393 claims have none). C-362 is told in three chapters (10.7, 12, 10.4), and C-367 in 10.4 and in chapter 4, so telling and destination are different things: a claim has one destination and may be told in several places by pointing at it.
7. **Planning straddles the current chapters.** The collections intend and plot are told in 10.4 Thinking and in 10.7 Choosing. In the skeleton I placed planning and purpose under Will and action (where C-359 and C-364 are told today) and the source of thought under Knowing and thinking; the researcher may place it differently. The destination levels worked for these six, but sub chapters do not exist in the current narrative (chapter, section, sub-section); the four sub chapters are my grouping.
8. **Levels worked, with one soft edge.** One surface, two interaction, two across and one meta. The line between interaction and across (C-364, C-362) is a judgement I made from the claim text and the collections reached; the data does not carry it.

## 5. What this says about the design

- The claim needs its own evidence: observations of the "what the verse says" kind, and the nodes it applies. For these six, the existing key-statements would be the claim's wording and would move to the claim (their territory), leaving the verse-level observations to carry the evidence.
- A node-level link is needed (finding 3): claim, observation, node, with the node's verse checked against the claim's cited verses.
- The destination is a skeleton key (a separate table of four levels), with the telling relation kept for "told in part in several places".
- The level is a property of the claim; it is not derivable from the data.
- Node roles and collections need completing before node evidence can be definitive (findings 4 and 5).

## 6. Decisions for the researcher

1. What happens to the strand-reading key-statements (83 of the 87 observations named as claim sources): taken as the claims' own wording and the claims re-based on verse-level observations, or the observations cut back to what the verse says.
2. Where planning and purpose sit in the skeleton (Will and action or Knowing and thinking), and whether the four-level skeleton and my sub chapter grouping are right.
3. Whether to mark, for these six, which of the 12 to 36 observations on each claim's verses it uses (the reading with the researcher that the plan names), as the next step.
4. How the 14,065 empty node roles and the unplaced surfaces are to be handled (a separate item).

## 7. Not done

No claim, observation, node or narrative row was changed. Nothing is marked used or not used. The other 387 claims are not touched. No rule, `cfg_*` row, document or live schema was changed. The copy and the named snapshot stay until the researcher closes the trial.
