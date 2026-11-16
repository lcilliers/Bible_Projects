<#
.SYNOPSIS
    The verse-lexical work package: builds the structural composition of the verse (Window 1 Layer 1) and reports on it. Chains lexical.build (the mechanical engine) then
    report.verse_lexical (a pure render off the DB) and report.lexical_exceptions (the self-audit) under one run_id, for one book/chapter-range.

.DESCRIPTION
    lexical.build resolves, per code within every span, role (content lexical entry vs. grammatical formative) and -- for content codes -- a morph-selected sense, writing
    version-aware rows to verse_lexical (soft-deletes the superseded row, never overwrites in place). report.verse_lexical renders an MD extract purely from that table.
    report.lexical_exceptions is the self-audit: a tally of the structure and of the lexical observations (stage lexical) with a node in the range, and the faults in their nodes.
    STEP-dependent for lexical.build only (step.required_for_runs, default true) -- a content-role code with no strong row yet needs a live STEP call to resolve.

    The lexical analysis of the words is not made here: it is stage 1 of the collection reading (Collection-Build.ps1 -Action LayerOpen -Step S1, #2507). lexical.enrich,
    lexical.notes and report.lexical_extract (the Layer 2 notes of Window 1, the table verse_lexical_note and its extract) are retired, #2507.

.PARAMETER Book       OSIS book code as stored in verse.osisId, e.g. Dan. Mandatory.
.PARAMETER Chapters   whole-chapter range, e.g. 1-3 or 1. Mutually exclusive with -Range.
.PARAMETER Range      single-chapter verse range, e.g. 8:1-27. Mutually exclusive with -Chapters.
.PARAMETER BookLabel  subfolder-name OVERRIDE, used verbatim; defaults to -Book (the subfolders of _analytics/Bible_Books are named exactly as cfg_book_order.book, e.g. Dan).
                      Omit unless there is a confirmed reason.
.PARAMETER Step       Run only this one step (lexical.build | report.verse_lexical | report.lexical_exceptions | lexical.readiness) instead of the full chained sequence.
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [string] $Book,
    [string] $Chapters,
    [string] $Range,
    [string] $BookLabel,
    [ValidateSet('lexical.build', 'report.verse_lexical', 'report.lexical_exceptions', 'lexical.readiness')] [string] $Step,
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
if ($Step) {
    $seq = $seq | Where-Object { $_.step -eq $Step }
}
$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-VERSE-LEXICAL" }

Write-IbaRunHeader -WorkPackage 'verse-lexical' -RunId $runId -RunsOver "book = '$Book'"
Write-Host "sequence     : $($seq.Count) steps, loaded from the DB config store (cfg_step)"
Write-Host ""

$paramArgs = @('--param', "Book=$Book")
if ($Chapters)      { $paramArgs += @('--param', "Chapters=$Chapters") }
if ($Range)         { $paramArgs += @('--param', "Range=$Range") }
if ($BookLabel)     { $paramArgs += @('--param', "BookLabel=$BookLabel") }

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
