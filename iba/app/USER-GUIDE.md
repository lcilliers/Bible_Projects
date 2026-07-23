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
> **The application is under active construction, and this guide grows with it — updated
> 2026-07-22.** Live today: the raw layer (**new-word**, §3), the base layer (**candidate
> stamping + passages**, §8), **config maintenance** (§9), **candidate curation** — one-row-at-a-time
> and JSON-batch (§10), **standalone quality checks** (§11), **reports and CSV export** (§12), and
> **log retention** (§13). The interpretive stages above the base layer (lexical, characteristics,
> findings) are not built yet. Where this guide describes a command or a report, it describes what
> exists now. Companion docs: `BUILD.md` (what's built, how the parts fit) and `GOVERNANCE.md` (how
> config governs the code) — this guide is *how to run it*.

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

  orientation (read before making changes):
    BUILD.md      The IBA app — build record — 2026-07-17, first slice...
    GOVERNANCE.md How the app is governed by config — the chain, first line to last...
READY.
```

It is **idempotent** — safe to run any time. What it does: validates the config, loads it into the
DB if needed, builds the data tables if missing, pre-flights STEP, and (added 2026-07-22) prints an
orientation pointer to `BUILD.md`/`GOVERNANCE.md` so a session doesn't start blind.

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

## 3. The first run — registering a word (the raw layer)

```powershell
iba\app\ps\New-Word.ps1 -Word <word> -Source "<why>"
# e.g.
iba\app\ps\New-Word.ps1 -Word hypocrisy -Source "gap scan 2026-07-18"
```

`-Word` is the English inner-being word; `-Source` is why you are registering it (it is recorded).

**The word is normalised and de-duplicated at entry.** Surrounding whitespace and stray characters
are stripped (`[hypocrisy]` → `hypocrisy`), and matching is **case-insensitive** (`Fear` and `fear`
are one word). So a typo like `[hypocrisy]` is recognised as the existing word, not registered as a
new one. A genuine qualifier like `blindness (spiritual)` is left alone — the stripping only removes
a stray bracket wrapping the *whole* word, not a parenthetical that's part of the word itself
(fixed 2026-07-22; see `BUILD.md` §9). Before registering, the app also checks whether an existing
word already holds the same Strong's — if so, it asks you to confirm it really is a distinct word
(see §4).

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

Every pause is answered through **one** front door, `Escalation.ps1` (added 2026-07-21 — every
other governed operation had a PS wrapper from the start, answering never did):

```powershell
iba\app\ps\Escalation.ps1 -Action List
#   #1 [hypocrisy] at registry.create — Register the new word 'hypocrisy'?
#   #238 (run RUN-...-CONFIGMAINT) at configmaint.propose — Add governance.build_md_on_code_change...
```

**Two shapes of pause**, both listed together but answered differently:

- **Word-scoped** (a new-word approval) — yes/no:
  ```powershell
  iba\app\ps\Escalation.ps1 -Action Answer -Word hypocrisy -Decision Yes    # or: No
  ```
- **Run-scoped** (a config proposal, or any quality-check finding) — three-way:
  ```powershell
  iba\app\ps\Escalation.ps1 -Action AnswerRun -RunId <run_id> -Decision Approve|Reject|Revise [-Comment "..."]
  ```

Then **re-run the same command** — it resumes where it paused and finishes:

```powershell
iba\app\ps\New-Word.ps1 -Word hypocrisy -Source "gap scan 2026-07-18"
#   registry.create   ok   'hypocrisy' already approved — proceeding
#   raw.discover … raw.validate   ok
#   COMPLETE — raw layer built for 'hypocrisy'.
```

The pause is durable — you can answer and resume minutes or a restart later.

**When the app suspects a duplicate**, the question changes to a confirmation — for example if the
word maps to Strong's already held by an existing word:

```text
#   #2 [envy] at registry.create —
#   'envy' shares ALL 3 strongs with existing word 'jealousy'. Register it as a SEPARATE word anyway?
```

Answering `No` stops it (it was a duplicate/typo); `Yes` registers it as a distinct word.

**Adding your OWN item** (something you noticed, not raised by a running step):

```powershell
iba\app\ps\Escalation.ps1 -Action Raise -Question "Revisit the anger/spirit dual-characteristic overlap in candidate_seed"
# prints a synthetic run_id — answer it later with -Action AnswerRun same as any other
```

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

## 6. The word report

```powershell
iba\app\ps\Reports.ps1 -Step ReportWord -Word hypocrisy      # -> iba/app/report-hypocrisy.md
```

It shows, per word: the **validation** results, the **strongs and their meaning**, and **sample
verses** with the verse text and every word's span (Strong's + morphology), each backtracking to
its sense. Every row is checkable against STEP — the `getInfo` / `masterSearch` URLs are in the
report header.

**The database** (`iba/app/db/iba.db`) holds the data directly — browse it with any SQLite tool, or
dump every table to CSV for a narrative-free look (§12).

---

## 7. What the reports show is configurable

Report content is config, not code — every toggle is a `cfg_setting` row, changed the sanctioned
way (§9), never by hand-editing a JSON seed:

| setting | effect |
|---|---|
| `report.sample_verses` | how many sample verses the word report shows |
| `report.show_verse_text` | show the verse text above its spans |
| `report.show_validation` | show the validation table |
| `report.span_fields` / `report.strong_fields` | which columns the span/strong tables show |
| `validation.show_health` / `show_delta` / `show_integrity` / `show_references` / `show_expectations` | word-report validation sections |
| `validation.show_health` / `show_candidate` / `show_passages` | book-report validation sections |

---

## 8. Building the base layer — candidates and passages

Two work packages, run **per book** (OSIS code, e.g. `Gen`, `Rom`, `Ps`), on top of an already-built
word (§3):

```powershell
iba\app\ps\Set-Candidates.ps1 -Book Gen
#   candidate.seed   ok   refreshes candidate_seed globally (not just this book) over lemma_inventory
#   candidate.set    ok   stamps span_candidate on this book's spans whose base-strong is a candidate

iba\app\ps\Build-Passages.ps1 -Book Gen
#   passage.build    ok   recomputes this book's passages from span_candidate
```

`candidate.seed` is **global** — every run re-syncs the whole candidate list against the curated
`cfg_candidate_rule` accept/reject/synonym rules (§10), even though you passed one book; `Book` is
just what triggers it. `candidate.set`/`passage.build` are book-scoped and **fully re-derive** that
book's stamps/passages from scratch each run (delete-then-rebuild), so re-running is always safe.

`Build-Passages.ps1` accepts `-Rule char-continuity|maximal` to override
`passage.default_rule` for one run.

---

## 9. Configuration maintenance — the only way to change a `cfg_*` row

**Never hand-edit a JSON seed or the DB directly.** Every config change — a setting, an enum value,
a candidate accept/reject rule, anything in a `cfg_*` table — goes through one gate:

```powershell
iba\app\ps\Config-Maintenance.ps1 -Step Validate
#   read-only coherence check: schema FKs, may_source, handlers resolve, on_fail paths, orphan
#   configs, settings needing justification — safe to run any time

iba\app\ps\Config-Maintenance.ps1 -Step Propose -Table cfg_setting -Op update `
    -Where '{"key":"passage.review_over"}' -Set '{"value":"12"}' `
    -Question "Raise passage.review_over from 10 to 12 — fewer long passages flagged needs_review."
#   PAUSED, run_id printed
iba\app\ps\Escalation.ps1 -Action AnswerRun -RunId <run_id> -Decision Approve
iba\app\ps\Config-Maintenance.ps1 -Step Propose -RunId <run_id> -Table cfg_setting -Op update `
    -Where '{"key":"passage.review_over"}' -Set '{"value":"12"}'
#   applied

iba\app\ps\Config-Maintenance.ps1 -Step Report
#   regenerates iba/app/config/CONFIG-REPORT.md — every cfg_* table, current, human-readable
```

`-Op insert|update|delete` on any `cfg_*` table. Coherence-checked before you ever see it (unknown
table/column, bad enum, invalid JSON, a new `cfg_setting` missing its `module`); only **Approve**
commits the write, logged row-by-row in `cfg_change_detail`. Full mechanism: `GOVERNANCE.md` §3A/§9A.

---

## 10. Candidate curation — correcting and adding to `candidate_seed`

`candidate_seed` (the base-layer candidate assessment) is a **data** table, not a `cfg_*` one, so
`Config-Maintenance.ps1` can't touch it — it has its own utility, `Candidate-Curate.ps1`, in two
modes.

### 10a. `-Mode Curate` (default) — correct/split/delete ONE existing row

```powershell
# correct a wrong tag:
iba\app\ps\Candidate-Curate.ps1 -LemmaKey H8085 -Field tag -Value "hearing" `
    -Question "Replace the raw dual-gloss 'to hear: hear' with a clean IB label."
#   PAUSED, run_id printed
iba\app\ps\Escalation.ps1 -Action AnswerRun -RunId <run_id> -Decision Approve
iba\app\ps\Candidate-Curate.ps1 -RunId <run_id> -LemmaKey H8085 -Field tag -Value "hearing"
#   applied

# reject a lemma (soft, reversible):
iba\app\ps\Candidate-Curate.ps1 -LemmaKey H2000 -Field decision -Value rejected -Question "..."

# split a base lemma into a per-sub-strong concept row:
iba\app\ps\Candidate-Curate.ps1 -LemmaKey H0639 -StrongVariant H0639G -Field split -Value "anger" `
    -Question "H0639 covers face/nose/anger across sub-strongs -- split H0639G off as 'anger'."

# remove an invalid row entirely (soft-delete):
iba\app\ps\Candidate-Curate.ps1 -LemmaKey G0112 -Field delete -Question "No tag, no registry_match."
```

`-Field` is `tag | decision | split | delete`. `-StrongVariant` targets a specific sub-lettered
strong (omit to target the base row); **required** for `split`. Single-row, approval-gated, same
shape as `Config-Maintenance.ps1 -Step Propose`. `Field=tag|decision|delete` needs the row to
already exist; adding a brand-new candidate LEMMA (not in `candidate_seed` at all) is still the
`cfg_candidate_rule` `accept` route via `Config-Maintenance.ps1` + a `Set-Candidates.ps1` re-run.
Full method: `iba/docs/iba-candidate-seed-curation-method-v1-20260721.md`.

### 10b. `-Mode Load` (added 2026-07-22) — batch add from a JSON file, no approval gate on clean items

The bulk, JSON-driven counterpart. You supply plain **English words**, not Strong's codes — the
tool derives the lemma/Strong's itself:

```powershell
iba\app\ps\Candidate-Curate.ps1 -Mode Load -InputFile iba\app\config\my-batch.json
```

where the file is:

```json
{
  "items": [
    { "word": "hearing", "reason": "gap scan 2026-07-22 — H8085 shama covers both senses" },
    { "word": "joy/gladness", "reason": "split on delimiter into two attempts" }
  ]
}
```

- A **clean, genuinely new** word **auto-loads immediately — no approval pause.** (This is the one
  place in the app that behaves like `candidate.seed`'s bulk net-matching, not like the
  approval-gated pattern everywhere else — a deliberate choice for a batch tool, not an oversight.)
- A **duplicate** (already an active `candidate_seed` row) is skipped **untouched** — nothing
  written, nothing changed on the existing row.
- Anything else (special characters, a sentence, a bare transliteration, no lemma/Strong's match,
  or a mismatch against STEP's own gloss) is written as an inspectable
  `candidate_seed` row with `decision='exception'` — query it directly, or read
  `iba/app/reports/candidate-load.md`.
- A word containing `:` or `/` is split into separate concepts up front (each tried independently,
  each its own row via the new `sense_seq` column if it doesn't map to a distinct sub-strong).
- **Omit `-InputFile`** (or pass an empty `items` list) to just **revalidate the whole existing
  seed** — no new items, re-derives `step_status`/`ib_referent_type` for every row and re-flags any
  now-broken tag.
- **One escalation for the whole run**, only if unresolved `decision='exception'` rows remain
  afterward:
  ```powershell
  iba\app\ps\Escalation.ps1 -Action AnswerRun -RunId <run_id> -Decision Approve
  #   acknowledges the exceptions as a known worklist; it does NOT fix them — that's still 10a.
  ```

Full design: the plan approved 2026-07-22 (`melodic-foraging-bunny`); build + a real incident
(and its fix) found while testing this same feature: `GOVERNANCE.md` §12.

---

## 11. Standalone quality checks

Read-only pictures of data health, run **whenever you want them** — not tied to any build step, so
they don't add noise to every `Set-Candidates`/`Build-Passages` run:

```powershell
iba\app\ps\Candidate-Quality.ps1
#   -> iba/app/reports/candidate-quality.md — span_candidate/candidate_seed/lemma_inventory
#      tag & gloss null/format quality, lemma_key -> strong resolution

iba\app\ps\Passage-Quality.ps1
#   -> iba/app/reports/passage-quality.md — verse-count distribution across every passage
```

Both escalate (one run, one escalation, counts + samples) if they find anything — acknowledging the
escalation (`Escalation.ps1 -Action AnswerRun ... -Decision Approve`) confirms you've seen the
picture; it doesn't fix anything. Actual fixes go through §10.

---

## 12. Reports and raw CSV export

```powershell
iba\app\ps\Reports.ps1 -Step ReportWord -Word hypocrisy          # word-raw report (§6)
iba\app\ps\Reports.ps1 -Step ValidationWord -Word hypocrisy      # raw-layer validation report
iba\app\ps\Reports.ps1 -Step ValidationBook -Book Gen            # base-layer validation report

iba\app\ps\Export-Tables.ps1                                     # every table -> iba/app/export/*.csv
iba\app\ps\Export-Tables.ps1 -Table candidate_seed,run           # just these tables
iba\app\ps\Export-Tables.ps1 -Out some\other\dir
```

`Export-Tables.ps1` dumps tables **verbatim** — no report narrative, no interpretation — for direct
review in a spreadsheet, or as a point-in-time reference (this is exactly how a same-morning
`candidate_seed.csv` export made a real recovery possible on 2026-07-22 — see `GOVERNANCE.md` §12).

---

## 13. Log retention (read-only)

```powershell
iba\app\ps\Log-Retention.ps1
#   -> iba/app/reports/log-retention.md
```

Row counts and age for `run`/`escalation`/`validation_result`, every open escalation, recent real
failures, and a "stuck chained runs" section (runs that paused mid-sequence and were never
resumed) listed as archival **candidates** for you to judge — it does not prune or delete anything.

---

## 14. Everyday commands, in order

```powershell
# once, at the start of a session:
iba\app\ps\Start-Iba.ps1

# for each new word:
iba\app\ps\New-Word.ps1 -Word <word> -Source "<why>"
#   if it pauses:
iba\app\ps\Escalation.ps1 -Action Answer -Word <word> -Decision Yes
iba\app\ps\New-Word.ps1 -Word <word> -Source "<why>"     # resume

# base layer, per book:
iba\app\ps\Set-Candidates.ps1 -Book <book>
iba\app\ps\Build-Passages.ps1 -Book <book>

# add/correct candidates:
iba\app\ps\Candidate-Curate.ps1 -Mode Load -InputFile <batch.json>     # batch, from outside the app
iba\app\ps\Candidate-Curate.ps1 -LemmaKey <k> -Field tag -Value <v> -Question "..."  # one row

# see what's open, answer it:
iba\app\ps\Escalation.ps1 -Action List
iba\app\ps\Escalation.ps1 -Action AnswerRun -RunId <id> -Decision Approve|Reject|Revise

# read it:
iba\app\ps\Reports.ps1 -Step ReportWord -Word <word>

# check on data/config health, any time:
iba\app\ps\Candidate-Quality.ps1
iba\app\ps\Passage-Quality.ps1
iba\app\ps\Config-Maintenance.ps1 -Step Validate
iba\app\ps\Log-Retention.ps1

# remove a test word (dry-run, then --yes):
python -m iba.app.tools.purge_word --word <word>

# start clean (drops data, keeps config):
iba\app\ps\Start-Iba.ps1 -Reset

# see every config the code reads, live:
iba\app\ps\New-Word.ps1 -Word <word> -Source "<why>" -Trace
```

---

## 15. Migrations (one-off setup)

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
strongs already in the app. Run it once; `candidate.seed`/`candidate.load` keep the seed current
thereafter.

---

## 16. Where things are

```text
iba/app/
  config/     schema/step/run/rules JSON seeds (archived — DB is master) · CONFIG-REPORT.md (generated)
  db/iba.db   the database (config tables cfg_* + the data)
  db/snapshots/  pre-run DB snapshots (added 2026-07-22) — every new run copies iba.db here first
  ps/         Start-Iba.ps1 · New-Word.ps1 · Set-Candidates.ps1 · Build-Passages.ps1 ·
              Config-Maintenance.ps1 · Candidate-Curate.ps1 · Candidate-Quality.ps1 ·
              Passage-Quality.ps1 · Reports.ps1 · Export-Tables.ps1 · Escalation.ps1 · Log-Retention.ps1
  init.py     the bootstrap (Start-Iba calls it)
  lib/        cfg (read) · cfgload+cfgcheck (load+validate) · cfgreport · cfgquality · valuequality ·
              dbsnapshot · db · stepapi · escalation · words
  handlers/   registry · raw · configmaint · candidate · passage · reports   (interpreters, no hard rules)
  migration/  one-off: Import-LegacyRegistry.ps1 · legacy_import · import_seed · several bootstrap/
              schema-addition scripts (see GOVERNANCE.md for the full list)
  tools/      purge_word · export_tables_csv · log_retention
  run.py            the dispatcher
  report.py · validation.py   the output + validation reports
  BUILD.md          what's built, how the parts fit
  GOVERNANCE.md     how config governs the code
  UTILITIES.md      the utilities around the run
  USER-GUIDE.md     this file
```

For the raw model (term → sense → span) and the data-layer design, see
`iba/docs/stream-registry-word-buildout-v7/v8` and `iba/docs/raw-config-design-v1`.
