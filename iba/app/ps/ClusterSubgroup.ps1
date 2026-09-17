<#
.SYNOPSIS
    The `char-subgroup` stage (`cluster.subgroup`, process b, escalation #1706 Phase F pipeline
    stage 2, design #1690/#1693) -- whole-cluster, one LLM session, groups a cluster's member
    strongs into meaning-based subgroups. Entry point for the new `cluster-reading` work package
    (houses this step now, char-reading/char-answers/char-synergy later).

.DESCRIPTION
    Reads the cluster's full member-strong list -- gloss/surface plus its already-captured
    verse-reading (Stage 1) observations -- in ONE call, never batched (#1690 §2(a): the whole
    cluster must be read before any assignment, never a streaming process). Always previews cost
    first (default: `-Live` is NOT given, so nothing is called and nothing is written). A live run
    hard-refuses unless `cluster.status='ready_for_subgroup_allocation'` (verse-reading must already
    be complete for every member strong), and refuses to re-run against a cluster that already has
    live subgroups (re-grouping/reconciliation is not designed yet, #1690 §5 item 1). On success,
    `lib/recordingpass.py:record_subgroups` writes `cluster_subgroup`/`cluster_subgroup_strong` in
    the same unit of work, then `cluster.status` advances to `ready_for_reading`.

.PARAMETER ClusterCode  The M-code or T-code to allocate subgroups for, e.g. M67. Mandatory.
.PARAMETER Live         Actually call the API and write results. Omit for a preview (cost estimate,
                      no API call, nothing written) -- always preview first.
.PARAMETER RunId        resume/re-tag a specific run.
.PARAMETER Trace        Print every config read (IBA_TRACE).

.EXAMPLE
    .\ClusterSubgroup.ps1 -ClusterCode M67
    # -> preview only: strong count + estimated cost, no API call, nothing written.
.EXAMPLE
    .\ClusterSubgroup.ps1 -ClusterCode M67 -Live
    # -> real run: one LLM call, subgroups/membership recorded, cluster.status -> ready_for_reading.
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [string] $ClusterCode,
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

$stepId = 'cluster.subgroup'
$runId  = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-CLUSTER-SUBGROUP" }

Write-IbaRunHeader -WorkPackage 'cluster-reading' -Step $stepId -RunId $runId -RunsOver "cluster_code = '$ClusterCode'"

$paramArgs = @('--param', "ClusterCode=$ClusterCode")
$paramArgs += @('--param', "Preview=$(if ($Live) { 'false' } else { 'true' })")

$json = python -m iba.app.run cluster-reading --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code

exit $code
