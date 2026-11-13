# Nodes and collections: what is mapped and what cannot be mapped (read-only, 2026-11-13)

Status: evaluation only. Nothing changed in iba/app/db/iba.db. For #2484 (the node review continues under it; #2487 is closed). Counts come from one read-only pass on 2026-11-13.

## What I read first (B:123)

- `ib_node.collection_id` (cfg_column.use): the one collection of the node's surface (its own row or its base is a member, tiers core, synonym, opposite, gathered, phrase); NULL on a node with no surface, whose surface is in no collection, or that is in several.
- `collection`: 169 confirmed (86 merged, 23 retired). `surface_term.surface_group`: entity, other, behaviour, inner_being_state.

## The mapping, checked against the rebuilt collections

| | nodes |
|---|---|
| live nodes | 61,473 |
| carry a collection | 45,302 |
| carry none | 16,171 |
| node on a merged or retired collection | 0 |
| node whose surface is in exactly one collection but carries a different one | 0 |

So the mapping is current after the rebuild (#2491): the column agrees with the surface for every node that has exactly one collection.

## What cannot be mapped (16,171 nodes, each in exactly one class)

| class | nodes | what it is |
|---|---|---|
| surface in group entity, in no collection | 7,891 | names, persons, things (examples: power, servant, brothers, firstfruits) |
| surface in group other, in no collection | 7,890 | generic words regrouped to other (examples: ineffective, careless) |
| surface has no surface_term row | 316 | text not in the surface hub (examples: bringing, leads, Titus, same) |
| no surface | 74 | question or cluster nodes with no word |

Study groups (behaviour, inner_being_state) leave no unmapped node: every such surface that has a node is in a collection.

## Can the unmapped nodes take a collection from their observation?

The #2487 plan v3 reading (D3): a node on an entity or other surface carries the collections of its own observation's collection-surface nodes. Measured now on all 16,171:

| | nodes |
|---|---|
| observation has nodes carrying exactly one collection | 2,722 |
| observation has nodes carrying two or more collections | 8,757 |
| observation has no node with a collection | 4,692 |

The 8,757 would need the node repeated per collection or a ruling, since the column holds one collection. The 4,692 have nothing to derive from.

## Things I did not settle

- 1,307 nodes carry a collection although their surface text resolves to more than one collection when a derived form's base is counted with its own row. I take this as the own-row rule (a derived form with its own link keeps it), not a fault, but I have not tested it (B:4).
- The 2,722 / 8,757 / 4,692 split counts a sibling collection by node, not by verse; I have not checked that the sibling is in the same verse.

## Decisions for you

- **D1 (recommended): the 2,722 with one sibling collection** take that collection through the observation, by script on a copy first, each change logged in `ib_observation_change` with the reason.
- **D2: the 8,757 with several sibling collections.** A: leave NULL and list them for you. B: repeat the node per collection (creates new nodes). Recommended A: the earlier ruling stopped at the same point.
- **D3: the 4,692 with no sibling.** List them per observation for you to place with a collection observation of the verse or restate; nothing guessed.
- **D4: the 316 with no surface_term row and the 74 with no surface.** List them; the 316 need their surface added to the hub or the node corrected, the 74 are by design without a word.

On your answer I build D1 on a copy, then report before touching the live database.
