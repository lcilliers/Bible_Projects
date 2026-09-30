# Backup health check — 2026-06-21

**Run:** 2026-06-21 ~18:40 BST (manual verification at researcher request) · **Verdict:** all three layers protect the data; one **monitoring defect** found and **fixed**.

## Summary verdict

| Layer | Schedule | Data safe? | Health signal | Notes |
|---|---|---|---|---|
| **DB backup → NAS** | 18:00 daily | ✅ Yes | ✅ OK (0.5h) | Today's snapshot `bible_research_20260621T170010Z.db` (487.2 MB) integrity-verified on NAS; daily series 18–21 Jun present; GFS retention working |
| **Full mirror → NAS** | 18:30 daily | ✅ Yes | ❌→✅ **was broken, now fixed** | Today's M09 essay (.md/.docx/.pdf) confirmed on NAS mirror (copied 18:11–18:12); the *job runs*, but its **status file wasn't updating** (see defect below) |
| **Memory mirror → NAS** | 18:30 (same job) | ✅ Yes | ✅ OK | `claude-backup\`; robocopy memory rc=1 (OK) today |
| **Watchdog** | 19:00 daily | — | ❌→✅ **fixed** | Was tripping daily on the stale mirror signal (false alarm); now reports "all backups healthy" |
| **Git** | on commit | ✅ (code/patches/memory) | — | Separate failure domain; covers source + memory mirror |

## The defect (found + fixed)

**Symptom:** `status_mirror.txt` was frozen at **18 Jun 17:27** despite the mirror running successfully every evening since. The watchdog therefore tripped every day ("NAS full mirror: job may not be running") — a **false alarm**, because the mirror *was* copying files correctly.

**Root cause:** an **encoding/engine mismatch**.
- The **mirror task runs `powershell.exe` (Windows PowerShell 5.1)**; the watchdog runs `pwsh.exe` (PowerShell 7); the DB backup writes its status directly from Python.
- `notify_backup_alert.ps1` (which writes the mirror's status file) was saved **UTF-8 without a BOM** and contained **em-dashes (`—`, U+2014)**.
- Windows PowerShell **5.1 reads BOM-less `.ps1` as ANSI**, so the em-dash bytes became mojibake (`â€"`) → **the whole script failed to parse** → `notify` never ran → status file never written. The mirror script swallowed the error (`$ErrorActionPreference='Continue'`) and still exited 0, so the scheduled task reported success.
- PowerShell 7 reads UTF-8 by default, so the watchdog's invocation parsed fine — which is why only the *mirror's* status went stale, and the last successful update (18 Jun 17:27) was a *manual* pwsh run.

**Why it mattered:** the data was safe, but a watchdog that cries wolf daily trains the eye to ignore it — so a *real* mirror failure would have been missed.

**Fix applied:** replaced all 11 em-dashes in `notify_backup_alert.ps1` (and 2 in `backup_watchdog.ps1`, defence-in-depth) with ASCII hyphens, making both scripts **pure ASCII** — parseable on any engine/encoding. Verified:
1. `notify_backup_alert.ps1` parses clean under 5.1.
2. Invoking it under 5.1 now updates `status_mirror.txt`.
3. Watchdog re-run → **"all backups healthy"**; `status_watchdog` flipped FAIL → OK.

## Other observations

- **16–17 Jun mirror failures (rc=16) were real** (NAS unreachable those evenings) and **self-recovered on 18 Jun**. The alert channels fired as designed; DB backup + git covered those two days.
- **DB backup is robust by construction**: refuses to run (and prunes nothing) if the source DB is missing / implausibly small / fails integrity_check; snapshots via SQLite online-backup; hash-verifies the NAS copy.

## Recommended (optional) hardening — not yet applied

- **Align the mirror task to `pwsh.exe`** (matching the watchdog) so all jobs run on one engine and future non-ASCII can't silently break parsing under 5.1. The ASCII fix above already resolves the live issue; this is belt-and-braces.
- **Commit the two script fixes** (`notify_backup_alert.ps1`, `backup_watchdog.ps1`).
