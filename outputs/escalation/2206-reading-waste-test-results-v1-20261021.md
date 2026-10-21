# 2206 — Test results: reading waste build (options 1, 2a, 3, 4, 5 and the sec 42 fix)

Escalation #2206. Test plan: `iba/app/tools/temp_2206_reading_waste_test_run.py`, run 2026-10-21 on a copy of iba.db and bible_research.db made with `lib/dbsnapshot.copy_db` (SQLite backup API). CONFIG-REPORT generation was redirected to scratch; no live DB or live file was written by the test. Synthetic cases: T3, T8, T11, T12, T13, T14, T15. Fixture notes: the new migration is filtered from the unregistered-script check in the copy run (it was registered at its archive path); T1 checks the live run's audited writes, since archived scripts are gated (#2200).

Found by testing and fixed before the live run: an unchanged re-run added a version to the open item instead of matching it (the stored context lacked the summary that open_duplicate matches on); T14 and T15 cover it.

15/15 pass.

| case | what | result | evidence |
|---|---|---|---|
| T1 | migration's 2 writes are in cfg_change_detail and the setting is live | PASS | [('cfg_setting', 'insert'), ('cfg_utility', 'insert')] |
| T2 | compliance.rules leaves out the 7 value settings, keeps scripts_ps_dir | PASS | 45 governance rows delivered; excluded 7 |
| T3 | no value_settings row: every governance setting delivered (fails open to reading) | PASS | 52 = 45 + 7 |
| T4 | unenforced list holds no context_delivered rule | PASS | 13 listed: [chat] #74 open-threads-carried-as-escalations — partially_enforced; [chat] #76 narrative-claim-register-kept-in-iba-db — partially_enforced; [chat] #81 session-compliance-restated-and-proved — partially_enforced; [chat] #82 session-close-blocks-commit-on-open-findings — partially_enforced; [development] #46 test-plan-per-module-utility — deliberately_deferred; [development] #66 cluster-label-must-track-membership — buildable_not_built; [development] #97 developer-mode-scope-and-conduct — partially_enforced; [documentation] #32 no-hedge-in-complete-records — partially_enforced; [filing] #56 naming-shape — partially_enforced; [filing] #58 archiving-trigger — partially_enforced; [filing] #60 tool-report-path-vs-deliverable-document — buildable_not_built; [sqlite] #68 stage1-corrections-only-via-real-rerun — buildable_not_built; [sqlite] #78 narrative-chapters-change-only-through-the-register — partially_enforced |
| T5 | baseline found from the latest approved advisory escalation (old format) | PASS | #2107, 259 fingerprints in 26 categories |
| T6 | validate vs baseline: escalates only new findings, preset is counts+fingerprints (no lists) | PASS | condition=needs-review; question=cfg_* is structurally coherent, but has new findings since #2107 was acknowledged needing your judgement: 3 utility module(s) with zero cfg.setting()/cfg.enum() usage, 5 behaviour rule(s) with no control, 9 escalation-tied file(s) not carrying their escalation-id prefix, 2 SQL scratch file(s) violat; preset 1943 bytes |
| T7 | after approval, the same findings are not asked again | PASS | raised #2207 context 2852 chars; rerun: ok: no new findings: 4 orphan config(s), 12 utility module(s) with zero cfg.setting()/cfg.enum() usage, 13 behaviour rule(s) with no control, 2 PS script(s) bypassing run.py, 27 escalation-tied file(s) no |
| T8 | a new finding is escalated, and only it counts as new | PASS | condition=needs-review; new={'query_file_convention': 1} |
| T14 | re-run with unchanged findings while an item is open: matched, no new version | PASS | #2208 v1 -> v1; identical to already-open escalation #2208 (raised 2026-10-21T17:47:47Z) — not re-raised; answer #2208 to resolve this f |
| T15 | findings change while open: recorded once as a new version, the next identical run matches it | PASS | #2208 v1 -> v2; second run: identical to already-open escalation #2208 (raised 2026-10-21T17:47:47Z) — not re-raised; answer #22 |
| T9 | list report: no per-version history table; parked items one line each | PASS | 10762 bytes (live v185 was 22345); 13 parked lines |
| T10 | item worked this session (#2177, latest 2026-10-21T17:23:31Z) does not block | PASS | no block |
| T11 | session started after the item's last change: it still blocks | PASS | block |
| T12 | no session record: nothing is left out, it blocks | PASS | block |
| T13 | retry after a block never blocks again | PASS | {} |
