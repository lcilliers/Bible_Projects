<#
.SYNOPSIS
    Pull meaning ONLY (not verses) for every strong a book's (or one chapter's verse range's)
    spans reference but that has no `strong` row yet — progressive, passage-driven DB coverage,
    per the researcher's 2026-07-25 direction (see BUILD.md).

.DESCRIPTION
    Reuses raw.detail_one() unchanged (already meaning-only, independent of raw.verses). Self-
    contained since 2026-07-25 (BUILD.md §18): the parsed-layer refresh and related-terms fetch
    for the newly pulled strongs happen automatically as part of this run — no separate
    Lexicon-Parse.ps1 call needed afterward.

.PARAMETER Book   OSIS book code as stored in verse.osisId, e.g. Dan
.PARAMETER Range  optional: chapter:verse-verse, e.g. 1:1-7 — narrows to one chapter's verse
                  range. Omit to backfill the whole book.
.PARAMETER RunId  resume a specific pending run.
.PARAMETER Trace  Print every config read (IBA_TRACE).

.EXAMPLE
    .\Raw-Backfill.ps1 -Book Dan -Range 1:1-7
.EXAMPLE
    .\Raw-Backfill.ps1 -Book Dan
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [string] $Book,
    [string] $Range,
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

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-RAW-BACKFILL" }

$paramArgs = @('--param', "Book=$Book")
if ($Range) { $paramArgs += @('--param', "Range=$Range") }

Write-IbaRunHeader -WorkPackage 'raw-backfill' -Step 'raw.backfill_meaning' -RunId $runId -RunsOver $Book

$json = python -m iba.app.run raw-backfill --step raw.backfill_meaning --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'raw.backfill_meaning' -Path $res.path -Message $res.message -Code $code

if ($code -eq 2) {
    Write-IbaPaused -WorkPackage 'raw-backfill' -RunId $runId -Message $res.message
}

exit $code
