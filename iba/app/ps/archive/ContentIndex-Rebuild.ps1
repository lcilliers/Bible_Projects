<#
.SYNOPSIS
    Rebuild the file-content concordance index — every .md file in file_manifest, scanned for
    Strong's numbers / glosses / words. Full rescan — replaces content_index/content_index_scan.

.DESCRIPTION
    Round 2 of the manifest + content-search plan (governance-alignment register item #6). Writes
    content_index.report_path (default iba/app/reports/content-index-rebuild.md): files scanned,
    total key occurrences indexed. Requires Manifest-Rebuild.ps1 to have run at least once —
    content_index's coverage never exceeds file_manifest's. See ContentIndex-Search.ps1 for
    querying the result (which also incrementally refreshes the index first).

.PARAMETER RunId  resume/re-tag a specific run (reuse the run_id from a prior call).
.PARAMETER Trace  Print every config read (IBA_TRACE).

.EXAMPLE
    .\ContentIndex-Rebuild.ps1
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

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-CONTENTINDEX-REBUILD" }

Write-IbaRunHeader -WorkPackage 'content-index-rebuild' -RunId $runId

$json = python -m iba.app.run content-index-rebuild --step content_index.rebuild --run-id $runId
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'content_index.rebuild' -Path $res.path -Message $res.message -Code $code

exit $code
