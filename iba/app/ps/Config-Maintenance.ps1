<#
.SYNOPSIS
    The configuration_maintenance work package — the ONE sanctioned path for changing a
    cfg_* row. Config-governed, approval-gated. Not a fixed pipeline: validate/propose/report
    are three independent operations sharing one registration, so you pick which to run.

.DESCRIPTION
    -Step Validate   read-only coherence check of the live cfg_* tables. Safe any time.
    -Step Propose    DB-direct, single-row, APPROVAL-GATED change. First call escalates and
                      pauses (exit code 2) as a decision_required item, assigned to the
                      Researcher. NOT answered via AnswerRun -- every propose pause is
                      resolution_kind=decision_required, and answer_for_run() (the code behind
                      AnswerRun) unconditionally refuses those (escalation #820, corrected here
                      2026-08-31 -- this help text told people to run something that could never
                      succeed). Answer it via Update's two-stage manual vocabulary instead:
                        Escalation.ps1 -Action Update -Id <id> -NextAction ready_for_approval `
                            -Resolution "<what's being proposed>" -AnsweredBy <who>
                        Escalation.ps1 -Action Update -Id <id> -NextAction approved `
                            -AnsweredBy Researcher -Resolution "..."
                      then re-run this SAME command (same run id is generated per invocation,
                      so pass -RunId to resume the same proposal rather than opening a new one).
                      This re-run is the app's own design for who applies it: needs_followup on
                      the escalation means the actual write is meant to happen as "a second
                      Claude-driven re-run with -RunId" (escalation #1301) AFTER the researcher's
                      own approved. CORRECTED 2026-08-31 (escalation #1306 v8/#1357): a same-day
                      session wrongly diagnosed this re-run as blocked by the Claude Code harness's
                      own permission classifier and deferred it undone. Reproduced clean in the
                      next session -- the real (and only) gate is the app's own state machine: the
                      resume only applies once Update() has recorded a genuine `approved` decision
                      (checked via answered_for_run()), which a re-assignment/"proceed" COMMENT
                      alone does not do. Once `-NextAction ready_for_approval` then `-NextAction
                      approved` are actually recorded, Claude CAN and does run this re-run itself --
                      no elevated permissions, no researcher-run workaround needed.
    -Step Report     regenerate CONFIG-REPORT.md from the live cfg_* tables. Safe any time.

.PARAMETER Step     Validate | Propose | Report
.PARAMETER Table    (Propose) the cfg_* table to change, e.g. cfg_setting
.PARAMETER Op       (Propose) insert | update | delete
.PARAMETER Where    (Propose) JSON object identifying the row, e.g. '{"key":"passage.review_over"}'
.PARAMETER Set      (Propose) JSON object of the new values, e.g. '{"value":"12"}'
.PARAMETER Title    (Propose) REQUIRED. A short, title-shaped name for the change (<=60 chars, no
                      "--" clause-stitching) -- this becomes the escalation's short_description
                      directly. Escalation #1326, 2026-08-31: -Question used to be forced to serve
                      as both the title and the description, silently word-sliced to 60 chars --
                      every real proposal's short_description was a mid-word-truncated fragment.
                      A badly-shaped -Title fails loudly here, immediately, rather than degrading
                      silently three layers downstream.
.PARAMETER Question (Propose) the fuller, REPRESENTATIVE description (what it is, why, what it
                      affects) -- not a bare diff, and no longer doubling as the title. Always
                      preserved verbatim in the escalation's context.
.PARAMETER RunId     resume a specific pending proposal (reuse the run_id from its first call).
.PARAMETER Trace     Print every config read (IBA_TRACE).

.EXAMPLE
    iba/app/ps/Config-Maintenance.ps1 -Step Validate

.EXAMPLE
    iba/app/ps/Config-Maintenance.ps1 -Step Propose -Table cfg_setting -Op update `
        -Where '{"key":"passage.review_over"}' -Set '{"value":"12"}' `
        -Title "Raise passage.review_over to 12" `
        -Question "Raise passage.review_over from 10 to 12 — fewer long passages flagged needs_review."
    # -> PAUSED, run_id printed. Answer it, then:
    iba/app/ps/Config-Maintenance.ps1 -Step Propose -RunId <the run_id> -Table cfg_setting -Op update `
        -Where '{"key":"passage.review_over"}' -Set '{"value":"12"}'

.EXAMPLE
    iba/app/ps/Config-Maintenance.ps1 -Step Report
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [ValidateSet('Validate', 'Propose', 'Report')] [string] $Step,
    [string] $Table,
    [string] $Op,
    [string] $Where,
    [string] $Set,
    [string] $Title,
    [string] $Question,
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

$stepId = @{ Validate = 'configmaint.validate'; Propose = 'configmaint.propose'; Report = 'configmaint.report' }[$Step]
# escalation #1326, 2026-08-31 -- real bug found live while testing the -Title guard below:
# PowerShell variable names are CASE-INSENSITIVE, so a local $runId and the -RunId PARAMETER
# are literally the same variable slot. The old code (`$runId = if ($RunId) {...} else {...}`)
# silently overwrote the parameter with the freshly-generated id on every fresh call -- harmless
# before now because nothing downstream re-checked "was -RunId actually supplied", but it made
# any such check permanently, silently impossible (checked here first, confirmed live: the guard
# below never fired, even with -RunId genuinely omitted). Captured BEFORE the collision, and the
# local renamed so this can't recur.
$isResume = [bool]$RunId
$resolvedRunId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-CONFIGMAINT" }

$paramArgs = @()
if ($Step -eq 'Propose') {
    if (-not $Table -or -not $Op) {
        Write-Host "Propose needs -Table and -Op (Where/Set/Title/Question as the change requires)." -ForegroundColor Yellow
        exit 1
    }
    # -Title only required on the FIRST call (no -RunId yet) -- a resume-with-RunId re-invokes
    # propose() past the point title/question are even read (escalation #1326).
    if (-not $isResume -and -not $Title) {
        Write-Host "Propose needs -Title on a fresh call -- a short, title-shaped name for the change (<=60 chars, no '--'). -Question is the fuller description." -ForegroundColor Yellow
        exit 1
    }
    $paramArgs += @('--param', "Table=$Table", '--param', "Op=$Op")
    if ($Where)    { $paramArgs += @('--param', "Where=$Where") }
    if ($Set)      { $paramArgs += @('--param', "Set=$Set") }
    if ($Title)    { $paramArgs += @('--param', "Title=$Title") }
    if ($Question) { $paramArgs += @('--param', "Question=$Question") }
}

Write-IbaRunHeader -WorkPackage 'configuration-maintenance' -Step $stepId -RunId $resolvedRunId

$json = python -m iba.app.run configuration-maintenance --step $stepId --run-id $resolvedRunId @paramArgs
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code

if ($code -eq 2) {
    Write-IbaPaused -WorkPackage 'configuration-maintenance' -RunId $resolvedRunId -Message $res.message
}
if ($code -eq 0 -and $Step -eq 'Propose') {
    $auto = python -c "from iba.app.lib.cfg import Cfg; c=Cfg(); print(str(c.setting('configmaint.auto_report', True)).lower()); c.close()"
    if ($auto -eq 'true') {
        Write-Host "`n(auto_report) regenerating CONFIG-REPORT.md..." -ForegroundColor DarkGray
        # -Param Auto=1 (escalation #1351-1356): this chained call is NOT a deliberate -Step
        # Report -- without the flag it hit the same handler as one and always exported the full
        # CSV pairing, which several Proposes applied back-to-back (e.g. a multi-row registration
        # batch) could re-write fast enough to collide with their own predecessor's still-in-
        # flight archive-rename (WinError 32). Auto=1 defers to configmaint.csv_export_on_auto_report
        # instead (default 0/suppressed), matching how validate()'s own auto-regeneration already behaves.
        python -m iba.app.run configuration-maintenance --step configmaint.report --run-id $resolvedRunId --param Auto=1 | Out-Null
    }
}

exit $code
