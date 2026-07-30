<#
.SYNOPSIS
    Re-syncs `passage.debate_status` for an already-generated `report.passage_debate` scaffold
    against its CURRENT on-disk content. Read-only against the debate file — does NOT regenerate
    or rewrite it (that stays PassageDebate-Report.ps1's job, and rerunning it on an already-filled
    range would overwrite real content with a blank scaffold). Run this after filling in every
    `<!-- fill in -->` placeholder by hand, so the tracked `passage` row's `debate_status` flips
    from `scaffold` to `filled` — closing the gap GOVERNANCE.md §3B names: previously nothing
    re-checked status after manual fill-in, forcing guesswork about how earlier books' rows ever
    reached `filled`.

.DESCRIPTION
    Looks up the already-tracked `passage` row for this exact book/range (from a prior
    VerseSpanMeaning-Report.ps1 + PassageDebate-Report.ps1 run), reads its `debate_path` file, and
    updates `debate_status` to `filled` or `scaffold` depending on whether any `<!-- fill in -->`
    marker remains. Fails with `no-debate-file` if no scaffold was ever tracked for this range, or
    `debate-file-missing` if the tracked path no longer exists on disk.

.PARAMETER Book       OSIS book code as stored in verse.osisId, e.g. Mic. Mandatory.
.PARAMETER Chapters   whole-chapter range, e.g. 1-3 or 1. Mutually exclusive with -Range.
.PARAMETER Range      single-chapter verse range, e.g. 2:17-30. Mutually exclusive with -Chapters.
.PARAMETER BookLabel  human-facing subfolder name (e.g. "Micah"). Defaults to -Book if omitted —
                      same convention as PassageDebate-Report.ps1's -BookLabel.
.PARAMETER RunId      resume/re-tag a specific run.
.PARAMETER Trace      Print every config read (IBA_TRACE).

.EXAMPLE
    .\PassageDebate-Sync.ps1 -Book Mic -Chapters 1 -BookLabel Micah
.EXAMPLE
    .\PassageDebate-Sync.ps1 -Book Dan -Range 3:1-7 -BookLabel Daniel
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [string] $Book,
    [string] $Chapters,
    [string] $Range,
    [string] $BookLabel,
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

if ([bool]$Chapters -eq [bool]$Range) {
    Write-Host "Give exactly one of -Chapters or -Range." -ForegroundColor Yellow
    exit 1
}

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-PASSAGE-DEBATE-SYNC" }

$paramArgs = @('--param', "Book=$Book")
if ($Chapters) { $paramArgs += @('--param', "Chapters=$Chapters") }
if ($Range)    { $paramArgs += @('--param', "Range=$Range") }
if ($BookLabel) { $paramArgs += @('--param', "BookLabel=$BookLabel") }

Write-IbaRunHeader -WorkPackage 'passage-debate-sync' -Step 'passage.debate_sync' -RunId $runId

$json = python -m iba.app.run passage-debate-sync --step passage.debate_sync --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'passage.debate_sync' -Path $res.path -Message $res.message -Code $code

exit $code
