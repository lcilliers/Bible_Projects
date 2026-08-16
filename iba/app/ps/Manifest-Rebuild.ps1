<#
.SYNOPSIS
    Rebuild the project-wide file manifest (filename/path metadata for every file in the project
    tree, incl. archives). Full rescan — replaces the file_manifest table's contents.

.DESCRIPTION
    Writes manifest.report_path (default iba/app/reports/file-manifest.md): counts by category and
    currency (active/archived/cross-reference/historical/backup/other). Metadata only — no file
    content is read here; see Manifest-Search.ps1 for querying the result, and (round 2)
    content-index tooling for searching file content itself.

.PARAMETER RunId  resume/re-tag a specific run (reuse the run_id from a prior call).
.PARAMETER Trace  Print every config read (IBA_TRACE).

.EXAMPLE
    .\Manifest-Rebuild.ps1
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

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-MANIFEST-REBUILD" }

Write-IbaRunHeader -WorkPackage 'file-manifest-rebuild' -RunId $runId

$json = python -m iba.app.run file-manifest-rebuild --step manifest.rebuild --run-id $runId
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'manifest.rebuild' -Path $res.path -Message $res.message -Code $code

exit $code
