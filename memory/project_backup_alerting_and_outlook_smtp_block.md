---
name: project_backup_alerting_and_outlook_smtp_block
description: NAS backups now have failure alerting (status files + watchdog + email); Outlook basic-auth SMTP is BLOCKED — use Gmail/relay
metadata:
  type: project
---

2026-06-18: the NAS backups had been failing SILENTLY since 2026-06-15 (NAS power failure; the 18:00 DB backup + 18:30 full mirror tasks fired but the copy target was gone). Root defect = no failure alerting. Fixed by adding:
- `scripts/notify_backup_alert.ps1` — central sink: writes a LOCAL status file `C:\Users\lerouxc\nas_mirror_logs\status_<job>.txt` (`OK|ISO|detail`) always; on FAIL also Event Log + Desktop `BACKUP_ALERT.txt` + toast + e-mail (reads `SMTP_*`/`ALERT_EMAIL_*` from `.env`, transport-agnostic).
- `mirror_to_nas.ps1` + `backup_db_to_nas.py` wired to it (the Python job now writes a LOCAL status — its normal log lives ON the NAS, invisible when the NAS is down).
- `scripts/backup_watchdog.ps1` + `install_backup_watchdog_task.ps1` — staleness backstop (alerts if either job's last success >26h or last status FAIL); task daily 19:00 + at logon; **install needs an elevated shell** (Register-ScheduledTask = Access denied non-elevated).

**E-mail transport (RESOLVED 2026-06-18):** Outlook was abandoned — Microsoft disabled basic-auth SMTP for personal Outlook (`535 5.7.139 ... basic authentication is disabled`), a policy block no app password fixes. Now sends via a **Gmail app password** (`smtp.gmail.com:587`, creds in gitignored `.env`); test send to leroux@cilliers.co.uk verified. Two .NET `SmtpClient` gotchas fixed in the helper: set `UseDefaultCredentials=$false` BEFORE `Credentials` (else AUTH is never sent → `5.7.0 Authentication Required`), and strip whitespace from the app password (Gmail displays it as 4 space-separated groups; must be exactly 16 chars).

**PS-engine/encoding gotcha (found+fixed 2026-06-21):** the **mirror task runs `powershell.exe` (Windows PowerShell 5.1)**; the watchdog runs `pwsh.exe` (PS7); the DB backup writes its status from Python. 5.1 reads BOM-less `.ps1` as ANSI, so a UTF-8 **em-dash (`—`, U+2014)** in `notify_backup_alert.ps1` became mojibake → whole script failed to PARSE under 5.1 → the mirror's `& notify` silently failed (ErrorActionPreference=Continue) → `status_mirror.txt` was never written, frozen for days, watchdog false-tripped daily — yet the mirror itself copied fine and the task showed 0x0. Fix: made `notify_backup_alert.ps1` + `backup_watchdog.ps1` **pure ASCII** (em-dash → `-`). **Rule: any `.ps1` that can run under 5.1 must be ASCII or UTF-8-with-BOM** — non-ASCII without a BOM breaks parsing under 5.1 and the failure is invisible. Optional hardening (not yet done): switch the mirror task to `pwsh.exe`. Check: `outputs/markdown/wa-backup-health-check-20260621.md`.

**How to apply:** when checking backups, read the local `status_*.txt` files / `nas_mirror.log` — don't trust Task Scheduler "green" (it ran the script; the copy may have failed rc=16, OR the status write silently failed — verify the status file mtime is fresh, not just present). Two backup tracks remain: git (curated source, see [[reference_operational_governance_git_backup_manifest]]) + NAS full mirror (everything, incl. gitignored VE extracts). Incidents: `outputs/markdown/wa-nas-backup-failure-20260618.md`, `outputs/markdown/wa-backup-health-check-20260621.md`.
