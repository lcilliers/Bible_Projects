<#
.SYNOPSIS
    Generate the run/escalation/validation_result log-retention & run-health report. Read-only —
    no rows are pruned, archived, or deleted; this is visibility so a retention POLICY can be
    decided with real numbers.

.DESCRIPTION
    Writes retention.report_path (default iba/app/reports/log-retention.md): row counts + age for
    run/escalation/validation_result, chained-package runs stuck mid-sequence (archival candidates,
    not relabelled), every open escalation, and recent failed runs. Now a registered dispatcher
    step (`log-retention` / `retention.report`, added 2026-07-22 — it used to call
    tools.log_retention directly, outside the dispatcher, with no run_id/audit trail).

.PARAMETER RunId  resume/re-tag a specific run (reuse the run_id from a prior call).
.PARAMETER Trace  Print every config read (IBA_TRACE).

.EXAMPLE
    .\Log-Retention.ps1
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

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-LOG-RETENTION" }

Write-IbaRunHeader -WorkPackage 'log-retention' -RunId $runId

$json = python -m iba.app.run log-retention --step retention.report --run-id $runId
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'retention.report' -Path $res.path -Message $res.message -Code $code

exit $code
