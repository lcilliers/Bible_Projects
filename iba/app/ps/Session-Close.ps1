<#
.SYNOPSIS
    Session-close checks — escalation update coverage, governance/config/doc drift signal, and
    BUILD.md tracking-id coverage for the current Claude Code session (escalation #1875, researcher
    design approval 2026-09-24). Standalone, single-step work package, like Spine-Check.ps1.

.DESCRIPTION
    Read-only detection. Always persists a report (session_close.report_path). Never blocks or
    escalates for a `gaps-found` condition — this step's own findings route to `report-continue`
    (exit 0), per the researcher's explicit instruction that remediation must not create an
    additional approval cycle. Remediation itself is a separate step: read the report this prints,
    then follow `.claude/commands/session-close.md` to fix any gap found.

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

exit $code
