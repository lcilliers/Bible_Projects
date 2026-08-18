<#
.SYNOPSIS
    Search .md file CONTENT (not just filenames) for a Strong's number, gloss, or project word —
    incrementally refreshes the index first, then looks up the current index.

.DESCRIPTION
    Round 2 of the manifest + content-search plan (governance-alignment register item #6). Runs an
    mtime-based incremental refresh (only .md files new/changed since the last pass are re-scanned)
    before querying, so the index is never stale at query time — then returns hits enriched with
    file_manifest metadata alongside the content hit's file path and line number. Writes results as
    a one-off report (governance.oneoff_* naming/archiving). Query forms: `strong:H2734`,
    `gloss:anger`, `word:anger`, or a bare value checked across all three key types.

.PARAMETER Query  the search term — required.
.PARAMETER Csv    also write the FULL result set as .csv (added 2026-08-17) — the .md report caps
                   at 500 rows for readability; a large query (e.g. gloss:compassion, 23,098+ hits)
                   needs the untruncated set for real spreadsheet review.
.PARAMETER RunId  resume/re-tag a specific run.
.PARAMETER Trace  Print every config read (IBA_TRACE).

.EXAMPLE
    iba/app/ps/ContentIndex-Search.ps1 -Query "strong:H2734"
.EXAMPLE
    iba/app/ps/ContentIndex-Search.ps1 -Query "gloss:compassion" -Csv
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string] $Query,
    [switch] $Csv,
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

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-CONTENTINDEX-SEARCH" }

Write-IbaRunHeader -WorkPackage 'content-index-search' -RunId $runId

$paramArgs = @('--param', "Query=$Query")
if ($Csv) { $paramArgs += @('--param', 'Csv=1') }

$json = python -m iba.app.run content-index-search --step content_index.search --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'content_index.search' -Path $res.path -Message $res.message -Code $code
if ($res.counts.csv_path) { Write-Output "  csv: $($res.counts.csv_path)" }

exit $code
