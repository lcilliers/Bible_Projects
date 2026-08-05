<#
.SYNOPSIS
    The chapter-generate work package — entry point (a) of the book-by-book pipeline's 3-way
    split (chapter generation / book overview / book narrative, per the researcher's 2026-08-02
    instruction). PowerShell orchestrates; Python works; CONFIG (in the DB) governs.

.DESCRIPTION
    First ensures the book's passages are current (`build-passages`' `passage.build`, redefined
    2026-08-05 around HIB-continuity — B4, debate-analytic-process-digest-20260805.md Step 2) — a
    genuinely SEPARATE governed step, its own run_id, run and checked BEFORE chapter-generate's own
    sequence, not chained into it (re-invoking a chained work package re-runs every ordinal in its
    sequence from the top, which is exactly the failure mode this script's own scaffold-overwrite
    guard below exists to avoid — the same risk would apply to passage.build if it shared a run_id).
    A `no-hibs`/paused result here stops the whole script — generating a debate scaffold against
    stale or absent passage boundaries is worse than not generating one at all.

    Then chains report.verse_span_meaning (base extract) then report.passage_debate (debate
    SCAFFOLD) under one run_id, for one book/chapter-range — the two purely mechanical prep steps a
    chapter needs before the manual interpretive fill-in can start. The sequence comes from
    cfg_step (work_package 'chapter-generate'), not from this script.

    Deliberately stops here. Filling in the scaffold's <!-- fill in --> placeholders is manual,
    unmechanised analytical work (same boundary every other debate-producing step in this app
    draws). Once filled, run PassageDebate-Sync.ps1 separately to flip debate_status to 'filled' —
    it is NOT chained into this script, because re-invoking a chained work package re-runs every
    ordinal in its sequence from the top, which would silently overwrite an already-filled
    scaffold with a fresh blank one.

    Guideline (advisory, not enforced — see cfg_setting passage.debate_session_chapter_guideline):
    fill roughly 3 chapters' worth of debates per Claude Code session, then clear context and
    start a fresh one, before generating the next batch. See
    iba/app/reports/token-consumption-diagnostic-20260802.md for why.

.PARAMETER Book       OSIS book code as stored in verse.osisId, e.g. Hos. Mandatory.
.PARAMETER Chapters   whole-chapter range, e.g. 1-3 or 1. Mutually exclusive with -Range.
.PARAMETER Range      single-chapter verse range, e.g. 2:17-30. Mutually exclusive with -Chapters.
.PARAMETER BookLabel  human-facing subfolder name (e.g. "Hosea"). Defaults to -Book if omitted.
.PARAMETER RunId      resume/re-tag a specific run.
.PARAMETER Trace      Print every config read (IBA_TRACE).

.EXAMPLE
    .\Chapter-Generate.ps1 -Book Amos -Chapters 1 -BookLabel Amos
    # writes amos-1-verse-span-meaning.md, then WA-amos-1-debate.md (scaffold) -- fill it in,
    # then: .\PassageDebate-Sync.ps1 -Book Amos -Chapters 1 -BookLabel Amos
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

Test-IbaWorkPackageActive -WorkPackage 'chapter-generate'
Test-IbaWorkPackageActive -WorkPackage 'build-passages'

# B4 — ensure passages are current BEFORE anything else runs (own run_id, NOT chained into the
# sequence below — see .DESCRIPTION). Book-scoped, not range-scoped: passage.build always
# recomputes the WHOLE book's passages (a clean drop+rebuild), so this stays correct regardless of
# which -Chapters/-Range this particular invocation is generating a debate for.
$passageRunId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-BUILD-PASSAGES"
Write-IbaRunHeader -WorkPackage 'build-passages' -RunId $passageRunId -RunsOver "book = '$Book'"
$json = python -m iba.app.run build-passages --step passage.build --run-id $passageRunId --param "Book=$Book"
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'passage.build' -Path $res.path -Message $res.message -Code $code
if ($code -eq 2) {
    Write-IbaPaused -WorkPackage 'build-passages' -RunId $passageRunId -Message $res.message
    exit 2
}
if ($code -eq 3) {
    Write-IbaStopped -Message $res.message
    exit 3
}
Write-Host ""

$guideline = python -c "from iba.app.lib.cfg import Cfg; c=Cfg(); print(c.setting('passage.debate_session_chapter_guideline', 3)); c.close()"

$seq   = python -c "import json; from iba.app.lib.cfg import Cfg; c=Cfg(); print(json.dumps([dict(r) for r in c.sequence('chapter-generate')])); c.close()" | ConvertFrom-Json
$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-CHAPTER-GENERATE" }

Write-IbaRunHeader -WorkPackage 'chapter-generate' -RunId $runId -RunsOver "book = '$Book'"
Write-Host "sequence     : $($seq.Count) steps, loaded from the DB config store (cfg_step)"
Write-Host "guideline    : ~$guideline chapters of debate fill-in per Claude Code session, then clear context (advisory)" -ForegroundColor DarkGray
Write-Host ""

$paramArgs = @('--param', "Book=$Book")
if ($Chapters)  { $paramArgs += @('--param', "Chapters=$Chapters") }
if ($Range)     { $paramArgs += @('--param', "Range=$Range") }
if ($BookLabel) { $paramArgs += @('--param', "BookLabel=$BookLabel") }

$halt = $false
$exitCode = 0                       # 0 done · 2 paused · 3 stopped — so the script is composable
foreach ($entry in $seq) {
    $json = python -m iba.app.run chapter-generate --step $entry.step --run-id $runId @paramArgs
    $code = $LASTEXITCODE
    $res  = $json | ConvertFrom-Json

    Write-IbaStepResult -Step $entry.step -Path $res.path -Message $res.message -Code $code

    if ($code -eq 2) {
        Write-IbaPaused -WorkPackage 'chapter-generate' -RunId $runId -Message $res.message
        $halt = $true; $exitCode = 2; break
    }
    if ($code -eq 3) {
        Write-IbaStopped -Message $res.message
        $halt = $true; $exitCode = 3; break
    }
}

if (-not $halt) {
    Write-IbaComplete -WorkPackage 'chapter-generate' -Vars @{ book = $Book }
    Write-Host "`nFill in every <!-- fill in --> placeholder by applying:" -ForegroundColor DarkGray
    $guidance = python -c "from iba.app.lib.cfg import Cfg; c=Cfg(); print(c.setting('method.passage_read_guidance_path')); c.close()"
    $interrogative = python -c "from iba.app.lib.cfg import Cfg; c=Cfg(); print(c.setting('method.interpretation_questions_path')); c.close()"
    Write-Host "  method:        $guidance" -ForegroundColor DarkGray
    Write-Host "  interrogative: $interrogative" -ForegroundColor DarkGray
}
exit $exitCode
