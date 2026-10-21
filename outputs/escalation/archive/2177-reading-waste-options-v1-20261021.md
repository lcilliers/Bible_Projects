# 2177 — Reading waste: what the routines make Claude read, and options to cut it

Escalation: #2177 (reset of the IBA app). Status: options for the researcher's decision. Nothing built.

## The instruction

Researcher, chat 2026-10-21 (verbatim): "my observation is that the there is a lot of
inconsistencies, redundant routines, incoherent rules still in the active processes. a) configs have
a long list of incoherent notifications/warning (#2197). Remember everything you read which is not
necessary/just result in an error or exception/ not coherent is a waste of real money in terms of
costs and tokens. we have spent the a lot of tokens on sorting out so far - resulting in multiple
corrective actions and still I see 'failed', 'configs', long lists of rules that is being read
unneccessary"

## What this session's start actually cost (checked facts, session ac12e7c5)

| Item | Measured | Why it is waste |
|---|---|---|
| Rule text read to fill the compliance file | 70,177 bytes, 145 rows (52 settings, 80 behaviour rules, 13 escalation rules) | 96 of 145 rows were `not engaged` before any task was named. Many settings are plain values, not rules (e.g. `governance.oneoff_report_format` = `md`, `governance.scripts_ps_dir` = `iba/app/ps`). Domain rules are delivered as `always` whatever the task: prose change-log (rules 48-55), API calls (5-10), cluster labels (66), ib_observation (68). |
| Compliance file written | 19,573 bytes | Mostly "not engaged, no task yet" restatements, re-done every session. |
| Escalation list report | 22,345 bytes, 20 items | Includes the full version history of 13 parked items that need no action. |
| #2197 record | `context` column holds 41,180 chars of JSON | Stale: it reports 165 unregistered scripts from run RUN-20261021_120244_669, before #2198/#2200 retired 798 scripts. #2177 v18 says validate is now clean except the 4 orphan enums. Reading #2197 costs tokens and gives wrong facts. |
| Permanent validate advisories | 81 "behaviour rules not mechanically enforced" | 68 of them are `context_delivered` by design. The warning can never clear, so it repeats every run (rule 44: a finding that recurs run after run is a design gap). Same shape: 10 "low config density" utilities. |
| Stop hook | fires at every turn end on #2177 | #2177 is a standing parent item. The hook demands a turn of acknowledgement each time, while nothing is due from Claude. |
| Claude's own errors this start | 2 | Compliance.ps1 run under Windows PowerShell 5 (parse errors; the scripts need pwsh 7); a bash heredoc that failed. Both are Claude execution slips (self-correctable), not app defects. |

## Options for decision

Each can be approved, rejected or revised on its own. Each one, once approved, becomes its own
task under #2177, built and tested on a copy (rule 97).

1. **Close #2197 as stale and stop storing validate output in escalations.** Validate writes its
   report to its report path (it already does); an escalation carries only the count and the path,
   never the JSON.
2. **Remove permanent advisories from validate.** Drop the `unenforced_behaviour_rules` and
   `low_config_density_utilities` checks from the run output. Either delete them, or move them to an
   on-demand report run only when someone asks.
3. **Compliance file: rules only, scoped by subject.**
   (a) Plain-value settings (paths, formats, naming patterns) leave the compliance file. They stay
   in `cfg_setting` and are read by the code that uses them.
   (b) Domain rules get a subject (prose, api, cluster, observation, narrative). They are delivered
   only when the session's task touches that subject, the same way `study_active` rules already drop
   out while the study is on hold.
   (c) A rule with no subject is restated. Rows for other subjects are not written at all, so there
   are no "not engaged" rows to fill.
4. **Escalation list: open items only, latest version only by default.** Parked items appear as one
   line each (id, title). Full history only with `-Action History -Id n`.
5. **Stop hook: skip standing parent items.** An item with `comes_back_when` set, or marked as a
   parent of other escalations, does not trigger the end-of-turn check.

## Not proposed here

A full sweep of every routine for redundancy. On 2026-10-21 (#2177 v4) the researcher said a
diagnosis without knowing what to do is not wanted. The five options above are the waste I measured
directly at this session's start. Other waste is added the same way when it is met.

## Decision

| Option | Approve / reject / revise | Comment |
|---|---|---|
| 1 |  |  |
| 2 |  |  |
| 3 |  |  |
| 4 |  |  |
| 5 |  |  |
