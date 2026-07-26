# PLAN — reports fully config-governed (content, not just path) — v3

**Status: PROPOSED, awaiting researcher approval. Nothing in this plan has been built.**
**v3 — 2026-07-22, revised per researcher feedback on v2 (§9.1–9.3) — see §0.**

---

## 0. What changed from v1

v1 under-scoped this. Your comments expanded it in four ways, all folded in below:

1. **Missing reports** — 4 new reports to build (seed-candidate, strong-meaning, span-analysis,
   schema-overview) plus a 5th that already has a script but no config/registration
   (table-csv-export) — §3.
2. **Dual output** — reports that summarise a core table (registry, strong, seed, span) must write
   **both** an `.md` analysis **and** a full `.csv` table dump (with joins where related tables
   apply) — §4.
3. **Naming, versioning, archiving** — every report needs a config-driven naming convention,
   and a previous version must be **auto-archived**, never silently overwritten — §6.
4. **Notifications** — run-completion (terminal) and exception notification (terminal + a
   persisted report) are a **third thing**, distinct from the report itself, and must also be
   config-driven (wording, routing, and — for completion — must name the report so it's findable)
   — §7.

Plus your four rulings on the v1 open questions (§9): 5.1 one-off reports still don't get a
`cfg_step` row, but their format/folder/naming **does** come from config. 5.2 redefines Phase 0 —
existing reports only, content unchanged, wiring only. 5.3 — new tables are fine but must not
fragment the config store; every new table must hang off something that already exists. 5.4 — you
want to re-review this plan before anything is built.

This revision re-audited the **live app** again (not just the docs) to ground the new sections in
fact, the same way v1 did — see §3 and §4 for what that found.

**v3 changes (your §9.1–9.3 on v2):**

- **9.1 — "every PS method should have a config-driven notification, hardcoded ones adjusted."**
  Much bigger than the `cfg_on_fail` extension v2 proposed. Re-audited all 12 `.ps1` scripts —
  ~70 hardcoded `Write-Host` lines, several genuinely repeated verbatim across scripts. §7 rewritten
  with the full inventory and a design that covers all of it.
- **9.2 — "yes, existing reports should by default also have CSV."** Not just
  candidate-quality/passage-quality — applies to all 7 existing reports by default. §4/§6 updated.
- **9.3 — agreed.** §3's content proposals stand as the first cut, to be expanded once built. No
  change needed.

---

## 1. The correction this plan implements (unchanged from v1, now the settled scope)

> For **every** report: need, type, and location are config-driven (already true) **and**
> content-shape is config-driven — title, headers/section list, table of contents, footer, plus
> each report's own bespoke content on top **and** its naming/versioning/archiving **and** its
> run-completion/exception notification wording and routing. **Every report must also have a
> PowerShell command to run it, and that mapping must itself be in config.**

---

## 2. Current-state audit — every existing report (unchanged from v1)

### 2A. Registered operational reports (7) — in scope for full content-governance

| # | Report | Step (`cfg_step`) | Work package → PS script | Path setting | Content config today |
|---|---|---|---|---|---|
| 1 | `CONFIG-REPORT.md` | `configmaint.report` | `configuration-maintenance` → `Config-Maintenance.ps1` | `configmaint.report_path` ✓ | none |
| 2 | `candidate-quality.md` | `candidate.validate` | `candidate-quality` → `Candidate-Quality.ps1` | `candidate.quality_report_path` ✓ | none |
| 3 | `candidate-load.md` | `candidate.load` | `candidate-curation` → `Candidate-Curate.ps1` | **✗ none of its own** (derived path) | none |
| 4 | `passage-quality.md` | `passage.validate` | `passage-quality` → `Passage-Quality.ps1` | `passage.quality_report_path` ✓ | none |
| 5 | `log-retention.md` | **not a registered step** | **no `cfg_work_package` row** | `retention.report_path` ✓ (orphaned) | none |
| 6 | `report-{word}.md` | `report.word` | `reports` → `Reports.ps1 -Step ReportWord` | `report.output_dir`+pattern ✓ | partial (`report.show_*`) |
| 7 | `validation-{word/book}.md` | `validation.word`/`validation.book` | `reports` → `Reports.ps1` | `validation.output_dir`+pattern ✓ | partial (`validation.show_*`) |

Two confirmed gaps (still standing, Phase 0 fixes both — see §8): `log-retention.md` has no
`cfg_step`/`cfg_work_package` row; `candidate-load.md` has no path setting of its own.

### 2C. A third, newly-found unregistered tool — `export_tables_csv.py`

Re-auditing for this revision surfaced a **third** standalone tool alongside retention:
`iba/app/tools/export_tables_csv.py` (run via `Export-Tables.ps1`) — no `cfg_work_package` row, no
`cfg_step` row, no path setting. This is exactly the report the researcher's comment asked about
(§3.5 below) — it already exists, it just isn't config-governed at all yet, and it has a real bug:
**its own docstring says it dumps "both the cfg_* config store and every data table"** — confirmed
in code ([export_tables_csv.py:5,27](iba/app/tools/export_tables_csv.py#L5)), i.e. it currently
duplicates what `cfgreport.py`/`CONFIG-REPORT.md` already owns. Your suspicion was correct — this
needs fixing, not just registering.

### 2B. One-off migration/batch transcripts (8) — corrected per your 5.1 ruling

Still not given a `cfg_step` (they don't recur), **but** per your ruling their format/folder/naming
now must be config-driven too — see §5.

---

## 3. Missing reports — 5 to build, first-cut content proposed (yours to expand after)

Re-checked the live (non-config) schema — the IBA app's core data tables are:

```text
candidate_seed · lemma_inventory · passage · run · span · span_candidate · strong ·
strong_lexicon · strong_meaning_tree · strong_sense · strong_verse · verse · verse_passage ·
word_registry · word_strong · escalation · validation_result
```

"registry / strong / seed / span" (your §core-tables framing) map to: `word_registry`;
`strong`+`strong_lexicon`+`strong_sense`+`strong_meaning_tree`+`strong_verse`; `candidate_seed`;
`span`+`span_candidate`+`word_strong`.

### 3.1 `seed-candidate` — analysis of `candidate_seed`

Broader than `candidate-quality.md` (which is error/exception-focused). Proposed content: counts by
`decision`/`layer`/`role`; tag-length and lemma_key distribution; top lemma_keys by candidate
count; open vs resolved counts over time. CSV: full `candidate_seed` joined to `lemma_inventory`
(gloss, strong) — the "related table" join your comment calls for.

### 3.2 `strong-meaning` — analysis of the meaning-parse layer

`strong` + `strong_lexicon` + `strong_sense` + `strong_meaning_tree`. Proposed content: parse
coverage (how many `strong` rows have a `strong_sense`/`strong_meaning_tree` row, and how many
don't — a gap list); sense-count distribution; lexicon-field completeness. CSV: `strong_sense` +
`strong_meaning_tree` joined to `strong` (gloss/lemma).

### 3.3 `span-analysis` — analysis of the span layer

`span` + `span_candidate` + `word_strong`. Proposed content: span coverage per book/verse;
confirmed (`span`) vs candidate (`span_candidate`) counts; morph-code distribution. CSV: `span`
joined to `word_strong`/`strong`.

### 3.4 `schema-overview` — the IBA app's own data-schema snapshot

There is currently **no equivalent** of the Bible-study side's `DBSchema.json`/`build_dbschema.py`
for the IBA app's data tables (only `cfgreport.py` §8 documents the config-governed tables, not the
16 data tables above). Proposed: introspect the live DB directly (`PRAGMA table_info` / `
foreign_key_list` / `index_list`, the same primitives `build_dbschema.py` already uses on the other
DB) and produce one report covering every data table: columns, types, PK/FK, row counts. No CSV
pairing needed — this report already **is** the schema, not a table dump.

### 3.5 `table-csv-export` — already exists, needs registering + the config bug fixed

Register `export_tables_csv.py` as a proper `cfg_step` (new work package, e.g. `table-export`).
**Fix the bug found in §2C: exclude `cfg_*` tables** — confirmed, `cfgreport.py`/`CONFIG-REPORT.md`
is already the dedicated config report writer (markdown, not CSV, but it is the authoritative
config snapshot); this tool should only ever touch data tables, per the same "one owner per
concern" principle the rest of the app already follows.

---

## 4. Dual output (MD + CSV) — design

**Per 9.2: CSV output is the default for all reports**, not only the core-table ones. The `.md`
carries the **analysis** (the numbers, the gaps, the distributions); the `.csv` (one file, or one
per table when a join spans more than one) carries the **full table content, verbatim** — "I want
to see table content, not just summaries." Both write on the same run, from the same step.

Applied to the concrete list: `CONFIG-REPORT.md` pairs with a CSV of the `cfg_*` tables (which,
per §3.5, is then the reason `table-csv-export` excludes `cfg_*` — one owner, not two); the 4
core-table reports (§3.1–3.3) pair with `candidate_seed`/`strong_*`/`span_*` as designed there;
`candidate-quality.md`/`passage-quality.md` pair with `candidate_seed`/`passage`+`verse_passage`;
`report-{word}.md`/`validation-*.md` pair with the word/book-scoped slice of `span`/`word_strong`/
`verse`/`passage` (filtered by the run's own `word`/`book` param, not a full-table dump — a
per-word report pairing with every word's rows would defeat the point). **`schema-overview` (§3.4)
is the one deliberate exception** — it already *is* the schema in full, a CSV of it would just be
the same information reformatted, not "table content" in the sense you mean.

---

## 5. One-off ("investigatory") reports — config-driven format/folder/naming, no `cfg_step`

Per your 5.1 ruling: these don't recur, so they don't get a `cfg_step`/`cfg_report` row (there's no
step to key off). Proposed: a small `governance` settings group, not a new table —

- `governance.oneoff_report_dir` — default `iba/app/reports/`
- `governance.oneoff_report_naming_pattern` — default `{topic}-{YYYYMMDD}.md`, **same-day
  version bump `-v{n}`** — this is the Bible-study side's own established convention
  (`docs/file-organisation-rules.md` §2.3), not a new one invented for this app; adopting it here
  keeps the two halves of the project consistent instead of diverging.
- `governance.oneoff_report_format` — default `md`

A shared helper (`reportkit.oneoff_path(cfg, topic)`) computes the path so any future migration
script uses config instead of a literal string, without requiring a `cfg_step` registration it
doesn't need.

---

## 6. Naming, versioning, auto-archiving — for the 7+5 registered reports

Extends `cfg_report` (the table proposed in v1, unchanged core shape) with:

```sql
CREATE TABLE cfg_report (
    step          TEXT PRIMARY KEY REFERENCES cfg_step(step),
    title         TEXT NOT NULL,
    show_toc      INTEGER NOT NULL DEFAULT 1,
    footer_text   TEXT,
    output_kind   TEXT NOT NULL DEFAULT 'md+csv',   -- 'md' | 'md+csv' — 'md' is the exception now (§4), not the default
    naming_scheme TEXT NOT NULL DEFAULT 'stable', -- 'stable' (fixed filename) | 'dated'
    archive_dir   TEXT NOT NULL DEFAULT 'archive'  -- relative to the report's own folder
);
```

`naming_scheme='stable'` (CONFIG-REPORT.md, candidate-quality.md, etc. — today's fixed filenames,
unchanged): on regenerate, the **existing** file is copied to `archive_dir/` with a
`-{YYYYMMDD}-{HHMMSS}` suffix before the new one is written in place — so a run never silently
destroys the prior snapshot, but the live filename stays stable for anything that links to it.
`naming_scheme='dated'` (the word/book reports, which already carry `{word}`/`{book}` in the name):
same-day re-runs get `-v{n}` per the existing project-wide convention (§5 above), archived the same
way on a new day.

`cfg_report_csv_table` (new, only populated where `output_kind='md+csv'`):

```sql
CREATE TABLE cfg_report_csv_table (
    step        TEXT NOT NULL REFERENCES cfg_report(step),
    table_name  TEXT NOT NULL,
    join_note   TEXT,
    PRIMARY KEY (step, table_name)
);
```

Both tables key off `cfg_report.step`, which keys off `cfg_step.step` — no free-floating table, per
your 5.3 instruction.

**General file archiving (your instruction to fold `log-retention` in too):** this plan's archiving
mechanism (above) covers **report files** — the physical `.md`/`.csv` artefacts. It's a different
concern from what `lib/retention.py` measures (row-count **growth of DB tables** — `run`,
`escalation`, `validation_result` — a data-retention *policy* question `retention.py`'s own
docstring already says is deliberately not decided yet). This plan does not conflate the two, but
does make sure `log-retention.md` **the file** gets the same auto-archive-on-regenerate treatment
as every other report (it currently gets none — it's overwritten in place, same as everything else
before this plan). The DB-row retention policy question stays open, unchanged, cross-referenced
here so it isn't lost.

---

## 7. Notifications — every PS method, not just the dispatcher's ok/fail message

v2 only looked at `run.py`'s Python-level condition→message resolution. Per 9.1 ("every PS method
should have a config-driven notification... those hardcoded need to be adjusted") this revision
audited the actual terminal output — grepped `Write-Host` across all 12 `.ps1` scripts in
`iba/app/ps/`. **~70 hits.** Most of it is not report-specific at all; it falls into a small number
of repeated categories, several *verbatim-identical* across scripts (evidence this was always meant
to be one thing, not twelve copies of the same string):

| Category | Example (live, unchanged) | Where seen |
|---|---|---|
| **A. Not-initialised guard** | `"The app is not initialised. Run first:  iba\app\ps\Start-Iba.ps1"` | identical in 10 of 12 scripts |
| **B. Run header block** | `"work package : X"` / `"step : X"` / `"run_id : X"` / `"runs over : X"` | 8 scripts, same shape, minor format drift |
| **C. Per-step result line** | `"  {0,-N} {1,-M} {2}" -f step, path, message` | every step-running script — **N/M drift: -16/-18/-20 inconsistently, a real bug** |
| **D. PAUSED banner + escalation instruction** | `"PAUSED — awaiting your decision. Answer with:"` + `.\Escalation.ps1 -Action AnswerRun ...` | **verbatim identical** in Candidate-Curate (×2), Candidate-Quality, Config-Maintenance, Passage-Quality |
| **E. STOPPED banner** | `"STOPPED — $($res.message)"` | Build-Passages, Set-Candidates, New-Word |
| **F. COMPLETE + next-step hint** | `"COMPLETE — candidates set for '$Book'. Next: iba\app\ps\Build-Passages.ps1 -Book $Book"` | **genuinely per-work-package** — Build-Passages, Set-Candidates, New-Word each say something different, this is real content, not boilerplate |
| **G. Param-validation / usage errors** | `"Propose needs -Table and -Op..."`, `"AnswerRun needs -RunId and -Decision..."` | scattered, script-specific, fire **before** any run_id/Python call exists |

**Design — three mechanisms, reusing what exists, nothing free-floating (5.3):**

1. **Categories A–E are global UI templates, not per-report content.** One new `cfg_setting`
   module, `notification` (plain settings, no new table) — e.g. `notification.not_initialised`,
   `notification.run_header`, `notification.step_result_line`, `notification.paused_banner`,
   `notification.stopped_banner` — each a template string with placeholders (`{work_package}`,
   `{step}`, `{run_id}`, `{runs_over}`, `{path}`, `{message}`, `{report_path}`). This is also where
   category C's width-inconsistency bug gets fixed — one template, one width, everywhere.
2. **Category F is genuinely per-work-package** — it varies with real content (what was built,
   what to run next). Rather than a new table, **add two columns to the existing
   `cfg_work_package`** (already has `chained` — this belongs right next to it):

   ```sql
   ALTER TABLE cfg_work_package ADD COLUMN complete_message TEXT;
   ALTER TABLE cfg_work_package ADD COLUMN next_step_hint TEXT;
   ```

   `complete_message` templates the COMPLETE banner (e.g. `"passages built for '{book}'"`);
   `next_step_hint` templates the "Next: ..." line, so it can reference the *next* work package's
   own registered PS script instead of a hand-typed one (`Set-Candidates` → `Build-Passages`
   currently hardcodes the next command as a literal string — with `cfg_work_package.ps_script`
   already the source of truth for that script name, the hint can be built from it instead of
   duplicating it).
3. **Category D/E's step-specific part (not the boilerplate wording, the *routing*) still uses
   the `cfg_on_fail` extension v2 proposed** — `route` column + `condition='ok'` rows — because
   *which* steps pause vs stop vs complete is already exactly what `cfg_on_fail` decides; this
   plan only adds "and here's the message template for that path," not a new decision mechanism.

**Mechanically, so PS scripts stop hardcoding English text at all:** one new shared file,
`iba/app/ps/_lib/Notify.ps1`, dot-sourced by every wrapper (`. $PSScriptRoot\_lib\Notify.ps1`),
exposing `Write-RunHeader`, `Write-StepResult`, `Write-Paused`, `Write-Stopped`, `Write-Complete` —
each pulls its template from `notification.*`/`cfg_work_package.*` via one `python -c` call (same
pattern the existing "is the app initialised" check already uses) and renders it. Every `.ps1`
script is retrofitted to call these instead of its own `Write-Host` lines — the string literals
move out of PowerShell entirely.

**Category G — open judgement call, not decided here:** these are pre-flight *argument* validation
(fires before `run_id`/Python are even involved) — closer to `argparse`'s own usage-error text than
to a "run notification." Two ways to read your 9.1 ruling: (a) it's still a "PS method," so it's in
scope, config-drive it too; or (b) usage/help text for a script's own parameters is a different
category entirely (every CLI tool hardcodes its own usage strings) and out of scope. **I don't know
which you meant — please say**, since it changes whether Phase 1 touches ~10 more lines or not.

---

## 8. Delivery sequence — Phase 0 redefined per your 5.2 ruling (and widened per 9.1)

**Phase 0 = every existing report AND every existing notification, transitioned to config-driven
wiring, wording/content unchanged.** Your 5.2 ruling is explicit that notifications and exceptions
are part of Phase 0, not a later phase — corrected from v2, which had split them out. Nothing about
what a report says or what a script prints changes visibly in Phase 0; only where the wording lives
changes (DB config vs. hardcoded string). New reports (§3) and anything not already existing today
are later phases, built on Phase 0's scaffolding.

| Phase | What | Touches |
|---|---|---|
| **0** | **Reports:** register `retention` and `export_tables_csv` as real `cfg_work_package`/`cfg_step` rows; give `candidate.load` its own path setting; add `cfg_report`/`cfg_report_section`/`cfg_report_csv_table`; seed rows for the **existing 7 reports as-is** (current headings, filenames, `naming_scheme` matching what's true today); build `lib/reportkit.py` and retrofit all 7 generators to call it; exclude `cfg_*` tables from `export_tables_csv`. **Notifications:** add `notification.*` settings (seeded with today's literal A–E strings), `cfg_work_package.complete_message`/`next_step_hint` (seeded with today's category-F text), extend `cfg_on_fail` (`route` column + `ok` rows, seeded to match today's actual paths); build `iba/app/ps/_lib/Notify.ps1`; retrofit all 12 `.ps1` scripts to call it instead of their own `Write-Host` lines. **No visible output change anywhere** — this phase is wiring only. | migrations, `lib/reportkit.py`, `iba/app/ps/_lib/Notify.ps1`, 6 generator modules, 12 `.ps1` scripts, `run.py` |
| **1** | Build the 4 new reports (§3.1–3.4) using the Phase-0 scaffolding from day one. | 4 new generator modules |
| **2** | One-off report helper (§5) — `reportkit.oneoff_path()`, `governance.oneoff_*` settings. | `lib/reportkit.py`, settings |
| **3** | `configmaint.validate` gains coherence checks: every `cfg_step` producing a persistent report has a matching `cfg_report` row; every `cfg_work_package` has `complete_message`/`next_step_hint` set. | `lib/cfgquality.py` |
| **4** | Update `GOVERNANCE.md` (new dated section) + `BUILD.md` with the corrected, full standard. | docs |

Phase 0 is the large one — 12 PS scripts + 6 report generators + `run.py`, all touched, none of
them changing behaviour. Given the size, I'd suggest landing it as a few small, independently
verifiable commits (e.g. `Notify.ps1` + one script at a time, same pattern §8's old per-generator
retrofit already used) rather than one commit — happy to sequence it either way, your call.

---

## 9. Answers folded in, and what's still open

- **5.1** — done (§5). **5.2** — done (§8, and widened per 9.1 — notifications are in Phase 0, not
  a later phase). **5.3** — addressed throughout: still only 3 new tables
  (`cfg_report`/`cfg_report_section`/`cfg_report_csv_table`, all FK-chained to `cfg_step`); the
  §7 notification design adds no new table at all — one settings module (`notification.*`) plus two
  columns on the existing `cfg_work_package`, and reuses `cfg_on_fail`. **5.4** — this is that
  re-review.
- **9.1** — done (§7): full 12-script/~70-line audit, categorised, design proposed. **One
  judgement call still open within it** — Category G (PS param/usage-validation errors) — see §7's
  closing paragraph; I don't know if your "every PS method" ruling was meant to reach that far.
- **9.2** — done (§4/§6): CSV is now the default (`output_kind='md+csv'`), `schema-overview` the
  one deliberate exception, word/book-scoped reports pair with a *filtered* slice not a full dump.
- **9.3** — no change needed, §3 stands as-is.

**Still open, still nothing built:**

1. **§3A/§7 schema shape** — you flagged getting this right as important; does the structure now
   read correctly (3 tables for report content, 2 columns + 1 settings module + `cfg_on_fail` reuse
   for notifications), or do you want it laid out differently before it's actually schema'd?
2. **§7 Category G** — in scope or not (above).
3. **§8 sequencing** — Phase 0 is large (12 PS scripts + 6 generators + `run.py`). Land it as
   several small verifiable commits, or one pass?

---

## 10. v4 — your review-clarity concern (9.1), Category G resolved (9.2), sequencing (9.3)

### 10.1 — the maintenance/review concern (9.1)

You're not asking for a different schema — you're asking two concrete questions a non-developer
reviewer needs answered, and rightly pointing out the track record so far (retention unregistered,
`candidate-load` missing its own path, `export_tables_csv` unregistered *and* buggy — three misses
found across two audit passes) doesn't inspire confidence that config won't get missed again:

1. *"When I look at something, am I seeing everything related to it?"* — right now, one report's
   full behaviour would be spread across up to 5 places (`cfg_report`, `cfg_report_section`,
   `cfg_report_csv_table`, two `cfg_work_package` columns, `cfg_on_fail` rows, `notification.*`
   settings). Correct to flag — nobody should have to mentally join 5 tables to review one report.
2. *"Will you miss configs when building?"* — the honest answer is: the same risk that already
   produced 3 misses exists for this too, unless something **checks** for it, not just documents it.

**Fix — not a schema change, a visibility change. Two additions, both already implied by the plan,
now made explicit and mandatory (not optional polish):**

- **A per-report rollup section in `CONFIG-REPORT.md` itself.** For each registered report, one
  block showing everything that governs it — title/ToC/footer, sections, CSV pairing,
  naming/archiving, the work package's complete/next-step message, and its `cfg_on_fail` rows — in
  reading order, in one place, generated (not hand-maintained, so it can't drift). This is now a
  **Phase 0 deliverable**, not a later nice-to-have — see §11.
- **An ownership ledger** — the ANSWER to "not conflict with each other," made concrete rather than
  asserted. Every config item governs exactly one thing, nothing shares a job:

  | Config item | Governs — and only this | Lives in |
  |---|---|---|
  | `cfg_step` / `cfg_work_package.ps_script` | which step exists, which PS script runs it | existing |
  | `cfg_report.title` / `.show_toc` / `.footer_text` | the report's title, whether it has a ToC, its footer | new |
  | `cfg_report.output_kind` / `.naming_scheme` / `.archive_dir` | md-only vs md+csv, filename stability, archive folder | new |
  | `cfg_report_section` | which sections exist, heading, order, ToC inclusion | new |
  | `cfg_report_csv_table` | which tables (+ joins) the CSV half dumps | new |
  | `cfg_on_fail(step, condition)` | which PATH a condition takes + its message + route | existing, extended |
  | `cfg_work_package.complete_message` / `.next_step_hint` | the COMPLETE banner + "next command" hint for a work package | existing, extended |
  | `notification.*` settings | shared boilerplate wording (header format, paused banner, not-initialised message, result-line format) | new, settings only |

  Eight rows, eight distinct jobs, no two rows can ever disagree about the same thing because no two
  rows describe the same thing. This ledger goes into `GOVERNANCE.md` verbatim in Phase 4 (§11), not
  just this plan — so it stays a live reference, per your existing standard that guidance belongs in
  the authoritative docs, not only a chat/plan file.
- **The "will you miss it" half gets a check, not a promise.** §8's Phase 3 coherence check
  (`configmaint.validate`) already catches missing report paths (this is the exact mechanism that
  would have caught `candidate-load`'s bug had it existed sooner) — extending it to also fail
  loudly if any `cfg_step` that persists a report has no `cfg_report` row, or any `cfg_work_package`
  has no `complete_message`, is what actually prevents a repeat of the 3 misses, not documentation.

### 10.2 — Category G resolved (9.2)

Your answer clarifies the boundary I was unsure of: **parameter values/choices stay in the PS
script and its own inline help — those are not config**, full stop, regardless of how "every PS
method should have a config-driven notification" reads in isolation. That settles Category G:
**out of scope.** The usage/validation error strings (`"Propose needs -Table and -Op..."` etc.) stay
exactly as they are — hardcoded PS parameter validation, same as any CLI tool's own argument
checking. Nothing in §7 touches them. (To be precise about what §7 *does* still cover: the
run-status notifications — header, result line, paused/stopped/complete banners — which are a
different thing from parameter validation; those remain in scope as designed.)

### 10.3 — sequencing (9.3)

Confirmed — Phase 0 breaks into smaller sub-phases rather than landing as one pass:

| Sub-phase | What |
|---|---|
| **0a** | Schema: add `cfg_report`/`cfg_report_section`/`cfg_report_csv_table`; extend `cfg_on_fail` (`route` + `ok` rows); extend `cfg_work_package` (`complete_message`/`next_step_hint`); add `notification.*` settings. Seed every row from **today's actual text** — no visible change yet, nothing reads these rows. |
| **0b** | `lib/reportkit.py` (render + archive-on-write) + retrofit the 7 existing report generators, one at a time, diffed against pre-change output for byte-equivalence. |
| **0c** | Register `retention` and `export_tables_csv` as real steps; fix `candidate.load`'s path; fix `export_tables_csv`'s config-table bug. |
| **0d** | `iba/app/ps/_lib/Notify.ps1` + retrofit the 12 `.ps1` scripts, one at a time, diffed against pre-change terminal output. |
| **0e** | The per-report rollup section in `CONFIG-REPORT.md` (§10.1) + the coherence-check extensions to `configmaint.validate`. |

Each sub-phase is independently committable and revertible, matches how the earlier per-generator
retrofit in v2 was already going to work, just made explicit end-to-end now.

---

Nothing will be built until you say go — the plan reads as settled to me after this round (schema
shape defended with the ownership ledger, Category G resolved, sequencing set). Say the word and
I'll start at **0a**, or take another pass first if anything above still doesn't sit right.

Researcher comments

9.1 I do have a concern about the config overall schema, but I am not a developer, and cannot just best practice for it.  If I look purely from a maintenance and review perspective then I do have a concern that when I look at a something, that I am taking everything related to it into account, and I am also concerned that you miss configs when you build the code and need to perform tasks.  The configs must be crystal clear, not conflict with each other, and serve it purpose - to dictate how the app works.
9.2 - if I understand you correctly, you are asking of the parameters of the PS scripts should be configs. Where a parameter is used to set the choices for the PS script, and the parameter is properly explained in the PS inline documentation, then it is not a config.  The parameters itself does not have to be derived from a config. That over complicates the PS script, and I am not even sure it is feasible nor good practice.
9.3 - feel free to break of phase 0 in smaller chunks, it is a big build.