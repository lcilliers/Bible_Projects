# How the app is governed by config — the chain, first line to last

> **2026-07-17.** The rebuild after the researcher caught the gap: *"not a single process
> rule from the config is used… I thought the configuration would live in the database."*
> Both are now fixed. This is how.

---

## 1. The two corrections

1. **Config lives in the DATABASE.** The JSON files are the human-editable **seed**;
   `cfgload.py` validates and writes them into `cfg_*` tables in the DB; the running app reads
   **only** from those tables (via `cfg.py`), never from the JSON.
2. **The rules ARE the config.** Every choice the code used to make — what to filter, which API
   may write which table, what happens on a failure, the dedup key, the status flow — is now a row
   in a `cfg_*` table. The code reads it and enforces it. **The code decides nothing.**

---

## 2. The config store (13 `cfg_*` tables in `iba/app/db/iba.db`)

| table | holds | fed from |
|---|---|---|
| `cfg_table` · `cfg_column` · `cfg_unique` | the schema — every data table and column, with `use`/`expectation`/`source`/`filled_by` | `schema.json` |
| `cfg_enum` | the controlled vocabularies (word_status, on_fail, …) | `schema.json` |
| `cfg_connection` · `cfg_api` · `cfg_api_source` | STEP: connection, the 3 routes, and **may_source** (which api may write which table) | `step.json` |
| `cfg_work_package` · `cfg_step` | the run sequence + each step's handler + scope | `run.json` |
| `cfg_setting` | scalar rules — cap, particle pattern, follow_related, head marker, … | `rules.json` |
| `cfg_on_fail` | the fork: `(step, condition) → path` (report-stop / pause-continue / …) | `rules.json` |
| `cfg_status_flow` | which step sets which status | `rules.json` |

**Reload the config:** `python -m iba.app.lib.cfgload`. **Rebuild the data tables from it:**
`python -m iba.app.lib.db --reset`.

---

## 3. The chain — where each part reads config

```
New-Word.ps1            reads the SEQUENCE from the DB (cfg_step) — not from JSON, not from the script
   │  per step:
run.py (dispatcher)     reads the STEP's handler + scope (cfg_step)
   │                    resolves the outcome's CONDITION -> PATH (cfg_on_fail)
handlers (raw/registry) read every rule from cfg:
   │                      · seed filter          cfg_setting discovery.particle_pattern
   │                      · follow relatedNos?    cfg_setting discovery.follow_related   (false)
   │                      · meaning split marker  cfg_setting meaning.head_marker
   │                      · may this api write?   cfg_api_source  (ENFORCED at every write)
   │                      · the status to set     cfg_status_flow
   │  using:
Step (stepapi)          reads connection, routes, cap, walk bounds, particle pattern from cfg
Db (db)                 builds the data tables from cfg_column;
                        write() rejects any column not in cfg_column;
                        upsert() takes its dedup key from cfg_unique
```

**Measured: one run = 1,041 config reads** across its 7 steps —
`columns` 323 · `may_source` 321 · `unique_key` 316 · `setting` 42 · `connection` 21 · `route` 11 ·
`step` 7. Turn it on: `New-Word.ps1 -Trace`, or `IBA_TRACE=1`.

---

## 4. Proofs it is real, not decorative

**A · `may_source` is enforced.** `call1_meanings` may write only `word_strong` (cfg_api_source).
Attempting `call1 → strong` is **blocked**:
```
PermissionError: may_source violation: api 'call1_meanings' may not write 'strong'
```
The control was written in `step.json` for two days and enforced nowhere. Now the code reads it and
refuses.

**B · A rule change in the DB changes behaviour, no code touched.** Set
`cfg_on_fail(registry.exists, word-exists).path` from `report-stop` to `report-continue` in the DB
→ the dispatcher reads the new path and no longer stops on a duplicate word. The behaviour is in
the config row, not in the handler.

**C · The data tables are the config's.** `db.build` reads `cfg_column` to `CREATE TABLE`; a handler
that tries to write an undeclared column is rejected by `write()` against `cfg_column`. The schema
cannot drift from the config because the schema **is** the config.

---

## 5. The one boundary: facts vs rules

Not everything is config. Two things stay in code, and the line is principled:

- **Facts** — the canonical OSIS book order, and the shape of STEP's `<span>` HTML. These are not
  choices anyone makes; they are how the canon and STEP *are*. A fact in config would be a fact
  pretending to be a decision.
- **Rules** — the cap, the filters, the paths, may_source, the dedup keys, the status flow. Every
  one is a choice, and every one is in config.

`rules.json`'s header states this boundary, so it is itself governed, not assumed.

---

## 6. What is still stubbed (honest)

- **The approval escalation** (word `proposed → approved`) is auto-approved; the pause/resume
  machinery and the `escalation` table exist and are used by the zero-strongs path, but the
  researcher-yes/no seam in `registry.create` is a stub.
- **`use` / `expectation` / `source` / `filled_by`** are in `cfg_column` but not yet *enforced* —
  they are the add-rule layer (V8), the next increment: a write would check that the value it
  supplies matches the column's declared `source`, and a validation pass would check every column
  with a `source` was fed.
- **base / cluster / analytics** remain out of scope; this is the raw slice.

---

## 7. Files changed in this increment

```
iba/app/config/rules.json      NEW — the process rules as a seed
iba/app/lib/cfgload.py         NEW — JSON seed -> cfg_* tables in the DB
iba/app/lib/cfg.py             NEW — the runtime reader (reads ONLY the DB, traces every read)
iba/app/lib/db.py              REWRITE — data tables built from cfg_column; keys from cfg_unique
iba/app/lib/stepapi.py         REWRITE — a Step session governed by cfg
iba/app/handlers/*.py          REWRITE — interpreters; every rule from cfg; may_source enforced
iba/app/run.py                 REWRITE — condition -> path via cfg_on_fail
iba/app/ps/New-Word.ps1        the sequence read from the DB; -Trace flag
```
