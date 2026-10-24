# #2268 Config alignment: test results on a copy (v1)

**Date:** 2026-10-24 · **Escalation:** #2268 · **Migration:** `iba/app/migration/config_alignment_2268_v1_20261024.py` · **Copies:** backup-API copies of iba.db (`dbsnapshot.copy_db`) in the session scratch folder.

| Case | Result | Detail |
|---|---|---|
| T1 dry run on the copy | PASS | DRY RUN -- 312 write(s): cfg_behaviour_rule update 30, cfg_column update 10, cfg_control_home update 3, cfg_enum insert 21, cfg_enum update 7, cfg_method_rule insert 60, cfg_method_rule update 92, cfg_prose_concept insert 6, cfg_quality_check insert 21, cfg_quality_check update 18, cfg_rule_scope insert 13, cfg_rule_scope update 10, cfg_setting insert 3, cfg_setting update 6, cfg_status_flow insert 8, cfg_table update 3, cfg_utility insert 1 |
| T2 apply on the copy | PASS | 312 write(s) applied (run DEVMODE-2268-CONFIG-ALIGNMENT-20261024, logged to cfg_change_detail): cfg_behaviour_rule update 30, cfg_column update 10, cfg_control_home update 3, cfg_enum insert 21, cfg_enum update 7, cfg_method_rule insert 60, cfg_method_rule update 92, cfg_prose_concept insert 6, cfg_quality_check insert 21, cfg_quality_check update 18, cfg_rule_scope insert 13, cfg_rule_scope update 10, cfg_setting insert 3, cfg_setting update 6, cfg_status_flow insert 8, cfg_table update 3, cfg_utility insert 1 |
| T3 validate: no new coherence error | PASS | before 53, after 53; new: none; cleared: none |
| T4 re-run refused (already applied) | PASS | already applied (run DEVMODE-2268-CONFIG-ALIGNMENT-20261024 is in cfg_change_detail) |
| T5 every write logged in cfg_change_detail | PASS | 312 rows under DEVMODE-2268-CONFIG-ALIGNMENT-20261024 |
| T6 reading.gap_types matches cfg_enum reading_gap_type (reading.gap_types() refuses otherwise) | PASS | 14 types; setting-only []; enum-only [] |
| T7 method rules delivered at Reading.ps1 (the hook's own query) | PASS | 53 rules, e.g. RG-01 read-outward, RG-02 passage-and-genre, RG-03 role-per-occurrence, RG-04 qualifier-binding |
| T8 retired rules inactive with no live scope link | PASS | active: []; links: [] |
| T9 reworded study rules now delivered at Reading.ps1 | PASS | 19 rules scoped to Reading.ps1 |
| T10 quality checks: 21 active on reading.check, none active elsewhere | PASS | [('closing.set', 0, 4), ('hib.set', 0, 4), ('operation.set', 0, 3), ('passage.build', 0, 1), ('phenomenon.set', 0, 6), ('reading.check', 1, 21)] |
| T11 D1/D2 session rules held inactive until build B3 | PASS | 7 rows, active 0 |
| T12 base-data method rules kept, 77 re-homed to cluster.assign | PASS | 9 kept |
| T13 rows read by live code left for their builds | PASS | [('cluster.recording_similarity_threshold', 0), ('ib_observation.meaning_source_aliases', 0), ('lexical.llm_model', 0), ('reading.output_dir', 0)] |
| T14 partial rewording kept the rest of the text (B:70) | PASS | Cluster allocation (cluster_strong) is a loose association for the purposes of analysis. A reading that finds a word associated with another cluster records tha... |
| T15 synthetic: expected text missing -> refused, nothing written | PASS | rc 2; REFUSED, nothing written: B:74 rule_text: expected text not found: A thread is not worked as a task: it moves only when a stran...; 0 rows |

**15 of 15 passed.**

