# #2293 design: the surface mapping steps (#2286 U3)

Date: 2026-10-25. Escalation #2293. Developer Mode session 3646374f. **Nothing is built.** The build
plan (`outputs/escalation/2286-build-plan-v4-20261025.md`) approved U3 at the level of what it does.
Building it needs a few points no ruling settles: the threshold of the size check (C4), and how the
API call for the tail is set up. Under B:44 and B:105 those come to you first, with the design they sit
in. The rules the steps follow are B:117 and B:118. Facts were queried today on live
`iba/app/db/iba.db`; what is marked *(inferential)* is my judgement.

## 1. The facts it is sized on

| measure | value |
|---|---|
| M clusters | 80 |
| (code, surface) pairs | 13,411 |
| head pairs, cut at 80% of each cluster's hits (B:118) | 4,269; median 39 per cluster, largest 256 (M24) |
| tail pairs | 9,142; median 85.5 per cluster, largest 375 |
| pilot clusters | M18: 454 pairs, head 163, tail 291. M67: 44 pairs, head 30, tail 14 (24 inherited, 20 missing) |
| pairs with an empty surface | 4 |

The E3 paper's 3,079 head pairs used one 80% cut over all clusters together. B:118, as approved, cuts
per cluster, which gives 4,269.

## 2. The steps

One PS script, `iba/app/ps/Surface-Map.ps1`, with four steps in a new work package,
`cluster-surface-map`, registered at the clustering stage (Base_data). Every step takes
`-Cluster <code>`.

| step | what it does | writes |
|---|---|---|
| **Pairs** (`cluster.surface_pairs`) | Builds the cluster's pairs file. For each pair it gives: code, gloss, surface, hits, verses, two sample references, head or tail, and its inherited subgroup where one exists (B5). It also lists the cluster's existing groups. The file has blank `groups` and `allocations` sections for Claude to fill. | a file only, `outputs/surface-map/<cluster>-pairs-v{n}-<date>.json` |
| **Apply** (`cluster.surface_apply`) | Writes Claude's filled file (the session pass, B1). Checks before writing anything:<br>- every head pair has a group and a reason;<br>- every group has a kind and a label;<br>- every pair belongs to the cluster.<br>It creates the cluster's anomaly group if missing. Inherited pairs are written as `inherited`. A correction of an inherited pair is written as `session`, its reason starting "correction:" (B5). The 4 empty-surface pairs go to the anomaly group. | `cluster_subgroup`, `surface_subgroup` |
| **Tail** (`cluster.surface_tail`) | Allocates the remaining pairs by the API. It sends the cluster's groups (label, description, kind) and each tail pair (code, gloss, surface, one sample verse). Every pair comes back with a group and a reason, or goes to the anomaly group with its reason. Without `-Live` it is a preview: the pairs, the prompt size and the estimated cost, with no call made. | `surface_subgroup` (`api`) |
| **Check** (`cluster.surface_check`) | Read-only report for the cluster: each group's pairs, hits and share; groups over the size limit (D1); the anomaly group's contents; pairs still unallocated; two-sense pairs. | a report file at a configured path |

So a cluster runs **Pairs → (Claude fills the file) → Apply → Tail → Check**. For M49, M67 and M83,
Pairs pre-fills the inherited placements, so Claude only allocates the missing pairs (M67's 20) and
records any correction.

A subgroup code is `<cluster>_<label slug>`, for example `M18_delight`. Reports and files always
show it with its label (B:100).

## 3. The API call for the tail *(inferential)*

- It reuses the existing call: `iba/app/lib/lexicalenrichgenerate.call_api`, with the key handling,
  cost cap and usage log it already has.
- Model, rates and the per-call cost cap are the existing `lexical.llm_model` (now
  `claude-sonnet-5`), `lexical.llm_rate_*` and `lexical.llm_max_cost_per_batch` ($1.00) (B:6). A new
  setting holds the output ceiling: `cluster.surface_map.tail_max_output_tokens`.
- There is one call per cluster, refused if it is over the cap. Estimate: about 250 characters in and
  120 out per pair, at the current rates. That gives roughly $0.20 for the largest cluster (M23, 345
  tail pairs) and about $6 for all 9,142 tail pairs. The preview gives the real figure before
  anything is spent.

## 4. Decisions

| # | point | options | my recommendation *(inferential)* | your answer |
|---|---|---|---|---|
| D1 | The size check's threshold (C4) | a) flag a group of kind `group` holding more than a set share of its cluster's hits. b) flag over a set number of hits. c) report sizes only, no threshold. | a, with the share at **30%**. In the M18 trial the largest groups held 24% (S8, a qualifier group) and 20% (S3); the gloss group that had to be split held 42%. A flag means "look at this group", not a forced split. | |
| D2 | What the API sees for each tail pair | a) code, gloss, surface and one sample verse. b) without the verse. | a. The surface alone misled on "please" and "love" in the trial. One verse costs little. | |
| D3 | The API settings | a) reuse `lexical.llm_*` as `cluster.subgroup` did. b) its own settings. | a | |
| D4 | Where the steps live | a) their own script `Surface-Map.ps1` and work package `cluster-surface-map`. b) added to `Cluster-Assign.ps1`. | a. Four steps with a cluster, a file and `-Live` don't fit Cluster-Assign's two whole-database steps. | |

## 5. Test plan (B:46), run on a copy

| # | case |
|---|---|
| 1 | Pairs on M18: every pair present once, hits and verses equal to a direct query, head and tail as the 80% cut gives, file versioned |
| 2 | Pairs on M67: the 24 inherited pairs pre-filled with their subgroup, the 20 missing ones blank |
| 3 | Apply refuses: a head pair with no group; a group with no kind; a kind not in the enum; a pair not in the cluster; a blank reason. Each refusal writes nothing |
| 4 | Apply on a valid file: groups and pairs written, the anomaly group created once, the empty-surface pairs in it; re-applying the same file changes nothing |
| 5 | Apply on M67: inherited pairs as `inherited`; a correction as `session` with its reason; the 13 old subgroups untouched apart from their pairs |
| 6 | Tail preview: no call, cost and pair count shown; a cluster over the cap is refused |
| 7 | Tail live on M67 (14 pairs, one small call): every tail pair allocated or in the anomaly group, each with a reason, as `api`; a bad model reply writes nothing |
| 8 | Check: group shares add to 100%; a group over the D1 threshold flagged; unallocated count 0 after Tail; the report file written |
| 9 | Registry: steps, work package, grants (`surface_subgroup` and `cluster_subgroup` for Apply and Tail), settings, utility; validate with no new finding |

Case 7 spends real money, a few cents (*inferential*). It runs only after the preview of case 6
shows the cost.

## 6. After U3

U8a, the pilot (#2298), then runs these steps for M18 and M67, and you see M18's groups against the
step 8 trial before the bulk run.
