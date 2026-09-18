<#
.SYNOPSIS
    The `char-reading` stage (`cluster.reading`, process c, escalation #1706 Phase F pipeline
    stage 3, design #1682 / `ib-observation-governing-rules-checklist-v1-20260916.md` §2). Entry
    point for `cluster-reading`'s second step -- reads one subgroup's member strongs, corpus-wide,
    synergising the similar/different meaning of the subgroup's own strongs against each other.

.DESCRIPTION
    Reads the subgroup's member strongs' full occurrence lists (every occurrence, no sampling),
    all meaning sources, and Stage 1/2's own already-captured observations as grounding -- ONE call
    per subgroup, never batched, never the whole cluster (checklist §2 rule 1). Always previews cost
    first (default: `-Live` is NOT given, so nothing is called and nothing is written). A live run
    hard-refuses unless `cluster_subgroup.status='ready_for_reading'`. On success,
    `lib/recordingpass.py:record_batch` writes the observations (`stage='char-reading'`) in the
    same unit of work, per-strong completeness is computed by code (never trusted from the model),
    then `cluster_subgroup.status` advances to `ready_for_answer`.

.PARAMETER ClusterCode   The M-code or T-code the subgroup belongs to, e.g. M67. Mandatory.
.PARAMETER SubgroupCode  The subgroup's own code, e.g. M67_A_dispositional_idleness. Mandatory.
.PARAMETER Live          Actually call the API and write results. Omit for a preview (cost
                       estimate, no API call, nothing written) -- always preview first.
.PARAMETER RunId         resume/re-tag a specific run.
.PARAMETER Trace         Print every config read (IBA_TRACE).

.EXAMPLE
    .\CharReading.ps1 -ClusterCode M67 -SubgroupCode M67_A_dispositional_idleness
    # -> preview only: strong/occurrence count + estimated cost, no API call, nothing written.
.EXAMPLE
    .\CharReading.ps1 -ClusterCode M67 -SubgroupCode M67_A_dispositional_idleness -Live
    # -> real run: one LLM call, observations recorded, cluster_subgroup.status -> ready_for_answer.
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

$stepId = 'cluster.reading'
$runId  = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-CLUSTER-READING" }

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
