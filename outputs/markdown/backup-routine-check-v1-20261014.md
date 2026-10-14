# Backup routine check — 2026-10-14

Researcher, chat 2026-10-14: *"i think there is an issue with the backup routines and daily processing of backups, can you check it."*

Read-only investigation. Nothing on the NAS or in the scheduled tasks was changed.

## Summary

| # | Problem | Since | Effect |
|---|---|---|---|
| 1 | `bible_research.db` backup refuses to run (size guard) | 2026-09-28 | No dedicated, integrity-checked NAS backup of the research DB for 17 days. Only the passive folder mirror holds a copy. |
| 2 | `iba.db` backup task killed or not run | 2026-10-10 | Last **verified** iba.db backup is 2026-10-09. The 10-11 file on the NAS is unverified. |
| 3 | The watchdog does not watch the iba.db job | since that job was added | Problem 2 raised no alert. |
| 4 | ~~Backup files deleted from `db_backups`~~ | — | **Not a fault.** The researcher deleted old backups to save space (chat 2026-10-14). |

The full mirror (18:30) is healthy: last run 2026-10-13, robocopy OK.

## 1. bible_research.db: refused as "implausibly small"

- The task `BibleResearch DB Backup to NAS` exits with code 3, meaning the source DB is implausibly small. Local status file `C:\Users\lerouxc\nas_mirror_logs\status_dbbackup.txt`: `FAIL|2026-10-13T18:00:02|source DB implausibly small (possible corruption) — backup refused`.
- `scripts/backup_db_to_nas.py` refuses any source under `MIN_PLAUSIBLE_BYTES = 50 MB`.
- `database/bible_research.db` is now **37,720,064 bytes (36 MB)**. It was last written 2026-09-27 18:03.
  - The last NAS backup, `bible_research_20260927T170004Z.db` from 18:00 that day, was 840.5 MB.
  - The shrink fits the 2026-09-24 ruling that the DB is prose-only, with the finding tables purged. I have not confirmed the exact operation.
- The live DB is healthy: `PRAGMA integrity_check` = `ok`, 115 tables.
- The script aborts **before** writing to the NAS log, so `backup_log.txt` shows no failed attempts at all. The last research DB entry there is 2026-09-27.
- The watchdog did report this: `status_watchdog.txt` = FAIL at 2026-10-14 09:05, naming this cause.

**Cause:** the size guard was set when the DB was around 800 MB. It no longer fits a prose-only DB.

## 2. iba.db: killed by a closed console window, or not run while the PC was off

Task `IBA DB Backup to NAS` (18:10) history:

| Date | Result | NAS log |
|---|---|---|
| 10-08 | 0x0 | OK, verified |
| 10-09 | 0x0 | OK, verified |
| 10-10 | no run | none |
| 10-11 | **0xC000013A**, about 2 min | `START` only. No `OK` and no hash check. The file was left on the NAS. |
| 10-12 | no run | none |
| 10-13 | **0xC000013A** after 3 s | none |

- 0xC000013A is the exit code of a console process whose window was closed, or which received Ctrl+C. All four backup tasks use `LogonType = Interactive` and `Hidden = False`. Each one pops a visible `python.exe` or `powershell.exe` window, and closing that window kills the job. This is likely, but not proven.
- On 10-10 and 10-12 the task did not start at all. It has `StartWhenAvailable = False`, so a run missed while the PC is off or asleep is never made up. The research DB task has `True`.
- Run by hand today with `--dry-run`, the script works: integrity check ok, exit 0, 18 s.
- `iba_20261011T171049Z.db` is the full size, but it was **never hash-verified**. It also has `-shm`/`-wal` files dated 2026-10-12 14:50, so something opened it with SQLite on the NAS. Do not rely on it until it is checked.

## 3. The watchdog does not cover iba.db

`scripts/backup_watchdog.ps1` checks only `mirror` and `dbbackup`. The iba.db job writes `status_dbbackup_iba.txt`, which last says OK on 2026-10-09. Nothing reads it, so problem 2 went unalerted.

The config text is also stale. `backup.nas_db_backup_schedule` (CONFIG-REPORT) still says *"iba/app/db/iba.db has NO equivalent dedicated backup+alerting script -- see backup.iba_db_gap"*. That script now exists; only its watchdog coverage is missing.

## 4. Old backups deleted: not a fault

Researcher, chat 2026-10-14, verbatim: *"i am deleting old backups to save space. my concern is that backups are not up to date"*. The deleted files sit in the Synology recycle bin (`#recycle\bible_study_projects\db_backups`, 159 files), so the space is only freed once that bin is emptied.

The real concern is currency. The newest **verified** backups are:

| Database | Newest verified NAS backup | Age on 2026-10-14 |
|---|---|---|
| `bible_research.db` | 2026-09-27 | 17 days |
| `iba.db` | 2026-10-09 | 5 days |

## What fixing it needs (your decision)

1. **Size guard:** lower `MIN_PLAUSIBLE_BYTES`, or set it per source (for example, refuse when the source is far smaller than its own last backup). After that, take a backup of `bible_research.db` at once.
2. **iba.db task:**
   - Set `StartWhenAvailable = True`.
   - Run all four tasks hidden, through `pythonw`/`-WindowStyle Hidden` or "run whether user is logged on or not", so a closed window can't kill them.
   - Then take an iba.db backup at once.
3. **Watchdog:** add `dbbackup_iba` to its job list. Restate the stale config text in `backup.nas_db_backup_schedule` and `backup.iba_db_gap` through Config-Maintenance.
4. **Space:** the deleted backups only free NAS space once the recycle bin is emptied.
5. **`iba_20261011T171049Z.db`:** integrity-check it, or delete it as unverified.

## Actions taken (2026-10-14)

Researcher, chat 2026-10-14, verbatim: *"corrective action: make the size check each database, no need to run catchup backups, add iba.db to the watchdog. take fresh backups now and ensure that the scheduled backups and mirrors take place as planned."*

| Action | Change | Checked |
|---|---|---|
| Size check per database | `scripts/backup_db_to_nas.py`: `MIN_PLAUSIBLE_BYTES` is now a per-database table (bible_research 10 MB, iba 400 MB, any other 10 MB). | The research DB backup ran and was verified (36.0 MB). |
| No catch-up | Left as it was: `IBA DB Backup to NAS` keeps `StartWhenAvailable = False`. | — |
| Watchdog covers iba.db | `scripts/backup_watchdog.ps1`: `dbbackup_iba` added to its job list. | Live run: "all backups healthy". A copy run against a fake `dbbackup_iba` FAIL, with the alert call stubbed, tripped as expected. |
| Fresh backups | Run by hand: `bible_research_20261014T100556Z.db` and `iba_20261014T100611Z.db`, both `OK backup verified on NAS`. | NAS `backup_log.txt` |
| Scheduled runs as planned | The DB backup and mirror tasks now start through PowerShell with `-WindowStyle Hidden` (python runs inside that hidden console), so no window is left to close. The exit code is passed through. | Each task started through Task Scheduler: research DB 0x0 (`bible_research_20261014T100743Z`, verified), iba.db 0x0 (`iba_20261014T100757Z`, verified), mirror 0x0 (robocopy rc=3 OK). |

**Not done:**

- **Watchdog task:** `Set-ScheduledTask` on `BibleResearch Backup Watchdog` returned *Access is denied*, because the task needs admin rights. It still runs, but with a visible window. To change it, run in an **elevated** PowerShell:

  ```powershell
  $a = New-ScheduledTaskAction -Execute 'C:\Program Files\PowerShell\7\pwsh.exe' -Argument '-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File "C:\Bible_study_projects\scripts\backup_watchdog.ps1"' -WorkingDirectory 'C:\Bible_study_projects'
  Set-ScheduledTask -TaskName 'BibleResearch Backup Watchdog' -Action $a
  ```

- **Config text:** `backup.nas_db_backup_schedule` is restated through `Config-Maintenance.ps1 -Step Propose`, run `RUN-20261014_111226_864-CONFIGMAINT`. It is paused for researcher approval.
- **`iba_20261011T171049Z.db`:** still on the NAS and still unverified. It is now superseded by today's verified backups.

The tasks are first proven on their own schedule tonight: 18:00, 18:10, 18:30 and the watchdog at 19:00.
