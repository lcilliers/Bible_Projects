# #2308 Node reference sweep: results and what is left (v1)

**Date:** 2026-10-26 · **Escalation:** #2308 · **Tool:** `iba/app/ps/Node-Resolve.ps1` (work package `node-resolve`, steps `node_resolve.plan` and `node_resolve.apply`, method rules NR-01 to NR-06, `iba/app/lib/noderesolve.py`).

## 1. What was done

The sweep looked up, through the strong and the verse, the occurrence (`verse_lexical_id`), the morph code and the sub_group
code of every node, in every stage and cluster (not only the migrated nodes). It fills null columns only (NR-05).
It was tested on a copy of the database first, then run live: **20,572 nodes written, 0 skipped**; a second plan finds
**0** nodes to fill. The plan with each node's values before and after is `outputs/node-resolve/resolve-plan-20261026.json`
(a file copy of the database before the run is kept in the session scratchpad).

| Stage | Nodes | Without sub_group, before | Without sub_group, after |
|---|--:|--:|--:|
| verse-reading | 11,043 | 11,043 | 3,179 |
| strand-reading | 3,992 | 3,992 | 214 |
| prior-capture | 52,068 | 3,752 | 31 |
| char stages | 1,866 | 19 | 0 |

## 2. What is left, and why

**A. 3,424 nodes with a strong still have no sub_group: the strong has no row in the cluster's sub_group map
(`surface_subgroup`).** This is a configuration gap, not a lookup failure: the lookup has nothing to find.
- M67: 2,970 nodes on 278 strongs (the cluster has 6 subgroups defined; most of its strongs are not mapped to them)
- M64: 189 nodes on 19 strongs; M83: 70 on 34; M49: 70 on 32; M25: 28 on 3; M47: 13 on 2; the other clusters 1 to 10 each
- 32 further nodes sit on a strong whose occurrences in the verse belong to different sub_groups (NR-04): left and listed in the plan.
The strongs with the most nodes are M67 H4430 (224), G4102G (131), G3056 (100), G3870 (83), G0026 (81).

**B. 4,505 nodes with a strong have no occurrence id:** the strong occurs more than once in the verse and the node's surface
does not pick one (prior-capture 3,899; verse-reading 408; strand-reading 128; char 70). Their sub_group is filled where all
the occurrences agree.

**C. 10,179 nodes name a verse and no word** (prior capture: the line named no M-coded word). These are findable by verse
but not by word or sub_group.

**D. 21,138 nodes carry no role** (all of the older stages, and 4,237 prior-capture nodes). 51,375 of the prior-capture nodes
carry no disposition (the document gave none).

## 3. Decisions for the researcher (each would be built only after the decision, B:105)

1. **The 399 (cluster, strong) pairs in A:** who assigns them to their cluster's sub_groups, and by what route (a config
   proposal per cluster, or a reading). M67 is the large one.
2. **C: verse-only nodes.** Option: where the verse holds exactly one word coded in the node's own cluster, the node takes
   that word (strong, occurrence, sub_group). It turns a verse reference into a word reference, but the finding may not be
   about that word; leave as they are, or fill only on the researcher's ruling per document.
3. **B: several occurrences.** Option: one node per occurrence, so each occurrence has its sub_group; or leave.
