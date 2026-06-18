<#
install_backup_watchdog_task.ps1 — register the 'BibleResearch Backup Watchdog' scheduled task.

MUST be run from an ELEVATED PowerShell (Run as administrator) — creating a Task Scheduler
task in the root folder requires admin rights, same as the existing backup tasks.

  Right-click PowerShell 7 → Run as administrator, then:
      pwsh -File C:\Bible_study_projects\scripts\install_backup_watchdog_task.ps1

Triggers: daily 19:00 + at logon. Runs as the current interactive user (so desktop toast /
sentinel show); e-mail + Event Log + status files work regardless. Re-run to update.
#>
$ErrorActionPreference = 'Stop'

$pwsh = (Get-Command pwsh -ErrorAction SilentlyContinue).Source
if (-not $pwsh) { $pwsh = (Get-Command powershell).Source }
$script = 'C:\Bible_study_projects\scripts\backup_watchdog.ps1'
$name   = 'BibleResearch Backup Watchdog'

$action    = New-ScheduledTaskAction -Execute $pwsh -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$script`""
$tDaily    = New-ScheduledTaskTrigger -Daily -At 7:00PM
$tLogon    = New-ScheduledTaskTrigger -AtLogOn
$principal = New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\$env:USERNAME" -LogonType Interactive -RunLevel Limited
$settings  = New-ScheduledTaskSettingsSet -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries

Unregister-ScheduledTask -TaskName $name -Confirm:$false -ErrorAction SilentlyContinue
Register-ScheduledTask -TaskName $name -Action $action -Trigger @($tDaily, $tLogon) `
    -Principal $principal -Settings $settings `
    -Description 'Alerts if the NAS mirror or DB backup has not succeeded within 26h (catches not-run / crashed / NAS-down).' | Out-Null

$i = Get-ScheduledTask -TaskName $name | Get-ScheduledTaskInfo
Write-Host "OK — registered '$name'. Next run: $($i.NextRunTime)" -ForegroundColor Green
Write-Host "Test it now with:  pwsh -File $script" -ForegroundColor Cyan
