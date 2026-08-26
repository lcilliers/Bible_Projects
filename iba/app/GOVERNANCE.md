# GOVERNANCE.md — how the app is governed by config (overview + history)

> **Start at [`CHARTER.md`](CHARTER.md) first** — the researcher's own statement of what this app
> is *for* (the single driver of all operational work in this project). Everything below describes
> the mechanism; `CHARTER.md` is the objective the mechanism serves.

> **What this file is for.** This is an OVERVIEW of the *mechanism* by which config governs the
> code — how the store works, how a rule changes, what's enforced vs. still a convention. It is
> **not** the place a rule's current value lives — that's always a `cfg_*` DB row, and the live
> snapshot of every one of them is [`iba/app/config/CONFIG-REPORT.md`](config/CONFIG-REPORT.md)
> (auto-regenerated, never hand-edited). **If this file and the live config ever disagree, the
> config wins, always** — a stale sentence here is a documentation bug, not a reason to doubt the
> config. §1–§8 below are the standing overview; §9 onward is a dated history of increments (kept
> for provenance, cross-referenced by `BUILD.md` and elsewhere — section letters are not
> renumbered even as new ones are appended).
>
> **Rewritten 2026-07-22** (researcher instruction: bring this file current, and make sure no
> governance rule exists only here — it must be in config too). This pass found and fixed two real
> drifts between this doc and the live app (§5, §6.1) and extended §7/§10's file lists to match
> 2026-07-21/22's work, which had gone un-recorded here. See §11 for what changed and why.

---

## 1. The two corrections (2026-07-17, still the foundation)

1. **Config lives in the DATABASE.** The JSON files are the human-editable **seed**;
   `cfgload.py` validates and writes them into `cfg_*` tables in the DB; the running app reads
   **only** from those tables (via `cfg.py`), never from the JSON. (As of 2026-07-21, the DB itself
   is master over the seed — an archived JSON is a one-time completeness reference only, never a
   reload source; see §10.)
2. **The rules ARE the config.** Every choice the code used to make — what to filter, which API
   may write which table, what happens on a failure, the dedup key, the status flow — is a row in
   a `cfg_*` table. The code reads it and enforces it. **The code decides nothing.**

---

## 2. The config store — 20 `cfg_*` tables in `iba/app/db/iba.db`

**CORRECTED 2026-07-23** — was stale at 17, and named a table (`cfg_api_source`) that has never
existed in the live schema.

| table | holds | fed from |
|---|---|---|
| `cfg_table` · `cfg_column` · `cfg_unique` | the schema — every data table and column, with `use`/`expectation`/`source`/`filled_by` | originally `schema.json`; the DB is master now (§10) |
| `cfg_enum` | the controlled vocabularies | ditto |
| `cfg_connection` · `cfg_api` | STEP: connection + the 3 routes. **may_source** (which api may write which table) is NOT its own table — `cfgload.py` translates each API's `may_source` list straight into `cfg_write_grant` rows at load time; enforcement reads `cfg_write_grant`, keyed by writer=API name, the same table `configmaint.propose`'s own write-grant check uses. *(Corrected 2026-07-23 — this section, §3, and §4 all previously named a `cfg_api_source` table that does not exist in the live schema; found by querying `sqlite_master` directly, not by re-reading this doc.)* | ditto |
| `cfg_work_package` · `cfg_step` | the run sequence + each step's handler + scope + `chained` (§10, 5G); `cfg_work_package` also carries `complete_message`/`next_step_hint`/`paused_message` (§13) | ditto |
| `cfg_setting` | scalar rules, always module-attributed (`cfg_setting.module`, enum `config_module`) | ditto |
| `cfg_on_fail` | the fork: `(step, condition) → path` (report-stop / pause-continue / report-continue / self-heal), plus `route` (terminal vs terminal+report, §13) | ditto |
| `cfg_status_flow` | which step sets which status | ditto |
| `cfg_book_order` | the canonical OSIS book order (see §5 — this used to be code, it is config now) | ditto |
| `cfg_candidate_rule` | the candidate-seed domain ruleset (its own dedicated table, not `cfg_setting` — §5F) | ditto |
| `cfg_write_grant` | which writer may write which table (data or `cfg_*`) — data writers AND api `may_source` writers both live here | added with `configuration_maintenance`, §9A |
| `cfg_report` · `cfg_report_section` · `cfg_report_csv_table` | a report's title/ToC/footer/naming/archiving, its sections, and its CSV pairing — read by `lib/reportkit.py` | added §13 (2026-07-22) |
| `cfg_meta` | config_version + bookkeeping | — |
| `cfg_change_log` | whole-reload audit events | — |
| `cfg_change_detail` | row-level audit of every `configmaint.propose` write (table/op/where/set/before/applied_at) | added §9A |

**Live counts, 2026-07-23:** 904 rows across the 20 tables above; `cfg_setting` alone holds 66 rows.
(Also found while re-verifying this count: `cfg_table`'s own declared data-table list wrongly
includes `cfg_change_detail` — a config-store table masquerading as a data table, so
`Start-Iba.ps1`'s "data tables present" count reads 18 instead of the true 17. Not fixed in this
pass — a `configmaint.propose` deleting that one `cfg_table` row is the correct fix; named here so
it isn't lost.)

**Every value, right now:** [`CONFIG-REPORT.md`](config/CONFIG-REPORT.md) — settings by module (§2),
STEP APIs (§3), every work package's steps (§4), the full `on_fail` fork table split into
escalates/doesn't (§5), write grants (§6), status flow (§7), the full schema (§8), enums (§9), book
order (§10), and the change-log (§11). **Read that for values. Read this file for how the
mechanism works.**

**Reload the config:** `python -m iba.app.lib.cfgload`. **Rebuild the data tables from it:**
`python -m iba.app.lib.db --reset`. Neither is how you change a *rule* — see §3A.

---

## 3. The chain — where each part reads config

```
New-Word.ps1            reads the SEQUENCE from the DB (cfg_step) — not from JSON, not from the script
   │  per step:
run.py (dispatcher)     reads the STEP's handler + scope (cfg_step)
   │                    resolves the outcome's CONDITION -> PATH (cfg_on_fail)
handlers (raw/registry) read every rule from cfg:
   │                      · seed filter          cfg_setting discovery.particle_pattern
   │                      · follow relatedNos?    cfg_setting discovery.follow_related   (false)
   │                      · meaning split marker  cfg_setting meaning.head_marker
   │                      · may this api write?   cfg_write_grant  (ENFORCED at every write)
   │                      · the status to set     cfg_status_flow
   │  using:
Step (stepapi)          reads connection, routes, cap, walk bounds, particle pattern, span_html from cfg
Db (db)                 builds the data tables from cfg_column;
                        write() rejects any column not in cfg_column;
                        upsert() takes its dedup key from cfg_unique
```

Measured (2026-07-17, `new-word`): one run = 1,041 config reads across its 7 steps — `columns` 323 ·
`may_source` 321 · `unique_key` 316 · `setting` 42 · `connection` 21 · `route` 11 · `step` 7. Turn it
on: `New-Word.ps1 -Trace`, or `IBA_TRACE=1`.

---

## 3A. Changing a rule — the ONE sanctioned path

**`iba\app\ps\Config-Maintenance.ps1 -Step Propose`** is the only sanctioned way to change a
`cfg_*` row — DB-direct, single-row, **approval-gated, never silent**. Full mechanism: §9A. In
short:

```powershell
iba\app\ps\Config-Maintenance.ps1 -Step Propose -Table cfg_setting -Op update `
    -Where '{"key":"passage.review_over"}' -Set '{"value":"12"}' `
    -Question "Raise passage.review_over from 10 to 12 — why, what it affects."
# -> PAUSED, run_id printed.
iba\app\ps\Escalation.ps1 -Action AnswerRun -RunId <run_id> -Decision Approve|Reject|Revise|Hold|Noted [-Comment ...]
# then re-run the SAME Propose command with -RunId <run_id> to act on the answer.
```

Coherence-checked before it ever reaches you (unknown table/column, bad enum, invalid JSON, a
`cfg_setting` insert missing `module`); only on **Approve** does the write commit, logged to
`cfg_change_detail`. **Hard technical enforcement** that *only* this path may write a `cfg_*` row
(vs. it being the one sanctioned path by convention) is not built — named in §6.

---

## 3B. Doc/output archaeology is a STOP signal, not a workaround (`governance.past_precedent_investigation_signals_missing_config`, 2026-07-30)

**What prompted this.** Asked to run the book-by-book passage-debate process for Micah, an AI
session found that `report.passage_debate` writes a scaffold and nothing ever flips
`passage.debate_status` from `scaffold` to `filled` once the researcher/AI fills in the content —
no registered step covers that transition. Instead of stopping and naming the gap, the session
read `BUILD.md`'s history and diffed archived output files from Jonah/Joel/Obadiah to reverse-
engineer how those books' debates must have reached `filled`, and was about to quietly repeat
whatever it inferred. The researcher's own words: *"you literally looked back at the completed
work, never really looked at config, and from your observations about the past re-assembled the
correct approach. That is exactly why, over the lifetime of this 7 months study, we never got a
consistent result... The app must first be completed, config loaded, then the instruction can be
resubmitted."*

**The rule, `cfg_setting` (module `governance`), committed via `configmaint.propose`
(escalation #409, approved 2026-07-30):** the moment running an already-registered instruction
requires investigating *how it was done in the past* — reading `BUILD.md`/session-log history,
diffing prior/archived output files, or otherwise reverse-engineering a missing step from
precedent — instead of a live `cfg_step`/`cfg_setting` row telling you directly what to run and
what rules apply, that investigation IS the signal a required config/mechanism is missing. Stop
immediately; do not proceed by reconstructing the missing rule from precedent and presenting it as
the standard process. Close the gap first (register the missing step/setting, build its code, per
§9B's `configuration-maintenance` pattern and `governance.build_md_on_code_change`/
`governance.governance_md_on_rule_change`), validate config clean, then resubmit the original
instruction.

**Closing this instance.** The same session built `passage.debate_sync` (BUILD.md §53) —
a registered step that re-checks an already-written debate file for the fill-in-placeholder marker
and updates `passage.debate_status` accordingly, without silently regenerating or guessing. This
is the config-driven mechanism that should have existed before Jonah/Joel/Obadiah were debated;
those books' own `filled` rows predate it and were not touched retroactively (out of scope of this
fix — a separate question if their provenance ever needs auditing).

---

## 4. Proofs it is real, not decorative

**A · `may_source` is enforced.** `call1_meanings` may write only `word_strong` (`cfg_write_grant`).
Attempting `call1 → strong` is **blocked**:
```
PermissionError: may_source violation: api 'call1_meanings' may not write 'strong'
```

**B · A rule change in the DB changes behaviour, no code touched.** Set
`cfg_on_fail(registry.exists, word-exists).path` from `report-stop` to `report-continue` in the DB
→ the dispatcher reads the new path and no longer stops on a duplicate word.

**C · The data tables are the config's.** `db.build` reads `cfg_column` to `CREATE TABLE`; a
handler that tries to write an undeclared column is rejected by `write()` against `cfg_column`.

**D · `write_grant` is enforced on `cfg_*` writers too.** `configmaint.propose` itself must hold a
grant on the table it's changing (`cfg_write_grant`), checked in `propose()` before the coherence
check even runs — the config governs changes to the config.

---

## 5. The one boundary: facts vs rules — CORRECTED 2026-07-22

**This section was wrong.** It used to name two examples of "facts, not choices, so they stay in
code": the canonical OSIS book order, and the shape of STEP's `<span>` HTML. **Neither is true any
more, and checking live code (not just re-reading the doc) is what caught it:**

- **Book order is `cfg_book_order`** (§2), read via `cfg.book_order()` (`lib/cfg.py`), populated by
  `cfgload.py`, used by `stepapi.py`'s forward-walk. Moved into config at some point after this
  section was written; nothing recorded the move here.
- **STEP's span shape is `cfg_setting step.span_html`** (`iba/app/lib/stepapi.py`:
  `self.span_re = re.compile(cfg.setting("step.span_html"))`), not a hardcoded pattern.

**What genuinely still is code, checked directly, 2026-07-22:**
- `handlers/raw.py:BASE_RE` — the `^([HG]\d+)([A-Z]?)$` split of a Strong's code into (base,
  sub-letter). Notably, `cfg_setting candidate.lemma_base_pattern` holds the **identical pattern**
  for the `candidate` module — so the same fact is expressed once in code (raw) and once in config
  (candidate), not "one rule, one home." Not fixed in this pass — named here so it doesn't hide.
- The STEP HTTP client's request/response shape itself, SQLite as the storage engine, and
  Python/PowerShell as the implementation languages — genuinely not choices this app makes.

**The principle stands, the examples were just stale — a fact is something nobody chooses (the
canon's structure, a wire format); a rule is a choice (a cap, a filter, a path), and the direction
of travel has been to move every rule that started in code into config, on request, as the
occasion arose. Nothing enforces that migration happening promptly — it's opportunistic, which is
exactly how book order and span_html went undocumented here.**

---

## 6. What is still stubbed (honest) — CORRECTED 2026-07-22

- **SUPERSEDED 2026-08-20 (`BUILD.md` §153) — the new-word approval escalation described below is
  GONE, not just revised.** `registry.create` is a standard operational routine, not a development/
  design control (the researcher's own distinction, drawn after a 79%-of-all-escalation-rows volume
  review found `registry.create` alongside `configmaint.propose`/`validate` as routine pipeline
  plumbing crowding out genuine issues). `handlers/registry.py:create()` no longer raises an
  escalation or pauses the run at all — a new word is created `'approved'` directly, in one call;
  its outcome (including the old duplicate/typo warning) is logged via `run.outcome`, the engine's
  own standard-run log. `Escalation.ps1 -Action Answer -Word ...` is dead for this handler.
  *(Historical text below, left for provenance — describes 2026-07-22 through 2026-08-19 behaviour,
  not current.)*
  - **The approval escalation for a new word is REAL, not stubbed** (correcting this section's prior
    claim). `handlers/registry.py:create()` raises a genuine `registry.create` escalation and pauses
    the run; the researcher answers `Escalation.ps1 -Action Answer -Word <w> -Decision Yes|No`
    (confirmed live: escalation `#169`, `[blindness (spiritual]`, currently open). What remains a
    named, deliberate fast-follow (per §9A) is only the **answer shape** — still yes/no, not yet the
    three-way approve/reject/revise every other escalation in this app uses. *(Historical note, left
    as-is per researcher decision 2026-08-17, escalation #664: the vocabulary itself has since moved
    on — see §39 and `BUILD.md` §115–117 for the current `type`/`next_action`/`state` model.)*
- **`source` / `filled_by`** are in `cfg_column` but not yet *enforced* — `validation.py` only
  checks a column's `source` is non-empty (informational WARN), not that the value it holds
  actually matches what its declared source says fed it. `expectation` IS enforced (value-quality
  + `enum.*`, §9F). `use` remains documentation only.
- **Hard technical enforcement** that *only* `configmaint.propose` may write a `cfg_*` row (vs. it
  being the one *sanctioned* path by convention) is named as Layer-2 work, not built.
- **base / cluster / analytics** remain out of scope; this is still the raw + base(candidate/passage)
  slice — no `span_analysis`/interpretive-layer table exists.
- **`reconciliation with the heavyweight `iba/config` configurator`** — unchanged, still open. This
  app runs its own lightweight `cfg_*` config; `iba/config/*.json` is a separate, more elaborate,
  **not-yet-loadable** design (no loader, nothing reads it). Whether/how the two converge is not
  decided. See `iba/config/README.md` (rewritten 2026-07-22 to say this plainly) and
  `iba/docs/iba-app-design-precedence-and-structure-v1-20260721.md` §2 item 5.

---

## 7. Files — current inventory (corrected/extended 2026-07-23; §11 has the increment-by-increment version; §15A has the script-folder consolidation)

```
iba/app/
  config/    schema/step/run/rules seeds (archived, DB is master, §10) · CONFIG-REPORT.md (generated,
             incl. §12 per-report governance rollup) · archive/ (auto-archived prior CONFIG-REPORT.md
             snapshots) · export/ (CONFIG-REPORT's own cfg_* CSV pairing — git-ignored)
  lib/       cfg.py (reader) · cfgload.py (seed->DB) · cfgcheck.py · cfgreport.py · cfgquality.py ·
             valuequality.py · retention.py · dbsnapshot.py · db.py · stepapi.py · escalation.py ·
             words.py · reportkit.py (§13, shared report scaffold + archive-on-write, extended to
             CSV writes §15A, + CSV pairing) · seedreport.py · strongreport.py · spanreport.py ·
             schemareport.py (§14, the 4 new reports) · registryreport.py (§15A, registry
             evaluation report, escalation #272)
  handlers/  base.py · registry.py · raw.py · configmaint.py (CFG_TABLES whitelist fixed §15A —
             cfg_report/cfg_report_section/cfg_report_csv_table were missing despite already having
             write_grant) · candidate.py · passage.py · reports.py
  migration/ Import-LegacyRegistry.ps1 · legacy_import.py · import_seed.py · allocate_strongs.py ·
             apply_semantic_allocation.py · build_base_all_books.py ·
             bootstrap_configuration_maintenance.py · bootstrap_setting_module_column.py ·
             bootstrap_quality_validate_steps.py · bootstrap_reports_registration.py ·
             bootstrap_report_persistence_governance.py · add_work_package_chained_column.py ·
             add_candidate_seed_strong_variant.py · add_candidate_seed_referent_columns.py ·
             fix_stuck_run_states.py · delete_blank_tag_candidates.py · repair_strong_sense_head.py ·
             bootstrap_report_content_governance.py · bootstrap_retention_table_export_registration.py ·
             bootstrap_new_reports_phase1.py · bootstrap_oneoff_report_naming.py   (§13-15)
  tools/     purge_word.py · export_tables_csv.py (archive-on-write §15A) · log_retention.py ·
             _apply_verse_plaintext_column.py · build_span_heatmap_v1.py (both relocated from
             iba\scripts\, §15A)
  ps/        Start-Iba.ps1 · New-Word.ps1 · Set-Candidates.ps1 · Build-Passages.ps1 ·
             Config-Maintenance.ps1 · Candidate-Curate.ps1 · Candidate-Quality.ps1 ·
             Passage-Quality.ps1 · Reports.ps1 · Export-Tables.ps1 · Escalation.ps1 · Log-Retention.ps1 ·
             SeedCandidate-Report.ps1 · StrongMeaning-Report.ps1 · SpanAnalysis-Report.ps1 ·
             SchemaOverview-Report.ps1 · create-iba-view-template.ps1 ·
             create-passage-view-and-export.ps1 · create-passages-by-book-view-and-export.ps1 ·
             export-iba-config-tables.ps1 · generate-iba-db-schema-report.ps1 (5 relocated from
             iba\scripts\, §15A) · _lib/Notify.ps1 (§13, shared terminal-notification rendering)
  run.py · report.py · validation.py · init.py
  db/iba.db · db/snapshots/ (pre-run rollback snapshots, §12 — git-ignored)
  reports/   candidate-quality.md · passage-quality.md · log-retention.md · candidate-load.md ·
             seed-candidate.md · strong-meaning.md · span-analysis.md · schema-overview.md ·
             validation-*.md / report-*.md (generated) · archive/ (auto-archived prior versions,
             incl. CSVs since §15A) · export/ (per-report CSV pairing AND table-export's dump since
             §15A, consolidated from two separate export folders into one — git-ignored)
  archive/   non-report historical files (new, §15A) — e.g. the superseded pre-restructure
             `New-Word.ps1` stub found in the (now-removed) `iba\ps\` folder
  BUILD.md · GOVERNANCE.md · USER-GUIDE.md · UTILITIES.md   (this doc set)
  PLAN-reports-config-governance-v1-20260722.md · SESSION-LOG-20260722-reports-config-governance.md
```

Full run-command reference (kept current in `BUILD.md` §2, not duplicated here).

---

## 8. This document's own currency — the rule this rewrite exists to satisfy

Per the researcher's 2026-07-22 instruction — *no governance rule may exist only in this file* —
two settings encode the discipline that keeps `BUILD.md`/`GOVERNANCE.md` matching the app, as real
`cfg_setting` rows (module `governance`), proposed via §3A like any other config change:

| key | states | status |
|---|---|---|
| `governance.build_md_on_code_change` | any code change under `iba/app/**` must update `BUILD.md` in the same unit of work | **LIVE** — approved and applied 2026-07-22 (escalation `#238`) |
| `governance.governance_md_on_rule_change` | any governance/config-rule change must be set in `cfg_*` first, then `GOVERNANCE.md` updated to match, same unit of work | **LIVE** — approved and applied 2026-07-22 (escalation `#239`) |

This section update — done in the same reply as approving `#239` — is the first real exercise of
the rule it records.

Like `governance.reports_must_persist` (§9E), a *stated* standard is not the same as an *enforced*
one: nothing today checks that a code change actually touched `BUILD.md`, or that a `cfg_*` change
actually touched `GOVERNANCE.md`. Building that check (most plausibly a `configmaint.validate`
addition comparing `BUILD.md`/`GOVERNANCE.md`'s file mtime against the newest file under
`iba/app/**` excluding the docs themselves, and against `cfg_change_log`'s latest `loaded_at`) is
named here as follow-up work, not done in this pass — consistent with §6's honesty convention:
declare it, don't pretend it's enforced until it is.

---

## 9A. `configuration_maintenance` — the utility that governs the governor (added 2026-07-21)

Rule c names this utility explicitly: config changes must go through it, and it tracks every
change. Until 2026-07-21 it didn't exist as a registered utility — `cfgload.py`/`cfgcheck.py`/
`cfgreport.py` were standalone scripts nothing else in the app knew about, and (found by directly
running them) `cfgload.py`'s JSON-seed path had been stale since the 07-19 config→configurator
restructure, so **no config change had actually been loadable since 2026-07-18**. Also resolved
that day: the DB (not any JSON file, old or new) is master — old/archived seed JSONs are a
one-time completeness reference only, never a reload source (see
`iba/docs/project_iba_db_is_master_over_legacy_json_seeds`-equivalent ruling, and
`iba-configuration-maintenance-layered-design-v1-20260721.md`).

**Now a registered work package**, `configuration-maintenance` (`iba/app/ps/Config-Maintenance.ps1`),
three independent steps (not a fixed pipeline — you pick which to run):

| step | handler | what |
|---|---|---|
| `configmaint.validate` | `handlers/configmaint.py:validate` | read-only coherence check of the LIVE `cfg_*` tables (schema FKs, may_source, handler resolution, on_fail paths, status flow, regex settings, report fields) — ports `lib/cfgcheck.py`'s checks from JSON dicts to the DB |
| `configmaint.propose` | `handlers/configmaint.py:propose` | **the only sanctioned path that may change a `cfg_*` row.** DB-direct (no file round-trip), single-row, and **approval-gated — never silent.** Coherence-checks the proposed change, then escalates and pauses; the researcher answers **approve / reject / revise-with-comment** (three-way, not yes/no — a standing rule for every escalation in this app, per the researcher: *"the data presented to approve must be representative... approve / not approve / resubmit with an opportunity to provide a comment"*). Only on `approve` does the write commit. |
| `configmaint.report` | `handlers/configmaint.py:report` | regenerate `iba/app/config/CONFIG-REPORT.md` — a full markdown snapshot of every `cfg_*` table. Auto-chains after an approved `propose` when `configmaint.auto_report` is true. |

**Schema additions this required:** `escalation.comment` (a real column addition, `ALTER TABLE`)
and a third `answer` value (`escalation_answer` enum: approve/reject/revise) — supports the
three-way rule for *any* escalation, though only `configmaint.propose` uses it so far;
`registry.create`'s word-approval is still yes/no, a deliberate fast-follow, not done in this pass.
`cfg_change_detail` — a new, small data table recording every row `propose` actually applies
(table/op/where/set/before/applied_at) — `cfg_change_log`'s existing shape only ever recorded
whole-reload events, with nowhere to say *what* changed; that gap is what `cfg_change_detail` closes.

**Bootstrap note:** `configuration_maintenance` cannot register itself through itself (the same
reason `cfgload.py`'s `CFG_DDL` is the one hard-coded schema bootstrap in the app) — its own
`cfg_work_package`/`cfg_step`/`cfg_setting`/`cfg_write_grant`/`cfg_on_fail` rows and the schema
additions above were written directly by
`iba/app/migration/bootstrap_configuration_maintenance.py` (idempotent, run once), approved by the
researcher via direct review of the design document rather than through the (not-yet-existing)
`propose` mechanism. Every `cfg_*` change from here on goes through `propose`.

Tested end-to-end 2026-07-21: `validate` (clean pass), `report` (first `CONFIG-REPORT.md` ever
generated), and `propose`'s full cycle — approve/reject/revise/insert/update/delete, plus the
write-grant and coherence-check rejections — all via a harmless, fully cleaned-up self-test row.

**Review pass, same day: module ownership + cross-table consistency + anti-catch-all rule.**
The researcher asked for three things on `validate`, all built and tested:

1. **Global step-name uniqueness** — `cfg_step`'s PK is `(work_package, step)`, which would
   silently allow two work packages sharing a step name; `escalation`/`cfg_on_fail` both match on
   `step` alone, so that would collide at runtime. Now a hard coherence error in `validate`.
2. **Orphan-config detection** — a `cfg_setting` key or `cfg_enum` group not referenced (as a
   literal string) anywhere in `iba/app/**/*.py`. Advisory, not a hard fail (a config can be
   legitimately pre-staged ahead of a not-yet-built step). Immediately found two real defects:
   `configmaint.report_path` was itself unused by `report()` (fixed same pass — it now actually
   drives the output path), and `passage.cross_chapter` is pure documentation — `handlers/passage.py`
   never reads it, and (found separately, reviewing `validation.py`) its own "passages do not cross
   chapters" check is *also* hard-coded rather than config-driven. The check excludes
   `iba/app/migration/*.py` from its scan — those scripts exist to *write* a setting's initial
   value, so they always mention its name; counting that as "usage" masked the real orphans at
   first (`configmaint.auto_report`/`reference_seed_dir` — the former is genuinely only consumed
   from `Config-Maintenance.ps1`, not Python).
3. **`cfg_setting` must not become an untracked catch-all.** The researcher's rule: *"there must
   be a very good reason why a config goes into settings, rather than the specific module or
   utility."* Built as: (a) a new `cfg_setting.module` column (`ALTER TABLE`, bootstrapped the same
   way as `escalation.comment`/`cfg_change_detail` — see below), governed by a new `config_module`
   enum (`registry`/`raw`/`step`/`report`/`candidate`/`passage`/`configmaint`/`validation`/
   `governance`/`retention`) so module values can't drift/typo; (b) `configmaint.propose` now
   *requires* `module` on every new `cfg_setting` row and rejects an unknown value before it ever
   reaches escalation; (c) `MODULE_DEDICATED_TABLE` (currently just `candidate` → `cfg_candidate_rule`)
   — a proposed `cfg_setting` row for a module that already has its own purpose-built table gets a
   mandatory "NEEDS JUSTIFICATION" warning prepended to the escalation's `question`, so the
   judgement call is part of the *representative payload* the researcher actually approves, not a
   separate, skippable step.

Backfilling the 26 pre-existing settings' `module` values required actually verifying each
setting's real consumer by grep, not trusting its key prefix — several didn't match (e.g.
`discovery.particle_pattern` is prefixed "discovery" but is read by `stepapi.py`'s `Step` class,
not `raw.py`; `registry.strip_ends_pattern` is read by `lib/words.py`, not `handlers/registry.py`).
Also found in this pass: `iba/app/validation.py` — a whole separate raw/base-layer quality-and-
completeness reporting utility (`iba/app/reports/`), invoked manually, not yet registered as a
work package, and not accounted for in any earlier module inventory.

---

## 9B. Escalation consistency — the whole app audited, not just one rule (2026-07-21, same day)

Asked to add an escalating rule for `span_candidate`, the researcher's sharper point: *"it seems
that you are not familiar with escalation and that make we question how many other rules do we
have that is linked to escalation."* Audited every condition app-wide rather than answer for just
the one rule — **before this pass, only 3 of 15 defined conditions actually escalated**
(`raw.discover`/zero-strongs, `registry.create`/needs-approval, `configmaint.propose`/
needs-approval); everything else was `report-stop` (hard block) or `report-continue` (silent
continue), and the `configmaint.validate` advisory checks built earlier the same day didn't even
fit that taxonomy — a fourth, unsanctioned "silent counts blob" pattern.

**Fixed, all in one batch** (`iba/app/migration/bootstrap_quality_validate_steps.py` — direct, not
routed through `configmaint.propose`, per the researcher's explicit instruction not to approve
infrastructure registration row-by-row):

- `configmaint.validate`'s orphan/needs-justification findings now escalate (`needs-review`)
  instead of sitting silently in `Outcome.counts`.
- **Two new standalone quality checks**, each its own work package (not tied to every
  `set-candidates`/`build-passages` run — see below for why):
  - `candidate-quality` / `candidate.validate` — `span_candidate.candidate_tag` null/format and
    `lemma_key`→`strong` resolution. Checked the live data before building: 17.7% of rows already
    have a null tag (normal — only the historical `import_seed.py` migration ever set one) and
    52.3% have a `lemma_key` with no `strong` row yet (also normal — `strong` grows per registered
    word; the candidate seed is deliberately independent of the registry). **Neither is hard-blocking
    — both escalate**, one escalation per invocation with counts + samples, not one per row.
  - `passage-quality` / `passage.validate` — reports the live verse-count distribution (measured:
    18,571 passages, avg 1.34 verses/passage, 81% single-verse) so the researcher can judge it
    against the still-open passage-rule question, rather than inventing a threshold.
  - **Deliberately NOT added as steps inside `set-candidates`/`build-passages`'s existing sequence**
    — at 17.7%/52.3%/81% prevalence, escalating on every single book build would be pure noise,
    training a reflexive approve rather than a real decision. Standalone, run when the researcher
    wants the picture (`Candidate-Quality.ps1`, `Passage-Quality.ps1`).
- **Reclassified** `raw.detail`/no-vocab and `raw.verses`/shortfall from `report-continue` to
  `pause-continue` — the latter is exactly the class of bug `BUILD.md` §5 already documents finding
  (STEP's forward-walk silently under-returning); continuing past a shortfall without asking was
  the same risk, unnoticed.
- **`CONFIG-REPORT.md` §5 rebuilt** so the researcher can see, at a glance, what escalates and what
  doesn't (§5a/§5b split, with a leading count) — the "easily review the rules" requirement.

Tested 2026-07-21: both new checks run end-to-end via their PS wrappers and correctly escalate with
real, current data (not synthetic) — both left genuinely paused for the researcher's actual decision,
not auto-answered.

**Three live escalations pending after this session's work** (none auto-answered — genuine
researcher decisions, not infrastructure): `candidate.validate`'s tag/lemma_key findings,
`passage.validate`'s verse-count distribution, and `configmaint.validate`'s own orphan/
needs-justification findings (which, now that it escalates instead of returning silently,
immediately surfaced for the first time). `Escalation.ps1 -Action List` shows all open ones — the
one PS front door for `lib/escalation.py` (§9D; every other governed operation already had one).

---

## 9C. Reports registered + config-governed (2026-07-21, same day — Phase 2)

`report.py` (word-raw) and `validation.py` (raw + base-layer quality) were standalone scripts,
invoked directly, outside the dispatcher — the same "no other module knows this exists" gap
`configuration_maintenance` closed for `cfgload`/`cfgcheck`/`cfgreport`. Now a registered work
package, `reports` (`iba/app/ps/Reports.ps1`, step-selection): `report.word`, `validation.word`,
`validation.book` — thin adapters (`handlers/reports.py`) over the same `generate()`/
`generate_book()` functions, unchanged logic.

**Config added — output location and content, for both:**
- `report.*` (already had content fields) gained `report.output_dir`/`report.output_pattern` — the
  output path was hard-coded before.
- `validation.*` had **zero** config before this — added `validation.output_dir` and seven
  section-inclusion toggles (`validation.show_health`/`show_delta`/`show_integrity`/
  `show_references`/`show_expectations` for the word report; `show_health`/`show_candidate`/
  `show_passages` for the book report), so any section can be turned off without touching code.

**Deliberately out of scope:** `migration/build_base_all_books.py` — a one-off batch transcript,
not an ongoing operational report; registering it would be scope creep beyond what was asked.

---

## 9D. `Escalation.ps1` — the one PS front door `lib/escalation.py` never had (2026-07-21)

Researcher's correction: *"the instruction python -m iba.app.lib.escalation list does not run in
ps. the rule is all user driven methods must be encapsulated in PS and added to the project
documentation."* Every other governed operation (config-maintenance, candidate/passage quality,
reports) has had a PS wrapper from the start; answering an escalation never did — `registry.py`'s
own docstring, and every "PAUSED" message this session's new code printed, told the researcher to
run raw `python -m iba.app.lib.escalation ...` directly. Fixed: `iba/app/ps/Escalation.ps1`
(`-Action List | Answer | AnswerRun`) is now the one sanctioned front door; every place that used
to print the raw command (`configmaint.py`, `Config-Maintenance.ps1`, `Candidate-Quality.ps1`,
`Passage-Quality.ps1`, `registry.py`'s docstring, `BUILD.md`'s run-command table) now points at it
instead. Tested end-to-end (list, and a full propose→pause→AnswerRun→resume→apply→cleanup cycle)
via the PS wrapper only, no raw `python -m` invocation.

`Escalation.ps1` later (§10) gained `-Action Raise` for a researcher-initiated item not raised by
any running step.

---

## 9E. Report persistence — a standard violation, found and fixed, then codified (2026-07-21)

Asked where the new quality-check configs direct their output (terminal or file) and what the
app's standard is: `report.py`/`validation.py`/`cfgreport.py` all write a persistent `.md`, matching
`CLAUDE.md`'s project-wide "output always goes to a file, never chat/terminal-only" rule —
but `candidate.validate`/`passage.validate`/`configmaint.validate`'s advisory findings (§9B) did
**not** — they only lived in a terminal print + an `escalation` row. Researcher's ruling: *"should
you fix it? why ask? why is there a standard if you don't follow it - obviously it must be fixed.
Errors is not optional to fix it. you can add this as a app config in settings so you do not have
to ask me again."*

**Fixed and codified, not just fixed:**
- `candidate.validate` now writes `candidate.quality_report_path` (default
  `iba/app/reports/candidate-quality.md`) every time it runs — every distinct messy tag and every
  orphan lemma, not just the escalation's 10-item sample.
- `passage.validate` now writes `passage.quality_report_path` (default
  `iba/app/reports/passage-quality.md`) — the full distribution, plus a per-book breakdown the
  escalation summary didn't have room for.
- `configmaint.validate`'s findings (orphans, needs-justification) are now also folded into
  `CONFIG-REPORT.md` §0, generated fresh every time — persistent, not only live in the current
  escalation.
- **`governance.reports_must_persist`** (new `governance` module) states the standard as a real
  cfg_setting, and `configmaint.validate` now has a genuine coherence check
  (`lib/cfgquality.find_missing_report_paths`) enforcing it — any quality-check step registered in
  `QUALITY_CHECK_REPORT_PATH` without a real report-path setting is a hard error, not an advisory.
  This is the researcher's "so you don't have to ask me again" — the app itself checks compliance
  going forward, not only memory. **§8 above applies the same pattern to this document's own
  currency.**
- `lib/cfgquality.py` (new) — `find_orphan_configs`/`find_settings_needing_justification`/
  `find_missing_report_paths` moved here from `handlers/configmaint.py` so `lib/cfgreport.py` could
  share them without a circular import.

---

## 9F. Value-quality enforcement — closing half of the "V8" gap, for real (2026-07-21)

Asked to assess `candidate_seed` for a proper report, why config didn't check its column values,
and why validation didn't check that values support the app's objectives. Investigation (not just
a `candidate_seed` patch — see
[`iba-candidate-seed-quality-findings-v1-20260721.md`](../docs/iba-candidate-seed-quality-findings-v1-20260721.md))
found the gap was systemic: **every validate step in this app checked structure — exists, FK
resolves, not-null, dedup, declared enum — and nothing checked that a column's actual VALUE served
what it is declared for.** Confirmed live: `candidate_seed.tag` (226/1732 messy, 281 null),
`lemma_inventory.gloss` (494/11421 messy — upstream of the seed tag AND matched by
`cfg_candidate_rule`'s synonym rule), `strong_sense.head` (228/3463 containing an entire unsplit
`<br>`-joined sense tree — a genuine parser bug, not a formatting nit), `word_registry.word` (1 live
corrupted entry), `span.surface` (59 empty). The two enums meant to constrain
`candidate_seed.decision`/`.layer` (`candidate_decision`/`candidate_source`) were declared in
`cfg_column.expectation` but referenced by **no code at all** — clean today by luck, not by
anything enforced.

**Built:**

- **`lib/valuequality.py`** (new) — the generic engine. `cfg_column.expectation` now drives a real
  value-quality scan, not just FK/enum documentation. Three forms: `notblank`, `nohtml`,
  `pattern:<cfg_setting key>` (reuses `candidate.tag_clean_pattern` rather than forking a parallel
  constant). `scan_column(...)` also takes an optional scope clause, reused by `validation.py`'s
  new per-word/per-book section.
- **`find_enum_violations`** (same module) — the missing enum-membership check, wired into
  `configmaint.validate` as a hard coherence fault (not an escalation — an enum violation is
  structural, same class as the existing FK/PK checks).
- **`candidate.validate`** rewritten onto the engine — now scans `span_candidate.candidate_tag`,
  `candidate_seed.tag`, AND `lemma_inventory.gloss` in one pass, one report, one escalation.
- **`validation.py`** gained a "6. Value quality" section (word- and book-scoped) via the same
  engine.
- **`handlers/raw.py:_split_def`** fixed (STEP's `<br>`-separated trees weren't split — normalise
  to `\n` first, case-insensitively — `<BR>` uppercase was a second miss, found and fixed the same
  day) + `migration/repair_strong_sense_head.py` (one-off, re-derives affected strongs from the
  live checks, not a fixed list — safe to re-run if the bug shape recurs). Two levels of the same
  root cause, both now at **0 violations, live-verified**:
  - `strong_sense.head` (`nohtml`) — 228 rows repaired, populating 1,114 `strong_meaning_tree`
    rows that had silently never been written.
  - `strong_meaning_tree.sense_text` — 2,244 of 3,178 lemmas affected. Corrected to a
    **blacklist** (reject only `<br>`/`<BR>` itself, tolerate every other STEP tag) after a first
    whitelist attempt produced false positives on legitimate `<b>`/`<i>`/`<greek>`/`<ref>` markup.
    1,383 lemmas repaired across two migration passes; 2,610 `strong_meaning_tree` rows written.
- **`candidate.curate`** (new step, `candidate-curation` work package, `Candidate-Curate.ps1`) —
  the ongoing `candidate_seed` add/correct/remove utility `configmaint.propose` cannot provide
  (it's restricted to `cfg_*`). Single-row, approval-gated, same shape as `configmaint.propose`.
  Method: [`iba-candidate-seed-curation-method-v1-20260721.md`](../docs/iba-candidate-seed-curation-method-v1-20260721.md).

8 `cfg_column.expectation` values registered via `configmaint.propose` (the 6 columns found dirty
in the first pass, `strong_meaning_tree.sense_text` found in the same-day follow-up, plus
`span_candidate.candidate_tag` and `candidate_seed.decision`'s pre-existing-but-unused
`enum.candidate_decision`/`enum.candidate_source` declarations, now actually enforced).

**Lesson, worth keeping:** a value-quality pattern for a column that legitimately carries rich,
variable third-party markup should be a **blacklist of the specific known defect**, not a whitelist
of every acceptable form. Test any such pattern against live data before registering it.

---

## 10. A DB review, closed loop — run.state bug, config_version, retention, sub-strong schema (2026-07-22)

The researcher reviewed `run`, `escalation`, and `candidate_seed` directly (exported to CSV via
`Export-Tables.ps1`) and found real defects, then made clear: findings without fixes are not
acceptable — every item below was investigated AND closed in this pass.

**`run.config_version` was permanently stale.** It was a string from `config/rules.json`'s seed,
written once by `cfgload.py` and never touched again — `configmaint.propose` never updated it, so
every run since pinned the same `"app-0.1.0"` regardless of how many real changes had landed.
Fixed: `cfg.config_version()` now computes a live SHA-256 fingerprint of every `cfg_*`
config-content table (`lib/cfg.py:_VERSION_TABLES`) on every call — no write, no discipline
required, changes the moment the config actually does (`app-0.1.0+<12-hex>`).

**`run.state` could never reach `'done'` for a standalone-step work package — a real bug, not a
real pause.** The dispatcher only marked a run done when its step was the LAST in the work
package's `cfg_step` sequence — correct for a chained work package (`new-word`, `set-candidates`,
`build-passages`), wrong for one whose steps are each invoked independently
(`configuration-maintenance`, `reports`). **185 runs** were stuck `'paused'`/`'running'` forever
despite being fully resolved. Fixed: `cfg_work_package.chained` (new column,
`migration/add_work_package_chained_column.py`) tells the dispatcher which shape a package is;
`run.py` marks a non-chained step's run done on its own first `ok`/`report-continue`/`self-heal`.
25 of the 185 (non-chained) were retroactively corrected (`migration/fix_stuck_run_states.py`); the
remaining 178 (`set-candidates`, chained) left alone deliberately — a chained run stuck mid-sequence
may be a genuinely abandoned run.

**No log-retention visibility existed** for `run`/`escalation`/`validation_result`. Built
`lib/retention.py` + `Log-Retention.ps1` → `iba/app/reports/log-retention.md`: row counts and age
per table, every open escalation, recent real failures, and a "stuck chained runs" section listing
the 178 above as archival CANDIDATES for a human decision. Deliberately **read-only**.

**No way for the researcher to add their own item to `escalation`.** Added `raise_manual()` +
`Escalation.ps1 -Action Raise -Question "..."` — writes a row under a synthetic
`MANUAL-<timestamp>` run_id, answered via the exact same `AnswerRun` path as every other
escalation. Used immediately to log the anger/spirit open issue (escalation `#228`).

**Found and fixed while building the above:** `registry.create`'s write-grant on `escalation` was
dead code — deleted via `configmaint.propose`. Also: a `cfg_setting` value that isn't valid JSON
now fails at `configmaint.propose` time, not with a runtime crash three steps later.

**`candidate_seed.strong_variant`** (new column, `migration/add_candidate_seed_strong_variant.py` —
a genuine table rebuild, since the dedup key changed from `lemma_key` alone to
`(lemma_key, strong_variant)`). Closes a real structural gap: 173 of 3,178 base lemma_keys have
multiple sub-lettered `strong` variants with genuinely different glosses. `candidate.set` now
prefers an exact `strong_variant` match, falling back to the base row. `candidate.curate` gained
`Field=split`/`Field=delete`.

**Applied the researcher's explicit data-quality ruling:** "a large number of blank tags... these
rows must be deleted." **280 `candidate_seed` rows soft-deleted**
(`migration/delete_blank_tag_candidates.py`).

**2026-07-22, later the same day — `run.py`'s escalation dedup bug (found proposing the two
`governance.*` settings in §8):** the pause-idempotency check was keyed on `(word, at_step)`. Every
config-scoped or quality-check step (`configmaint.propose`, `candidate.validate`, `passage.validate`,
...) runs with `ctx.word == ""`, so it wrongly treated *any* second concurrent escalation at the
same step as a duplicate of the first and silently never wrote its `escalation` row — the run still
showed `state='paused'`, making it look like it had escalated when it hadn't. Fixed: dedup is now
keyed on `run_id` (already unique per invocation) + `at_step`, which is correct for both word-scoped
and word-less runs. Verified: re-proposing `governance.governance_md_on_rule_change` under its
existing `run_id` after the fix produced escalation `#239` as it should have the first time.

---

## 11. What changed in this rewrite (2026-07-22)

- Restructured: §1–§8 is now the standing overview (was previously interleaved with the
  chronological log); §9A onward (formerly §5A onward — letters kept for existing cross-references
  from `BUILD.md` and elsewhere, renumbered under the new §9/§10/§11 umbrella) is explicitly framed
  as dated history.
- **§5 corrected** — book order and `step.span_html` were claimed to be "facts, stay in code";
  both are `cfg_*` rows today, found by checking `lib/cfg.py`/`stepapi.py` directly, not by
  re-reading the old sentence.
- **§6 corrected** — the new-word approval escalation was claimed "stubbed to auto-approve"; it is
  a real, live yes/no escalation (`handlers/registry.py:create`), confirmed against escalation
  `#169` currently open. Only the three-way *answer shape* is still a fast-follow, not the whole
  mechanism.
- **§2/§7 extended** — table count corrected (13 → 17), and the file inventory brought current to
  include everything from §9F/§10 (`valuequality.py`, `retention.py`, `Export-Tables.ps1`,
  `Log-Retention.ps1`, the six 2026-07-21/22 migration scripts) that had landed but never been
  added to a "files" list here.
- **§8 added** — the two governance-currency settings this rewrite itself was asked to add,
  proposed but not yet approved (escalations `#238`/`#239`).
- **A real bug found and fixed while doing this work** (§10, last entry) — `run.py`'s escalation
  dedup logic, which silently swallowed the second of the two `governance.*` proposals raised for
  §8 until fixed.

---

## 12. `candidate.load` built — a real incident, a genuine recovery, and the rollback mechanism
this app never had (2026-07-22, later the same day)

Escalation `#222`'s backlog (candidate quality findings) led to a design decision — approved plan
`iba/docs` "melodic-foraging-bunny" — to stop hand-curating one lemma at a time and build a proper
JSON-batch create/update/validate routine for `candidate_seed`: `candidate.load`, extending the
`candidate-curation` work package. Full design in the plan file; this section is the build and
incident account.

**What it does.** Input is `{"word", "reason"}` only — no `lemma_key` — the tool derives the
lemma/`strong_variant` itself, preferring a sub-lettered variant's own gloss over the collapsed
base lemma when one matches. A clean item **auto-loads** (no approval gate — follows `seed()`'s
bulk-apply precedent, not `curate()`'s per-row gate, per the researcher's explicit correction of
my first draft's assumption). A duplicate is skipped **untouched**. Anything else (format failure,
no lemma match, a cross-reference mismatch against STEP's own gloss) is written as an inspectable
`decision='exception'` row in `candidate_seed` itself, not just reported. Then the whole existing
seed is revalidated the same way. **One** escalation for the entire run, only if unresolved
exception rows remain. New schema: `candidate_seed.sense_seq` (resolves `#228`'s dual-sense-one-
Strong's problem — a lemma can now have a second row when one Strong's code genuinely carries two
IB concepts with no distinct sub-strong to split onto), `step_status` (STEP cross-reference,
read-only, never writes to `strong`), `ib_referent_type` (informational: characteristic / other
being / body part).

**The incident.** Testing the empty-input (revalidate-only) mode before ever touching new data
found nothing wrong on inspection — but running it live wrote `decision='exception'` over **1029
of 1806** `candidate_seed` rows. Root cause: `candidate.transliteration_pattern`'s shipped default
(`^(?=.*[a-z])[a-z]{2,10}$"`) matches almost any all-lowercase single-word tag — it cannot tell
`hearing` from `asah` by shape alone, a limitation the design doc had named as a real risk but the
actual default still got wrong in practice. There was **no rollback mechanism for `iba.db` at
all** — the only recovery candidates were a manual backup 3 days stale
(`iba.db.bak-20260719-precandidatefix`) and, found only because the researcher had independently
run `Export-Tables.ps1` that same morning, `iba/app/export/candidate_seed.csv` (05:47, before any
of the day's changes). Recovery: matched every corrupted row by its stable `id` (survives the
schema migration, since both this migration and the earlier `strong_variant` one explicitly copy
`id` across the table rebuild) against the CSV — **1028 of 1029 restored exactly**; the 1 row
created after the export (a `curate()` split, `H0639G` "anger") restored by code-path reasoning
(`curate()`'s split branch only ever writes `decision='candidate'` for a new row — confirmed 0 of
1028 verifiable rows were anything but `'candidate'` before the bug, so this was not a guess made
under uncertainty, it was arithmetic).

**Two more bugs found by testing a small batch before running the full seed again** — exactly the
discipline this whole programme exists to enforce, turned on its own build:
- `_resolve_lemma`'s matching used raw, unbounded substring containment. A gloss of literally `'I'`
  matched inside the test word `hearing` (resolving to the *wrong* lemma instead of recognising
  `H8085`'s existing `tag='hearing'` row); a gloss of `'word'` matched inside the nonsense test
  word `zzznotarealword`, which then auto-loaded as a real candidate. Fixed: word-boundary regex
  matching, and an exact-match against an existing `candidate_seed.tag` tried first.
- The duplicate-check path reused `_write_exception` — since the row already existed, it took the
  UPDATE branch and **overwrote the pre-existing legitimate row**, the exact opposite of the
  approved design ("no second row is written for a true duplicate"). Found on the very next test
  run, before it could reach the full seed a second time. Fixed: a duplicate now writes and
  touches nothing.

Every mutated row from every test iteration was tracked (`layer='batch-load'` is written by
nothing else in this app) and either restored from the snapshot/CSV or purged as genuine test
artifacts with no prior existence — verified back to the exact pre-incident row count and decision
distribution (1806 total; 1733 `candidate` immediately after the first recovery, then 1489
`candidate` / 244 `exception` / 73 `rejected` once the FIXED revalidation correctly identified the
real, pre-existing messy-tag backlog with zero false positives — spot-checked against a random
sample).

**The rollback mechanism, built in direct response.** `iba/app/lib/dbsnapshot.py` — `snapshot(reason)`
copies `iba.db` (WAL-checkpointed first, so the copy is consistent) to `iba/app/db/snapshots/`,
pruning to `retention.snapshot_keep_count` (new setting, default 20). Wired into
`run.py:_ensure_run()`: every NEW run snapshots before anything else happens, not just
data-writing ones, since a run's own bug is exactly what this protects against; a resumed paused
run does not re-snapshot. `IBA_NO_SNAPSHOT=1` skips it, mirroring the legacy Bible-study engine's
own `_apply_*` pre-op snapshotting and its `--no-backup`-for-loops escape hatch — the researcher's
own words: *"you should have had one from the word go... I know you had one on the old DB."*
Correct: this app had none until this incident forced it, and now every run — not only
`candidate.load` — has a rollback point.

**Verified end-to-end after all fixes**, in order: the transliteration pattern change produces zero
false positives against the same word list that broke it; a small test batch (new clean word,
exact duplicate, split-on-delimiter, no-match nonsense word) produces the correct outcome for
every case (1 auto-loaded, 2 duplicates skipped untouched, 2 written as exceptions); `candidate.set()`
still stamps correctly with `sense_seq` present (ran clean for Genesis — the span-count drop from
the previous stamp is explained by legitimate causes: excluding the 244 real messy-tag rows from
stamping, and `candidate.seed()`'s own accept-list catch-up, unrelated to this change); the
snapshot utility fires automatically and prunes correctly.

---

## 13. Reports fully config-governed — Phase 0 built (2026-07-22, later the same day)

Full design: `iba/app/PLAN-reports-config-governance-v1-20260722.md` (v3, researcher-approved
after several review rounds — §9.1–9.3, §10.1–10.3). Researcher's corrected standard: *"the need
for, the type of, and the location of the report is config driven for ALL reports... the content
of the report is also config driven — Titles, headers, section, ToC, footer... naming convention,
version control... archiving... run completion, and exception notification... all need to be
config driven, to control wording, routing."* Phase 0 — wiring every EXISTING report/notification
onto config, content/wording unchanged — is built, verified, and complete (sub-phases 0a–0e).

**Schema added** (3 new tables, 2 migrations — `bootstrap_report_content_governance.py`,
`bootstrap_retention_table_export_registration.py` — both idempotent, re-run safe):

- `cfg_report` (step → title/show_toc/footer_text/output_kind/naming_scheme/archive_dir)
- `cfg_report_section` (step, ordinal, section_key, heading, toc_label, include)
- `cfg_report_csv_table` (step, table_name, join_note) — the MD analysis / CSV verbatim-dump
  pairing the researcher asked for; CSV is now the default output for every report
  (`schema-overview`, not yet built, will be the one deliberate exception — it already is the
  schema, a CSV of it would be redundant)
- `cfg_on_fail` gained a `route` column (`terminal` | `terminal+report`) and `condition='ok'` rows
- `cfg_work_package` gained `complete_message` / `next_step_hint` / `paused_message` (nullable —
  NULL means "use the shared default", set means "this package's own text")
- `notification.*` settings (module `notification`, new) — the shared terminal boilerplate every
  `.ps1` script now renders from instead of its own hardcoded strings

**Ownership ledger — every config item governs exactly one thing, per the researcher's "must not
conflict with each other" instruction (9.1):**

| Config item | Governs — and only this |
|---|---|
| `cfg_step` / `cfg_work_package.ps_script` | which step exists, which PS script runs it |
| `cfg_report.title` / `.show_toc` / `.footer_text` | the report's title, ToC, footer |
| `cfg_report.output_kind` / `.naming_scheme` / `.archive_dir` | md vs md+csv, filename stability, archive folder — `naming_scheme='stable'` writes both a versioned file AND keeps a fixed-name copy current (CONFIG-REPORT.md-style, living docs other files link to); `naming_scheme='dated'` writes ONLY the versioned file, no fixed-name duplicate (point-in-time snapshots — `escalation.history`/`escalation.list`/word-registry-span reports). Wired live 2026-08-26 (BUILD.md §179, escalation #857) — the column existed since 2026-07-22 but `reportkit.write_report()` ignored it until then. |
| `cfg_report_section` | which sections, heading, order, ToC inclusion — **except** `report.word`/`validation.word`/`validation.book`, where the pre-existing `report.show_*`/`validation.show_*` settings own inclusion; `cfg_report_section` there only supplies heading text/order for whatever those toggles already chose |
| `cfg_report_csv_table` | which tables (+ joins) the CSV half dumps |
| `cfg_on_fail(step, condition)` | which PATH a condition takes + its message + route |
| `cfg_work_package.complete_message` / `.next_step_hint` / `.paused_message` | the whole-package COMPLETE/PAUSED banners (chained packages only) |
| `notification.*` settings | shared boilerplate wording (header lines, result-line format, the two generic PAUSED variants, STOPPED) |

**Fixed along the way (real bugs, not scope creep — found by re-auditing the live app per this
plan's own §2/§2C, same discipline as §9B/§9E/§9F):**

- `log-retention` and `export_tables_csv` were standalone, unregistered — the same "no other module
  knows this exists" gap §9C fixed for `report.py`/`validation.py`/`cfgreport.py`. Both now real
  `cfg_work_package`/`cfg_step` rows (`log-retention`/`retention.report`,
  `table-export`/`table.export`), both PS wrappers now call `python -m iba.app.run`, not the tool
  module directly.
- `export_tables_csv` dumped `cfg_*` tables too, duplicating `configmaint.report`. Fixed — excludes
  `cfg_%` unconditionally now; stale pre-fix `cfg_*.csv` files in `iba/app/export/` removed.
- `candidate.load` derived its report path from `candidate.quality_report_path`'s parent dir instead
  of having its own setting — now `candidate.load_report_path`.
- Two seed-data typos caught only by diffing generated output against the pre-change file, not by
  code review: a lost `→` (became `-` in `report.word`'s "L1 → L2" heading) and lost quote marks in
  `validation.word`/`validation.book`'s titles (Python's `!r}` repr vs a plain `.format()` template).
  Both fixed in the migration source and the live rows.
- `Config-Maintenance.ps1`/`Set-Candidates.ps1`'s per-step result line used three different column
  widths (`-16`/`-18`/`-20`) for the same line type — the exact inconsistency §7 of the plan
  predicted. Normalised to one shared template (`notification.step_result_line`), the one deliberate
  formatting change in an otherwise content-frozen phase.
- One pre-existing inconsistency found and **deliberately left as-is**, not silently normalised:
  `candidate.load`'s Load-mode PAUSED banner has always used slightly different wording than the
  other four guided-pause banners (missing the "then re-run..." line). Flagged in
  `Candidate-Curate.ps1` with a comment; a decision for the researcher, not made here.

**`configmaint.validate` coherence, extended** (`lib/cfgquality.find_missing_cfg_report_rows` /
`find_chained_packages_missing_complete_message`) — every step in the known report-producing set
(`REPORT_STEPS`) must have a `cfg_report` row, every chained work package must have a
`complete_message`; both are now hard structural errors, not something that can quietly regress the
way the retention/`candidate.load` gaps did before this pass found them. `CONFIG-REPORT.md` §12
("Reports — full governance per report") is the generated, can't-drift answer to the researcher's
"am I seeing everything related to it" concern — one block per report joining `cfg_report` +
`cfg_report_section` + `cfg_report_csv_table` + its work package's banners + its `cfg_on_fail` rows.

**Verified**, not asserted: every one of the 8 existing report-producing steps re-run live and
diffed against its pre-change output (headings/titles byte-identical bar the intentional new ToC
and the two typo fixes above); all 13 `.ps1` scripts syntax-checked, 10 of them re-run live
end-to-end through their full PowerShell wrapper (not just the Python dispatcher) with matching
terminal output; `configmaint.validate`/`configmaint.report` re-run clean throughout. `New-Word.ps1`
was syntax-checked and code-reviewed but **not** run live (STEP API calls + a new `word_registry`
row — a blast-radius call, not a coverage gap; its logic is the same shared `Notify.ps1` functions
already proven correct on every other script).

**Not done yet (separate, later phases per the plan — §10.3/§8):** the 4 new reports (seed-candidate,
strong-meaning, span-analysis, schema-overview), the one-off/investigatory report naming helper, and
`BUILD.md`'s own update. Nothing in Phase 1+ has been started.

---

## 14. Reports fully config-governed — Phase 1 built: the 4 new reports (2026-07-23)

Continues §13. Design: `PLAN-reports-config-governance-v1-20260722.md` §3.1–3.4. Unlike the
original 8 reports (which started hardcoded and were retrofitted onto `lib/reportkit.py` in Phase
0), these 4 were built **directly on the scaffolding** — no hardcoded headings ever existed for
them.

**Built:**

- `report.seed_candidate` (`lib/seedreport.py`, `SeedCandidate-Report.ps1`) — whole-`candidate_seed`
  picture: counts by decision/layer/role, tag word-count and rows-per-lemma distribution, the
  busiest lemmas, and an open (`decision='exception'`)-vs-resolved trend by day. CSV: `candidate_seed`
  joined to `lemma_inventory.gloss`.
- `report.strong_meaning` (`lib/strongreport.py`, `StrongMeaning-Report.ps1`) — meaning-parse layer
  coverage: `strong` rows with no `strong_sense` row (a gap list, ordered by usage `count`),
  sense-count distribution (`strong_meaning_tree` rows per lemma), lexicon completeness
  (`lsj`/`mounce`). CSV: `strong_sense` + `strong_meaning_tree`, both joined to `strong.stepGloss`.
- `report.span_analysis` (`lib/spanreport.py`, `SpanAnalysis-Report.ps1`) — span-layer coverage per
  book (spans + candidate spans), morph-code distribution, particle split. CSV: `span` +
  `span_candidate`, full verbatim dumps (a join to `word_strong`/`strong` was considered per the
  plan's first-cut proposal but dropped — the two tables don't share a clean join key at the same
  grain, and a verbatim dump already satisfies "table content, not just summaries" without a
  fragile join).
- `report.schema_overview` (`lib/schemareport.py`, `SchemaOverview-Report.ps1`) — the IBA app's own
  data-schema snapshot (the equivalent of the Bible-study side's `build_dbschema.py`, which had no
  counterpart here): every one of the 17 data tables, columns/types/PK/FK/indexes, row counts.
  Introspects the live DB directly (`PRAGMA table_info`/`foreign_key_list`/`index_list`) —
  deliberately no CSV pairing, since this report already *is* the schema.

**Registered** as 4 new single-step work packages (`seed-candidate-report`, `strong-meaning-report`,
`span-analysis-report`, `schema-overview-report`), each with its own PS script, matching the
established one-script-per-standalone-report pattern (`candidate-quality`, `passage-quality`,
`log-retention`, `table-export`). Migration: `bootstrap_new_reports_phase1.py` (idempotent).
`lib/cfgquality.REPORT_STEPS` extended to cover all 4, so `configmaint.validate`'s coherence check
(§13) covers them from day one, not retrofitted later.

**A real accuracy bug found and fixed while reviewing this report's own first output** (not by
inspection — by reading what it actually said): `strong_meaning.md`'s lexicon-completeness table
originally counted only *within* `strong_lexicon` (1506 rows), silently excluding the ~1957 `strong`
entries with no `strong_lexicon` row at all — the table looked 100%-accounted-for when nearly 57%
of `strong` was invisible to it. Fixed to count against every `strong` row via `NOT EXISTS`/`LEFT
JOIN`, not just existing `strong_lexicon` rows.

**`reportkit.render_scaffold` fixed too** (benefits all 12 reports, not just these 4): a section's
body not ending in a blank line ran straight into the next `## heading` with no separating blank
line — cosmetically wrong Markdown, found on this batch's first output and fixed at the shared
level rather than patched per-report.

**Verified**: all 4 re-run live end-to-end through their PS wrapper; `configmaint.validate` clean
(no new coherence errors — REPORT_STEPS check passes for all 4); `CONFIG-REPORT.md` §12's per-report
rollup picked all 4 up automatically, no extra wiring needed.

**Still not done**: the one-off/investigatory report naming+folder config helper (Phase 2, §5 of the
plan) — the last item from the plan's phase list.

---

## 15. Reports fully config-governed — Phase 2 built: one-off report naming (2026-07-23)

Continues §13/§14 — the last item on the plan's phase list
(`PLAN-reports-config-governance-v1-20260722.md` §5/§8, sub-phase "Phase 2"). One-off
("investigatory") reports don't recur, so they get no `cfg_step`/`cfg_report` row — but their
folder/naming/format now come from config too, via 3 new `governance.oneoff_*` settings
(`bootstrap_oneoff_report_naming.py`) and `lib/reportkit.oneoff_path(cfg, topic)`.

Same-day collisions get `-v2`/`-v3`/... appended automatically, per the Bible-study side's own
`docs/file-organisation-rules.md` §2.3 convention (adopted, not reinvented). Verified directly:
first call for a topic returns `{topic}-{YYYYMMDD}.md`; a second call the same day for the same
topic returns `-v2`, a third `-v3`; a different topic gets its own clean path; punctuation/spaces
in the topic are slugified. `configmaint.validate`/`configmaint.report` re-run clean.

**All phases of `PLAN-reports-config-governance-v1-20260722.md` are now built** (Phase 0 §13,
Phase 1 §14, Phase 2 this section). Nothing from the plan remains outstanding — future
one-off/investigation scripts should call `reportkit.oneoff_path()` instead of hardcoding a path,
but no existing script needed retrofitting (none existed yet using a hardcoded one-off path in a
way this replaces).

---

## 15A. Script-folder consolidation, `configmaint.propose`'s stale table whitelist, CSV archive-on-write (2026-07-23, escalations #271/#273/#274/#275)

Clearing the day's researcher-flagged escalation backlog (raised earlier the same session, held
without action per the researcher's explicit escalate-only instruction, then actioned once told to
clear it) surfaced two real app bugs and one real folder-scatter problem, alongside the
report-content fixes §14 already covers the shape of.

**A real `configmaint.propose` bug, found while actioning #274.** `handlers/configmaint.py`'s
`CFG_TABLES` whitelist — the hard-coded list of tables the coherence check will accept — still
listed only the 17 tables from before the §13 report-governance work; `cfg_report`,
`cfg_report_section`, and `cfg_report_csv_table` (added that same day, §13) were never added to it,
despite already correctly holding `cfg_write_grant` rows for `configmaint.propose`. Practical effect:
**no report title/section/CSV-pairing config had been changeable via the sanctioned path since §13
landed** — `configmaint.propose` rejected any such attempt with "not a recognised cfg_* table"
before the write-grant check even ran. Fixed: the three table names added to `CFG_TABLES`. (The
sibling `CFG_TABLES` constant in `migration/bootstrap_configuration_maintenance.py` — a one-off,
already-executed bootstrap script predating `cfg_report`'s existence — was deliberately left as a
historical artifact, not updated; it is not on any live enforcement path.)

**Escalation #273 — two export folders.** `table_export.output_dir` (default `iba/app/export`) and
every report's own CSV pairing (`{report.output_dir}/export`, now uniformly `iba/app/reports/
export` after #269/#270) were two separate physical folders holding overlapping table names with
different content — e.g. `candidate_seed.csv` was independently written by `candidate.load`,
`candidate.validate`, `report.seed_candidate`, AND `validation.book`, each a different scoped slice,
all landing at the same filename. Worse: **no CSV writer archived on overwrite** — `write_report()`
had done this for `.md` output since the researcher's 2026-07-22 instruction, but `reportkit.
write_csv_pairing`'s `_write_csv` and `tools/export_tables_csv.py`'s own inline writer both did not,
so every regenerate silently destroyed whichever report's slice had been there before. Fixed:
`lib/reportkit.archive_before_write()` (new, shared helper — the same timestamp-suffix-into-
`archive/` convention `write_report` already used) is now called by `_write_csv` AND by
`export_tables_csv.export()`; `table_export.output_dir` reproposed to `iba/app/reports/export` so
there is exactly one export folder; the old `iba/app/export/`'s contents archived (not deleted) and
the folder removed. Verified: running `table-export` immediately after archived every pre-existing
same-named file from the folder it now shares (12 files correctly archived with original
timestamps, none lost).

**Escalation #271 — scripts scattered across four folders.** `iba\scripts\`, `iba\ps\`, `iba\app\
ps\`, `iba\app\tools\` all held scripts. Investigated each file rather than moving by folder name
alone: 7 files in `iba\scripts\` (2 Python, 5 PowerShell) already targeted `iba/app/db/iba.db`
explicitly in their own code — genuinely IBA-app-scoped, just misplaced — and were relocated into
`iba/app/tools/`/`iba/app/ps/` (BUILD.md §8 has the full list); their own docstring usage lines
updated to match. The other 5 files remaining in `iba\scripts\` (`cfg_apply.py`/`cfg_helper.py`/
`cfg_kernel.py`/`probe_step_api.py`, `build_dbschema.py`) were confirmed, by reading each file, to
belong to genuinely different systems — the separate `iba/config` heavyweight configurator (§6) and
the main Bible-study programme's own schema tool respectively — and were deliberately left in place;
moving them would have been scope creep past what the escalation actually found broken.
`iba\ps\New-Word.ps1` turned out to be a stale, pre-restructure STUB (its own docstring: "nothing is
built out", referencing the old `iba/config/utility/run.json` design) superseded entirely by the
real `iba/app/ps/New-Word.ps1` — archived (not deleted) to the new `iba/app/archive/`, and the
now-empty `iba\ps\` folder removed. **The canonical locations are now real config**, not just
convention: `cfg_setting governance.scripts_ps_dir` = `iba/app/ps`, `governance.scripts_python_dir`
= `iba/app/tools`. Also normalized 4 `cfg_work_package.ps_script` rows
(`configuration-maintenance`/`candidate-quality`/`passage-quality`/`reports`) that held a bare
filename instead of a full path, for consistency with every other row — cosmetic (the field is
informational, read only by `cfgreport.py`, not used to actually locate/invoke anything), found
while auditing this table for the same escalation.

**Left open, not self-resolved:** re-running `configmaint.validate` after all of the above flagged
the two new `governance.scripts_*_dir` settings as orphans (not referenced by any executing code —
they are stated convention, the same class as the pre-existing `governance.build_md_on_code_change`/
`governance_md_on_rule_change` orphans). This is a genuine judgement call for the researcher (is a
documentation-only convention setting an acceptable "orphan," per the orphan-detector's own design —
§9A), not a mechanical implementation of an already-given instruction, so it was left as its own
open escalation rather than self-approved under this session's backlog-clearing authorization.

---

## 15B. Escalation lifecycle extended — Edit/Pause/Resume/Retract (2026-07-23, later same day)

Asked to consolidate `USER-GUIDE.md`'s scattered escalation instructions (§4, §9, §10a/b, §11, §13,
§14 each showed a fragment, no single complete reference existed) and to add real methods to edit,
pause, and retract a manual escalation — the table increasingly doubles as a backlog of work items
for Claude, not only design decisions awaiting the researcher's approval, and `raised → answered`
alone wasn't enough lifecycle for that.

**Schema:** new `cfg_enum` group `escalation_state` (`raised`/`answered`/`paused`/`retracted`,
4 rows via `configmaint.propose`) — `escalation.state` had no governed controlled vocabulary at all
before this, unlike every other enum-backed field in the app (a small pre-existing gap, closed in
passing).

**`lib/escalation.py`:** `edit_question()` / `pause_run()` / `resume_run()` / `retract_run()`, each
guarded by a new `_manual_only()` check. **Restricted to `MANUAL-`-prefixed run_ids** — found
necessary while building, not part of the original request: a real dispatcher-tied escalation
(`configmaint.propose`, `candidate.validate`, `passage.validate`, ...) is read by two checks keyed
specifically on `state='raised'`/`'answered'` — `run.py`'s pause-continue dedup and
`answered_for_run()`. Flipping one of those to `state='paused'` would match neither, so re-running
the underlying command before resuming it would raise a **second** escalation row for the same
run_id+step rather than recognize the existing pause — the same class of bug §10's `run.state` fix
closed for a different reason. Manual items have no such downstream reader, so the guard simply
refuses a non-manual run_id with a clear message. `write_list_report()` (§ escalation-list, §15A)
now shows `raised`+`paused` together, paused ones flagged, with a state column.

**`ps/Escalation.ps1`:** four new `-Action` values, added to the existing `ValidateSet`, each with
its own parameter validation matching the existing Answer/AnswerRun pattern.

**`USER-GUIDE.md` §4 rewritten** as the single, complete escalation reference — the three shapes,
the state machine, all 8 actions, resume behavior, and the new §4.6 for Edit/Pause/Resume/Retract.
Every other section's mention of `Escalation.ps1` now points back here rather than re-explaining.

**Verified end-to-end:** raise → edit (old wording preserved in `tried`, not overwritten silently) →
pause → list (correctly showed 1 paused among the total) → resume → retract → list (item gone from
the open count); the `MANUAL-` guard confirmed rejecting a real `RUN-...-CONFIGMAINT` run_id with
the intended message, not silently succeeding; `configmaint.validate` re-run clean of hard errors
(`escalation_state` joins `escalation_answer` as an expected orphan enum, same accepted class).

---

## 15C. Orphan-config detector redefined — the researcher's correction on what "usage" means (2026-07-23, escalation #305)

§15B's own closing line — accepting `escalation_state` as an orphan "same accepted class" as
`escalation_answer` — is exactly what the researcher flagged as the underlying bug, via escalation
number 305 (raised as a `MANUAL-` item, its wording arrived truncated mid-sentence in the terminal
paste; recovered in full in chat and the escalation's stored text repaired via `Escalation.ps1
-Action Edit` rather than left corrupted). Their point, close to verbatim: *"the check for usage of a config
is inadequate... usage is defined differently for different types of config... the test is if the
value of the config change, will the code automatically respond to it."* They named the shapes
explicitly: (1) most settings — code applies the value, so real usage is an actual read call; (2)
`governance.*` — must be read by the startup routine explicitly, "to ensure that AI complies with
it"; (3) enums — "a lookup, or options... not hard coded but use the config."

**`lib/cfgquality.find_orphan_configs()` rewritten** to check each shape on its own terms instead of
one "is the key quoted anywhere in the multi-file corpus" grep, which a stray comment or unrelated
docstring could satisfy without the code ever reading the value:

1. **Plain `cfg_setting`** — usage = the key literal and an actual `.setting(` call appear in the
   SAME file (not just the same corpus). Deliberately same-file rather than same-call-site: several
   settings are read through one level of indirection (`validation.py`'s `_WORD_SECTIONS =
   {"label": "validation.show_health", ...}` then `cfg.setting(key, True)` in a loop) and are
   genuinely applied, just not via a literal `cfg.setting("validation.show_health", ...)` call.
2. **`cfg_setting` with `module='governance'`** — these are process rules for the AI/researcher
   workflow, not runtime application inputs; there is no "the code applies the value" behaviour to
   look for. Usage = read explicitly by `iba/app/init.py`, the startup routine every session is
   required to run first (per `CLAUDE.md`). Built as a generic `SELECT key, value FROM cfg_setting
   WHERE module='governance'` read (init.py's new step 6, printed under a "governance rules (must
   be complied with this session)" heading) rather than hardcoding each key — a NEW governance
   setting is picked up automatically, and the detector recognizes the generic `WHERE
   module='governance'` read pattern as covering every row under it (the same reasoning already
   applied to `cfg_column.expectation`-driven settings).
3. **`cfg_enum` group** — usage = looked up BY NAME at runtime: `cfg.enum(name)` (the `Cfg` class's
   own accessor, already the real pattern for `candidate_decision`), or the equivalent raw
   `cfg_enum WHERE name='<name>'`/`name="<name>"` SQL a couple of handlers use directly (`on_fail`'s
   real, pre-existing usage, confirmed unaffected by this change). A group's individual VALUES
   turning up as hardcoded string comparisons elsewhere (`state == "paused"`, `decision ==
   "approve"`) is explicitly NOT counted — that's the vocabulary duplicated as Python literals, not
   actually read from `cfg_enum`.

**The two real gaps the old check had been masking, now closed, not just reclassified:**
`escalation_answer`'s validation in `lib/escalation.py:answer_for_run()` used a hardcoded
`RUN_ANSWERS = ("approve", "reject", "revise")` Python tuple — replaced with a live
`cfg.enum("escalation_answer")` call, so a DB-side change to the enum's membership is something the
function actually notices. Every `escalation.state` write (`raise_`, `answer_for_word`,
`raise_manual`, `answer_for_run`, `pause_run`, `resume_run`, `retract_run`) now goes through a new
`_check_state()` helper that validates against a live `cfg.enum("escalation_state")` lookup instead
of writing a bare literal — removing `'paused'` from the enum via `configmaint.propose` would now
make `pause_run()` raise, where before it would have silently written a value the enum no longer
recognized.

**Verified:** `find_orphan_configs()` re-run directly against the live DB — 0 orphans (was 6:
the 4 `governance.*` settings from §15A plus `escalation_answer`/`escalation_state` from §15B). A
synthetic check (an in-memory DB seeded with one genuinely-unused fake setting and one genuinely-
unused fake enum, alongside a real known-good one of each) confirmed the rewritten detector still
correctly flags real orphans — the fix tightened definitions, it did not make the check permissive.
`lib/escalation.py`'s full lifecycle re-verified post-change via the real `Escalation.ps1` CLI:
raise → pause → resume → retract, and `answer-run` with an invalid decision (`'maybe'`, correctly
rejected via the live enum, same message shape as before) and a valid one (`approve`, succeeded).
`configmaint.validate` re-run via the actual dispatcher (`python -m iba.app.run`) — the resulting
message no longer mentions any orphans, only the 7 pre-existing `candidate.*` "needs justification"
findings (Part B of the review file below, an unrelated, untouched check).

**Not done in this pass — left for the researcher:** escalation #304 itself (the original 6-orphan +
7-justification finding, detailed per-item in
`iba/app/docs/escalation-304-orphan-justification-review-v1-20260723.md`) is still `raised`. This
session fixed the DETECTOR and the two real code gaps it had been hiding; it did not answer #304 —
that remains the researcher's judgement call on the review file, not something to self-resolve.
A verification run during this work (`python -m iba.app.run configuration-maintenance --step
configmaint.validate --run-id RUN-verify-orphan-fix-20260723`) raised its own escalation (id 307,
carrying the same 7 pre-existing justification findings) as a side effect of testing through the
real dispatcher rather than the bare function — not a `MANUAL-` run_id, so it cannot be retracted
via the sanctioned Edit/Pause/Retract path; left as-is rather than touched directly, flagged here
for the researcher's awareness.

---

## 15D. `inactive` config, and the whole candidate system deactivated together (2026-07-23, escalations #306/#310)

Two escalations converged into one piece of work. **#306** claimed `cfg_candidate_rule` "makes no
sense... assume it is not used in any routine" — checked against live code before acting on it
(the researcher's own standing rule: investigate, don't guess): `handlers/candidate.py:seed()`
reads its `accept`/`reject` kinds directly, and — the part that actually mattered —
`_resolve_lemma()`'s docstring says outright it reuses the `synonym` kind "same substring
mechanism as seed()... reused, not duplicated," and `_ib_referent()` reads `body-part`/
`other-being` the same way. Both helpers are called from `candidate.load`, the NEWER routine, not
the one #306 was pointing at. So the table is genuinely shared across old and new; deleting it
outright — the literal ask — would have broken the replacement routine along with the one being
retired. Reported back rather than executed. The researcher's actual reply: the whole candidate
system, old routines and the "new" ones alike, came out of "a substantial mess up over the past
few days" and "will all be retracted in due course" — so the right action was never selective
deletion of one table, it was deactivating the whole surface together.

**#310**, raised separately and earlier the same session, asked for the general mechanism this
needed: *"Add a column in each config table to mark a config as inactive. Inactive configs must be
excluded from the validation but included as a list in the report."* Scoped to 14 of the 20 `cfg_*`
tables — the ones holding actual config CONTENT a researcher would toggle, not the 6 that are
audit trail (`cfg_change_log`/`cfg_change_detail`), internal state (`cfg_meta`), or describe other
tables' schema rather than being a config item themselves (`cfg_table`/`cfg_column`/`cfg_unique`).

**Built:**

1. `migration/bootstrap_inactive_column.py` — the DDL (`ALTER TABLE ... ADD COLUMN inactive
   INTEGER NOT NULL DEFAULT 0`) plus a `cfg_column` row per table, one-off and idempotent, same
   class of exception as `bootstrap_configuration_maintenance.py`/`bootstrap_setting_module_column.py`
   (`configmaint.propose` can only write rows on already-existing columns, not add one).
2. Every `_validate_live()` (`handlers/configmaint.py`) query against one of the 14 tables now
   filters `WHERE inactive=0`, and so do `find_orphan_configs`/`find_settings_needing_justification`
   in `lib/cfgquality.py`. Two checks (`find_missing_report_paths`,
   `find_missing_cfg_report_rows`) are keyed off hardcoded Python tuples
   (`QUALITY_CHECK_REPORT_PATH`, `REPORT_STEPS`) rather than a live `cfg_step` join, so a new
   `_step_inactive()` helper checks the step's own `cfg_step.inactive` explicitly and skips it —
   otherwise a retired step's now-deliberately-stale report config would keep getting flagged as a
   live defect.
3. `lib/cfgreport.py:_inactive_configs()` — every inactive row, listed by table (not silently
   dropped from view just because it's excluded from validation), folded into `CONFIG-REPORT.md`'s
   existing "findings" section. `cfg_candidate_rule` is summarised by `kind` + count rather than
   individual Strong's codes — the whole point of a report is to inform, and 289 raw values in one
   bullet would not.
4. `migration/retract_candidate_system.py` — applies all of the above to the real candidate
   system, scope taken from a direct enumeration query first, not assumed: 4 work packages
   (`set-candidates`, `seed-candidate-report`, `candidate-quality`, `candidate-curation`), 6 steps,
   5 write-grants, 7 settings (`module='candidate'`), 3 `cfg_report` rows + their 10 sections + 5
   CSV pairings, 10 `on_fail` rows, 4 enum groups (`candidate_decision`/`candidate_ib_referent`/
   `candidate_source`/`candidate_step_status`, 15 values), and all 289 `cfg_candidate_rule` rows —
   354 rows across 10 tables.

**Verified:** `configmaint.validate` via the real dispatcher — clean `"ok"` both immediately after
the column bootstrap (nothing yet inactive, confirming the new filters caused no regression) and
after the retraction ran (the 7 pre-existing `candidate.*` justification findings gone entirely, no
new errors). `CONFIG-REPORT.md` regenerated — "Inactive configs (354 row(s) across 10 table(s))"
renders correctly, every row accounted for and grouped by table.

**Deliberately not built:** `inactive` only excludes a row from `configmaint.validate`'s checks —
it does not stop `run.py`'s dispatcher from actually executing a deactivated step if someone runs
`Set-Candidates.ps1`/`Candidate-Quality.ps1`/`Candidate-Curate.ps1` directly. Blocking execution
outright is a different, not-yet-made decision (hard error vs. warning vs. leaving it callable
until the replacement lands) — not assumed here, flagged for whenever the actual replacement
system is being designed.

---

## 16. `governance.rules_must_be_config_driven` — the general standard behind §8's two settings, raised after a concrete violation (2026-07-26)

§8 already states two governance settings must exist as real `cfg_setting` rows, not just prose
here. This section generalises that into the standard itself, raised directly by the researcher
after catching a concrete instance: *"ALL rules must be config driven. NO rules should be specified
only in Governance or Build or Memory or User Guide that is not in the config. Reading the config
MUST be a startup rule and MUST be executed with every startup instruction."*

**The trigger.** `BUILD.md` §19/§20 record it in full: "runs refuse to start without STEP" existed
only as a hardcoded `init.py` check plus prose in `init.py`'s own comments and `USER-GUIDE.md` — no
`cfg_setting` backed it. A STEP-dependent tool was run (and its degraded result reported as a pass)
while STEP was down, and separately, `init.py`'s startup preflight printed the right warning but
`return 0`ed regardless — the stated rule had no enforcement teeth at the one place every session is
required to run first.

**Proposed via `configmaint.propose` (per §3A — approval-gated, never a silent write), approved and
applied** (escalations `#319`/`#320`, runs `RUN-20260726_082346_730-CONFIGMAINT-GOV` /
`RUN-20260726_082355_788-CONFIGMAINT-STEPREQ`):

- **`governance.rules_must_be_config_driven`** (module `governance`) — the general standard: no
  operational/process rule may exist only in `GOVERNANCE.md`/`BUILD.md`/`USER-GUIDE.md`/memory
  without a backing `cfg_*` row. Read the same way as every other `governance.*` row — `init.py`'s
  existing generic `WHERE module='governance'` print at startup (§9A/step 6) — no new code needed
  for this row specifically to satisfy its own requirement.
- **`step.required_for_runs`** (module `step`, default `true`) — the concrete fix for the trigger
  case: `init.py`'s STEP preflight and `build_verse_span_meaning_extract.py`'s `build()` both now
  read this ONE setting instead of each hardcoding its own copy of "STEP is mandatory." Flip it to
  `false` and both actually respond — proceeding without STEP rather than refusing — which is this
  project's own standing proof-of-life test for "is this a real rule or decorative" (§4).

**A second, independent bug found while wiring this in:** `init.py`'s exit code never actually
reflected the STEP-preflight outcome (`return 0` regardless of `step_ok`) — fixed alongside, full
detail in `BUILD.md` §21.

**Honest scope note, not deferred quietly:** this is the general standard plus the one concrete case
that triggered it — it is NOT a completed audit of every "must"/"never" sentence across this file,
`BUILD.md`, and `USER-GUIDE.md` for a missing `cfg_*` row. Unlike `find_orphan_configs()` (a
mechanical cfg→code key-string scan), the inverse direction — docs/memory prose → "is this backed by
config" — has no equivalent mechanical check; new instances are expected to keep surfacing and
should be fixed as found, per this standard, rather than claimed complete by a one-time sweep.

---

## 17-23. Backfill: three days of real rule changes this file missed (2026-07-29)

**Found during a full config-system audit, not self-reported at the time.** §8's own rule —
any config-rule change updates this file, same unit of work — was not honoured for the passage
method's three rewrites between 2026-07-26 and 2026-07-28. `BUILD.md` recorded every one of them;
this file did not get a single matching entry, and §16 above (2026-07-26) is, chronologically,
*before* the very retirement that happened later the same day. Backfilled here as the specific
remediation the audit's own plan requires (`PLAN-config-system-remediation-v1-20260729.md`, Phase
1 item 5) — not rewritten as if it happened on time.

**§17 — the `passage`/`verse_passage` system retired (2026-07-26, `BUILD.md` §23).** Researcher's
own words: *"the past use, and rules have moved on... there is nothing to migrate from the old to
the new."* `migration/retract_passage_system.py` deactivated 2 work packages (`build-passages`,
`passage-quality`), 2 steps, 5 `passage.*` settings, 1 `cfg_report` row + 2 sections, 4 `cfg_on_fail`
rows, 2 `cfg_write_grant` rows — and, going further than the candidate precedent (§15D), soft-deleted
the DATA itself (18,504 `passage` / 24,763 `verse_passage` rows) since the researcher wanted it out
of the way, not just frozen. Three long-open `passage.validate` escalations (`#195`/`#256`/`#262`)
answered `reject` — not "wrong," but "the system producing this finding is retired."

**§18 — `report.passage_debate` registered (2026-07-27, `BUILD.md` §27).** The Daniel passage-debate
method (four manually-written debates already existed) baked into the app as a registered scaffold
generator: new work package `passage-debate-report`, step `report.passage_debate` →
`lib/passagedebatereport.py`. Reads `method.passage_read_guidance_path`/
`method.interpretation_questions_path` (new `method`-module settings) rather than hardcoding the
method; writes a debate SKELETON only, no interpretive content.

**§19 — `passage`/`verse_passage` repurposed (2026-07-27, `BUILD.md` §28).** The researcher's own
framing: *"the passage tables becomes the record of the passages that were... debate."* The tables
§17 emptied were rebuilt as a plain completion-tracking record for the verse-fanout method
(`report.verse_span_meaning`/`report.passage_debate`), via new `lib/passagetrack.py` — 6 new
nullable columns on `passage` (`book_label`, `verse_span_meaning_path`/`_written_at`, `debate_path`/
`_written_at`/`_status`), a new `enum.passage_debate_status` (`scaffold`/`filled`), 2 new
`cfg_write_grant` rows (`report.verse_span_meaning`/`report.passage_debate` → `passage`,
`verse_passage`). **Not done in this backfill, found by the same 2026-07-29 audit that produced
it:** the OLD `cfg_column` rows this repurposing left behind (`rule`/`source`/`needs_review`/
`filled_by='passage.build'` etc.) were never updated to describe the new regime — see the audit's
own `passage-config-full-extract-20260729.md` and the `cfg_column`/`cfg_enum` fixes proposed via
`configmaint.propose` the same day this backfill was written.

**§20 — `passage-quality`/`passage.validate` reactivated, book-scoped (2026-07-28, `BUILD.md`
§31).** Deliberately scoped reactivation (`migration/reactivate_passage_quality.py`): only
`passage.validate`'s own `cfg_work_package`/`cfg_step`/one setting
(`passage.quality_report_path`)/`cfg_report`+2 sections/3 `cfg_on_fail` rows — the other 4
`passage.*` settings (`cross_chapter`/`default_rule`/`min_shared_strongs`/`review_over`) stayed
`inactive=1` on purpose, since `review_over=10` is calibrated for 1-3-verse raw spans and every
Daniel debate range (7-45 verses) would trip it as-is. New optional `-Book` param gives the check a
second purpose: a spot-check on debate-range sizes, not raw span fragmentation. The escalation
question's wording was corrected at the same time to stop naming "the char-continuity rule"
(misleading once applied to debate ranges, which never go through `passage.build`).

**§21 — `report.whole_book_read` registered (2026-07-28, `BUILD.md` §32).** New work package
`whole-book-read`, step `report.whole_book_read` → `lib/wholebookread.py`: gathers every
`debate_status='filled'` passage for a book, extracts each debate's "Emergent questions log"/
"Passage-level linkages" sections (tolerant heading match across three real variants found by
reading all sixteen Daniel files by hand — BUILD.md §30/§32/§33), lays them out with an empty
Resolution slot. Deliberately does not decide how any emergent question resolves itself.

**§22 — `governance.verse_gap_by_design` + `report.verse_gap_note` added (2026-07-29, `BUILD.md`
§35).** Researcher's ruling after measuring the full-Bible extent of the term-discovery verse gap
(2,049/31,086 verses, 6.59%, concentrated in genealogy/list-heavy books): a verse missing from
`iba.db` is BY DESIGN (verse-existence is gated on prior term discovery), not a data-integrity
error — do not escalate or attempt to backfill it. Both `report.verse_span_meaning` and
`report.passage_debate` now note each detectable gap inline and skip to the next available verse.

**§23 — Daniel `1:7-21` corrected to `1:8-21` (2026-07-29, `BUILD.md` §36).** A `passage` row whose
boundaries were mechanically self-consistent (start/end/verse_count all agreed with each other) but
substantively wrong — verse 7 belonged to the *previous* range too, a real content error the
`passage` table's own structural checks could not catch since nothing checks a boundary against the
actual verse text's content, only against its own internal arithmetic.

**What this backfill does not do:** it does not build the mechanical GOVERNANCE.md-currency check
§8 already named as follow-up (2026-07-22) and still unbuilt at the time this backfill was written
— built later the same day, §25 below.

---

## 24. `configmaint.validate` extended — inactive-reference coherence, write-grant-writer completeness, stale-`filled_by`, doc-currency (2026-07-29, same day as §17-23)

Four new checks (`lib/cfgquality.py`), verified live against the real dispatcher, not just unit
tests: **hard errors** — `find_report_step_references` (every active `cfg_report`/
`cfg_report_section`/`cfg_report_csv_table.step` must name a currently-active step — the same
discipline the existing `on_fail.step` check already had, extended to three tables that were never
checked against anything before); `find_unknown_write_grant_writers` (every active
`cfg_write_grant.writer` must resolve to an active step or a declared `cfg_enum writer_identity`).
**Advisory** (judgement calls, escalated like orphans/justification, not hard-failed) —
`find_filled_by_referencing_inactive_step` (surfaced 22 `cfg_column.filled_by` rows across the
candidate/passage retirements naming a retired step — §2/A2 of `passage-config-full-extract-
20260729.md`, now a standing check instead of a one-off finding); `find_stale_governance_docs`
(compares `GOVERNANCE.md`'s own mtime against the newest applied `cfg_change_detail` row — the
mechanical version of §8's 2026-07-22 follow-up, built four weeks-worth-of-calendar-time-equivalent
later than promised, same day this note was written).

---

## 25. `inactive` made real at runtime — escalation #334 closed (2026-07-29, later the same day)

Until this, `inactive` was **validator-only metadata** — confirmed by direct inspection: not one of
`lib/cfg.py`'s read methods filtered on it, so "retiring" a `cfg_*` row changed nothing about
whether the app actually still read and applied it. §15D built the column and the
`configmaint.validate`-side exclusion in 2026-07-23; it also explicitly named, and deferred,
runtime enforcement: *"Blocking execution outright is a different, not-yet-made decision... flagged
for whenever the actual replacement system is being designed."* That moment arrived with escalation
#334, raised 2026-07-29: a near-miss running `Set-Candidates.ps1 -Book Obad`, a retired work
package, caught only by a manual DB query.

**Fixed.** `AND inactive=0` added to every `Cfg` read method whose table actually carries the
column (checked directly, not assumed — `cfg_book_order`/`cfg_connection`/`cfg_api` all have it too,
correcting `PLAN-config-system-remediation-v1-20260729.md`'s own wrong guess). `run.py:run_step()`
now refuses (uncaught `PermissionError`, before any DB write) if the requested work package or step
is `inactive=1` or unknown. A second bug, found only by testing the actual near-miss scenario
rather than trusting the unit-level fix: the three CHAINED work-package scripts (`Set-Candidates.ps1`/
`Build-Passages.ps1`/`New-Word.ps1`) pre-fetch their step list via `Cfg.sequence()` and loop over
it — an empty (correctly-filtered) sequence made the loop run zero times and fall through to a
FALSE "COMPLETE" banner, worse than the original silent-execution gap for a "did this actually
work" question. Fixed at its source, once, in the shared `ps/_lib/Notify.ps1`
(`Test-IbaWorkPackageActive`), not per-script. Full account, including every verification run:
`BUILD.md` §38.

**§25a — remaining §17-24 proposals closed out, same day.** Researcher approved the outstanding
`passage_rule` enum deactivation, `passage.source`/`.needs_review` `filled_by` clears, and all 6
`writer_identity` values — `passage_rule`/`passage_source` and `passage.rule`/`.source`/
`.needs_review` are now symmetric (§19's asymmetry note above resolved). 19 `cfg_column.filled_by`
findings remain genuinely open (not a duplicate/artifact — tracked by §24's standing check, not
raised again as individual escalations). Full detail: `BUILD.md` §38's closing note.

**§25b — the 19 remaining `filled_by` findings closed, same day.** Researcher asked to see the
actual live rows and get ready-to-run commands rather than a fill-in-the-blank template — both
given, then executed at the researcher's go-ahead: 10 dormant clears (`candidate_seed`/
`span_candidate`, naming retired `candidate.seed`/`.set`/`.load` steps) and 9 corrections to the
real current writer (`passage`/`verse_passage`, now naming `report.verse_span_meaning /
report.passage_debate (via lib/passagetrack.py)` instead of retired `passage.build`). `lib/
cfgquality.find_filled_by_referencing_inactive_step` now returns **0**, confirmed both directly and
live through the real dispatcher. Full detail: `BUILD.md` §38's second closing note.

## 26. `cfg_utility` registry built — Phase 4, on direct instruction (2026-07-29, later the same day)

The one deliberately-deferred piece of `PLAN-config-system-remediation-v1-20260729.md`, built after
the researcher pointed out that "proceed to implement the plan" already covered it — sequencing it
after the higher-risk Phase 2 work was a scoping call that should have been checked back on, not
made alone. New table `cfg_utility` (module/file_path/purpose/inactive), one row per `iba/app/
lib/*.py` module (23, enumerated directly from disk), added via a direct schema bootstrap
(`migration/bootstrap_cfg_utility.py` — DDL, same class of exception as the `inactive` column
itself) since `configmaint.propose` cannot create tables. Two new advisory `configmaint.validate`
checks close the completeness gap `cfg_step`/`REPORT_STEPS` already closed for *steps* but never
existed for library utilities: an unregistered-module check, and a config-density check that found,
live, 14 of 23 modules touch zero `cfg_setting`/`cfg_enum` — 13 legitimate (helpers whose caller
resolves config for them) and one real, already-known gap (`lib/lexiconparse.py`), both surfaced
for judgement rather than either being silently accepted or forced into config that doesn't fit.
Full account: `BUILD.md` §39.

## 27. `cfg_step.kind` — operations/utility classification, dispatch requires it (2026-07-30)

Corrected framing from the researcher: the operations/utility split is real, but it belongs on the
*handler modules* (`raw`/`registry`/`lexicon`/the passage-debate-prep steps/`narrative` vs.
`configmaint`/general reporting) — `cfg_utility` (§26) only ever covered `lib/*.py`, leaving exactly
what the researcher named: *"the handler modules are not in the table."* Then: *"you need to build
controls that routines not in the tables need special permission to be use."*

New `cfg_step.kind` column (`operations`|`utility`, `enum.step_kind`) — on `cfg_step`, not a new
table, because the split is per-step (`reports.py` itself mixes both). All 35 steps classified in
one bootstrap pass (`migration/bootstrap_step_kind.py`): 22 operations, 13 utility. `run.py`'s
dispatch gate (§25) now also refuses a step with `kind IS NULL` — "special permission" is the
existing `configmaint.propose` approval gate, not a separate bypass; classifying a step already
requires that same sanctioned path. New hard `configmaint.validate` check
(`find_unclassified_active_steps`) keeps a future unclassified step from silently existing. Full
account, including the live refusal test: `BUILD.md` §40.

---

## 28. `cfg_enum.escalation_type` gains `report-stop` and `crash` (2026-07-30, escalations #384/#385, both approved+applied same day)

Until now `escalation.type` only ever held `interactive` (a `raise`/word-scoped item) or `prompted`
(a real dispatcher pause-continue awaiting a decision, which *resumes* the run on answer — §9). The
2026-07-30 rule (recorded in `run.py`, §-adjacent to the `report-stop` path in `cfg_on_fail`): every
`report-stop` condition now ALSO writes a recorded, visible `escalation` row when it fires, not just
a silent `run.state` flip to `failed` — so a hard-stop failure shows up in `Escalation.ps1 -Action
List`/`escalation-list.md` the same way a real pause does, distinguishable from `prompted` by `type`.
A `report-stop` escalation is a **terminal record, not a live pause** — answering it does not resume
anything (there is nothing to resume; the run already ended). Approved via `configmaint.propose`,
applied (`INSERT cfg_enum escalation_type='report-stop'`) after fixing the id/run_id resolution bug
that had blocked the approval from going through — see `BUILD.md` §43. The sibling value, `crash`
(uncaught exception, caught+recorded+re-raised by `run.py`; escalation #385), is **also now
approved and applied** (`INSERT cfg_enum escalation_type='crash'`) — resumed the same way once the
researcher's own `Escalation.ps1 -Action AnswerRun` answer was recorded; see `BUILD.md` §44. Both
values are live in `enum.escalation_type` as of 2026-07-30T05:14:23Z (the DB's own
`cfg_change_detail` timestamp for the `crash` insert — the authoritative record of when this
became true, not this doc's edit time).

*Correction, same day:* this section originally said `crash` was "proposed but not yet approved"
— true when first written, but the researcher applied it shortly after and this entry wasn't
updated in the same unit of work, which is exactly what `find_stale_governance_docs` (§5B) exists
to catch. That check flagged this as stale and Claude Code initially misread the finding as a
sandbox clock artifact rather than checking `cfg_change_detail` directly — a real content-currency
gap, now fixed here.

---

## 29. Validation extended past `cfg_setting`/`cfg_enum` — every `cfg_*` table now has SOME usage or referential check (2026-07-30, later same day)

Researcher's factual challenge, confirmed by direct mapping: `find_orphan_configs` (§5B) — the
check asking "is this genuinely consumed, not just structurally valid" — had only ever covered
`cfg_setting`/`cfg_enum` since it was written. `cfg_book_order`, `cfg_connection`,
`cfg_candidate_rule` had ZERO checking of any kind; `cfg_report_csv_table.table_name` had a step-
reference check but nothing confirming the table name itself is real.

**Closed, four new checks (`lib/cfgquality.py`, full account: `BUILD.md` §51):**
`find_orphan_book_order` (is `cfg.book_order()` called anywhere + duplicate book/ordinal
detection), `find_orphan_connection_keys` (same per-file co-occurrence methodology as
`find_orphan_configs`), `find_orphan_candidate_rules` (two-directional — a called kind with zero
active backing rows, skipped while both real callers are inactive per the 2026-07-23 retraction;
an active kind no code ever asks for, unconditionally), `find_bad_report_csv_table_references`
(hard structural check — a `table_name` must be a real DATA or `cfg_*` table).

**Every `cfg_*` table now has at least one form of check** — either a referential/structural check
(unchanged, `_validate_live`) or a genuine usage check (`find_orphan_configs` + the four new ones).
Verified end to end: `Config-Maintenance.ps1 -Step Validate` returns clean `ok` — no coherence
errors, no advisory findings — the first fully clean validate run of this whole 2026-07-30 session.

---

## §30. `report.book_narrative_generate` — the first step that spends real money, and how config governs that (2026-07-30, later same day)

Every step registered so far either reads/writes this app's own DB or makes a free local STEP call.
`report.book_narrative_generate` (full build account: `BUILD.md` §52) is the first to call an
external, pay-as-you-go API — the Anthropic Messages API, to generate a book's inner-being
narrative from its filled passage debates. Two governance points worth recording as rules, not just
implementation detail:

1. **`ANTHROPIC_API_KEY` is read from the environment or the repo-root `.env`** — the one deliberate
   exception to this app's own "no secrets, no `.env`" boundary (`USER-GUIDE.md` §1). It is not a
   new provision: it is the same key `scripts/_run_ve_reads_governed.py` and the repo-root
   `_apply_*_via_api_*.py` scripts already use for the legacy (non-IBA) pipeline. This app reads it,
   it does not own or duplicate it.
2. **Spend is config-gated, not just estimated.** `narrative.generate_max_cost` (a `cfg_setting`,
   changeable via `configmaint.propose` like anything else) is a hard ceiling checked against the
   PRE-call estimate — over it, the step refuses outright (`cost-cap-exceeded`), no pause, no
   escalation, nothing spent. Under it, the step still does not spend automatically: it escalates
   (`needs-approval`, pause-continue) with the estimate in the question, the same shape
   `registry.create`/`configmaint.propose` already use for anything that writes or spends, and the
   live call is made only once that exact run_id comes back answered `approve`. The model, both
   token/cost rates, the output-token ceiling, the output filename pattern, and the usage-log path
   are all `narrative.*`/`method.*` settings too — per the researcher's own instruction the same
   day, nothing about report content, defaults, narrative style, or filing lives as a literal in the
   handler.

---

## §31. The book-by-book pipeline split into 3 module entry points — session-scope guidance as config, and a real global-uniqueness rule found live (2026-08-02)

**Trigger.** Hosea (book 6) was run end-to-end — 14 chapters of `report.verse_span_meaning` +
`report.passage_debate` fill-in, then `report.whole_book_read`, then
`report.book_narrative_generate` — in one unbroken Claude Code session, immediately after an
equally large Micah cycle the same day (`BUILD.md` §54 has the full diagnostic:
`iba/app/reports/token-consumption-diagnostic-20260802.md`, ≈1.13M tokens moved through one
session, daily+weekly caps both exhausted). The researcher's instruction: separate the pipeline
into three distinct modules — chapter generation (data + debate), book overview/summary, book
narrative — each with its own PS entry point, and record the recommended ~3-chapters-per-session
pacing as config, not just chat.

**Advisory session guidance belongs in `cfg_setting` even when the code cannot enforce it.**
`passage.debate_session_chapter_guideline` (module `passage`, value `3`) records the rule per
`governance.rules_must_be_config_driven` (§16) — but nothing in `run.py` gates on it, because the
thing it bounds (how many chapters' worth of manual interpretive fill-in happen in one Claude Code
conversation) is not something any dispatched step can see or measure (established the same day,
in chat, before this build — the debate-fill step is never dispatched through `run.py` at all).
Recording an unenforceable-by-code rule as `cfg_setting` is a deliberate exception to "config
should be enforced," not a gap: the alternative was leaving it in memory/chat only, which §16
already forbids for exactly this reason (rules drift when only one of several enforcement paths
gets updated).

**A real coherence rule, found by actually running `configmaint.validate`, not assumed.** The
initial plan (recorded in chat before this build) was to add the three new chained work packages
(`chapter-generate`, `book-narrative`; `whole-book-read` needed no change) while leaving the four
old standalone ones (`verse-analysis-report`, `passage-debate-report`, `book-narrative-generate`,
`book-narrative-validate`) active too, as lower-level recovery tools. Running `configmaint.validate`
after applying that plan failed hard (`report-stop`, not advisory): `cfg_step.step` must be globally
unique across `work_package`, not just unique within one (§24's own check,
`find_filled_by_referencing_inactive_step`'s sibling) — `escalation.pending_for_word`/
`answered_for_word` and `cfg_on_fail` both match on `step` alone, with no `work_package` in the
`WHERE` clause, so two work packages sharing a step name collide at runtime. The four old work
packages (and their now-duplicate `cfg_step` rows) were retired (`inactive=1`) instead — the
"exactly 3 entry points" outcome the researcher asked for turned out to be a real constraint, not
just a tidiness preference. Full build account: `BUILD.md` §54.

**A known false-positive accepted, not silently dismissed.** Retiring the old `cfg_step` rows while
the same step NAMES remain active under their new work packages trips
`find_filled_by_referencing_inactive_step` (§24) — it flags any step name with *any* `inactive=1`
row, without checking whether an active registration of the same name exists elsewhere. The 6
resulting `passage.*` column findings were reviewed and confirmed accurate (still filled by the
same, still-active steps, just re-homed) — answered on the `configmaint.validate` escalation with
that reasoning recorded, not silently cleared. `find_filled_by_referencing_inactive_step` itself is
unchanged; this is a documented limitation, not a bug fixed today.

**Per-step separation gates content, not invocation (2026-08-07, added retroactively next to the
constraint that makes it work).** Found live building `Debate-Run.ps1` (`BUILD.md` §72): running
Dan 1's debate meant discovering, one manual PS invocation and one failure message at a time, that
`hib.set` → `passage.build` → `phenomenon.set` → `operation.set` → `closing.set` are always
sequentially dependent, yet had to be typed as five separate commands. Researcher's correction,
direct: "having different steps is only necessary if the steps are required to enforce the
controls of not trying to do everything at once... There is no need to type in each ps command for
all the steps by hand if these steps always is run as a package and is dependent on each other."
The distinction that resolves this, stated as a standing rule: **a step boundary that exists to
gate genuine analytical judgement (a fresh JSON payload, an actual reading pass) stays a real
boundary — that discipline is never removed.** A boundary that exists only because nobody wrote the
orchestration is a gap, not a control, and should be closed the same way any other chained work
package already closes it (`cfg_setting`-driven sequencing over the EXISTING step registrations —
§31's "global step-name uniqueness" constraint above is exactly why this can't be done by
registering the steps a second time under a new work package). Applied: `passage.debate_run_sequence`
or a `debate-run` PS script that sequences `operations-ingest`/`build-passages` steps in order,
stopping only where a step's own DB precondition genuinely isn't met yet.

---

## §32. `governance.rules_must_be_config_driven` (§16) violated again the same day, this time by the AI, not just found live in old code — `cfg_report_section` brought in line with the v1.5/v1.4 method restructure (2026-08-02, later same day)

**Trigger — a researcher correction, not a self-caught bug.** The same session that restructured
`WA-passage-read-guidance`/`WA-interpretation-questions` to v1.5/v1.4 (`BUILD.md` §35's drift-and-
restructure entry) repointed the two `method.*` `cfg_setting` rows at the new files and called the
fix done. Asked to redo the Amos 1-3 debate under the new method, the researcher stopped the
approach before any content was written: *"it is because you are not working all the rules through
config, but you think by updating the instruction documents you can get away with it — so you are
not adhering [to] the governance policies when making updates."* Checked against the live
`cfg_report_section` table: correct. The two `cfg_setting` doc-pointer rows were genuine config, but
Part C's actual structural rule — phenomena register (Phase 1) as its own section, ahead of
operations (Phase 2), with a closing validation section (Phase 3) — existed only as prose in the
new `.md` files. `cfg_report_section` for `step='report.passage_debate'` still had its old 6-section
shape from before the restructure, and `lib/passagedebatereport.py` still emitted the old single
per-verse block. §16's own honest-scope note ("new instances are expected to keep surfacing... fixed
as found, rather than claimed complete by a one-time sweep") is exactly what this is: not a new kind
of gap, the SAME kind, found live a second time in one day — this time in a change the AI itself had
just made, not in pre-existing code.

**The general lesson, stated plainly.** Editing a method/instruction doc and repointing a
`cfg_setting` that names *which file* is current is necessary but not sufficient when the doc also
specifies a *structure* (section order, required sections) that some other `cfg_*` table already
governs mechanically. `governance.rules_must_be_config_driven` (§16) requires the structural rule
itself to be written into that table — here, `cfg_report_section`, which `reportkit.render_scaffold`
already reads for every report's headings/order/ToC (§9C/§13) — not left for the AI to remember to
apply by hand from the doc's prose each time a scaffold is generated.

**Fix — 7 governed `cfg_report_section` changes, proposed/approved/applied via `configmaint.propose`
per §3A** (escalations #436-442, chat-approved by the researcher then answered
`AnswerRun -Decision Approve` per row, never a silent write): `phenomena_register` inserted at
ordinal 1, `verses` renamed to `operations` (ordinal 2, heading updated to "Per-verse operations
(Phase 2 output)"), `linkages`/`insufficiencies`/`emergent` shifted to ordinals 3/4/5,
`validation` inserted at ordinal 6, `open_decisions` shifted to ordinal 7 — the exact 8-section
order Part C specifies. `lib/passagedebatereport.py` updated to match: `_verse_block()` split into
`_phenomena_block()`/`_operations_block()`, a `validation` section body added, and — found in the
same pass — `Q12` (added to the interrogative in v1.4) restored to the per-verse scaffold, which had
never carried it even before this fix. Full change detail: `BUILD.md` §55.

---

## §33. `cfg_index` — indexes are now config, not a per-table hand decision; cascade guards made a general rule, not a `hib.set` special case (2026-08-07)

**Trigger.** Researcher's own live discovery: the debate schema had no real FK constraints, no
indexes, and a HIB correction could silently orphan already-written phenomena — widened to a
full-app review (a-l). Root cause + full change detail: `BUILD.md` §79. This section records the
two additions that change HOW config governs the schema going forward, not just what got fixed once.

**New config table: `cfg_index(table_name, name, col, ordinal)`.** Same shape as `cfg_unique`.
`build_data_tables()` (`lib/db.py`) already built real `FOREIGN KEY`/`UNIQUE` DDL from `cfg_column`/
`cfg_unique` — it had never had ANY mechanism for plain secondary indexes, on any table, ever. That
gap is now closed the same way every other piece of this schema is governed: a data table's indexes
are config rows (`Cfg.indexes(table)`), not a decision left to whoever writes that table's migration.
**The rule this establishes:** every FK column on every data table gets an index — mechanical,
checkable (`populate_cfg_index_rows.py` is re-runnable and syncs `cfg_index` to current
`cfg_column.fk` on demand), not something a future migration can quietly skip the way the original
debate-table migration skipped FK constraints entirely.

**Also fixed in the same builder: composite `UNIQUE` was wrong for any table with a `deleted`
column.** A plain table-level `UNIQUE(...)` collides with this app's own soft-delete-and-reconcile
convention the first time a row is ever corrected (soft-deleted, reinserted under the same natural
key). `passage` had already hand-fixed this once (`idx_passage_range_live`) by bypassing the
builder; the builder itself now knows the rule (`lib/db.py:table_ddl()`) — a partial unique index
(`WHERE deleted=0`) for any table with `deleted`, plain inline `UNIQUE` otherwise.

**Cascade-guard convention generalised.** `passage.py` already had the right rule (§67: a
correction updates the existing row in place, same id, so it can never orphan a child row).
`hib.set`/`phenomenon.set`/`operation.set` (built in the same debate-schema work, §61-70) never got
it — each soft-deleted-and-reinserted a `changed` item under a new id, silently orphaning any
already-written `phenomenon`/`operation`/`passage_linkage` still pointing at the old one. Fixed
identically in all three, plus a genuine new rule: `removed` items are now checked for live
dependents FIRST and refused outright if any exist. **The general rule this establishes:** any
writer that reconciles (soft-delete-and-correct) a row other tables can point at must (a) preserve
that row's id across a `changed` correction, and (b) refuse a `removed` correction while a live
dependent still exists — not a `hib.set`-only convention; the next reconciling writer built in this
app is expected to follow it too, the same way `governance.build_md_on_code_change` etc. apply to
every future code change, not just the one that prompted the rule.

**Scope note, honestly recorded:** the `cfg_*` config tables themselves (23 of them) were not
brought into this FK/index retrofit — a different reference-integrity problem (config-to-code,
several legitimately reference not-yet-built targets during a pending `configmaint.propose`
approval), already served by `lib/cfgquality.py`'s orphan-detectors, not by DB-level FKs. Not an
oversight; a recorded scoping decision (`BUILD.md` §79 has the full reasoning).

---

## §34. `debate_change_detail` — a shared per-row CRUD audit trail across all 5 debate writers; §33's "preserve id" rule extended to child tables (2026-08-08)

**Trigger.** Researcher direction, following a `hib.set` scope/CRUD reconciliation
(`PLAN-revise-hib-set-scope-and-crud-v1-20260808.md`): "each entry (insert, update, delete) must
have entries in the table to be able to trace the changes to the run... full CRUD is required for
all table update controls." Full change detail: `BUILD.md` §81/§82.

**New data table: `debate_change_detail(run_id, writer, table_name, op, where_json, set_json,
before_json, applied_at)`** — mirrors `cfg_change_detail`'s own shape exactly (the existing per-row
audit trail for `configmaint.propose` writes), kept separate since this is data-write audit, not
config-write audit. Shared by all 5 debate writers (`hib.set`, `passage.build`, `phenomenon.set`,
`operation.set`, `closing.set`) via one lib function, `lib/debateaudit.py:log_change` — centralised
rather than duplicated per-handler (unlike this app's small `_may`/`_now` helpers, which each
handler file still defines locally) because the audit shape has to stay byte-identical across all
five. One `cfg_write_grant` row per writer → `debate_change_detail`, same governance as any other
table write. (Originally built as `hib_change_detail`, `hib.set`-only; renamed once its scope
broadened to every writer, `migration/rename_hib_change_detail_to_debate_change_detail_
20260808.py` — same rename-on-outgrown-name precedent as `span_reading` → `verse_lexical`.)

**§33's "preserve id across a `changed` correction" rule extended down to child tables.** §33
fixed this for the parent rows (`hib`/`phenomenon`/`operation`) but explicitly left
`hib_referent_option`/`operation_party` on the older soft-delete-and-reinsert-under-a-changed-parent
shape ("no downstream referent, so no id to preserve" — reasonable at the time, since nothing
pointed at their own id). The audit trail changes that calculus: a stable id across a correction is
now itself the more traceable shape, not just the orphan-safe one. Both upgraded to real per-row
CRUD, matched by ordinal position within their parent — a position whose content is unchanged is
left untouched (no write, no log); `closing.set`'s four list tables (`passage_linkage`/
`passage_insufficiency`/`passage_emergent_question`/`passage_validation_note`), found to still be
using the old soft-delete-and-reinsert-under-a-`changed`-item shape too (missed by §33's original
sweep, which only reached the operations-schema writers), were fixed the same way.

**Corollary for the next writer.** Same standing instruction §33 already established, restated
because it now covers one more layer: any writer that reconciles a row — parent OR child — must
preserve that row's id across a `changed` correction and log every insert/update/delete to
`debate_change_detail`. Not a `hib.set`-only convention.

**Housekeeping, same session:** `lib/debateaudit.py` (this section's own new module) registered in
`cfg_utility` and marked `config_exempt` — a pure DB-write helper with no `cfg.setting()`/
`cfg.enum()` usage by design, same class as the other already-exempt utilities (§2's registry). Not
a new rule, an instance of the existing `config_exempt` convention — noted here only because
`configmaint.validate`'s stale-doc check compares this file's mtime against the newest applied
config change regardless of whether that change was itself rule-shaped.

---

## §35. `oneoff_path()` never archived — the OTHER report-writing path §60's fix missed, fixed and now actively detected (2026-08-08)

**Trigger.** Researcher, inspecting `iba/app/reports/`: *"this folder is really dirty... not sure
if it is because the configs are incoherent, or if you just do not comply with the rules."*
Investigated against the live code, not assumed either way.

**Root cause: §60's "every report writer already funnels through this one function" was wrong.**
§60 (2026-08-05) fixed `write_report()` to archive the previously-live version alongside every
version bump. `lib/reportkit.py` has a SECOND, separate report-writing path — `oneoff_path()`,
used for "investigatory" reports with no `cfg_step`/`cfg_report` row (§15) — that bypasses
`write_report()` entirely: a caller gets a path from `oneoff_path()` and writes to it directly.
§60 never touched this path. It versioned correctly (`-v2`/`-v3`/...) but never archived anything,
so every report going through it (every `hib.set`/`phenomenon.set`/`operation.set`/`closing.set`
reconciliation report, the `hib.set`-by-type report, `build_debate_report.py`, both
`build_verse_span_*_extract.py` tools) accumulated its FULL lineage flat in the live folder,
forever, since before §60 even existed. Not a compliance failure by whoever called `oneoff_path()`
— every caller used it exactly as documented; the mechanism itself had the gap.

**Fixed at the source, not per-caller.** `oneoff_path()` (`lib/reportkit.py`) now archives whatever
is currently live for a topic-day before computing the next version — same "archive alongside
versioning" rule §60 established, same live-folder-holds-exactly-one-current-file-per-report
outcome, applied via a NEW shared helper (`reportkit.group_oneoff_versions`/
`archive_oneoff_clutter`) rather than copying `write_report`'s own version-numbering scheme (the
two paths' naming conventions differ — `{topic}-{date}[-vN]` vs `{stem}-v{n}-{date}` — kept as-is,
not unified, to avoid a breaking rename across every existing report file). New `cfg_setting`
`governance.oneoff_report_archive_dir` (default `"archive"`, same shape as `cfg_report.archive_dir`).

**Existing clutter swept, not left for the fix to slowly catch up on.**
`migration/archive_oneoff_report_clutter_20260808.py` (idempotent) — reused the exact same
grouping/archiving helper `oneoff_path()` itself now calls, so the one-time cleanup and the
going-forward behaviour are provably the same rule, not two hand-written copies of it. 18 files
across 10 report lineages archived (kept the newest live), verified 0 remaining.

**The "never happens again" half: an active detector, not just a code fix trusted to hold.**
`cfgquality.find_report_version_clutter()` — scans `governance.oneoff_report_dir` for any report
lineage with more than one version simultaneously live, wired into `configmaint.validate`'s
findings dict and `CONFIG-REPORT.md` (mirrored the same way every other advisory check in this app
is). If `oneoff_path`'s own archiving is ever bypassed (a future caller writing to a hand-built
path, or the archiving logic itself regressing), this surfaces it as a real advisory finding on the
next `configmaint.validate` run — matching this app's standing convention that a rule is enforced,
not just documented and trusted.

**Verified live**, not assumed: two consecutive real `hib.set` calls confirmed the SECOND call
archives the FIRST call's freshly-written report (both the reconciliation report and the
`hib.set`-by-type report) before writing its own next version — live folder held exactly one file
per stem throughout, full lineage in `archive/`. `find_report_version_clutter` returns 0 findings
before AND after. Full work record: `BUILD.md` §83.

## §36. `report.word_registry_span` — new registered report, word_registry -> Strong's -> parse
meaning -> span analysis (2026-08-09)

Promoted from an ad-hoc prototype (`tools/word_strong_span_report.py`, built the same session to
answer "for a registry word, what do its linked Strong's actually resolve to and how do they show
up in the text") into a real registered report, per the researcher's direct instruction: "add this
report into the app as a standard report, define it in the configs, and ensure that it has a
powershell script to run the report."

**What it shows**, for one `word_registry` word: every linked Strong's (`word_strong`), each with
its gloss/transliteration/count (`strong`), its full parse-meaning breakdown
(`strong_meaning_parsed` — falling back to the base lemma's tree for suffixed sub-entries like
`H3372G`, which have none of their own), and its **unique surface-span applications** — the
distinct `span.surface` text forms tagged with that Strong's across `verse_lexical`, each with an
occurrence count and one example verse (reference + text). "Unique span" was checked against real
data before building: `resolved_sense` turned out to be fixed per Strong's in this DB, so surface
diversity (e.g. G5399 realised as "afraid"/"fear"/"feared"/"awe"/"terrified"/… — 13 distinct forms)
is what actually carries the signal, not sense grouping.

**Registered per the infrastructure-registration carve-out** (§9B/this section's own precedent —
`bootstrap_verse_analysis_report.py` et al.): direct, idempotent `cfg_*` inserts
(`migration/bootstrap_word_registry_span_report.py`), not `configmaint.propose` row-by-row — the
researcher's own explicit request IS the up-front design approval that carve-out requires. New
work package `word-registry-span-report` (own PS script, `WordRegistrySpan-Report.ps1 -Word
<word>`, matching the one-script-per-standalone-report pattern already used for
`strong-meaning-report`/`span-analysis-report`), scope `word`, step `report.word_registry_span`.
`cfg_report` (title/ToC/`naming_scheme='dated'`, same versioning-with-archive convention every
other report gets from `reportkit.write_report`) + 2 `cfg_report_section` rows (Overview /
Strong's breakdown) + one `cfg_on_fail` row (`word-not-found` -> `report-stop`, mirrors
`report.word`'s own row exactly). New setting `report.word_registry_span_output_dir` — a **new
folder**, `iba/app/verse-analysis/word_registry/`, distinct from the per-book
`verse-analysis/{Book}/` folders the rest of that tree already holds, since this report is
word-registry-scoped, not book-scoped. `lib/wordregistryspanreport.py` also needed its own
`cfg_utility` row (`migration/bootstrap_cfg_utility.py`, re-run — auto-discovers any new `lib/*.py`
module, idempotent) before `configmaint.validate` came back clean.

**Verified live**: ran for `fear` (62 linked Strong's) — wrote
`iba/app/verse-analysis/word_registry/fear-strong-span-v1-20260809.md`; ran for a nonexistent word
— clean `report-stop` (exit 3), no crash. `configmaint.validate` clean after both migrations.
`USER-GUIDE.md` updated with a run example.

## §37. `report.word_registry_span` clustered by meaning — a working, meaning-first ToC
(2026-08-09, same day, later still)

§36's first output was reviewed immediately and corrected: a flat per-Strong's list with no real
in-body table of contents wasn't what was asked for. Researcher: cluster Strong's with similar
meaning together (his own example: "timidity, be timid, timid" — G1167/G1168/G1169), and the ToC
must be built off the *meaning*, not the Strong's number, and must actually link.

**The clustering itself uses `strong_related`** — an existing table (STEP's own root-family
cross-reference data) the report wasn't reading before. Restricted to edges where both ends are
already among the word's own linked Strong's, then grouped by union-find. This is a genuine data-
grounded reduction, not an invented similarity heuristic — checked live against `fear` before
committing to the design: 62 Strong's -> 33 clusters (12 real multi-member root families, 21
singletons), and the researcher's own three-way example (G1167/G1168/G1169) clustered together
exactly as named.

**Full design/rationale/verification record: `BUILD.md` §86** (this section stays short — the
detail belongs in one place, not duplicated).

One general point worth recording here rather than only in BUILD.md: `reportkit.anchor()` (was
`render_scaffold`'s private `_anchor`) is now public, because this is the SECOND report generator
that needed to build its own in-body sub-ToC beyond what the static `cfg_report_section` table can
represent (per-run, per-word cluster counts can't be pre-registered rows) — any future report
generator with the same need should call `reportkit.anchor()`, not hand-roll a second slugging
rule that could silently drift from the one `render_scaffold` itself uses.

## §38. ToC links fixed for every registered report, not just one (2026-08-09, same day, later
still)

The researcher's own testing caught what §36/§37 missed: "I notice that links in all of the
reports in the app does not work as a link" — this was never report-specific. `render_scaffold`
computed a heading's anchor itself and trusted the Markdown renderer to independently generate the
identical id — a real gap, since different renderers slug punctuation differently (this app's own
`anchor()` collapses repeated hyphens; GitHub's own slugger does not). Fixed at the shared source,
not per-report: `render_scaffold` now emits an explicit `<a id="...">` immediately before every
heading and links the ToC to that exact id — no renderer's own slugging is trusted anymore. Every
report that calls `render_scaffold` is fixed by this one change.

Full record (including a second, real over-merging bug caught and fixed the same session in the
new English-gloss ToC grouping added to `report.word_registry_span`): `BUILD.md` §87.

## §39. Escalation reset — own rule table, wider vocabulary, `configmaint.propose` recalibrated as one path among several, not the default gate (2026-08-16)

**Researcher ruling, 2026-08-16** (full digest `outputs/markdown/iba-table-review-response-v1-
20260816.md`; build record `BUILD.md` §113): the escalation table's original three-way
approve/reject/revise shape, and the `governance` module's drift into per-incident notes rather
than standing rules, were both named as root causes of process inconsistency this session. Two
governing corrections, both now live:

1. **`escalation` is no longer approve/reject/revise-only.** `next_action` (renamed from `answer`)
   adds `hold`/`noted`; a new `resolution` column records what was actually done — nothing
   previously captured that. `next_action_assigned_to`/`answered_by` (Claude|Researcher) route and
   attribute every row. Rule text for the utility's own operation (source-classification,
   duplicate-suppression, module-blocking, resolution-precedence, chat-routing) now lives in its
   own table, `cfg_escalation` — same pattern §33/§34 already established for `cfg_index`/
   `debate_change_detail`: a mechanism's own control rules get their own table, not scattered
   settings.
2. **`configmaint.propose`'s approve/reject/revise gate is not the default path for every
   escalation.** Researcher, verbatim: *"not all escalations goes through propose / approved, lots
   of it would raise, schedule, notify... The real reason why I am using you for the App is to use
   your special skills, and only when you really need my agreement on choices or different
   approach, then channel it back to me."* Practical effect: a fully-worded, already-settled
   `cfg_setting` change (this session wrote 22 of them) is applied directly and recorded, not routed
   through a proposal-and-approval round; the gate is reserved for genuine judgement calls. This
   sits alongside, and narrows, `governance.rules_must_be_config_driven` (§16) — the standing rule
   that a process rule must be config-backed is unchanged; what changed is that not every config
   write needs its own approval cycle to count as properly governed.

Both corrections are themselves now `cfg_setting` rows (`governance.escalation.scope`,
`governance.utility.config`, `escalation.control_objectives`, `escalation.control_process`, module
`escalation`/`governance`) — per `governance.governance_md_on_rule_change`'s own requirement, this
section documents the config, it does not hold a rule the config does not.

**Deferred, not decided here:** wiring `cfg_escalation.module_blocking` into `run.py`'s dispatcher
(rule recorded, `enforced_by` says "not yet wired"); the `governance.oneoff_report_dir` folder
relocation the CSV proposed (a filing decision, tracked as its own escalation, not applied). Both
are real open items, listed in full in `BUILD.md` §113 and the response doc — not silently dropped.

**§39 correction, same day, later still — declared rules that turned out not to be wired.** The
researcher asked directly, reading USER-GUIDE.md's stale §4.2: had the new vocabulary this section
describes actually been built into the code, or just documented? Checked rather than assumed:
`type` has no behavioural effect anywhere (disclosed as classification-only, not fixed — that's a
legitimate design, just needed saying); `next_action='hold'/'noted'` were silently mishandled as
rejections by every one of the 7 handlers that resume a real pause (both always wrote
`state='completed'`, and no handler understands anything but approve/reject); `state='re-assign'`
was declared here and in `cfg_escalation` and never once produced by any function. All three fixed
— `hold`→`on-hold`, `noted`→`closed` (neither satisfies a dispatcher's `answered_for_run` lookup
any more, so a real pause answered either way correctly stays paused rather than being misread as
a decision), new `reassign_run()`. Full record: `BUILD.md` §116.

## §40. `configmaint`'s own machinery made config-driven, not just what it governs (2026-08-18)

Five mechanism changes to `configmaint.py`/`cfgquality.py` themselves — not new content in a
governed table, changes to the governing code's own behaviour, which is why they're recorded here
rather than only in `BUILD.md`'s build history (full content/data detail: `BUILD.md` §§145-147).

**`configmaint.propose`'s known-table list is no longer a hardcoded tuple.** `CFG_TABLES` (a
Python literal, edited by hand every time a new `cfg_*` table was created — missed twice inside
24 hours, escalations `#712`/`#715`) is retired; `_known_cfg_tables(conn)` derives it live from
`cfg_table`. A new `cfg_*` table becomes proposable the moment its own migration registers it —
`governance.new_utility_registration_timing`'s "same unit of work" requirement is now sufficient
on its own, no second file to remember.

**`_validate_live`'s schema-integrity checks no longer hardcode `database='iba'`.** They loop over
`cfg_enum 'project_database'` — collision-safe per database still (escalation `#653`'s original
concern), but no longer blind to `bible_research.db`'s own coherence, which had literally never
been checked before (found live: 7 tables there with the same compound-PK registration defect 11
`iba.db` tables had, invisible until this loop existed).

**A `database.<name>.path` structured pair replaces `governance.project_databases`'s prose for
anything that needs to iterate "every known project database" programmatically** — the prose
setting stays for a human reader, per `cfg_behaviour_rule
documentation.single-authority-pointer-not-copy` (a fact has one authoritative FORM per
consumer-kind, not one authoritative row full stop). `Cfg.database_path(name)` is the real
consumer, wired into `init.py`'s startup sequence as a live path-drift check, not a read-and-
discard.

**`find_orphan_configs` gained a second documentation-only module class.** Previously only
`module='governance'` settings were exempt from the "must co-occur with a literal `.setting(`
call" rule (they're process rules for the AI, not runtime-applied values). `_NARRATIVE_MODULES`
generalises this to any module whose settings are pure infrastructure documentation with no
apply-the-value behaviour to grep for — seeded with `'backup'` (all 6 live rows checked
individually against their content before adding the module, not assumed).

**Two new governance-layer mechanisms exist as of today, both still mid-build:**
`governance.operational_behaviour_control` (`cfg_behaviour_class`/`cfg_behaviour_rule` — chat/
terminal/sqlite/documentation/llm_output operational-behaviour rules, project-wide scope, escalation
`#715`, cycle 3 as of §41 below — `chat` no longer empty) and `governance.prose_canonical_authority`
(`cfg_prose_chapter`/`cfg_prose_concept` — the programme prose as the project's canonical
definition source, pointed at rather than restated, escalation `#714`, chapters 4-6 still
unaligned). Neither is finished; both are named here because they're new *governing* mechanisms,
not because the work is done.

## §41. `#715` cycle 3 — `chat` populated, three new `governance.*` settings (2026-08-18)

Content-only cycle (no mechanism/code change to `configmaint`/`cfgquality` themselves), so full
detail lives in `BUILD.md` §149 per this file's own scope discipline (§40's precedent — mechanism
changes here, build content there). Recorded here because three new rows are new *governing*
settings: `governance.behaviour_boundary.git_commit` and `.backup_recovery` (git/commit and
backup/durability discipline classified under the existing `terminal`/`sqlite` classes rather than
new ones — the researcher's own fallback: "if in doubt, define it and let it live in
settings.governance"), and `governance.procedural_document_taxonomy` (the researcher's 4-way future-
document taxonomy — planning · config-extract · history-of-changes · guidance/baseline — recorded
verbatim, not yet applied to the existing document set). `cfg_behaviour_rule` `chat` class populated
from empty (9 rules); `governance.operational_behaviour_control`'s "chat still empty" caveat in §40
above no longer applies. Two orphaned 2026-06-14 consolidation documents retired in the same pass —
see `BUILD.md` §149 for which, and for the new `documentation.consolidation-doc-must-be-load-
bearing-or-retired` rule they're the concrete instance of.

## §42. `#715` cycle 4 — a 6th behaviour class (`development`), `Behaviour.ps1` built (2026-08-18)

Full detail `BUILD.md` §150, same scope split as §41. Recorded here for one new *governing*
setting: `governance.engineering_documentation_folder` designates `iba/docs/` as the IBA-side home
for planning/design documentation — main-project-side consolidation of the equivalent scattered
content stays explicitly out of scope, parked alongside escalation `#650`. `cfg_behaviour_class`
now has 6 members, not 5 — `chat`/`terminal`/`sqlite`/`documentation`/`llm_output`/`development` —
42 active rules total. The operational-behaviour system's own completeness gap (no supporting PS
script across 3 build cycles) was found and closed in the same pass that added the rule naming it:
`iba/app/lib/behaviour.py` + `iba/app/ps/Behaviour.ps1 -Action List`.

## §43. Escalation design plan v5 / decision register v9 built (2026-08-21)

Full detail `BUILD.md` §162 (D-numbers below refer to
`iba/docs/escalation-design-decision-register-v9-20260821.md`). Ten governing changes this round:

1. **Current-state/history split, true-delta model** — unchanged from the 2026-08-20 rebuild
   (§39); reconfirmed, not reopened.
2. **State-derivation engine** (`cfg_escalation_transition`) — `ready_for_approval` now has its own
   explicit priority-5 row (D27) rather than depending on the incidental `assignee_changed`
   condition; the two generic fallback rules shifted to priority 6/7.
3. **Field-requirement engine** (`cfg_escalation_requirement`) — gained a `check_kind` column
   (`field_required` — the prior, only, implicit behaviour, now named — plus
   `not_raised_with_content`/`exists`/`not_self`, D14/D25/D26).
4. **Two-stage approval is AUTHORITY-based, not same-party** (D25) — `approved` is refused only if
   the caller differs from whoever `ready_for_approval` assigned the item to; same-party is fine
   when that party holds the authority. Corrects a shipped defect: the prior same-party refusal
   blocked legitimate self-authorisation.
5. **Five-type model, per-type behaviour** — `notice` now closes on arrival at Raise (D12:
   `state='closed'`, `next_action=NULL`, no review cycle); every other type still defaults
   `raised`/`review`. `issue` continues to reuse the manual vocabulary in full (D11/D21,
   reconfirmed, no separate scheme).
6. **`from_id`/`related_activity`** (D14) — new `escalation.from_id` column: which item this one
   was spawned from. Enforced (when set): references a real row, isn't self-referential, and is
   paired with `related_activity`. **Mutable, settable on Raise or Update alike** (corrected
   2026-08-21, escalation #763 — built immutable-after-Raise the first time, contradicting the
   researcher's own recorded instruction, `#6` v5: "not immutable-after-raise ... can be
   re-pointed/corrected later"; root cause traced to register v7's fuller wording being thinned
   during the v9 consolidation pass, then the code built from the thinner text without checking
   back).
7. **`chat_routing`** — extended with the verbatim-quote convention (D19): content captured under
   this rule quotes the operative instruction/correction VERBATIM, Claude's own framing kept
   distinguishable from the quoted part.
8. **This register's own "configs touched" discipline** — each decision in the register states
   exactly which `cfg_*` rows it touches, so a build pass can be checked against the register
   directly rather than re-deriving scope from prose.
9. **Produced-documentation-task pattern** (D18) and the **raised-state guard** (D26, next item) —
   both now `cfg_escalation` rule rows, not prose-only conventions.
10. **`update()` refuses content on a still-`raised` item** (D26) — `comment`/`context`/`tried`
    requires the state to actually move first (e.g. `-State in-progress`); mechanically enforced,
    not just a session-practice convention (the "researcher says 'start work'" half stays
    session-practice, honestly distinguished from the enforced half).

Also this round, not separately numbered above: `escalation.list`/`escalation.history` now dispatch
through `run.py` like every other report (`cfg_work_package`/`cfg_step`/`cfg_report`/
`cfg_report_section`/`cfg_report_csv_table`, D4/D16/D23) instead of `Escalation.ps1` calling the
module directly; the report gained five D15 exception sections (cycle/dangling/mismatched-pairing/
missing-link/incoherent-link) computed over the `from_id`/`related_activity` graph; a new
`configmaint.validate` advisory check (D28) flags drift between `Escalation.ps1`'s `ValidateSet`
literals and the live `cfg_enum` groups they're meant to mirror; `cfg_utility` gained
`crash_escalation_reviewed`/`crash_escalation_note` columns, and all 39 active modules were reviewed
under them (D3) — three genuine, unfixed crash-recovery gaps flagged (`bootstrap_behaviour_rules*`,
`engine_migrate`, `cfgload` — each mixes DDL with a single end-of-script commit and has no
try/except, so a mid-script crash can leave inconsistent partial state with no escalation record;
not fixed this round, out of D3's scope). D1 (rebuilding `escalation` from the 2026-08-20 export +
this session's live rows) has a dry run built and run
(`iba/app/reports/escalation-rebuild-dry-run-20260821.md`) but deliberately NOT executed — the
register's own two-phase gate ("execute — only after the dry run is reviewed and corrected") is a
human-review checkpoint, not a step to auto-chain through.

## §44. Every active PS script dispatches through `run.py` — new `cfg_behaviour_rule`, escalation #8 (2026-08-21)

Researcher, on `#8` (the 2026-08-20 finding that 8 of 45 PS scripts under `iba/app/ps/` bypass
`run.py`): "confirm that there are a governance rule that every active PS script must use run.py to
ensure that it is recorded in the engine. If it exists, then this item can be closed down with that
as the action, if not then create the config and then close both down."

Checked live against `cfg_behaviour_rule` and this document directly, not assumed: no such rule
existed. Rule 41 (`every-interactive-module-needs-ps-script`, §42) is the adjacent-but-different
rule — a hand-operated module MUST have a PS script, not a PS script MUST dispatch through
`run.py`. Created `cfg_behaviour_rule` id 43, class `development`, key
`every-active-ps-script-dispatches-through-run-py`
(`iba/app/migration/add_ps_scripts_dispatch_through_run_py_rule_20260821.py`).

Written to be honest against live reality, not a blanket claim of compliance: the rule names two
permanent, legitimate exceptions — (1) `Start-Iba.ps1`, necessarily, since it bootstraps what
`run.py` itself depends on; (2) `Escalation.ps1`'s `-Action Raise/Update/AnswerRun`, a deliberate
manual front door onto the escalation backlog, not a pipeline run (`-Action List/History` already
dispatch through `run.py`, §43). The other 6 scripts `#8` found still bypassing `run.py`
(`Behaviour.ps1`, `Debate-Run.ps1`'s ungoverned post-run side-call, and 5 lowercase one-off
scripts) are real, current non-compliance — NOT retroactively fixed by the rule's existence, and
NOT silently dropped when `#8` closes: split off as its own escalation, `#767`, for a scoping
decision. `enforced_by`: no `configmaint.validate` scan exists yet for this rule; honestly
recorded as unmechanised, matching this project's own convention elsewhere (e.g. rule 41).

## §45. `retention.snapshot_keep_count` lowered 20 → 5 — escalation #771 (2026-08-21)

Researcher, on `#771` (spawned from `#758`'s disk-space investigation — `run.py`'s `_ensure_run()`
snapshots the full `iba.db` before every new run, unconditionally, including pure read-only
reports): *"Set the retention of snapshots to a maximum of 5 ensure that it is maintained as
such."* A stopgap, not the root fix — the per-step write-classification design that would let
read-only steps skip the snapshot entirely is still open, tracked in `#771` itself.

Applied via `configmaint.propose` (the sanctioned path — `cfg_setting` update, `Where
{"key":"retention.snapshot_keep_count"}` / `Set {"value":"5"}`), approved same turn per the
researcher's own direct instruction. "Maintained as such" taken literally, not just the config
value: the existing snapshot directory (`iba/app/db/snapshots/`, 14 files/67.8GB — a mix of
pre-`content_index`-clear 8.06GB snapshots and post-clear 0.66GB ones) was NOT going to self-prune
until the next incidental `snapshot()` call happened to fire `prune()` internally — called
`dbsnapshot.prune()` directly to enforce the new count immediately: 14 → 5 files, 67.8GB → 3.3GB.

**Files:** none beyond `cfg_setting` (`retention.snapshot_keep_count`) and the snapshot directory's
own contents.

## §46. `from_id` `-1` sentinel + the `Correction` transaction — escalations #773/#774 (2026-08-21)

Researcher's decisions on the two items `#767`'s full `related_activity`/`from_id` audit spawned
(`BUILD.md` §168):

- `#773`: *"Use a sentinal of -1."*
- `#774`: *"create a copy of update transaction as Correction and allow the Correction transaction
  to update any column in any state. ensure that this is update in the documentation and that
  correction is stated as only to be used for error correction."*

`_NO_PARENT_SENTINEL = -1` (`lib/escalation.py`) — non-falsy in Python, unlike `0`, so genuinely
distinguishable from `NULL` wherever `from_id` is read. Wired into the write-time `exists` check
(shared by `raise_new()`/`update()`/`correction()`) and `_find_dangling` (the D15 report check) —
both explicitly treat `-1` as valid, not a broken reference. `cfg_column.use` corrected on both
`escalation`/`escalation_history`'s `from_id` to document it (`configmaint.propose`).

**`correction()`** — new function, `lib/escalation.py`, exposed as `-Action Correction`
(`Escalation.ps1`) and `python -m iba.app.lib.escalation correction`. Differs from `update()` in
exactly the two ways asked for: works on ANY item state (including closed/completed, which
`update()` structurally refuses — `#774`'s own finding), and exposes `short_description` as a real
parameter (`update()` has none — `#10`'s finding). Does NOT auto-derive state/next_action via
`cfg_escalation_transition` (not a workflow action), does NOT apply the D25 authority check or the
D26 raised-state guard (both workflow-transition safeguards, irrelevant to a data-repair
transaction). A runtime warning prints on every invocation: *"Correction is for ERROR CORRECTION
ONLY... Use -Action Update for ordinary changes."* `USER-GUIDE.md` §4.6/§4.7 updated in the same
unit of work, per the researcher's explicit instruction to document it.

Live-tested against real data: `#1` correctly refused (dispatcher-tied — revealed that
dispatcher-tied items structurally cannot carry `from_id` through any front door at all, not a
bug; `#1`/`#7` left genuinely exempt, not "no parent found"). The 17 genuinely-manual no-parent
rows from `#767`'s audit corrected via `-Action Correction -FromId -1`, several already
closed/completed — the open-state bypass proven live, not just in principle.

**Files:** `iba/app/lib/escalation.py`, `iba/app/ps/Escalation.ps1`, `iba/app/USER-GUIDE.md`.

## §47. `#768` closure check — 3 completeness gaps found and fixed (2026-08-21)

Researcher, on `#768`: *"is the actual configs and code, and guides now updated with the completion
of related_activity and from_id. Are there any confusion on using it still."* Checked live, found
real gaps: `Escalation.ps1`'s own top-of-file help block never mentioned `-Action Correction`;
`cfg_escalation_requirement`'s `from_id` `exists`-check messages (raise + update) didn't document
the `-1` sentinel exception; `cfg_utility.escalation.purpose` still said "raise/update", missing the
third verb. All three fixed (`BUILD.md` §171 has the detail; the two config text changes via
`configmaint.propose`). `#768`'s own original subject — the mismatched-pairing check only catching
one direction — remains genuinely open, not resolved by this pass, still awaiting the researcher's
choice of fix-shape.

**Files:** `iba/app/ps/Escalation.ps1`.

## §48. `resolution_kind` — decision-required vs self-correctable, the axis missing from escalation itself (2026-08-22, escalations #798/#799)

The researcher's own diagnosis of why `#753` (the escalation module rebuild) was never signed off:
*"I read through the escalation routing. We are mixing two things and working with two different
methods which is causing all the confusion. You like to build, find a problem, go through a
process of clarification, then proceed where you left off. My aim is to design, specify, and
resolve all the open issues through debate and validate, and then build and test thereafter... a
build validation or other stoppage for clarification should be TERMINAL. This is always a sign of
poor upfront design."* A follow-up correction sharpened the OTHER half: *"the self-correctable must
be able to escalate to a decision_required (that was the original idea behind the `tried`
column)... there should be very few cases where decision_required is a constant output from every
run. This means the design is inadequate."* Both halves are now `cfg_behaviour_rule`
`decision-points-are-terminal-not-inline` (class `development`, quoted in full — see the rule row
itself; enforced_by names `escalation.resolution_kind`), the first project-wide working-method rule
recorded there rather than only in a session log.

**The mechanism**, built via `iba/docs/escalation-decision-vs-defect-axis-proposal-v5-20260822.md`
(4 review rounds, approved v5) and tracked through 4 build stages on `#799`:

- New `cfg_enum` group `resolution_kind`: `decision_required` | `self_correctable`.
- New `escalation.resolution_kind` / `escalation_history.resolution_kind` columns (migration
  `add_resolution_kind_column_v1_20260822.py`).
- New `cfg_escalation_requirement` row: `raise` + `resolution_kind` is `field_required` — no
  default, mirroring `-AnsweredBy`'s own no-silent-default rule (§ various). `raise_new()` also
  forces `type='issue'` whenever `resolution_kind='decision_required'` is passed — a
  decision-required item is definitionally an issue — but only AT RAISE, never on conversion
  (`type` stays immutable after Raise everywhere else, same as `run_id`/`source`/`at_step`/
  `raised_at`).
- Two new transactions in `lib/escalation.py`: `resolve_self_correctable()` (closes a
  self-correctable item directly — no approval step, because the design was already approved and
  only the execution slipped) and `escalate_to_decision()` (converts a self-correctable item to
  decision_required mid-fix, when the attempted correction reveals a genuine judgement call the
  design didn't anticipate — this is `tried`'s original purpose, now load-bearing). Both exposed on
  `Escalation.ps1` as `-Action ResolveSelfCorrectable` / `-Action EscalateToDecision`.
- **Two DIFFERENT run.py-adjacent decisions, easy to conflate, kept distinct on purpose:**
  `run.py`'s own crash and fail()-shaped report-stop sites (uncaught exception, hard error with no
  handler-supplied `escalate()`) are `self_correctable` by DEFAULT — proposal v4 §4, the
  researcher's own later, more specific correction: *"these are code-bug territory by nature, not
  open design questions"* — Claude fixes it directly and `escalate_to_decision()` converts the
  SAME item to `decision_required` (never closed-and-reopened) only if the fix attempt itself
  reveals a genuine new judgement call. Separately, `reports.py`'s `.validate()`-step escalations
  (`_validation_outcome()`) are always `decision_required` — a DIFFERENT, later instruction, §6.1
  of the v1 proposal, about a different code path: *"§6.1 build these now as decision_required. I
  will very quickly complain if there are missing configs when these modules are run."*
  `configmaint.propose`'s pause is likewise always `decision_required` (a config change is
  definitionally a design decision). `run.py`'s dispatch was fixed so ANY `decision_required`
  pause — whichever site raised it — always routes to a terminal `report-stop` (never resumes
  inline as `pause-continue`) — found live during build: the `path` reassignment originally
  happened too late (inside the branch, after `PATH_EXIT` had already been read at the point of
  use), so exit code stayed 2 (paused) even though `run.state` was
  correctly `'failed'`; fixed by moving the reassignment before the dispatch `if/elif`.

**The other half — closing the "constant decision_required" gap** — required real config, not more
escalation machinery, in the three modules the researcher named directly:

- `narrative.generate()` — no config existed to approve/reject an over-budget API cost; correction:
  *"narrative API spend should be a config limit that is approved, if spend above then it is a
  failure that requires a review of either to call, or the limit."* Fixed by removing the
  pause-continue/escalate() entirely — `narrative.generate_max_cost` (already a `cfg_setting`, §30)
  is now the sole gate: over cap is a hard refusal (`cost-cap-exceeded`), never a question asked at
  run time.
  - `raw.discover()`'s zero-strongs branch previously escalated every time; correction: *"When this
  happen it will give me a chance to rethink the system because it should not happen"* → new
  `raw.zero_strongs_action` setting (`cfg_setting`, module `raw`), default `"reject"` — a hard
  refusal by config, not a question.
- `passage.validate()` had no threshold at all — any passage distribution asked the researcher a
  question. Correction: *"single verse passages per book should not be > 20% of the total verses in
  the book. average verses per passage should not be > 30 ... these configs should not be in
  cfg_settings, it should be in cfg_passage and it does not exist, create it."* Built as the
  project's second per-module settings table (`governance.module.config`, precedent `cfg_passage`
  already existed from an earlier build) — `passage.max_single_verse_pct` / `_max_avg_verses_per_passage`
  as new `cfg_passage` rows, read via new `Cfg.module_setting(table, key, default)`. `validate()`
  now returns `ok()` directly when a book is within both thresholds and only escalates
  (`decision_required`) naming the specific breaching books when one is actually exceeded — the
  common case no longer asks anything.

**A vocabulary bug found live during Stage 3 testing** (escalation #809, a real false positive):
`configmaint.py`/`cluster.py`/`lexicon.py`/`reports.py` all checked `if decision == "approve":`, but
a `decision_required` item resolved via the MANUAL vocabulary (`Update -NextAction approved`) stores
the PAST TENSE `"approved"`, not `"approve"` — `"approve"` is only ever a dispatcher-shape
`-Decision` literal. Fixed across all 4 handler sites with `decision in ("approve", "approved")`.

**Files:** `iba/app/migration/bootstrap_decision_vs_defect_axis_v1_20260822.py`,
`add_resolution_kind_column_v1_20260822.py`; `iba/app/lib/escalation.py`, `cfg.py`,
`debaterun.py`; `iba/app/handlers/base.py`, `run.py`, `narrative.py`, `raw.py`, `passage.py`,
`configmaint.py`, `cluster.py`, `lexicon.py`, `reports.py`; `iba/app/ps/Escalation.ps1`,
`Chapter-Generate.ps1`, `Debate-Run.ps1`. Full design: the 5 proposal versions in `iba/docs/`; build
tracking: `#799`.

## §49. `AnswerRun` fixed + `decision_required` now closed off from it entirely — escalation #795 (2026-08-22)

Three real defects in the dispatcher-tied `AnswerRun` path, none touched by §48's build (that build
gave `decision_required` items an *alternate* route via `Update`; it never closed the old route off).

**Items 1-2** — researcher, verbatim: *"Calling AnswerRun with approve, reject, or revise all land
on the same completed state is still not solved then solve it. it is a bug. that is not the correct
behaviour... the runid should be allowed to use the number."* `cfg_escalation_transition`
(`shape='dispatcher'`) had one catch-all rule sending approve/reject/revise all to `completed` —
split into 3 rules matching the manual shape's own outcomes (`approve`→`completed`,
`reject`→`withdraw`, `revise`→`in-progress`); `cfg_status_flow` retargeted to name each specific
`decision=` key. `pending_for_run()` now also accepts the bare escalation id, not only the full
generated `run_id` string.

**Item 3** — the A/B routing question §48 itself never answered. Researcher, verbatim: *"I suggest
to check and test the answer to the question in the configs, my expectation is that it should not
be possible and that the configs should now state that."* Checked live BEFORE fixing, per that
instruction: raised a real `decision_required` item (escalation #820) and confirmed `AnswerRun`
would silently flat-approve it — no refusal existed. Fixed: `answer_for_run()` now refuses any item
with `resolution_kind='decision_required'` at the top of the function, before evaluating any
decision — the exact mirror of `update()`'s own existing carve-out (`update()` refuses a
dispatcher-tied item UNLESS `decision_required`; `answer_for_run()` now refuses one IF
`decision_required`). Together the two guards mean a `decision_required` item is answerable **only**
through `Update`'s richer vocabulary — `AnswerRun` is `self_correctable`-only from now on. The rule
itself is recorded in `cfg_behaviour_rule` (class=`development`,
`rule_key='decision-required-answered-via-update-not-answerrun'`), not just in code, per the
researcher's explicit instruction.

**Tested live throughout, not unit tests alone**: 6 real throwaway escalations (`#815`-`#822`) —
approve/reject/revise transition outcomes, short-id `AnswerRun`, the pre-fix `decision_required`
gap confirmed on `#820`, the post-fix refusal confirmed on `#821` (then successfully closed via
`Update`'s full `ready_for_approval`→`approved` flow instead), and `#822` confirming
`self_correctable` items are unaffected. `configmaint.validate` re-run clean after each change.

**Still open, not part of this fix**: none — items 1-3 were the entirety of what `#795` and its
attached routing proposal (`iba/docs/escalation-type-routing-proposal-v1-20260822.md`) asked for;
the proposal's option A (stop `.validate`-style steps pausing at all) is now moot, since option B
(unblock only via the richer flow) is what got built.

**A second gap found checking this, not from the researcher's instruction but from re-reading
#799's own approved spec while fixing item 3**: the ORIGINAL approved proposal
(`escalation-decision-vs-defect-axis-proposal-v4-20260822.md` §6 + §11 Stage 2's own named test)
already required `self_correctable` items to have "no reachable AnswerRun path (attempting it
should refuse, citing resolution_kind)" — the opposite direction from item 3's `decision_required`
guard. **This was never built in #799 either**, and #799's own Stage 2 test record (`BUILD.md`
§172) never mentions testing it — confirmed live (escalation #822): a flat `approve` via AnswerRun
succeeded on a self_correctable item with no refusal. Fixed in the same pass: `answer_for_run()`
now refuses BOTH `resolution_kind` values. **Net effect, stated plainly**: `AnswerRun`'s flat
vocabulary is now unreachable for any item raised since #799 (resolution_kind required at every
Raise) — this is what the approved design actually specified throughout, not a new decision made
here. Zero live disruption: checked first, no pending dispatcher-tied escalation existed at the
time of the fix. This is the second of two real "approved-but-not-built" gaps found in one review
pass of #799's own spec — see the researcher's follow-up question about build trustworthiness,
answered directly in escalation #795's own record.

**Files:** `iba/app/migration/fix_dispatcher_answerrun_795_20260822.py` (new);
`iba/app/lib/escalation.py` (`pending_for_run()`, `answer_for_run()`). Build record: `iba/app/
BUILD.md` §173.

## §50. New governance rule — a test plan per module/utility, run after build, results in the resolution (2026-08-22)

Direct consequence of §49: the approved design for #798/#799 contained a specific, named test
(§6/§11 Stage 2 of `escalation-decision-vs-defect-axis-proposal-v4-20260822.md`) that was never
actually run before the build was reported complete — found twice, once per half of the same
function. Researcher, verbatim: *"I think we got to the stage where we need to have a re-usable
test pack for all development tasks... each module or utility in future must have a test plan. the
test plan must include testing all the different interations, params options of each of the
module/utility intended functionality. this test plan must be updated to include modifying the
testing plan for each functional component after a change. the test plan must then run through
after the design, and the results of the test must be included in the resolution of the build...
however, the test plan method will be introduced case by case as further development takes place,
rather than trying to develop test plans for all modules."*

**The rule, anchored in two places** (`iba/app/migration/
anchor_test_plan_governance_rule_20260822.py`):

- `cfg_behaviour_rule` (class=`development`, `rule_key='test-plan-per-module-utility'`) — full text
  and rationale, same shape as `decision-points-are-terminal-not-inline`.
- `cfg_setting` (`module=governance`, `key='governance.module_utility_test_plan'`) — the compact
  form, because this is the row `init.py` actually prints at every `Start-Iba.ps1` run — the
  mechanism that makes a process rule genuinely "anchored" rather than an unread database row (per
  `init.py`'s own comment on why `governance.*` settings exist).

**What the rule requires, going forward, case-by-case (NOT retrofitted to existing modules):**

1. Every module/utility design, from now on, includes a test plan covering its meaningfully
   different interaction/parameter/option combinations — not one happy-path example.
2. The test plan is a living artifact: a change to the functional component updates its test plan
   in the same unit of work, before the change is considered complete (same discipline as
   `governance.build_md_on_code_change`).
3. The test plan RUNS after the approved design is built — a required stage inside the existing
   plan/propose/design (in detail) → approve → build per the plan → approve cycle, not optional and
   not skippable.
4. The test's actual results go INTO the build's escalation resolution — not a prose claim of
   "tested live" without the per-case results shown.

**Deliberately not built now**: no `cfg_test_plan` table, no template, no retrofit of any existing
module's tests — rollout is case-by-case, starting the next time a module/utility is designed or
changed, per the researcher's explicit instruction not to speculatively engineer this ahead of a
real case.

**Files:** `iba/app/migration/anchor_test_plan_governance_rule_20260822.py` (new).

## §51. Flag Management — `wa_quality_flag_types`/`wa_data_quality_flags` repurposed for prose quality; `cfg_column.inactive` added; `wa_session_research_flags` retained (2026-08-23, escalation #833)

**What this closes.** Escalation #833 ("Flag Management," spawned from #784/#829's storage-layer
audit) found the project's flag-related tables badly fragmented across four generations built over
five months, each because the previous shape wasn't working (full history:
`iba/docs/flag-management-current-status-v1-20260823.md` §2.1). This section records the
researcher's decisions on the first slice of that fragmentation, dictated directly and captured
verbatim before being built (`iba/docs/flag-management-prose-quality-repurpose-capture-v1-20260823.md`,
`iba/docs/flag-management-proposal-v1-20260823.md`).

**1. `wa_quality_flag_types`/`wa_data_quality_flags` — repurposed, not merely cleaned up.** All
prior content (29 term-quality flag types, 19,866 instances) was **hard-deleted** — a deliberate,
one-time, researcher-authorised purge of data confirmed invalid (the term-quality vocabulary
predates IBA's reworked Strong's handling), not a change to the project's standing
no-physical-delete-in-automated-flows convention. Both tables were rebuilt (`DROP`/`CREATE`, since
no data survived to preserve) as the **prose-quality-check** mechanism:

- `wa_quality_flag_types.deprecated` → `delete_flagged` (project-standard soft-delete naming).
- `wa_data_quality_flags` gains `delete_flagged` (had none); `term_id` → `strong_id`, `file_id` →
  `verse_id` (both optional, documented-only references — SQLite cannot enforce a foreign key
  across `bible_research.db`/`iba.db`, the same limitation every other cross-database reference in
  this project already has); two new columns, `corrective_action` and `correction_date`.
- A cascade trigger (`wa_quality_flag_types_cascade_delete`) enforces, automatically: soft-deleting
  a flag type soft-deletes every `wa_data_quality_flags` row using it. Tested live (throwaway
  rows): confirmed the cascade fires correctly and does not touch unrelated rows.
- Seeded with 3 real types (`flag_group='PROSE_QUALITY'`): `Terminology change`, `Methodology
  change`, `Style change` — explicitly open-ended, more will be added as they come up in practice.

**2. `cfg_column.inactive` — new column, project-wide.** `cfg_column` had no `inactive` field at
all (only `cfg_table` did, since escalation #678). Added, mirroring `cfg_table.inactive`'s own
bootstrap exactly (`add_cfg_table_inactive_column.py`) — not DB-enforced (nothing stops a write to
a column marked inactive), but makes "this column is config-known dead" a real, queryable fact for
the first time, general to the whole project. Researcher, verbatim: *"this may not be DB
enforceable, but at least it sets the config that the column is not used."* First real use: `passage
.review_flag` (`bible_research.db`; barely populated, TEXT-typed holding only `'0'`) and
`session_d_observations.researcher_flag` (the whole table is empty — the abandoned Session D
workstream) both marked `inactive=1`.

**3. `phase2_flag_types` → `inactive=1`**, matching its two junction tables (`mti_term_flags`,
`wa_term_phase2_flags`), which were already inactive — a different-purpose vocabulary (content
classification, not a "needs attention" signal) not touched by item 1's repurpose.

**4. `wa_session_research_flags` (715 rows) — kept exactly as-is, deliberately.** Researcher:
*"wa_session_research_flags are analysis phase, and at this point stay as is, and should be alive
and incorporated in IBA."* No schema change. "Incorporated" is scoped narrowly here — a
`cfg_behaviour_rule` (`sqlite`, `wa-session-research-flags-retained-as-is`) now records that this is
the live, deliberate analysis-phase flag mechanism; **no `cfg_write_grant` was added**, since
nothing in governed code currently writes to it (checked directly) — one gets built when analytics
work actually resumes and a real writer exists, not invented ahead of need. Its own known
data-quality issues (`priority`/`session_target` vocabulary drift, `cluster_link` as a
comma-separated string rather than a junction) are explicitly deferred, per the researcher: *"the
value of the data can only be assessed when analytics kicks back in."*

**5. `wa_flag_type_question_link` (12 rows) — untouched, "for now."** Its rows FK to the *old*
`wa_quality_flag_types` ids that item 1 just deleted — a known, accepted orphan, not fixed here, per
direct instruction.

**Explicitly deferred, registered not dropped** (full list:
`iba/docs/flag-management-proposal-v1-20260823.md` §4): the flags-vs-escalation weight-class
question; `verse_context.flagged_for_review` vs. `triage_status='ESCALATE'` (an apparent duplicate);
which generation's shape (on-record vs. separate-table) should be the general pattern going
forward. All wait on the analytics-phase restart.

**Files:** `iba/app/migration/flag_management_build_v1_20260823.py` (idempotent — re-running it is
always safe). Pre-op backup: `backups/bible_research_pre_flagmgmt_<timestamp>.db`. Full design
record: `iba/docs/flag-management-current-status-v1-20260823.md` (explore),
`iba/docs/flag-management-prose-quality-repurpose-capture-v1-20260823.md` (dictated decisions),
`iba/docs/flag-management-proposal-v1-20260823.md` (proposal + test plan + results). Test plan: all
12 cases passed, including a clean `configmaint.validate` run after the build.

## §52. `prose_section`/`prose_section_type` rebuilt onto Model A (system-versioned temporal tables); `record_change_log` — a project-wide change-audit log, not prose-specific (2026-08-24, escalation #836)

**What this closes.** `prose_section` had only `created_at` (silently stale — the one sanctioned
in-place write, `session_a_replace`, never touched it), and `prose_section_type` had **no**
version/last-modified concept at all despite being edited in place. Nine rounds of design
(`iba/docs/prose-change-log-design-v1` through `-v9-20260824.md`) and three of consolidated proposal
(`iba/docs/prose-change-log-proposal-v1` through `-v3-20260824.md`) settled the shape; this section
records the approved, built result.

**1. The model — mutate-in-place, current-state-only tables.** Both tables now hold **current
content only**; no historical row is retained live. This is the SQL-standard *system-versioned
temporal table* pattern (`iba/docs/prose-change-log-design-v5-20260824.md` §16.1 — researched
directly, not invented for this project), not the old insert-a-new-row-per-supersede mechanism.

**2. `record_change_log` (new, `bible_research.db`) — the paired history table, deliberately
generic.** One row per change event, keyed by `target_table`/`target_id` so it isn't prose-specific
(researcher, direct instruction: *"this is opening a big door, and I think we should consider
it"*) — this build wires up write paths for `prose_section`/`prose_section_type` only; `finding` is
the named future candidate (`bible_research.db` already has an unrelated, unused `finding_revision`
table — a genuinely different field-level-delta shape, found live and left for whoever picks up
findings-integration to reconcile, not solved here). Columns: `target_table`/`target_id`,
`change_type` (`insert`/`change`/`delete`), `change_datetime` (system-applied time, not the
underlying event's real-world date), `change_source` (file name or originating script/module),
`change_reason` (population rule: flag type for a flag-driven change, otherwise the source
reference), `changed_by` (who/what executed the change — a third concept, distinct from
`prose_section.author`'s authorial voice and `.approved_by`'s accountable sign-off), `status`
(`change_proposed`/`change_applied`/`declined` — the `change_proposed` state is the intended home for
#835's not-yet-built flag-fix workflow), and `payload` (gzip-compressed JSON — **the prior content a
change overwrote, never the resulting content**; NULL for inserts and migration-baseline rows). A
target row's own `version` column **is** the corresponding `record_change_log.id` — a literal
pointer, not an incrementing per-item counter (researcher, direct: *"individual row version
sequencing is meaningless... the log id is as good as anything"*) — this **corrects** the
`version = old.version + 1` text #829 §5 drafted before this item existed; that text is superseded
by `cfg_behaviour_rule` `record-change-log-version-is-pointer`, not left standing alongside it.

**3. Schema deltas.** `prose_section`: `supersedes_id`/`superseded_by_id`/`source_file` dropped
(nothing to chain once only one row per section exists; `source_file`'s value lives inside migrated
`payload` blobs, not as a live column); `updated_at` added (touched on every write, closing the
staleness gap). `prose_section_type`: `version` and `updated_at` added (had neither before).

**4. Migration — real facts found live, not assumed from the design.** 91 rows were superseded
(9% of 1,040) at build time; each was logged (its own content as `payload`, `change_reason=
'migration'`) then **hard-deleted** — a one-time, researcher-instructed exception to the standing
no-physical-delete convention, matching #833's own precedent (now generalised as
`cfg_behaviour_rule` `one-time-hard-delete-exception`). **4 of the 91 sat in 2-hop supersede chains**
(e.g. id 45 → 52 → 54) — found only by walking the live data, not visible in the design docs; each
such row's log entry targets the chain's *final* live row, not its immediate successor (which, in
these 4 cases, was itself also being deleted). The 949 surviving `prose_section` rows and all 108
`prose_section_type` rows each received one baseline `record_change_log` row
(`change_reason='migration baseline'`, `payload=NULL` — nothing preceded them) so every row's new
`version` pointer is valid from the moment the migration completes; **0 dangling pointers**, verified
directly. A second real finding, only surfaced by testing the migration against a full copy before
running it live: **3 partial indexes** (`idx_ps_supersedes`, and two others whose `WHERE` clause
itself referenced `superseded_by_id`) blocked the column drops outright — SQLite refuses to drop a
column an index references. Dropped and recreated against `delete_flagged = 0` only, the sole
meaning "current row" retains under Model A. Side effect, not a separate fix: `prose_section_fts`'s
row count fell from 1,040 to 949 automatically (its sync trigger fired on the `DELETE`) — the
superseded rows' stale text is no longer searchable, fixing a live defect found during design (every
row, including retired ones, was previously indexed).

**5. `apply_session_patch.py` rewritten, not just wrapped.** All 6 `prose_section` operations
(`insert`, `supersede`, `delete`, `approve`, `session_a_replace`, `bulk_supersede`) and both
`prose_section_type` operations (`insert`, `update`) now go through one shared helper,
`_write_change_log()` — the choke-point `cfg_behaviour_rule` requires every one of them to, closing
the exact selective-coverage gap that motivated this item (`session_a_replace` and `prose_section_
type.update` previously bypassed all tracking entirely). `supersede` and `bulk_supersede` are genuine
rewrites (in-place `UPDATE`, not insert-a-new-row) rather than additions. `session_a_replace`'s own
long-standing defect — it wrote `created_at = now()` on every replace, silently corrupting the "true
creation time" meaning — is fixed in the same change: it now touches `updated_at` instead,
`created_at` is never written again after a row's first insert. All 8 operations were tested directly
(a synthetic patch run against a full copy of the live, post-migration schema) before the real
migration ran.

**6. One advisory finding from `configmaint.validate`, not treated as a defect.** The two new
`cfg_enum` groups (`record_change_log_change_type`, `record_change_log_status`) are flagged as
"orphan" — no runtime `cfg.enum(...)` call site reads them, because `change_type`/`status` are
enforced by the table's own `CHECK` constraint directly. This is the same shape already accepted at
#833's `wa-session-research-flags-retained-as-is` rule (`cfg_enum` as documentation-of-record
alongside DB-level enforcement, not a code-driven lookup) — recorded here rather than silently
suppressed, per the standing practice of surfacing every finding.

**Files:** `iba/app/migration/prose_change_log_build_v1_20260824.py` (idempotent — re-running it
after the schema already exists is a safe no-op). Pre-op backup:
`backups/bible_research_pre_changelog_<timestamp>.db`. Full design record: `iba/docs/prose-change-
log-design-v1` through `-v9-20260824.md`; proposal + literal config content + test plan:
`iba/docs/prose-change-log-proposal-v1` through `-v3-20260824.md`.

---

## §53. Prose module — dispatcher registration, write-layer governance, `cfg_prose`, `prose.flag` (2026-08-24, escalation #829)

**What this closes.** `prose_section`/`prose_section_type` were fully catalogued in `cfg_table`/
`cfg_column` (and, after §52, under `record_change_log` versioning discipline) but had zero
`cfg_work_package`/`cfg_step`/`cfg_prose`/`cfg_enum`/`cfg_status_flow`/`cfg_write_grant` governing
the module itself — the schema described the tables, nothing in config operated the app around
them. Eight rounds of proposal (`iba/docs/prose-management-iba-first-layer-proposal-v1` through
`-v8-20260824.md`) converged on a design; the researcher then asked for one consolidated,
self-contained document rather than a chain of deltas — `-v9-20260824.md` is that consolidation
(found live, not carried from memory: a "drop 3 stale `cfg_column` rows" item v7/v8 both listed as
outstanding was already done via `inactive=1`, and a new tension between `prose.book_stage_map`
and `book_label` on 1/949 rows, D10). Researcher approved v9 as written, D10 explicitly deferred
("D10 will be edited in prose edit stage, not in this IBA processing build").

**1. `cfg_prose` — new per-module table, 4 keys** (`governance.module.config`, matching
`cfg_passage`'s precedent): `prose.chapter_names`, `prose.book_stage_map` (corrected to include the
`findings` stage, a gap the architecture doc and the code's own hardcoded default both had),
`prose.search_default_limit`, `prose.edit_file_dir`. `prosestore.py`'s `chapter_names()`/
`book_stage_map()`/`search_default_limit()` now read `cfg.module_setting("cfg_prose", ...)` (were
`cfg.setting(...)`, the generic project-wide table — an earlier-round mistake this build corrects);
a new `edit_file_dir()` replaces the `CHAPTER_EDIT_OUT_DIR` hardcoded constant. `cfg_prose` is
itself catalogued in `cfg_table`/`cfg_column` (4 rows) and granted to `configmaint.propose` — found
live during this build's own `configmaint.validate` run (escalation #839, self-corrected): the
first version of the migration script created the table and its content rows but never
self-registered the table, the same gap every other project table avoids.

**2. Dispatcher registration.** `prose` as a `cfg_work_package` (`Prose.ps1`, `runs_over='none'`) +
5 `cfg_step` rows: the original 4 (`prose.extract`/`.search`/`.export_chapter`/`.import_chapter`,
code already built under escalation #784, config was the only missing piece) plus `prose.flag`
(new, §4 below).

**3. Write-layer governance.** `cfg_enum` for `prose_section.status`(4)/`.author`(3); `cfg_status_
flow` (4 rows, `entity='prose_section'`); `cfg_behaviour_rule` — 2 rows
(`prose-section-session-a-replace-author-gate`, `prose-section-two-patch-ordering`) — a third,
drafted in earlier rounds (`prose-section-supersede-only-discipline`, asserting `version = old.
version + 1`), is **not built**: §52's Model A rebuild already made that assertion false and built
the correct rule (`record-change-log-version-is-pointer`) — building both would leave two rules
disagreeing about the same table. `cfg_write_grant` — `apply_session_patch`→`prose_section`/
`prose_section_type` (`database='bible_research'`; the `record_change_log` grant already existed
from §52).

**4. `prose_section_type` column governance.** `cfg_enum` for `source_stage`(11)/`lifecycle_tag`(4)/
`book_label`(4) — documentation-of-record against columns with no CHECK constraint, not a runtime
lookup (matches §52.6's already-accepted `record_change_log` orphan-enum precedent, confirmed again
this round, escalations #840/#845). `cfg_column.use` filled for 4 previously-blank
`prose_section_type` columns (`book_order`/`book_label`/`section_order`/`section_label`) and
corrected for `prose_section`'s 4 citation columns (`registry_id`/`cluster_code`/
`characteristic_id`/`cluster_subgroup_id` — researcher: these belong in a future Concordance index
table, not decided/moved in this build).

**5. `prose.flag` — angle (a) of the quality-flag mechanism (proposal §12).** One new dispatcher
step, `iba.app.handlers.prose:flag` → `prosestore.run_flag()` — the only direct DB write
`prosestore.py` performs itself (every other operation is read-only or generates a patch file).
Raises one `wa_data_quality_flags` row (`flag_group='PROSE_QUALITY'`, escalation #833), deliberately
**with no `prose_section` reference** — which rows a flag concerns is found by search when a fix
actually runs (angle b, escalation #835, not built), never stored from raise time. `cfg_write_grant`
`prose_flag`→`wa_data_quality_flags`. A third `cfg_behaviour_rule` row,
`prose-quality-flag-on-upstream-change`, records the governing discipline (a methodology/
terminology/finding change touching live prose obligates a flag, not an immediate fix).

**6. `Prose.ps1` bug found and fixed during this build's own testing.** `-Input` (the
`ImportChapter` file parameter) silently failed to bind from the command line — `$Input` is a
PowerShell automatic variable (the pipeline-input enumerator); assigning a same-named parameter is
accepted at parse time but never actually set. Reproduced three ways (direct, splatted, colon
syntax), all failed identically. Renamed to `-InputFile` project-wide in the script; confirmed fixed
live. Not previously caught because `ImportChapter` had never been dispatcher-tested end-to-end
before this build (escalation #784 built it, but v1's own test plan tested the underlying Python
function, not the PS wrapper's argument binding).

**7. Reactivation.** The 4 original scripts (`build_programme_prose_extract.py`,
`export_prose_chapter_edit.py`, `import_prose_chapter_edit.py`, `search_prose.py`) —
`cfg_utility.inactive` `1→0`, `purpose` text rewritten to point at `prosestore.py` as the real
implementation. All 4 verified live (this round, not assumed) to already be thin wrappers with no
duplicate logic — `configmaint.validate` flagged them as "low config-density" (no direct
`cfg.setting()`/`cfg.enum()` call site of their own, since they delegate entirely); resolved as
`config_exempt=1`, matching 11 other pass-through scripts already carrying that flag, not left as a
standing advisory.

**Explicitly deferred, not silently dropped:** D10 (`prose.book_stage_map` vs. `book_label`
disagreement on 1 row) — researcher instruction, to the prose-edit stage, not this build. D3/D4/D5
(`prose_section_finding_link`'s FK, `prose_section_dimension_link`'s retirement, `cluster_code`'s
FK) — escalation #832. Angle (b) of the quality-flag mechanism (propose/approve/apply against real
flags) — escalation #835, on-hold.

**Files:** `iba/app/migration/prose_first_layer_build_v1_20260824.py` (idempotent, confirmed by a
clean re-run). Full design record: `iba/docs/prose-management-iba-first-layer-proposal-v1` through
`-v9-20260824.md`. Test results: `BUILD.md` §177.
