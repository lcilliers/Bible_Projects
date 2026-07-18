# IBA app — user guide

## About the application

The **Inner Being Analysis (IBA) app** serves the Inner Being Analysis Programme — a structured
academic Bible-research programme whose object is **how Scripture expresses the workings of the
human inner being**: the whole inner life (moral, emotional, volitional, relational, vertical and
horizontal), with no theological bias and the human in focus. It works from a registry of ~214
inner-being words, growing over time, each mapped through the STEP Bible to its Hebrew/Greek
originals via Strong's — but the word registry is **scaffolding, not the object**. The analytical
unit is a **focus point**: a latent, emergent configuration of the inner being that is never
observed directly, only **inferred** from what a verse describes it doing. The method is therefore
**infer, don't extract**, with validity established by the **convergence** of independent
verse-grounded witnesses. *(Plan §1.1.)*

**Why the app exists.** For roughly six months the study was attempted through an AI chat interface
and failed repeatedly — the recurring root causes were rules that lived in a model's memory and
were ignored, extraction masquerading as inference, "completeness" measured as coverage rather than
sound reading, and a fragile, un-replayable chat loop. The application exists to make the study
reliable by moving **the rules, the verse-grounding, and the gates out of a model's memory and into
enforced software**: rules encoded and checked deterministically; the model used only for genuine
inference and always validated; runs that are gated, tracked, resumable and replayable in the
database. *(Plan §1.2, §1.4.)*

**How it is built.** PowerShell is the framework (orchestration and process logic); Python modules
do the work; **rules, settings and dependencies live in the configurator, never hard-coded** —
changing a study rule or the pipeline is a configuration change, not a code change. The app is
built out **operation by operation**, within a common framework. *(Plan §2.)*

> ### Scope of this guide — read this
>
> **The application is under active construction, and this guide grows with it.** Today **one
> operation is live: the new-word run** (register an inner-being word and build its **raw layer**
> from STEP — terms, meanings, verses, and the per-word span layer). The raw layer is the
> evidentiary floor; the interpretive stages (base, lexical, characteristics, findings) and their
> operations will be added in later increments, and this guide will be extended to cover each as it
> lands. Where this guide describes a command or a report, it describes what exists now.

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
