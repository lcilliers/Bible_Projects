# What the open escalations point to

> Generated 2026-10-22T04:18:20Z by `Escalation.ps1 -Action Context` (#2173 P1). Every file named in any field of any version of each open escalation (raised, in-progress, re-assigned), resolved to its latest live version. **Read the resolved file**, not the one named. Findings: `missing` = no live version exists (the escalation points at nothing); `bare` = a bare filename (cfg_escalation rule 7).

- escalation #2207; findings: **4**


## Contents

- [Escalations](#open-escalations-and-their-files)

<a id="open-escalations-and-their-files"></a>
## Open escalations and their files

### #2207 -- cfg_* is structurally coherent, but has new findings since…

state `in-progress`, next action `approved`, assigned Claude

| named | where named | read this (latest live) | status | size / changed |
|---|---|---|---|---|
| `/cfg.enum() usage, 13 behaviour rule(s) with no control, 2 PS script(s) bypassing run.py` | context v1 | -- | **missing** -- outside the project (rule 83: not an authoritative source) | -- |
| `outputs\\configs\\CONFIG-REPORT-v605-20261021.md` | context v1, context v1 | `outputs/configs/CONFIG-REPORT-v608-20261022.md` | newer -- a newer version than the one named exists | 743101 B, 2026-10-22 04:19 |
| `/cfg.enum() usage, 5 behaviour rule(s) with no control, 9 escalation-tied file(s) not carrying their escalation-id prefix, 2 SQL scratch file(s) violating the scripts/SQLite/ folder convention. All findings: 4 orphan config(s), 12 utility module(s) with zero cfg.setting()/cfg.enum() usage, 13 behaviour rule(s) with no control, 2 PS script(s) bypassing run.py` | context v1 | -- | **missing** -- outside the project (rule 83: not an authoritative source) | -- |
| `outputs/escalation/2207-new-config-findings-v1-20261022.md` | context v3, resolution v3, comment v4, context v6 … | `outputs/escalation/2207-new-config-findings-v1-20261022.md` | current | 7877 B, 2026-10-22 04:55 |
| `outputs/escalation/2207-fix-not-count-v1-20261022.md` | context v6, resolution v6, comment v8 | `outputs/escalation/2207-fix-not-count-v1-20261022.md` | current | 4102 B, 2026-10-22 04:57 |
| `BUILD.md` | comment v9, comment v12 | `iba/app/BUILD.md` | **bare** -- bare filename (rule 7); resolved by its unique name | 1522387 B, 2026-10-22 05:11 |
| `lexicalenrich/lexicalscope retired (touches iba/app/handlers/cluster.py` | comment v9 | `iba/app/handlers/cluster.py` | current | 32268 B, 2026-10-21 11:28 |
| `iba/app/handlers/lexical.py` | comment v9 | `iba/app/handlers/lexical.py` | current | 60681 B, 2026-10-21 11:04 |
| `iba/app/lib/taggingguidance.py` | comment v9 | `iba/app/lib/taggingguidance.py` | current | 9738 B, 2026-10-21 11:25 |
| `scripts/backup_db_to_nas.py` | comment v9 | `scripts/backup_db_to_nas.py` | current | 12810 B, 2026-10-14 11:05 |
| `run.py` | comment v9 | `iba/app/run.py` | **bare** -- bare filename (rule 7); resolved by its unique name | 14185 B, 2026-10-21 11:11 |
| `iba/app/lib/recordingpass.py` | comment v12 | `iba/app/lib/recordingpass.py` | current | 34979 B, 2026-10-22 05:06 |
