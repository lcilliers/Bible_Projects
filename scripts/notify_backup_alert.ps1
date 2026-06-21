<#
notify_backup_alert.ps1 - central alert sink for the NAS backup jobs + watchdog.

Called by mirror_to_nas.ps1, backup_db_to_nas.py and backup_watchdog.ps1.
Every call records a LOCAL status file (so failures are visible even when the NAS -
where the DB-backup log lives - is unreachable). On FAIL it also raises a Windows
Event Log error, writes a Desktop sentinel, fires a best-effort toast, and e-mails
the address in .env (the only off-machine channel; works while the NAS is down).

Usage:
  pwsh scripts/notify_backup_alert.ps1 -Job mirror   -Status OK
  pwsh scripts/notify_backup_alert.ps1 -Job dbbackup -Status FAIL -Detail "NAS unreachable (rc=5)"

Status files: C:\Users\lerouxc\nas_mirror_logs\status_<job>.txt  =  "<STATUS>|<ISO-8601>|<detail>"
#>
param(
    [Parameter(Mandatory)][ValidateSet('mirror','dbbackup','watchdog')][string]$Job,
    [Parameter(Mandatory)][ValidateSet('OK','FAIL')][string]$Status,
    [string]$Detail = ''
)
$ErrorActionPreference = 'Continue'

$statusDir = 'C:\Users\lerouxc\nas_mirror_logs'
if (-not (Test-Path $statusDir)) { New-Item -ItemType Directory -Path $statusDir -Force | Out-Null }
$now = (Get-Date).ToString('o')

# 1) LOCAL status file - the watchdog and any human read this. Always written.
"$Status|$now|$Detail" | Out-File (Join-Path $statusDir "status_$Job.txt") -Encoding utf8 -Force

if ($Status -eq 'OK') { Write-Output "[$Job] OK $now"; return }

# ---- failure channels ------------------------------------------------------
$subject = "BACKUP FAILURE: $Job - $($now.Substring(0,19))"
$body    = "The '$Job' NAS backup job reported FAILURE.`n`nWhen: $now`nDetail: $Detail`nHost: $env:COMPUTERNAME`n`nThis is an automated alert from the Bible_study_projects backup system."

# 2) Windows Event Log (best-effort; creating the source needs one elevated run - try/catch)
try {
    if (-not [System.Diagnostics.EventLog]::SourceExists('BibleResearchBackup')) {
        New-EventLog -LogName Application -Source 'BibleResearchBackup' -ErrorAction Stop
    }
    Write-EventLog -LogName Application -Source 'BibleResearchBackup' -EntryType Error -EventId 1001 -Message $body -ErrorAction Stop
} catch { Write-Output "  (event-log skipped: $($_.Exception.Message))" }

# 3) Desktop sentinel - visible at next logon
try {
    $desktop = [Environment]::GetFolderPath('Desktop')
    "$subject`n`n$body" | Out-File (Join-Path $desktop 'BACKUP_ALERT.txt') -Encoding utf8 -Force
} catch { }

# 4) Toast (best-effort; silent if no interactive session / module)
try {
    $null = [Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime]
    $xml = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02)
    $t = $xml.GetElementsByTagName('text'); $t[0].AppendChild($xml.CreateTextNode('Bible backup FAILED')) | Out-Null
    $t[1].AppendChild($xml.CreateTextNode("$Job - $Detail")) | Out-Null
    [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('BibleResearchBackup').Show(
        [Windows.UI.Notifications.ToastNotification]::new($xml))
} catch { }

# 5) E-mail (the off-machine channel) - reads SMTP_* from .env
try {
    $envFile = Join-Path $PSScriptRoot '..\.env'
    if (Test-Path $envFile) {
        $cfg = @{}
        Get-Content $envFile | ForEach-Object {
            if ($_ -match '^\s*([A-Z_]+)\s*=\s*(.*)$') { $cfg[$Matches[1]] = $Matches[2].Trim() }
        }
        if ($cfg['ALERT_EMAIL_ENABLED'] -eq 'true' -and $cfg['SMTP_PASSWORD']) {
            $msg = New-Object System.Net.Mail.MailMessage
            $msg.From = $cfg['ALERT_EMAIL_FROM']
            $cfg['ALERT_EMAIL_TO'].Split(',') | ForEach-Object { $msg.To.Add($_.Trim()) }
            $msg.Subject = $subject
            $msg.Body = $body
            $smtp = New-Object System.Net.Mail.SmtpClient($cfg['SMTP_HOST'], [int]$cfg['SMTP_PORT'])
            $smtp.EnableSsl = $true            # STARTTLS on 587
            $smtp.DeliveryMethod = [System.Net.Mail.SmtpDeliveryMethod]::Network
            $smtp.UseDefaultCredentials = $false   # MUST precede Credentials, else .NET drops them (AUTH never sent)
            $pw = ($cfg['SMTP_PASSWORD'] -replace '\s', '')   # Gmail shows app pwd as 4 space-separated groups; strip spaces
            $smtp.Credentials = New-Object System.Net.NetworkCredential($cfg['SMTP_USER'], $pw)
            $smtp.Send($msg)
            Write-Output "  alert e-mail sent to $($cfg['ALERT_EMAIL_TO'])"
        } else { Write-Output "  (e-mail disabled or SMTP_PASSWORD blank - local alerts only)" }
    }
} catch { Write-Output "  (e-mail send FAILED: $($_.Exception.Message))" }

Write-Output "[$Job] FAIL alert raised $now - $Detail"
