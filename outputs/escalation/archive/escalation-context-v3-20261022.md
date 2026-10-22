# What the open escalations point to

> Generated 2026-10-22T03:22:14Z by `Escalation.ps1 -Action Context` (#2173 P1). Every file named in any field of any version of each open escalation (raised, in-progress, re-assigned), resolved to its latest live version. **Read the resolved file**, not the one named. Findings: `missing` = no live version exists (the escalation points at nothing); `bare` = a bare filename (cfg_escalation rule 7).

- escalation #2211; findings: **3**


## Contents

- [Escalations](#open-escalations-and-their-files)

<a id="open-escalations-and-their-files"></a>
## Open escalations and their files

### #2211 -- Context drops the dot from .claude/ paths

state `in-progress`, next action `review`, assigned Claude

| named | where named | read this (latest live) | status | size / changed |
|---|---|---|---|---|
| `Escalation.ps1` | comment v1 | `iba/app/ps/Escalation.ps1` | **bare** -- bare filename (rule 7); resolved by its unique name | 39041 B, 2026-10-22 04:14 |
| `iba/app/lib/escalationcontext.py` | comment v1, context v1 | `iba/app/lib/escalationcontext.py` | current | 11286 B, 2026-10-22 04:14 |
| `claude/hooks/rules_at_point_of_use.py` | comment v1, comment v1 | -- | **missing** -- no live version exists | -- |
| `claude/) loses its leading dot, so every escalation naming a .claude file gets a false missing finding. The same run also flagged a bare Escalation.ps1` | comment v1 | -- | **missing** -- no live version exists | -- |
| `outputs/escalation/escalation-context-v2-20261022.md` | context v1 | `outputs/escalation/escalation-context-v2-20261022.md` | current | 2021 B, 2026-10-22 04:16 |
