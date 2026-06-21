<#
backup_watchdog.ps1 - independent staleness check for the NAS backup jobs.

The on-failure alerts inside mirror_to_nas.ps1 / backup_db_to_nas.py only fire when those
scripts RUN. This watchdog catches the cases they can't: the task was disabled, the PC was
off at backup time, or the script crashed before its alert. It reads the LOCAL status files
each job writes and raises an alert if either job has not SUCCEEDED within the threshold,
or its last recorded status was FAIL.

Run by the 'BibleResearch Backup Watchdog' scheduled task (daily 19:00 + at logon).
#>
$ErrorActionPreference = 'Continue'
$statusDir = 'C:\Users\lerouxc\nas_mirror_logs'
$notify    = Join-Path $PSScriptRoot 'notify_backup_alert.ps1'
$maxAgeHrs = 26   # one daily run (+margin) must have succeeded within this window

$jobs = @(
    @{ Job = 'mirror';   Label = 'NAS full mirror (18:30)' },
    @{ Job = 'dbbackup'; Label = 'NAS DB backup (18:00)'  }
)

$problems = @()
foreach ($j in $jobs) {
    $f = Join-Path $statusDir "status_$($j.Job).txt"
    if (-not (Test-Path $f)) {
        $problems += "$($j.Label): no status file yet (job has not reported a result)"
        continue
    }
    $parts = (Get-Content $f -Raw).Trim().Split('|')
    $status = $parts[0]
    $ts = $null
    try { $ts = [datetimeoffset]::Parse($parts[1]) } catch { }
    $ageHrs = if ($ts) { [math]::Round(((Get-Date) - $ts.LocalDateTime).TotalHours, 1) } else { 9999 }
    if ($status -ne 'OK') {
        $problems += "$($j.Label): last status FAIL ($($parts[2])) at $($parts[1])"
    } elseif ($ageHrs -gt $maxAgeHrs) {
        $problems += "$($j.Label): last SUCCESS was $ageHrs h ago (>$maxAgeHrs h) - job may not be running"
    }
}

if ($problems.Count -gt 0) {
    & $notify -Job watchdog -Status FAIL -Detail ("Backup watchdog tripped:`n - " + ($problems -join "`n - "))
    Write-Output "WATCHDOG: ALERT raised ($($problems.Count) problem(s))"
} else {
    & $notify -Job watchdog -Status OK
    Write-Output "WATCHDOG: all backups healthy"
}
