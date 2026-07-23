<#
.SYNOPSIS
    Dump every DATA table in the live DB to CSV, one file per table — direct visibility into the
    actual data, no report narrative or sampling in the way. Excludes cfg_* tables — those are
    configmaint.report's job (CONFIG-REPORT.md + its own CSV pairing), not this tool's.

.DESCRIPTION
    Writes one CSV per table to table_export.output_dir (default iba/app/export/), every column,
    every row, verbatim. Now a registered dispatcher step (`table-export` / `table.export`, added
    2026-07-22 — it used to call tools.export_tables_csv directly, outside the dispatcher).

.PARAMETER Out    output folder (default: table_export.output_dir)
.PARAMETER Table  export only these tables (default: every data table)
.PARAMETER RunId  resume/re-tag a specific run.
.PARAMETER Trace  Print every config read (IBA_TRACE).

.EXAMPLE
    iba/app/ps/Export-Tables.ps1
.EXAMPLE
    iba/app/ps/Export-Tables.ps1 -Table candidate_seed,lemma_inventory
.EXAMPLE
    iba/app/ps/Export-Tables.ps1 -Out C:\Users\lerouxc\Desktop\iba-review
#>

[CmdletBinding()]
param(
    [string] $Out,
    [string[]] $Table,
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

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-TABLE-EXPORT" }

$paramArgs = @()
if ($Out)   { $paramArgs += @('--param', "Out=$Out") }
if ($Table) { $paramArgs += @('--param', "Table=$($Table -join ',')") }

Write-IbaRunHeader -WorkPackage 'table-export' -RunId $runId

$json = python -m iba.app.run table-export --step table.export --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'table.export' -Path $res.path -Message $res.message -Code $code

exit $code
