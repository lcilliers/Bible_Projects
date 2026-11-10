# #2412 — can engagement be derived from the existing observations? (test v1)

Basis: read-only queries on `iba/app/db/iba.db`, 2026-11-10 (scripts in the session scratchpad: `obs_coverage.py`, `obs_vs_engagement.py`); table meanings read from `cfg_table.use` of ib_observation and `cfg_column.use` of ib_observation.stage and ib_node.role (B:123). Counts are checked; what they mean is mine and inferential (B:4).

## The question (researcher, verbatim)

> "I have not seen a single instance where your reading of the observations for a verse, and the newly crafted observation in relation to the collection where in conflict. there are a large number of verses that already have observations. is it therefore necessary to re-read the verse text. what if we derive the same result from reading the observation of the surface and use the observations to get the engagement status and observation for each collection."

## What the record says about the first sentence

Across the engagement runs so far, no observation of another stage was modified or deleted (0 prior-capture observations changed; the 58 deletions and 1 status change touched engagement's own observations; 1,626 changes are `reviewed` marks). That agrees with the researcher's experience: the existing observations were accepted as they stood.

## Coverage of the work still to do (64,568 items in 24,896 verses)

| items | count |
|---|---|
| with a live node of their own (the surface in this verse is on an observation) | 9,472 (14.7%) |
| of those, only characteristic or qualifier roles | 4,380 |
| of those, a standalone or no-role node among them (no engagement meaning) | 5,092 |
| with no node of their own, in a verse that has other observations | 22,156 (9,494 verses) |
| with no node of their own, in a verse with no observation at all | 32,940 (13,984 verses) |

Reading only the items without a node of their own still means 23,478 verses, against 24,896: 6% fewer. The stage `prior-capture` (37,938 of the live nodes) is "observations captured from prior study documents" (`cfg_column.use` of ib_observation.stage), not a reading of every verse, so an item with no observation is not an item that was read and found empty: the record cannot tell the two apart.

## The six engaged collections as a test (4,636 items, my reading as the reference)

| the item before engagement | items | engagement found no bearing | found bearing |
|---|---|---|---|
| has a node of its own | 1,253 | 206 (16.4%) | 1,047 |
| no node of its own, verse has other observations | 1,086 | 313 (28.8%) | 773 |
| verse has no observation | 2,297 | 1,151 (50.1%) | 1,146 |

Where the item had a node of its own with the role characteristic (849 items), engagement gave characteristic for 262, bears_on (object, relational target, enactment) for 446, qualifier for 18 and no bearing for 123. The stored role and the engagement role are different questions: the observation's role says what the word is in that finding, engagement says what the surface does for the inner being in the verse, and bears_on has no counterpart among the stored roles (characteristic, qualifier, standalone).

## Reading of the test

- A verse with other observations, or none, does not tell that the surface has no bearing: engagement found bearing for 71% of the items in verses that had other observations, and for 50% where the verse had none.
- The stored roles cannot give the engagement role directly: they agree in kind for a minority (262 of 849 characteristic nodes).
- The sample is the seven collections the researcher chose (aloud, call, deal, new, anger, godly, choose), and the reading is mine, so it shows what happened there and does not prove the same for the rest.
- What the existing observations do give is context for the reading and a check, which the pull already passes in (accept, modify, delete, merge, leave); none was changed.

## What can be done with it (for the researcher)

- Deriving the status of the 4,380 items with a clean characteristic or qualifier node would be a rule that replaces the reading of those items; on this test it would differ from engagement in most cases, so I do not propose it.
- The saving that holds is the one in plan v2: read each verse once with its observations once and write compactly.
- A rule that takes "the verse has other observations" as "no bearing" for the 22,156 items would be wrong for about 71% of the engaged sample; it is the researcher's decision to make or not, and the figures above are the evidence.
