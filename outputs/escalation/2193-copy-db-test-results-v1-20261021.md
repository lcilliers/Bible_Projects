# #2193 test results: dbsnapshot.copy_db and snapshot

Run by `iba/app/tools/temp_2193_test_plan_run.py` on 2026-10-21, against `iba/app/lib/dbsnapshot.py` as changed under #2193.

| case | expected | actual | result |
|---|---|---|---|
| WAL row: plain file copy | 0 rows (misses the WAL write) | 0 rows | pass |
| WAL row: copy_db | 1 row | 1 rows | pass |
| copy_db onto an existing file | FileExistsError | FileExistsError | pass |
| live iba.db: row counts, every table | 102 tables equal | 102 equal, differ: none | pass |
| live iba.db copy: quick_check | ok | ok | pass |
| snapshot() | a snapshot that passes quick_check | iba-20261021T094923Z-t2193.db | pass |
| snapshot() with IBA_NO_SNAPSHOT=1 | None | None | pass |
| CLI --copy-to | exit 0, file written | exit 0, exists=True | pass |
| run.py pre-run snapshot (Escalation.ps1 -Action List, run 20261021-104942) | snapshot made by copy_db, quick_check ok, latest escalation present | iba-20261021T094943Z-escalation-reporting-run-20261021-104942.db, 854.0 MB, quick_check ok, max escalation id 2199 = live | pass |
