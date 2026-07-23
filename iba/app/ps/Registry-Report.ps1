<#
.SYNOPSIS
    Evaluate/review the registry (word_registry): a summary, its join to strong (via word_strong),
    and a sense report grouping registry words by the gloss/broad meaning their strong carries.
    Read-only. Built 2026-07-23, escalation #272 -- the registry had no evaluation report.

.DESCRIPTION
    Writes report.registry_path (default iba/app/reports/registry.md) + a CSV pairing (word_registry
    joined to word_strong/strong/strong_sense) to report.registry_path's export/ subfolder.

.PARAMETER RunId  resume/re-tag a specific run.
.PARAMETER Trace  Print every config read (IBA_TRACE).

.EXAMPLE
    .\Registry-Report.ps1
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

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-REGISTRY-REPORT" }

Write-IbaRunHeader -WorkPackage 'registry-report' -RunId $runId

$json = python -m iba.app.run registry-report --step report.registry --run-id $runId
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'report.registry' -Path $res.path -Message $res.message -Code $code

exit $code
