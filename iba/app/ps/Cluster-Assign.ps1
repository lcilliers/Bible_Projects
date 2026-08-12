<#
.SYNOPSIS
    Cluster-assignment (T02) -- DB-wide mechanical classification + backfill-to-active promotion,
    and a read-only coverage/exception report. Standalone work package (each step invoked
    independently), same shape as Lexicon-Parse.ps1/Candidate-Quality.ps1/Passage-Quality.ps1.

.DESCRIPTION
    -Step Assign     DB-wide sweep: lib.strongreconcile.reconcile() against every strong row --
                     mechanical HIGH-precedent cluster match (P1/P2, no researcher decision needed)
                     plus the backfill->word promotion cascade wherever a non-T2 classification and
                     a word_registry link both already hold. Safe to re-run (idempotent).
    -Step Validate   read-only coverage + exception check. If there are findings, escalates ONCE,
                     then pauses. Answer with
                     `Escalation.ps1 -Action AnswerRun -RunId <run_id> -Decision <Approve|Reject|Revise>`,
                     then re-run this script with -Step Validate -RunId <run_id> to act on the answer.

.PARAMETER Step   Assign | Validate
.PARAMETER RunId  resume a specific pending check (reuse the run_id from its first call).
.PARAMETER Trace  Print every config read (IBA_TRACE).

.EXAMPLE
    .\Cluster-Assign.ps1 -Step Assign
.EXAMPLE
    .\Cluster-Assign.ps1 -Step Validate
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [ValidateSet('Assign', 'Validate')] [string] $Step,
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

$stepId = @{ Assign = 'cluster.assign'; Validate = 'cluster.validate' }[$Step]
$runId  = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-CLUSTER-ASSIGN" }

Write-IbaRunHeader -WorkPackage 'cluster-assign' -Step $stepId -RunId $runId

$json = python -m iba.app.run cluster-assign --step $stepId --run-id $runId
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code

if ($code -eq 2) {
    Write-IbaPaused -WorkPackage 'cluster-assign' -RunId $runId -Message $res.message
}

exit $code
