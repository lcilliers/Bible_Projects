# #2504 Draft: the stated procedure for adding a data table (v1, 2026-11-15)

Status: a draft for the researcher to correct (B:105). Nothing is written to GOVERNANCE.md, USER-GUIDE.md or config. Basis: the order that worked three times in Developer Mode: `collection_subgroup` and `collection_subgroup_surface` (#2503), `collection_layer_item` and the column `ib_node.subgroup_id` (#2505), read from `iba/app/migration/archive/collection_subgroup_index_2503_v1_20261114.py` and `layers_2505_v1_20261115.py`, and the requirement already stated in `cfg_behaviour_rule` 62 and `iba/app/GOVERNANCE.md` section 4. Every statement below is a step those migrations took, not a new rule.

## 1. What is stated today and what is missing

Rule 62 and GOVERNANCE.md section 4 say a new table registers itself in `cfg_table` and `cfg_column` (with the step, utility and write grants) in the same unit of work. Neither says in what order, through which call, how the physical table is made, or what the validation then expects. That order is learned today by reading an archived migration, which `governance.past_precedent_investigation_signals_missing_config` and rule 123 call the signal of a missing procedure.

## 2. The procedure (Developer Mode; standard mode proposes each row through `configmaint.propose`)

1. **Record and design.** An escalation is the record of the task (B:97); the design is approved first (B:105). The tables, columns, keys, enums, steps and the writers are named in the design.
2. **One migration script** in `iba/app/migration/`, named `<what>_<escalation>_v<n>_<yyyymmdd>.py`, with a run id `DEVMODE-<escalation>-<what>-<yyyymmdd>`. It is idempotent (a second run changes nothing), runs in one savepoint, and takes `--db`, `--dry-run` and `--no-snapshot`.
3. **Registration first, every write through `apply_logged`** (rule 75), in this order, each only where the row is absent:
   - `cfg_table` (database, name, grain, use, category `data`);
   - `cfg_column` for every column of the table (name, ordinal from 0, type, `is_pk`, `notnull`, `dflt`, `fk`, `use`, `expectation` as `enum.<name>` where the values are controlled, `source`, `filled_by`);
   - `cfg_unique` and `cfg_index`;
   - `cfg_enum` rows for each controlled value (with ordinals), and the `config_module` value when a new settings module is introduced;
   - `cfg_write_grant`: `migration` for the table, and the writer (the step, library or tool) that fills it, for every table it writes;
   - `cfg_setting` for every tunable value (the code holds none), `cfg_step`, `cfg_on_fail` (condition `refused`), `cfg_utility` for the library and for the migration itself (its `file_path` the archive path, with `config_exempt_reason`), `cfg_method_rule` and `cfg_behaviour_rule` where the change carries rules.
4. **Then the physical table**, in the same savepoint: `lib/db.table_ddl(cfg, table)` returns the `CREATE TABLE` and index SQL from the `cfg_column`, `cfg_unique` and `cfg_index` rows just written. A column added to an existing table is a `cfg_column` row with the next ordinal and then `ALTER TABLE ... ADD COLUMN`, with its index. A table with a `deleted` column gets a partial unique index over live rows (the soft-delete convention).
5. **Before any live run:** test on a copy (`python -m iba.app.lib.dbsnapshot --copy-to <path>`), with the tests of the module (B:46); a named snapshot before the live apply (`dbsnapshot.snapshot(<name>, named=True)`, the migration takes it unless `--no-snapshot`).
6. **Validate** with `Config-Maintenance.ps1 -Step Validate`. The one error expected before archiving is that the migration script is in no utility; after the live run the script moves to `iba/app/migration/archive/` (its `cfg_utility` row already names that path) and validate is run again. A validation run against a copy needs the copy inside `iba/app/db/`, because the value-quality check finds the project root from the database path.
7. **In the same unit of work:** the library, handler and PS entry point (B:41); the folder registration for any new folder (`FolderPurpose.ps1 -Action Set`, B:128); USER-GUIDE.md (B:42); BUILD.md with every file named (SC10); the ps tools worksheet when a PS script's parameters changed; the compliance and session records.

## 3. Decisions for the researcher

| # | Decision | Options | Recommendation |
|---|---|---|---|
| 1 | Where the procedure lives | A: a numbered procedure in GOVERNANCE.md section 4 (the control map's `mechanism` home), with USER-GUIDE.md pointing to it; B: USER-GUIDE.md only | A: the control map puts how config governs the code and the change path in GOVERNANCE.md; rule 62 and the document then agree |
| 2 | A config row for it | A: none (the control map holds procedures of this kind in the mechanism document; rule 62 already states the requirement); B: a `cfg_setting` listing the registration order | A: a second home would restate it (B:3) |
| 3 | Whether to build a helper (a function that registers a table from one description) | A: not now, the stated procedure first; B: build it | A: a mechanism is a design of its own (B:105) |
| 4 | Whether the validation should also check that a table written by a step has a write grant and a `use` text | A: already checked (`find_unregistered_tables_and_columns`, `cfg_write_grant`); B: add | A: no change |

## 4. Not done

No document or config row changed; no helper built.
