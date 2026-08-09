# Debate-Run.ps1 — full read/write/rule trace — 2026-08-08

## Context

You asked to see, in detail, everything `Debate-Run.ps1` touches when it runs — every
read, every write, and every rule it depends on. This is a pure investigation (three
Explore agents traced the PowerShell orchestrator, the Python layer it invokes, and the
governance/config rules that constrain it). Nothing was changed. This file is the
consolidated findings, organised so you can audit the pipeline end to end.

---

## 0. Shape of the system

`Debate-Run.ps1` (`iba/app/ps/Debate-Run.ps1`, 237 lines) is a **pure orchestrator** — it
never touches the DB or writes a file itself. Every actual read/write happens one level
down, in Python it shells out to:

```
Debate-Run.ps1
 ├─ dot-sources  iba/app/ps/_lib/Notify.ps1              (console messages, cfg_setting reads)
 ├─ python -c ...  iba.app.init                          (readiness gate)
 ├─ python -c ...  iba.app.lib.debaterun                 (lexical-complete gate, staging path, is_ready)
 ├─ python -c ...  iba.app.lib.cfg  (Cfg.setting)         (loads the step sequence)
 ├─ python -m iba.app.run <pkg> --step <step> ...         (THE per-step dispatcher — all DB writes happen here)
 │    └─ dynamically imports the handler named in cfg_step.handler:
 │         iba.app.handlers.passage:build
 │         iba.app.handlers.operations:hib_set / phenomenon_set / operation_set / closing_set
 └─ python -m iba.app.tools.build_debate_report            (final report render + one passage UPDATE)
```

Single DB for everything: `iba/app/db/iba.db`, constant defined once at
`iba/app/lib/cfg.py:35`. Config is **never read from JSON at runtime** — only from
`cfg_*` tables in that DB (`cfg.py:1-9`).

---

## 1. Control flow, in order

1. **Setup** (`Debate-Run.ps1:91-98`) — strict mode, `$env:PYTHONUTF8='1'`, optional
   `$env:IBA_TRACE='1'` (`-Trace` switch), `cd` to repo root, dot-source `Notify.ps1`.
2. **Readiness gate** (`:100-104`) — `iba.app.init._config_loaded()` +
   `_data_tables_exist()`; not-ready → `Write-IbaNotInitialised`, exit 1.
3. **Param validation** (`:106-109`) — exactly one of `-Chapters`/`-Range` required
   (hardcoded XOR check), else exit 1.
4. **Scope setup** (`:111-117`) — builds `runId` (`RUN-yyyyMMdd_HHmmss_fff-DEBATE`,
   hardcoded format), `scope`, `scopeLabel`, `scopeToken` (`:` → `_` for filename safety).
5. **Step-1 hard gate — lexical completeness** (`:124-144`) — calls
   `debaterun.lexical_complete_for_scope()`: fetches every live verse in the chapter
   scope, checks each has a live `verse_lexical` row. Incomplete, or zero
   live verses (verse-gap-by-design, `governance.verse_gap_by_design`) → prints the
   missing verses and a hint to run `VerseLexical.ps1`, exit 1.
6. **Load sequence from config** (`:147-152`) — `Cfg.setting('passage.debate_run_sequence', [])`.
   Empty/missing → exit 1. This list is what actually drives the step order.
7. **`-Step` filter** (`:153`) — if given, narrows the sequence to that one step and
   suppresses the final auto-render.
8. **Per-step loop** (`:162-221`), for each `{work_package, step}` in sequence
   (default order: `hib.set → passage.build → phenomenon.set → operation.set → closing.set`):
   a. Resolve staging path via `debaterun.staging_path()` (config-pattern-driven).
   b. Check `debaterun.is_ready()` — if the step's target scope is already satisfied in
      the DB, print "skip" and `continue` (the only silent-skip path in the whole pipeline).
   c. If not ready and the staging JSON doesn't exist → print the expected path, exit 1
      (no DB write ever attempted).
   d. Otherwise invoke `python -m iba.app.run <pkg> --step <step> --run-id <runId>
      --param Book=... --param PayloadPath=<stagingPath> [Chapters/Range/BookLabel]`.
   e. Inside that subprocess (`run.py:run_step`, see §1 sub-section below) the handler
      runs, writes to the DB, and returns a JSON result + exit code. PS reads it:
      - exit 2 (`pause-continue`) → `Write-IbaPaused`, `$exitCode=2`, **break loop**.
      - exit 3 (`report-stop`) → `Write-IbaStopped`, `$exitCode=3`, **break loop**.
      - exit 0 → next step.
9. **Auto-render** (`:223-235`) — only if the loop finished with `$exitCode==0` **and**
   no `-Step` was given (full sequence completed through `closing.set`): runs
   `python -m iba.app.tools.build_debate_report --book ... --chapters|--range ...
   [--book-label ...]`, prints "COMPLETE".
10. `exit $exitCode` (`:237`).

### Inside `run.py:run_step`, per step invocation
Fresh `Cfg()` → dispatch gate (refuses if work package/step inactive or step has no
`cfg_step.kind`, raising `PermissionError`) → `Db(cfg)` → resolve handler from
`cfg_step.handler` → `_ensure_run` (new run → DB snapshot unless `IBA_NO_SNAPSHOT=1`,
insert `run` row, pre-snapshot to `validation_result`) → call handler → on exception:
rollback, write `crash` escalation, mark `run` failed, re-raise → on return: map
`outcome.condition` through `cfg_on_fail(step, condition)` to a `path`
(`ok`/`pause-continue`/`report-stop`/…), act accordingly, commit, return JSON;
`PATH_EXIT = {ok:0, report-continue:0, self-heal:0, pause-continue:2, report-stop:3}`
(hardcoded dict) sets the process exit code.

### Inside each handler (`hib_set`/`phenomenon_set`/`operation_set`/`closing_set`/`build`)
Load+validate payload → resolve/validate references → `_reconcile()` (classify each
payload item as unchanged/changed/new/removed against live DB rows; unreconciled rows
or missing `reconciliation_note`/`reason` raise `ReconciliationError`) → check
`cfg_quality_check` attestations on new/changed items (missing → clean fail, zero
writes) → cascade-guard any `removed` item for live dependents (refuse if found) →
grant-check every table about to be written against `cfg_write_grant` → write rows via
real per-row CRUD (not blind soft-delete-reinsert, since the 2026-08-08 revision) → log
every mutation to `debate_change_detail` → commit → write a Markdown reconciliation
report → return `Outcome`.

---

## 2. Every file read

| # | Path | Reader |
|---|---|---|
| 1 | `iba/app/ps/_lib/Notify.ps1` | dot-sourced, `Debate-Run.ps1:98` |
| 2 | `iba/app/db/iba.db` | every `Cfg()`/`Db()` call, throughout |
| 3 | Staging payload JSON — `iba/app/staging/operations/{book_lower}-{scope}-{step}.json` (pattern from `cfg_setting.passage.debate_staging_path_pattern`) | `handlers/operations.py:122-132` (hib/phenomenon/operation/closing), `handlers/passage.py:74-84` (passage.build) |
| 4 | Prior report files (glob'd for versioning, not parsed) | `lib/reportkit.py:127-152, 303-317` |
| 5 | `.py` source of every module imported (static) | `lib/cfg.py`, `lib/db.py`, `lib/stepapi.py`, `lib/words.py`, `lib/dbsnapshot.py`, `handlers/base.py`, `handlers/passage.py`, `handlers/operations.py`, `lib/passagetrack.py`, `lib/debateaudit.py`, `lib/reportkit.py`, `lib/versespanmeaningreport.py` |
| — | Config seed JSON | **never read at runtime** — only `cfg_*` DB tables are live |
| — | `BUILD.md`/`GOVERNANCE.md` headings | only if `iba.app.init` runs as `__main__` — dormant on this path (Debate-Run.ps1 only imports two functions from it) |

---

## 3. Every DB read (table / exact SQL, by module)

**`lib/cfg.py` (`Cfg`, used everywhere)** — `cfg_setting`, `cfg_table`, `cfg_column`,
`cfg_index`, `cfg_unique`, `cfg_enum`, `cfg_connection`, `cfg_api`, `cfg_write_grant`,
`cfg_step`, `cfg_work_package`, `cfg_book_order`, `cfg_candidate_rule`, `cfg_meta`,
`cfg_on_fail` — one SELECT method each, exact statements at `cfg.py:64-229`.

**`lib/debaterun.py`** — `lexical_complete_for_scope` (verse_lexical), `hib_ready`
(verse_hib), `operation_ready` (phenomenon, operation), `closing_ready`
(passage_linkage / passage_insufficiency / passage_emergent_question /
passage_validation_note counts) — `debaterun.py:93-167`.

**`lib/versespanmeaningreport.py:fetch_verses`** (shared) —
`SELECT id, osisId, reference, text FROM verse WHERE osisId LIKE ? AND deleted=0`
(`:62-64`), filtered in Python for exact scope.

**`lib/passagetrack.py`** — `_find_live_passage`:
`SELECT * FROM passage WHERE book=? AND start_chapter=? AND start_verse=? AND
end_chapter=? AND end_verse=? AND deleted=0` (`:45-47`).

**`run.py`** — `run` row lookup, per-table `COUNT(*)` snapshot over every `cfg.tables()`
entry, idempotent `escalation` lookups, `cfg.sequence(package)` (`cfg_step`).

**`handlers/passage.py:build`** — verse fetch, HIB-count-per-verse, tracked-passage
lookup, overlap check against `verse_passage`/`passage` (`passage.py:121-158`).

**`handlers/operations.py`** (all 4 debate writers) — `hib`, `hib_referent_option`,
`verse_hib`, `phenomenon`, `operation`, `operation_party`, `passage_linkage`,
`passage_insufficiency`, `passage_emergent_question`, `passage_validation_note`,
`verse_passage`, `cfg_quality_check`, `cfg_enum` — full statement list at
`operations.py:136-1376`.

**`tools/build_debate_report.py`** — re-reads everything the handlers wrote (verse,
hib, phenomenon, operation, operation_party, passage_linkage, passage_insufficiency,
passage_emergent_question, passage_validation_note, verse_hib control total) plus
`cfg_write_grant` for its own write permission — `build_debate_report.py:103-319`.

---

## 4. Every DB write (table / exact statement, by module)

**`run.py`** — `INSERT` into `validation_result` (pre/post snapshot), `run`,
`escalation` (crash / pause-continue / report-stop types); `UPDATE run SET
state=...` (failed/paused/done) and `resume_point`.

**`handlers/passage.py:build`** — retires overlapping `verse_passage`/`passage` rows
(soft-delete), `UPDATE passage` (correction in place) or `INSERT INTO passage` (new,
`rule` hardcoded `"input-scope"`, `source` hardcoded `"passage-build"`), `INSERT INTO
verse_passage` per verse. Every mutation logged to `debate_change_detail`.

**`handlers/operations.py:hib_set`** — soft-delete cascade on remove
(`hib_referent_option`→`verse_hib`→`hib`); `UPDATE hib`/`INSERT INTO hib`; real
per-ordinal CRUD on `hib_referent_option`; insert/soft-delete on `verse_hib`. Logged to
`debate_change_detail`.

**`handlers/operations.py:phenomenon_set`** — soft-delete on remove; `UPDATE`/`INSERT
phenomenon`; phase-gate `UPDATE passage SET phenomena_complete_at=...` (NULL to
re-open, or a timestamp on completion). Logged.

**`handlers/operations.py:operation_set`** — soft-delete cascade (`operation_party`→
`operation`); `UPDATE`/`INSERT operation`; real per-role/ordinal CRUD on
`operation_party`. Logged.

**`handlers/operations.py:closing_set`** — per-section real CRUD (soft-delete /
in-place update / insert) across `passage_linkage`, `passage_insufficiency`,
`passage_emergent_question`, `passage_validation_note`; optional `UPDATE passage SET
open_decisions_note=...`. Logged.

**`tools/build_debate_report.py`** — its *only* write: `UPDATE passage SET
debate_path=?, debate_written_at=?, debate_status=? WHERE id=?` — gated on
`cfg_write_grant('report.debate','passage')`; if the grant is missing it still renders
the file but skips this UPDATE and prints a NOTE.

All writes go through `Db.write`/`upsert`/`update` and are preceded by a
`_may()`/`_grant()` check against `cfg_write_grant` — an unlisted table raises
`PermissionError`, caught by `run.py` as a crash (rollback + escalation).

---

## 5. Every file write

| Writer | Path template | Governing config key |
|---|---|---|
| `dbsnapshot.snapshot()` | `iba/app/db/snapshots/iba-<UTC ts>-<reason>.db` | `retention.snapshot_keep_count` = **20** (live) |
| `operations.py` reconciliation reports (hib/phenomenon/operation) | `{report.verse_analysis_output_dir}/{book_label}/{step}-reconciliation-{scope_label}.md` → versioned `-v{n}-{YYYYMMDD}.md` | `report.verse_analysis_output_dir` = `iba/app/verse-analysis` |
| `hib.set` by-type report | `.../{book_label}/hib.set-by-type-{book}.md` | same |
| `closing.set` reconciliation | `.../{book_label}/closing.set-reconciliation-{book}-{passage_id}.md` | same |
| `build_debate_report.py` final render | `.../{book_label}/{book_lower}-{chapters|ch-vlo-vhi}-debate-report.md` → versioned | `report.verse_analysis_output_dir`, `report.version_on_regenerate` = **true** |

`Debate-Run.ps1` itself never writes a file — console output only
(`Write-Host`/`Write-IbaNotInitialised`/`Write-IbaStepResult`/`Write-IbaPaused`/
`Write-IbaStopped`, from `Notify.ps1`). This filing convention (book-scoped, not flat
under `iba/app/reports/`) was itself the subject of a same-day fix — see §8.

---

## 6. Config (`cfg_*`) rules the run depends on

| Key / table | Live value | Effect |
|---|---|---|
| `cfg_setting.passage.debate_run_sequence` | 5-step list (hib.set → passage.build → phenomenon.set → operation.set → closing.set), each tagged with its work package | **Drives step order entirely**; empty/missing halts the run |
| `cfg_setting.passage.debate_staging_path_pattern` | `iba/app/staging/operations/{book_lower}-{scope}-{step}.json` | Exact staging-payload path the script looks for |
| `cfg_setting.passage.debate_session_chapter_guideline` | `3` | Advisory max chapters/session (post token-blowout incident) |
| `cfg_setting.report.verse_analysis_output_dir` | `iba/app/verse-analysis` | Root of all filed reports |
| `cfg_setting.report.version_on_regenerate` | `true` | Every report write is versioned+archived, never silently overwritten |
| `cfg_setting.governance.verse_gap_by_design` | — | Missing verses are by-design, not an error; both extract and debate note gaps inline and skip on |
| `cfg_setting.governance.past_precedent_investigation_signals_missing_config` | — | If running debate requires reverse-engineering precedent from history/output files instead of a live `cfg_step`/`cfg_setting` row, STOP — that's a missing-config signal, not a puzzle to solve |
| `cfg_step` (handler / kind / inactive, per step) | table in §1 | Names the actual Python function dispatched; inactive/missing kind → hard refuse |
| `cfg_work_package.inactive` / `.chained` | both active | Inactive → refuse dispatch; `chained` controls whether `run.state` flips to `done` mid-sequence |
| `cfg_on_fail(step, condition)` | **only one row exists**: `passage.build/no-candidates → report-stop` | Every other failure condition across all 5 handlers has no row, so defaults to `report-stop` — **every non-"ok" outcome is currently a hard stop**, none configured as pause-continue or self-heal |
| `cfg_write_grant(writer, table)` | per-writer table list (§4) | Enforces every write; missing grant = crash |
| `cfg_quality_check(step, required=1, active=1)` | 17 active rows across the 5 steps | Every new/changed payload item must carry a non-empty attestation string per row, or the whole call fails clean before any write |
| `cfg_enum('hib_kind')` / `cfg_enum('operation_decision')` | — | Payload values outside the enum fail clean; an *empty* active enum skips the check entirely (treated as "not yet approved," not "nothing valid") |
| `cfg_method_rule` | 37 active rows, 6-9 per writer | The analytical/CRUD rules themselves (see §8) — cited by `source_doc` back to the two WA method docs |

---

## 7. Hardcoded rules (NOT config-driven — code-level literals)

- `-Chapters`/`-Range` mutual exclusivity (PS boolean XOR).
- `-Step` parameter's `ValidateSet` (5 step names) — hardcoded in PowerShell,
  independent of whatever `cfg_setting.passage.debate_run_sequence` actually contains;
  a config-side rename wouldn't be reflected here without also editing the script.
- Run-id format `RUN-yyyyMMdd_HHmmss_fff-DEBATE`.
- `:` → `_` scope-token substitution (duplicated between PS and `debaterun.py`,
  acknowledged in-code as intentional).
- Exit-code semantics (2=paused, 3=stopped) and `run.py`'s `PATH_EXIT` dict.
- `passage.build`'s `rule="input-scope"` / `source="passage-build"` literals (module
  docstring notes this is a deliberate retirement of older `passage.*` config settings).
- Per-step natural-key matching logic for reconciliation (HIB by `label`; phenomenon by
  `(verse, hib_label, ordinal)`; operation by `(verse, hib_label, phenomenon_ordinal)`;
  closing.set lists by `ordinal`) — Python logic, not data.
- `closing_set`'s `LIST_QUALITY_PREFIX` and `ROW_COLUMNS` dicts (section→column
  mapping).
- `lib/cfg.py:24-28` `_VERSION_TABLES` — the fixed list of `cfg_*` tables hashed into
  `config_version`; **known gap**: several newer `cfg_*` tables (`cfg_quality_check`,
  `cfg_method_rule`, `cfg_report*`, `cfg_change_detail`) are not included.

---

## 8. Governing rules from docs/config (the "why", not just the "what")

**USER-GUIDE.md §12b** (rewritten 2026-08-07) — authoritative operator description:
two-tool pipeline (`VerseLexical.ps1` once per book, then `Debate-Run.ps1` per
chapter/range); per-step contract (check done → look for staging payload → else stop
and print expected path, payload authored by the AI in-session, never hand-typed);
auto-render on `closing.set` success; new cascade-refusal conditions
(`hib-has-dependent-phenomena` etc.); `report.passage_debate`/`Chapter-Generate.ps1`
explicitly retired in favour of this DB-first model.

**GOVERNANCE.md §33** — any reconciling writer must preserve a row's id across a
`changed` correction and refuse a `removed` correction while a live dependent exists.

**GOVERNANCE.md §34** — full per-row CRUD audit trail is mandatory for all 5 debate
writers, via `debate_change_detail` + `lib/debateaudit.py:log_change` (direct
researcher quote: *"full CRUD is required for all table update controls"*).

**Two method documents govern the analytical content** (pinned by
`cfg_setting.method.passage_read_guidance_path` / `method.interpretation_questions_path`):
- `iba/docs/WA-passage-read-guidance-v1.5-2026-08-02.md` (Steps 1-6)
- `iba/docs/WA-interpretation-questions-v1.4-2026-08-02.md` (Parts A/B/C) — most
  `cfg_method_rule` rows cite a specific step/part/item from these two docs as
  `source_doc`.

**37 `cfg_method_rule` rows** carry the actual analytical rules per writer (e.g.
`hib.set`: presumptive-candidate, non-human-scope, referent-crux-resolution;
`phenomenon.set`: phase-separation, hidden-behind-act, silence-is-a-finding,
hib-still-warranted; `operation.set`: four-parts, source-vs-enablement,
divine-mirroring-anchored; `closing.set`: linkages-q7, debate-quality-validation,
open-decisions) — each with a `source_doc` and, where mechanically enforced, an
`enforced_by` code pointer.

**Most recent same-day history** (2026-08-08, per session logs — relevant because it
explains *why* the current CRUD/filing shape exists):
- `hib.set` was rewritten from whole-book to scope-only reconciliation to match the
  other 3 writers; full-CRUD audit extended to all 5 writers, catching a real
  `operation_party` count bug; a real orphaned-`hib_id` bug in Dan 8 found and repaired
  only after explicit approval.
- Report filing for all 4 debate writers + the final render was found flat-filing under
  `iba/app/reports/` instead of the book-scoped `iba/app/verse-analysis/{book}/`
  convention every sibling module uses — fixed, 41 pre-existing files retrofitted via
  `git mv`, one dangling `debate_path` flagged (not auto-fixed).
- 2026-08-07: first-ever complete Dan 1 run surfaced a real bug — the loop variable
  `$step` collided case-insensitively with the `-Step` parameter, so the final-render
  condition was silently always false; fixed by renaming to `$stepName`. Researcher's
  verdict on that run: "does not meet expectation, suitability under review."

---

## 9. Error handling / escalation model

- **Silent skip** — only when `debaterun.is_ready()` is already true for a step (prints
  "skip", continues). The only silent path in the whole pipeline.
- **Hard stop, no DB record at all** — missing staging file, lexical-incomplete
  pre-flight, empty run-sequence config, app not initialised: all exit 1 from
  PowerShell before Python's `run.py` is ever invoked; no `escalation` row is written.
- **Clean fail inside a handler** → `condition != "ok"` → `cfg_on_fail` lookup → (no row
  exists for almost every condition) → defaults to `report-stop` → `escalation` row
  (idempotent per run+step) + `run.state='failed'` + PS exit 3, "STOPPED". Nothing
  partially written — validation and grant-checks happen before any row is touched.
- **`pause-continue`** exists as a code path but none of the 5 debate steps currently
  route to it (no `cfg_on_fail` row sends them there) — only `passage.validate` (not in
  this sequence) calls `escalate()`.
- **Uncaught exception** (e.g. missing write-grant) → rollback first, then `crash`
  escalation, `run.state='failed'`, re-raise — surfaces to PowerShell as a genuine
  script error, distinct from a clean stop.
- **Cascade guards** refuse a `remove` outright if live downstream rows still reference
  it, before any row is touched.
- **Reconciliation gate** (`_reconcile`) raises `ReconciliationError` on any unaddressed
  pre-existing row, any `changed` item missing a `reconciliation_note`, or any `remove`
  missing a `reason` — zero rows written.
- **Quality-check gate** raises `QualityCheckIncomplete` if a required
  `cfg_quality_check` attestation is missing on a new/changed item — before any write.

---

## Sources

Three parallel Explore-agent traces (PowerShell layer, Python layer, governance/config
layer), each reading the actual files in full: `iba/app/ps/Debate-Run.ps1`,
`iba/app/ps/_lib/Notify.ps1`, `iba/app/lib/{cfg,db,debaterun,stepapi,words,dbsnapshot,
passagetrack,debateaudit,reportkit,versespanmeaningreport}.py`, `iba/app/run.py`,
`iba/app/handlers/{base,passage,operations}.py`, `iba/app/tools/build_debate_report.py`,
`iba/app/init.py`, `iba/app/GOVERNANCE.md`, `iba/app/BUILD.md`, `iba/app/USER-GUIDE.md`,
`iba/app/config/export/cfg_*.csv` (live DB export), and the three most recent
`iba/logs/SESSION-LOG-20260808-*.md` / `20260807-*.md` files.
