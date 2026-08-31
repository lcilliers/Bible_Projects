# Escalation deep history

## #1312 — cfg_table.category built; grant revocation pending approval
type=task source=Claude

**v1** (2026-08-31T05:05:26Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** cfg_table.category built; grant revocation pending approval
> **comment (set this version):** Escalation #1146s approved design implemented: cfg_table.category (rule|data|log) added, all 189 rows backfilled (33 rule, 2 log, 154 data), the 2 scan sites with an actual behavioural bug fixed and verified live in isolation (_known_cfg_tables now excludes both log tables from write-touchable scope; find_cfg_tables_missing_configmaint_grant no longer flags them). The other 2 named sites reviewed and correctly left as-is (existence checks, not write-permission scope -- category doesnt change their correctness). Write-grant revocation itself proposed via configmaint.propose, pending your approval: cfg_write_grant.inactive=1 for configmaint.propose on both log tables (run ids RUN-20260831_060427_200-CONFIGMAINT, RUN-20260831_060428_295-CONFIGMAINT). One loose end, unrelated: a full configmaint.validate run hit a PermissionError on workflow\schema\cfg_table.csv (file locked by another process) -- not caused by this change, not yet chased down. Full record: iba/app/BUILD.md sec215.
> **context (set this version):** iba/app/BUILD.md#215; supersedes/continues #1146

**v2** (2026-08-31T05:28:08Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):**  proceed 
> **context (set this version):**   
