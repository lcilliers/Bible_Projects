# Thread audit

> Generated 2026-10-23T16:26:43Z by `Escalation.ps1 -Action ThreadAudit` (#2173 P5). Read-only. Each finding is named by its thread item with its reason; a check with no findings is not listed.

- worked strands (all listed escalations completed, `escalation.worked_strand_escalations`): M01 (#1962), M02 (#1963), M08 (#2156), M09 (#2148), M18 (#1993), M25 (#1932), M64 (#1978, #1986), M72 (#1998)
- findings: **1** (T-g 1)


## Contents

- [Findings](#findings-by-check)

<a id="findings-by-check"></a>
## Findings by check

### T-g register file current (1)

- **_analytics/cross-cluster-web/open-threads-register.md**: the register file differs from the escalation table (run Escalation.ps1 -Action Export -Type thread)
