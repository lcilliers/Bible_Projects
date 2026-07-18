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
  ✓ config loaded (247 rows in 15 cfg_* tables)
    config_version: app-0.1.0
  ✓ data tables present (12 tables)
  ✓ STEP up and tagged (http://localhost:8989, ESV_th)
    known-answer probe: H0430 -> H0430G gloss 'God', 2088 verses
READY.
```

It is **idempotent** — safe to run any time. What it does: validates the config, loads it into the
DB if needed, builds the data tables if missing, and pre-flights STEP.

**The STEP check is a known-answer probe, not a ping.** It does not merely ask "did something
answer on the port" — it fetches a fixed Strong's (`H0430`) and requires the *expected* answer back:
the gloss must contain `God` and the verse count must clear a floor. A stale, degraded, or wrongly
tagged server that still answers the port **fails** the check with a specific reason — so a green
STEP line means STEP genuinely served the right data, and the probe line shows the evidence. (The
probe values live in config: `iba/app/config/step.json` → `preflight`.)

**If STEP is not running / not right**, it says so and stops short of ready — for example:

```
  ⚠ STEP not ready: STEP answered but the known answer is WRONG: H0430 glossed '…',
    expected to contain 'God'. Stale or wrong module.
```

Start (or restart) the STEP server and run `Start-Iba.ps1` again. Runs refuse to start without STEP.

> **A note on "STEP looks closed but the app says up."** Closing the STEP *window* does not always
> stop its *server* — a `step.exe` process can keep holding port 8989 and answering. If the app
> reports up when you thought STEP was down, that stale process is why. Check what is really on the
> port and, if it is a leftover, stop it before restarting STEP:
>
> ```powershell
> Get-NetTCPConnection -LocalPort 8989 -State Listen | Select-Object OwningProcess
> Get-Process -Id <that-pid>          # confirm it is step.exe
> Stop-Process -Id <that-pid>         # only if it is a stale STEP you want gone
> ```

**Variants:**

```powershell
iba\app\ps\Start-Iba.ps1 -Reload    # reseed the config from the JSON (after editing a config file)
iba\app\ps\Start-Iba.ps1 -Reset     # rebuild the data tables — DROPS all data, keeps config
```

---

## 3. The first run

```powershell
iba\app\ps\New-Word.ps1 -Word <word> -Source "<why>"
# e.g.
iba\app\ps\New-Word.ps1 -Word hypocrisy -Source "gap scan 2026-07-18"
```

`-Word` is the English inner-being word; `-Source` is why you are registering it (it is recorded).

**The word is normalised and de-duplicated at entry.** Surrounding whitespace and stray characters
are stripped (`[hypocrisy]` → `hypocrisy`), and matching is **case-insensitive** (`Fear` and `fear`
are one word). So a typo like `[hypocrisy]` is recognised as the existing word, not registered as a
new one. Before registering, the app also checks whether an existing word already holds the same
Strong's — if so, it asks you to confirm it really is a distinct word (see §4).

The run walks 7 steps, and **the first time a genuinely new word is seen it pauses for your
approval**:

```
  registry.exists    ok             'malice' is not in the registry — a new word
  registry.create    pause-continue a new word needs researcher approval — Register the new word 'malice'?
PAUSED — a researcher escalation was raised; the run is resumable.
```

`registry.exists` tells you the true state of the word rather than a vague label:

| the word is… | you see |
| --- | --- |
| never seen | `'<w>' is not in the registry — a new word` |
| awaiting your approval | `'<w>' is in the registry awaiting your approval — will resume its approval` |
| approved, not yet built | `'<w>' is approved but its raw layer is not built — will build it` |
| previously rejected | `'<w>' was rejected before — will propose it again` |
| already built | **stops:** `'<w>' is already built (status raw-complete)` |

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

**When the app suspects a duplicate**, the question changes to a confirmation — for example if the
word maps to Strong's already held by an existing word:

```text
#   #2 [envy] at registry.create —
#   'envy' shares ALL 3 strongs with existing word 'jealousy'. Register it as a SEPARATE word anyway?
```

Answering `no` stops it (it was a duplicate/typo); `yes` registers it as a distinct word.

---

## 5. Removing test data

To remove a word you registered by mistake or while testing:

```powershell
python -m iba.app.tools.purge_word --word "[hypocrisy]"          # dry-run: shows what would go
python -m iba.app.tools.purge_word --word "[hypocrisy]" --yes    # actually delete
```

It matches the word **literally** (so you can target malformed residue exactly as it sits in the
registry) and removes only that word's own rows — its registry entry, discovery links, escalations,
runs, and validations. It **does not** touch the shared raw layer (strongs, verses, spans), which
other words may reference; a full cascading delete is a later operation. Always dry-run first.

---

## 6. The output

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

## 7. What the report shows is configurable

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

## 8. Everyday commands, in order

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

# remove a test word (dry-run, then --yes):
python -m iba.app.tools.purge_word --word <word>

# start clean (drops data, keeps config):
iba\app\ps\Start-Iba.ps1 -Reset

# see every config the code reads, live:
iba\app\ps\New-Word.ps1 -Word <word> -Source "<why>" -Trace
```

---

## 9. Migrations (one-off setup)

These run **once** to bring the legacy study into the app. They live in `iba/app/migration/`
(kept separate from the standard methods) and are not part of the daily flow.

**Migrate the legacy registry** — load the old word list, running the new-word build for each word
in series:

```powershell
iba\app\migration\Import-LegacyRegistry.ps1 -DryRun     # preview the words (no changes, no STEP)
iba\app\migration\Import-LegacyRegistry.ps1 -Limit 5    # trial the first few
iba\app\migration\Import-LegacyRegistry.ps1             # the full run, in series
```

It reads the old registry **read-only** (excluding words marked deleted/excluded), auto-approves
each (the list is your own curated, already-approved registry), **skips words already built** — so
if it stops it can simply be re-run and it continues — and writes a transcript to
`iba/app/reports/`.

**Migrate the candidate seed** — load the independent candidate-characteristic seed (the base layer
needs this before `Set-Candidates`):

```powershell
python -m iba.app.migration.import_seed
```

It imports the lemma inventory + candidate assessment from the old study and maps it against the
strongs already in the app. Run it once; the new-word build keeps the seed current thereafter.

---

## 10. Where things are

```text
iba/app/
  config/*.json     the config SEEDS you edit (schema, step, run, rules, report, reference, candidate)
  db/iba.db         the database (config tables cfg_* + the data)
  ps/               Start-Iba.ps1 · New-Word.ps1 · Set-Candidates.ps1 · Build-Passages.ps1
  init.py           the bootstrap (Start-Iba calls it)
  lib/              cfg (read) · cfgload+cfgcheck (load+validate) · db · stepapi · escalation · words
  handlers/         registry · raw · candidate · passage   (the step logic — interpreters, no hard rules)
  migration/        one-off: Import-LegacyRegistry.ps1 · legacy_import · import_seed
  tools/            purge_word (maintenance: remove a word's own records)
  run.py            the dispatcher
  report.py · validation.py   the output + validation reports
  GOVERNANCE.md     how config governs the code
  UTILITIES.md      the utilities around the run
  USER-GUIDE.md     this file
```

For the raw model (term → sense → span) and the data-layer design, see
`iba/docs/stream-registry-word-buildout-v7/v8` and `iba/docs/raw-config-design-v1`.
