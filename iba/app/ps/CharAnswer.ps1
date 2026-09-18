<#
.SYNOPSIS
    The `char-answers` stage (`cluster.answer`, process d, escalation #1706 Phase F pipeline
    stage 4, design #1682 §4A / `ib-observation-governing-rules-checklist-v1-20260916.md` §3).
    Entry point for `cluster-reading`'s third step -- answers the catalogue's characteristic-grain
    question battery for one subgroup, against its Stage 1/2/3 accumulated evidence.

.DESCRIPTION
    Reads the subgroup's member strongs' full evidence (occurrences, meaning sources, and every
    prior stage's own observations) and answers the catalogue's 52 live "characteristic-grain"
    questions (excludes D7.7.1, already Stage 1's territory, and science-extract-dependent
    questions, not yet wired) -- ONE call per subgroup, never batched, never the whole cluster.
    Multiple distinct slants are recorded separately under the same question_code where the
    evidence genuinely differs across the subgroup's own strongs. Always previews cost first
    (default: `-Live` is NOT given). A live run hard-refuses unless
    `cluster_subgroup.status='ready_for_answer'`. On success, `lib/recordingpass.py:record_batch`
    writes the observations (`stage='char-answers'`) in the same unit of work, per-question
    completeness is computed by code, then `cluster_subgroup.status` advances to `answer_complete`.

.PARAMETER ClusterCode   The M-code or T-code the subgroup belongs to, e.g. M67. Mandatory.
.PARAMETER SubgroupCode  The subgroup's own code, e.g. M67_A_dispositional_idleness. Mandatory.
.PARAMETER Live          Actually call the API and write results. Omit for a preview (cost
                       estimate, no API call, nothing written) -- always preview first.
.PARAMETER RunId         resume/re-tag a specific run.
.PARAMETER Trace         Print every config read (IBA_TRACE).

.EXAMPLE
    .\CharAnswer.ps1 -ClusterCode M67 -SubgroupCode M67_A_dispositional_idleness
    # -> preview only: strong/question count + estimated cost, no API call, nothing written.
.EXAMPLE
    .\CharAnswer.ps1 -ClusterCode M67 -SubgroupCode M67_A_dispositional_idleness -Live
    # -> real run: one LLM call, observations recorded, cluster_subgroup.status -> answer_complete.
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [string] $ClusterCode,
    [Parameter(Mandatory = $true)] [string] $SubgroupCode,
    [switch] $Live,
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

Test-IbaWorkPackageActive -WorkPackage 'cluster-reading'

$stepId = 'cluster.answer'
$runId  = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-CLUSTER-ANSWER" }

Write-IbaRunHeader -WorkPackage 'cluster-reading' -Step $stepId -RunId $runId `
    -RunsOver "cluster_code = '$ClusterCode', subgroup_code = '$SubgroupCode'"

$paramArgs = @('--param', "ClusterCode=$ClusterCode")
$paramArgs += @('--param', "SubgroupCode=$SubgroupCode")
$paramArgs += @('--param', "Preview=$(if ($Live) { 'false' } else { 'true' })")

$json = python -m iba.app.run cluster-reading --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code

exit $code
