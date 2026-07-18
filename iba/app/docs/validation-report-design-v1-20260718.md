# Design: validation reports for the raw layer

> Directed 2026-07-18. Deliver visibility that a raw build is **correct and complete**, the
> **database is sound**, and the **app ran successfully** — covering registry and every raw table.
> Simple, config-driven, read-only where it can be.

## What the researcher asked for

1. **Pre / post validation** — what state a run changed (the delta it produced).
2. **Update expectations + validation of success** — declare what a run *should* produce and check
   the actual result against it.
3. **Validation of the database and app running success** — the store is sound and the run finished.

## Approach — two pieces

**A. Pre/post snapshots (the only pipeline touch).** The dispatcher records a row-count snapshot of
every data table at **run start** (`pre`) and at **run close** (`post`), into `validation_result`
(reused; no new table). Delta = post − pre = exactly what the run contributed. This makes pre/post
real and general (works for future update runs too), captured where the run lifecycle already lives.
Config: `run` gains a write-grant on `validation_result`.

**B. The validation report (new, read-only).** `python -m iba.app.validation --word <w>` computes
the full check suite live over the DB and writes `iba/app/reports/validation-<word>.md`. It does
**not** change the gate — `raw.validate` stays the authoritative stop — it *reports*. Sections:

| section | answers | how |
| --- | --- | --- |
| **1. App & DB running success** | did the app run, is the store live | config loaded · all data tables present · STEP known-answer probe · latest run for the word = `done` |
| **2. Pre/post (the delta)** | what the run changed | per table: pre-count, post-count, delta (from the run's snapshots) |
| **3. Integrity (all raw tables)** | is the store sound | config-**derived**: every `notnull` column has 0 NULLs; every dedup key has 0 duplicates |
| **4. References** | do links resolve | every `fk` column (from config): orphans. FK→`verse`/`run`/`word_registry` **must** resolve (FAIL); FK→`strong` **may** orphan by design (WARN — the raw model names strongs it need not hold) |
| **5. Expectations vs actual** | is the build correct & complete | registry built (`status=raw-complete`, source set) · word_strong ≥1 and all non-particle · every `strong` has a `strong_sense` (1:1) · **parse-check**: `span` recovers every `strong_verse` (per word) · `verse.osisId` unique · particles flagged |

Each check yields `expected · actual · verdict (PASS/FAIL/WARN) · detail`. Overall verdict = FAIL if
any FAIL; WARN is allowed. The report leads with the verdict and a PASS/FAIL/WARN tally.

## Why config-driven

Integrity and reference checks are generated from `cfg_column` (notnull, unique key, fk) — so when a
column is added to the schema, its checks appear automatically; no check is hand-maintained per
column. Only the handful of semantic expectations (section 5) are stated explicitly, because they
encode meaning the schema can't (e.g. "span must recover strong_verse").

## Not in v1 (kept simple)

Trend/history across runs; diffing two reports; persisting the section 3–5 results back into
`validation_result` (the report computes them live — the authoritative persisted gate remains
`raw.validate`). These can follow if wanted.

## Files

- `iba/app/config/rules.json` — `run` write-grant += `validation_result`.
- `iba/app/run.py` — pre snapshot at run create, post snapshot at run close.
- `iba/app/validation.py` — the report generator + CLI (read-only).
- output: `iba/app/reports/validation-<word>.md`.
