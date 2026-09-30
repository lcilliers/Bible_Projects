# Backup Alerting — Design as Built (v1, 2026-06-18)

**File:** wa-backup-alerting-plan-v1-20260618.md · **Prefix:** wa · **Type:** Operational design / as-built (markdown)
**Date:** 2026-06-18 · **Trigger:** silent NAS backup failure (`wa-nas-backup-failure-20260618.md`)

---

## Goal
Never again let a backup fail silently. Catch **both** failure modes: (A) a job runs and fails, and
(B) a job does not run at all (task disabled, PC off, crash before its own alert).

## Components (all under `scripts/`)

| File | Role |
|---|---|
| `notify_backup_alert.ps1` | **Central alert sink.** Always writes a local status file `C:\Users\lerouxc\nas_mirror_logs\status_<job>.txt` (`OK\|ISO\|detail`). On FAIL also: Windows Event Log (best-effort), Desktop `BACKUP_ALERT.txt` sentinel, toast (best-effort), and **e-mail** (reads `SMTP_*`/`ALERT_EMAIL_*` from `.env`). Transport-agnostic: any basic-auth SMTP works by editing `.env` only. |
| `mirror_to_nas.ps1` *(modified)* | Calls the sink with OK/FAIL after the robocopy summary (FAIL when project or memory rc ≥ 8). |
| `backup_db_to_nas.py` *(modified)* | Writes a **local** status file + calls the sink on every exit (its normal log lives on the NAS, so a NAS-down failure previously left no local trace). rc→detail mapped. Skips on `--dry-run`. |
| `backup_watchdog.ps1` | **Mode-B backstop.** Reads the two status files; alerts if either job's last success is >26 h old, or last status was FAIL. |
| `install_backup_watchdog_task.ps1` | Registers the `BibleResearch Backup Watchdog` task (daily 19:00 + at logon). **Run elevated** (task creation needs admin). |

## Alert channels (in order of reliability)
1. **E-mail** — the only off-machine channel; survives the PC/NAS being down. *(pending working transport — see below.)*
2. **Desktop sentinel** `BACKUP_ALERT.txt` — visible at next logon.
3. **Local status files** — machine-readable; what the watchdog reads.
4. **Windows Event Log** (Application / source `BibleResearchBackup`) — best-effort (source creation needs one elevated run).
5. **Toast** — best-effort; only shows in an interactive session.

## Status — done vs pending
**Done:** all five scripts written + syntax-checked; both backup jobs wired to the sink; local-status mechanism verified via a test alert; `.env` extended with `SMTP_*` / `ALERT_EMAIL_*`.

**E-mail transport — RESOLVED 2026-06-18.** Outlook abandoned (Microsoft disabled basic-auth SMTP, `535 5.7.139`). Now sends via a **Gmail app password** (`smtp.gmail.com:587`, creds in `.env`); test send to leroux@cilliers.co.uk delivered + confirmed received. Helper fixes: `UseDefaultCredentials=$false` set before `Credentials` (else AUTH never sent → `5.7.0`); app-password whitespace stripped (Gmail shows it as 4×4 groups; must be 16 chars).

**Pending:**
1. **Install the watchdog task** (elevated): `pwsh -File scripts/install_backup_watchdog_task.ps1` — could not be registered from the non-elevated session ("Access is denied").
2. **Close the backup gap** once the NAS is back (run both jobs manually; confirm green).
3. *(optional)* Create the `BibleResearchBackup` Event Log source once from an elevated shell so that channel works (harmless if skipped).

## Notes / limitations
- Watchdog runs as the interactive user (so toast/sentinel show); it fires at logon + daily 19:00. It does **not** run when logged off — but the in-job e-mail alerts (fired during the unattended 18:00/18:30 runs) cover that window once e-mail works. Switch the task to a run-when-logged-off principal later if desired.
- Event-log source `BibleResearchBackup` needs to be created once from an elevated shell, else that channel is skipped (harmless).
