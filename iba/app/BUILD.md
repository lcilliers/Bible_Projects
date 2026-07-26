# The IBA app — build record

> **2026-07-17, first slice.** The first working vertical slice of the IBA application:
> PowerShell, Python, config, DB, output and controls, fitting together. It registers a new word
> and builds its **raw layer** from STEP into a new database, and it runs end to end. §1–§7 below
> describe that slice as built that day (§7 has 2026-07-22 corrections where later work changed
> what was true).
>
> **Grown since (2026-07-21/22, see §3A and GOVERNANCE.md §9A–§10 for the full history).** Six
> more work packages now exist beyond `new-word`: `set-candidates`/`build-passages` (the base
> layer — candidate stamping + reading-frame passages), `configuration-maintenance` (the sole path
> to change a `cfg_*` row), `candidate-quality`/`passage-quality` (standalone data-quality checks),
> `candidate-curation` (ongoing seed correction), and `reports` (word/book reporting, registered).
> **Read this file for what's built and how; read `GOVERNANCE.md` for how config governs it;
> read `USER-GUIDE.md` to actually run it.**
>
> Originally evaluated against the blueprint in `iba/docs/stream-registry-word-buildout-v7/v8`.
> Run it (§2), read the tables (§4), check the decisions I made without asking (§6).

---

## 1. What it is, and how the parts fit

**This diagram is `new-word`'s shape specifically** (the first work package built) — the other six
(§3A) plug into the exact same chain, swapping only the handler module and lib functions used;
the generic, work-package-agnostic version of this chain is GOVERNANCE.md §3. Note also: the
config it "loads from" is the **DB** (`cfg_step`, `cfg_setting`, ...), not the JSON files named
below — the JSON is the archived seed, the DB is master (GOVERNANCE.md §10). This diagram is kept
in its original 2026-07-17 phrasing (the JSON was still the live source that day) rather than
silently rewritten, since the distinction — seed vs. runtime store — is itself worth seeing.

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
(As of 2026-07-21 these are read from the live `cfg_*` tables the JSON was loaded into, not the
JSON files themselves on every run — see GOVERNANCE.md §1.)

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

**Full run-command list (per work package — kept current here, not only in GOVERNANCE.md §5A):**

| script | does |
|---|---|
| `iba\app\ps\Start-Iba.ps1 [-Reload] [-Reset]` | session bootstrap: config load, data tables, STEP pre-flight |
| `iba\app\ps\New-Word.ps1 -Word <w> -Source <s> [-Fresh]` | the `new-word` work package |
| `iba\app\ps\Set-Candidates.ps1 -Book <b>` | the `set-candidates` work package |
| `iba\app\ps\Build-Passages.ps1 -Book <b>` | the `build-passages` work package |
| `iba\app\ps\Config-Maintenance.ps1 -Step Validate` | coherence-check the live `cfg_*` tables (read-only) |
| `iba\app\ps\Config-Maintenance.ps1 -Step Propose -Table .. -Op .. [-Where ..] [-Set ..] -Question ..` | the ONLY sanctioned path to change a `cfg_*` row — approval-gated, see GOVERNANCE.md §5A |
| `iba\app\ps\Config-Maintenance.ps1 -Step Report` | regenerate `iba/app/config/CONFIG-REPORT.md` |
| `iba\app\ps\Candidate-Quality.ps1 [-RunId <id>]` | standalone quality check: `span_candidate`/`candidate_seed`/`lemma_inventory` tag/gloss/lemma_key — one generic value-quality engine (`lib/valuequality.py`), escalates if findings, not tied to `set-candidates` |
| `iba\app\ps\Candidate-Curate.ps1 -LemmaKey <k> -Field tag\|decision\|split\|delete [-StrongVariant <v>] -Value <v> [-Question ..]` | `-Mode Curate` (default): the ongoing `candidate_seed` correct/split/remove utility — single-row, approval-gated (see `iba/docs/iba-candidate-seed-curation-method-v1-20260721.md`) |
| `iba\app\ps\Candidate-Curate.ps1 -Mode Load [-InputFile <batch.json>]` | JSON-batch create/update/validate (added 2026-07-22) — clean items auto-load, duplicates skip untouched, everything else becomes an inspectable `decision='exception'` row; omit `-InputFile` to just revalidate the existing seed. See §3A and GOVERNANCE.md §12 |
| `iba\app\ps\Passage-Quality.ps1 [-RunId <id>]` | standalone quality check: passage verse-count distribution — escalates if findings, not tied to `build-passages` |
| `iba\app\ps\Reports.ps1 -Step ReportWord -Word <w>` | the word-raw report (`report.py`) |
| `iba\app\ps\Reports.ps1 -Step ValidationWord -Word <w>` | the raw-layer validation report (`validation.py`) |
| `iba\app\ps\Reports.ps1 -Step ValidationBook -Book <b>` | the base-layer validation report (`validation.py`) |
| `iba\app\ps\Export-Tables.ps1 [-Out <dir>] [-Table t1,t2,...]` | `table-export`/`table.export` (registered 2026-07-22/23) — dump every DATA table (or a subset) to CSV, one file per table, verbatim, excluding `cfg_*` (that's `configmaint.report`'s job); direct DB visibility for review, no report narrative in the way; default `iba/app/export/` |
| `iba\app\ps\Escalation.ps1 -Action List` | write every open escalation to `escalation.list_report_path` (default `iba/app/reports/escalation-list.md`, archived on regenerate) — fixed 2026-07-23, used to dump the full list to the terminal only |
| `iba\app\ps\Escalation.ps1 -Action Answer -Word <w> -Decision Yes\|No` | answer a new-word approval |
| `iba\app\ps\Escalation.ps1 -Action AnswerRun -RunId <id> -Decision Approve\|Reject\|Revise [-Comment ..]` | answer a config-proposal or quality-check escalation |
| `iba\app\ps\Escalation.ps1 -Action Raise -Question ".."` | add your OWN item to the escalation table — a researcher-initiated flag, not raised by a running step |
| `iba\app\ps\Log-Retention.ps1` | `log-retention`/`retention.report` (registered 2026-07-22/23) — run/escalation/validation_result log-retention & run-health report (read-only — no pruning) |
| `iba\app\ps\SeedCandidate-Report.ps1` | whole-`candidate_seed` analysis (decision/layer/role, tag/lemma distribution, busiest lemmas, open-vs-resolved over time) — added 2026-07-22/23, see GOVERNANCE.md §14 |
| `iba\app\ps\StrongMeaning-Report.ps1` | meaning-parse layer coverage (`strong`/`strong_sense`/`strong_meaning_tree`/`strong_lexicon` gap list, sense-count distribution, lexicon completeness) |
| `iba\app\ps\SpanAnalysis-Report.ps1` | span-layer coverage per book, confirmed vs candidate span counts, morph-code distribution |
| `iba\app\ps\SchemaOverview-Report.ps1` | the app's own data-schema snapshot — every data table, columns, types, PK/FK, indexes, row counts, introspected live |
| `iba\app\ps\Registry-Report.ps1` | evaluate/review `word_registry` — summary (by status/source), joined to `strong` via `word_strong`, sense report grouping registry words by gloss/broad meaning — added 2026-07-23, escalation #272, see GOVERNANCE.md §15A |

`-Fresh` rebuilds the DB from `schema.json` first. Without it, the run adds to the existing DB.

---

## 3. What one run does (the blueprint, executing)

| step | call | → tables | proven |
|---|---|---|---|
| `registry.exists` | — | reads `word_registry` | stops if the word exists |
| `registry.create` | — | `word_registry` | status → approved (**real escalation**, yes/no — see §6) |
| `raw.discover` | CALL 1 `meanings=` | `word_strong` | the seed strongs; **relatedNos not followed** |
| `raw.detail` | CALL 2 `getInfo` | `strong` · `strong_sense` · `strong_meaning_tree` · `strong_lexicon` | **the meaning, normalised** (O4) |
| `raw.verses` | CALL 3 `strong=` | `strong_verse` · `verse` · `span` | span = a **parse** of preview; no morphology call |
| `raw.write` | — | commit | word → raw-complete |
| `raw.validate` | — | the parse-check | `span` recovers `strong_verse`, per strong |

---

## 3A. What the other work packages do (added since the raw slice — this section was missing until 2026-07-22)

The raw slice (§3) was the first work package built; six more exist now, each its own registered
`cfg_work_package` (source of truth: `iba/app/config/CONFIG-REPORT.md` §4, regenerated from the
live `cfg_step` rows — reproduced here so a reader doesn't have to cross two documents for "what
does a run actually do").

**`set-candidates`** — runs over `book` · `iba\app\ps\Set-Candidates.ps1 -Book <b>`

| # | step | handler | → tables | does |
|---|---|---|---|---|
| 0 | `candidate.seed` | `candidate:seed` | `candidate_seed`, `lemma_inventory` | refresh the candidate seed over the independent lemma inventory (registry-direct + curated-synonym + ib-judgement nets); recompute `registry_match` (the double control) |
| 1 | `candidate.set` | `candidate:set` | `span_candidate` | stamp the book's spans whose base-strong is a live candidate |

**`build-passages`** — runs over `book` · `iba\app\ps\Build-Passages.ps1 -Book <b>`

| # | step | handler | → tables | does |
|---|---|---|---|---|
| 0 | `passage.build` | `passage:build` | `passage`, `verse_passage` | recompute the book's passages from `span_candidate` (rule = `char-continuity` or `maximal`); flag any run longer than `passage.review_over` (10) `needs_review` |

**`configuration-maintenance`** — runs over `none` · `iba\app\ps\Config-Maintenance.ps1 -Step <s>`
(the mechanism is GOVERNANCE.md §3A/§9A; this is just its step table)

| # | step | handler | does |
|---|---|---|---|
| 0 | `configmaint.validate` | `configmaint:validate` | read-only coherence check of the live `cfg_*` tables — no approval needed |
| 1 | `configmaint.propose` | `configmaint:propose` | the only path that may change a `cfg_*` row — approval-gated (escalation, 3-way) |
| 2 | `configmaint.report` | `configmaint:report` | regenerate `CONFIG-REPORT.md` from the live `cfg_*` tables |

**`candidate-quality`** — runs over `none` · `iba\app\ps\Candidate-Quality.ps1`

| # | step | handler | → report | does |
|---|---|---|---|---|
| 0 | `candidate.validate` | `candidate:validate` | `iba/app/reports/candidate-quality.md` | `candidate_tag`/`tag`/`gloss` null-or-format quality + `lemma_key`→`strong` resolution — one escalation per invocation, standalone (not part of `set-candidates`) |

**`passage-quality`** — runs over `none` · `iba\app\ps\Passage-Quality.ps1`

| # | step | handler | → report | does |
|---|---|---|---|---|
| 0 | `passage.validate` | `passage:validate` | `iba/app/reports/passage-quality.md` | verse-count distribution across every passage — one escalation per invocation, standalone (not part of `build-passages`) |

**`candidate-curation`** — runs over `none` · `iba\app\ps\Candidate-Curate.ps1`

| # | step | handler | does |
|---|---|---|---|
| 0 | `candidate.curate` | `candidate:curate` | single-row, approval-gated correction on `candidate_seed` (tag/decision/split/delete) — the ongoing utility `configmaint.propose` cannot provide, since that path is restricted to `cfg_*` tables |
| 1 | `candidate.load` (added 2026-07-22) | `candidate:load` | JSON-batch create/update/validate — `Candidate-Curate.ps1 -Mode Load -InputFile <path.json>`. Input is `{"word","reason"}` only, no `lemma_key` — the handler derives the lemma/`strong_variant` itself (exact-tag match first, then word-boundary gloss match, preferring a sub-lettered variant's own gloss over the collapsed base). A clean item **auto-loads, no approval gate** (follows `seed()`'s bulk-apply precedent, not `curate()`'s per-row gate); a duplicate is skipped **untouched** (no row written, no existing row touched); anything else (format failure, no match, gloss mismatch) is written as an inspectable `decision='exception'` row. Then revalidates the whole existing seed the same way. **One** escalation total, only if exception rows remain unresolved. Full design: `iba/docs` plan "melodic-foraging-bunny" (approved 2026-07-22); build/incident account: GOVERNANCE.md §12. |

**`reports`** — runs over `word` or `book` (per step) · `iba\app\ps\Reports.ps1 -Step <s>`

| # | step | handler | scope | does |
|---|---|---|---|---|
| 0 | `report.word` | `reports:word_report` | word | the word-raw report (`report.py`), content governed by `report.*` settings |
| 1 | `validation.word` | `reports:validation_word` | word | the raw-layer validation report (`validation.py`), sections governed by `validation.show_*` |
| 2 | `validation.book` | `reports:validation_book` | book | the base-layer validation report (`validation.py`), same toggles |

**`log-retention`** — runs over `none` · `iba\app\ps\Log-Retention.ps1` (registered 2026-07-22/23,
GOVERNANCE.md §13 — was a standalone script calling `tools.log_retention` directly, outside the
dispatcher, until this session)

| # | step | handler | → report | does |
|---|---|---|---|---|
| 0 | `retention.report` | `reports:retention_report` | `iba/app/reports/log-retention.md` | `run`/`escalation`/`validation_result` row counts + age, stuck chained runs, open escalations, recent failures — read-only, no pruning |

**`table-export`** — runs over `none` · `iba\app\ps\Export-Tables.ps1 [-Out <dir>] [-Table t1,t2,...]`
(registered 2026-07-22/23, same session — was also standalone before)

| # | step | handler | does |
|---|---|---|---|
| 0 | `table.export` | `reports:table_export` | CSV dump of every DATA table, verbatim, one file per table — **excludes `cfg_*`** (fixed 2026-07-22/23: it used to dump those too, duplicating `configmaint.report`). `-Out`/`-Table` are plain PS parameters (destination/subset override), not config — a parameter explained in the script's own inline help isn't a setting just because the script is dispatcher-registered. |

**`seed-candidate-report`** / **`strong-meaning-report`** / **`span-analysis-report`** /
**`schema-overview-report`** — each runs over `none`, single step, its own PS script (added
2026-07-22/23, GOVERNANCE.md §14) — the 4 "missing reports" from
`PLAN-reports-config-governance-v1-20260722.md` §3.1–3.4, built entirely on `lib/reportkit.py`
(never hardcoded first, unlike the original 8):

| work package | step | handler | does |
|---|---|---|---|
| `seed-candidate-report` | `report.seed_candidate` | `reports:seed_candidate_report` | whole-`candidate_seed` analysis |
| `strong-meaning-report` | `report.strong_meaning` | `reports:strong_meaning_report` | meaning-parse layer coverage |
| `span-analysis-report` | `report.span_analysis` | `reports:span_analysis_report` | span-layer coverage per book |
| `schema-overview-report` | `report.schema_overview` | `reports:schema_overview_report` | the app's own data-schema snapshot |

**`registry-report`** — runs over `none` · `iba\app\ps\Registry-Report.ps1` (added 2026-07-23,
escalation #272 — the registry had no evaluation report)

| # | step | handler | does |
|---|---|---|---|
| 0 | `report.registry` | `reports:registry_report` | evaluate/review `word_registry`: summary (by status/source), joined to `strong` via `word_strong`, sense report grouping registry words by gloss/broad meaning |

---

## 4. What is in the DB (measured, `hypocrisy` + `gratitude`, 2026-07-17)

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

**Current scale, measured live 2026-07-22** (added — the table above is a 2-word snapshot from
day one; grown far beyond it since via the legacy-registry migration + set-candidates/build-passages
runs across many books):

| table | rows | table | rows |
|---|---|---|---|
| `word_registry` | 178 | `lemma_inventory` | 11,781 |
| `strong` | 3,463 | `candidate_seed` | 2,087 |
| `verse` | 29,037 | `span_candidate` | 87,922 |
| `strong_verse` | 112,446 | `passage` | 18,571 |
| `span` | 534,075 | `verse_passage` | 24,847 |
| `run` | 779 | `escalation` | 232 |

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

## 7. What this slice does NOT do (deliberately out of scope) — CORRECTED 2026-07-22

**This section describes the 2026-07-17 raw slice only.** Base-layer work (candidate + passage,
§3A) was built afterward and is real, not "not done" — corrected below so this section doesn't
read as still true of the whole app:

- ~~base / cluster / analytics — not a table here; this slice is raw only~~ **base-layer IS built**:
  `candidate_seed`/`span_candidate` (the candidate stamp, §3A `set-candidates`) and
  `passage`/`verse_passage` (the reading-frame layer, §3A `build-passages`) both exist and run.
  What remains genuinely out of scope is the **interpretive** layer above base — cluster/
  characteristics/lexical/findings (VE-lexical) — no table for any of those exists yet.
- **the real approval + escalation UI** — the pause/resume machinery, the `escalation` table, and a
  genuine yes/no approval on `registry.create` all exist and run (§6 in GOVERNANCE.md corrects the
  old "stubbed to auto-approve" claim). What's still a stub is only the **answer shape** for word
  approval — yes/no, not yet the three-way approve/reject/revise every other escalation in this app
  uses (`configmaint.propose`, `candidate.curate`, the quality checks).
- **the meaning tree parsing is shallow for Greek** — unchanged: the Greek `mediumDef` is prose with
  `<ref>` tags, not a numbered tree, so it lands as one node. Hebrew numbered trees parse into
  nodes. The sense **head** (what analytics reads) is exact either way.
- **reconciliation with the heavyweight `iba/config` configurator** — still unresolved. This app
  runs its own lightweight `cfg_*` config; `iba/config/*.json` is a separate, more elaborate,
  **not-yet-loadable** design (no loader, nothing reads it — confirmed live, `_manifest.json.status`
  says so explicitly). Whether/how the two converge is not decided — see GOVERNANCE.md §6 and
  `iba/docs/iba-app-design-precedence-and-structure-v1-20260721.md` §2 item 5.
- **still genuinely not built, checked directly 2026-07-22:** `source`/`filled_by` enforcement
  (declared in `cfg_column`, not checked against actual values); hard technical enforcement that
  *only* `configmaint.propose` may write a `cfg_*` row (it's the sanctioned path by convention, not
  by permission); a check that `BUILD.md`/`GOVERNANCE.md` actually stay current (the two
  `governance.*` settings proposed today, GOVERNANCE.md §8, state the rule but nothing enforces it
  yet).

---

## 8. Files — CORRECTED 2026-07-23, script-folder consolidation (escalation #271, same day)

Was frozen at 2026-07-22's state; §9/§10's own text had already moved past it — `dbsnapshot.py`,
`reportkit.py`, the 4 new report modules, `Notify.ps1` and the new migrations were named in prose
below but missing from this tree. **Extended again the same day**: 7 standalone investigation/
utility scripts previously scattered outside `iba/app/` (2 in `iba\scripts\`'s Python side, 5 in its
PowerShell side — view-creation, schema-report, and a one-off column-migration script, all of which
already targeted `iba/app/db/iba.db`) were relocated into `iba/app/tools/`/`iba/app/ps/`; a stale,
pre-restructure duplicate `iba\ps\New-Word.ps1` (a STUB referencing the old `iba/config/utility/
run.json` design, superseded by the real `iba/app/ps/New-Word.ps1`) was archived to
`iba/app/archive/`, and both now-empty folders (`iba\ps\` entirely; the 7 relocated files' entries
in `iba\scripts\`) were removed. The canonical folders are now real config (`cfg_setting
governance.scripts_ps_dir` = `iba/app/ps`, `governance.scripts_python_dir` = `iba/app/tools`), not
just convention.

**`iba\scripts\` still holds 5 files deliberately NOT moved** — they belong to genuinely different
systems, confirmed by reading each file, not by folder name alone: `cfg_apply.py`/`cfg_helper.py`/
`cfg_kernel.py`/`probe_step_api.py` are the OTHER, separate `iba/config` heavyweight configurator's
own maintenance utilities (GOVERNANCE.md §6 — a different, not-yet-reconciled system from this app);
`build_dbschema.py` is the main Bible-study programme's schema tool (root `CLAUDE.md` §3, operates
on `bible_research.db`, not `iba.db`). Moving these would have been scope creep past what the
folder name implies — the actual owning system, not the folder, decides where a script belongs.

```
iba/app/
  config/     schema/step/run/rules JSON seeds (archived — DB is master, GOVERNANCE.md §10) ·
              CONFIG-REPORT.md (generated snapshot, never hand-edited, incl. §12 per-report rollup) ·
              archive/ (auto-archived prior snapshots) · export/ (cfg_* CSV pairing — git-ignored)
  lib/        cfg.py (the runtime reader) · cfgload.py (seed -> cfg_* on load) · cfgcheck.py ·
              cfgreport.py · cfgquality.py (orphan/justification/report-path/report-governance
              checks) · valuequality.py (the value-quality engine) · retention.py · dbsnapshot.py
              (pre-run rollback snapshots) · db.py (schema from cfg_column) · stepapi.py (STEP,
              governed by cfg) · escalation.py (the one researcher interaction) · words.py
              (normalise) · reportkit.py (shared report scaffold + archive-on-write, incl. CSV
              writes since escalation #273 + CSV pairing + one-off report naming) · seedreport.py ·
              strongreport.py · spanreport.py · schemareport.py (the 4 new reports, §3A) ·
              registryreport.py (registry evaluation report, escalation #272)
  handlers/   base.py (Ctx/Outcome/ok/fail/escalate) · registry.py · raw.py · configmaint.py ·
              candidate.py · passage.py · reports.py
  migration/  Import-LegacyRegistry.ps1 · legacy_import.py · import_seed.py · allocate_strongs.py ·
              apply_semantic_allocation.py · build_base_all_books.py ·
              bootstrap_configuration_maintenance.py · bootstrap_setting_module_column.py ·
              bootstrap_quality_validate_steps.py · bootstrap_reports_registration.py ·
              bootstrap_report_persistence_governance.py · add_work_package_chained_column.py ·
              add_candidate_seed_strong_variant.py · add_candidate_seed_referent_columns.py ·
              fix_stuck_run_states.py · delete_blank_tag_candidates.py · repair_strong_sense_head.py ·
              bootstrap_report_content_governance.py · bootstrap_retention_table_export_registration.py ·
              bootstrap_new_reports_phase1.py · bootstrap_oneoff_report_naming.py   (all one-off, idempotent)
  tools/      purge_word.py · export_tables_csv.py (archive-on-write, escalation #273) ·
              log_retention.py · _apply_verse_plaintext_column.py (relocated from iba\scripts\,
              escalation #271) · build_span_heatmap_v1.py (ditto)
  ps/         Start-Iba.ps1 (session bootstrap) · New-Word.ps1 · Set-Candidates.ps1 ·
              Build-Passages.ps1 · Config-Maintenance.ps1 · Candidate-Curate.ps1 ·
              Candidate-Quality.ps1 · Passage-Quality.ps1 · Reports.ps1 · Export-Tables.ps1 ·
              Escalation.ps1 · Log-Retention.ps1 · SeedCandidate-Report.ps1 ·
              StrongMeaning-Report.ps1 · SpanAnalysis-Report.ps1 · SchemaOverview-Report.ps1 ·
              create-iba-view-template.ps1 · create-passage-view-and-export.ps1 ·
              create-passages-by-book-view-and-export.ps1 · export-iba-config-tables.ps1 ·
              generate-iba-db-schema-report.ps1 (5 relocated from iba\scripts\, escalation #271;
              standalone investigation utilities, not dispatcher-registered) ·
              _lib/Notify.ps1 (shared terminal-notification rendering, dot-sourced by every script)
  run.py                                               the dispatcher + run-state machine
  init.py                                              the session bootstrap (Start-Iba.ps1 calls it)
  report.py · validation.py                            the two original report generators
  db/iba.db                                            the IBA database (built; git-ignored)
  db/snapshots/                                        pre-run rollback snapshots (git-ignored)
  reports/    candidate-quality.md · passage-quality.md · log-retention.md · candidate-load.md ·
              seed-candidate.md · strong-meaning.md · span-analysis.md · schema-overview.md ·
              validation-book-*.md / report-*.md       (generated, per-run outputs) ·
              archive/ (auto-archived prior versions, incl. archived CSVs since #273) ·
              export/ (per-report CSV pairing AND table-export's full dump since #273 — git-ignored;
              was two separate folders, `iba/app/export/` and this one, consolidated to one)
  archive/    non-report historical files (new, escalation #271) — e.g. the superseded pre-
              restructure `New-Word.ps1` stub
  BUILD.md · GOVERNANCE.md · USER-GUIDE.md · UTILITIES.md    this doc set
  PLAN-reports-config-governance-v1-20260722.md · SESSION-LOG-20260722-reports-config-governance.md
```

The full run-command reference (one line per script/mode) is §2 above, kept current there — not
duplicated here.

---

## 9. Code changes this session (2026-07-22) — per `governance.build_md_on_code_change`

- **`lib/words.py:normalise()`** — fixed a real bug: the trailing-strip used to remove ANY
  trailing non-letter run unconditionally, including a closing bracket that legitimately paired
  with an opening one earlier in the word. `'blindness (spiritual)'` silently lost its `)` on
  every registration, becoming `'blindness (spiritual'` (found via a real malformed registry row,
  id 168, migrated from the legacy registry). Fixed: only strip trailing junk that doesn't leave
  an unmatched opening bracket behind — `[hypocrisy]` still strips cleanly (whole-word wrapper),
  `blindness (spiritual)` no longer does (a real qualifier). Known limitation: a doubly-wrapped
  input like `'[blindness (spiritual)]'` is left with trailing junk rather than partially cleaned
  — rare enough not to be worth the extra complexity.
- **`run.py`** — the escalation pause-idempotency check was keyed on `(word, at_step)`; every
  word-less step (`configmaint.propose`, `candidate.validate`, `passage.validate`, ...) runs with
  `ctx.word == ""`, so a second concurrent escalation at the same step was silently swallowed as a
  "duplicate" of the first even though its run correctly paused. Fixed: keyed on `run_id` + `step`
  instead (GOVERNANCE.md §10 has the full account).
- **`lib/cfgquality.py:find_orphan_configs()`** — the orphan-config detector only grepped `.py`
  source for a quoted literal; it couldn't see a setting/enum read dynamically via
  `cfg_column.expectation` DB data (`pattern:<key>`/`enum.<name>`), or a setting consumed only
  from a `.ps1` script's inline `python -c`. Wrongly flagged 10 actively-enforced configs as
  orphans (`candidate.tag_clean_pattern`, `raw.meaning_tree_clean_pattern`, `configmaint.auto_report`,
  and 6 of 7 flagged `cfg_enum` groups) — deleting any of the 6 enums would have broken
  `find_enum_violations`, which hard-fails when a declared enum has zero members. Fixed to check
  both `cfg_column.expectation` data and `.ps1` source, closing the false-positive class.
- **`handlers/passage.py:build()`** — `passage.cross_chapter` was declared but read nowhere (a
  confirmed true orphan, unlike the 10 above). Wired in: the chapter-boundary check now reads it,
  though flipping it to `true` currently has no practical effect — "adjacent" is computed purely
  from verse numbers (`vs == pvs + 1`), which never holds across a real chapter break since verse
  numbers reset to 1; true cross-chapter adjacency would need per-chapter verse-count data this
  app doesn't have. Documented in the code, not silently left half-true.
- **`cfg_setting.configmaint.reference_seed_dir`** removed (via `configmaint.propose`) — confirmed
  genuinely unused, staged for Layer-2 hard-enforcement work that isn't scheduled.

**Later the same day — `candidate.load` built, a real incident found and fixed by testing before
it reached the full seed, and the resulting missing capability (a DB rollback point) built.
Full account: GOVERNANCE.md §12.**

- **`iba/app/migration/add_candidate_seed_referent_columns.py`** (new) — `candidate_seed` gains
  `sense_seq` (extends the dedup key to `(lemma_key, strong_variant, sense_seq)`, resolving
  escalation `#228`'s dual-sense-one-strong problem), `step_status`, `ib_referent_type`; two new
  enums; the `exception` value on `candidate_decision`; three new `cfg_setting` rows; the
  `candidate.load` `cfg_step`/`cfg_write_grant`/`cfg_on_fail` registration.
- **`handlers/candidate.py`** — new `load()` (the JSON-batch pipeline) plus supporting functions
  (`_split_concepts`, `_format_violation`, `_resolve_lemma`, `_step_status`, `_ib_referent`,
  `_write_exception`, `_process_item`, `_revalidate_existing`); `_set_decision`/`curate()`/`set()`
  made `sense_seq`-aware (defaulting to 0, preserving existing behaviour exactly).
- **`ps/Candidate-Curate.ps1`** — added `-Mode Load -InputFile <path>`.
- **Three real bugs found by testing a small batch BEFORE running the full seed, not by
  inspection** — the exact discipline this app exists to enforce, applied to its own build:
  1. `candidate.transliteration_pattern`'s shipped default (`^(?=.*[a-z])[a-z]{2,10}$"`) matched
     almost any clean single-word English tag (`hearing`, `heart`, `spirit`, ...) — it cannot
     distinguish those from a real transliteration (`asah`, `halak`) by shape alone. **Ran once
     against the full seed before this was caught, writing `decision='exception'` over 1029 of
     1806 rows.** Recovered via `iba/app/export/candidate_seed.csv` (a same-morning export,
     matched by the stable `id` surviving the schema migration) — 1028 rows restored exactly,
     1 post-export row restored by code-path reasoning (a `curate()` split, which only ever writes
     `decision='candidate'`). Fixed: narrowed to a mid-word-apostrophe signal only
     (`^[a-z]+'[a-z]+$"`), verified against the same word list with zero false positives.
  2. `_resolve_lemma`'s matching used raw, unbounded substring containment (`w in gloss or gloss
     in w`) — a short real gloss like `'I'` or `'word'` matched inside an unrelated longer test
     word (`hearing` contains `i`; `zzznotarealword` contains `word`), causing a wrong-lemma match
     and, separately, letting a nonsense input auto-load as a real candidate. Fixed: word-boundary
     regex matching (`\bword\b`) plus an exact-tag-match-against-existing-`candidate_seed` check
     tried first (so a word that's already correctly seeded resolves to ITS row, not a
     coincidentally-matching different lemma).
  3. The duplicate-check path called the same `_write_exception` helper used for genuine
     exceptions — since the row already existed, it took the UPDATE branch and **overwrote the
     pre-existing legitimate row's `decision`/`tag`**, exactly contradicting the approved design
     ("no second row is written for a true duplicate... the existing row is already the record").
     Found on the SECOND test run (after fix 1, before this one). Fixed: a duplicate now writes
     and touches nothing — counted and named in the report/escalation only.
- **`iba/app/lib/dbsnapshot.py`** (new) — the rollback mechanism this app never had. `snapshot(reason)`
  copies `iba.db` (WAL-checkpointed first) to `iba/app/db/snapshots/`, prunes to
  `retention.snapshot_keep_count` (new setting, default 20, oldest deleted first). Wired into
  `run.py:_ensure_run()` — every NEW run (not a resumed one) snapshots first. `IBA_NO_SNAPSHOT=1`
  skips it for a tight loop, the same escape hatch the legacy Bible-study engine's own `_apply_*`
  pre-op snapshotting uses. Built directly in response to the incident above — the only recovery
  path available at the time was a stale 3-day-old manual `.bak` file and a lucky same-morning CSV
  export; this closes that gap going forward, not just for `candidate.load`.

---

## 10. Code changes this session (2026-07-22/23) — per `governance.build_md_on_code_change`

Reports fully config-governed — Phase 0 (existing reports + PS notifications wired to config,
content unchanged) and Phase 1 (the 4 new reports built). Full design:
`PLAN-reports-config-governance-v1-20260722.md`. Full technical account of both phases:
GOVERNANCE.md §13 (Phase 0) and §14 (Phase 1).

**New library modules:** `lib/reportkit.py` (shared scaffold render + archive-on-write + CSV
pairing — every report generator calls this instead of hand-building `## N. Title` lines),
`lib/seedreport.py`, `lib/strongreport.py`, `lib/spanreport.py`, `lib/schemareport.py` (the 4 new
reports), `lib/cfgquality.py` gained `REPORT_STEPS`/`find_missing_cfg_report_rows`/
`find_chained_packages_missing_complete_message`.

**New PS scripts:** `ps/_lib/Notify.ps1` (shared terminal-notification rendering, dot-sourced by
every work-package script instead of each hardcoding its own `Write-Host` strings — reads
`notification.*` settings), `ps/SeedCandidate-Report.ps1`, `ps/StrongMeaning-Report.ps1`,
`ps/SpanAnalysis-Report.ps1`, `ps/SchemaOverview-Report.ps1`.

**New migrations:** `migration/bootstrap_report_content_governance.py`,
`migration/bootstrap_retention_table_export_registration.py`,
`migration/bootstrap_new_reports_phase1.py` — all idempotent, re-run safe.

**Schema:** `cfg_report` / `cfg_report_section` / `cfg_report_csv_table` (new tables);
`cfg_on_fail.route` (new column); `cfg_work_package.complete_message` /
`.next_step_hint` / `.paused_message` (new columns); `notification.*` settings (new module).

**Registered as real dispatcher steps for the first time** (were standalone/unregistered before):
`log-retention` / `retention.report`, `table-export` / `table.export`. Fixed along the way:
`export_tables_csv` no longer dumps `cfg_*` tables (was duplicating `configmaint.report`);
`candidate.load` has its own `candidate.load_report_path` instead of a derived one; a real 2.2GB
gap in `.gitignore` (`iba/app/db/snapshots/` was uncovered) found and fixed while processing git
for this session's commits.

---

## 11. Code changes this session (2026-07-23, later) — clearing the escalation backlog (#269–#275)

Full technical account: GOVERNANCE.md §15A. Summary of what changed in code (config changes are
§15A's, not repeated here):

- **`handlers/configmaint.py:CFG_TABLES`** — added `cfg_report`/`cfg_report_section`/
  `cfg_report_csv_table`, missing since §13 despite already having `cfg_write_grant` rows. Real
  regression: `configmaint.propose` could not change any report config until this was fixed
  (escalation #274 surfaced it).
- **`lib/reportkit.py`** — new `archive_before_write()` helper (the same archive-on-write convention
  `write_report()` already used, now shared); wired into `_write_csv` so every CSV pairing archives
  its predecessor instead of silently overwriting it (escalation #273).
- **`tools/export_tables_csv.py`** — uses the same `archive_before_write()`; `DEFAULT_OUT` moved to
  `iba/app/reports/export` (was a separate `iba/app/export`, escalation #273).
- **`lib/strongreport.py`** (escalations #274/#275) — the intro's "with lexicon detail" figure was
  computed by a raw, un-joined `strong_lexicon` count while the completeness breakdown table used a
  properly `strong`-joined one; they happened to agree on live data (1506 both ways) but were one
  orphan-row away from silently disagreeing. Now both derive from the same joined counts, plus an
  explicit reconciling total line. Added: a "neither meaning nor lexicon" heading stat, and a new
  `sense_by_registry` section (registry word → strong → gloss → sense count, 4767 rows) —
  registered via a new `cfg_report_section` row (ordinal 2, shifting `lexicon_completeness` to 3).
- **7 files relocated** from `iba\scripts\` into `iba/app/tools/`/`iba/app/ps/` (escalation #271;
  full list in §8); their own usage-docstring path references updated to match. A stale
  pre-restructure `iba\ps\New-Word.ps1` stub archived to the new `iba/app/archive/`.
- **`registry-report` built** (escalation #272) — `lib/registryreport.py` (new), `handlers/
  reports.py:registry_report`, `ps/Registry-Report.ps1` (new), fully config-registered (`cfg_report`/
  3 `cfg_report_section` rows/`cfg_report_csv_table`/`report.registry_path` setting); added to
  `lib/cfgquality.REPORT_STEPS` so its own coherence check covers the new report from day one.
- **`lib/escalation.py:list`** (raised separately, same session, not one of #269–#275) — `Escalation.
  ps1 -Action List` had always printed the open-escalation list to the terminal only, never
  persisting it — the same `governance.reports_must_persist` standard every other report in this app
  already followed. New `write_list_report()` writes `escalation.list_report_path` (default
  `iba/app/reports/escalation-list.md`, archived on regenerate); the CLI now prints a one-line
  pointer + count instead of the full dump. New `escalation` config_module (enum value) added so the
  new path setting has a proper home, matching every other utility's own module.

**Verified:** `report.hypocrisy.md` and `strong-meaning.md` both regenerated and manually inspected
post-fix; `table-export` re-run confirmed archive-on-write fires correctly against the now-shared
export folder (12 pre-existing files archived with original timestamps, none lost);
`registry.md` regenerated and inspected (summary/by_strong/sense_report sections all correct);
`Escalation.ps1 -Action List` re-run, confirmed it now writes the file and the terminal shows only
the pointer line; `configmaint.validate` re-run clean of hard errors throughout (advisory orphan/
justification findings are a separate, still-open researcher judgement call, not a regression from
this work).

---

## 12. Escalation lifecycle extended — Edit / Pause / Resume / Retract (2026-07-23, later)

The researcher pointed out `USER-GUIDE.md`'s escalation instructions were scattered across six
sections with no single complete reference, and asked for the ability to edit/pause/retract a
work item raised via `Escalation.ps1 -Action Raise` — the escalation table doubles as a backlog of
things for Claude to action, not only design decisions awaiting approval, and that lifecycle needed
more than raised → answered.

**Schema:** new `cfg_enum` group `escalation_state` (`raised`/`answered`/`paused`/`retracted`) —
`state` had no governed vocabulary at all before this (free-text, unlike every other enum-backed
field in the app).

**`lib/escalation.py`:** four new functions — `edit_question()`, `pause_run()`, `resume_run()`,
`retract_run()` — plus a shared `_manual_only()` guard. **Deliberately restricted to
`MANUAL-`-prefixed run_ids**, found necessary while building, not part of the original ask: a real
dispatcher-tied escalation (`configmaint.propose`, `candidate.validate`, ...) is read by two
downstream checks keyed specifically on `state='raised'`/`'answered'` — `run.py`'s own pause-continue
dedup (line ~112) and `answered_for_run()`. Pausing one of those would flip its state to `paused`,
matching neither check, so re-running the underlying command before resuming it would raise a
**second** escalation row for the same run_id+step instead of recognizing the existing pause. Manual
items have no such downstream reader, so the four new actions simply refuse a non-`MANUAL-` run_id
with a clear message rather than risk that class of bug. `write_list_report()` (§ escalation-list,
above) now shows `raised`+`paused` together (paused flagged), with a state column.

**`ps/Escalation.ps1`:** four new `-Action` values (`Edit`/`Pause`/`Resume`/`Retract`), each with its
own parameter validation, added to the existing `ValidateSet`.

**`USER-GUIDE.md` §4 rewritten** as the single, complete escalation reference (states, the three
scopes, all 8 actions, resume behavior) — every other section's mention of `Escalation.ps1` is now
just that section's own usage moment, pointing back here instead of re-explaining.

**Verified end-to-end:** raise → edit (old wording preserved in `tried`) → pause → list (shows
`38 open (37 active, 1 paused)`) → resume → retract → list (back to 37, item gone from the open
list); the `MANUAL-` guard confirmed rejecting a real `RUN-...-CONFIGMAINT` run_id with the intended
message; `configmaint.validate` re-run clean of hard errors (`escalation_state` joins `escalation_answer`
as an expected orphan enum — free-text state values, not looked up by enum name in code, same class
already accepted for `escalation_answer`).

---

## 13. Orphan-config check redefined — usage is per-kind, not one grep (2026-07-23, escalation #305)

The researcher raised escalation #305 flagging §12's own closing note above as itself the bug:
accepting `escalation_state`/`escalation_answer` as orphans "same class already accepted" was
papering over a check that was too weak, not confirming they were actually fine. Their correction:
"usage" isn't one shape — it differs by config kind, and the existing grep-anywhere test proved
none of them. Full detail: `GOVERNANCE.md` §15C.

**`lib/cfgquality.find_orphan_configs()` rewritten**, three kinds now checked differently:

- **plain `cfg_setting`** (most rows): the key literal must co-occur, in the SAME file, with an
  actual `.setting(` call — not just appear anywhere in the multi-file corpus (which a stray
  comment could satisfy without the code ever applying the value). Same-file rather than
  same-call-site so settings read via a level of indirection (e.g. `validation.py`'s
  `_WORD_SECTIONS` dict → `cfg.setting(key, True)` in a loop) still pass correctly.
- **`cfg_setting` with `module='governance'`**: these are process rules for the AI/researcher
  workflow, not runtime application inputs, so there's no "applies the value" behaviour to find.
  Usage = read explicitly by `init.py` (the startup routine) — either the literal key, or (what
  was actually built, see below) a generic `WHERE module='governance'` read.
- **`cfg_enum` group**: usage = looked up BY NAME at runtime (`cfg.enum(name)`, or the equivalent
  raw `cfg_enum WHERE name='<name>'` SQL a couple of handlers use directly) — a group's individual
  VALUES appearing as hardcoded string literals elsewhere (`state == "paused"`) does NOT count;
  that's the vocabulary being duplicated in Python, not read from the config.

**`init.py`** gained step 6: prints every `module='governance'` `cfg_setting` row explicitly at
startup, queried generically (`SELECT key, value FROM cfg_setting WHERE module='governance'`) so a
future governance setting is picked up automatically, no init.py edit required each time. `cfg.close()`
moved to after this block (was closing the connection before the orientation/governance-print steps
even ran — harmless before since nothing after it touched `cfg.conn`, but this section now does).

**`lib/escalation.py`**: `escalation_answer`'s hardcoded `RUN_ANSWERS` Python tuple replaced with a
live `cfg.enum("escalation_answer")` call inside `answer_for_run()`. New `_check_state()` helper
validates every `state=` write (`raise_`, `answer_for_word`, `raise_manual`, `answer_for_run`,
`pause_run`, `resume_run`, `retract_run`) against a live `cfg.enum("escalation_state")` lookup
instead of a bare literal — a DB-side enum change (e.g. removing `'paused'`) now actually changes
what these functions accept, closing the exact gap the researcher described ("if the value of the
config change, will the code automatically respond to it").

**Verified:** `find_orphan_configs()` re-run directly against the live DB — 0 orphans (was 6:
`governance.build_md_on_code_change`/`governance_md_on_rule_change`/`scripts_ps_dir`/
`scripts_python_dir`, `escalation_answer`, `escalation_state`). A synthetic sanity check (fake
never-used setting + fake never-used enum injected into an in-memory DB) confirmed the rewritten
check still correctly flags genuinely-unused config — not just permissive. Full `escalation.py`
lifecycle re-verified end-to-end post-change: raise → pause → resume → retract, and answer-run with
both an invalid decision (correctly rejected via the live enum) and a valid one (`approve`) —
all via the real `cfg.enum()` calls, not the old hardcoded tuples. `configmaint.validate` re-run via
the actual dispatcher (`python -m iba.app.run`) confirms the message no longer mentions any
orphans — only the 7 pre-existing `candidate.*` "needs justification" findings remain (a separate,
untouched check — see `iba/app/docs/escalation-304-orphan-justification-review-v1-20260723.md` Part
B for that one).

**Left open:** escalation #304 itself (the original 6-orphan + 7-justification finding) is still
`raised` — this session fixed the DETECTOR and the two real code gaps it found (governance settings
unread, enums not looked up), it did not answer #304, since answering it is the researcher's
judgement call on the review file, not something to self-resolve. A by-product `RUN-verify-orphan-
fix-20260723` escalation (id 307) was raised by a manual dispatcher test run during verification —
not a `MANUAL-` id, so it can't be retracted via the sanctioned path; flagged to the researcher
rather than touched directly.

---

## 14. `inactive` config column built and applied to the whole candidate system (2026-07-23, escalations #306/#310)

Escalation #306 ("`cfg_candidate_rule` makes no sense, assume unused — delete it") turned out
factually wrong on inspection: `handlers/candidate.py`'s `seed()` reads its `accept`/`reject` kinds,
but `_resolve_lemma()`/`_ib_referent()` — helpers the NEWER `candidate.load` routine calls — reuse
its `synonym`/`body-part`/`other-being` kinds too (confirmed by grep + each function's own
docstring). Deleting it would have broken the routine meant to replace `seed()`, not just retired
dead weight. The researcher's actual instruction, once given: the WHOLE candidate system — old
(`set-candidates`, `seed-candidate-report`) and new (`candidate-quality`, `candidate-curation`)
alike — "will all be retracted in due course" as part of "a substantial mess up over the past few
days," so ALL of it needs deactivating together, not selectively.

That reuses escalation #310's separate ask ("add a column in each config table to mark a config as
inactive. Inactive configs must be excluded from the validation but included as a list in the
report") — built generally, not just for this one case:

- **`migration/bootstrap_inactive_column.py`** (new, one-off): `ALTER TABLE ... ADD COLUMN
  inactive INTEGER NOT NULL DEFAULT 0` + a `cfg_column` registration row, on 14 config-CONTENT
  `cfg_*` tables (excludes `cfg_meta`/`cfg_change_log`/`cfg_change_detail` — audit/state, not
  config content — and `cfg_table`/`cfg_column`/`cfg_unique` — describe other tables' schema, not
  a toggleable item themselves).
- **`handlers/configmaint.py:_validate_live()`** and **`lib/cfgquality.py`**
  (`find_orphan_configs`/`find_settings_needing_justification`/`find_missing_report_paths`/
  `find_missing_cfg_report_rows`/`find_chained_packages_missing_complete_message`) — every check
  that reads one of the 14 tables now filters `WHERE inactive=0`; a new `_step_inactive()` helper
  lets the two report-completeness checks (keyed off hardcoded `REPORT_STEPS`/
  `QUALITY_CHECK_REPORT_PATH` Python tuples, disconnected from `cfg_step`) skip a retired step
  entirely rather than keep flagging its now-deliberately-stale report config.
- **`lib/cfgreport.py`**: new `_inactive_configs()` — every inactive row, listed (not silently
  dropped), grouped by table; `cfg_candidate_rule` summarised by kind+count rather than listing
  289 individual Strong's codes. Folded into the existing "findings" section of `CONFIG-REPORT.md`
  rather than a new `cfg_report_section` row — same "config health" content, no new report
  registration needed.
- **`migration/retract_candidate_system.py`** (new, one-off): applies the above to every row
  genuinely part of the candidate system, enumerated by direct query first (not guessed) — 4 work
  packages, 6 steps, 5 write-grants, 7 settings, 3 `cfg_report` rows + 10 sections + 5 CSV
  pairings, 10 `on_fail` rows, 4 enum groups (15 values), all 289 `cfg_candidate_rule` rows. 354
  rows total, across 10 tables.

**Verified:** `configmaint.validate` — clean `"ok"` before AND after (no regression from the new
`WHERE inactive=0` filters when nothing was yet inactive; the pre-existing 7 candidate.*
justification findings gone entirely after the retraction ran). `CONFIG-REPORT.md` regenerated,
"Inactive configs" lists all 354 rows correctly grouped by table.

**Deliberately NOT done:** `inactive` only excludes a row from `configmaint.validate`'s advisory/
coherence checks — it does not block a retired step from actually being invoked (`run.py`'s
dispatcher doesn't check it). Actually preventing execution of a deactivated work package wasn't
asked for and is a separate decision (error vs. warn vs. silently allow) — flagged here rather than
assumed.

---

## 15. Lexicon term extraction + IB-relevance triage pass — built and concluded in one session (2026-07-24)

Not wired into the app/DB pipeline — all of `iba/app/tools/` scripts below are exploratory data-prep,
runnable standalone. Full narrative: `iba/logs/SESSION-LOG-20260724-lexicon-extraction-ib-relevance-
classifier-span-reconciliation.md`. Short version: this investigated whether Inner-Being relevance
can be judged from a term's own meaning (no registry/Strong's-number lookup), found real coverage is
already high, found the word-level classification approach hits a hard ceiling on accuracy, and
concluded the next phase should analyse individual spans/characteristics directly rather than keep
investing in pre-classification. The tooling below is a **one-time triage pass**, not an ongoing
method — kept for its actual findings (coverage numbers, the function-word list), not as infrastructure
to build on.

**Built:**

- `lexicon_split_common.py` — shared bracket-aware comma/semicolon gloss-splitter and word-count/
  script-based row classifier (`split_multi_gloss`, `classify_row`), factored out of
  `build_mounce_lexicon_extract.py` so `build_lsj_sense_extract.py`/`build_meaning_tree_extract.py`
  could reuse the identical logic instead of duplicating it. Mounce refactor verified byte-identical
  before/after.
- `build_lsj_sense_extract.py`/`build_meaning_tree_extract.py` — added a `row_type` column
  ("headword"/"lookup" for LSJ; always "lookup"→classify_row-driven for meaning-tree, since it has no
  headword concept), and exploded bundled comma/semicolon gloss text into one row per term, matching
  Mounce's existing shape. Also fixed a real LSJ bug: bare-numeric sub-sense labels nested under the
  implicit first "I" now correctly compose to "I.2" etc. (3,856 of 25,775 rows affected).
- `build_lexicon_lookup_extract.py` — combines all three sources' `row_type == "lookup"` rows into
  one flat (strong, term, source) list, with its own blank/script/duplicate filtering. 40,039 rows.
- `ib_relevance_classifier.py` — free, local, wordlist-based `classify_ib_relevance(term)`: IB
  related / Not relevant / Could impact IB (default). Category wordlists (emotion, volition/cognition,
  character/moral trait, spiritual state vs. concrete objects, plants/animals, body parts, kinship,
  numbers, proper names, generic verbs/nouns/adjectives, quantifiers, stopwords) built and repeatedly
  corrected against actual output inspection across the session — see the session log for the full
  sequence of researcher-found gaps and fixes (numerals, transliteration false alarm → real proper-
  name gap, curly-apostrophe normalization, hyphenated-compound-name structural rule).
- `build_span_term_reconciliation.py` — reconciles the term list against `span` (real text
  occurrences), joined on STRONG ALONE (word-level mismatches are not gaps). Two outputs: span words
  with zero lexicon coverage ("missing term" signal) and lexicon-covered strongs with zero text
  occurrence ("missing verse" signal). Also owns `FUNCTION_WORD_STRONGS` — ~61 hand-verified Hebrew/
  Greek function words (direct-object marker, copula, prepositions, conjunctions, pronouns,
  interrogatives, particles, numeral carriers) excluded because `is_particle` doesn't catch them and
  their `surface` text in `span` is borrowed from an adjacent word, not their own content. Found
  systematically (querying `span` for the strongs with the most distinct surface words attached) after
  the researcher spotted `H0853` behaving this way, then again after spotting `H4069` at smaller scale.
- `_check_missing_strongs_in_step.py` / `_check_ib_related_span_step_coverage.py` — one-off, read-only
  STEP-coverage checks (govered `lib.stepapi.Step` client, no writes) confirming: all 240 lexicon-
  covered-but-textless strongs genuinely have zero verses in STEP (not a loading gap), and of 235
  strongs behind the "IB related" span rows, 174 (74%) are already fully covered locally with only a
  460-verse combined gap across the rest.

**Verified:** every wordlist/structural fix in `ib_relevance_classifier.py` was checked against the
specific failing examples before being trusted (unit-style `classify_ib_relevance()` calls in the
terminal, not assumed); the Mounce refactor was diffed byte-identical; the LSJ sub-label fix and the
STEP-variant-vs-base-strong bug in the coverage-checker were each caught by the researcher/self before
being reported as done, not after.

**Deliberately NOT done further:** did not keep expanding `ib_relevance_classifier.py`'s wordlists
after the researcher's own conclusion that word-level pre-classification is the wrong level of
investment going forward (see the session log's closing section) — remaining known false positives
(e.g. a rare borrowed-surface-text word coinciding with a content strong's wordlist, like `H3068G`
tagged "IB related" from one stray "peace") are left as a documented, understood limitation, not
patched.

## 16. `span` model correction — combined-code tags were being split, not just mis-tallied (2026-07-25)

**Bug found by the researcher**, working from `outputs/csv/span-unmatched-lexicon-json-iba-20260725.csv`
(the lexicon-combined completeness check, §15's line of work): `span_id=7` (verse `2Cor.6.6`, "purity")
showed `strong_variant='G1722'` alone — but STEP's own HTML tags that word `<span morph='PREP N-DSF'
strong='G1722 G0054'>purity</span>`, i.e. ONE combined unit (the preposition ἐν fused with its noun for
this English rendering). The old `parse_spans()` exploded every multi-code tag into one row per code,
pairing the SAME surface text with each — so the `G1722` row for "purity" showed `surface="purity"`,
which is wrong; "purity" is `G0054`'s surface, not `G1722`'s (`G1722` has none of its own here). This
repeated across every multi-code tag in the DB: 116,953 of the rebuilt 370,200 rows now carry more than
one code.

**Verified the fault was in our parsing, not STEP's data**, before touching anything: fetched
`2Cor.6.6` live from STEP (`rest/search/masterSearch/strong=G1722|version=ESV_th|reference=2Cor.6.6-
2Cor.6.6`) and diffed its `preview` against the stored `verse.preview` — byte-for-byte identical (816
chars). Also sampled ~4,000 verses to check the multi-code pattern generalizes correctly: Hebrew
multi-code tags are a different, already-correct phenomenon (one written word = root + attached
prefix/suffix particles, e.g. `H7931 H9033 H0408 H9002` on "dwell" — genuinely one unit, particles
already flagged `is_particle`); Greek multi-code tags have NO fixed code order (`PREP` first on
"purity" `G1722 G0054`, but `PREP` second on "leaven" `G2219 G1722`, and no head at all on "But"
`G1161 G2532` — two conjunctions fused into one English word) — ruling out a "take the last code"
heuristic and confirming the only correct fix is: keep a tag's codes together, don't split them.

**The declared config model was itself wrong**, not just the code: `cfg_table.span.grain` said "ONE ROW
PER CODE"; `cfg_column.span.strong_variant.use` said "ONE strong code" with an FK to
`strong.strongNumber`. That's what justified the split in the first place. Corrected via
`Config-Maintenance.ps1 -Step Propose` (approval-gated, all three approved by the researcher):

- `RUN-20260725_133709_153-CONFIGMAINT` — `cfg_table.span`: grain/use → one row per HTML `<span>` TAG,
  not per code; `(verse, position)` is the key on tag index, not code index.
- `RUN-20260725_133720_920-CONFIGMAINT` — `cfg_column.span.strong_variant`: dropped the single-code FK
  to `strong.strongNumber` (doesn't hold for a combined value); redescribed as "one or more strong
  codes, space-separated, as STEP's HTML has them."
- `RUN-20260725_133735_587-CONFIGMAINT` — `cfg_column.span.is_particle`: redefined as "1 only if EVERY
  code on the tag is a particle" (was implicitly single-code).

**Code fixed to match:**

- `lib/stepapi.py` `Step.parse_spans()` — now one row per `<span>` tag: `strong_variant`/`morph_code`
  keep the tag's full space-separated list; `position` is the tag index; `is_particle` is `1` only if
  every code in the tag is a particle.
- `handlers/raw.py` `validate()` — the parse-check (`span` recovers every `strong_verse` assertion) now
  matches a code against any whitespace-delimited *token* in `strong_variant`, not exact string equality
  against the whole column, so it still works once a row can hold multiple codes.

**`span` fully regenerated**, not patched: `migration/rebuild_span_combined_units.py` (dry-run by
default, `--apply` to write) deletes and reinserts every row from the already-stored `verse.preview` —
no STEP re-fetch needed, since the preview HTML was already confirmed correct and unchanged. DB backed
up first (`db/iba.db.bak-20260725-prespanregen`). Result: 534,075 → 370,200 rows (fewer, since combined
tags collapse to one row instead of N). Verified `verse_id=2` produces exactly the 9 tags in its HTML
(was 14 rows exploded from 9 tags).

**Global re-verification of the parse-check** (all 112,446 `strong_verse` assertions, not just one
word): 424 still unrecoverable, across 5 codes (`G1510`, `G2192`, `G1096`, `H5462`, `G3588`). Traced to
a **separate, pre-existing bug**, NOT caused by this fix and NOT fixed in this pass: `cfg_setting.
step.span_html`'s regex requires a `morph='...'` attribute to match at all, but 1,076 span tags across
823 verses have none (e.g. `<span strong='G3588'>which</span>`, Jas 1:21 — no `morph=`) and are silently
skipped by both the old and new parser alike. Flagged to the researcher; not yet actioned.

**Ripple effects not yet addressed** (flagged, not silently left implicit): any downstream consumer
that assumed `span.strong_variant` is always a single clean code will need the same token-aware
handling as the `validate()` fix — in particular `_check_span_unmatched_lexicon_json.py` (§ this
session's earlier work) matched on `split_strong_variant(strong_variant)`, which will now mis-split a
combined value; it needs re-running with token-aware matching before its numbers can be trusted again.

## 17. Lexicon-parsed layer baked into the core app + progressive meaning-only backfill (2026-07-25, later)

Continues §16 — the same session's corrected parsing rules (comma/semicolon are not sense
separators, refs/notes scoped per `<b>` span) were still only living in `iba/app/tools/`'s
exploratory extract scripts, output to `outputs/csv|json/`. Researcher's instruction: "bake this
into the app... create the schemas, create the configs, and update the methods to follow the
standard of the IBA app and be included in the core system... check every aspect to ensure you
build this in accordance with the rules" — full GOVERNANCE.md re-read first, not assumed from
memory, per that instruction.

**New parsed layer — 4 tables, physically built FROM `cfg_column`, not hand-written DDL**
(`migration/bootstrap_lexicon_parsed_layer.py`, bootstrap-direct — brand-new mechanism, same
class as `bootstrap_new_reports_phase1.py`, not `configmaint.propose`-able):

- `strong_meaning_parsed` (base-keyed, `lemma_key` — matches `strong_meaning_tree`'s own key)
- `strong_lsj_parsed` / `strong_mounce_parsed` (full-code-keyed, `strong` — matches `strong.
  strongNumber`/`strong_lexicon.strong` exactly, FK'd)
- `strong_related` (full-code-keyed; STEP's `relatedNos`, fetched live — no raw table captures
  this, so it's not "parsed FROM" anything, it's fetched fresh. `related_strong` deliberately
  unconstrained — STEP can name a code never onboarded here)

**Parsing logic ported to `lib/lexiconparse.py`**, not imported from `tools/` — the exploratory
scripts stay "not wired into the app" as their own docstrings say; the app gets its own governed
copy of the same corrected algorithm (`SegmentParser` for meaning-tree, `SenseParser` for LSJ,
`RowSplittingParser` for Mounce), verified byte-identical row counts against the tools/ output
before trusting it (11788/10020/1547).

**New standalone work package `lexicon-parse`** (3 steps, each independently invokable —
`Lexicon-Parse.ps1 -Step Parse|Related|Validate`):
- `lexicon.parse` — no network, deterministic, full clear-and-rebuild every run (no natural dedup
  key on a parsed-sense table, same shape as `strong_meaning_tree` itself).
- `lexicon.related` — one live STEP `getInfo` call per `strong` row. A genuine zero-related result
  writes a placeholder row (empty `related_strong`) so it's distinguishable from "never
  attempted" — found this the hard way: the first version of `lexicon.validate` flagged all 362
  legitimate zero-result strongs as a coverage gap because of this exact ambiguity; fixed by
  writing the placeholder, not by loosening the check.
- `lexicon.validate` — coverage (`strong_lexicon`/`strong` rows with no parsed/related output) +
  value-quality (`lib.valuequality`, `notblank` on `strong_meaning_parsed.gloss`) — same shape as
  `candidate.validate`/`passage.validate`, escalates only if findings exist, persists
  `iba/app/reports/lexicon-parse.md` every run (`governance.reports_must_persist` — registered in
  `lib/cfgquality.QUALITY_CHECK_REPORT_PATH`/`REPORT_STEPS`, the hardcoded Python tuples that make
  `configmaint.validate` actually check for it, not just a convention).

New `config_module` enum value `lexicon` (bootstrapped alongside, same batch — a new VALUE on an
already-existing group, not a schema change). No new `cfg_write_grant` rows needed for `strong`/
`strong_sense`/etc. — `lexicon.parse`/`lexicon.related` only write their own 4 new tables.

**A real, pre-existing coherence bug found and fixed while verifying** (unrelated to this layer):
§16's `span.strong_variant.fk` correction had set it to `''` (empty string) to mean "no FK" —
`configmaint.validate`'s FK check treats any non-NULL `fk` as a declared reference to parse, so
`''` failed as "FK -> unknown table ''". Fixed via `configmaint.propose` (`fk: null`) — the
correct NULL representation, no behaviour change intended. `configmaint.validate` was clean
before this layer's work started (§16 didn't re-run it) — this was sitting latent until today's
full re-check surfaced it, exactly why the researcher's "check every aspect" instruction mattered.

**Progressive meaning-only backfill — `handlers/raw.py:backfill_meaning`, new standalone work
package `raw-backfill`** (`Raw-Backfill.ps1 -Book <book> [-Range C:V-V]`). Researcher's finding,
working from `tools/build_verse_span_meaning_extract.py`'s output: a "(not yet registered)" span
is often a supporting term still relevant to reading a passage, even though nobody onboarded it as
its own study word. Of three approaches offered (bulk-pull the whole Bible; pull live at
report-render time; pull progressively per passage, persisted), chose the third — reuses `raw.
detail_one()` completely unchanged (already meaning-only, already independent of `raw.verses` —
the split asked for already existed, just only ever invoked from the per-word `new-word` chain).
No new write grants needed (writes under the existing `call2_getInfo` writer identity, which
already holds every grant it needs) and no new "meaning pulled" marker column — a `strong` row
existing with no matching `strong_verse` row already IS "meaning without verses", the same
signal the verse:span:meaning report already reads to detect coverage.

**`tools/build_verse_span_meaning_extract.py` itself updated twice more, same day** (it had
already been fixed once this session for §16's span-combined-code regression):
- Meaning source switched from raw `strong_meaning_tree.sense_text`/`strong_lexicon.mounce`
  (unparsed HTML) to the new `strong_meaning_parsed`/`strong_mounce_parsed` tables. `strong_sense.
  head` dropped entirely (superseded). `strong_lsj_parsed` deliberately NOT pulled in by
  default — LSJ is the classical lexicon, often dozens of senses per term, and would bloat a
  per-verse table past readability for this report's stated use.
- Added `--range C:V-V` (e.g. `1:1-7`) alongside the existing whole-chapter `--chapters`, for a
  study passage narrower than a chapter — the researcher's actual next request.

**Verified end-to-end for Dan 1:1-7** (the researcher's own worked example): `raw.backfill_meaning`
found 84 distinct strongs referenced, 62 unregistered, pulled all 62 clean (0 STEP failures);
`lexicon.parse` re-run picked them up (`strong_meaning_parsed` 11788 -> 12073); the report
regenerated from 24% to **100%** meaning coverage for that range, e.g. "year" (`H8141 H9003`,
a combined preposition-prefix tag) now shows both codes' real meaning instead of one failed
lookup. `configmaint.validate` re-run clean after every step (`ok`, 0 coherence errors,
0 orphans) — confirming both the lexicon-parsed layer and raw-backfill mechanism, plus the §16
FK fix, are fully coherent together.

## 18. `raw.backfill_meaning` now self-contained — parse + related folded in (2026-07-25, later)

Continues §17. Found immediately in use: after the first Dan 1:1-7 backfill, `lexicon.validate`
correctly flagged 62 strongs with no `strong_related` fetch yet — the parse/related refresh had to
be remembered and run manually as separate steps, and the related refresh specifically was missed
once before being caught. Researcher's instruction: fold both into the backfill method itself.

**`handlers/lexicon.py` refactored, no behaviour change to the existing steps**: the rebuild body
of `parse()` extracted to `rebuild_parsed_tables(ctx) -> dict`, and `related()`'s fetch body to
`fetch_related_for(ctx, codes, clear_first) -> dict` (`clear_first=True` for `lexicon.related`'s
own full-table use; `False` for a targeted append, since brand-new strongs can't collide with an
existing row). `lexicon.parse`/`lexicon.related` now thin wrappers over these.

**`handlers/raw.py:backfill_meaning` calls both directly** after `detail_one()`, imported inside
the function body (not at module top) to avoid shadowing its own local `c["lexicon"]` counter.
One command now does the whole job: pull meaning for unregistered strongs -> rebuild the parsed
layer -> fetch relatedNos for exactly the newly-registered strongs (not a full 3000+-strong
re-fetch — cheap, targeted).

**Verified**: smoke-tested on Dan 1:8 (one previously-unregistered strong) — a single
`Raw-Backfill.ps1` call reported the meaning pull AND the parsed-layer rebuild (12073 -> 12080
meaning rows) AND the related fetch (5 rows) in one outcome message; `lexicon.validate` and
`configmaint.validate` both re-run clean immediately after, no manual follow-up step needed.

## 19. `build_verse_span_meaning_extract.py` — meaning renderer corrected again, researcher's direct challenge (2026-07-26)

Found live via H3581B (a real homonym pair — H3581A "reptile" vs H3581B "strength", same
`accentedUnicode`/transliteration, unrelated meanings): the researcher's verdict was blunt —
"you building of the report is faulty and not reliable, you are not working strictly with the
strong variant... I also do not like the way that you filter the information... Meaning means
considering the three parse files together, not pick the first one." Both true, both fixed in
`tools/build_verse_span_meaning_extract.py`:

- `strong_meaning_parsed` is base-keyed in the SOURCE data (`strong_meaning_tree` collapses
  sub-entry letters — a known, pre-existing limitation, not new). The renderer was presenting its
  content as if specific to the exact span code with no indication otherwise. It cannot be MADE
  code-specific here, but it can stop being presented as if it already were: now labeled with its
  base and an explicit `[AMBIGUOUS - base shared with <siblings>, may not be specific to <code>]`
  flag whenever `strong` has more than one code sharing that base (22 spans flagged in Dan 1:1-7
  alone).
- `stepGloss`/`meaning_tree`/`lsj`/`mounce` were a priority cascade (first non-empty wins), and
  `lsj` was excluded outright (an earlier, now-corrected scoping decision, §17). All four are now
  shown together on every covered span, each its own labeled line, `(none)` where empty — never
  silently merged or dropped.

Not a schema/mechanism change — this tool stays a standalone, read-only one-off
(`oneoff_path`-governed naming only, same as before). Regenerated for Dan 1:1-7 and verified live
against H3581B specifically: the ambiguity is now visible in the output, not hidden.
