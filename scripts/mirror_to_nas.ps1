<#
mirror_to_nas.ps1 - daily full MIRROR of the project to the NAS.

Mirrors two trees with robocopy /MIR (dest is made to match source exactly):
  1. the whole project folder  C:\Bible_study_projects        -> NAS\mirror
  2. the live Claude memory     ...\.claude\...\<project>      -> NAS\claude-backup

/MIR deletes files in the destination that no longer exist in the source (that is the point of a mirror).
Junk dirs/files are excluded. robocopy exit codes 0-7 = success, 8+ = failure.
Log (summaries only) is written OUTSIDE the repo so it does not churn the mirror.
#>
$ErrorActionPreference = 'Continue'

$src    = 'C:\Bible_study_projects'
$dst    = '\\LSUK-SYNRACK\HomeMedia\bible_study_projects\mirror'
$memSrc = 'C:\Users\lerouxc\.claude\projects\c--Bible-study-projects'
$memDst = '\\LSUK-SYNRACK\HomeMedia\bible_study_projects\claude-backup'

$logDir = 'C:\Users\lerouxc\nas_mirror_logs'
$log    = Join-Path $logDir 'nas_mirror.log'
if (-not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir -Force | Out-Null }
foreach ($d in @($dst, $memDst)) { if (-not (Test-Path $d)) { New-Item -ItemType Directory -Path $d -Force | Out-Null } }

$exclDirs  = @('__pycache__', '.pytest_cache', '.mypy_cache', '.ruff_cache', '.venv', 'venv', 'env', 'node_modules')
$exclFiles = @('*.pyc', '*.pyo', '*.tmp', '.__writetest.tmp')

"==== mirror run $(Get-Date -Format o) ====" | Out-File $log -Append -Encoding utf8

# 1) project folder -> NAS
robocopy $src $dst /MIR /R:2 /W:5 /NFL /NDL /NP /XD $exclDirs /XF $exclFiles /LOG+:$log | Out-Null
$rc1 = $LASTEXITCODE

# 2) live Claude memory -> NAS
robocopy $memSrc $memDst /MIR /R:2 /W:5 /NFL /NDL /NP /XD $exclDirs /XF $exclFiles /LOG+:$log | Out-Null
$rc2 = $LASTEXITCODE

$ok1 = $rc1 -lt 8
$ok2 = $rc2 -lt 8
$summary = "{0}  project rc={1} ({2})  memory rc={3} ({4})" -f (Get-Date -Format o), $rc1, $(if($ok1){'OK'}else{'FAIL'}), $rc2, $(if($ok2){'OK'}else{'FAIL'})
$summary | Out-File $log -Append -Encoding utf8
Write-Output $summary

# raise/clear the alert (local status file always; e-mail + toast + event log on failure)
$notify = Join-Path $PSScriptRoot 'notify_backup_alert.ps1'
if ($ok1 -and $ok2) {
    & $notify -Job mirror -Status OK
    exit 0
} else {
    & $notify -Job mirror -Status FAIL -Detail "robocopy failed: project rc=$rc1, memory rc=$rc2 (>=8 = serious error, e.g. NAS unreachable)"
    exit 1
}
