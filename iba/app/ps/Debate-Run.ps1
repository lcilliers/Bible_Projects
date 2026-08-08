<#
.SYNOPSIS
    The single entry point for running a debate over one book/chapter-range — replaces the old
    Chapter-Generate.ps1 scaffold route (retired 2026-08-07, superseded by the DB-first
    hib/phenomenon/operation/closing model). PowerShell orchestrates; Python works; CONFIG (in the
    DB) governs.

.DESCRIPTION
    Step 1 (researcher direction, 2026-08-06): validates the WHOLE book+chapter scope has a
    complete lexical before any reading starts -- hard stop, naming the missing verses, if not
    (lib/debaterun.py:lexical_complete_for_scope). Verses genuinely absent from the `verse` table
    are intentional (governance.verse_gap_by_design) and never counted as missing.

    Then reads the live step order from `cfg_setting` (`passage.debate_run_sequence`), not a
    hardcoded array — walks: hib.set -> passage.build -> phenomenon.set -> operation.set ->
    closing.set,
    each still under its OWN existing work package (operations-ingest / build-passages —
    `cfg_step.step` must be globally unique across work_package, GOVERNANCE.md ~line 1470, so this
    script registers no new steps; it only sequences what already works). Once closing.set
    succeeds, auto-renders the debate report (`python -m iba.app.tools.build_debate_report`).

    Per-step separation still exists to gate the ANALYTICAL CONTENT — each content step still
    needs its own genuinely-authored JSON payload; that discipline is unchanged (BUILD.md
    §61-71, the "failure modes" this whole method guards against). What's removed is only the
    manual-invocation ceremony: for each step, this script

      1. Checks whether it's already satisfied for this scope (lib/debaterun.py's readiness
         checks, mirroring each handler's own DB gate) — if so, skips it.
      2. Otherwise looks for a staging payload at the config-pattern path
         (`passage.debate_staging_path_pattern`, e.g.
         iba\app\staging\operations\dan-1-hib.set.json) — if present, runs the step with it.
      3. Otherwise STOPS, printing the exact path expected. That payload is authored by whoever
         does that step's actual analytical reading (the AI, in-session, from the lexical + prior
         DB state) — never something typed in by hand at this command line. Once it's written,
         rerunning the EXACT SAME command picks up from wherever DB+staging state now is; no
         run-id bookkeeping needed for resume.

    Does NOT run lexical.build — the lexical is a separate, book-scoped, run-ahead-of-time
    prerequisite (VerseLexical.ps1), independent of how many small debate chapters follow
    (researcher direction, 2026-08-06). hib.set's own hard gate refuses cleanly
    (`lexical-incomplete`) if it's missing; this script just surfaces that message.

.PARAMETER Book       OSIS book code as stored in verse.osisId, e.g. Dan. Mandatory.
.PARAMETER Chapters   whole-chapter range, e.g. 1-3 or 1. Mutually exclusive with -Range.
.PARAMETER Range      single-chapter verse range, e.g. 8:1-27. Mutually exclusive with -Chapters.
.PARAMETER BookLabel  human-facing subfolder name (e.g. "Daniel"). Defaults to -Book if omitted --
                      same shape as VerseLexical.ps1. Corrected 2026-08-08: every step's own
                      reconciliation report AND the final rendered debate report now file under
                      report.verse_analysis_output_dir/<BookLabel>/, same convention every sibling
                      book tool (VerseLexical.ps1/BookNarrative-Generate.ps1/WholeBookRead-Report.ps1)
                      already uses -- these had been landing flat in governance.oneoff_report_dir
                      instead, a filing bug, not a deliberate design difference (found live,
                      researcher: "the filing for all Book related operations should be in the
                      iba/app/verse-analysis/[book] folders where it has been since we started").
.PARAMETER Step       run only this one step (hib.set|passage.build|phenomenon.set|operation.set|
                      closing.set), same readiness/staging logic, then stop — for a targeted
                      standalone correction/rerun (mirrors the real Dan 8 rollback/redo,
                      BUILD.md §71). Omit to walk the full sequence.
.PARAMETER RunId      resume/re-tag a specific run.
.PARAMETER Trace      Print every config read (IBA_TRACE).

.EXAMPLE
    iba\app\ps\Debate-Run.ps1 -Book Dan -Chapters 1 -BookLabel Daniel
    # single chapter, filed under iba/app/verse-analysis/Daniel/
.EXAMPLE
    iba\app\ps\Debate-Run.ps1 -Book Dan -Chapters 1
    # -BookLabel omitted -- files under iba/app/verse-analysis/Dan/ instead (defaults to -Book)
.EXAMPLE
    iba\app\ps\Debate-Run.ps1 -Book Dan -Chapters 1-3
    # multi-chapter range
.EXAMPLE
    iba\app\ps\Debate-Run.ps1 -Book Dan -Range 8:1-27
    # sub-chapter range
.EXAMPLE
    iba\app\ps\Debate-Run.ps1 -Book Dan -Chapters 1 -Step hib.set
    # targeted single-step rerun/correction
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [string] $Book,
    [string] $Chapters,
    [string] $Range,
    [string] $BookLabel,
    [ValidateSet('hib.set', 'passage.build', 'phenomenon.set', 'operation.set', 'closing.set')]
    [string] $Step,
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

$runId  = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-DEBATE" }
$scope  = if ($Chapters) { $Chapters } else { $Range }
$scopeLabel = "$Book $scope"
# Filesystem-safe token for the staging path only (':' is invalid in a Windows filename) --
# lib/debaterun.py:scope_token does the same substitution; kept here too since this script
# builds the path string directly rather than shelling out for every use of it.
$scopeToken = if ($Chapters) { $Chapters } else { $Range -replace ':', '_' }

# Step 1 of the debate pipeline (researcher direction, 2026-08-06, quoted verbatim in
# operations.py:_check_lexical_complete): validate the WHOLE book+chapter scope has a complete
# lexical BEFORE any HIB reading starts -- hard stop here, not a side-effect of hib.set refusing a
# submitted payload after the fact. Missing verses in the `verse` table itself are intentional
# (governance.verse_gap_by_design) and never counted as missing lexical coverage.
$lexCheck = python -c "
import json
from iba.app.lib.cfg import Cfg
from iba.app.lib import debaterun as dr
cfg = Cfg()
ok, missing = dr.lexical_complete_for_scope(cfg.conn, '$Book', $(if ($Chapters) { "'$Chapters'" } else { 'None' }), $(if ($Range) { "'$Range'" } else { 'None' }))
print(json.dumps({'ok': ok, 'missing': missing}))
cfg.close()
"
$lex = $lexCheck | ConvertFrom-Json
if (-not $lex.ok) {
    Write-Host ""
    if ($lex.missing.Count -eq 0) {
        Write-Host "STOPPED -- no live verses found for $scopeLabel." -ForegroundColor Yellow
    } else {
        Write-Host "STOPPED -- lexical incomplete for $scopeLabel -- $($lex.missing.Count) verse(s) with no live verse_lexical row:" -ForegroundColor Yellow
        Write-Host "  $($lex.missing -join ', ')" -ForegroundColor Yellow
        Write-Host "  Build it first: iba\app\ps\VerseLexical.ps1 -Book $Book -Chapters <whole book>" -ForegroundColor Yellow
    }
    exit 1
}

# Sequence comes from the DB config store, not a hardcoded array here.
$seqJson = python -c "import json; from iba.app.lib.cfg import Cfg; c=Cfg(); print(json.dumps(c.setting('passage.debate_run_sequence', []))); c.close()"
$seq = $seqJson | ConvertFrom-Json
if (-not $seq -or $seq.Count -eq 0) {
    Write-Host "passage.debate_run_sequence is empty/missing in cfg_setting -- nothing to run." -ForegroundColor Yellow
    exit 1
}
if ($Step) { $seq = $seq | Where-Object { $_.step -eq $Step } }

Write-Host "work package : debate-run (steps under their own existing work packages)"
Write-Host "run_id       : $runId"
Write-Host "runs over    : scope = '$scopeLabel'"
Write-Host "sequence     : $($seq.Count) step(s), loaded from the DB config store (cfg_setting.passage.debate_run_sequence)"
Write-Host ""

$exitCode = 0
foreach ($entry in $seq) {
    # NOTE (found live, 2026-08-07): the per-iteration step name MUST NOT be named $step --
    # PowerShell variable names are case-insensitive, so a lowercase $step silently collides
    # with the -Step PARAMETER above it, overwriting it with the last-iterated step name by the
    # time the loop exits. That made "-not $Step" false on every full-sequence (no -Step) run,
    # silently skipping the auto-render block below -- found when it never fired after a real
    # closing.set success. Named $stepName here instead to keep the parameter intact.
    $pkg      = $entry.work_package
    $stepName = $entry.step

    $stagingPath = python -c "
from iba.app.lib.cfg import Cfg
from iba.app.lib import debaterun as dr
cfg = Cfg()
print(dr.staging_path(cfg, '$Book', '$scopeToken', '$stepName'))
cfg.close()
"

    $isReady = python -c "
import sqlite3
from iba.app.lib.cfg import Cfg
from iba.app.lib import debaterun as dr
cfg = Cfg()
print('1' if dr.is_ready(cfg.conn, '$stepName', '$Book', $(if ($Chapters) { "'$Chapters'" } else { 'None' }), $(if ($Range) { "'$Range'" } else { 'None' })) else '0')
cfg.close()
"

    if ($isReady -eq '1') {
        Write-Host "  $($stepName.PadRight(20)) skip           already satisfied for this scope" -ForegroundColor DarkGray
        continue
    }

    if (-not (Test-Path $stagingPath)) {
        Write-Host ""
        Write-Host "STOPPED -- $stepName needs its analytical payload next." -ForegroundColor Yellow
        Write-Host "  Write it to: $stagingPath" -ForegroundColor Yellow
        Write-Host "  Then rerun the exact same command -- readiness is re-derived from the DB" -ForegroundColor Yellow
        Write-Host "  and staging files each time, no run-id bookkeeping needed to resume." -ForegroundColor Yellow
        exit 1
    }

    $paramArgs = @('--param', "Book=$Book", '--param', "PayloadPath=$stagingPath")
    if ($Chapters)   { $paramArgs += @('--param', "Chapters=$Chapters") }
    if ($Range)      { $paramArgs += @('--param', "Range=$Range") }
    if ($BookLabel)  { $paramArgs += @('--param', "BookLabel=$BookLabel") }

    $json = python -m iba.app.run $pkg --step $stepName --run-id $runId @paramArgs
    $code = $LASTEXITCODE
    $res  = $json | ConvertFrom-Json
    Write-IbaStepResult -Step $stepName -Path $res.path -Message $res.message -Code $code

    if ($code -eq 2) {
        Write-IbaPaused -WorkPackage $pkg -RunId $runId -Message $res.message
        $exitCode = 2; break
    }
    if ($code -eq 3) {
        Write-IbaStopped -Message $res.message
        $exitCode = 3; break
    }
}

if ($exitCode -eq 0 -and -not $Step) {
    Write-Host ""
    Write-Host "closing.set complete -- rendering the debate report..." -ForegroundColor DarkGray
    $reportArgs = @()
    if ($BookLabel) { $reportArgs += @('--book-label', $BookLabel) }
    if ($Chapters) {
        python -m iba.app.tools.build_debate_report --book $Book --chapters $Chapters @reportArgs
    } else {
        python -m iba.app.tools.build_debate_report --book $Book --range $Range @reportArgs
    }
    Write-Host ""
    Write-Host "COMPLETE -- debate built and rendered for '$scopeLabel'." -ForegroundColor Green
}

exit $exitCode
