# #2484 — Add the collection to every observation node: design for decision

Status: design only. Nothing built, nothing changed in iba/app/db/iba.db. Raised under #2463 (researcher, 2026-11-12, session d281b154). It precedes #2485 (fill the missing verse_lexical_id).

## What I read first (B:123)

- `ib_node`: one row per verse, word, cluster, subgroup, question or other thing a finding applies to. 78,099 live rows.
- `ib_node.cluster_code` is "the word's own classification" and nodes written before #2273 "may hold the cluster of the pass that cited the word". `ib_node.reading_id` is NULL on nodes written before #2273.
- `collection`: 277 collections, all `confirmed`. `collection_link` places a base (a `surface_term` row) in a collection by tier. `collection.member_tiers` = core, synonym, opposite, gathered, phrase.
- `surface_term`: the hub for a surface text. A node's surface (lower-cased, trimmed) joins to it by text; its `base_id` is the base that `collection_link.term_id` points to.

## What the data shows (read-only, 2026-11-12)

Node counts, live nodes only:

| group | nodes |
|---|---|
| all live nodes | 78,099 |
| with a surface | 67,874 |
| with no surface (question, cluster and similar nodes) | 10,225 |
| surface matches no `surface_term` row | 458 |

For the 67,416 nodes whose surface matches a `surface_term`, by how many collections the base is a member of (member tiers only):

| collections | nodes |
|---|---|
| none | 20,993 |
| exactly one | 35,129 |
| two or more | 11,294 (up to 43 collections for one node) |

So "the node's collection" is not one value for most of the table: no collection for 20,993 + 458 + 10,225 = 31,676 nodes (41%) by this route, and several for 11,294.
Limit: the query keys on a node's own surface and takes `coalesce(base_id, id)` as the base; I have not tested other keys.

## Decisions needed before any build (B:105, B:44)

### D1. How a node is tied to its collection

- **A (recommended). By the node's word:** the node's surface, through `surface_term` and `collection_link`, to every collection the base is a member of. Rule is mechanical and repeatable, uses only recorded links.
- **B. By the finding's reading:** only nodes with a `reading_id` (1,397) get a collection, from the reading's scope. Exact but covers 2% of nodes.
- **C. By cluster:** map `cluster_code` to a collection. Against your own words (cluster allocations are "no longer of analytic consequence or value, and often is misleading"); listed only to record it was considered.

### D2. Where it is stored

- **A (recommended). A link table** `ib_node_collection` (node_id, collection_id, how it was found, run_id, deleted): many collections per node, none allowed. Fits the 11,294 multi-collection nodes and keeps the history convention of `collection_link`.
- **B. One nullable column** `ib_node.collection_id`. Simple, but forces one collection for 11,294 nodes, a new judgement made by a script (B:127).

### D3. Nodes with no collection

- **A (recommended):** leave them with no link rows and report the count in the migration result. A node with no collection is a fact, not an error.
- **B:** raise an item per group (no surface, surface unmatched, word in no collection).

### D4. cluster_code and cluster_subgroup_code

- **A (recommended):** keep the columns and values untouched; update their `cfg_column.use` text to say they are not analytic; new reports read the collection. No drop, no rewrite.
- **B:** blank or drop them in a later, separate item, after no report reads them.

### D5. Keeping it current

- **A (recommended):** one shared function maps a node to its collections; the migration fills existing nodes and the node-writing path (Reading.ps1 Record) calls the same function at write time.
- **B:** migration only, new nodes filled by a later re-run.

## Plan if you approve the recommended options

1. Table `ib_node_collection` by the procedure in iba/app/USER-GUIDE.md and iba/app/GOVERNANCE.md, with `cfg_table` and `cfg_column` meaning rows (B:123), written through `apply_logged` (rule 75).
2. The shared mapping function, tested on a copy made with `iba/app/lib/dbsnapshot.copy_db`, never the live database.
3. Migration: named rollback snapshot (`iba/app/lib/dbsnapshot.py --named`), fill every live node, check the counts against the tables above, record the result on #2484.
4. Reading.ps1 Record calls the function at node write.
5. BUILD.md entry naming every script by full path; USER-GUIDE.md and GOVERNANCE.md as the changes require (E:12).
6. Then #2485 (fill the missing verse_lexical_id). #2486 (cross-link claims to collections) stays separate.

## What you are asked to approve

Decisions D1 to D5, as recommended or as you change them, and the plan above. On approval I build and test on a copy first.

Counts come from a read-only query run once on 2026-11-12. The mapping D1-A is inferential (B:4) until the migration result is checked against them.
