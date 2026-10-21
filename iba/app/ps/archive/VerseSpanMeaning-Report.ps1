<#
.SYNOPSIS
    Verse : span : meaning extract for a book/chapter-range — per-span meaning from all three
    parse tables (meaning_tree/lsj/mounce), live STEP disambiguation for AMBIGUOUS (sibling-shared-
    base) spans. Read-only.

.DESCRIPTION
    Writes to report.verse_analysis_output_dir/<BookLabel>/<pattern> (config-governed folder +
    filename, not hardcoded — see CONFIG-REPORT.md, module 'report'). STEP-dependent: refuses
    (exit code from cfg_on_fail report.verse_span_meaning/unreachable) if STEP is down and
    step.required_for_runs is true (the default).

.PARAMETER Book       OSIS book code as stored in verse.osisId, e.g. Dan. Mandatory.
.PARAMETER Chapters   whole-chapter range, e.g. 1-3 or 1. Mutually exclusive with -Range.
.PARAMETER Range      single-chapter verse range, e.g. 1:1-7. Mutually exclusive with -Chapters.
.PARAMETER BookLabel  human-facing subfolder name (e.g. "Daniel"). Defaults to -Book if omitted —
                      a per-call parameter, not a setting (which folder label a given call uses
                      varies per invocation, it isn't a rule; see lib/versespanmeaningreport.py).
.PARAMETER RunId      resume/re-tag a specific run.
.PARAMETER Trace      Print every config read (IBA_TRACE).

.EXAMPLE
    .\VerseSpanMeaning-Report.ps1 -Book Dan -Range 1:1-7 -BookLabel Daniel
.EXAMPLE
    .\VerseSpanMeaning-Report.ps1 -Book Dan -Chapters 1-3 -BookLabel Daniel
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

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-VERSE-ANALYSIS" }

$paramArgs = @('--param', "Book=$Book")
if ($Chapters) { $paramArgs += @('--param', "Chapters=$Chapters") }
if ($Range)    { $paramArgs += @('--param', "Range=$Range") }
if ($BookLabel) { $paramArgs += @('--param', "BookLabel=$BookLabel") }

Write-IbaRunHeader -WorkPackage 'verse-analysis-report' -Step 'report.verse_span_meaning' -RunId $runId

$json = python -m iba.app.run verse-analysis-report --step report.verse_span_meaning --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'report.verse_span_meaning' -Path $res.path -Message $res.message -Code $code

exit $code
