<#
.SYNOPSIS
    The verse-lexical work package — replaces VerseSpanMeaning-Report.ps1 (retired). Chains
    lexical.build (the mechanical T1-T3 engine) then report.verse_lexical (a pure render off
    the DB) under one run_id, for one book/chapter-range.

.DESCRIPTION
    lexical.build resolves, per code within every span, role (content lexical entry vs.
    grammatical formative) and — for content codes — a morph-selected sense (not the whole
    stem/voice paradigm), writing version-aware rows to verse_lexical (soft-deletes the superseded
    row, never overwrites in place). report.verse_lexical then renders an MD extract purely from
    that table — it does not re-derive anything from span/strong/strong_meaning_parsed itself.
    Runs independent of report.passage_debate/T4-T9; see
    iba/app/reports/t1-t3-design-decisions-20260805.md for the full design record.

    STEP-dependent for lexical.build only (step.required_for_runs, default true) — a
    content-role code with no strong row yet needs a live STEP call to resolve. report.verse_lexical
    itself has no STEP dependency.

.PARAMETER Book       OSIS book code as stored in verse.osisId, e.g. Dan. Mandatory.
.PARAMETER Chapters   whole-chapter range, e.g. 1-3 or 1. Mutually exclusive with -Range.
.PARAMETER Range      single-chapter verse range, e.g. 8:1-27. Mutually exclusive with -Chapters.
.PARAMETER BookLabel  subfolder-name OVERRIDE, used verbatim -- exists for the rare case the
                      folder must differ from -Book. Defaults to -Book if omitted, and that
                      default is almost always what you want: _analytics/Bible_Books subfolders
                      must be named EXACTLY as cfg_book_order.book (the OSIS code, e.g. Dan, not
                      a full name like "Daniel") -- passing -BookLabel with anything else creates
                      a second, wrong, non-compliant folder next to the real one (found live
                      2026-08-29, escalation #1007 thread). Omit this parameter unless you have a
                      specific, confirmed reason not to.
.PARAMETER Step       Run only this one step (lexical.build | report.verse_lexical) instead of
                      the full chained sequence -- e.g. report.verse_lexical alone, to VIEW
                      already-built results for a range without re-running the build (which may
                      make live STEP calls). Omit to run the full sequence, unchanged default.
.PARAMETER RunId      resume/re-tag a specific run.
.PARAMETER Trace      Print every config read (IBA_TRACE).

.EXAMPLE
    .\VerseLexical.ps1 -Book Dan -Range 8:1-27
.EXAMPLE
    .\VerseLexical.ps1 -Book Dan -Range 8:1-27 -Step report.verse_lexical
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [string] $Book,
    [string] $Chapters,
    [string] $Range,
    [string] $BookLabel,
    [ValidateSet('lexical.build', 'report.verse_lexical')] [string] $Step,
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

Test-IbaWorkPackageActive -WorkPackage 'verse-lexical'

$seq   = python -c "import json; from iba.app.lib.cfg import Cfg; c=Cfg(); print(json.dumps([dict(r) for r in c.sequence('verse-lexical')])); c.close()" | ConvertFrom-Json
if ($Step) { $seq = $seq | Where-Object { $_.step -eq $Step } }
$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-VERSE-LEXICAL" }

Write-IbaRunHeader -WorkPackage 'verse-lexical' -RunId $runId -RunsOver "book = '$Book'"
Write-Host "sequence     : $($seq.Count) steps, loaded from the DB config store (cfg_step)"
Write-Host ""

$paramArgs = @('--param', "Book=$Book")
if ($Chapters)  { $paramArgs += @('--param', "Chapters=$Chapters") }
if ($Range)     { $paramArgs += @('--param', "Range=$Range") }
if ($BookLabel) { $paramArgs += @('--param', "BookLabel=$BookLabel") }

$halt = $false
$exitCode = 0
foreach ($entry in $seq) {
    $json = python -m iba.app.run verse-lexical --step $entry.step --run-id $runId @paramArgs
    $code = $LASTEXITCODE
    $res  = $json | ConvertFrom-Json

    Write-IbaStepResult -Step $entry.step -Path $res.path -Message $res.message -Code $code

    if ($code -eq 2) {
        Write-IbaPaused -WorkPackage 'verse-lexical' -RunId $runId -Message $res.message
        $halt = $true; $exitCode = 2; break
    }
    if ($code -eq 3) {
        Write-IbaStopped -Message $res.message
        $halt = $true; $exitCode = 3; break
    }
}

if (-not $halt) {
    Write-IbaComplete -WorkPackage 'verse-lexical' -Vars @{ book = $Book }
}
exit $exitCode
