# Engine-controls migration into IBA — integrated plan (v3)

> v1 → v2 archived under `archive/`; the separate config-stubs draft (`engine-controls-config-stubs-draft-20260817.md`)
> is folded into this version rather than kept apart — per the researcher's correction: *"I actually
> want to see the config stubs and the plan as an integrated whole. While conceptualising each phase
> (mechanism, migration, code changes, rules for daily running of all the different dimensions) the
> plan should ensure that the appropriate configs are in place."* Every phase below now carries all
> four of those dimensions together — **Concept → Configs → Code → Daily-running rules** — instead
> of prose in one document and stub rows in another. **No config row below has been written to the
> DB.** All are drafts pending your decisions (§6).

## 1. The actual goal (unchanged from v2 — the researcher's own words, in full)

> *"The migration of the engine from research_db to IBA-db aims at consolidating the entire run
> control of the project and ensuring that the disciplines and structure of the research_db engine
> control is not neglected or lost. With the advent of IBA-db the run controls are fragmented and
> incomplete. A single and complete set of rules should apply for all engine activity. All engine
> activity across the whole project must consistently be captured. In terms of project governance,
> IBA App is in control of all processing in the project. Therefore, I expect to see the engine
> control to be in the configs, the governing principles captured in configs, the rules, tables,
> and everything else to be captured in configs. All routines should enforce the configs, and no
> engine operations should run outside the control of IBA and the configs."*

## 2. The real size of the fragmentation (measured, not assumed)

| surface | live `.py` files | registered in `cfg_utility`? |
|---|---|---|
| `iba/app/` | (the governed core) | yes, 33 modules |
| `engine/` | 15 (excl. `__init__.py`) | no |
| `scripts/` (excl. `archive/`) | ~330 | no |
| `research/`, `iba/prototype/`, `iba/scripts/`, repo-root loose scripts | ~15 | no |
| **total outside `iba/app/`+`engine/`+`archive/`** | **345** | **no** |

This is also escalation #648's own scope ("project-wide config-driven-rule sweep... on hold until
further instruction") — flagged again in §6, not resumed unilaterally.

---

## Phase 0 — the governance mechanism itself

### Concept
Before touching `engine/` or `scripts/`, close the hole that let all 345 files start life
ungoverned in the first place: any *new* script, anywhere, must be registered the moment it's
created, and the app must be able to catch it if it isn't — the forward-looking half v1 lacked.

### Configs
`governance.scripts_and_routines` already exists and half-covers this (scripts must belong to a
module/utility/library) but has no timing and no enforcement. One new companion row, not a
duplicate:

| table | row |
|---|---|
| `cfg_setting` | `key='governance.new_utility_registration_timing'`, `module='governance'`, `value="Any new script or routine, anywhere in the project, must be registered in cfg_utility (and cfg_step/cfg_write_grant if it writes data) in the same unit of work it is created -- operationalizes governance.scripts_and_routines with a timing rule and a real enforcement check (configmaint.validate: find_unregistered_project_scripts)."` |

### Code
`lib/cfgquality.py`: new `find_unregistered_project_scripts()` — walk the repo for `.py`/`.ps1`
files outside `iba/app/`/`archive/`/`temp_*`, flag any not present in `cfg_utility.file_path`, same
shape as `find_cfg_tables_missing_configmaint_grant()` already built tonight for #657 (`BUILD.md`
§120). Wired into `handlers/configmaint.py:validate()` as a hard error, same severity class.

### Daily-running rules
No new discipline to remember — it rides on the existing habit of running
`Config-Maintenance.ps1 -Step Validate`. From the moment this lands, *any* unregistered script
anywhere in the project is a hard-error finding the next time validate runs, not a thing that has
to be rediscovered by a manual sweep again. This is the one piece of the plan with **zero**
dependency on #653/#657 or the DB question below — buildable now, on its own.

---

## Phase 1 — `engine/` itself (gated on #653/#657 landing)

### Concept
Not a lift-and-shift (escalation #656's standing rule: redesign, don't auto-adopt). `audit_word.py`'s
own 12-step `Pre-A1`…`A11` sequence already reads as an IBA-shaped `cfg_step` chain — the redesign
is mostly *translation*, not invention.

### Configs

**`cfg_utility`** — 15 rows, one per `engine/` module, purpose text from each file's own docstring
(not invented). `gap_fill.py` drafted **already `inactive=1`** — registering its retirement, not
reviving it:

| module | file_path | purpose | inactive | config_exempt |
|---|---|---|---|---|
| `engine_audit` | `engine/audit.py` | Audit framework — WR-01 through WR-20, run after all writes | 0 | 0 |
| `engine_audit_word` | `engine/audit_word.py` | AUDIT_WORD mode (v4) — Pre-A1 through A11, unified new-word + re-audit pipeline | 0 | 0 |
| `engine_backup` | `engine/backup.py` | DB backup management (SG-01, SG-12, SG-13) — timestamped pre-run backup, abort if it fails | 0 | 0 |
| `engine_constants` | `engine/constants.py` | Shared constants | 0 | 1 *(values move to cfg_setting instead — see redesign note below)* |
| `engine_db` | `engine/db.py` | DB access helpers (wraps `analytics/db_client.py`) | 0 | 0 |
| `engine_cli` | `engine/engine.py` | CLI entry point (`python -m engine.engine`) | 0 | 0 |
| `engine_flag` | `engine/flag_engine.py` | Derivable flag evaluation (S5/N16/A7) | 0 | 0 |
| `engine_gap_fill` | `engine/gap_fill.py` | GAP_FILL mode (S1–S8), superseded by `audit_word` | **1** | 0 |
| `engine_meaning_parser` | `engine/meaning_parser.py` | Meaning text parser → `wa_meaning_parsed`/`_sense`/`_stem`, `wa_lsj_parsed` | 0 | 0 |
| `engine_migrate` | `engine/migrate.py` | Schema migration runner v2.2→v3.0 (M01–M10) | 0 | 1 *(one-shot historical, same class as `iba/app/migration/*`)* |
| `engine_register` | `engine/register.py` | REGISTER subcommand — new `word_registry` row | 0 | 0 |
| `engine_report` | `engine/report.py` | Word overview report | 0 | 0 |
| `engine_run_log` | `engine/run_log.py` | `engine_run_log`/`word_run_state` write helpers | 0 | 0 |
| `engine_softdelete` | `engine/softdelete.py` | Shared soft-delete cascade helpers (H1–H3, H5) | 0 | 0 |
| `engine_span_filter` | `engine/span_filter.py` | STEP `masterSearch` HTML span filtering (§5.2 v4) | 0 | 0 |

**`cfg_work_package`** — 1 row: `name='word-audit'`, `ps_script='TBD: Word-Audit.ps1'`,
`runs_over='word'`, `chained=1` (no name collision — checked live against `new-word`/
`word-registry-span-report`, the only other `word*` work packages that exist today).

**`cfg_step`** — the real 12-step sequence, straight from `audit_word.py`'s own docstring
(lines 47–88), `handler` placeholder (`TBD:` — the Python doesn't exist yet):

| ordinal | step | does | kind |
|---|---|---|---|
| 0 | `word.lock_open` | Lock sentinel + open run log | operations |
| 1 | `word.confirm` | Registry display + CONFIRM prompt | operations |
| 2 | `word.snapshot` | DB snapshot + structural completeness check | operations |
| 3 | `word.load_json` | Load + validate latest Step 1 JSON | operations |
| 4 | `word.gap_report` | Build gap report (Term/Related/Verse/VTL) | operations |
| 5 | `word.gap_display` | Display gap report (+ interactive approve gate) | operations |
| 6 | `word.apply_changes` | Apply changes, one transaction per stream | operations |
| 7 | `word.meaning` | Meaning handler — parse + migrate legacy fields | operations |
| 8 | `word.flag_reset` | Quality flag reset (DATA_COVERAGE), re-derive | operations |
| 9 | `word.audit_checks` | WR-01–WR-20 + write `word_run_state` (PROVISIONAL) | operations |
| 10 | `word.registry_close` | Registry + file-index update, `last_automation_run='AUDITED'` | operations |
| 11 | `word.export` | Full-word JSON export | operations |

**`cfg_on_fail`** — the pattern `audit_word.py` already has built in (a CONFIRM prompt at A1, an
`--interactive` approve gate at A5) maps directly to IBA's pause-continue path, same shape as
`registry.create`'s existing rows:

| step | condition | path | message |
|---|---|---|---|
| `word.confirm` | `needs-confirmation` | `pause-continue` | word display shown; confirm to proceed |
| `word.gap_display` | `needs-approval` | `pause-continue` | gap report shown; approve to apply (only when run `--interactive`) |

**`cfg_write_grant`** — deliberately left shape-only, not filled in: which table each writer
touches depends entirely on the still-open one-DB-vs-two question (Phase 3, below) — a real
`table_name` here would be a guess, not a draft, until that's answered.

### Code
New `iba/app/handlers/wordaudit.py` (12 functions, one per step above) + a bootstrap migration
script (`iba/app/migration/bootstrap_word_audit.py`, same shape as every other `bootstrap_*.py`) to
load the config rows above. `constants.py`'s thresholds (`HIGH_FREQ_THRESHOLD`,
`THIN_DATA_THRESHOLD`, `STALE_LOCK_SECONDS`, etc.) become `cfg_setting` rows, module `engine` —
mechanical, no logic change, **can start independently of the 12-step redesign** since it doesn't
touch data tables at all. `audit.py`'s 20 `WR-*` checks get reviewed one-by-one once #653 confirms
which `bible_research.db` tables persist — each becomes either a `configmaint`-style validate check
or a `word-audit` step, not a batch port.

### Daily-running rules
Once built: `Word-Audit.ps1 -Registry N` (or `python -m iba.app.run word-audit --step ...`)
replaces `python -m engine.engine --mode=audit_word`. `module_blocking` (already live, #646)
automatically applies — an unresolved escalation against any `word.*` step blocks the whole
sequence, same as everything else in IBA. `cfg_write_grant` automatically enforces which tables
each step may touch. No separate "remember to run the audit" discipline — it's dispatched,
gated, and recorded exactly like every other IBA work package, which is the entire point.

---

## Phase 2 — `scripts/`'s ~330 files (sized here for the first time; representative pattern, not a full stub set)

### Concept
`CLAUDE.md` §6 already sorts these by prefix (`_check_*`/`verify_*` = read-only,
`_apply_*`/`_repair_*` = mutates, `_delete_*` = destructive) — a naming *convention*, enforced by
nobody. The registration burden differs sharply by category, so the plan shows one real example
per category rather than treating all 330 as equal-weight work.

### Configs (3 real, representative examples — not the full 330)

| script | category | `cfg_utility.purpose` (from its own docstring) | `cfg_write_grant` needed? |
|---|---|---|---|
| `_assess_cluster_profiles.py` | read-only (`_assess_*`) | "Per-cluster L1 profile correlated to the co-occurrence matrix... NO DB writes." | none — registration only |
| `_apply_backfill_verse_id_active_20260701.py` | mutating (`_apply_*`) | "Backfill `wa_verse_records.verse_id` for ACTIVE rows where it is currently NULL." | yes — `wa_verse_records` |
| `_delete_empty_fi.py` | destructive (`_delete_*`) | (no docstring today — itself a finding: destructive scripts are exactly the ones that most need one) | yes — the `wa_file_index` rows it targets |

### Code
Read-only scripts (the majority, by count — `_assess_*`/`_check_*`/`build_*`/`generate_*`/
`export_*`) need **only** a `cfg_utility` row; nothing about how they run changes. Mutating and
destructive scripts need the full treatment: a `cfg_step`/`cfg_write_grant` pair and, per escalation
#656's standing rule, a deliberate review of whether the operation still makes sense against IBA's
current model before it's wired to run through `run.py` at all — some of the 330 are almost
certainly stale enough to retire outright rather than migrate (`_delete_empty_fi.py`'s missing
docstring is a small, live instance of exactly that risk).

### Daily-running rules
Phase 0's integrity check is what actually keeps 330 files from being a one-time sweep that goes
stale again — every script here shows up as a `configmaint.validate` finding until it's registered,
so this phase can be worked incrementally (a handful at a time) rather than as one big-bang pass,
without silently losing track of what's left.

---

## Phase 3 — the one-DB-vs-two-DB question (a decision, not a build phase)

Explicitly undecided by the researcher: *"I am not sure what would work best, if the tables should
be consolidated into a single DB, or if the rules can be clear and precise so that the current
tables can continue to operate without confusion, neglect or duplication."*

| | consolidate into one DB (`iba.db`) | keep two DBs, config-precise ownership |
|---|---|---|
| **for** | "one set of rules" becomes literally true; no cross-DB reference friction | avoids a ~766 MB physical migration and its risk (this project already lost 6 weeks once to DB corruption, `wa-db-loss-incident-20260603.md`); prose/findings (`bible_research.db`) is genuinely different data-shape from process-control/base-data (`iba.db`) |
| **against** | large, one-way, risky migration of live research data; blurs `governance.scope_research_db` vs `governance.scope_iba_db`'s current clean split | needs real discipline (`cfg_table`/`cfg_column` coverage across **both** DBs, checked not just documented) or it becomes exactly the "confusion, neglect, duplication" being worried about |
| **config footprint either way** | `cfg_write_grant.table_name` values become `iba.db` table names throughout | `cfg_write_grant.table_name` values stay `bible_research.db` names for those writers; `cfg_table`/`cfg_column` describe both DBs (per governance.tables/`governance.table_columns`, already stated as "applies to all databases") |

Position (unchanged from v2): don't decide this now. Phase 0's mechanism and Phase 2's
categorisation work identically either way — a `cfg_utility` row and a write-grant don't care which
physical file the table lives in. Revisit once #653/#657 finish surfacing which `bible_research.db`
tables are actually base-data-vs-findings, with evidence instead of a guess.

---

## 4. Sequencing

**Phase 0 → build now, no dependency.** **Phase 1 (`engine/`) and Phase 2 (`scripts/`) → after
#653/#657 land**, for the same reason v1/v2 already gave: building checks/steps against tables about
to be marked inactive is wasted work. **Phase 3 → a decision, revisited with #653/#657's evidence**,
not built.

## 5. What changed from v2

Everything in v2 is still here, but restructured so every phase carries its own configs, code, and
day-to-day operating rule together — not a plan document and a separate stub-examples document.
Phase 2 (`scripts/`) now has real representative stubs (3 scripts, one per risk category) instead of
being deferred entirely to "its own follow-up plan." The `47`→`20` WR-check correction (found while
drafting the original stub doc) carries forward.

## 6. Decisions requested

1. Approve **Phase 0** to start now, independent of #653/#657?
2. Does this reading — the researcher's comments on v1 effectively supersede escalation #648's "on
   hold until further instruction" — hold, or should #648 stay separately gated?
3. Confirm the "don't decide the DB question yet" stance in Phase 3, or state a preference now?
4. Is the Phase 2 representative-3-script pattern the right grain for the `scripts/` triage, or did
   you want the full ~330 sized/categorised now rather than deferred to its own pass?
