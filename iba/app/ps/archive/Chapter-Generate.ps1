<#
.SYNOPSIS
    The chapter-generate work package — entry point (a) of the book-by-book pipeline's 3-way
    split (chapter generation / book overview / book narrative, per the researcher's 2026-08-02
    instruction). PowerShell orchestrates; Python works; CONFIG (in the DB) governs.

.DESCRIPTION
    First CHECKS the book's passage is already registered for this exact scope (`build-passages`'
    `passage.build`, redefined 2026-08-06 — a passage is now the debate's own input scope, read and
    judged feasible by a real analytical pass, not derived by an algorithm). Redefined 2026-08-05
    (B4) around HIB-continuity, then redefined again 2026-08-06 after a visualization across four
    sample chapters showed HIB-continuity didn't correspond to a real narrative break in any of
    them — passaging turned out to be about reading capacity, not story structure. Because
    registering a passage now requires a genuine reading judgement (a story synthesis + a
    feasibility self-assessment), this script no longer auto-invokes it — it only checks one is
    already live for the scope, and stops with a clear message (run `Build-Passages.ps1` yourself
    first) if not.

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

    Guideline (advisory, not enforced — see cfg_passage passage.debate_session_chapter_guideline):
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

# Redefined 2026-08-06: passage.build now requires a real analytical payload (a story synthesis +
# a feasibility judgement) -- it is a writer like hib.set/phenomenon.set/operation.set, not a
# mechanical rebuild-on-demand utility, so it can no longer be silently auto-invoked here the way
# B4's algorithm was. This script now only CHECKS a passage is already registered for the exact
# scope being generated -- run Build-Passages.ps1 yourself first if not.
$tracked = python -c "
from iba.app.lib.cfg import Cfg
from iba.app.lib import passagetrack, versespanmeaningreport as vsm
cfg = Cfg()
if '$Range':
    ch, vlo, vhi = vsm.parse_range('$Range'); lo = hi = ch
else:
    lo, hi = vsm.parse_chapters('$Chapters'); vlo = vhi = None
row = passagetrack.find_tracked_passage(cfg.conn, '$Book', lo, hi, vlo, vhi)
print('1' if row else '0')
cfg.close()
"
if ($tracked -ne '1') {
    Write-Host "No passage registered yet for this exact scope." -ForegroundColor Yellow
    Write-Host "Run Build-Passages.ps1 -Book $Book $(if ($Range) {"-Range $Range"} else {"-Chapters $Chapters"}) -PayloadPath <json> first." -ForegroundColor Yellow
    exit 1
}
Write-Host ""

$guideline = python -c "from iba.app.lib.cfg import Cfg; c=Cfg(); print(c.module_setting('cfg_passage', 'passage.debate_session_chapter_guideline', 3)); c.close()"

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
