# #2484 — How nodes are used in analysis, and the consistency checks that follow

Design for decision. Read-only counts from iba/app/db/iba.db, 2026-11-12. Nothing built or changed. It sits beside outputs/escalation/2484-add-collection-to-nodes-design-v1-20261112.md (decisions D1 to D5), which these rules refine.

## Your four rules, verbatim (2026-11-12)

1. "every node related to a verse or part of a verse should have a surface."
2. "every surface that is part of collection should carry the collection on the node."
3. "any node that are verse related but does not have a collection must be on the list of surfaces that is either a being or other type."
4. "any node without a surface need my attention to figure out if it has any value."

## What a node is for in analysis

A node is where a finding touches one verse, or one word of a verse. Analysis reaches a node through its surface (the word), and the collection is the unit of study (B:127). So a node can only take part in a collection's analysis if it has a surface, and the surface is in that collection. A node with no surface, or a surface the collections do not know, drops out of every collection reading without any warning. The checks exist to make that visible.

I read "being" as the `surface_term.surface_group` value `entity` (collection b in the data). The other values are `behaviour` and `inner_being_state` (the study, collection a) and `other` (collection c).

## The checks, with today's counts (live nodes, 78,099)

Verse-related means `verse_reference` or `verse_lexical_id` is filled: 78,053 nodes. The other 46 have no verse, no word, no Strong's code and no question code; they are not verse-related and none of these checks reach them.

| check | rule | what it tests | today |
|---|---|---|---|
| C1 | 1 | a verse-related node has a non-empty surface | 10,179 fail |
| C2 | 2 | a node whose surface is in a collection carries every such collection (and none the surface is not in) | 46,423 nodes should carry one or more (35,129 one, 11,294 several); 0 carry any, because there is no column yet |
| C3 | 3 | a node with a surface in no collection has a surface whose group is `entity` or `other` | 13,948 pass (8,623 entity, 5,325 other); 7,045 fail (7,044 `behaviour` or `inner_being_state`, 1 not judged) |
| C4 | precondition | the node surface has a `surface_term` row | 458 fail |
| C5 | consistency | node surface and Strong's code equal those of its verse_lexical row | 0 fail of 63,371 (outputs/escalation/2484-node-surface-vs-verse-lexical-surface-findings-v1-20261112.md) |

Counts C2 to C4 are over the 67,874 verse-related nodes that have a surface and key on the lower-cased, trimmed surface through `surface_term` and `collection_link` (tiers of `collection.member_tiers`). 35,129 + 11,294 + 13,948 + 7,045 + 458 = 67,874.

### What the failures are

- **C1 (rule 4), 10,179 nodes, for you.** 10,177 are draft nodes made by the prior-capture stage on 2026-10-26, cluster code M, no Strong's code, no occurrence, no word: they are verse-level statements (8,690 statement, 738 face, 585 link, 104 term, 42 silence, 18 other), 3,443 observations in all. 2,169 of those observations also have another node that has a surface, so the verse-level node may be redundant with it. The other two are node 36374 (H6586, 2Kgs.8.22) and node 49716 (kind `shared`, empty surface). Per your rule these go to you, and I will not decide their value.
- **C3 (rule 3), 7,045 nodes.** The word is a study word (for example 'haste' and 'zeal', G4710) with no collection yet: either the collection for it is not built, or the word is wrongly grouped. Both are for you; I do not move a word between groups.
- **C4, 458 nodes.** The surface (for example 'priests', 'presenting', 'faces') has no `surface_term` row, so no group and no collection can be read for it. Neither C2 nor C3 can be tested for these until the surface cycle covers them.
- **C2.** Closed by the #2484 migration: every node gets the collections its surface is in. Where the node's surface is a `shared` unit rendering (4,282 linked nodes) the match is less certain.

## What I propose (to settle before any build, B:105)

- **P1.** Run C1 to C5 as one repeatable check registered in config (B:rules_must_be_config_driven), reading the same mapping function as the migration, so the check and the fill cannot disagree. Its output is one list per check, each node with its verse and surface. Where it runs: after the migration, after each Reading record that writes nodes, and on demand.
- **P2.** The C1 list is grouped by observation (3,443) for you to assess, not by node (10,177). Each is marked kept or dropped by you; I do not delete or change any.
- **P3.** C3 and C4 failures are open items per group (study word in no collection; surface with no `surface_term`), not silent.
- **P4.** C2 uses the link table already proposed in D2-A, so a node with several collections carries all of them.

## What I need from you

Whether "being" means `entity`; whether the checks and P1 to P4 are what you want; then D1 to D5 of the earlier design, which they now depend on. On approval I build the table and mapping on a copy of the database first.

Limits: counts come from one read-only pass; the surface-to-collection mapping is inferential (B:4) until the migration result is checked against them.
