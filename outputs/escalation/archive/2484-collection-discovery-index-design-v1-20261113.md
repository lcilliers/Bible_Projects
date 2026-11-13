# Finding every observation and node of a collection: design for decision

Status: design only. Nothing built, nothing changed in iba/app/db/iba.db. Raised by the researcher, 2026-11-13 (session 6ae98364), on #2484: supportive nodes (entity and other surfaces) belong with the collection of the surface they support; the way observations and nodes are discovered must be looked at again, orphans found, and a method devised that does the complex search once and not at every read. Read-only measures below are from 2026-11-13.

## What I read first (B:123)

`ib_node.collection_id` (cfg_column.use): the one collection of the node's own surface; NULL otherwise. `ib_observation`: the finding; reached by its nodes. `verse_lexical`: the occurrence a node reads (`ib_node.verse_lexical_id`). Code read: iba/app/lib/collectionevidence.py, iba/app/lib/engagement.py, iba/app/lib/reading.py.

## How a reader finds a collection's observations today: four different routes

| reader | route | what it misses |
|---|---|---|
| evidence report (iba/app/lib/collectionevidence.py, header lines 8 to 20) | member surface text to `verse_lexical` occurrences to `ib_node.verse_lexical_id` to the observation | every node with no verse_lexical_id (4,268 live nodes); every supportive node, since entity and other surfaces are not occurrences of a member surface |
| engagement (iba/app/lib/engagement.py lines 170 to 176) | the verses of the member occurrences, then every observation with a node in those verses | picks up observations about other words in the same verse (too wide); misses observations whose node sits in another verse |
| reading (iba/app/lib/reading.py lines 407 to 416, 1056) | by verse reference of the scope | same as engagement |
| node column `collection_id` | the node's own surface only | the supportive nodes (16,171 live nodes carry none) |

Each reader rebuilds the link from raw tables, so they can disagree.

## What the routes reach today (live observations 14,947, 14,884 with a live node)

| | nodes | observations |
|---|---|---|
| reached by column, surface text and verse_lexical_id | 42,949 | 12,440 |
| reached by column and surface text but not by verse_lexical_id (evidence report would miss them) | 2,353 | 197 |
| reached by no route | 16,171 | 2,247 |

The 16,171 are the unmapped nodes of the earlier evaluation. Of the 2,247 observations that no route reaches, by stage: verse-reading 1,291; prior-capture 570; engagement 130; char-answers 117; Analysis_phase_1 70; strand-reading 33; char-reading 18; reading 13; char-subgroup 4; engagement-note 1. Where the column and the verse_lexical route both apply they never disagree (0 of 42,949).
Limit: surface-text matching uses surface_term and its base, as the exports do; I have not read the observations one by one, so "orphan" means "no stored link reaches a collection", not "malformed" (B:4).

## The method: build the link once, store it, make every reader use it

**A. A stored index, `observation_collection`** (observation_id, collection_id, how: `own-surface` or `supports`, via_node_id, run_id, deleted), one row for each observation and collection it belongs to. A discovery function in one place (iba/app/lib/, with its Collection-Build.ps1 or Reading.ps1 entry point) builds it; the writing path calls the same function when a node is written, changed or withdrawn, and a rebuild reproduces it from the tables. Readers join the index; none rebuilds the chain. An observation with several collections has several rows, which is the repeat that you said must make sense, without repeating nodes.

**B. The support link on the node, `ib_node.supports_node_id`** (the collection-surface node of the same observation that this entity or other node plays a role on). The supportive node's collection is then the collection of that node, read, not copied. Where an observation has several collection surfaces, the link names which one this node supports; I would set it by reading the observation, with your confirmation, not by script (B:127). Without this link a supportive node can only be matched by the observation, which is the 3,725 + 1,915 nodes with several collections.

**C. A standing check, as a stored-data fault in the evidence report and a check in the app:** every live observation has at least one index row or is listed as an orphan; every live node has a collection or a support link or is listed; a live node with no verse_lexical_id is listed. Orphans are shown in a list on every read, never silently absent.

**D. The readers moved to the index** in one change: evidence report, engagement (Pull and Check), reading scope. Counts before and after on three collections are compared and the differences explained.

## Decisions for you

- **D1. Storage of the index.** A (recommended): table `observation_collection`, maintained by the function. B: a database view over the node column and the support link (nothing stored, but computed at every read, the thing you want to avoid). C: no index, only the node column (supportive nodes stay out).
- **D2. How a supportive node names its collection.** A (recommended): `supports_node_id`, set by reading, observation by observation, starting with the 4,764 nodes that have exactly one collection among the same-verse nodes of their observation. B: derive by the same observation and verse, by script (cannot decide the 3,725 with several).
- **D3. The 2,247 orphan observations** (no node reaches a collection). A (recommended): list them per stage for you; the 1,291 verse-reading and 570 prior-capture are older work, which I would examine first for restatement or withdrawal (plan v3 R2, R5). B: leave them out of collection reads and show only the count.
- **D4. Readers.** A (recommended): all three on the index in one change, with before and after counts. B: evidence report first, others after.
- **D5. The 4,268 live nodes with no verse_lexical_id** (#2485, which held this, waits for your approval to close): A: the standing check lists them and the support link or the index covers them, so the missing id stops hiding them; B: fill the ids first (match rule for 2 or more candidates still undecided).

## What you are asked to approve

D1 to D5, as recommended or changed. On approval I build on a copy (iba/app/lib/dbsnapshot.copy_db), run a test plan for each mode, compare with predicted counts, and report before the live write, after a named snapshot. Nothing is built before then.
