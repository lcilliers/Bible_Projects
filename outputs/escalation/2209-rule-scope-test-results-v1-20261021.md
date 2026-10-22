# 2209 — Test results: rules linked to operations and shown at the point of use

Escalation #2209 part (a). Test plan: `iba/app/tools/temp_2209_rule_scope_test_run.py`, run 2026-10-21 on a copy of iba.db made with `lib/dbsnapshot.copy_db`; the hook ran against the copy (IBA_RULES_DB) in a scratch project folder. No live DB, state file or report written by the test. Synthetic cases: T1, T4, H9, H12, H13, H15. T2 checks the live run record, since archived scripts are gated (#2200).

Found live and fixed: the first hook matched words inside text (a heredoc body mentioning git commit), not only commands. Commands are now matched at the start of a line or segment; H13-H15 cover it. Also trimmed: with an action given, only that action's usage is shown, not the whole tool's (H1). Found live 2026-10-22 and fixed: a grep alternation ("a\|b") was split as a pipe; a pipe now needs a space either side (H17, H18).

22/22 pass.

| case | what | result | evidence |
|---|---|---|---|
| T2 | migration's audited writes are on record (229) and the table exists | PASS | 229 |
| T1 | with the table missing the check reports it | PASS | ['cfg_rule_scope is missing (#2209)'] |
| T3 | after the migration: no gaps; method rules on retired steps deactivated | PASS | 202 links, 41 general rules; gaps=[] |
| T4 | synthetic: unlinked rule, link to missing rule, unknown PS script, method rule on retired step | PASS | ['rule B:63 has no cfg_rule_scope link', 'cfg_rule_scope links B:9999, which is missing or inactive', 'cfg_rule_scope B:26 names PS script Nope.ps1, not in ps/', 'method rule 49 (one-integrated-read-genre-first) is active on step lexical.enrich, which is not active'] |
| H1 | first Escalation Update: refused with its rules (63, 45, escalation 13) and only the Update usage | PASS | deny; 9112 chars; refs: ['B:45', 'B:63', 'E:1', 'E:11', 'E:12', 'E:13', 'E:15', 'E:16', 'E:17', 'E:18', 'E:2', 'E:3', 'E:7'] |
| H2 | the same call re-issued passes | PASS | allow |
| H3 | a new action of the same tool: only its usage is new, so refused once with the usage | PASS | deny; Rules for this operation (Escalation.ps1, Escalation.ps1 -Action Raise), shown once per session before first use (#2209, cfg_rule_scope). Check the call against them, then re-issue it.  How to run Esc |
| H4 | a write under _analytics/Clusters: refused with the study and filing rules | PASS | deny; 17456 chars |
| H5 | an edit under iba/app: refused with the build rules (BUILD.md, USER-GUIDE, test plan) | PASS | deny; 7025 chars |
| H6 | git commit: refused once with rule 26, then passes | PASS | deny -> allow |
| H7 | a call with no governed operation passes | PASS | allow |
| H8 | a new session shows the rules again | PASS | deny |
| H9 | no database: the call passes (a broken check never blocks) | PASS | allow |
| H10 | a database query: refused once with the database rules (11, 13, 61, 67) | PASS | deny |
| H11 | a PS tool brings the method rules of its steps | PASS | deny; 32 method rules |
| H12 | a write outside the project passes | PASS | allow |
| H13 | text that only mentions git, a PS tool, a migration or a database (a heredoc body) passes | PASS | allow;  |
| H14 | git after cd ... && is a command: refused once | PASS | deny |
| H15 | a PS call after a here-string is found with its action; the here-string text is not | PASS | deny; refs B:63=True |
| H16 | a migration run: refused once with the migration rules (75, 62) | PASS | deny |
| H17 | a grep alternation naming a PS script or git is text, not a command: passes | PASS | allow;  |
| H18 | a PS call piped to Out-String is still found | PASS | deny |
