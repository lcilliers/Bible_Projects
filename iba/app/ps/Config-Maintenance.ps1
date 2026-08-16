<#
.SYNOPSIS
    The configuration_maintenance work package — the ONE sanctioned path for changing a
    cfg_* row. Config-governed, approval-gated. Not a fixed pipeline: validate/propose/report
    are three independent operations sharing one registration, so you pick which to run.

.DESCRIPTION
    -Step Validate   read-only coherence check of the live cfg_* tables. Safe any time.
    -Step Propose    DB-direct, single-row, APPROVAL-GATED change. First call escalates and
                      pauses (exit code 2) — answer it with:
                        Escalation.ps1 -Action AnswerRun -RunId <run_id> -Decision <Approve|Reject|Revise|Hold|Noted>
                      then re-run this SAME command (same run id is generated per invocation,
                      so pass -RunId to resume the same proposal rather than opening a new one).
    -Step Report     regenerate CONFIG-REPORT.md from the live cfg_* tables. Safe any time.

.PARAMETER Step     Validate | Propose | Report
.PARAMETER Table    (Propose) the cfg_* table to change, e.g. cfg_setting
.PARAMETER Op       (Propose) insert | update | delete
.PARAMETER Where    (Propose) JSON object identifying the row, e.g. '{"key":"passage.review_over"}'
.PARAMETER Set      (Propose) JSON object of the new values, e.g. '{"value":"12"}'
.PARAMETER Question (Propose) plain-text description of the change, shown to the researcher —
                      make this REPRESENTATIVE (what it is, why, what it affects), not a bare diff.
.PARAMETER RunId     resume a specific pending proposal (reuse the run_id from its first call).
.PARAMETER Trace     Print every config read (IBA_TRACE).

.EXAMPLE
    iba/app/ps/Config-Maintenance.ps1 -Step Validate

.EXAMPLE
    iba/app/ps/Config-Maintenance.ps1 -Step Propose -Table cfg_setting -Op update `
        -Where '{"key":"passage.review_over"}' -Set '{"value":"12"}' `
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
$runId  = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-CONFIGMAINT" }

$paramArgs = @()
if ($Step -eq 'Propose') {
    if (-not $Table -or -not $Op) {
        Write-Host "Propose needs -Table and -Op (Where/Set/Question as the change requires)." -ForegroundColor Yellow
        exit 1
    }
    $paramArgs += @('--param', "Table=$Table", '--param', "Op=$Op")
    if ($Where)    { $paramArgs += @('--param', "Where=$Where") }
    if ($Set)      { $paramArgs += @('--param', "Set=$Set") }
    if ($Question) { $paramArgs += @('--param', "Question=$Question") }
}

Write-IbaRunHeader -WorkPackage 'configuration-maintenance' -Step $stepId -RunId $runId

$json = python -m iba.app.run configuration-maintenance --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code

if ($code -eq 2) {
    Write-IbaPaused -WorkPackage 'configuration-maintenance' -RunId $runId -Message $res.message
}
if ($code -eq 0 -and $Step -eq 'Propose') {
    $auto = python -c "from iba.app.lib.cfg import Cfg; c=Cfg(); print(str(c.setting('configmaint.auto_report', True)).lower()); c.close()"
    if ($auto -eq 'true') {
        Write-Host "`n(auto_report) regenerating CONFIG-REPORT.md..." -ForegroundColor DarkGray
        python -m iba.app.run configuration-maintenance --step configmaint.report --run-id $runId | Out-Null
    }
}

exit $code
