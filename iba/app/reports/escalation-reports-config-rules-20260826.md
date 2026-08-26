# Configs that govern the escalation reports — live extract

> Extracted 2026-08-26 for escalation #857 — the two report-producing steps behind
> `Escalation.ps1 -Action List` and `-Action History`: `escalation.list` (writes
> `escalation-list.md`) and `escalation.history` (writes `escalation-<id>-history.md`). Queried
> live across every config layer these two steps actually touch: `cfg_work_package`, `cfg_step`,
> `cfg_report`, `cfg_report_section`, `cfg_report_csv_table`, `cfg_setting`, `cfg_write_grant`,
> `cfg_utility`.

## 1. Dispatch layer — `cfg_work_package` + `cfg_step`

**`cfg_work_package`** (1 row): `escalation-reporting` — `ps_script='iba/app/ps/Escalation.ps1'`,
`runs_over='none'`, `chained=0`, no complete/paused/next-step messages. This is what makes
`-Action List`/`-Action History` dispatch through `run.py` rather than calling the module
directly (`cfg_behaviour_rule` id 43 — both are named there as the two dispatcher-compliant
actions on `Escalation.ps1`, distinct from `Raise`/`Update`/`AnswerRun`, which are the deliberate
manual front-door exception).

**`cfg_step`** (2 rows, both `kind='utility'`, `scope='none'`):

| ordinal | step | handler | does |
|---|---|---|---|
| 0 | `escalation.list` | `iba.app.handlers.reports:escalation_list` | every open escalation, full history inline, grouped by `related_activity`, plus the D15 exception sections |
| 1 | `escalation.history` | `iba.app.handlers.reports:escalation_history` | deep history for one item, its downward chain (`from_id` children), and every `related_activity`-named item |

## 2. Report-shape layer — `cfg_report` / `cfg_report_section` / `cfg_report_csv_table`

**Both steps ARE registered in the standard reportkit** — this was previously a real gap
(escalation #755 finding 3: "both reports bypass the app's reportkit/cfg_report standard
entirely"), fixed in the register-v9 rebuild (D4/D16/D23, per `cfg_behaviour_rule` id 43's own
note). Confirmed live, not assumed:

**`cfg_report`:**

| step | title | show_toc | output_kind | naming_scheme | archive_dir |
|---|---|---|---|---|---|
| `escalation.list` | "Open escalations" | 1 | `md+csv` | `stable` | `archive` |
| `escalation.history` | "Escalation deep history" | 1 | `md` | `stable` | `archive` |

`naming_scheme='stable'` means both overwrite their fixed filename on every regenerate, rather
than the timestamp-versioned scheme one-off reports use (`governance.oneoff_report_naming_pattern`
does **not** apply to these two — they're routine reportkit outputs, not one-offs).

**`cfg_report_section`** — 9 rows total:

`escalation.list` (7 sections, all `include=1`): `open_items`, `cycle`, `dangling`,
`mismatched_pairing`, `missing_link`, `incoherent_link`, `recently_resolved` — exactly the
sections visible in the live `escalation-list.md` output.

`escalation.history` (2 sections, both `include=1`): `item_history`, `downward_chain`.

**`cfg_report_csv_table`** — 1 row, `escalation.list` only: `table_name='escalation'`, join_note
*"raw, unprocessed dump of the escalation table itself -- NOT the exception-category findings
(those are markdown-only report sections, D4 correction from v4's original, wrong claim that the
CSV was the flagged-exception rows)."* `escalation.history` has no CSV row — consistent with its
`output_kind='md'` only, no gap.

## 3. Output-path layer — `cfg_setting`

- `escalation.list_report_path` = `"iba/app/reports/escalation-list.md"` — the fixed, full path.
- `escalation.history_report_dir` = `"iba/app/reports"` — a directory only; the filename
  (`escalation-<id>-history.md`) is built per-call from the `-Id` argument, so a fixed full path
  setting doesn't apply the same way `escalation.list` uses one.

Both steps satisfy `governance.reports_must_persist` (*"every quality-check or report-producing
step must persist its output to a config-defined report path"*, enforced by
`lib.cfgquality.find_missing_report_paths`, checked in `configmaint.validate`) — confirmed live:
the most recent `configmaint.validate` run this session (§2 of the earlier extracts) reported
`Missing report paths (0)`, and both settings above resolve to real, existing files
(`iba/app/reports/escalation-list.md` and the 40+ live `escalation-<id>-history.md` files
currently in that directory were confirmed present on disk).

## 4. Write-side — `cfg_write_grant` — correctly absent

No `cfg_write_grant` row exists for `escalation.list` or `escalation.history` as writer — correct,
since both are read-only report generators that query `escalation`/`escalation_history` but never
write to them. The only active writer of those two tables remains the `escalation` module itself
(`writer='escalation'`, confirmed in the prior column-rules extract).

## 5. Module registration — `cfg_utility`

`iba/app/lib/escalation.py` is registered (`module='escalation'`, `inactive=0`) — this is where
`write_list_report`/`write_history_report` (named in the `cfg_step.does` text) actually live. The
**handler module itself, `iba/app/handlers/reports.py`, has no `cfg_utility` row** — checked, and
this is **not** an escalation-specific gap: zero files anywhere under `iba/app/handlers/` are
registered in `cfg_utility` (confirmed by sweeping the whole directory), so handler modules as a
category are wired through `cfg_step.handler` directly rather than double-registered. Consistent
with the rest of the project's handler layer, not a defect to raise here.

## Summary

Unlike the `next_action`/enum findings on this same escalation, **the report-generation config
for these two steps is in good order**: fully wired through `cfg_work_package`/`cfg_step`, fully
registered in the standard `cfg_report`/`cfg_report_section`/`cfg_report_csv_table` reportkit
(the one thing #755 previously flagged as missing here, now fixed), output paths satisfy
`governance.reports_must_persist` and were confirmed to exist on disk, and the write-grant/utility
layers are correctly shaped for a read-only reporting pair. No new gap found in this slice.
