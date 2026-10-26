# #2294 decision: when the reading gate starts to bite (#2286 U4)

Date: 2026-10-25. Escalation #2294. Developer Mode session 3646374f. Nothing is built yet.

## What U4 enforces

Behaviour rule B:118 (approved as worded on #2291):

> When a code joins or leaves a cluster its pairs are allocated again, and a cluster with unallocated
> or stale pairs is not read until they are.

U4 builds two things:
- **The check.** For each M cluster it finds its *unallocated* pairs: (code, surface) pairs that
  occur in `verse_lexical` with no live `surface_subgroup` row. These include the pairs of a code
  that has just joined the cluster. It also finds its *stale* pairs: live rows whose code is no
  longer in the cluster, or whose surface no longer occurs.
- **The gate.** `reading.open` refuses a reading whose home cluster has either kind.

## The facts today (queried on live iba.db)

- No M cluster has a single live pair yet. U3 (#2293) built the steps and wrote no pairs; the pilot
  is #2298, and the other 78 clusters come in the bulk run.
- No reading is open. All 4 readings (M64: choose, willing, plan, dedicate) are published.
- The study is active (`governance.study_status`), with `Reading.ps1` as the way readings run.

**So, as worded, the gate refuses every M cluster from the day U4 goes live** until that cluster is
mapped: M18 and M67 after the pilot, the rest after the bulk run (#2298).

## The decision

| option | what it means | |
|---|---|---|
| **G-a** | The gate applies as worded, from now on. No new reading opens on an M cluster until that cluster is mapped. | Matches B:118 exactly. Readings wait for the pilot (M18, M67) and the bulk run. The reading process is itself being rebuilt (#2268 parked behind this prototype), and U5 needs the mapping anyway. |
| **G-b** | The gate applies now to a cluster that has started its mapping (it has at least one live pair). An unmapped cluster can still be opened until the bulk run is done; then a setting, `cluster.surface_map.reading_gate` (`started` → `all`), is switched to make the gate total. | No interruption to standard-session readings meanwhile. Needs one extra setting and a switch at the end of U8, and B:118 gets a sentence saying when it begins. |

**My recommendation *(inferential)*: G-a.** It is the rule as you approved it. No reading is open
today. And under the new model a reading of an unmapped cluster has no home subgroup to read from
(S1). The cost is that no new reading opens until the pilot and bulk run are done.

| your answer: G-a or G-b | |
|---|---|

## What does not depend on this

`cluster.validate` reports unmapped clusters only as a count in its report, never as a finding. On
G-a, 80 unmapped clusters would otherwise re-raise its escalation on every run until the bulk run.
Stale pairs, and partly mapped clusters, are findings. `Surface-Map.ps1 -Step Check` lists a
cluster's stale pairs, and `-Step Apply` soft-deletes them with the reason "stale: <why>" before
writing.
