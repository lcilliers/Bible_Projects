# #2286 prototype step 5: cluster.subgroup on M18, the experiment

Date: 2026-10-25. Escalation #2286 v11. Only previews were run: no API call was made and nothing was
written, apart from the escalation the step raised itself (#2288).

## 0. The instruction (v11, verbatim)

> you are rightly pointing out that a verse can belong to many sub groups. lets experiment. can you
> run the cluster.subgroup for M18 (one of the clusters that was done through ledger method). Take
> not of the time it takes to generate the subgroups for this cluster.

## 1. What happened

| step | command | result | time |
|---|---|---|---|
| cluster.subgroup, preview | `iba\app\ps\ClusterSubgroup.ps1 -ClusterCode M18` | **refused** (report-stop, exit 3): M18 is at status `t_cluster_assignment_completed`, not `ready_for_subgroup_allocation`. The step raised #2288 itself. | 6.7 s (the refusal, not a grouping) |
| Stage 1 verse-reading, preview | `iba\app\ps\VerseReading.ps1 -ClusterCode M18` | PREVIEW: 1,366 batches, 1,366 verses, 88 codes, **estimated $850.55**, 4 verses already covered; no API call made | 7.9 s |

**No subgroups were generated, so I have no timing for that.**

## 2. Why the step refused

The as-built pipeline only lets subgrouping start once Stage 1 is done
(`iba/app/lib/clusterstatus.py`, `verse_reading_completeness`). Every one of the cluster's member
codes must have at least one `ib_observation` row with `stage='verse-reading'` and
`cluster_code='M18'`.

| fact on M18 Desire & Longing | value |
|---|---|
| live member codes (`cluster_strong`) | 88 |
| `ib_observation` rows with cluster_code M18 | 0 |
| `ib_node` rows with cluster_code M18 | 60, all source_stage verse-reading |
| status | t_cluster_assignment_completed (since 2026-09-16) |
| subgroups | none |

The ledger-method work on M18 doesn't count towards the gate. The gate reads only Stage 1
observations recorded under the cluster's own code. Across all 95 live clusters, 92 are at
`t_cluster_assignment_completed`. So this refusal will happen for every cluster except the three
that already have subgroups.

## 3. Ways forward

Choosing one is a new decision (B:44), so it's for you:

| option | what it means | cost and risk |
|---|---|---|
| **A. Run the pipeline as built.** Stage 1 first (VerseReading, API), then cluster.subgroup (API). | gives subgroups the way M49, M67 and M83 got them | about $850 estimated for Stage 1 alone. These are the API steps #2275 (#2268 B3, parked) plans to retire. #2267 notes that observations from these stages were never checked against the observation rules. |
| **B. Do the subgrouping by hand in this session, as the prototype.** I read M18's 88 codes: their glosses, their senses, and what the ledger work recorded on them. I group them by meaning into at most 10 subgroups, in a file, timed. Nothing goes into `cluster_subgroup`. | answers your timing question, and shows whether the ledger work is enough of a base for grouping | session time only. The result is a trial for you to judge, not data. |
| **C. Change the gate** so that ledger work, or no prior reading at all, is enough to start subgrouping. | lets the step run on clusters done through the ledger method | design and build work, not for this experiment (B:105) |

My recommendation is **B**. It's the experiment you asked for, it costs nothing, and the timing it
gives is the one that matters if the API steps are being retired.

| your decision | |
|---|---|
