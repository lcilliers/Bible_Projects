# #2200: retire every script not in a utility or module, and gate their use

Session 3cea0e6c, Developer Mode, 2026-10-21. Researcher, verbatim: "my view is that you should
retire all the scripts that is not already in the utilities or modules. and ensure that using a
retired script is gated on me explicitely giving approval for it. It is much cheaper to find the one
or two worhtwhile snippets in this way, than to try and maintain and sort out the large number of
uncontrolled items hanging around."

This replaces the narrower #2200 list (22 `iba/app` modules) and answers #2198 (b): an unregistered
script is retired, not registered after the fact. **Nothing is built or moved yet.** Approve, change
or answer the decisions below.

## 1. What counts as "in a utility or module"

A script (`.py` or `.ps1`, anywhere in the project, archive folders excluded) is **controlled** if
any of these holds:

1. it has an **active** `cfg_utility` row;
2. it is reached from an active entry point: `run.py`, `init.py`, the handler of an **active**
   `cfg_step`, or anything those import (the #2192 reachability test);
3. it is the `ps_script` of an **active** `cfg_work_package`, or a PS script dispatching one;
4. it is wired in `.claude/settings.json` (hooks, status line), or is a package marker
   (`__init__.py`) or PS helper library.

Everything else is **retired**.

## 2. The count (measured read-only today)

**180 controlled, 806 to retire.** Every file is listed in
`outputs/escalation/2200-script-classification-v1-20261021.md`.

| where | to retire | what they are |
|---|---|---|
| `scripts/` | 336 | 328 already registered inactive in `cfg_utility`, plus 8 unregistered |
| `iba/app/migration/` | 245 | one-off migrations, all applied (58 registered inactive, 20 registered *active*, the rest unregistered) |
| `_analytics/` | 163 | study scripts in the cluster/book folders, none registered |
| `iba/app/tools/` | 19 | the #2192 list (exploratory extracts, diagnostics, superseded tools) |
| `iba/app/ps/` | 19 | PS scripts of **inactive** work packages, plus 5 with hardcoded paths and no work package |
| `engine/` | 13 | legacy engine, already registered inactive |
| `iba/prototype/`, `iba/scripts/`, `query_db.py` | 10 | already registered inactive |
| `iba/app/handlers/` | 1 | `candidate.py` (all its steps are inactive) |

**Retire** means: `git mv` into the folder's own `archive/` subfolder, so the folder layout stays
recognisable and a snippet can be found again, plus a `cfg_utility` row set or added with
`inactive=1`, through `apply_logged`. The `_analytics/` scripts go to the `archive/` of the cluster or
book folder they sit in.

## 3. Decisions

**3A. Wrongly classified as retire (they are in use).** Recommended: register each as an active
utility instead of retiring it.
- `iba/app/ps/Start-Iba.ps1`: the session bootstrap.
- `iba/app/ps/Behaviour.ps1`: the front end of the active `lib/behaviour.py`.
- `iba/app/ps/Debate-Run.ps1`: orchestrates the active `operations-ingest` steps.
- The backup scripts that Windows Task Scheduler runs: `scripts/backup_watchdog.ps1`,
  `scripts/mirror_to_nas.ps1`, `scripts/notify_backup_alert.ps1`,
  `scripts/install_backup_watchdog_task.ps1`. Retiring them would stop the backups. `scripts/env_setup.ps1`
  goes the same way if you use it.

**3B. Modules in active use but registered inactive.** `iba/app/lib/narrativegenerate.py`
(`book-narrative`) and `iba/app/lib/wordregistryspanreport.py` (`word-registry-span-report`) carry a
NON-COMPLIANT inactive row (#2201 item 5), but active work packages call them. Option 1: keep them
live and fix the hardcoded constants under #2201 (recommended). Option 2: retire them, together with
their two work packages.

**3C. The `_analytics/` study scripts (163).** The study is on hold. Moving them is filing only:
no study content changes. Option 1: retire them now, into each folder's `archive/` (recommended; you
said "all"). Option 2: leave them until the study re-opens.

**3D. The 20 migrations registered active.** All migrations are one-offs already applied, so
recommended: retire all 245, those 20 included.

## 4. The gate

Recommended design: one hook plus the validate check from #2198.

- **Hook** `.claude/hooks/gate_retired_script.py`, a `PreToolUse` hook on the Bash and PowerShell
  tools, so it runs before any command executes. It refuses a command that runs a retired script.
  "Retired" means a path under any `archive/` folder, a file whose `cfg_utility` row is inactive, or
  `python -m` of such a module. **Unless** an escalation names that script's path in its context and
  is `approved`, with the approval given by you (originator Researcher).
- **How you approve:** I raise a decision_required item naming the script and why it's needed. Your
  `approved` on that item is the permission, for that script only. No approval, no run. A refusal
  names the item to approve.
- **What it doesn't cover:** reading a retired file to find a snippet. Reading is not running, and
  that's how the worthwhile snippets get found. Copying a snippet into a controlled module goes
  through the normal registration (rule 62).
- Already in place: `run.py` refuses an inactive work package or step.
- **Validate** (#2198): `configmaint.validate` gets a hard error for any live unregistered script
  outside `archive/` (temp_ scripts excepted), so nothing new floats unregulated. #2198 (c) is
  answered by this design: hard error.
- **Test plan**, run before it is live:
  - synthetic: a retired path is blocked; the same path with an approved item is allowed; an active
    script is allowed; `python -m` of a retired module is blocked; a read (`cat`/Read) of a retired
    file is allowed.
  - real: a run of `Escalation.ps1` and `Start-Iba.ps1` passes.

## 5. Order of work, once approved

1. The gate hook and its test plan, then registration in `.claude/settings.json`.
2. Register the 3A scripts as active utilities.
3. The retirement: one migration for the `cfg_utility` rows (`apply_logged`) and the `git mv`s,
   committed per folder group. Then the manifest rebuild and the BUILD.md list.
4. The validate check (#2198).
5. Verify: `Start-Iba.ps1`, `Config-Maintenance.ps1 -Step Validate`, the escalation list and a
   session-close dry run all pass.
