<#
.SYNOPSIS
    The IBA app's own data-schema snapshot — every data table, columns, types, PK/FK, indexes,
    row counts. Read-only. Introspects the live DB directly, no CSV pairing (this report already
    is the schema).

.DESCRIPTION
    Writes report.schema_overview_path (default iba/app/reports/schema-overview.md). First-cut
    content per PLAN-reports-config-governance-v1-20260722.md §3.4 — expected to be expanded once
    built.

.PARAMETER RunId  resume/re-tag a specific run.
.PARAMETER Trace  Print every config read (IBA_TRACE).

.EXAMPLE
    .\SchemaOverview-Report.ps1
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

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-SCHEMA-OVERVIEW" }

Write-IbaRunHeader -WorkPackage 'schema-overview-report' -RunId $runId

$json = python -m iba.app.run schema-overview-report --step report.schema_overview --run-id $runId
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'report.schema_overview' -Path $res.path -Message $res.message -Code $code

exit $code
