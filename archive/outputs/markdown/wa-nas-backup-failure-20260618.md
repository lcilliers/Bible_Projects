# NAS Backup Failure — Incident Record (2026-06-18)

**File:** wa-nas-backup-failure-20260618.md · **Prefix:** wa · **Type:** Operational incident record (markdown)
**Date raised:** 2026-06-18 · **Status:** OPEN (NAS rebooting after power failure; alerting being added)

---

## 1. Summary
The daily NAS backups (full mirror 18:30 + DB backup 18:00) have been **failing silently** since the NAS
went offline on a **power failure**. The scheduled tasks kept firing on time, but the copy target was gone,
so they failed with no notification. Discovered 2026-06-18 while checking backup evidence for the M02 work.

## 2. Evidence (three independent sources, gathered 2026-06-18 ~16:5x BST)
- **Mirror run-log** (`C:\Users\lerouxc\nas_mirror_logs\nas_mirror.log`): daily runs OK through **2026-06-15 18:31** (rc=3 OK = last good mirror). **2026-06-14** run started but wrote no completion summary (interrupted). **2026-06-16** and **2026-06-17**: `project rc=16 / memory rc=16` = robocopy serious error (copied nothing).
- **NAS reachability (now):** host `LSUK-SYNRACK` does not respond to ping; `\\LSUK-SYNRACK\HomeMedia` and sub-folders `mirror`, `claude-backup`, `db_backups` all unreachable.
- **DB-backup task** (`BibleResearch DB Backup to NAS`): last run 2026-06-17 18:00, result **0x5** (the script's "NAS target unreachable" exit code).

## 3. Exposure
- **Last offsite copy of anything not-in-git: 2026-06-15** (~3 days).
- **Protected throughout:** all git-tracked source (code, `.md`, patches, schema, by-characteristic JSON) — GitHub is offsite and unaffected.
- **Not offsite right now:** the live DB, this week's DB work, and gitignored VE extracts (incl. the 2026-06-18 M02 `wa-ve-lexical-extract-M02-*.json` files). They exist only on the C: drive.
- **Partial mitigation that held:** local DB snapshots in `backups/` are current (newest 2026-06-18 10:08 + daily all week) — but same C: drive, so they cover corruption, **not** drive loss.
- Context that raises the stakes: this project already lost its DB once (2026-06-03) — the NAS mirror exists precisely to prevent a repeat, and it was not running.

## 4. Root cause
1. **Primary:** NAS power failure took the share offline; robocopy/script then fail (expected) — but
2. **The real defect:** there was **no failure alerting**. Task Scheduler showed the tasks "running"; the scripts' non-zero exit codes were not surfaced anywhere a human would see. A backup with no alerting is not a trustworthy backup. The DB-backup script also wrote its only log *to the NAS*, so when the NAS was down there was no local trace at all.

## 5. Resolution
- **Alerting added** (see `wa-backup-alerting-plan-v1-20260618.md`): on-failure alerts inside both jobs (local status file + Event Log + Desktop sentinel + toast + e-mail) and an independent **staleness watchdog** task.
- **Pending — e-mail transport:** the chosen sender (`lerouxcilliers@outlook.com`) is blocked — Microsoft has disabled basic-auth SMTP for personal Outlook (error `535 5.7.139 ... basic authentication is disabled`). Email will work once `.env` points at a basic-auth-capable SMTP (Gmail app password, or a relay such as Brevo/SendGrid).
- **Pending — close the gap:** once the NAS is back, run both jobs manually and confirm green.
- **Pending — install watchdog task:** run `scripts/install_backup_watchdog_task.ps1` from an elevated PowerShell.

## 6. Action checklist
- [ ] NAS powered back on and reachable (`Test-Path \\LSUK-SYNRACK\HomeMedia`)
- [ ] Point `.env` SMTP_* at a working transport; re-test alert e-mail delivers
- [ ] Install the watchdog task (elevated): `pwsh -File scripts/install_backup_watchdog_task.ps1`
- [ ] Run `python scripts/backup_db_to_nas.py` → expect "OK backup verified on NAS"
- [ ] Run `pwsh -File scripts/mirror_to_nas.ps1` → expect `project rc=… (OK) memory rc=… (OK)`
- [ ] Confirm `status_mirror.txt` / `status_dbbackup.txt` show `OK` and watchdog reports healthy
