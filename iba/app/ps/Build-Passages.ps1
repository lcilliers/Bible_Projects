<#
.SYNOPSIS
    Register the debate's own input scope as a passage. Config-governed.

.DESCRIPTION
    Runs the 'build-passages' work package's passage.build step for one book+scope. Redefined
    2026-08-06 (researcher direction, following the HIB-distribution visualization across four
    chapters): a passage is no longer derived by a HIB-continuity algorithm — it IS the given
    scope, verbatim. This step reads the whole scope in light of the HIBs already identified
    (hib.set must have run first for these verses), and requires a JSON payload carrying the
    already-decided reading judgement: a high-level story synthesis, and a self-assessment of
    whether the scope can be read as a whole without quality loss. If not, the step refuses
    outright (no passage row written) with a message to narrow the scope and resubmit.

.PARAMETER Book         OSIS book code, e.g. Dan, Hos, Jon.
.PARAMETER Chapters     Whole-chapter range, e.g. 1-3 or 1. Mutually exclusive with -Range.
.PARAMETER Range        Single-chapter verse range, e.g. 8:1-27. Mutually exclusive with -Chapters.
.PARAMETER PayloadPath  Path to the JSON payload file (story_summary/feasible/feasibility_note,
                        and reconciliation_note if correcting an already-registered scope).
                        Not used with -Suggest (that mode makes no table write).
.PARAMETER Suggest      Runs passage.suggest_boundary first (escalation #1383, build spec §C.3/
                        §F.2) instead of passage.build -- proposes the next candidate passage
                        boundary for -Book from cheap mechanical proxy signals only (NOT a genre
                        determination), prints it, and pauses (exit code 2) for the researcher to
                        either re-run with an explicit -Chapters/-Range of their own choosing, or
                        accept the suggestion verbatim with -Confirm. Mutually exclusive with
                        -Chapters/-Range/-PayloadPath -- the suggester computes its own starting
                        point from what's not yet passaged in -Book.
.PARAMETER Confirm      Only meaningful with -Suggest: skips the pause and feeds the suggested
                        range straight into the existing, unchanged passage.build call --
                        PayloadPath is still required (the human-confirmation gate is about the
                        BOUNDARY, not about skipping passage.build's own story/feasibility
                        payload).
.PARAMETER Trace        Print every config read (IBA_TRACE).

.EXAMPLE
    .\Build-Passages.ps1 -Book Dan -Range 8:1-27 -PayloadPath iba\app\staging\passages\dan-8.json
.EXAMPLE
    .\Build-Passages.ps1 -Book Hos -Chapters 1 -PayloadPath iba\app\staging\passages\hos-1.json
.EXAMPLE
    .\Build-Passages.ps1 -Book Gal -Suggest
.EXAMPLE
    .\Build-Passages.ps1 -Book Gal -Suggest -Confirm -PayloadPath iba\app\staging\passages\gal-next.json
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [string] $Book,
    [string] $Chapters,
    [string] $Range,
    [string] $PayloadPath,
    [switch] $Suggest,
    [switch] $Confirm,
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

Test-IbaWorkPackageActive -WorkPackage 'build-passages'

if ($Suggest) {
    if ($Chapters -or $Range) {
        Write-Host "-Suggest computes its own starting point in -Book -- don't also pass -Chapters/-Range." -ForegroundColor Yellow
        exit 1
    }
    if ($Confirm -and -not $PayloadPath) {
        Write-Host "-Confirm needs -PayloadPath (the story/feasibility payload passage.build still requires)." -ForegroundColor Yellow
        exit 1
    }

    $runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-BUILD-PASSAGES"
    Write-IbaRunHeader -WorkPackage 'build-passages' -RunId $runId -RunsOver "book = '$Book'"

    $json = python -m iba.app.run build-passages --step passage.suggest_boundary --run-id $runId --param "Book=$Book"
    $code = $LASTEXITCODE
    $res  = $json | ConvertFrom-Json
    Write-IbaStepResult -Step 'passage.suggest_boundary' -Path $null -Message $res.message -Code $code

    if ($code -ne 0) {
        if ($code -eq 3) { Write-IbaStopped -Message $res.message } else { Write-IbaPaused -WorkPackage 'build-passages' -RunId $runId -Message $res.message }
        exit $code
    }
    if (-not $Confirm) {
        Write-Host ""
        Write-Host "Proposal only -- no table write. Re-run with an explicit -Chapters/-Range of your own" -ForegroundColor Cyan
        Write-Host "choosing (adjusted or verbatim), or with -Confirm -PayloadPath <path> to accept it as-is." -ForegroundColor Cyan
        exit 2
    }

    # suggest_boundary never crosses a chapter boundary (its own candidate query is chapter-
    # scoped) -- start_ref/end_ref are always "<chapter>:<verse>" in the SAME chapter, so this
    # is always expressible as a single -Range "<chapter>:<startVerse>-<endVerse>".
    $startCh, $startVs = $res.start_ref -split ':'
    $endCh,   $endVs   = $res.end_ref   -split ':'
    if ($startCh -ne $endCh) {
        Write-Host "Suggestion spans chapters ($($res.start_ref)-$($res.end_ref)) -- re-run with an explicit -Chapters/-Range." -ForegroundColor Yellow
        exit 1
    }
    $Range = "${startCh}:${startVs}-${endVs}"
    Write-Host "Accepted suggestion -- passing straight into passage.build: -Range $Range" -ForegroundColor Cyan
}

if ([bool]$Chapters -eq [bool]$Range) {
    Write-Host "passage.build needs exactly one of -Chapters or -Range." -ForegroundColor Yellow
    exit 1
}
if (-not $PayloadPath -or -not (Test-Path $PayloadPath)) {
    Write-Host "PayloadPath '$PayloadPath' does not exist." -ForegroundColor Yellow
    exit 1
}

$runId = if ($Suggest) { $runId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-BUILD-PASSAGES" }
$scopeLabel = if ($Range) { "$Book $Range" } else { "$Book $Chapters" }
if (-not $Suggest) {
    Write-IbaRunHeader -WorkPackage 'build-passages' -RunId $runId -RunsOver "scope = '$scopeLabel'"
}

$paramArgs = @('--param', "Book=$Book", '--param', "PayloadPath=$PayloadPath")
if ($Chapters) { $paramArgs += @('--param', "Chapters=$Chapters") }
if ($Range)    { $paramArgs += @('--param', "Range=$Range") }

$json = python -m iba.app.run build-passages --step passage.build --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'passage.build' -Path $res.path -Message $res.message -Code $code

if ($code -eq 3) { Write-IbaStopped -Message $res.message }
elseif ($code -eq 2) { Write-IbaPaused -WorkPackage 'build-passages' -RunId $runId -Message $res.message }
else { Write-IbaComplete -WorkPackage 'build-passages' -Vars @{ scope = $scopeLabel } }

exit $code
