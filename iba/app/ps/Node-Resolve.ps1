<#
.SYNOPSIS
    The sweep that resolves the references on ib_node (escalation #2308): the occurrence (verse_lexical_id), the morph
    code and the sub_group code of every node that names a strong and a verse, looked up from the tables.

.DESCRIPTION
      Plan                    what the sweep would fill on ib_node and what it cannot, with the reason. Reads only.
                              Writes the plan JSON and its report to node_resolve.output_dir (outputs/node-resolve).
      Apply -File <plan JSON> writes the plan: each node only into a null column, and only if it still holds what the
                              plan saw. Writes a report of the run.

    Method rules NR-01 to NR-06 are on node_resolve.apply (cfg_method_rule).

.EXAMPLE
    iba\app\ps\Node-Resolve.ps1 -Step Plan
.EXAMPLE
    iba\app\ps\Node-Resolve.ps1 -Step Apply -File outputs\node-resolve\resolve-plan-v1-20261026.json
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [ValidateSet('Plan', 'Apply')] [string] $Step,
    [string] $File,
    [switch] $Trace
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'
if ($Trace) { $env:IBA_TRACE = '1' }

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot
. $PSScriptRoot\_lib\Notify.ps1

$stepId = @{ Plan = 'node_resolve.plan'; Apply = 'node_resolve.apply' }[$Step]
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-NODERESOLVE"

$paramArgs = @()
if ($File) { $paramArgs += @('--param', "File=$File") }

Write-IbaRunHeader -WorkPackage 'node-resolve' -Step $stepId -RunId $runId
$json = python -m iba.app.run node-resolve --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code
exit $code
