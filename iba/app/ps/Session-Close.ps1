<#
.SYNOPSIS
    Session-close detection (escalation #1875; rebuilt #2173, SC1-SC14): session and window, spine
    (FATAL first), researcher's words recorded, open items in the register, analysis integrity,
    rule compliance evidence, session log, decisions' targets, BUILD.md coverage, publish flags.

.DESCRIPTION
    Read-only detection; always persists a report (session_close.report_path). A finding is
    cleared only by fixing it or by a disposition in the session compliance file that the check
    accepts. While any finding is open this script exits 3 and the commit is BLOCKED (SC13): the
    findings route to report-continue (no escalation, no approval cycle -- the researcher's
    2026-09-24 instruction), and the block is this exit code. Remediation follows
    `.claude/commands/session-close.md`.

.PARAMETER RunId   resume a specific run_id (rarely needed — this step never pauses).
.PARAMETER Trace   Print every config read (IBA_TRACE).

.EXAMPLE
    .\Session-Close.ps1
#>

[CmdletBinding()]
param(
    [string] $RunId,
    [switch] $Trace
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'
if ($Trace) { $env:IBA_TRACE = '1' }

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot
. $PSScriptRoot\_lib\Notify.ps1

$ready = python -c "from iba.app.init import _config_loaded, _data_tables_exist; from iba.app.lib.cfg import Cfg; print('1' if (_config_loaded() and _data_tables_exist(Cfg())) else '0')" 2>$null
if ($ready -ne '1') {
    Write-IbaNotInitialised
    exit 1
}

$stepId = 'session.close'
$runId  = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-SESSION-CLOSE" }

Write-IbaRunHeader -WorkPackage 'session-close' -Step $stepId -RunId $runId

$json = python -m iba.app.run session-close --step $stepId --run-id $runId
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code

if ($code -eq 2) {
    Write-IbaPaused -WorkPackage 'session-close' -RunId $runId -Message $res.message
}
if ($res.counts -and ($res.counts.PSObject.Properties.Name -contains 'open_findings')) {
    $pub = @()
    if ($res.counts.narrative_copy -eq 1) { $pub += 'narrative copy NEEDED' } else { $pub += 'narrative copy not needed' }
    if ($res.counts.thread_export -eq 1) { $pub += 'threads export NEEDED' } else { $pub += 'threads export not needed' }
    Write-Host "  publish (SC12): $($pub -join '; ')"
    if ($res.counts.open_findings -gt 0) {
        Write-Host "  COMMIT BLOCKED: $($res.counts.open_findings) open finding(s) ($($res.counts.fatal) FATAL). Fix each, or disposition it in the compliance file, then re-run." -ForegroundColor Red
        exit 3
    }
}

exit $code
