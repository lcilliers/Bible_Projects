# Spec: IBA config report — full visibility, auto-produced after every change

> Directed 2026-07-18. Build this FIRST next session. It is a local, read-only generator —
> running it costs no AI allowance. Keep it simple.

## Purpose

Give the researcher **full visibility of every configuration the app holds**, from a single
readable file, and keep that file **current automatically** — regenerated after every accepted
config load. Today the only way to see the DB-held config is to query `cfg_*` tables by hand.

## What it produces

One markdown file — `iba/app/config/CONFIG-REPORT.md` (overwritten in place; a live snapshot, not a
versioned deliverable). It reads **only** the `cfg_*` tables from `iba/app/db/iba.db` (the
authoritative config store — not the JSON seeds), and renders, with headings:

1. **Header** — config_version, database, generated-at, and the current seed_hash (from the latest
   `cfg_change_log` row).
2. **Connection** — `cfg_connection` (STEP base/version/timeout).
3. **Settings** — `cfg_setting`: key, value, use (every rule/threshold: walk bounds, particle
   pattern, head marker, greek prefix, registry.strip_ends_pattern, step probe values, report.*).
4. **STEP apis** — `cfg_api`: name, route, input, returns; plus each api's write grants.
5. **Work packages + steps** — `cfg_work_package` + `cfg_step`: the ordered sequence, each step's
   handler, scope, does.
6. **on_fail rules** — `cfg_on_fail`: step, condition, path, message (the fork table).
7. **Write grants** — `cfg_write_grant`: writer -> tables (who may write what).
8. **Status flow** — `cfg_status_flow`: entity, status, set_by, order.
9. **Schema** — `cfg_table` + `cfg_column`: every data table, its columns with type/pk/notnull/
   unique/fk and use/expectation/source/filled_by; `cfg_unique` dedup keys.
10. **Enums** — `cfg_enum`.
11. **Book order** — `cfg_book_order` (summarised: count + first/last, not all 66 inline).
12. **Change-log audit** — `cfg_change_log`: every accepted load, seed_hash, timestamp, validated.

## How it is triggered ("after each change")

- A function, e.g. `iba/app/lib/cfgreport.py::generate(db_path) -> path`.
- Called at the END of `cfgload.load()` (after the audit row is written and committed), so **every
  accepted load regenerates the report**. That is the "after each change" hook — config only
  changes through the loader.
- Also runnable standalone: `python -m iba.app.lib.cfgreport` (for an on-demand refresh), and
  surfaced from `Start-Iba.ps1` output as a one-line pointer ("config report: iba/app/config/
  CONFIG-REPORT.md").

## Constraints

- Read-only over the DB; no writes.
- No AI calls.
- Simple: a straight table-per-section dump. No diffing, no styling beyond markdown tables. (A
  change-diff could come later; not now.)
