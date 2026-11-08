<#
.SYNOPSIS
    Start, watch and stop a long job against the Ollama server (escalation #2388).

.DESCRIPTION
    Every long Ollama job keeps a progress file, a stop flag and a log under Logs\longrun\ (lib/longrun.py). The first job is collection-batch: the
    collections built from the sub-groups of the bases not yet in a collection (a seed word, then the AI judging its candidates, per sub-group).

      Plan      -Job collection-batch   write the plan (one seed word per sub-group) and say how many there are
      Start     -Job collection-batch [-Limit n]   start the job detached, through Windows' own process service (rule B:125), so it does not end when
                the Claude app closes. It keeps the machine from idle sleep while it runs. Closing the lid or sleeping the machine by hand still ends it:
                Progress then says NOT running, and Start again resumes (finished sub-groups are skipped).
      Progress  -Job <name>   state, done of total, the item in hand, seconds per item, estimated finish, process id, last problem. Read-only.
      Stop      -Job <name>   ask it to end after the item in hand (a collection takes about 12 minutes); Start resumes it.

.EXAMPLE
    iba\app\ps\Long-Run.ps1 -Action Progress -Job collection-batch
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('Plan', 'Start', 'Progress', 'Stop')]
    [string] $Action,
    [Parameter(Mandatory = $true)]
    [string] $Job,
    [string] $Limit,
    [switch] $Trace
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'
if ($Trace) { $env:IBA_TRACE = '1' }

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot
. $PSScriptRoot\_lib\Notify.ps1

$stepMap = @{ Plan = 'long.plan'; Start = 'long.start'; Progress = 'long.progress'; Stop = 'long.stop' }
$stepId = $stepMap[$Action]
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-LONGRUN"

$paramArgs = @('--param', "Job=$Job")
if ($PSBoundParameters.ContainsKey('Limit')) { $paramArgs += @('--param', "Limit=$Limit") }

Write-IbaRunHeader -WorkPackage 'long-run' -Step $stepId -RunId $runId
$json = python -m iba.app.run long-run --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Message $res.message -Code $code
exit $code
