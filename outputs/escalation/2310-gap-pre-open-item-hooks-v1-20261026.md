# 2310: 0.GAP pre without document reading, and the open items' hooks (v1, 2026-10-26)

Researcher, chat 2026-10-26: 0.GAP pre no longer needs to read documents; what remains is the pull of the observations and the open items. Asked: do the open items have logical hooks into the verses and subgroups that let them be pulled into the gap work. All figures below are read-only queries on the live iba.db at 2026-10-26.

## 1. What 0.GAP pre is today (checked)

- Step `reading.gather` (`cfg_step`): writes the pre-gap items and their records. Rules RO4 and RO5 (`cfg_method_rule` 134, 135): base data read only in 0.C and 0.GAP pre; gather once.
- Pre-phase gap types in `cfg_setting reading.gap_types`: term_cluster, meaning_missing, base_missing, term_reading_missing, **read_in_files_only**, face_not_gathered, **open_item**.
- Document reading is the type **read_in_files_only** (a verse an earlier study file reads with no finding in the tables). The documents are now captured into `ib_observation` (#2305), so this type has nothing left to find.
- Behaviour rule 93 (`strand-checks-its-m47-verses`) names a 0.GAP pre check by word; it is not a document read and is left alone.

## 2. Open items: their hooks (checked)

305 thread items are open. Kinds: scope 296, cluster 6, escalation 3.

| hook | items | meaning |
|---|---|---|
| verse rows (`escalation_thread_item_verse`) | 296 of 305 (3,594 verse links, all resolve to `verse`) | every scope item is pulled by its own verses |
| target cluster and source terms | 204 of 305 | the cluster (M-code) and the Strong's on each side |
| target (cluster, Strong's) has a `surface_subgroup` row | 202 of 204 | the route from an item to a subgroup exists |
| source Strong's in `cluster_strong` | 204 of 204 | |
| names a subgroup in its own fields | 0 | no item carries a subgroup code |

The 9 open items with no verse rows: items 27, 420 and 632 (kind escalation: #1891, #2147, #2161) and items 500 to 505 (kind cluster: M72, M08, M09, M07, M18, M53). They match by cluster or escalation, not by verse.

`escalation.match_open_items` (`iba/app/lib/escalation.py:801`) already pulls by verse (scope items on their target verses, never a whole cluster), by cluster code, by Strong's and by strand; `iba/app/lib/reading.py` line 748 calls it with the scope's verses for the open_item gap type.

## 3. Finding

- **Verses: a logical hook exists** and is already the pull used for the open_item gap.
- **Subgroups: a hook exists, but only through (target cluster, target Strong's) to `surface_subgroup`**, then to `cluster_subgroup`. It holds for 202 of 204 worded items. Two items do not reach a subgroup and are not yet identified. No item names a subgroup.
- The 9 items without verses cannot be pulled by verse or by subgroup; a cluster item can only be pulled by cluster.

Limit: I checked that the join exists, not that the subgroup it reaches is the right one for the item's question; that is for the reading.

## 4. Decision sought (nothing built; B:105)

1. Retire the document read from 0.GAP pre: mark gap type `read_in_files_only` inactive and reword RO4 so it no longer implies documents are read there. Config only.
2. Option A: leave the open_item pull as it is (by verse, cluster, Strong's). Option B (recommended, inferential): add to the gathered open_item record the subgroup each item reaches through (cluster, Strong's, `surface_subgroup`), so the gap work shows it; no change to which items are pulled. Option C: add a subgroup field to items; a larger change, and 0 items carry one today.
3. The 9 items with no verses: leave them pulled by cluster or escalation, or give each a verse scope.

On the answers I build it as its own small unit and test it on a copy.
