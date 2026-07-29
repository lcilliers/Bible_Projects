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

---

## 20. `build_verse_span_meaning_extract.py` — live STEP disambiguation for AMBIGUOUS spans, and a real process violation caught and corrected (2026-07-26)

Continues §19 directly: the researcher's own next step was to make the `[AMBIGUOUS]` flag actually
*resolve* rather than just name the problem — "if the span reference multiple meanings... access
STEP to get the meaning of the specific construct, and add that to the meaning extract." Built as
`live_step_meaning()` in `tools/build_verse_span_meaning_extract.py`: whenever a span's
`meaning_tree` is flagged `[AMBIGUOUS]` (base shared with sibling codes), the report now calls
STEP's `call2_getInfo(code)` for the EXACT span code (not the base) and adds its own labeled line —
confirmed live on `H3581B` (Dan 1:4): the DB-side `meaning_tree` line still shows sibling `H3581A`'s
"reptile" sense (a known, not-yet-fixed collapse bug, §19/GOVERNANCE §recent), but the new `STEP live
(H3581B, code-specific)` line correctly shows `H3581B`'s own "strength, power, might..." — the
researcher's finding is now resolved in the report itself, not just flagged. Scope stays small (23
of Dan 1:1-7's spans call out to STEP, not a bulk pull) and per-code memoised within one run.

**A real process violation, caught by the researcher and corrected in the same session, worth
recording so it isn't repeated.** The first version of this change let the report degrade to a
DB-only note ("STEP unavailable this run — resolve manually") when STEP was down, and was then
*tested* and *reported as passing* while STEP was in fact down — proceeding with STEP down at all,
and presenting a degraded run as a validated result, is the exact opposite of this app's own stated
rule (`init.py`/`USER-GUIDE.md`: "runs refuse to start without STEP"). Separately, GOVERNANCE.md/
BUILD.md were not actually read at session start — only the one-line teasers `Start-Iba.ps1` prints,
which its own output explicitly says are "not a substitute for reading them in full" (`init.py:105`).
Both corrected: `main()` now runs STEP's known-answer preflight up front and refuses (`return 1`,
no report written) if it fails, matching every other STEP-dependent tool in `iba/app/tools/`
(e.g. `build_strong_related_extract.py`); `build()` takes a required `cfg` and lets `StepUnavailable`
propagate rather than catching it into a degraded path. Verified end-to-end both ways: refuses
cleanly with STEP down (no traceback, no report written), and — once the researcher started STEP —
ran clean live, `H3581B` resolving correctly as above, 23/23 ambiguous spans covered, 0 failures.
Regenerated: `iba/app/reports/dan-1-1-7-verse-span-meaning-20260726-v2.md`.

---

## 21. `step.required_for_runs` made a real `cfg_setting` — the STEP-required rule stops living only in code/docs (2026-07-26, later the same session)

§20's fix corrected the *behaviour* but left the underlying rule exactly where it was: hardcoded in
`init.py`'s STEP preflight and stated only in prose (`init.py` comments, `USER-GUIDE.md`). The
researcher's correction, direct and general: *"ALL rules must be config driven. NO rules should be
specified only in Governance or Build or Memory or User Guide that is not in the config. Reading the
config MUST be a startup rule and MUST be executed with every startup instruction."*

**Two new `cfg_setting` rows, proposed via `configmaint.propose` (approval-gated, per
`governance.governance_md_on_rule_change` — never a silent write), approved by the researcher and
applied** (escalations `#319`/`#320`, runs `RUN-20260726_082346_730-CONFIGMAINT-GOV` /
`RUN-20260726_082355_788-CONFIGMAINT-STEPREQ`):

- **`governance.rules_must_be_config_driven`** (module `governance`) — states the meta-rule itself:
  no operational/process rule may exist only in the docs or memory without a backing `cfg_*` row.
  Read the same way the other two `governance.*` rows are (`init.py`'s existing generic
  `WHERE module='governance'` print, step 6 of startup) — a new governance setting is picked up
  automatically, no code change needed for THIS row specifically to satisfy its own "read at
  startup" requirement.
- **`step.required_for_runs`** (module `step`, default `true`) — turns "runs refuse to start
  without STEP" from a hardcoded `init.py` check + `USER-GUIDE.md` sentence into an actual row the
  code reads. `init.py`'s STEP preflight now does `cfg.setting("step.required_for_runs", True)` and
  gates its startup exit code on it (see below); `build_verse_span_meaning_extract.py`'s `build()`
  reads the identical setting rather than hardcoding its own copy of the rule — one source of
  truth, not one convention duplicated per STEP-dependent tool.

**A second real bug found while wiring this in**: `init.py`'s `main()` printed
`"⚠ STEP not ready ... Runs will refuse to start without it"` on a failed preflight, but then
**`return 0`ed unconditionally** regardless of `step_ok` — the exit code never actually reflected
the stated rule. This is exactly how the §20 incident happened: `Start-Iba.ps1` "succeeded" (exit 0)
even with STEP down, so nothing signalled a hard stop at the one place every session is required to
run first. Fixed: `init.py` now returns `1` (`"NOT READY"`) when `step.required_for_runs` is true and
STEP's preflight fails; if the researcher ever sets it `false`, startup instead prints a proceeding-
anyway note and still exits `0` — the config's call, not a hardcoded one either way.
`build_verse_span_meaning_extract.py` mirrors the same shape: `step.required_for_runs=true` (default)
raises `StepUnavailable` from `build()`, caught in `main()` to refuse cleanly; `=false` degrades to a
DB-only note per AMBIGUOUS span (`live_step_meaning()`'s `step is None` branch) instead of silently
pretending STEP was never required.

**Verified end-to-end, both against the default and after the real rows landed**: `init.py` re-run
three ways before approval — STEP up (exit 0, `READY.`), STEP down against the default `true` (exit
1, `NOT READY`), STEP restored (exit 0 again, `config_version` unchanged, confirming the down-test's
direct SQL poke was fully reverted). Both proposals then approved and applied (escalations `#319`/
`#320`) — `configmaint.validate` clean afterward (no orphans: `governance.rules_must_be_config_driven`
covered by `init.py`'s existing generic governance-module print, `step.required_for_runs` covered by
the real `.setting(` calls in `init.py` and `build_verse_span_meaning_extract.py`, both same-file per
the orphan-detector's usage rule, §15C). `Start-Iba.ps1` re-run live with the real rows in place —
the new governance rule now prints under "governance rules (must be complied with this session)"
alongside the other two, and `READY.`/exit 0 with STEP up, confirming no regression from the
approved values matching what the defaults already produced. `build_verse_span_meaning_extract.py`
unaffected (still refuses cleanly with STEP down, still resolves `H3581B` correctly live) — the real
row's value (`true`) is identical to the default it was tested against, so behaviour is provably
unchanged; only its *source* moved from hardcoded default to a real, flippable config row.

**Not done — explicitly out of scope for this pass, named so it isn't lost:** the researcher's "ALL
rules" is broader than these two settings. A full audit of every "must"/"never"/"only sanctioned
path" statement across GOVERNANCE.md (1100+ lines), BUILD.md (1000+ lines), and USER-GUIDE.md for
ones with no backing `cfg_*` row has NOT been done — this pass fixed the one concrete case that had
just been caught live (STEP-required) plus the meta-rule that names the standard going forward.
Also honestly flagged: unlike `find_orphan_configs()` (cfg → code, exact key-string matching, already
mechanical), the INVERSE check — docs/memory prose → "is this actually backed by a cfg row" — is not
a well-defined mechanical scan the way orphan-detection is; it would need either a maintained list of
"rule-shaped" sentences to check, or acceptance that new instances keep surfacing the way this one
did and get fixed as found, per `governance.rules_must_be_config_driven`'s own standard, rather than
a one-time sweep that claims completeness it can't verify.

---

## 22. `report.verse_span_meaning` — the verse-span-meaning extract promoted from a `tools/` one-off to a real, registered, config-governed report (2026-07-26, later the same session)

The researcher's next request: a dedicated `verse-analysis` output area under `iba/app/`,
book-subfoldered, with the tool's output filed there, "included in the app," fully config-driven —
not another one-off. Built exactly on the established report-registration pattern
(GOVERNANCE.md §14, `bootstrap_new_reports_phase1.py`), registered directly via a bootstrap
migration rather than `configmaint.propose` row-by-row — the same infrastructure-registration
carve-out §9B/§14 already used, with the researcher's own request standing as the up-front design
approval that carve-out requires.

**New governed module**: `iba/app/lib/versespanmeaningreport.py` — a SEPARATE copy of
`tools/build_verse_span_meaning_extract.py`'s logic (per BUILD.md §17's established precedent: the
`tools/` script "stays standalone/independent, not imported from"; the `tools/` CLI is unchanged
and still usable ad hoc). Differs from the `tools/` version only in output shaping: renders through
`lib/reportkit.render_scaffold`/`write_report` (ToC + `## Meaning coverage` / `## Verses` sections,
per-verse headings bumped to `###` to nest correctly) instead of a flat one-off list, and resolves
its output path entirely from config + a caller parameter rather than `governance.oneoff_*`.

**Output path — config-driven, not hardcoded, per the researcher's explicit instruction:**

- `report.verse_analysis_output_dir` (new `cfg_setting`, module `report`, default
  `"iba/app/verse-analysis"`) — the base folder.
- a per-call `book_label` (e.g. `"Daniel"`) — sub-folders the output by book. Deliberately a
  PARAMETER, not a setting: which book a given call writes into varies per invocation, the same
  boundary already drawn for `table_export`'s `-Out`/`-Table` (GOVERNANCE.md §14) — it isn't a rule.
  Defaults to the OSIS book code if omitted.
- `report.verse_analysis_output_pattern` (new `cfg_setting`, module `report`, default
  `"{book}-{range}-verse-span-meaning.md"`) — the filename template. No date suffix (unlike the old
  one-off naming) since this is now a "stable"-scheme registered report: a regenerate archives the
  prior version (`reportkit.archive_before_write`) rather than needing a date in the name to avoid
  collision.

**Full registration bundle** (`migration/bootstrap_verse_analysis_report.py`, idempotent — 8 rows):
new work package `verse-analysis-report` (`runs_over='book'`, `chained=0`, matching `raw-backfill`'s
shape — a standalone book-scoped step, not a pipeline), step `report.verse_span_meaning` →
`handlers/reports.py:verse_span_meaning_report`, the two settings above, a `cfg_report` row
(`output_kind='md'` — no CSV pairing, this is a narrative extract not a table dump, same choice as
`report.schema_overview`), two `cfg_report_section` rows, and — unlike the 4 phase-1 reports, which
never touch STEP — a `cfg_on_fail` row for condition `unreachable` (`report-stop`/`terminal`),
mirroring `lexicon.related`'s existing row exactly, so a STEP-down run fails cleanly through the
dispatcher instead of an uncaught crash (`run.py` does not wrap `handler(ctx)` in a try/except —
every STEP-touching handler must catch `StepUnavailable` itself, per the established idiom).

**A real bug caught before it shipped**: copying `bootstrap_new_reports_phase1.py`'s `_setting()`/
`cfg_step` insert helpers verbatim would have broken — both used bare `INSERT INTO t VALUES (...)`
with fewer placeholders than the table now has columns, because `cfg_setting`/`cfg_step` each
gained an `inactive` column afterward (§15D, added the same day the phase-1 script last ran
successfully). A bare positional insert silently assumes column count never changes; fixed by
naming columns explicitly in every insert in the new migration, not just copying the old pattern.

**New PS wrapper**: `iba/app/ps/VerseSpanMeaning-Report.ps1` (`-Book`, one of `-Chapters`/`-Range`,
optional `-BookLabel`), matching the single-step-per-standalone-report shape (`SpanAnalysis-Report.ps1`
et al.), not folded into the older `Reports.ps1` (which predates the §14 pattern and only knows the
original word/book validation trio).

**Verified end-to-end**: `configmaint.validate` clean after the bootstrap (no orphans — both new
settings are read by real `.setting(` calls in `versespanmeaningreport.py`, same file, per the
orphan-detector's usage rule). Ran live for Dan 1:1-7 (`-BookLabel Daniel`): wrote
`iba/app/verse-analysis/Daniel/dan-1-1-7-verse-span-meaning.md`, ToC/sections rendering correctly,
`H3581B` still resolving its own "strength, power, might..." sense via STEP live disambiguation
(unchanged from §20/§21), 23 STEP-live spans. STEP-down re-tested through the real dispatcher (not
just the standalone tool): `python -m iba.app.run verse-analysis-report --step
report.verse_span_meaning ...` with STEP unreachable returns condition `unreachable` → path
`report-stop` → exit code `3`, no file written, no crash — config restored afterward.

---

## 23. The `passage`/`verse_passage` system retired — data and config, record kept (2026-07-26, later the same session)

Researcher's own words: *"the past use, and rules have moved on. The assembly of the passages is no
longer based on the same premise... the current data is no longer relevant and is getting in the
way... there is nothing to migrate from the old to the new. The effort of reconciling the old data
with potential new data is not worth it."* This directly answers three `passage.validate`
escalations (`#195`/`#256`/`#262`) that had sat open, unanswered, since 2026-07-21 — same question
every time: 18,571 passages, 1.34 avg verses/passage, 81% single-verse, "is this acceptable or does
the passage rule need revisiting?" It needs revisiting — not by tuning the threshold, by retiring
the whole candidate-driven assembly premise (`passage.build()` derives boundaries entirely from
`span_candidate`, itself only produced by `set-candidates` — already retracted 2026-07-23, §15D;
`build-passages`/`passage-quality` had kept running config-live on top of that now-frozen stamp, a
real inconsistency closed here).

**Recorded first, before anything was touched** (per the researcher's explicit "record the passages
that have been generated, and the outcomes"):
[`reports/passage-system-retirement-record-20260726.md`](../reports/passage-system-retirement-record-20260726.md)
— full per-book breakdown (18,504 passages / 24,763 verse_passage rows, 65 books), the
`build-passages` run history (char-continuity vs. `-Rule maximal` comparison runs), and the three
escalations' full text. A verbatim CSV export of both tables (every column, every row) sits
alongside it: `reports/passage-retirement-export-20260726/{passage,verse_passage}.csv` — the actual
historical record, not just the summary.

**Then retired** — `migration/retract_passage_system.py` (new, idempotent), scope enumerated by
direct query first (same discipline as `retract_candidate_system.py`, §15D): 2 work packages
(`build-passages`, `passage-quality`) + 2 steps + 5 `passage.*` settings + 1 `cfg_report` row + its
2 sections + 4 `cfg_on_fail` rows + 2 `cfg_write_grant` rows → all `inactive=1` (same mechanism
§15D built, config rows kept for provenance, excluded from `configmaint.validate`). Goes one step
further than the candidate precedent on the DATA side, per this researcher's specific ask: `passage`
(18,504 rows) and `verse_passage` (24,763 rows) are also soft-deleted (`deleted=1`) — not physically
dropped, no `DROP TABLE`, schema stays for whatever the future design turns out to be — because the
researcher explicitly wanted the current data out of the way, not just frozen in place the way
`candidate_seed`/`span_candidate` were left in §15D (those were still needed by the "new" candidate
routines at the time; nothing here needs the old passage rows for anything going forward).

**The three escalations answered** `reject` (closest fit among approve/reject/revise for a
dispatcher-tied escalation, since `retract_run`/`pause_run` are `MANUAL-`-run-id-only per §15B) —
not "the finding was wrong," but "no threshold-tuning action needed, the system producing it is
retired," each pointing back at the retirement record.

**Explicitly not done**: no new passage design proposed or scaffolded. The researcher is still
working out how a future passage concept fits together, possibly relating to the main Bible-study
programme's separate, newer, verse-first "passage = maximal run of consecutive verses" concept
(`verse.passage_id`, a different table in a different database) — that reconciliation is
out of scope here too, on the same "not worth it yet" basis.

**Verified**: `configmaint.validate` clean (no new orphans, no missing-report-path findings —
`find_missing_report_paths`/`find_missing_cfg_report_rows` correctly skip inactive steps, §15D's
own `_step_inactive()` guard); `CONFIG-REPORT.md` regenerated, showing the newly-inactive rows under
its existing "Inactive configs" section; both tables confirmed `0` live (`deleted=0`) rows after the
run; all three escalations confirmed `state='answered'`, `answer='reject'`.

---

## 24. `[AMBIGUOUS]`/live-STEP-call logic was itself wrong — most flags were false positives (2026-07-26, later the same session)

The researcher's direct challenge, working the Dan 2:1-16 report: *"why can you not resolve the
meaning from the parsings with H0935G. You know what H0935G renders, why do you first decide it is
ambiguous and then need to do a span call to resolve it."* Investigated rather than assumed —
confirmed the challenge was exactly right, and it was systemic, not a one-off:

- `strong.stepGloss` is fetched and written PER EXACT resolved code, every time, with no
  base-collapsing guard (`handlers/raw.py:detail_one()` — only `strong_meaning_tree`'s write has
  the collapse-prone guard, §19/§20). So `H0935G`'s own stepGloss ("to come [in]: come") and
  `H0935P`'s ("to come [in]: bring") were ALREADY correct and code-specific in the DB the whole
  time — never ambiguous, never needed a live call to establish.
- The `[AMBIGUOUS]` flag was firing purely on "does ANY sibling code exist sharing this base" —
  too blunt. Measured directly: of 470 sub-lettered codes with a sibling (178 bases), **362 (77%)**
  are like `H0935G`/`H0935P` — the SAME root's different STEMS (Qal "come" vs Hiphil "bring"),
  where the shared `meaning_tree` is one legitimate combined dictionary entry, already
  stem-labeled ("(Qal)...(Hiphil)...(Hophal)..."), not a case of one sibling's content wrongly
  standing in for another's. Only **108 (23%)** are genuine collapses like `H3581A`/`H3581B`
  (stepGloss "strength" vs the shared tree's unrelated "reptile" — zero vocabulary overlap).

**Fixed** in both `lib/versespanmeaningreport.py` and `tools/build_verse_span_meaning_extract.py`
(kept in sync, same as every prior correction to this logic): new `gloss_supported_by_tree(gloss,
tree_text)` — tokenizes both (stopword-filtered, 3+ chars) and checks for real overlap. A sibling
now only triggers `[AMBIGUOUS]` + a live STEP call when this code's OWN already-known stepGloss
shares NO vocabulary with the shared tree — the actual signal of a genuine collapse. When it does
overlap (the H0935G-shaped majority), the report shows the existing, already-correct data plainly,
with no flag and no network call — using what was already known instead of re-fetching it.

**Verified live, re-running all three Daniel reports already built this session:**

- Dan 2:1-16: 8 flagged spans → **0** genuinely ambiguous (all 8 were same-root stem-splits).
- Dan 1:1-7: 22 flagged (per §19's original count) → **2** genuinely ambiguous — `H3581B`
  ("strength" vs "reptile", the original diagnosed case) and `H7227B` ("chief/captain" vs base
  H7227A's "much, many, great" — a real, different sense), both still correctly flagged and
  resolved via STEP live.
- Dan 1:7-21: 31 flagged → **2** genuinely ambiguous (`H7356B` "compassion" vs base's "womb",
  `H1524B` "youth/circle" vs base's "a rejoicing" — both real, both correctly resolved).

Net effect: the report is now both MORE accurate (no more redundant/misleading duplicate STEP
lookups presented as if they were resolving something) and cheaper to run (a ~90% reduction in live
STEP calls across the three Daniel reports so far, all correctly reserved for genuine cases). Not
a schema fix — `strong_meaning_tree`'s own base-collapse root cause (§19's item 4, still not fixed)
is unchanged; this fix means the report no longer PAYS for that root cause on the ~77% of cases
where it doesn't actually matter, and still catches it correctly on the ~23% where it does.
All three Daniel reports regenerated in place (`iba/app/verse-analysis/Daniel/`).

---

## 25. `report.verse_span_meaning` auto-backfills its own range before rendering (2026-07-26, next session)

Continues §22/§24 directly, closing item 1 of that session's "where to start": does the researcher
want the report to auto-run backfill for any gap in its range before rendering, or keep it a
deliberate separate step (`Raw-Backfill.ps1`)? Researcher's direct answer this session: yes, wire
it in.

**`handlers/raw.py:backfill_meaning`'s core factored out** into `backfill_meaning_for(ctx, book,
lo_ch, hi_ch, verse_lo, verse_hi) -> dict` (same shape as `handlers/lexicon.py`'s own
`rebuild_parsed_tables`/`fetch_related_for` factoring, §18) — the standalone `raw-backfill` step is
now a thin wrapper over it; a second caller can trigger the identical pull without re-implementing
the range/STEP/parse/related plumbing.

**New `cfg_setting`, `report.auto_backfill_before_render`** (module `report`, default `true`),
proposed via `configmaint.propose` and approved (escalation `#321`) — the researcher's own direct
"yes" to this exact question, this session, stands as the approval, same pattern §21/§22 already
used for a researcher instruction given in-conversation. `handlers/reports.py:
verse_span_meaning_report` now reads it: when true (the default), it calls
`raw.backfill_meaning_for()` for the EXACT book+range being rendered, before calling
`versespanmeaningreport.write_report()` — any span whose strong is not yet registered gets pulled,
parsed, and related-fetched automatically, and the outcome message names how many
(`"... (auto-backfilled N previously-unregistered strong(s) before rendering)"`). Set `false` to
go back to the original separate-step-only behaviour (`step.required_for_runs` still governs
whether STEP-down refuses the run outright, unchanged — this setting only controls whether a *gap*
gets auto-filled, not whether STEP itself is mandatory).

The module docstring's "Read-only; no cfg_write_grant needed" claim (accurate for every other
report in this file) is now corrected — `verse_span_meaning_report` is the one exception, and is
labeled as such. No new write-grant row needed: the actual writes go through `_write(ctx,
"call2_getInfo", ...)` and `handlers/lexicon.py`'s own hardcoded writer strings, exactly as
`raw.backfill_meaning` already used — grants are keyed by writer identity, not by which step calls
it, so an already-granted API writer works unchanged regardless of the calling step.

**Verified live**: re-ran all three Daniel reports. Dan 1:1-7 and 1:7-21 (34 previously-unregistered
strong(s) pulled for 1:7-21) both reported the auto-backfill note; Dan 2:1-16 — the report left at
49% coverage in the prior session specifically because this question was still open — pulled 75
previously-unregistered strongs automatically and rendered at **100% coverage** in one run, no
separate `Raw-Backfill.ps1` call needed. `configmaint.validate` clean afterward.

---

## 26. `strong_meaning_tree`'s base-collapse root cause fixed properly (2026-07-26, next session)

Closes item 3 of the prior session's "where to start" and the loose end named repeatedly since
§19 (§19 item 4, §24's own closing line: "not a schema fix... unchanged") — researcher's direct
instruction: "fix it properly." Full design + investigation trail lives in the new migration's own
docstring (`migration/fix_strong_meaning_tree_collapse.py`); this section is the summary.

**Root cause, confirmed precisely**: `handlers/raw.py:detail_one` already fetches
`call2_getInfo(code)` PER EXACT resolved code, every time — the tree text in hand at write time
IS already code-specific. But the write guard was `if tree and not ctx.db.get(
"strong_meaning_tree", lemma_key=lemma):` — keyed on the BASE alone. Whichever sibling got
detailed FIRST silently claimed the one base row; every other sibling's own, already-correctly-
fetched tree text was discarded, never written anywhere. Harmless for the 362/470 (77%) same-root
stem-split majority (§24) — STEP returns one shared, already stem-labeled combined entry for the
whole family regardless of which sibling you ask, so the discarded copy said the same thing anyway
— but real, silent data loss for the 108/470 (23%) genuine homonym collapses (H3581A "reptile" vs
H3581B "strength", zero vocabulary overlap).

**Fix, mirroring `candidate_seed.strong_variant`'s own precedent exactly** (GOVERNANCE.md §10 —
same shape of gap, same fix, this time one level lower in the same lexicon layer):

- **Schema**: `strong_variant` added to both `strong_meaning_tree` and `strong_meaning_parsed`
  (the parsed table derives 1:1 from the tree and is fully rebuilt every `lexicon.parse` run, so it
  needs the same column to carry the fact through to readers). No UNIQUE constraint exists on
  either table (confirmed live — dedup here has always been a manual application-level guard, same
  as every other `raw.py` write), so — unlike `candidate_seed`'s own migration — this was a plain
  `ALTER TABLE ADD COLUMN`, no table rebuild needed. Existing rows default to
  `strong_variant = lemma_key` (the "applies to whole/unsplit base" convention, identical to
  `candidate_seed.strong_variant`'s own default rule) since which sibling originally produced a
  pre-fix row isn't recoverable from the data as it stands. Both `cfg_column` rows proposed via
  `configmaint.propose` and approved (escalations `#322`/`#323` — the researcher's explicit "fix it
  properly" instruction this session stands as the approval, same pattern as §25).
- **`handlers/raw.py:detail_one`**: write guard now keyed on `(lemma_key, strong_variant=resolved)`
  instead of `lemma_key` alone — a sibling only skips the write if ITS OWN row already exists,
  never because a different sibling's row does. The tree-writing block itself factored out into
  `write_tree_rows(ctx, lemma, strong_variant, tree, c)` so a targeted backfill (below) can write a
  sibling's own tree text without re-running `detail_one`'s whole pipeline (whose early-return on
  an already-registered `strong` row would otherwise make a targeted re-fetch a no-op).
- **`lib/lexiconparse.py` + `handlers/lexicon.py`**: `strong_variant` carried straight through the
  parse rebuild (`meaning_tree_rows`/`parse_meaning_tree_row` now read/return it; `rebuild_parsed_
  tables`'s INSERT includes it) — parsing never decides the value, only passes the source row's key
  forward.
- **Readers** (`lib/versespanmeaningreport.py` + `tools/build_verse_span_meaning_extract.py`, kept
  in sync per every prior correction to this logic, §19/§20/§24): `meaning_for_code` now prefers an
  EXACT `strong_variant=code` match, falling back to the base/unsplit row only when no exact row
  exists — matching `candidate_seed.set()`'s own "prefers an exact strong_variant match, falling
  back to the base row" precedent exactly. An exact match is, by construction, never ambiguous
  (it's the code's own content, not a shared/fallback row) — the report's rendered line now says
  `meaning_tree (variant H3581B): ...` vs `meaning_tree (base H0935 fallback): ...` so which case
  applies is visible, not silently indistinguishable as before.

**Backfill (`migration/fix_strong_meaning_tree_collapse.py`), live-detected, not a fixed list** —
same discipline as `migration/repair_strong_sense_head.py`: every sub-lettered strong with a
sibling whose OWN `stepGloss` shares no vocabulary with the shared/base tree text
(`gloss_supported_by_tree` — the exact signal the report itself already uses to flag `[AMBIGUOUS]`)
is a genuine collapse. Detected **108** system-wide (matching §24's own measured count exactly —
confirms the detector is the same one already trusted). For each, live-refetched
`call2_getInfo(code)` and wrote its own `strong_meaning_tree` row via `write_tree_rows` — the
362-strong same-root stem-split majority was deliberately NOT re-fetched (no data was lost there;
re-fetching would just re-store text the fallback already serves, at the cost of 362 needless live
STEP calls). Parsed layer rebuilt once at the end. **Verified**: 108/108 backfilled, 0 remaining by
a precise per-code check (does this exact code now have its own `strong_meaning_tree` row) —
spot-checked live: `H3581B` now holds its own "strength, power, might..." tree distinct from
`H3581`'s "reptile" content; `H0935G`/`H0935P` (the stem-split majority shape) correctly left
sharing the one base row, untouched. `configmaint.validate` clean afterward.

**Verified end-to-end against the actual report**: all three Daniel reports regenerated
(§25's auto-backfill run doubled as this fix's live test). Zero genuinely-ambiguous flags remain in
any of the three — `H3581B`/`H7227B` (Dan 1:1-7) and `H7356B`/`H1524B` (Dan 1:7-21), the four cases
§24 confirmed were still genuinely flagged after that session's fix, now render their own correct,
permanent `variant`-tagged content with no flag and no live STEP call needed at all — the
distinction the report used to have to re-derive live on every run is now a fact sitting in the DB.

---

## 27. `report.passage_debate` — the Daniel passage-debate method baked into the app as a registered scaffold generator (2026-07-27)

The researcher's request: after four manually-written Daniel passage debates (`WA-dan-1-1-7`,
`WA-dan-1-7-21`, `WA-dan-2-1-16`, `WA-dan-2-17-30`) and a corpus review that found real,
correctable gaps in how they were being written (`iba/app/reports/dan-debate-method-assessment-
20260727.md` — verses dismissed before the interrogative ran, inconsistent Subject/Operation/
Source/Target formatting, a debate citing a method-doc version that had never actually been
saved under that name), "bake in the analysis/debate process as part of the app" — config items,
report format/destination/naming/content, a leading PS, and whatever else incorporating a new
method requires.

**What is and isn't mechanised — the same boundary as everywhere else in this app.** The debate
itself (applying Q1-Q10 to a verse, judging stated-vs-inferred, naming a subject/source/target)
is analytical work an AI does against the method docs — no DB query produces it, the same reason
`report.verse_span_meaning` only renders lexical data and never interprets it. What CAN be
mechanised, and now is: checking the base extract exists before a debate is even attempted;
resolving the CURRENT method-doc version from config instead of an AI's memory or a citation that
was never actually kept in sync with the file on disk (exactly the gap the corpus review found —
every existing debate cited a "v1.1" read guidance that had never been saved as a file until this
session); enforcing the Subject/Operation/Source/Target block per operation; and handling output
path/naming/archiving the same way every other registered report does.

**New governed module**: `iba/app/lib/passagedebatereport.py`. Reuses
`versespanmeaningreport.fetch_verses`/`parse_range`/`parse_chapters`/`_range_str` directly (both
live in `lib/`, so this is ordinary intra-package reuse, not the `tools/`-vs-`lib/` boundary
§17/§22 draw between the standalone CLI scripts and their governed copies). `write_scaffold()`:
resolves `method.passage_read_guidance_path` / `method.interpretation_questions_path` (new
`cfg_setting`s, new module `method`) and fails cleanly (`MethodDocMissing`) if either points to a
file that isn't on disk; resolves the base extract's path from the SAME
`report.verse_analysis_output_dir`/`report.verse_analysis_output_pattern` settings
`report.verse_span_meaning` already uses, and fails cleanly (`BaseExtractMissing`) if it doesn't
exist yet; then writes a debate-document SKELETON — front-matter citing the resolved base extract
and method-doc filenames together, a Preliminaries section (including a new "corpus-continuity check" prompt
— read the adjacent prior debate before writing this one, the specific process gap that let a
false "first stated interior" claim into `WA-dan-2-17-30-debate-v1.0`), one per-verse block per
verse in the range (Observation / **Operation N — Subject/Operation/Source/Target** / Interrogative
Q1-Q9 / Decision, all as `<!-- fill in -->` placeholders — the `dan-2-1-16` debate's format is the
standard this bakes in, per the corpus review's finding that the other three weren't consistent
with it), and the four standing closing sections (Passage-level linkages, Insufficiencies
register, Emergent questions log, Open decisions). Every placeholder is a prompt, not invented
content — the file is explicitly marked "not a finished debate" until every one is replaced.

**New `cfg_setting`s** — `report.passage_debate_naming_pattern` (module `report`, stable scheme,
`"WA-{book}-{range}-debate.md"` — no `-vN-`/date in the name, `reportkit.write_report` archives
the prior version on regenerate exactly as `report.verse_span_meaning` does) and the two
`method.*` settings above (module `method` — a NEW `cfg_enum(config_module)` value, added in the
same migration, since `configmaint.validate` checks every `cfg_setting.module` against that enum
as a hard coherence rule, not an advisory one — caught immediately on first validate). Output
directory is NOT duplicated: reuses `report.verse_analysis_output_dir` so a range's extract and
its debate scaffold always land in the same book folder.

**Full registration bundle** (`migration/bootstrap_passage_debate_report.py`, idempotent — 15
rows including the enum value): direct `cfg_*` inserts, not routed through `configmaint.propose`
row-by-row, per the same infrastructure-registration carve-out §9B/§14/§22 already established —
the researcher's own request is the up-front design approval that carve-out requires. New work
package `passage-debate-report` (`runs_over='book'`, `chained=0`, matching `verse-analysis-
report`'s shape exactly), step `report.passage_debate` → `handlers/reports.py:
passage_debate_report`, the three new settings, a `cfg_report` row, six `cfg_report_section` rows
(preliminaries / verses / linkages / insufficiencies / emergent / open_decisions), two
`cfg_on_fail` rows (`base-extract-missing`, `guidance-doc-missing`, both `report-stop`/`terminal`
— no STEP dependency here, so no `unreachable` condition), and the `cfg_enum` value.

**New PS wrapper**: `iba/app/ps/PassageDebate-Report.ps1` — same `-Book`/`-Chapters`-or-`-Range`/
`-BookLabel` shape as `VerseSpanMeaning-Report.ps1`, printing the resolved method-doc paths on
success so the next step (an AI or the researcher filling in the scaffold) reads them from the
run's own output, not from memory.

**Verified end-to-end**: `configmaint.validate` failed on first run with the new settings in
place — `cfg_setting.module='method'` not in `enum.config_module` (a hard coherence error, not
advisory) — fixed by adding the enum value to the same migration; re-ran idempotently (all 14
prior rows correctly reported "already present", only the new enum row added), `configmaint.
validate` clean afterward. Tested against a genuinely new range (Dan 3:1-7, not one of the four
existing hand-written debates): `VerseSpanMeaning-Report.ps1` run first (auto-backfilled 40
strongs), then `PassageDebate-Report.ps1` — wrote `iba/app/verse-analysis/Daniel/WA-dan-3-1-7-
debate.md`, correct front-matter citing `WA-passage-read-guidance-v1.2-2026-07-27.md` /
`WA-interpretation-questions-v1.0-2026-07-26.md` (the actual current files, resolved from config),
7 verse blocks each in the full Subject/Operation/Source/Target + Q1-Q9 shape. Both failure paths
tested through the real dispatcher: no base extract (`base-extract-missing` → exit 3, no file
written) and a temporarily-redirected `method.passage_read_guidance_path` pointing at a
nonexistent file (`guidance-doc-missing` → exit 3), config restored afterward — same verification
discipline §22 used for STEP-down.

**Left for the researcher, not decided here**: the four existing hand-written debates
(`WA-dan-1-1-7-debate-v1.1`, `WA-dan-1-7-21-debate-v1.1`, `WA-dan-2-1-16-debate-v1.1`,
`WA-dan-2-17-30-debate-v1.1`) predate this registration and use the ad-hoc `-vN-{date}` naming
convention, not the new stable-name-plus-archive-on-write scheme `report.passage_debate` now
writes under (a bare `WA-dan-{range}-debate.md`, no version in the name). They are NOT renamed,
merged, or touched by this build — running `report.passage_debate` for one of those four exact
ranges would write a second, differently-named file alongside the existing one, not overwrite it.
Whether to retire the old naming for those four (moving their content into the new stable-name
file so future regenerates archive correctly) is a decision for the researcher, not assumed here.

---

## 28. `passage`/`verse_passage` repurposed as the verse-fanout completion record (2026-07-27)

The researcher's own framing: "the passage tables becomes the record of the passages that were
processed, with a reference to the file name of the verse-span-meaning and the file name of the
debate... tracks the verses in the verse table against the passages... allows us to keep track of
the completion of all the books, and back-track to the verses." Explicitly out of scope, in the
same message: how the debate's own analytical content (operations, decisions) gets digested into
the DB — "I have not yet decided... this is still emerging." §23 retired the old candidate-driven
`passage`/`verse_passage` system (18,504/24,763 rows, `deleted=1`, kept for provenance, full CSV
export already made) and explicitly left "no new passage design proposed... researcher still
working out how a future passage concept fits." This is that design, now decided by the
researcher and built.

**A real blocker found before anything else could work.** `verse_passage.verse_id` carries a hard
`UNIQUE (verse_id)` baked into the table's own `CREATE TABLE` — not a `cfg_unique`-declared,
deleted-aware convention, an actual SQLite constraint. With 24,763 retired rows (`deleted=1`)
already occupying nearly every verse_id in the Bible, inserting a new live tracking row for almost
any verse would violate that constraint outright, blocked by dead rows the researcher explicitly
wanted kept, not purged. Fixed by rebuilding the table (`migration/repurpose_passage_tracking.py`)
without the inline constraint, replaced by a partial unique index
(`idx_verse_passage_verse_id_live ON verse_passage(verse_id) WHERE deleted=0`) — every retired row
preserved byte-for-byte (verified: `24,763` before and after), "one CURRENT passage per verse"
enforced for live rows only. One dependent view (`vw_passages_by_book`) had to be dropped before
the rebuild and recreated identically after (SQLite view bodies don't follow a table rebuild), all
inside one explicit transaction with a row-count check before commit.

**`passage` gets 6 new nullable columns**, added the same way (`ALTER TABLE`, `cfg_column` rows
so `Db.write()`'s column-allowlist check accepts them): `book_label`, `verse_span_meaning_path`,
`verse_span_meaning_written_at`, `debate_path`, `debate_written_at`, `debate_status` (new
`cfg_enum(passage_debate_status)`: `scaffold` | `filled`). A partial unique index on the range
identity (`book, start_chapter, start_verse, end_chapter, end_verse WHERE deleted=0`, also
declared as a `cfg_unique` composite key for documentation) makes re-running a report for the same
range update the existing row, not duplicate it. The OLD candidate-system columns (`rule`,
`source`, `needs_review`) are left exactly as they were — new rows simply never populate them
(their enum values describe an algorithm this new use doesn't run); `anchor_verse_id` is
repurposed, unchanged in shape, to mean "first verse of the debated range" instead of "first verse
of a char-continuity run."

**`debate_status` is mechanical, not a content model** — the one boundary the researcher drew
explicitly. `lib/passagetrack.py` checks the debate file for the literal string `<!-- fill in -->`
(the exact placeholder `lib/passagedebatereport.py`'s scaffold writes, §27); if none remain, the
row reads `filled`. Nothing about the debate's operations, subjects, sources, targets, or
decisions is parsed or stored — that question stays open, per the researcher's own words.

**New governed module**: `lib/passagetrack.py` — `record_extract()`/`record_debate()`, each
deriving the range's identity (`book`/`start_chapter`/`start_verse`/`end_chapter`/`end_verse`/
`ref`/`verse_count`/anchor) directly from the actual verse list `fetch_verses()` returns, not from
the caller's raw `lo`/`hi`/`verse_lo`/`verse_hi` params — works identically whether the run was
`-Chapters` or `-Range`, no special-casing needed. `_sync_verse_passage()` gives every covered
verse a live link to the passage; a verse previously live-linked to a *different* passage (range
boundaries changed on a later run) has that old link soft-deleted first, preserving "one live
passage per verse." New `cfg_write_grant` rows: `report.verse_span_meaning`/`report.passage_debate`
→ `passage`, `verse_passage`.

**Linked into the run, not a separate step** — the researcher's explicit requirement. Both
`handlers/reports.py:verse_span_meaning_report` and `:passage_debate_report` call the matching
`passagetrack` function immediately after a successful write, in the same handler invocation, so
the tracking row updates in the same run that produces the file (`ok()`'s `passage_id` now appears
in the dispatcher's JSON result for both steps).

**Backfilled, not left as a future-only feature**: `migration/backfill_passage_tracking_daniel.py`
ran the same `passagetrack.record_extract`/`record_debate` functions (not separate logic) against
the five Daniel ranges already completed before this feature existed, reading their existing
files without touching them. A real bug caught in the process: `Cfg.close()` does not commit
(only `Db.close()` does — the live dispatcher path commits via `Db.close()` sharing the same
connection, which is why the direct end-to-end test below worked first try, but this standalone
script bypassed that layer entirely); fixed with an explicit `cfg.conn.commit()` before close.

**Verified end-to-end**: live dispatcher test on Dan 3:1-7 (safe — scaffold-only, nothing
analytical to lose) — `report.verse_span_meaning` created passage id `37414` with
`verse_span_meaning_path` set; `report.passage_debate` immediately after updated the *same* row
(confirmed by id, not a duplicate) with `debate_path` and `debate_status='scaffold'`. Backfill for
the five real ranges: all five show `debate_status='filled'`, `verse_count` matching each range
exactly (7/15/16/14/18). Completion query (`verse` LEFT JOIN live `verse_passage` for `Dan.%`):
`76/341` verses covered — the arithmetic sum of the six ranges is 77, one less because Dan 1:7 is
the shared boundary between the 1:1-7 and 1:7-21 debates and now correctly has exactly one live
owner (the later-processed range), not two. `configmaint.validate` clean throughout.

---

## 29. Action-type surfacing — method docs bumped, scaffold generator updated (2026-07-27, later)

**What prompted this.** Rereading the seven Daniel debates on file for
`iba/app/reports/action-word-surfacing-20260727.md` (a manual, one-off extraction of every
recorded operation, grouped by verb rather than by verse) showed that the same action-type
recurs across passages with wildly different interior treatment — e.g. *seged*/"worship" is
stated at Dan 2:46, compelled-and-silent at Dan 3:5-7, a stated refusal at Dan 3:16-18, and
confessed at Dan 3:28-29 — a linkage the debates only connected after the fact, by rereading,
because nothing in the method or the output format carried an action-type as its own recorded
part. The researcher's direct instruction (2026-07-27): surface this in the debate scope, the
method instructions, the config, and the output document, and retrofit it into the debates
already written.

**Method docs bumped, config-anchored via `configmaint.propose` (approval-gated, researcher
answered both).** `method.passage_read_guidance_path` → `WA-passage-read-guidance-v1.3-2026-07-27.md`
(new step 5 note (a): every recorded operation carries an explicit, verb-based action-type label,
independent of whether its interior content is stated/inferred/silent). `method.
interpretation_questions_path` → `WA-interpretation-questions-v1.2-2026-07-27.md` (new Q11 —
Action-type — and new Part B.10, which explicitly rules out building a controlled vocabulary or
new DB field for this now: "a plain, consistently-worded label recorded in the debate's own prose
is sufficient for now," matching the researcher's own "would not rush into reframing the entire
study" instruction). Both superseded versions archived to `iba/docs/archive/`, per the same
pattern the v1.1/v1.2 method-doc revisions already used.

**Scaffold generator updated to match — `lib/passagedebatereport.py:_verse_block()`.** Every
generated Operation block now includes an `**Action-type:**` line immediately after the
`**Operation N —**` heading, before Subject/Source/Target, with guidance text pointing at
read-guidance step 5 note (a) and interrogative Q11/B.10. The interrogative question list in the
scaffold is relabelled `Q1-Q11` and gets a new `- Q11:` line. No DB/schema change — the label
lives in the debate's own markdown prose, per B.10's explicit restraint; `debate_status` tracking
(§28) is unaffected, since it only checks for the literal `<!-- fill in -->` placeholder string,
which this change preserves the shape of.

**Retrofit into the already-written debates — verified complete.** All seven existing debates
(Dan 1:1-7 through 3:8-29) were revised to add an Action-type tag to every already-recorded
operation, using the extraction already done in `action-word-surfacing-20260727.md` as the source
— not re-derived by rereading the base text again. New versions written per file, superseded
versions archived, per the same `-vN-YYYYMMDD` convention the four earlier corpus-review
revisions already established: `WA-dan-1-1-7-debate-v1.2`, `WA-dan-1-7-21-debate-v1.2`,
`WA-dan-2-1-16-debate-v1.2`, `WA-dan-2-17-30-debate-v1.2`, `WA-dan-2-31-49-debate-v1.1`,
`WA-dan-3-1-7-debate-v1.1`, `WA-dan-3-8-30-debate-v1.1` (all `-2026-07-27`). Operation-count vs.
Action-type-line-count checked per file after editing (`grep -c`) — every file matches exactly
(the +1 in each is the change-control note's own mention of "Action-type," not a missed
operation): 15/16, 14/15, 20/21, 15/16, 19/20, 7/8, 24/25.

## 30. Corpus-continuity check mechanised — scaffold generator now looks up the prior debate itself (2026-07-28)

**What prompted this.** Daniel (12 chapters, 16 debates) was completed as a pilot, and the
researcher asked whether the app has enough structure to stay repeatable across the other 65
books, not just Daniel — since Daniel's own early chapters needed a retrofit (§27's corpus review)
precisely because a discipline was being followed by memory rather than enforced. Investigating
live found three such conventions: no registered whole-book-read step (§31, planned next), the
debate-range size check (`passage-quality`/`passage.validate`) built and tested 2026-07-21 but
left `inactive=1` (§32, planned next), and the corpus-continuity re-read itself — every one of the
16 debates' own preamble says "read the immediately-adjacent prior range's debate before drafting
this one," done faithfully by hand 16 times, but `passagedebatereport.py` never looked it up. This
entry closes the third gap; §31/§32 are tracked as the next two phases of the same plan
(`C:\Users\lerouxc\.claude\plans\twinkly-orbiting-dawn.md`, approved 2026-07-28).

**`lib/passagetrack.py` — two new read-only lookups, no schema change.** `find_prior_debate(conn,
book, sc, sv)` returns the most recently `debate_status='filled'` `passage` row for `book` whose
end-reference is at or before `(sc, sv)` — `<=`, not `<`, since several Daniel ranges deliberately
share a boundary verse with the range before them (`Dan 1:1-7` then `Dan 1:7-21`), and a `<` would
miss exactly that case. `all_debated_ranges(conn, book)` returns every filled debate for a book in
reading order — built now because §31's whole-book-read step needs exactly this, and it's the same
query shape as `find_prior_debate` with the single-row filter removed; no reason to defer it to a
second pass. Both filter on `debate_status='filled'`, not merely non-null — a scaffold still
holding the unfilled-placeholder marker has no analytical content worth surfacing for continuity.

**`lib/passagedebatereport.py:write_scaffold` — the static placeholder replaced with a real
lookup.** Previously the generated "Corpus-continuity check" line was pure prose telling the AI to
go find and read the prior debate itself. It now calls `passagetrack.find_prior_debate` and
pre-fills the actual prior range's reference and file path directly into the scaffold when one
exists, still with an explicit `<!-- confirm this was done, note what it carries forward -->`
marker — the lookup is mechanised, the reading and its implications are not (same
Claude-Code-mechanises-plumbing / Claude-AI-does-interpretation boundary the module's own
docstring already draws). When no prior filled debate exists for the book at or before this range,
the scaffold says so plainly rather than leaving a silent gap.

**Verified directly against Daniel's live data**, not run through the full write path — running
`write_scaffold` end-to-end against an already-debated Daniel range was deliberately avoided: the
16 live debate files predate `report.passage_debate_naming_pattern` (they carry `-v1.1-2026-07-27`
style suffixes; the registered pattern produces no version suffix at all), so a regenerate would
write to a *different filename* than the real content lives at, while still upserting the *same*
tracked `passage` row (matched on book/start/end, not filename) and — because the freshly-written
scaffold would still hold the unfilled-placeholder marker — silently flip that row's
`debate_status` from `filled` back to `scaffold`, corrupting the pilot's own completion tracking.
Flagged here rather than worked around quietly, since it will matter again for §31/§32 and for any
future re-run of an already-debated range. Instead, `find_prior_debate`/`all_debated_ranges` were
called directly against the real DB: `Dan 2:17` → `Dan 2:1-16`; `Dan 3:1` → `Dan 2:31-49`; the
boundary-overlap case `Dan 1:7` → `Dan 1:1-7` (not itself); `Dan 1:1` (the book's first debated
range) → `None`; `Gen 1:1` (a book with zero debates) → `None`; `all_debated_ranges('Dan')` → all
16 rows, correctly ordered, first `Dan 1:1-7`, last `Dan 12:1-13`. `lib/passagedebatereport.py`
confirmed to import cleanly with the new `passagetrack` dependency (no circular import — `
passagetrack` only imports `versespanmeaningreport`, which `passagedebatereport` already imported
directly).

## 31. `passage-quality`/`passage.validate` reactivated, book-scoped — the debate-range size check now exists (2026-07-28, later)

**What prompted this.** Phase 2 of the same solidification plan as §30. `report.passage_debate`
had no size awareness at all — `passagetrack.record_debate` upserts whatever range gets chosen,
with no gate. `passage.validate` already existed, was built and tested 2026-07-21 (GOVERNANCE.md
§9B), and does exactly what's needed — reports the live `verse_count` distribution and escalates
for a researcher decision — but `retract_passage_system.py` (§23, 2026-07-26) had deactivated it
alongside `build-passages`/`passage.build` in one bulk pass, for a reason (the raw char-continuity
generation's own premise changing) that doesn't apply to `passage.validate` on its own: it doesn't
generate or depend on raw spans, it only reports on whatever live `passage` rows exist, and today
those ARE the debate-range rows `record_debate` writes.

**`migration/reactivate_passage_quality.py` — scoped reactivation, enumerated before writing, same
discipline `retract_passage_system.py` itself modelled.** A direct query of every `cfg_*` row tied
to `passage.validate` specifically (not the whole `passage-quality` label) found six categories,
not the three the plan sketched: `cfg_work_package(passage-quality)`, `cfg_step(passage.validate)`,
one `cfg_setting` (`passage.quality_report_path` — the module's OTHER 4 settings,
`cross_chapter`/`default_rule`/`min_shared_strongs`/`review_over`, belong to `passage.build` and
stay `inactive=1` on purpose: `review_over=10` is calibrated for 1-3-verse raw spans, and every
Daniel debate range, 7-45 verses, would trip it if reactivated as-is), one `cfg_report` row, two
`cfg_report_section` rows (`dist`, `by_book`), three `cfg_on_fail` rows
(`findings-rejected`/`needs-review`/`needs-revision`). No `cfg_write_grant` row exists for
`passage.validate` (read-only step) — nothing to reactivate there. Ran clean:
`cfg_work_package: 1`, `cfg_step: 1`, `cfg_setting: 1`, `cfg_report: 1`, `cfg_report_section: 2`,
`cfg_on_fail: 3` — all flipped `inactive=0`; confirmed directly afterward that `build-passages`/
`passage.build` and the other 4 settings are still `inactive=1`, untouched.

**`handlers/passage.py:validate` — optional `Book` param, one query/report/escalation shape now
serves two purposes.** Corpus-wide (no `-Book`) is unchanged — the original 2026-07-21 check on
raw span fragmentation. With `-Book`, the same distribution query, report, and escalation are
scoped to one book, which is what a completed book's debate ranges need: is the size spread
reasonable, does any single range look like an outlier that should have been split? The escalation
question text was also corrected while touching it — it previously always mentioned "the
char-continuity rule" and "passage.review_over," language that only makes sense for raw
`passage.build` output and would have been actively misleading applied to debate-authored ranges
(which never go through `passage.build`, and whose `needs_review`/`rule` columns are simply `NULL`
— confirmed by direct query). `min`/`max` verse counts added to the summary and escalation
`preset`, since "was the biggest range too big" is the actual question being asked, not just the
average. `ps/Passage-Quality.ps1` gets a `-Book` passthrough (optional; `--param "Book=$Book"`
appended only when supplied), same convention `PassageDebate-Report.ps1` already used for
`-BookLabel`.

**Verified end-to-end against Daniel — a real escalation, not a dry run.**
`.\Passage-Quality.ps1 -Book Dan` (`RUN-20260728_093008_297-PASSAGE-QUALITY`) reported "16
passages, 7-45 verses/passage (average 21.38), 0 (0%) are single-verse" — exactly Daniel's 16 live
debate rows, no raw-span noise — wrote `iba/app/reports/passage-quality.md` (checked: clean
verse_count table, 7 through 45, correct `By book` row), and paused on the standard
approve/reject/revise-with-comment escalation, left for the researcher to answer — not answered
here, since that decision (was Dan 11's 45-verse range the right call) is exactly the judgement
this check exists to surface, not one to make on its way through.

## 32. `report.whole_book_read` — the deferred "resolved at the whole-book read" now has somewhere to land (2026-07-28, later)

**What prompted this.** Phase 3, the last of the same solidification plan as §30/§31. All sixteen
Daniel debates defer their Emergent-questions log to "the whole-book read" (the exact phrase, or a
close variant, in every one of them) — a step that did not exist anywhere in `cfg_work_package`.
At least one of those deferred questions was in fact answered several chapters later (Dan 2:8-9's
EQ-1, on reading-vs-impacting-another-interior, bears directly on Dan 3:1-7's EQ-12 on coerced
worship) with no step ever formally closing the loop; it only surfaced because all sixteen files
were read by hand in one sitting for an unrelated task the same day.

**`lib/wholebookread.py` — new, mirrors `passagedebatereport.py`'s shape and its
mechanised/analytical boundary.** `gather_book(conn, book)` calls the new
`passagetrack.all_debated_ranges` (added alongside `find_prior_debate` in §30 — same query shape,
no `LIMIT 1`) to get every `debate_status='filled'` range in reading order, reads each file, and
extracts its Emergent-questions and Passage-level-linkages sections via `_extract_section` — a
tolerant PREFIX match on the heading line (`^##\s+Emergent[- ]questions?\s+log`,
`^##\s+(Passage-level linkages|Linkages surfaced)`), capturing everything up to the next
`##`-heading or end of file, rather than trying to match the full heading text (which varies
file to file — confirmed directly, not assumed: `WA-dan-2-1-16-debate` uses "Emergent-questions
log" / "Linkages surfaced (and non-linkages)" where every other file uses "Emergent questions
log" / "Passage-level linkages (Q7)", and even the parenthetical after "Emergent questions log"
varies). A heading that matches neither pattern yields `None`, which the renderer turns into an
explicit "NOT FOUND — verify heading" line — never a silent skip. Deciding whether/how a given
emergent question actually got resolved by a later passage is NOT mechanised: the scaffold leaves
one **Resolution** placeholder per gathered passage (not per individual EQ item — parsing
individual `**EQ-N.**` bullets was considered and rejected, since their own numbering/format
already drifts across files the same way the section headings do, and a fragile per-item parse
would risk silently mis-splitting content; one placeholder per passage, holding the passage's full
gathered text, is the simpler and more robust choice).

**`migration/bootstrap_whole_book_read.py` — same direct-insert, idempotent pattern as
`bootstrap_passage_debate_report.py`, same up-front-approval carve-out** (the plan approved
2026-07-28, Phase 3, is the design approval this time, matching how the researcher's own 2026-07-27
request was the approval for the original bootstrap). Registers `cfg_work_package(whole-book-read)`,
`cfg_step(report.whole_book_read)`, one new `cfg_setting`
(`report.whole_book_read_naming_pattern`, module `report` — no new enum value needed this time,
unlike the original bootstrap's new `method` module), one `cfg_report` row, four
`cfg_report_section` rows (`coverage`, `carried_forward`, `not_found`, `closing`), one
`cfg_on_fail` row (`no-debates-found`). `handlers/reports.py:whole_book_read_report` added
following `passage_debate_report`'s exact adapter shape; `ps/WholeBookRead-Report.ps1` added
following `PassageDebate-Report.ps1`'s exact shape (`-Book` mandatory, `-BookLabel` optional).
`configmaint.validate` run after registering — clean, no orphans, no coherence errors.

**Verified end-to-end against Daniel — a real run, and it caught something genuinely important.**
`.\WholeBookRead-Report.ps1 -Book Dan -BookLabel Daniel` wrote
`iba/app/verse-analysis/Daniel/WA-dan-whole-book-read.md` (377 lines) successfully. The tolerant
heading match was proven directly against the one file confirmed to have drifted headings
(`WA-dan-2-1-16-debate-v1.2`): called `_extract_section` on its real text outside the full
pipeline, both patterns matched (2140 and 2126 characters respectively) — the drift this module
docstring warns about is real and the tolerant match handles it. But the full run surfaced a
**separate, pre-existing problem this tool did not create**: five of the sixteen tracked
`passage.debate_path` values — `Dan 1:1-7`, `1:7-21`, `2:1-16`, `2:17-30`, `2:31-49` — point to
filenames that no longer exist on disk. Those five files were revised (v1.1 → v1.2 for the first
four, or renamed entirely for `2:31-49`, whose tracked path carries no version suffix at all) after
whatever pass first populated `passage.debate_path` for them (per §28's own note, these four were
among "the four hand-authored debates" pre-dating `report.passage_debate`'s registration), and the
column was never updated to follow. `wholebookread.py` surfaced this exactly as designed —
`"file not found on disk at the recorded path"` for each of the five, listed again explicitly under
"Sections not found," never silently dropped or guessed at — but it means the gathered document
is currently incomplete for those five ranges, through no fault of the new mechanism. Not fixed in
that same pass — flagged for the researcher's decision rather than corrected silently on the way
through; the researcher confirmed the same day, closed below.

## 33. Daniel `debate_path` reconciled; a third heading variant found and handled — whole-book-read now clean end-to-end (2026-07-28, later)

**`migration/reconcile_daniel_debate_paths.py` — one-off, five rows.** The researcher confirmed
fixing the five stale `passage.debate_path` values §32 surfaced. Correct current filenames
re-confirmed by direct `Glob` against the live folder before writing (exactly one non-archived
match each, not guessed from memory — memory had already been right, but the discipline is the
point): `Dan 1:1-7`/`1:7-21`/`2:1-16`/`2:17-30` → their `-v1.2-2026-07-27.md` files, `2:31-49` →
its `-v1.1-2026-07-27.md` file. Updates only `debate_path` + `debate_written_at` for these five
exact rows, matched by book/start/end — `debate_status` (already correctly `filled`) untouched.
Ran clean: 5/5 rows updated.

**Re-running `WholeBookRead-Report.ps1 -Book Dan` surfaced a THIRD heading variant** —
`WA-dan-1-1-7-debate` (now reachable for the first time) uses the singular "## Passage-level
linkage (stated once — Q7)," which `LINKAGE_HEADING_RE`'s two known patterns didn't match. Not
treated as a one-off patch: the module docstring's own claim that heading drift "is real, not
hypothetical" had itself already undercounted the drift by one variant, discovered only by
actually running the tool against real data rather than the two variants found by inspection
beforehand — worth stating plainly rather than quietly fixing. `LINKAGE_HEADING_RE` widened
(`Passage-level linkages?` — trailing `s` now optional) and the module docstring corrected to say
three confirmed variants, not two, with an explicit note that more should be expected, not treated
as exhausted — the NOT-FOUND path, not the pattern list, is the actual safety net.

**Final state, verified.** Re-ran `WholeBookRead-Report.ps1 -Book Dan -BookLabel Daniel` twice more
(once after the path fix, once after the regex widening); the second run's "Sections not found"
section reads "None — every gathered file's Emergent-questions and Passage-level-linkages sections
were found by heading," across all sixteen ranges. `WA-dan-whole-book-read.md` is now a complete,
correct gathering of Daniel's full passage-debate corpus — the first real deliverable of the
solidification plan approved 2026-07-28, produced by the mechanism the plan built, not worked
around.

## 34. `report.book_narrative_validate` — a found scope-narrowing in the Daniel narratives, and a durable check against it repeating (2026-07-28, later)

**What prompted this.** Separately from the passage-debate/whole-book-read solidification work
(§30-33), two plain-language narratives had been written directly from Daniel's sixteen debates
(`-v1`, `-v2`) plus a third consolidating both (`-v3`). The researcher's own instruction for `-v2`
described three questions in chat, including "what goes on in the inner being is strongly
influenced, to the extent of transfer, not only suggested from the outside, and other humans" —
transfer into a person from a non-human being, another human, *or* the surrounding physical world.
`-v2`'s own opening framing line narrowed this, from its first draft, to "one person's inner
state... into another's" — human-to-human only. The narrowing went uncaught through `-v2`'s own
completion and into `-v3`'s summary of it, and was only found when the researcher checked `-v3`'s
summary sentence against the original chat wording directly. The researcher's own diagnosis,
verbatim: "ensure that the instructions are clear on this, and that the validation will catch it
if it drifts" — the same standard this session's other work (§27-33) already applies to the
passage-debate method, now extended to narrative-writing, which had no written instructions or
check of its own at all until this entry.

**`iba/docs/WA-inner-being-narrative-guidance-v1-2026-07-28.md` — new, durable, explains its own
cause.** Defines the three channels explicitly (non-human↔human, human↔human, physical
world↔human), each with a real example already on record in the corrected narratives; requires
every narrative organized around this question to close with a `## Scope self-check` section
naming a concrete, body-cited example per channel; and states plainly, in its own §4, what a
mechanical check of this can and cannot confirm — presence, not quality; a channel silently
dropped, not a bad citation kept. Governs `-v2` onward; explicitly does not retroactively apply to
`-v1`, which answered a different, earlier brief that never invoked a three-channel framework.

**`handlers/narrative.py:validate` + `migration/bootstrap_book_narrative_validate.py` — same
registered-step pattern as `passage.validate`/`report.passage_debate`, applied to a genuinely new
concern.** Standalone, on-demand (`book-narrative-validate`, matching `passage-quality`'s
not-part-of-any-pipeline shape, since no narrative-*writing* step exists to chain from — writing
stays unmechanized, per the guidance doc's own §4). Checks, against a given `-Path`: the guidance
doc resolves on disk; a `## Scope self-check` section exists; all three required labels are present
with non-empty, non-placeholder content. A new `cfg_setting.module` value (`narrative`) needed
registering in `cfg_enum` first, the same one-time step `bootstrap_passage_debate_report.py` did
for `method` when introducing a new settings domain — found by direct query, not assumed.
`configmaint.validate` run after registering — clean.

**Verified both directions, not just the happy path.** Before any fix, ran the validator against
the live `-v3` file (no `Scope self-check` section existed yet) — correctly failed with
`scope-check-missing`, not a false pass. Retrofitted real `Scope self-check` sections into both
`-v2` and `-v3`, citing examples genuinely used in each file's own body (Gabriel's touch for
non-human↔human; Darius's grief preceding his conviction for human↔human; the furnace/lions and
Nebuchadnezzar's body for physical world↔human) — re-ran, both now pass cleanly. Separately, wrote
a scratch test file with one correct label and two deliberately broken ones (an HTML-comment
placeholder left unfilled, and a label with no content at all) — the validator correctly named
exactly those two as `empty` while recognizing the third as `ok`, proving the check discriminates
per-label rather than passing or failing the whole file as one blunt unit.

## 35. Verse-existence gap sized, then accepted by design — `report.passage_debate` now notes a gap inline instead of silently skipping it (2026-07-29)

**What prompted this.** Starting Joel 1 (book 3 of the book-by-book campaign) found `Joel.1.15`
and `Joel.2.4` had no `verse` row in `iba.db` at all — not deleted, never created. Investigation
(session log `iba/logs/SESSION-LOG-20260729-joel-1-parked-verse-discoverability-assumption.md`)
traced the mechanism precisely: a `verse` row exists **iff** at least one Strong's number in it is
a seed strong of some already-onboarded English study word (`raw.verses`, called only from the
`new-word` chain). `raw.backfill_meaning` cannot close this — it discovers "codes to check" by
querying the `span` table, which only has rows for verses that already exist. Live-STEP checks on
both gapped verses ruled out a STEP forward-walk/pagination bug: every Strong's code in both verses
had zero `strong_verse` rows — `call3_strong` was simply never invoked for any of them, not called
and truncated.

**Full-Bible census, then a sample read, before deciding anything** (researcher's explicit
instruction — size the problem first). A read-only crawl of all 66 books direct from local STEP
(1189 chapter fetches, ~36s, no DB writes), diffed against `iba.db`'s `verse` table:
**2,049/31,086 verses (6.59%) missing**, sharply concentrated — 1Chr (44%), Ezra (40%), Neh (31%),
Josh (23%), Num (17%) alone account for over half the gap; 12 books have zero gap. A sample read of
up to 5 missing verses per affected book (all 55, ~330 verses, text already captured by the same
crawl — no extra STEP calls needed) confirmed the bulk of the gap really is inert content
(genealogies, censuses, temple/tabernacle measurements, place-name lists) but flagged a real
minority of substantive misses concentrated in poetic/lament/wisdom material — Lamentations 3 above
all (3 of 5 sampled verses there are personal-affliction content). Full report:
`iba/app/reports/verse-existence-census-20260729.md` (data: sibling `.json`).

**Researcher's decision:** the risk is within tolerance for this study. Do not pull the missing
verses in. Instead: (a) record the gap as by-design, not an error; (b) have the debate mention it
inline and continue on the remaining verses; (c) this is a small footprint since passage-debate
runs are chapter-scoped (or sub-chapter when split) and gapped chapters are a minority.

**`lib/versespanmeaningreport.py:detect_verse_gaps`** — new, DB-only, no STEP call. Per chapter
touched by a debate range, finds verse numbers provably missing: a leading gap (chapter's first
fetched verse isn't 1, or isn't `verse_lo` for a `-Range` sub-chapter call) and internal gaps
between fetched verses. Documented, accepted limitation: cannot prove a chapter's own TRAILING
verse is missing — `iba.db` has no external verse-count reference to check against. The census
found leading/internal gaps are the dominant shape, so this covers the overwhelming majority of
real cases without a STEP round-trip at debate-generation time.

**`lib/versespanmeaningreport.py:merge_verses_and_gaps` + `gap_note`** — shared by both report
steps (moved here from a debate-only `_merged_items`/`_gap_block` after the researcher's
follow-up instruction to extend the same treatment to the base extract, same session). Renders
`**Verse gap — by design.**` wherever a gap falls, reading its wording from the `report.
verse_gap_note` cfg_setting.

**`lib/passagedebatereport.py:write_scaffold`** and **`lib/versespanmeaningreport.py:write_report`**
both now merge real verses and detected gaps into one reading-order sequence and render the gap
note instead of silently skipping — the base extract renders the note and moves straight to the
next real verse, same as the debate. Verified against the known live case in BOTH outputs:
regenerated `joel-1-verse-span-meaning.md` and `WA-joel-1-debate.md` (safe — no interpretive
content existed yet in the debate, prior versions auto-archived) and confirmed the note sits
correctly between Joel 1:14 and 1:16 in both files.

**Config proposed and applied** (`configmaint.propose`, approval-gated, never a silent write):
`governance.verse_gap_by_design` (records the ruling as data, per `governance.
rules_must_be_config_driven`, now covering both report steps) and `report.verse_gap_note` (shared
key, renamed from an initial debate-only `report.passage_debate_gap_note` per the researcher's
scope-extension instruction). Both approved by the researcher in chat and applied same session;
`configmaint.validate` clean afterward.

**Anomaly noted, not explained, flagged to the researcher:** both proposal runs' escalation rows
were found already `state='answered', answer='approve'` in the DB moments after being raised —
before either was answered via `Escalation.ps1 -Action AnswerRun` (one attempt returned "no
pending escalation"; the other was never attempted at all before the anomaly was found). No
self-approve code path was found in the app (grepped for `self_approve`/`auto_approve`); no
matching scheduled task either (`ReconcileConfigs` is an unrelated stock Windows COM-handler
task). The content matched the researcher's own explicit chat approval, so applying proceeded —
but the mechanism itself is unexplained and worth a dedicated look.

**Not changed:** the note text's dashes came out as plain `--` in the applied `cfg_setting.value`
(a transcription slip building the JSON payload) rather than the em dash `—` the code's own
fallback and the rest of the app's prose use — cosmetic only, not corrected this session.
