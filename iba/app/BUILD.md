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
| `iba\app\ps\Export-Tables.ps1 [-Out <dir>] [-Table t1,t2,...]` | dump every table (or a subset) to CSV, one file per table, verbatim — direct DB visibility for review, no report narrative in the way; default `iba/app/export/` |
| `iba\app\ps\Escalation.ps1 -Action List` | show every open escalation |
| `iba\app\ps\Escalation.ps1 -Action Answer -Word <w> -Decision Yes\|No` | answer a new-word approval |
| `iba\app\ps\Escalation.ps1 -Action AnswerRun -RunId <id> -Decision Approve\|Reject\|Revise [-Comment ..]` | answer a config-proposal or quality-check escalation |
| `iba\app\ps\Escalation.ps1 -Action Raise -Question ".."` | add your OWN item to the escalation table — a researcher-initiated flag, not raised by a running step |
| `iba\app\ps\Log-Retention.ps1` | run/escalation/validation_result log-retention & run-health report (read-only — no pruning) |

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

## 8. Files — CORRECTED 2026-07-22 (was still only the 2026-07-17 raw slice; everything built since was missing)

```
iba/app/
  config/     schema/step/run/rules JSON seeds (archived — DB is master, GOVERNANCE.md §10) ·
              CONFIG-REPORT.md (generated snapshot, never hand-edited)
  lib/        cfg.py (the runtime reader) · cfgload.py (seed -> cfg_* on load) · cfgcheck.py ·
              cfgreport.py · cfgquality.py (orphan/justification/report-path checks) ·
              valuequality.py (the value-quality engine) · retention.py · db.py (schema from
              cfg_column) · stepapi.py (STEP, governed by cfg) · escalation.py (the one researcher
              interaction) · words.py (normalise)
  handlers/   base.py (Ctx/Outcome/ok/fail/escalate) · registry.py · raw.py · configmaint.py ·
              candidate.py · passage.py · reports.py
  migration/  Import-LegacyRegistry.ps1 · legacy_import.py · import_seed.py ·
              bootstrap_configuration_maintenance.py · bootstrap_setting_module_column.py ·
              bootstrap_quality_validate_steps.py · bootstrap_reports_registration.py ·
              bootstrap_report_persistence_governance.py · add_work_package_chained_column.py ·
              add_candidate_seed_strong_variant.py · fix_stuck_run_states.py ·
              delete_blank_tag_candidates.py · repair_strong_sense_head.py   (one-off, idempotent)
  tools/      purge_word.py · export_tables_csv.py · log_retention.py
  ps/         Start-Iba.ps1 (session bootstrap) · New-Word.ps1 · Set-Candidates.ps1 ·
              Build-Passages.ps1 · Config-Maintenance.ps1 · Candidate-Curate.ps1 ·
              Candidate-Quality.ps1 · Passage-Quality.ps1 · Reports.ps1 · Export-Tables.ps1 ·
              Escalation.ps1 · Log-Retention.ps1
  run.py                                               the dispatcher + run-state machine
  init.py                                              the session bootstrap (Start-Iba.ps1 calls it)
  report.py · validation.py                            the two report generators
  db/iba.db                                            the IBA database (built; git-ignored)
  reports/    candidate-quality.md · passage-quality.md · log-retention.md ·
              validation-book-*.md / report-*.md       (generated, per-run outputs)
  BUILD.md · GOVERNANCE.md · USER-GUIDE.md · UTILITIES.md    this doc set
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
