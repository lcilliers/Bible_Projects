# GOVERNANCE.md — how the app is governed by config (overview + history)

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
iba\app\ps\Escalation.ps1 -Action AnswerRun -RunId <run_id> -Decision Approve|Reject|Revise [-Comment ...]
# then re-run the SAME Propose command with -RunId <run_id> to act on the answer.
```

Coherence-checked before it ever reaches you (unknown table/column, bad enum, invalid JSON, a
`cfg_setting` insert missing `module`); only on **Approve** does the write commit, logged to
`cfg_change_detail`. **Hard technical enforcement** that *only* this path may write a `cfg_*` row
(vs. it being the one sanctioned path by convention) is not built — named in §6.

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

- **The approval escalation for a new word is REAL, not stubbed** (correcting this section's prior
  claim). `handlers/registry.py:create()` raises a genuine `registry.create` escalation and pauses
  the run; the researcher answers `Escalation.ps1 -Action Answer -Word <w> -Decision Yes|No`
  (confirmed live: escalation `#169`, `[blindness (spiritual]`, currently open). What remains a
  named, deliberate fast-follow (per §9A) is only the **answer shape** — still yes/no, not yet the
  three-way approve/reject/revise every other escalation in this app uses.
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
| `cfg_report.output_kind` / `.naming_scheme` / `.archive_dir` | md vs md+csv, filename stability, archive folder |
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
