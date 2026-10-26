<#
.SYNOPSIS
    The surface mapping of an M cluster (escalation #2293, #2286 U3): each (Strong's code, surface) pair
    placed in one of the cluster's subgroups (behaviour rules subgroups-are-surface-groups and
    surface-mapping-conditions).

.DESCRIPTION
    Run per cluster, in this order:

      Pairs  -Cluster M18                  the pairs file: every pair with its hits, verses, gloss, samples, head
                                           or tail (cluster.surface_map.head_share of the hits), its inherited
                                           subgroup and its live allocation. Reads only.
             (Claude fills the file's groups and head allocations in session)
      Apply  -Cluster M18 -File <file>     writes the filled file: new groups (with kind) and the pairs. Refuses
                                           the whole file on any problem. Makes the cluster's anomaly group.
      Tail   -Cluster M18 [-Live]          the pairs still unallocated, allocated by the API (code, gloss, surface,
                                           one sample verse). Without -Live: a preview with the cost, no call.
      Check  -Cluster M18                  the report: group sizes and shares (a group over
                                           cluster.surface_map.max_group_share is flagged), the anomaly group,
                                           unallocated and two-sense pairs. Reads only.

    Files go to cluster.surface_map.output_dir (outputs/surface-map), versioned per day. The design is
    outputs/escalation/2293-surface-map-design-v1-20261025.md.

.EXAMPLE
    iba\app\ps\Surface-Map.ps1 -Step Pairs -Cluster M18
.EXAMPLE
    iba\app\ps\Surface-Map.ps1 -Step Apply -Cluster M18 -File outputs\surface-map\m18-pairs-20261025.json
.EXAMPLE
    iba\app\ps\Surface-Map.ps1 -Step Tail -Cluster M18 -Live
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [ValidateSet('Pairs', 'Apply', 'Tail', 'Check')] [string] $Step,
    [Parameter(Mandatory = $true)] [string] $Cluster,
    [string] $File,
    [switch] $Live,
    [switch] $Trace
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'
if ($Trace) { $env:IBA_TRACE = '1' }

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot
. $PSScriptRoot\_lib\Notify.ps1

$stepId = @{ Pairs = 'cluster.surface_pairs'; Apply = 'cluster.surface_apply'; Tail = 'cluster.surface_tail';
             Check = 'cluster.surface_check' }[$Step]
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-SURFACEMAP"

$paramArgs = @('--param', "Cluster=$Cluster")
if ($File) { $paramArgs += @('--param', "File=$File") }
if ($Live) { $paramArgs += @('--param', 'Live=1') }

Write-IbaRunHeader -WorkPackage 'cluster-surface-map' -Step $stepId -RunId $runId
$json = python -m iba.app.run cluster-surface-map --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code
exit $code
