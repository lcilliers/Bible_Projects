# Engine-controls migration — draft config stubs

> **Nothing here has been written to the DB.** These are illustrative rows for the plan
> ([engine-controls-migration-plan-v2-20260817.md](engine-controls-migration-plan-v2-20260817.md))
> pending your decisions on escalation #670. Real values (handlers especially) are placeholders —
> `TBD:` marks code that doesn't exist yet. One correction made while drafting these: v1/v2 of the
> plan said `audit.py` has 47 `WR-*` checks; re-counted by **distinct** code (not `grep`
> line-matches) — it's 20 (`WR-01`–`WR-20`), matching `CLAUDE.md` §4 all along. Fixed in v2.

## 1. `cfg_setting` (module `governance`) — the standing rule, 1 row

Found while drafting: this isn't a brand-new rule — `governance.scripts_and_routines` already says
scripts must belong to a module/utility/library. What's missing is *timing* (when does
registration have to happen) and *enforcement* (what checks it). Proposed as a companion row, not a
duplicate:

| key | value | module |
|---|---|---|
| `governance.scripts_and_routines` *(existing, unchanged)* | `"All scripts and routines must belong to a module, utility, library, or be a temporary script. Temporary scripts must be prefixed with temp_."` | governance |
| `governance.new_utility_registration_timing` **(new)** | `"Any new script or routine, anywhere in the project, must be registered in cfg_utility (and cfg_step/cfg_write_grant if it writes data) in the same unit of work it is created -- operationalizes governance.scripts_and_routines with a timing rule and a real enforcement check (configmaint.validate: find_unregistered_project_scripts)."` | governance |

## 2. `cfg_utility` — one row per `engine/` module, 15 rows

Real purposes, taken from each file's own docstring header, not invented. `gap_fill.py` drafted
**already `inactive=1`** — it's already-superseded (`CLAUDE.md` §4), so registering it means
registering its retirement, not reviving it.

| module | file_path | purpose | inactive | config_exempt |
|---|---|---|---|---|
| `engine_audit` | `engine/audit.py` | Audit framework — WR-01 through WR-20, run after all writes | 0 | 0 |
| `engine_audit_word` | `engine/audit_word.py` | AUDIT_WORD mode (v4) — steps Pre-A1 through A11, unified new-word + re-audit pipeline | 0 | 0 |
| `engine_backup` | `engine/backup.py` | DB backup management (SG-01, SG-12, SG-13) — pre-run timestamped backup, abort if it fails | 0 | 0 |
| `engine_constants` | `engine/constants.py` | Shared constants for the engine | 0 | 1 *(defines values other rows would read as cfg_setting instead — see §1's redesign note)* |
| `engine_db` | `engine/db.py` | DB access helpers — wraps `analytics/db_client.py`, engine-specific queries | 0 | 0 |
| `engine_cli` | `engine/engine.py` | CLI entry point (`python -m engine.engine`) | 0 | 0 |
| `engine_flag` | `engine/flag_engine.py` | Derivable flag evaluation (S5/N16/A7) — flags determinable from data alone | 0 | 0 |
| `engine_gap_fill` | `engine/gap_fill.py` | GAP_FILL mode (S1–S8) — fills missing-data streams on already-imported words | **1** | 0 |
| `engine_meaning_parser` | `engine/meaning_parser.py` | Meaning text parser — populates `wa_meaning_parsed`/`_sense`/`_stem`, `wa_lsj_parsed` | 0 | 0 |
| `engine_migrate` | `engine/migrate.py` | Schema migration runner v2.2→v3.0 (M01–M10) | 0 | 1 *(one-shot historical migrations, same class as `iba/app/migration/*`)* |
| `engine_register` | `engine/register.py` | REGISTER subcommand — adds a new `word_registry` row | 0 | 0 |
| `engine_report` | `engine/report.py` | Word overview report (`--report`) | 0 | 0 |
| `engine_run_log` | `engine/run_log.py` | `engine_run_log`/`word_run_state` write helpers | 0 | 0 |
| `engine_softdelete` | `engine/softdelete.py` | Shared soft-delete cascade helpers (H1–H3, H5 hardening) | 0 | 0 |
| `engine_span_filter` | `engine/span_filter.py` | STEP `masterSearch` HTML span-tag filtering (§5.2 v4) | 0 | 0 |

## 3. `cfg_work_package` — 1 row (illustrative name, not fixed)

| name | ps_script | runs_over | chained | complete_message |
|---|---|---|---|---|
| `word-audit` | `TBD: Word-Audit.ps1` | `word` | 1 | `TBD` |

## 4. `cfg_step` — the Pre-A1…A11 sequence, 12 rows

Real step names + descriptions from `audit_word.py`'s own docstring (lines 47–88), not invented.
`handler` is placeholder — none of this Python exists in `iba/app/` yet; that's phase 2 of the plan,
gated on #653/#657 per the plan's §5.

| ordinal | step | does | handler | kind |
|---|---|---|---|---|
| 0 | `word.lock_open` | Lock sentinel + open run log | `TBD: handlers.wordaudit:lock_open` | operations |
| 1 | `word.confirm` | Registry display + CONFIRM prompt | `TBD: handlers.wordaudit:confirm` | operations |
| 2 | `word.snapshot` | DB snapshot (Word Extract Report) + structural completeness check | `TBD: handlers.wordaudit:snapshot` | operations |
| 3 | `word.load_json` | Load + validate latest Step 1 JSON | `TBD: handlers.wordaudit:load_json` | operations |
| 4 | `word.gap_report` | Build gap report (Term/Related/Verse/VTL streams) | `TBD: handlers.wordaudit:gap_report` | operations |
| 5 | `word.gap_display` | Display gap report (+ interactive approve gate) | `TBD: handlers.wordaudit:gap_display` | operations |
| 6 | `word.apply_changes` | Apply changes, all streams, one transaction per stream | `TBD: handlers.wordaudit:apply_changes` | operations |
| 7 | `word.meaning` | Meaning handler — parse from JSON, migrate legacy term-field records | `TBD: handlers.wordaudit:meaning` | operations |
| 8 | `word.flag_reset` | Quality flag reset (DATA_COVERAGE group), re-derive | `TBD: handlers.wordaudit:flag_reset` | operations |
| 9 | `word.audit_checks` | Audit checks WR-01–WR-20 + write `word_run_state` (PROVISIONAL) | `TBD: handlers.wordaudit:audit_checks` | operations |
| 10 | `word.registry_close` | Registry + file-index update, close run, `last_automation_run='AUDITED'` | `TBD: handlers.wordaudit:registry_close` | operations |
| 11 | `word.export` | Full-word JSON export | `TBD: handlers.wordaudit:export` | operations |

## 5. `cfg_write_grant` — 2 illustrative rows (shape only)

Left minimal deliberately: real table names depend entirely on the still-open one-DB-vs-two
question (plan §4) — a grant naming a `bible_research.db` table means something different
depending on that answer, so filling this in now would be guessing, not drafting.

| writer | table_name | inactive |
|---|---|---|
| `word.apply_changes` | `TBD: wa_verse_records (or its iba.db successor, per plan §4)` | — |
| `word.audit_checks` | `TBD: word_run_state (or its iba.db successor, per plan §4)` | — |

## What's deliberately NOT stubbed here

- The 20 `WR-*` checks themselves (§3 "redesign, don't port" — each needs a real per-check
  decision against whichever tables persist, not a mechanical row).
- Any `scripts/`-side stub (345 files) — phase 3 of the plan, its own follow-up sizing pass.
- `cfg_table`/`cfg_column` rows for whichever `bible_research.db` tables `word-audit` would touch —
  that's escalation #653's work, already in progress separately.
