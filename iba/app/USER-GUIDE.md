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
> 2026-07-30.** Live today: the raw layer (**new-word**, §3; **raw-backfill**, §3a), **config
> maintenance** (§9), **standalone quality checks** (§11), **the lexicon-parsed layer** (§11a),
> **reports and CSV export** (§12), **log retention** (§13), **4 analysis reports** —
> strong-meaning, span-analysis, schema-overview, registry (§12a), and **verse-analysis /
> passage-debate / whole-book-read / narrative-check** (§12b/§12c) — the live method for building a
> book's study content. **§8's candidate-stamping-and-passages pipeline
> (`Set-Candidates.ps1`/`Build-Passages.ps1`), §10's candidate curation (`Candidate-Curate.ps1`),
> `Candidate-Quality.ps1`, and `SeedCandidate-Report.ps1` are all RETIRED** (2026-07-23/26) — do not
> run them; §12b/§12c is the current method. Every report auto-archives its previous version and
> pairs with a CSV export by default (§12). The interpretive stages above this layer (lexical,
> characteristics, findings) are not built yet. Where this guide describes a command or a report, it
> describes what exists now. Companion docs: `BUILD.md` (what's
> built, how the parts fit) and `GOVERNANCE.md` (how config governs the code) — this guide is *how
> to run it*.

---

## 1. The environment — what the app needs

| requirement | detail |
|---|---|
| **Python 3.14** | with one package: `requests`. Install: `python -m pip install requests` |
| **the local STEP server** | running at `http://localhost:8989` with the tagged module `ESV_th`. The app never uses the web. |
| **nothing else, for everything except §12d** | **no `.env`, no secrets, no keys.** STEP is local and takes no key. The connection is in the config, not the environment. §12d's narrative generator is the one exception — it reads `ANTHROPIC_API_KEY` from the environment or the repo-root `.env` (added 2026-07-30; same key `scripts/_run_ve_reads_governed.py` at the repo root already uses, not a new provision). |

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
  ✓ config loaded (904 rows in 20 cfg_* tables)
    config_version: app-0.1.0
  ✓ data tables present (18)
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

Start (or restart) the STEP server and run `Start-Iba.ps1` again. Runs refuse to start without STEP
— governed by `cfg_setting step.required_for_runs` (`true`, approved 2026-07-26 — see
`GOVERNANCE.md` §16), not just this sentence; `init.py`'s exit code and every STEP-dependent tool
read that one row rather than each hardcoding the rule separately.

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

## 3a. Backfilling meaning for supporting terms (`Raw-Backfill.ps1`)

`New-Word.ps1` only pulls `strong`/`strong_sense`/etc. for the strongs a *registered* word maps to.
A verse full of spans references many OTHER strongs too — words never onboarded as their own study
term but still needed to read the verse. `Raw-Backfill.ps1` pulls meaning **only** (never verses)
for every strong a book's (or one chapter/verse-range's) spans reference that has no `strong` row
yet — progressive, passage-driven coverage, not a full-Bible bulk pull:

```powershell
iba\app\ps\Raw-Backfill.ps1 -Book Dan                # whole book
iba\app\ps\Raw-Backfill.ps1 -Book Dan -Range 1:1-7   # just this chapter:verse-verse range
```

Self-contained: the lexicon-parsed layer (§11a) and `relatedNos` fetch for the newly-pulled strongs
happen automatically as part of this run — no separate `Lexicon-Parse.ps1` call needed afterward.
You will rarely need to run this by hand — `report.verse_span_meaning` (§12b) auto-backfills the
exact range it's about to render before writing the report (`report.auto_backfill_before_render`),
so this is here for when you want the pull done ahead of time, or on its own.

---

## 4. Escalations — the complete reference

**This is the one, complete place for how escalations work.** Every other section that mentions
`Escalation.ps1` (§9, §10a, §10b, §11, §13, §14) is just that section's own moment of using it —
come back here for the mechanism itself, rather than piecing it together from those examples.

### 4.1 What an escalation is

The **one** mechanism the app uses to pause and ask you something. Every pause — whatever raised
it — becomes exactly one row in the `escalation` table. `Escalation.ps1` (added 2026-07-21) is the
**one** front door for it; every other governed operation had a PS wrapper from the start, answering
never did until then.

### 4.2 The three shapes

| shape | raised by | scope | answered with |
|---|---|---|---|
| **word-scoped** | `registry.create` (a genuinely new word, or a suspected duplicate) | one word | yes/no |
| **run-scoped** | a real dispatcher pause — a `configmaint.propose` change, or a quality-check finding (`candidate.validate`/`passage.validate`/`configmaint.validate`) | one run | approve / reject / revise |
| **manual** | **you**, via `-Action Raise` — not raised by any running step | a synthetic run_id | approve / reject / revise |

Manual escalations answer through the exact same `AnswerRun` path as a real run-scoped one — there
is no separate mechanism to learn. This is also how this session's "flag it now, fix it later"
backlog workflow works: raising an item doesn't fix anything by itself, it just records it.

### 4.3 The state a row moves through

Today: **`raised`** (open, unanswered) → **`answered`** (you gave a decision; `answer` holds
approve/reject/revise, `comment` optional unless revise). That is the whole lifecycle that exists
right now — there is currently no way to edit an already-raised question's wording, pause one aside
without answering it, or withdraw one without it counting as a decision. See the proposal below
(§4.6) if you want those.

### 4.4 The four actions that exist today

```powershell
# see what's open — writes escalation.list_report_path (default iba/app/reports/escalation-list.md,
# archived on regenerate) and prints a one-line pointer + count (fixed 2026-07-23; used to dump the
# full list to the terminal only):
iba\app\ps\Escalation.ps1 -Action List

# answer a WORD-scoped one:
iba\app\ps\Escalation.ps1 -Action Answer -Word hypocrisy -Decision Yes    # or: No

# answer a RUN-scoped one (config proposal, quality-check finding, or your own manual item):
iba\app\ps\Escalation.ps1 -Action AnswerRun -RunId <run_id> -Decision Approve|Reject|Revise [-Comment "..."]

# raise your OWN item — not raised by a running step:
iba\app\ps\Escalation.ps1 -Action Raise -Question "<exactly what you want recorded>"
# prints a synthetic run_id — answer it later with -Action AnswerRun same as any other
```

`-Action Raise`'s `-Question` text is stored **verbatim** — it does not get reworded or have
analysis folded into it. That is deliberate: what you write is the record.

### 4.5 Resuming after answering a REAL (non-manual) pause

A word- or run-scoped pause from an actual dispatcher run is durable — answer it any time, even
after a restart — then **re-run the exact same command** that paused; it resumes where it stopped:

```powershell
iba\app\ps\New-Word.ps1 -Word hypocrisy -Source "gap scan 2026-07-18"
#   registry.create   ok   'hypocrisy' already approved — proceeding
#   raw.discover … raw.validate   ok
#   COMPLETE — raw layer built for 'hypocrisy'.
```

A **manual** item (§4.2) has no underlying run to resume — answering it just closes the record; if
it named a fix, the fix is done separately (by hand, or by asking Claude), not by re-running
anything.

**Duplicate-word suspicion** is the same word-scoped mechanism with a different question — if a new
word maps to Strong's already held by an existing word:

```text
#   #2 [envy] at registry.create —
#   'envy' shares ALL 3 strongs with existing word 'jealousy'. Register it as a SEPARATE word anyway?
```

`No` stops it (it was a duplicate/typo); `Yes` registers it as a distinct word.

### 4.6 Editing, pausing, and retracting a MANUAL item (added 2026-07-23)

Built for the "escalation as a backlog of work for Claude" workflow — a manual item (§4.2) is
often a work instruction, not only a design decision awaiting approval, so it needs a bit more
lifecycle than raised → answered. **Restricted to `MANUAL-`-prefixed run_ids only** — a real
dispatcher-tied escalation (a config proposal, a quality-check finding) must still go through
`AnswerRun`; pausing one of those risks a duplicate escalation on the next run (the dispatcher's own
resume logic keys on `state='raised'`/`'answered'` specifically).

```powershell
# replace the wording on a still-open item (old wording preserved in the row's history, not lost):
iba\app\ps\Escalation.ps1 -Action Edit -RunId MANUAL-... -Question "corrected instruction..."

# set one aside without answering it — still shown in -Action List, flagged, excluded from the
# active queue:
iba\app\ps\Escalation.ps1 -Action Pause -RunId MANUAL-... -Comment "why it's on hold"

# bring it back into the active queue:
iba\app\ps\Escalation.ps1 -Action Resume -RunId MANUAL-...

# withdraw it — "never mind", NOT a reviewed decision (distinguishable in the record from an
# actual approve/reject/revise):
iba\app\ps\Escalation.ps1 -Action Retract -RunId MANUAL-... -Comment "why it's withdrawn"
```

`-Action List`'s output now shows `raised` and `paused` items together (paused ones flagged), with
a state column; `answered`/`retracted` items drop off the open list, same as before, but remain in
the `escalation` table (and its own row's `answer`/`comment` fields) for audit — an `answer` of
approve/reject/revise means a real decision was made; `retracted` means it was withdrawn instead.

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

## 8. Building the base layer — candidates and passages — RETIRED, corrected 2026-07-29

**This whole pipeline is retired and must not be run.** `Set-Candidates.ps1`
(`candidate.seed`/`candidate.set`) was retracted 2026-07-23 (`GOVERNANCE.md` §15D);
`Build-Passages.ps1` (`passage.build`) was retired 2026-07-26 (`GOVERNANCE.md` §17/`BUILD.md`
§23) — *"the past use, and rules have moved on... there is nothing to migrate from the old to the
new"* (the researcher's own words). Both work packages are `inactive=1` in `cfg_work_package`
today. This section previously showed them as the live way to build a book's passages — stale
since 2026-07-26, found and corrected in the same 2026-07-29 audit that produced
`PLAN-config-system-remediation-v1-20260729.md`.

**Nothing today derives a passage's boundaries algorithmically.** A passage is now whatever range
`report.verse_span_meaning`/`report.passage_debate` is run over — a judgement call per debate, per
the reading method — tracked (not generated) by `lib/passagetrack.py`. **See §12b below** for the
current method: `VerseSpanMeaning-Report.ps1` then `PassageDebate-Report.ps1`.

`candidate_seed`/`span_candidate` remain in the DB (retracted data kept for provenance, not
purged — same as `passage`/`verse_passage`'s own retirement, §17) but nothing writes to them or
reads them for any live workflow.

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

## 10. Candidate curation — correcting and adding to `candidate_seed` — RETIRED, corrected 2026-07-30

**This work package is retired and must not be run.** `Candidate-Curate.ps1`'s work package
(`candidate-curation`) is `inactive=1` — retired alongside the rest of the candidate system
(`GOVERNANCE.md` §15D, 2026-07-23; `candidate_seed`/`span_candidate` themselves kept in the DB for
provenance, nothing writes to them or reads them for any live workflow, same as §8's passage
tables). This section previously showed it as the live way to correct/add candidate rows — stale
since 2026-07-23, found and corrected in the same 2026-07-30 pass that added §3a/§11a/§12c. The
commands below are kept as a record of what this utility did; running any of them is now refused by
the dispatcher (`cfg_work_package.inactive`).

`candidate_seed` (the base-layer candidate assessment) is a **data** table, not a `cfg_*` one, so
`Config-Maintenance.ps1` can't touch it — it had its own utility, `Candidate-Curate.ps1`, in two
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

Read-only pictures of data health, run **whenever you want them** — not tied to any build step:

```powershell
iba\app\ps\Passage-Quality.ps1                 # corpus-wide raw distribution
iba\app\ps\Passage-Quality.ps1 -Book Dan       # book-scoped: sanity-check that book's debate-range
                                                # sizes (§12b) instead — added 2026-07-28
#   -> iba/app/reports/passage-quality.md — verse-count distribution
```

Escalates (one run, one escalation, counts + samples) if it finds anything — acknowledging the
escalation (`Escalation.ps1 -Action AnswerRun ... -Decision Approve`) confirms you've seen the
picture; it doesn't fix anything.

**`Candidate-Quality.ps1` is retired**, corrected here 2026-07-30 — this section used to list it
alongside `Passage-Quality.ps1` as a normal, currently-usable command. Its work package
(`candidate-quality`) is `inactive=1` (retired with the rest of the candidate system, §8) — running
it is now refused outright by the dispatcher (`cfg_work_package.inactive`), not just pointless.

---

## 11a. The lexicon-parsed layer (`Lexicon-Parse.ps1`)

Not read-only like the checks above — `-Step Parse`/`-Step Related` actually write. Three
independent steps (run whichever you need, not a fixed pipeline):

```powershell
iba\app\ps\Lexicon-Parse.ps1 -Step Parse      # strong_meaning_tree/strong_lexicon -> the 3 parsed
                                               # tables. No network, deterministic, clears+rebuilds,
                                               # safe to re-run any time.
iba\app\ps\Lexicon-Parse.ps1 -Step Related    # strong -> strong_related, one live STEP getInfo
                                               # call per row. Can take a couple of minutes over the
                                               # full strong table.
iba\app\ps\Lexicon-Parse.ps1 -Step Validate   # read-only coverage + value-quality check across all
                                               # 4 tables -> iba/app/reports/lexicon-parse.md;
                                               # escalates once if it finds anything, same shape as
                                               # §11's checks.
```

**You will rarely need to run `Parse`/`Related` by hand.** `Raw-Backfill.ps1` (§3a) and
`New-Word.ps1`'s own raw-detail step both rebuild this layer automatically for whatever strongs
they just pulled — this script exists for a manual full rebuild/check, not as a required step in
the everyday flow.

---

## 12. Reports and raw CSV export

```powershell
iba\app\ps\Reports.ps1 -Step ReportWord -Word hypocrisy          # word-raw report (§6)
iba\app\ps\Reports.ps1 -Step ValidationWord -Word hypocrisy      # raw-layer validation report
iba\app\ps\Reports.ps1 -Step ValidationBook -Book Gen            # base-layer validation report

iba\app\ps\Export-Tables.ps1                                     # every DATA table -> iba/app/export/*.csv
iba\app\ps\Export-Tables.ps1 -Table candidate_seed,run           # just these tables
iba\app\ps\Export-Tables.ps1 -Out some\other\dir
```

`Export-Tables.ps1` (now the registered `table-export`/`table.export` step) dumps tables
**verbatim** — no report narrative, no interpretation — for direct review in a spreadsheet, or as a
point-in-time reference (this is exactly how a same-morning `candidate_seed.csv` export made a real
recovery possible on 2026-07-22 — see `GOVERNANCE.md` §12). It excludes `cfg_*` tables —
`Config-Maintenance.ps1 -Step Report` (§9) is the dedicated config snapshot/export.

**Every report now auto-archives and CSV-pairs by default (added 2026-07-22/23).** Every report in
this guide (§6, this section, §11, §13, §12a below) — when it regenerates — first copies its
*previous* version into an `archive/` subfolder beside it (timestamped), so a run never silently
overwrites the last snapshot; and it writes a matching CSV of its underlying table(s) into an
`export/` subfolder (git-ignored), so you get both the narrative analysis and the raw rows on every
run, no extra command needed. `schema-overview` (§12a) is the one exception — it already *is* the
schema, a CSV of it would just repeat the same information.

---

## 12a. The 4 analysis reports (added 2026-07-22/23; registry report added 2026-07-23; was 5, corrected 2026-07-30)

Read-only, run whenever you want them — same standalone shape as the quality checks (§11), each its
own work package. **`SeedCandidate-Report.ps1` is retired** (`seed-candidate-report` work package,
`inactive=1`) — it reports on `candidate_seed`, itself retired data (§10); running it is now refused
by the dispatcher. The remaining 4:

```powershell
iba\app\ps\StrongMeaning-Report.ps1
#   -> iba/app/reports/strong-meaning.md — meaning-parse coverage: strong rows with no strong_sense
#      yet, sense-count distribution, lsj/mounce lexicon completeness

iba\app\ps\SpanAnalysis-Report.ps1
#   -> iba/app/reports/span-analysis.md — span coverage per book, confirmed vs candidate span
#      counts, morph-code distribution

iba\app\ps\SchemaOverview-Report.ps1
#   -> iba/app/reports/schema-overview.md — every data table: columns, types, PK/FK, indexes, row
#      counts, introspected live (no CSV pairing — see above)

iba\app\ps\Registry-Report.ps1
#   -> iba/app/reports/registry.md — evaluate/review word_registry: summary (by status/source),
#      joined to strong via word_strong, and a sense report grouping registry words by the
#      gloss/broad meaning their strong carries
```

Full design + content rationale (first 4): `PLAN-reports-config-governance-v1-20260722.md` §3.1–3.4;
build account: `GOVERNANCE.md` §14. Registry report: escalation #272, `GOVERNANCE.md` §15A.

---

## 12b. Verse-analysis: lexical, then the debate pipeline (rewritten 2026-08-07 — supersedes the scaffold-based version of this section)

**This section replaces the scaffold-based workflow entirely.** The old two steps documented here
(`VerseSpanMeaning-Report.ps1` → `PassageDebate-Report.ps1`, added 2026-07-26/27) are both fully
retired — `report.verse_span_meaning` since `BUILD.md` §56-59 (2026-08-05, superseded by
`report.verse_lexical`/`lexical.build`), `report.passage_debate`/`Chapter-Generate.ps1`/
`passage-debate-sync` since 2026-08-07 (superseded by the DB-first `hib`/`phenomenon`/`operation`/
`closing` model, which is what the real Dan 8 debate actually used — `BUILD.md` §61-71). Leaving
both routes live side by side was a confirmed, live-hit source of confusion (a half-migrated
pipeline pointing at itself) — this rewrite is the fix, not a parallel option.

**The real pipeline, two separate tools:**

1. **The lexical** (`lexical.build`/`report.verse_lexical`, `VerseLexical.ps1`) — mechanical,
   deterministic, no analytical judgement. Book-scoped, run once ahead of time — independent of
   how many small debate chapters follow, since a debate is always chapter/range-scoped while the
   lexical is naturally a whole-book pass.
2. **The debate** (`Debate-Run.ps1`) — the single entry point for everything from HIB
   identification through the rendered report, for one chapter/range at a time.

### Step 1 — build the lexical for the whole book (once, ahead of time)

```powershell
iba\app\ps\VerseLexical.ps1 -Book Dan -Chapters 1-12
#   -> iba/app/verse-analysis/Daniel/dan-1-12-verse-lexical-v{n}-{date}.md
# -Range 8:1-27 also works for a sub-chapter slice, but the normal case is the WHOLE book at once.
```

`hib.set` (below) hard-refuses (`lexical-incomplete`) against any verse this hasn't covered yet —
build it first, for the whole book, and you won't hit that per-chapter.

### Step 2 — run the debate, one chapter/range at a time

```powershell
# single chapter
iba\app\ps\Debate-Run.ps1 -Book Dan -Chapters 1

# multi-chapter range
iba\app\ps\Debate-Run.ps1 -Book Dan -Chapters 1-3

# sub-chapter verse range
iba\app\ps\Debate-Run.ps1 -Book Dan -Range 8:1-27

# targeted single-step rerun/correction (mirrors the real Dan 8 rollback/redo, BUILD.md §71)
iba\app\ps\Debate-Run.ps1 -Book Dan -Chapters 1 -Step hib.set
```

One call walks the whole sequence (`cfg_setting.passage.debate_run_sequence` — `hib.set` →
`passage.build` → `phenomenon.set` → `operation.set` → `closing.set`), each step still under its
own existing work package. **Per-step separation is unchanged and load-bearing** — each step still
needs its own genuinely-authored analytical content (the digest's "failure modes," `BUILD.md`
§61-71); what's gone is only the need to invoke five separate scripts by hand in a fixed order.

For each step, in order, the script:

1. **Checks if it's already done** for this exact scope (a DB read, mirroring that step's own
   gate) — if so, skips it silently.
2. **Looks for a staging payload** at a predictable path (`cfg_setting.
   passage.debate_staging_path_pattern`: `iba/app/staging/operations/{book}-{scope}-{step}.json`)
   — if present, runs the step with it.
3. **Otherwise stops**, printing the exact path expected. That payload is authored by whoever does
   that step's actual reading (the AI, in-session, from the lexical + prior DB state) — it is
   never something typed by hand at this command line. Once it exists, **rerun the exact same
   command** — readiness is re-derived from the DB and the staging files every time, no `-RunId`
   bookkeeping needed to resume.

Example of a stop, and what happens next:

```text
PS> iba\app\ps\Debate-Run.ps1 -Book Dan -Chapters 1

  hib.set              skip           already satisfied for this scope     <- example only;
                                                                                first run always
                                                                                stops at hib.set

STOPPED -- hib.set needs its analytical payload next.
  Write it to: iba\app\staging\operations\dan-1-hib.set.json
  Then rerun the exact same command -- readiness is re-derived from the DB
  and staging files each time, no run-id bookkeeping needed to resume.
```

Once `closing.set` succeeds, `Debate-Run.ps1` automatically renders the report
(`python -m iba.app.tools.build_debate_report`, standalone — deliberately not a `cfg_report` step,
`BUILD.md` §65) to `iba/app/reports/{book}-{scope}-debate-report-{date}.md`.

**Known gap, not yet updated for this model:** `WholeBookRead-Report.ps1`/`report.whole_book_read`
(`BUILD.md` §32) still reads the old scaffold's `debate_status='filled'` .md sections
(Emergent-questions/Passage-level-linkages) — it has not been rebuilt against the new
`passage_emergent_question`/`passage_linkage` DB tables. Still correct for the six pre-existing
scaffold-model books (Amos/Hosea/Joel/Jonah/Micah/Obadiah); not yet exercised against a
`Debate-Run.ps1`-produced book.

**New failure conditions (2026-08-07, `BUILD.md` §79 — full-app schema remediation).** A correction
payload for `hib.set`/`phenomenon.set`/`operation.set` naming an item under `remove` can now stop
with `hib-has-dependent-phenomena` / `phenomenon-has-dependent-operations` /
`operation-has-dependent-linkage` — the removal is refused because live analytical work is already
built on top of it. Not a bug: clear the dependent first (remove the phenomenon/operation/linkage
that depends on it, via that step's own `remove` list), or withdraw the item from `remove` and leave
it in place. A `changed` correction (same label/key, different content) no longer needs this —
corrections update the existing DB row in place now, they never orphan anything downstream.

`operation.set`'s `sources`/`targets` party objects also gained an optional `hib_label` field —
set it when a source/target genuinely IS a HIB already registered via `hib.set` (structurally links
`operation_party.hib_id`, not just the free-text `detail` gloss); omit it for a party that isn't its
own registered HIB. An unresolvable `hib_label` fails the call the same way an unresolvable verse or
HIB label already does.

---

## 12c. Inner-being narrative — structural check (`BookNarrative-Validate.ps1`, added 2026-07-30)

Narrative writing itself is unmechanised analytical work (no pipeline produces it) — this is a
read-only check you run **on a finished narrative file**, before treating it as done. Confirms a
`## Scope self-check` section exists and cites all three required channels (non-human↔human,
human↔human, physical world↔human — see `WA-inner-being-narrative-guidance-v1-2026-07-28.md` §4)
with non-empty content. A presence check only — it does not judge whether the narrative's content or
citations are actually good.

```powershell
iba\app\ps\BookNarrative-Validate.ps1 -Path iba\app\verse-analysis\Daniel\WA-dan-inner-being-narrative-v3-consolidated-2026-07-28.md
#   -> iba/app/reports/book-narrative-scope-check.md
```

Fails (`scope-check-missing`/`scope-check-incomplete`) if the section is absent or any channel is
missing/empty — the message names exactly which.

---

## 12d. Generating the narrative itself (`BookNarrative-Generate.ps1`, added 2026-07-30)

Everything above through §12c gathers material and checks structure; this step is the one that
actually **writes** the narrative, by calling the Anthropic Messages API — the first place in this
app that costs real, pay-as-you-go money rather than running on the Claude Code subscription or a
free local STEP call.

```powershell
iba\app\ps\BookNarrative-Generate.ps1 -Book Dan -BookLabel Daniel
```

Requires at least one filled `report.passage_debate` for the book (§12b) and `ANTHROPIC_API_KEY` in
the environment or the repo-root `.env` (see §1 — the one exception to this app's "no secrets"
rule; the same key `scripts/_run_ve_reads_governed.py` at the repo root already uses). It assembles
every filled debate for the book plus the two governing docs — `method.narrative_hard_constraints_
path` (the book-agnostic hard constraints: nothing invented, open threads stay open, no forced
unity, plain language, no self-reference — generalized from the original Daniel-only brief) and
`method.inner_being_narrative_guidance_path` (the three-channel requirement + the `## Scope
self-check` section, §12c) — resolves both live from `cfg_setting`, not memory, then **estimates**
the token count/cost before ever calling the network.

- Over `narrative.generate_max_cost` (default $3.00): refused outright (`cost-cap-exceeded`) — raise
  the cap deliberately via `configmaint.propose` for a book large enough to need it, don't just
  re-run.
- Under the cap: **pauses** (`needs-approval`) with the exact estimate in the question — same
  approval shape as `registry.create`/`configmaint.propose`, nothing spent yet:

  ```powershell
  iba\app\ps\Escalation.ps1 -Action AnswerRun -RunId <run_id> -Decision Approve
  iba\app\ps\BookNarrative-Generate.ps1 -Book Dan -BookLabel Daniel -RunId <run_id>   # resume — makes the live call
  ```

Once approved and resumed, ONE live API call is made, the result is filed under `report.verse_
analysis_output_dir/<BookLabel>/` (`narrative.output_pattern`, archived-on-regenerate like every
other report), and the call's real token/cost (from the API response itself, not the estimate) is
appended to `narrative.usage_log_path` — `scripts/cost_ledger.py` at the repo root only ingests
Console CSV exports, not this app's own calls, so this is the audit trail for those. Run
`BookNarrative-Validate.ps1` (§12c) on the result next.

Every one of these is a `cfg_setting` (module `narrative`), changeable via `configmaint.propose`,
never hard-coded: `narrative.generate_model` (default `claude-sonnet-5`), `narrative.generate_max_
output_tokens`, `narrative.generate_max_cost`, `narrative.rate_input_per_million`/`rate_output_per_
million`, `narrative.output_pattern`, `narrative.usage_log_path`. The `cfg_report` row for
`report.book_narrative_generate` governs the title/footer the same way every other report's does.

**What this doesn't do.** The actual writing is still not mechanized by this app's own code — the
model does the writing, working strictly from the assembled package; this step's job is making sure
that package is complete and consistent every time, not judging what the narrative should say.

**Proven live** on Daniel ($1.19, 328,276 in / 13,711 out tokens) and Joel ($0.35, 86,420 in / 5,740
out tokens), both 2026-07-30 — both passed `report.book_narrative_validate` clean.

**Flagged, not built: a cross-book mechanism.** A single book's narrative holds together on its own,
but nothing yet pulls information ACROSS books — recurring or varying themes and focal points. The
researcher is confident this can be drawn from the same debate corpus this step already reads, but
the shape of that data is not yet decided — nothing here should be read as a design for it. See
`BUILD.md` §52's closing note when that direction is given.

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

**Corrected 2026-07-30** — this list used to show the retired `Set-Candidates.ps1`/
`Build-Passages.ps1`/`Candidate-Curate.ps1` as the normal per-book workflow, contradicting §8/§10's
own RETIRED markings. Replaced with the current verse-analysis/passage-debate method (§12b/§12c),
and the 4 previously-undocumented scripts (§3a/§11a/§12b/§12c) added.

```powershell
# once, at the start of a session:
iba\app\ps\Start-Iba.ps1

# for each new word:
iba\app\ps\New-Word.ps1 -Word <word> -Source "<why>"
#   if it pauses:
iba\app\ps\Escalation.ps1 -Action Answer -Word <word> -Decision Yes
iba\app\ps\New-Word.ps1 -Word <word> -Source "<why>"     # resume

# fill in supporting-term meaning for a book/range, if you want it done ahead of time (§3a):
iba\app\ps\Raw-Backfill.ps1 -Book <book> [-Range <ch:v-v>]

# the current per-book study method — extract, then debate, then whole-book read (§12b):
iba\app\ps\VerseSpanMeaning-Report.ps1 -Book <book> -Chapters <n-n> -BookLabel <Label>
iba\app\ps\PassageDebate-Report.ps1 -Book <book> -Chapters <n-n> -BookLabel <Label>
#   ... fill in the debate's <!-- fill in --> placeholders, repeat per range, then:
iba\app\ps\WholeBookRead-Report.ps1 -Book <book> -BookLabel <Label>

# generate the narrative itself — real API cost, approval-gated (§12d):
iba\app\ps\BookNarrative-Generate.ps1 -Book <book> -BookLabel <Label>

# structural check on a finished inner-being narrative (§12c):
iba\app\ps\BookNarrative-Validate.ps1 -Path <narrative file>

# see what's open, answer it:
iba\app\ps\Escalation.ps1 -Action List
iba\app\ps\Escalation.ps1 -Action AnswerRun -RunId <id> -Decision Approve|Reject|Revise

# read it:
iba\app\ps\Reports.ps1 -Step ReportWord -Word <word>

# check on data/config health, any time:
iba\app\ps\Passage-Quality.ps1 [-Book <book>]
iba\app\ps\Lexicon-Parse.ps1 -Step Validate
iba\app\ps\Config-Maintenance.ps1 -Step Validate
iba\app\ps\Log-Retention.ps1

# the 4 analysis reports, any time (§12a):
iba\app\ps\StrongMeaning-Report.ps1
iba\app\ps\SpanAnalysis-Report.ps1
iba\app\ps\SchemaOverview-Report.ps1
iba\app\ps\Registry-Report.ps1

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

**Migrate the candidate seed** — historical record only, corrected 2026-07-30: this loaded the
independent candidate-characteristic seed that the now-retired `Set-Candidates.ps1`/§10 pipeline
depended on (§8/§10). Not part of the current method (§12b/§12c) and not needed for it.

```powershell
python -m iba.app.migration.import_seed
```

It imports the lemma inventory + candidate assessment from the old study and maps it against the
strongs already in the app.

---

## 16. Where things are

```text
iba/app/
  config/     schema/step/run/rules JSON seeds (archived — DB is master) · CONFIG-REPORT.md (generated,
              incl. a per-report governance rollup) · archive/ + export/ (auto-archived snapshots /
              CSV pairing for CONFIG-REPORT.md itself)
  db/iba.db   the database (config tables cfg_* + the data)
  db/snapshots/  pre-run DB snapshots (added 2026-07-22) — every new run copies iba.db here first
  ps/         Start-Iba.ps1 · New-Word.ps1 · Set-Candidates.ps1 · Build-Passages.ps1 ·
              Config-Maintenance.ps1 · Candidate-Curate.ps1 · Candidate-Quality.ps1 ·
              Passage-Quality.ps1 · Reports.ps1 · Export-Tables.ps1 · Escalation.ps1 ·
              Log-Retention.ps1 · SeedCandidate-Report.ps1 · StrongMeaning-Report.ps1 ·
              SpanAnalysis-Report.ps1 · SchemaOverview-Report.ps1 · Registry-Report.ps1 ·
              VerseSpanMeaning-Report.ps1 · PassageDebate-Report.ps1 · WholeBookRead-Report.ps1 ·
              BookNarrative-Generate.ps1 (§12d — real API cost) · BookNarrative-Validate.ps1 ·
              create-iba-view-template.ps1 · create-passage-view-and-export.ps1 ·
              create-passages-by-book-view-and-export.ps1 · export-iba-config-tables.ps1 ·
              generate-iba-db-schema-report.ps1 (5 standalone investigation utilities, relocated
              here from iba\scripts\ 2026-07-23) ·
              _lib/Notify.ps1 (shared terminal wording, not run directly)
  init.py     the bootstrap (Start-Iba calls it)
  lib/        cfg (read) · cfgload+cfgcheck (load+validate) · cfgreport · cfgquality · valuequality ·
              dbsnapshot · db · stepapi · escalation · words · reportkit (shared report rendering +
              archiving, incl. CSV writes + CSV pairing + one-off naming) · seedreport ·
              strongreport · spanreport · schemareport · registryreport (the 5 analysis reports,
              §12a) · passagetrack · passagedebatereport · wholebookread · versespanmeaningreport
              (§12b) · narrativegenerate (§12d — assembly + Anthropic Messages API call + filing)
  handlers/   registry · raw · configmaint · candidate · passage · reports   (interpreters, no hard rules)
  migration/  one-off: Import-LegacyRegistry.ps1 · legacy_import · import_seed · ~20 further
              bootstrap/schema-addition scripts (see GOVERNANCE.md §7 for the full current list)
  tools/      purge_word · export_tables_csv · log_retention · _apply_verse_plaintext_column ·
              build_span_heatmap_v1 (2 relocated from iba\scripts\ 2026-07-23)
  run.py            the dispatcher
  report.py · validation.py   the two original output + validation reports
  reports/    every generated report (candidate-quality.md, seed-candidate.md, registry.md, ...) ·
              archive/ (auto-archived prior versions, incl. CSVs) · export/ (per-report CSV AND
              table-export's dump, consolidated into one folder 2026-07-23 — git-ignored)
  archive/    non-report historical files (new 2026-07-23) — e.g. a superseded pre-restructure
              New-Word.ps1 stub found outside iba/app/
  BUILD.md          what's built, how the parts fit
  GOVERNANCE.md     how config governs the code
  UTILITIES.md      the utilities around the run
  USER-GUIDE.md     this file
  PLAN-reports-config-governance-v1-20260722.md   the reports-config-governance design + build log
```

For the raw model (term → sense → span) and the data-layer design, see
`iba/docs/stream-registry-word-buildout-v7/v8` and `iba/docs/raw-config-design-v1`.
