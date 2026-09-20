<#
.SYNOPSIS
    The soft-delete purge audit -- app-wide, both databases (escalation #1766). Standalone,
    single-step work package, like Spine-Check.ps1/Lexical-Readiness.ps1.

.DESCRIPTION
    Read-only. For every table with a registered soft-delete column, counts soft-deleted rows and
    flags any table over purge.unsafe_check_min_soft_deleted as UNSAFE if a live row elsewhere
    still references one of its soft-deleted PKs. Always persists a report
    (purge.audit_report_path). Removes nothing -- there is no delete/purge capability in this
    script; that is a separate, not-yet-designed follow-up (escalation #1766 v3/v5: dependency-
    aware purge order and a retention window are still open questions).

.PARAMETER RunId   resume a specific pending check (reuse the run_id from its first call).
.PARAMETER Trace   Print every config read (IBA_TRACE).

.EXAMPLE
    .\Purge-SoftDeletes.ps1
.EXAMPLE
    .\Purge-SoftDeletes.ps1 -RunId RUN-20260919_...-PURGE-AUDIT
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

$stepId = 'purge.audit'
$runId  = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-PURGE-AUDIT" }

Write-IbaRunHeader -WorkPackage 'purge-audit' -Step $stepId -RunId $runId

$json = python -m iba.app.run purge-audit --step $stepId --run-id $runId
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code

if ($code -eq 2) {
    Write-IbaPaused -WorkPackage 'purge-audit' -RunId $runId -Message $res.message
}

exit $code
