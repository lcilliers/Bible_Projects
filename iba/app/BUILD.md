# The IBA app — raw slice · build record

> **2026-07-17.** The first working vertical slice of the IBA application: PowerShell, Python,
> config, DB, output and controls, fitting together. It registers a new word and builds its **raw
> layer** from STEP into a new database, and it runs end to end.
>
> **This is the thing to evaluate.** Against the blueprint in
> `iba/docs/stream-registry-word-buildout-v7/v8`. Run it (§2), read the tables (§4), check the
> decisions I made without asking (§6).

---

## 1. What it is, and how the parts fit

```
  PowerShell            iba/app/ps/New-Word.ps1      the ORCHESTRATOR — owns no process logic
     │  loads the sequence from ▼
  config                iba/app/config/run.json      the work package: the ordered steps
     │  calls, once per step ▼
  Python dispatcher     iba/app/run.py               the run-state machine (resumable)
     │  dispatches to ▼
  handlers              iba/app/handlers/…           registry.exists/create · raw.discover/detail/
     │                                                verses/write/validate
     │  which use ▼
  lib                   iba/app/lib/stepapi.py       the 3 STEP calls + the span parse
                        iba/app/lib/db.py            the DB, built FROM config/schema.json
     │  writing ▼
  database              iba/app/db/iba.db            the new IBA DB (SQLite)
     │  read by ▼
  output                iba/app/report.py            a markdown report of a word's raw layer
```

**The config drives everything.** `schema.json` defines every table and column (with its `use`,
`expectation`, and the STEP field that feeds it) — the DB is generated from it, and a handler
cannot write a column it does not declare. `run.json` defines the step order — PowerShell reads it,
it is not in the script. `step.json` defines the three API routes and what each may source.

**PowerShell orchestrates; Python works.** This is the locked design decision (PS is the framework,
calls Python). PS loops the sequence and branches on each step's exit code (`0` ok · `2` paused ·
`3` stop). It contains no knowledge of what a step does.

---

## 2. Run it

```powershell
# a clean slice, one word, end to end:
iba\app\ps\New-Word.ps1 -Word hypocrisy -Source "gap scan" -Fresh

# a second word into the same DB (proves global dedup):
iba\app\ps\New-Word.ps1 -Word gratitude -Source "build test"

# the report:
python -m iba.app.report --word hypocrisy      # -> iba/app/report-hypocrisy.md
```

`-Fresh` rebuilds the DB from `schema.json` first. Without it, the run adds to the existing DB.

---

## 3. What one run does (the blueprint, executing)

| step | call | → tables | proven |
|---|---|---|---|
| `registry.exists` | — | reads `word_registry` | stops if the word exists |
| `registry.create` | — | `word_registry` | status → approved |
| `raw.discover` | CALL 1 `meanings=` | `word_strong` | the seed strongs; **relatedNos not followed** |
| `raw.detail` | CALL 2 `getInfo` | `strong` · `strong_sense` · `strong_meaning_tree` · `strong_lexicon` | **the meaning, normalised** (O4) |
| `raw.verses` | CALL 3 `strong=` | `strong_verse` · `verse` · `span` | span = a **parse** of preview; no morphology call |
| `raw.write` | — | commit | word → raw-complete |
| `raw.validate` | — | the parse-check | `span` recovers `strong_verse`, per strong |

---

## 4. What is in the DB (measured, `hypocrisy` + `gratitude`)

| table | rows | is |
|---|---|---|
| `word_registry` | 2 | the words |
| `word_strong` | 7 | L1 — (word, strong) links |
| `strong` | 7 | L2 — identity, one per strong, global |
| `strong_sense` | 7 | the **head** = the span's meaning |
| `strong_meaning_tree` | — | the lemma's tree, keyed on the lemma |
| `strong_lexicon` | 5 | LSJ/Mounce |
| `verse` | ~177 | unique verses |
| `strong_verse` | ~179 | the m:m index |
| `span` | ~2,670 | one row per **code** of a verse |
| `run` | 2 | the control records, distinct ids |

**Checks that passed (not asserted — run against STEP):**

- **Completeness.** Every strong's stored verse count equals STEP's reported total — `G5485`
  146/146 after the forward-walk fix (§5). No silent under-return.
- **The verse does not belong to a strong.** `Gal.2.13` returned by both `G5272` and `G4942` →
  **one `verse` row, two `strong_verse` rows.**
- **One row per code.** Matt 23:28 → 15 `span` rows; "appear" splits into `G3303`+`G5316` at two
  positions; particles (`H9002` "and") are their own rows.
- **The parse-check.** `span` (what we parsed) recovers `strong_verse` (what STEP asserted), for
  every strong. 0 missed.
- **The meaning is where analytics can read it.** `strong_sense.head` = 'hypocrisy' for `G5272` —
  the sense, one field, not the ESV surface word the old `D101` stored.

---

## 5. Bugs the BUILD surfaced (that the design docs did not)

This is why building was the right call — two real defects, found by running:

1. **The forward-walk under-returned by 39 verses.** `G5485` stored 107 of 146. Cause: the frontier
   sort keyed on the book *name*, and book order is not alphabetical ("Gen" before "Exod"). Fixed
   with the canonical OSIS index. **This is the exact silent-under-return class the whole programme
   fears** — and it was invisible until a real high-frequency word ran.
2. **run_id collision.** Two runs in the same second shared an id; the second ran under the first's
   record. Fixed with millisecond precision.

Both are now verified fixed (§4 completeness; §4 run rows).

---

## 6. Decisions I made without asking (evaluate these)

Per your instruction — build autonomously, document the calls:

| # | decision | why |
|---|---|---|
| D1 | **FKs declared but not hard-enforced** | the raw model legitimately records a reference before its referent: `word_strong` lists seed strongs before `detail` fetches them, and `span` names every code in a verse including strongs this word does not hold. Enforcing FKs would reject both. They stand as documentation + join paths. |
| D2 | **the handler contract** (open B2) | `def h(ctx) -> Result`. `ctx` = the open Db + run + word + params. `Result` = an `on_fail` path + message + counts. Small on purpose — the run only needs the path. |
| D3 | **the tree is written once per lemma** | the prototype proved a lemma's senses share one tree; `strong_meaning_tree` is keyed on `lemma_key` and skipped if present. |
| D4 | **the approval escalation is stubbed to auto-approve** | `util.escalation` is not built this slice. `registry.create` marks the seam in a comment and approves directly so the slice completes. The pause/resume machinery (run.state, escalation table) IS built and used by `raw.discover`'s zero-strongs path. |
| D5 | **`language` from the code prefix** | H→Hebrew, G→Greek. Aramaic is invisible here (known limitation); the span's true language is `morph_code`, which is stored. |
| D6 | **the run is resumable via persisted state** | `run.state`/`resume_point` in the DB, per O7. A `pause-continue` writes an escalation, marks paused, and stops; re-running resumes (idempotent via dedup). Exercised by the zero-strongs path, not yet by a real mid-run pause. |

---

## 7. What this slice does NOT do (deliberately out of scope)

- **base / cluster / analytics** — `span_analysis` (the derived overlay) is designed in the schema
  docs but not a table here; this slice is raw only.
- **the real approval + escalation UI** — stubbed (D4). The tables and the pause/resume path exist.
- **the meaning tree parsing is shallow for Greek** — the Greek `mediumDef` is prose with `<ref>`
  tags, not a numbered tree, so it lands as one node. Hebrew numbered trees parse into nodes. Good
  enough for raw; the sense **head** (what analytics reads) is exact either way.
- **reconciliation with the heavyweight `iba/config` configurator** — this app uses its own
  lightweight runtime config. Whether the two configs converge is a later decision.

---

## 8. Files

```
iba/app/
  config/  schema.json · step.json · run.json        the runtime config
  lib/     db.py · stepapi.py                          DB (from schema) · STEP
  handlers/ base.py · registry.py · raw.py            the step handlers
  run.py                                               the dispatcher + run-state machine
  ps/New-Word.ps1                                      the orchestrator
  report.py                                            the output
  db/iba.db                                            the new IBA database (built)
  report-hypocrisy.md                                  a sample output
  BUILD.md                                             this file
```
