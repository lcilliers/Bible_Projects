# #2463 A new index of collection, surface and subgroup: the clash with `surface_subgroup` and the design (v1, 2026-11-14)

Status: a design for the researcher to correct and approve; read-only; nothing built or changed. Prompted by the researcher (#2463, 2026-11-14, verbatim): "I am changing may decision. leave concepts alone. not yet sure, but they may be redundant.  create a new index table that links the collection and surface and have a surface-subgroup. This is likely a clash with surface-subgroup, but maybe the current surface subgroup can be re-used." The concept rows are left as they are (the plan of `2463-concept-rows-destroy-and-reform-plan-v1-20261114.md` is not carried out). Read first (B:123): `cfg_table.use`, `cfg_column.use` and the stored schema of `surface_subgroup`, `collection_link`, `surface_term`. Readings are inferential (B:4).

## 1. The answer on re-use: do not re-use `surface_subgroup`

`surface_subgroup` (13,452 live pairs, last written 2026-11-06) is the allocation of a (Strong's code, surface) pair to a cluster subgroup. It cannot carry a subgroup of a collection without being changed into something else:

| Fact | Why it blocks re-use |
|---|---|
| `cluster_code` is `NOT NULL` with a foreign key to `cluster`; the live unique index is (`cluster_code`, `strong`, `surface`) | a collection surface has no cluster of its own; the key would have to change |
| `cluster_subgroup_id` is `NOT NULL` with a foreign key to `cluster_subgroup` | the new subgroup is not a cluster subgroup |
| `allocated_by` and `status` carry the cluster allocation vocabulary (api, session, inherited; provisional) and every row is `provisional` | a second meaning in the same column |
| Eight live code paths read or write it: `versescope.py` and `versecollate.py` (Reading Open, still on subgroups until #2448), `surfacemap.py`, `surfacejudge.py`, `collectionexport.py`, `collectionevidence.py`, `collectionevidencereport.py`, `tools/collection_batch_run.py` | changing the table's meaning changes all of them at once |
| the key is the Strong's code, which you say is the wrong level | the new grouping is by surface in a collection |

My recommendation: a new pair of tables with names that do not clash, `surface_subgroup` and the cluster subgroups left as history. The old pairs stay readable as a hint beside a surface (as the report's subgroup, concept and not_this_sense hint), and may seed the first placement of a pilot collection (a proposal, not a copy).

## 2. The design

Two tables, one for the group and one for the index, so that a group has an identity (a name can change; an id does not) that a node and a layer 1 observation can point at.

**`collection_subgroup`: a group of surfaces inside one collection (your surface-subgroup).**

| Column | Holds |
|---|---|
| `id` | the identity a node and an observation point at |
| `collection_id` | the collection it is in (foreign key to `collection`) |
| `name` | what the group is (for example starting, weighing, meditation, minding and musing) |
| `status` | indicative (made by a run or by me, not reviewed), confirmed (the researcher confirmed it), retired |
| `note` | the researcher's or the reading's short note; the definition and the Strong's enrichment of the group are its layer 1 observations (found through their nodes), not columns here |
| `run_id`, `created_at`, `updated_at`, `created_by`, `deleted` | the table convention (a change is a soft delete and a new row; the change goes to `surface_event`) |

**`collection_subgroup_surface`: the index of a collection's surfaces (your index table).**

| Column | Holds |
|---|---|
| `id` | surrogate key |
| `collection_id` | the collection (foreign key) |
| `term_id` | the surface (foreign key to `surface_term`: the same text key as `verse_lexical.surface`) |
| `strong` | empty = the whole surface; a Strong's code = only that sense of the surface (used when one surface has two senses in different groups, for example `thoughts` as plan and as thinking) |
| `subgroup_id` | the group it is placed in (foreign key to `collection_subgroup`); empty while unplaced |
| `state` | unplaced (in the index, no group yet), placed, isolated (no inner-being role: layer 1 step 1; the surface is bound to its partner or excluded, and a surface wrongly in the collection is moved by the collection change procedure of B:129) |
| `reason`, `run_id`, `created_at`, `updated_at`, `created_by`, `deleted` | the table convention |

Constraints: a live row is unique on (`collection_id`, `term_id`, `strong`); the surface must be a member of that collection by the rule of section 3 of the collections paper (own link, else the base's); the group must belong to the same collection; if one row of a surface has a Strong's code, every row of that surface has one (a completeness check, as the node checker does for nodes).

**The first fill is mechanical, not a judgement:** one row for each member surface of each confirmed collection, `state` unplaced, no group. Sizes from the tables on 2026-11-14: 3,437 member surfaces in the 169 confirmed collections (none is in more than one, though 274 live links still carry the `shared` flag); 3,419 index rows at the surface level; 17,899 at the surface-and-code level. For thought: 33 surfaces and 197 surface-and-code pairs. 2,232 of the 3,419 surfaces carry two or more Strong's codes in their collection, so the sense split is common and not an edge case.

## 3. How it reaches the nodes (discoverable)

A node carries `collection_id` and the surface and Strong's code of its `verse_lexical` row; the index gives the group by the join (`collection_id`, `surface`, `strong`, falling back to the whole-surface row). No column on `ib_node` is needed to start; B:130 lists the node's columns and a new column amends it. If the join proves slow or the researcher wants the group on the node, adding `subgroup_id` to the node is a later, separate change with the node checker.

## 4. What it would change in the app (if you approve)

1. **A named snapshot and a build on a copy** (B:97): the two tables, their `cfg_table` and `cfg_column` rows and write grants, in one migration through `apply_logged`; the first fill of 3,419 rows.
2. **A tool** (`Collection-Build.ps1` action, or its own script; B:41): `Index` fills and refreshes the index, `Subgroup` makes a group and places surfaces in it, each on your instruction with a reason, and each change a `surface_event`.
3. **A checker:** every member surface has an index row; no placed surface sits in a group of another collection; the sense rule above; a surface that left the collection leaves the index.
4. **The report:** the evidence report shows the group on each member occurrence, in the verse view and the pairings, and counts the pairings by group (the group level you asked for), with the old subgroup and concept shown as a hint.
5. **Tests (B:46), USER-GUIDE and BUILD**, in the same unit.

## 5. Decisions for the researcher

| # | Decision | Options | My recommendation |
|---|---|---|---|
| 1 | Re-use `surface_subgroup` or a new pair of tables | re-use (alter the cluster columns, change its meaning, change eight code paths); or a new pair | a new pair; leave `surface_subgroup` as history |
| 2 | Names | `collection_subgroup` and `collection_subgroup_surface`; or other names (the name `surface_subgroup` is taken) | those two |
| 3 | The grain of the index | the surface only (3,419 rows); or the surface with an optional Strong's code for the split senses (up to 17,899 rows) | the surface, with a Strong's code only on the rows of a surface that is split between groups |
| 4 | One table or two | one index table with the group as a text column; or two tables (a group has an id for nodes and observations) | two |
| 5 | The group on the node | by the join now; or a column on `ib_node` later | by the join now |
| 6 | The first fill | empty groups (all unplaced); or seeded from the old subgroup pairs as indicative placements | empty, with the old subgroup shown as a hint; the placement is the layer 1 reading |
| 7 | The `shared` flags | leave; or check them (274 live links carry them, none of the surfaces is in two collections) | check them in the same unit |

## 6. Not done

Nothing built, written or changed; the concept rows are untouched. The build needs an escalation of its own and your approval of this design (B:105, B:44).
