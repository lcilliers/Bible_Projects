<#
.SYNOPSIS
    The verse-span-reading work package — replaces VerseSpanMeaning-Report.ps1 (retired). Chains
    span_reading.build (the mechanical T1-T3 engine) then report.span_reading (a pure render off
    the DB) under one run_id, for one book/chapter-range.

.DESCRIPTION
    span_reading.build resolves, per code within every span, role (content lexical entry vs.
    grammatical formative) and — for content codes — a morph-selected sense (not the whole
    stem/voice paradigm), writing version-aware rows to span_reading (soft-deletes the superseded
    row, never overwrites in place). report.span_reading then renders an MD extract purely from
    that table — it does not re-derive anything from span/strong/strong_meaning_parsed itself.
    Runs independent of report.passage_debate/T4-T9; see
    iba/app/reports/t1-t3-design-decisions-20260805.md for the full design record.

    STEP-dependent for span_reading.build only (step.required_for_runs, default true) — a
    content-role code with no strong row yet needs a live STEP call to resolve. report.span_reading
    itself has no STEP dependency.

.PARAMETER Book       OSIS book code as stored in verse.osisId, e.g. Dan. Mandatory.
.PARAMETER Chapters   whole-chapter range, e.g. 1-3 or 1. Mutually exclusive with -Range.
.PARAMETER Range      single-chapter verse range, e.g. 8:1-27. Mutually exclusive with -Chapters.
.PARAMETER BookLabel  human-facing subfolder name (e.g. "Daniel"). Defaults to -Book if omitted.
.PARAMETER RunId      resume/re-tag a specific run.
.PARAMETER Trace      Print every config read (IBA_TRACE).

.EXAMPLE
    .\VerseSpanReading.ps1 -Book Dan -Range 8:1-27 -BookLabel Daniel
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

Test-IbaWorkPackageActive -WorkPackage 'verse-span-reading'

$seq   = python -c "import json; from iba.app.lib.cfg import Cfg; c=Cfg(); print(json.dumps([dict(r) for r in c.sequence('verse-span-reading')])); c.close()" | ConvertFrom-Json
$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-VERSE-SPAN-READING" }

Write-IbaRunHeader -WorkPackage 'verse-span-reading' -RunId $runId -RunsOver "book = '$Book'"
Write-Host "sequence     : $($seq.Count) steps, loaded from the DB config store (cfg_step)"
Write-Host ""

$paramArgs = @('--param', "Book=$Book")
if ($Chapters)  { $paramArgs += @('--param', "Chapters=$Chapters") }
if ($Range)     { $paramArgs += @('--param', "Range=$Range") }
if ($BookLabel) { $paramArgs += @('--param', "BookLabel=$BookLabel") }

$halt = $false
$exitCode = 0
foreach ($entry in $seq) {
    $json = python -m iba.app.run verse-span-reading --step $entry.step --run-id $runId @paramArgs
    $code = $LASTEXITCODE
    $res  = $json | ConvertFrom-Json

    Write-IbaStepResult -Step $entry.step -Path $res.path -Message $res.message -Code $code

    if ($code -eq 2) {
        Write-IbaPaused -WorkPackage 'verse-span-reading' -RunId $runId -Message $res.message
        $halt = $true; $exitCode = 2; break
    }
    if ($code -eq 3) {
        Write-IbaStopped -Message $res.message
        $halt = $true; $exitCode = 3; break
    }
}

if (-not $halt) {
    Write-IbaComplete -WorkPackage 'verse-span-reading' -Vars @{ book = $Book }
}
exit $exitCode
