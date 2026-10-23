# 2228 — Cluster reading index and the scope guard: test results (v1)

Escalation #2228 tool 2 (outputs/escalation/2228-cluster-reading-index-design-v1-20261023.md) and the guard on the scope resolver. Run 2026-10-23 by iba/app/tools/temp_2228_reading_index_test_run.py on a copy of iba.db (lib/dbsnapshot.copy_db), the files a scratch copy of _analytics/Clusters. R8 compares parse_refs with its default arguments against the committed version (git HEAD) over every current narrative block and cluster file. Result: 20/20 PASS.

| # | case | result | evidence | s |
|---|---|---|---|---|
| R0 | migration: applied (or already), then skipped | PASS | ['already applied -- 0 write(s); tables to create: []', 'already applied -- 0 write(s); tables to create: []'] |  |
| G1 | -Thread OT-108 (29,743 verses): refused as too wide, selectors listed | PASS | the request is too wide -- verses in the result (29743 against the limit 4000); reform it to a narrower scope. Verses by selector, widest first: cluster T2 (OT-108.17): 29605; cluster T3 (OT-108.13): 25976; cluster M72 (OT-108.4): 3972; cluster M15 (OT-108.11): 2203; cluster M18 (OT-108.8): 1370; cl |  |
| G2 | -Cluster T2: refused as too wide | PASS | the request is too wide -- verses in the result (29605 against the limit 4000); reform it to a narrower scope. Verses by selector, widest first: cluster T2: 29605 |  |
| G3 | -Cluster M72 (the largest M cluster, 3,972): allowed | PASS | {'verses': 3972, 'selectors': 1, 'not_resolved': 0} |  |
| G4a | -Cluster M72,M02 (over 4,000): refused | PASS | the request is too wide -- verses in the result (4553 against the limit 4000); reform it to a narrower scope. Verses by selector, widest first: cluster M72: 3972; cluster M02: 681 |  |
| G4b | -Cluster M72,M02 -OnlyStrong H3708A: allowed (the size is checked after the filter) | PASS | {'verses': 22, 'selectors': 2, 'not_resolved': 0} |  |
| G5 | time guard (max_seconds 0 on the copy): refused | PASS | the request is too wide -- still resolving after the time limit, seconds (0 against the limit 0); reform it to a narrower scope. Verses by selector, widest first: cluster M02: 681 |  |
| R8 | parse_refs with its default arguments: identical to the committed version over every current narrative block and every cluster file | PASS | 2935 texts, 0 differ |  |
| R1 | build over a scratch copy of _analytics/Clusters: every file, every reference less the bare follow-ons | PASS | 230 files; 50352 refs = parser 50352 (1598 bare follow-on refs left out); 0 file(s) indexed, 230 unchanged, 0 marked removed (0.8s) | 0.8 |
| R2 | build again, nothing changed: no file read, no row written | PASS | 0 file(s) indexed, 230 unchanged, 0 marked removed (0.7s) | 0.7 |
| R3 | one file edited: only it re-read; its earlier rows kept as deleted; the new reference found | PASS | 1 file(s) indexed, 229 unchanged, 0 marked removed (1.0s); rows 1753 -> 1754 live, 1753 deleted |  |
| R4 | one file deleted, one moved into archive/: both marked removed, their rows deleted | PASS | 0 file(s) indexed, 228 unchanged, 2 marked removed (0.7s); [<sqlite3.Row object at 0x0000018F50F6B430>, <sqlite3.Row object at 0x0000018F50F6AD40>] |  |
| R5 | synthetic file: each written form recorded with found_by, line kind and kind; the bare '(220)' not taken | PASS | missing []; extra [] |  |
| R5b | line numbers | PASS | [<sqlite3.Row object at 0x0000018F511779A0>, <sqlite3.Row object at 0x0000018F51176C20>, <sqlite3.Row object at 0x0000018F51174FD0>] |  |
| R6 | unresolved references kept with their reason | PASS | see R5 |  |
| R7 | query by a verse collection (M02 -OnlyStrong H3708A, 22 verses): one query | PASS | 22 of 22 verses named in the cluster files | 0.0 |
| R9 | time guard on the build (max_seconds 0): stops between files, says how many are left; the next build carries on | PASS | 0 file(s) indexed, 0 unchanged, 0 marked removed (0.7s); stopped at the time limit (reading_index.max_seconds 0) with 229 file(s) still to index -- run Build again to carry on // 229 file(s) indexed, 0 unchanged, 0 marked removed (7.2s) |  |
| R10 | report written to the setting's folder; its total equals the tables | PASS | reading-index-coverage-v1-20261023.md; 50075 |  |
| R11 | configmaint.validate hard checks on the copy (a migration not yet archived set aside) | PASS | none |  |
| R12 | speed: full build within a minute | PASS | 0.8s |  |

