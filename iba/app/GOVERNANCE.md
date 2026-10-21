# GOVERNANCE.md — how config governs the app

This file describes the mechanism as it is now. It holds no rule: every rule is a `cfg_*` row,
named here by key, and the config wins wherever this file and the config differ. It holds no
history. Changes are recorded in [`BUILD.md`](BUILD.md), in `cfg_change_detail` (every config
write, with the row's prior state) and in the escalation history. Read those only to assess a past
state.

**The earlier file, with its dated sections §1–§97, is history at
`archive/docs/governance-md-history-to-20261021.md`.** A reference elsewhere to "GOVERNANCE.md §NN"
points to that file.

What the app is for: [`CHARTER.md`](CHARTER.md). How to run each tool:
[`USER-GUIDE.md`](USER-GUIDE.md).

---

## 1. Where every kind of control lives

The control map is `cfg_control_home`: one row per kind of control content (a behaviour rule, a
setting, a procedure, tool usage, change history, study state, and so on). Each row names:
- the kind's **one home**
- **when** that home is read (`cfg_enum control_read_when`)
- **where replaced versions go**, kept out of the routine read path

Everything else points to the home and does not restate it (`cfg_behaviour_rule` 3). The map is
printed as section 15 of the config report.

## 2. The config store

- **Where:** the `cfg_*` tables in `iba/app/db/iba.db`. Each table is registered in `cfg_table` with a
  `category`. `rule` tables are configuration; `log` tables (`cfg_change_log`, `cfg_change_detail`)
  are its audit; `data` tables are not config.
- **The database is master.** The JSON seeds under `iba/app/config/` are a one-time reference, not a
  reload source. The code reads config only through `lib/cfg.py`; a value the code needs is a row,
  never a literal (`governance.rules_must_be_config_driven`).
- **Every value, now:** the config report, written by
  `iba\app\ps\Config-Maintenance.ps1 -Step Report` to `cfg_setting configmaint.report_path`
  (versioned; never edited by hand).

| Area | Tables |
|---|---|
| Schema | `cfg_table`, `cfg_column` (with `use`, `expectation`, `source`, `filled_by`), `cfg_table_purpose`, `cfg_unique`, `cfg_index`, `cfg_trigger` |
| Values and vocabularies | `cfg_setting` (always with a `module`, `cfg_enum config_module`), `cfg_enum` |
| What runs | `cfg_work_package`, `cfg_step`, `cfg_utility`, `cfg_on_fail` (condition → path), `cfg_status_flow` |
| Who may write what | `cfg_write_grant` (data writers, API writers and `configmaint.propose` alike) |
| Reports | `cfg_report`, `cfg_report_section`, `cfg_report_csv_table` |
| Behaviour | `cfg_behaviour_class`, `cfg_behaviour_rule` (with `enforcement_status`) |
| Escalations | `cfg_escalation`, `cfg_escalation_requirement`, `cfg_escalation_transition` |
| The control map | `cfg_control_home` |
| Domain rule sets | e.g. `cfg_candidate_rule`, `cfg_method_rule`, `cfg_passage`, `cfg_book_order`, `cfg_api`, `cfg_connection` |
| Audit | `cfg_change_detail` (row level), `cfg_change_log` (whole reloads), `cfg_meta` |

## 3. How a run reads config

Each `iba\app\ps\*.ps1` script that does project work dispatches through
`python -m iba.app.run <package> --step <step> --run-id <id>` (`cfg_behaviour_rule` 43). `run.py`:
- reads the step's handler and scope from `cfg_step`
- records the run
- resolves each outcome's condition to its path in `cfg_on_fail` (report-stop, pause-continue,
  report-continue, self-heal)

Handlers read their rules from `cfg_setting` and the domain tables. `lib/db.py` builds data tables
from `cfg_column`, refuses a column not declared there, and takes dedup keys from `cfg_unique`. Every
write is checked against `cfg_write_grant`. `IBA_TRACE=1` prints the config reads of a run.

## 4. Changing config

- **App Mode (standard):** `iba\app\ps\Config-Maintenance.ps1 -Step Propose` is the one sanctioned
  path. It writes one row, after a coherence check, and pauses on a `decision_required` escalation.
  The write commits only when the researcher approves (through `Escalation.ps1 -Action Update`),
  and is logged to `cfg_change_detail`.
- **Developer Mode:** the approval gate is removed and nothing else is. Every `cfg_*` write still
  goes through `configmaint.apply_logged()`, so it is audited the same way (`cfg_behaviour_rule` 75).
- **The mode is chosen by the researcher at session start** (`CHARTER.md` §4; `/developer-mode`).
- **A change to config registers itself in the same unit of work:** a new table in `cfg_table` and
  `cfg_column`, a new step in `cfg_step`, `cfg_utility` and `cfg_write_grant`, and so on
  (`cfg_behaviour_rule` 62).
- **Every script is in a utility or module, or it is retired** (#2200). Controlled means an active
  `cfg_utility` row, the handler of a `cfg_step`, the `ps_script` of an active `cfg_work_package`,
  or a hook named in `.claude/settings.json`. Any other script sits in its folder's `archive/`, and
  its `cfg_utility` row is inactive. A migration runs once, then moves to `iba/app/migration/archive/`
  in the same unit of work.
- **Running a retired script needs the researcher's approval.** `.claude/hooks/gate_retired_script.py`
  (PreToolUse, Bash and PowerShell) refuses a command that runs a retired script, unless an
  escalation naming its path carries an `approved` written by the researcher. Reading a retired
  file is never blocked.
- **Not built:** a hard technical block on writing `cfg_*` by any other path. Today it is the
  sanctioned path by rule.

## 5. Checks that config is coherent and used

`configmaint.validate` (`Config-Maintenance.ps1 -Step Validate`):
- **Coherence errors** fail it outright:
  - schema and foreign keys
  - enums
  - value quality through `cfg_column.expectation` (`enum.<name>`, `pattern:<key>`)
  - tables, columns or triggers in the live schema but missing from `cfg_table`/`cfg_column`/`cfg_trigger`
  - a live script (`.py`/`.ps1` outside `archive/`) in no utility or module, or a retired script left
    outside `archive/` (§4)
- **Findings** are raised as an escalation and listed in the config report's section 0:
  - orphan configs, read by nothing
  - behaviour rules whose enforcement is only declared
  - rule text that a governance document restates

Every active governance setting and behaviour rule is delivered by the start routine (§7).

## 6. Escalations

The `escalation` table holds every open item, task, issue, decision and thread
(`cfg_behaviour_rule` 40). It is operated only through `iba\app\ps\Escalation.ps1`.
- **Shape:** an item raised by a run (dispatcher-tied, `run_id` `RUN-…`) or raised by hand
  (manual, `MANUAL-…`).
- **Type** and **state:** `cfg_enum`. The state groups for open and parked are
  `escalation_state_open` and `escalation_state_parked`.
- **`resolution_kind`:** `decision_required` (answered through Update: `ready_for_approval` →
  `approved`, or reject, revise, noted) or `self_correctable` (closed by Claude through
  ResolveSelfCorrectable).
- **`needs_followup`:** sends an approved item back to Claude instead of closing it.
- **What each move may do:** `cfg_escalation_transition` and `cfg_escalation_requirement`.
- **Hand-over to the researcher:** governed by `cfg_behaviour_rule` 63.
- **Threads** (`type='thread'`, alias `OT-nn`) carry the open-threads register as items and
  responses (`cfg_behaviour_rule` 74). The register file is generated, never edited.
- **History:** every version of an item is a row in `escalation_history`.

## 7. Session routines

- **Start:** `.claude/commands/start-project.md`. `iba/app/ps/Start-Iba.ps1` runs `init.py`: config check and
  load, data tables, the STEP pre-flight, how the last session ended. It then prints every active
  governance setting, behaviour rule and escalation rule in full, from the database. The session
  restates each one in its compliance file, and `Compliance.ps1 -Action Check -Phase Start` must pass
  (`cfg_behaviour_rule` 81).
- **Close:** `.claude/commands/session-close.md`. `iba/app/ps/Session-Close.ps1` checks what the session did,
  decided and left open against the record. Nothing is committed while it shows an open finding
  (`cfg_behaviour_rule` 82). The close writes the session log
  (`governance.session_log_required_content`) and commits twice
  (`governance.session_log_triggers_commit`).

## 8. Open, not decided

- `iba/config/` keeps `DBSchema/` and two JSON files under `utility/`, read only by the retired
  history copies `iba/scripts/archive/build_dbschema.py` and `iba/scripts/archive/probe_step_api.py`
  (#2200). They sit outside `cfg_*` (#2188). The rest of the second configurator design was retired on the researcher's
  instruction (#2182) and is history in `iba/config/archive/configurator-design-to-20261021/`.
- `cfg_column.source` and `filled_by` are recorded but not enforced. `expectation` is enforced
  (§5).
