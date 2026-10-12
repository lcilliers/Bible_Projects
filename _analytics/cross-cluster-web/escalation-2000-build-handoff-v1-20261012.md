# Escalation #2000: build handoff for a Developer Mode session

**Date:** 2026-10-12 · **Status:** the design and the import preview are approved. ~~Nothing is built.~~ **Built 2026-10-12** (steps 1–8; `iba/app/BUILD.md` §336). What is left is §4: the test plan `iba/docs/2000-open-threads-test-plan-v1-20261012.md`, run in a standard session.

**Researcher, verbatim:** *"approve the preview, proceed with the build"*.

**Why the build is not in the approving session.** The build changes the IBA app's escalation module, so it needs Developer Mode. Developer Mode is declared only as the first prompt of a fresh session (`/developer-mode`; CHARTER.md §4, GOVERNANCE.md §69). See #2001 for the gate gap found while stopping.

## 1. Start

1. A fresh session, with `/developer-mode` as the first prompt.
2. Read the spec: `_analytics/cross-cluster-web/open-threads-table-proposal-v3-20261012.md`. §0 holds rounds 1 to 6 verbatim, §3 to §5 the design, and §7 and §8 the order and the tests.
3. Read the data to import: `_analytics/cross-cluster-web/escalation-2000-open-threads-register-import-preview-v1-20261012.json`, rebuilt by `escalation-2000-open-threads-import-preview-v1-20261012.py`.
   - Re-run the script first. Import only if its summary is unchanged:
     - 100 threads, 278 items, 50 responses
     - 2 rebuilt threads (OT-101, OT-102), with 6 items between them
   - If the register changed after approval, show the difference to the researcher before importing.

## 2. Build order (proposal §8); one checkpoint each

| Step | What | Where |
|---|---|---|
| 1 | Config, T0 to T9 | `cfg_enum`: `escalation_type` + `thread`; `escalation_thread_item_kind`; `escalation_thread_item_response_kind`. `cfg_escalation`: amend row 4; new rows T1, T2, T6. `cfg_escalation_transition`: T3, T6. `cfg_escalation_requirement`: T4, T6 (`no_open_thread_items`, a new check kind, so also `cfg_enum escalation_requirement_check_kind`), T7. `cfg_behaviour_rule` `open-threads-carried-as-escalations`. Register every new table and column in `cfg_table` / `cfg_column` in the same unit of work. |
| 2 | Schema | `escalation` and `escalation_history`: `alias` (unique where set) and `comes_back_when`. New tables `escalation_thread_item` (with `item_no`, `status`, `opened_at`, `opened_by`; no closing columns) and `escalation_thread_item_response`. As a migration under `iba/app/migration/`. |
| 3 | Raise | `-State` on manual Raise only (T2); `raise_()`, the code path, keeps `raised` (module blocking, proposal §2.1). Threads must be `self_correctable`, with at least one `-Item`; the alias is assigned automatically. |
| 4 | Match and transitions | `-Action Match -For nnnn` adds an `escalation` item, which moves the thread `on-hold` → `in-progress`. Closing items: if all are closed, a thread may go to `approved`; if some stay open, it goes back to `on-hold`. A task closing closes its `escalation` items. |
| 5 | Views | `-Action Thread` (with `-Id OT-16`, showing items and responses), the List section, and `-Action Export -Type thread`, which regenerates `open-threads-register.md` with `OT-nn · #id`. `-Id` accepts the alias everywhere. |
| 6 | Session start | `.claude/commands/start-project.md` step 4B: the T5 check, counting **in-progress** tasks and issues only. `cfg_escalation` 4 now counts `in-progress` threads only. |
| 7 | Import | Back up iba.db. Freeze the `.md` as `archive/open-threads-register-frozen-20261012.md`. Import from the JSON, check the counts, export, and compare row by row. |
| 8 | Documents | GOVERNANCE.md (a new section), BUILD.md, USER-GUIDE.md, CLAUDE.md pointer, session-close (regenerate the register). |

## 3. Facts met while designing (so they are not rediscovered)

- `lib/escalation.py`:
  - `_title_shape_error` enforces 60 characters, one line, and no "--"
  - `raise_()` (line ~583) is the code path, and `raise_new()` (~834) the manual one
  - `update()` is at ~888
  - `write_list_report()` is at ~1152
- `Escalation.ps1` has ValidateSets at lines ~182 to 214. The `-Type` set must gain `thread`. All values are lowercase (#872).
- `escalation_history` mirrors every column of `escalation`, so the new columns go on both.
- `cfg_escalation_transition` and `cfg_escalation_requirement` hold rows by priority, shape, and condition or check kind. They were read in full on 2026-10-12 (13 active requirement rows), and only the T-rows above change.
- `cfg_escalation` 3, module blocking (`run.py` `run_step()`), checks for items at `raised` or `re-assigned` against a module or step. Threads never sit at `raised`.

## 4. After the build

Testing happens in a later standard-mode session, not the one that built it. That session runs the §8 test list, then one full session start and close on the new path.
