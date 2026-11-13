<#
.SYNOPSIS
    The node and observation checker (escalation #2484): every live node and live observation against the node rules
    (behaviour rules B:130 and B:131), listed by the check it fails.

.DESCRIPTION
      Report    reads the live database and writes a Markdown report and a workbook (one sheet for each check, every finding a
                row) to node_check.output_dir (_analytics/reading-tools/node-check). Writes nothing to any table.

    A finding says what is wrong or missing, not what to do. Candidates marked 'to be read' (an observation repeating the
    verse text) need a reading and are not judged. Method rules NC-01 to NC-04 are on node_check.report (cfg_method_rule).

.EXAMPLE
    iba\app\ps\Node-Check.ps1 -Step Report
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [ValidateSet('Report')] [string] $Step,
    [switch] $Trace
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'
if ($Trace) { $env:IBA_TRACE = '1' }

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot
. $PSScriptRoot\_lib\Notify.ps1

$stepId = @{ Report = 'node_check.report' }[$Step]
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-NODECHECK"

Write-IbaRunHeader -WorkPackage 'node-check' -Step $stepId -RunId $runId
$json = python -m iba.app.run node-check --step $stepId --run-id $runId
$code = $LASTEXITCODE
$res = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code
exit $code
