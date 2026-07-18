# IBA app — user guide

> The Inner Being Analysis app, raw slice. Registers an inner-being word and builds its **raw
> layer** from STEP into a database. This guide covers the environment, startup, running, answering
> the app when it needs you, and reading the output.

---

## 1. The environment — what the app needs

| requirement | detail |
|---|---|
| **Python 3.14** | with one package: `requests`. Install: `python -m pip install requests` |
| **the local STEP server** | running at `http://localhost:8989` with the tagged module `ESV_th`. The app never uses the web. |
| **nothing else** | **no `.env`, no secrets, no keys.** STEP is local and takes no key. The connection is in the config, not the environment. |

The app lives in `iba/app/`. The database it builds is `iba/app/db/iba.db` (git-ignored). Run all
commands from the repo root (`C:\Bible_study_projects`).

---

## 2. Startup — once per session

```powershell
iba\app\ps\Start-Iba.ps1
```

This prepares the environment and reports `READY`:

```
IBA app — startup
  ✓ config loaded (244 rows in 15 cfg_* tables)
    config_version: app-0.1.0
  ✓ data tables present (12 tables)
  ✓ STEP up and tagged (http://localhost:8989, ESV_th)
READY.
```

It is **idempotent** — safe to run any time. What it does: validates the config, loads it into the
DB if needed, builds the data tables if missing, and pre-flights STEP.

**If STEP is not running**, it says so and stops short of ready — start the STEP server and run
`Start-Iba.ps1` again. Runs refuse to start without STEP.

**Variants:**

```powershell
iba\app\ps\Start-Iba.ps1 -Reload    # reseed the config from the JSON (after editing a config file)
iba\app\ps\Start-Iba.ps1 -Reset     # rebuild the data tables — DROPS all data, keeps config
```

---

## 3. The first run

```powershell
iba\app\ps\New-Word.ps1 -Word hypocrisy -Source "gap scan 2026-07-18"
```

`-Word` is the English inner-being word; `-Source` is why you are registering it (it is recorded).

The run walks 7 steps, and **the first time a word is seen it pauses for your approval**:

```
  registry.exists    ok             word is new or mid-build
  registry.create    pause-continue a new word needs researcher approval — Register the new word 'hypocrisy'?
PAUSED — a researcher escalation was raised; the run is resumable.
```

This is by design: the app will not add a new registry word without you.

---

## 4. Answering the app (escalations)

When the app pauses, it is waiting for a decision. See what is open:

```powershell
python -m iba.app.lib.escalation list
#   #1 [hypocrisy] at registry.create — Register the new word 'hypocrisy'?
```

Answer it:

```powershell
python -m iba.app.lib.escalation answer hypocrisy yes     # or: no
```

Then **re-run the same command** — it resumes where it paused and finishes:

```powershell
iba\app\ps\New-Word.ps1 -Word hypocrisy -Source "gap scan 2026-07-18"
#   registry.create   ok   'hypocrisy' already approved — proceeding
#   raw.discover … raw.validate   ok
#   COMPLETE — raw layer built for 'hypocrisy'.
```

The pause is durable — you can answer and resume minutes or a restart later. `yes` approves the
word; `no` rejects it and the run stops.

---

## 5. The output

**The report:**

```powershell
python -m iba.app.report --word hypocrisy      # -> iba/app/report-hypocrisy.md
```

It shows, per word: the **validation** results, the **strongs and their meaning**, and **sample
verses** with the verse text and every word's span (Strong's + morphology), each backtracking to
its sense. Every row is checkable against STEP — the `getInfo` / `masterSearch` URLs are in the
report header.

**The database** (`iba/app/db/iba.db`) holds the data directly — browse it with any SQLite tool:
`word_registry · word_strong · strong · strong_sense · strong_meaning_tree · strong_lexicon ·
verse · strong_verse · span`, plus the control tables `run · escalation · validation_result`.

---

## 6. What the report shows is configurable

The report content is config, not code. To change what it shows, edit the settings in the DB
(`cfg_setting`) or the seed `iba/app/config/report.json` then `Start-Iba.ps1 -Reload`:

| setting | effect |
|---|---|
| `report.sample_verses` | how many sample verses to show |
| `report.show_verse_text` | show the verse text above its spans |
| `report.show_validation` | show the validation table |
| `report.span_fields` | which columns in the span table |
| `report.strong_fields` | which columns in the strong table |

---

## 7. Everyday commands, in order

```powershell
# once, at the start of a session:
iba\app\ps\Start-Iba.ps1

# for each word:
iba\app\ps\New-Word.ps1 -Word <word> -Source "<why>"
#   if it pauses:
python -m iba.app.lib.escalation answer <word> yes
iba\app\ps\New-Word.ps1 -Word <word> -Source "<why>"     # resume

# read it:
python -m iba.app.report --word <word>

# start clean (drops data, keeps config):
iba\app\ps\Start-Iba.ps1 -Reset

# see every config the code reads, live:
iba\app\ps\New-Word.ps1 -Word <word> -Source "<why>" -Trace
```

---

## 8. Where things are

```
iba/app/
  config/*.json     the config SEEDS you edit (schema, step, run, rules, report, reference)
  db/iba.db         the database (config tables cfg_* + the data)
  ps/               Start-Iba.ps1 · New-Word.ps1
  init.py           the bootstrap (Start-Iba calls it)
  lib/              cfg (read) · cfgload+cfgcheck (load+validate) · db · stepapi · escalation
  handlers/         registry · raw   (the step logic — interpreters, no hard rules)
  run.py            the dispatcher
  report.py         the output
  GOVERNANCE.md     how config governs the code
  UTILITIES.md      the utilities around the run
  USER-GUIDE.md     this file
```

For the raw model (term → sense → span) and the data-layer design, see
`iba/docs/stream-registry-word-buildout-v7/v8` and `iba/docs/raw-config-design-v1`.
