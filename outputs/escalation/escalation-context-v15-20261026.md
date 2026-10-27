# What the open escalations point to

> Generated 2026-10-26T17:37:48Z by `Escalation.ps1 -Action Context` (#2173 P1). Every file named in any field of any version of each open escalation (raised, in-progress, re-assigned), resolved to its latest live version. **Read the resolved file**, not the one named. Findings: `missing` = no live version exists (the escalation points at nothing); `bare` = a bare filename (cfg_escalation rule 7).

- escalation #2301; findings: **2**


## Contents

- [Escalations](#open-escalations-and-their-files)

<a id="open-escalations-and-their-files"></a>
## Open escalations and their files

### #2301 -- Named pre-run snapshots are pruned by the run snapshots

state `re-assigned`, next action `approved`, assigned Claude

| named | where named | read this (latest live) | status | size / changed |
|---|---|---|---|---|
| `run.py` | comment v1 | `iba/app/run.py` | **bare** -- bare filename (rule 7); resolved by its unique name | 14185 B, 2026-10-21 11:11 |
| `iba/app/db/snapshots to retention.snapshot_keep_count (5), oldest first, without regard to name. The named pre-run snapshots taken before Developer Mode migrations are pruned with them: the folder now holds only the 5 latest run snapshots, so pre-2292, pre-2293, pre-2294, pre-2298-tail-ceiling and pre-2298-bulk are gone, as are the earlier ones BUILD.md` | comment v1, context v1, comment v2 | `iba/app/BUILD.md` | **bare** -- bare filename (rule 7); resolved by its unique name | 1631597 B, 2026-10-26 17:27 |
| `iba/app/lib/dbsnapshot.py` | context v1, comment v2 | `iba/app/lib/dbsnapshot.py` | current | 4295 B, 2026-10-21 10:48 |
