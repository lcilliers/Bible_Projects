<#
.SYNOPSIS
    The first split of the concept surfaces into behaviour, state, being or other, judged by the Ollama server
    (escalation #2354).

.DESCRIPTION
    The list is the distinct surface of surface_subgroup. Each surface goes to the server on its own (no verse,
    no Hebrew or Greek code); the answer is one of behaviour, inner_being_state, being or other. A surface goes
    to the first three only when it definitely belongs there, otherwise to other. Every answer is inferential
    until the researcher confirms it. Nothing is written to iba.db: the answers are appended, one JSON line per
    surface as it finishes, to the batch file <surface_judge.batch_dir>/<Batch>.jsonl.

      Status   -Batch <name>   how far the batch file has got against the list: judged per group, failed, left
      Run      -Batch <name> [-Limit n]   judge the surfaces not yet judged; -Limit stops after n surfaces
               (a pilot is a Run with a small -Limit). Resumable: run it again with the same -Batch and it
               carries on; a surface that failed is tried again. Ctrl+C stops after the surface in hand.
      Cycle    -Batch <name>   the whole list, unattended: work periods (surface_judge.cycle_work_minutes) with a
               cool-down between (cycle_cooldown_minutes); after a halt it waits (cycle_halt_wait_minutes) and
               tries again, and ends after cycle_max_halts_in_a_row periods in a row with no progress. The ssh
               tunnel is open only during a work period. Run it in its own terminal; the machine is kept awake.
      Progress -Batch <name>   (any terminal, while a cycle runs or after) state, judged per group, failed, left,
               the recent speed and the estimated finish; says so when the cycle is no longer alive
      Stop     -Batch <name>   asks the running cycle to end after the surface in hand; Cycle again resumes

    -Batch is lower-case words joined by hyphens, then -v and a number, then -yyyymmdd.
    The server, the model, the groups and the prompt are cfg_setting rows (modules ollama and surface_judge).

.EXAMPLE
    iba\app\ps\Surface-Judge.ps1 -Action Run -Batch first-split-v1-20261102 -Limit 20
.EXAMPLE
    iba\app\ps\Surface-Judge.ps1 -Action Run -Batch first-split-v1-20261102
.EXAMPLE
    iba\app\ps\Surface-Judge.ps1 -Action Status -Batch first-split-v1-20261102
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('Status', 'Run', 'Cycle', 'Progress', 'Stop')]
    [string] $Action,
    [Parameter(Mandatory = $true)] [string] $Batch,
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

$stepMap = @{ Status = 'surface_judge.status'; Run = 'surface_judge.run'; Cycle = 'surface_judge.cycle';
              Progress = 'surface_judge.progress'; Stop = 'surface_judge.stop' }
$stepId = $stepMap[$Action]
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-SURFACEJUDGE"

$paramArgs = @()
foreach ($p in @('Batch', 'Limit')) {
    if ($PSBoundParameters.ContainsKey($p)) { $paramArgs += @('--param', "$p=$($PSBoundParameters[$p])") }
}

Write-IbaRunHeader -WorkPackage 'surface-judge' -Step $stepId -RunId $runId
$json = python -m iba.app.run surface-judge --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Message $res.message -Code $code
exit $code
