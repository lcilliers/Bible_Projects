# The utilities around the run — build record

> **2026-07-18.** After the researcher's correction — *"you didn't build out all the utilities and
> IBA app configs around the run… this leaves the app vulnerable… hardcoding scripts that should
> never have taken place."* Fair. This increment builds the surrounding utilities and removes the
> hardcoding, so the run is not a bare vertical but a governed whole.

---

## 1. What was built

| # | utility | what it does | answers |
|---|---|---|---|
| A | **config-maintenance** (`lib/cfgcheck.py`) | validates the seeds are coherent **before** they load; `cfgload` refuses invalid config; every accepted load is audited (`cfg_change_log`, seed hash) | *"are you using the utility to maintain the configs?"* — now there is one |
| B | **de-hardcoding** (`config/reference.json`) | the canonical book order and the STEP HTML span pattern moved from Python into config (`cfg_book_order`, `cfg_setting`) | *"hardcoding scripts that should never have taken place"* |
| C | **write grants** (`cfg_write_grant`) | every writer — an API, a step, or the dispatcher — is granted its tables in config; a write outside the grant is refused | generalises `may_source` so **no write is ungoverned** |
| D | **util.validation** (`validation_result`) | the validate step **persists** its checks (parse-check + no-null) as inspectable rows | *"how would I add the validation output to the report"* — it is now stored, so it can be |
| E | **util.escalation** (`lib/escalation.py`) | a real, durable, resumable researcher approval — pause → answer → resume | the stub is gone |
| F | **validation in the report** | a config toggle (`report.show_validation`) renders the validation table | the second half of the researcher's question |

---

## 2. The config-maintenance utility (A) — the discipline that was missing

`cfgload` no longer trusts the JSON. It calls `cfgcheck.check()` first, and **rejects the load**
if anything is incoherent:

- a `may_source` / write-grant naming a table that does not exist
- a step whose handler does not import or resolve
- an `on_fail` path not in `enum.on_fail`; a status not in `enum.word_status`
- a FK to an unknown table/column; a regex setting that does not compile
- a report field naming a column that is not there

**Proved:** injecting `call2_getInfo.may_source += 'nonexistent_table'` →
`config INVALID — step: api call2_getInfo may_source unknown table 'nonexistent_table'`, and
**nothing is written.** Bad config cannot reach the running app. Every accepted load writes a
`cfg_change_log` row with a seed hash — so "the config that ran" is a record.

---

## 3. De-hardcoding (B) — the line I drew, removed

I had kept the OSIS book order and the span-HTML regex in Python behind a "facts vs rules" line I
invented. The researcher's principle is simpler and I was wrong to carve the exception: **if the
code reads it, it is config.** Both now live in `config/reference.json` → `cfg_book_order` (66
rows) and `cfg_setting['step.span_html']`, read by `stepapi.Step` at construction. The frontier
sort and the span parse read config, not constants.

---

## 4. util.escalation (E) — a real pause, proven

The approval was a stub (auto-approve). Now:

```
RUN 1:  registry.create  pause-continue   "Register the new word 'gratitude'?"   -> PAUSED
        python -m iba.app.lib.escalation answer gratitude yes
RUN 2:  registry.create  ok               "already approved — proceeding"
        raw.* … raw.validate  ok           -> COMPLETE
```

- The word is created **`proposed`**, an escalation is raised, the run **pauses** (exit 2).
- The researcher answers from the terminal (O6); the answer sets the word **`approved`**.
- A **fresh invocation resumes** — because the state is durable in the DB, not in memory. This is
  the pause-not-a-fork the design docs required (O7).
- **Idempotent:** re-running while paused does not raise a duplicate escalation; exactly one row.
  The word advances `proposed → approved → raw-complete`.

---

## 5. The governance surface now

Everything reads config, and every write is granted by config. A full run's config reads are traced
(`New-Word.ps1 -Trace` / `IBA_TRACE=1`). The config store is now **15 `cfg_*` tables**:

```
cfg_table cfg_column cfg_unique cfg_enum            the schema (data tables built from it)
cfg_connection cfg_api cfg_write_grant             STEP + who-may-write-what (ENFORCED)
cfg_work_package cfg_step                          the sequence + handlers
cfg_setting cfg_on_fail cfg_status_flow            the rules
cfg_book_order                                     reference data (was hard-coded)
cfg_change_log                                     the audit of accepted loads
```

**Data tables:** `word_registry · word_strong · strong · strong_sense · strong_meaning_tree ·
strong_lexicon · verse · strong_verse · span · validation_result · run · escalation`.

---

## 6. Still honestly out of scope

- **base / cluster / analytics** — this remains the raw slice. `span_analysis` (the derived
  overlay) is designed but not built here.
- **`use` / `expectation` / `source` / `filled_by`** are in `cfg_column` and now partly checked by
  `cfgcheck` (FK/source coherence), but not yet *enforced per write* (a write proving its value
  matches the column's `source`). That is the add-rule layer — the next increment, and now the
  config carries what it needs for it.
- **util.db** as a distinct connection/transaction/backup utility — `lib/db.py` is the access
  layer; a formal `util.db` (pooling, transactions, backup policy) is not yet separated out.

---

## 7. Files this increment

```
config/reference.json          NEW  — book order + patterns (de-hardcoded)
lib/cfgcheck.py                NEW  — validate-before-load (the maintenance utility)
lib/escalation.py              NEW  — util.escalation: raise / answer / resume
lib/cfgload.py                 +    — validate, audit, cfg_write_grant, cfg_book_order, reference
lib/cfg.py                     +    — may_write, book_order accessors
lib/stepapi.py                 +    — book order + span pattern from config
lib/db.py                      (unchanged interface)
handlers/registry.py           REWRITE — the durable approval flow
handlers/raw.py                +    — write grants; validate persists to validation_result
run.py                         +    — control writes under the 'run' grant; idempotent escalation
report.py                      +    — the Validation section (config-toggled)
config/schema.json rules.json report.json  +  — validation_result, escalation.word, grants, toggles
```
