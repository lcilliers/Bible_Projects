# #2315 Config alignment for the three steps: inventory so far (not final)

Researcher, chat 2026-10-27 (verbatim): "All stale configs for step 1 - 3 must now be soft deleted or update, and all missing configs for these steps must now be created." Also on #2161 and #2259: "allign these rules and configs, if they are old retire them." Nothing is changed yet. The inventory stopped when the command check failed; the last pass (section 4) is not run.

## 1. Where the three steps' config lives (read from the live store)

- Steps: `cfg_step` work package `reading` (reading.open, gather, observe, record, check; synergy to account are later steps), `verse_scope.resolve`, `verse_collate.collate`, `open_item.*`, `cluster.surface_*`.
- Method rules on `reading.open` (RM-01 to RM-04, RO3 to RO6, RO8, RO10, RO13) and `reading.observe` (RO1, RO2, RO11, RG-01 to RG-25, RW-01 to RW-11, RS-01, RS-02), all active.
- Settings: `reading.*` (8 rows), `verse_collate.*`, `verse_scope.*`, `open_item.*`.
- Enums: `reading_gap_type` (15, 2 inactive), `reading_state`.

## 2. Already inactive (no action)

Method rules for `word.read`, `cluster.read` (RC-01 to RC-07), `cluster.subgroup`, `cluster.reading`, `cluster.answer`, `lexical.*`; steps `cluster.subgroup`, `cluster.reading`, `cluster.answer`; `strand_reading.output_dir`.

## 3. Findings that bear on the plan

1. `lexical.llm_*` settings are still read by live code (`iba/app/lib/surfacemap.py`, `iba/app/handlers/surfacemap.py`, `iba/app/handlers/lexical.py`, `iba/app/handlers/cluster.py`). The surface-map tail pass uses the API. They are not stale for the three steps; soft deleting them would break `cluster.surface_tail`.
2. Candidate duplicates among active rules, by title (texts not yet compared): RM-03 and RO8 (no whole cluster), RM-04 and RO3 (gather, not redo), RM-02 and RO10 (objective is home), RO2 and RW-09 (earlier observations read into focus).
3. Candidate stale labels: RO6 and others use D1 to D4 from the superseded design; the `reading.open`, `gather`, `observe` and `record` step descriptions use "D3 and D4".
4. Candidate missing, from the researcher's rulings (chat 2026-10-26 and 2026-10-27): (a) the scope is a subgroup or a segment of one, and the scope JSON is one file per scope run, saved to the cluster's folder (`reading.output_dir` is `outputs/reading`); (b) node creation: nodes are created when a subgroup is processed, the rest of a verse's surfaces are completed when the verse enters a scope, one node per surface and no duplicate scan (#2308 D1 to D3; the NR rules cover only the sweep); (c) nodes without an occurrence id are completed as their verses are read, nodes with no verse and observations with no node are not reached (a stated limit); (d) open items related to a scope are never silently ignored (no rule found by title).

## 4. Not yet run

Compare the full text of the pairs in finding 2; list every rule and step text using D-labels; search the reading rules for an open-item rule; confirm `reading.output_dir` use in code; check that each gap type in `reading.gap_types` has a detector or is marked as having none.

## 5. Proposal

After section 4, one table: each row to soft delete or update (with the replacing row), and each row to create, for approval before any write. Writes go through a migration under `iba/app/migration/`, tested on a copy first.
