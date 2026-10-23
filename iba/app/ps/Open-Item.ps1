<#
.SYNOPSIS
    Register open items to a clear purpose (escalation #2236).

.DESCRIPTION
    An open item points from the analysis in hand to related work that does not interrupt it. It is
    scoped to specific verses, states what to read for and why it is open, and is cleared at some point.

      Add      -Thread OT-nn -Origin <task/issue id> -Anchor <strong|verse|observation|claim|block>:<value>
               -Source <strong(s)> -TargetCluster Mxx -TargetTerms <strong(s)>   (or -Verse "<refs>")
               -ReadFor "<what to read for>" -Why "<why it is open>" -ComesBackWhen "<the trigger>"
      Reword   -Item OT-nn.n  with the same parameters; the earlier wording goes to the item's history
      Split    -Item OT-nn.n -File <parts.json>   several items, one purpose each, replace one
      Due      -Cluster Mxx    the worded items that come back when that cluster is worked
      Review                   the stragglers report -> open_item.output_dir

    Add and Reword take -File (a JSON list of specs) to register many in one unit; any refusal writes
    nothing. A target over open_item.max_verses (200) is refused: split it. Answering and closing an
    item stay with Escalation.ps1 (or a reading's gate 2). The design is
    outputs/escalation/2236-open-item-design-v2-20261023.md.

.EXAMPLE
    iba\app\ps\Open-Item.ps1 -Action Add -Thread OT-103 -Origin 2172 -Anchor strong:H0639G -Source H0639G -TargetCluster M58 -TargetTerms H7563 -ReadFor "how anger joins the wicked man's ..." -Why "..." -ComesBackWhen "when M58 Wickedness is read"
.EXAMPLE
    iba\app\ps\Open-Item.ps1 -Action Review
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('Add', 'Reword', 'Split', 'Due', 'Review')]
    [string] $Action,
    [string] $Thread, [string] $Item, [string] $Origin, [string] $Anchor, [string] $Source,
    [string] $TargetCluster, [string] $TargetTerms, [string] $Verse, [string] $ReadFor, [string] $Why,
    [string] $ComesBackWhen, [string] $File, [string] $Cluster,
    [ValidateSet('Claude', 'Researcher')] [string] $By,
    [switch] $Trace
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'
if ($Trace) { $env:IBA_TRACE = '1' }

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot
. $PSScriptRoot\_lib\Notify.ps1

$stepId = "open_item.$($Action.ToLower())"
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-OPENITEM"

$paramArgs = @()
foreach ($name in @('Thread', 'Item', 'Origin', 'Anchor', 'Source', 'TargetCluster', 'TargetTerms', 'Verse',
                    'ReadFor', 'Why', 'ComesBackWhen', 'File', 'Cluster', 'By')) {
    $value = Get-Variable -Name $name -ValueOnly
    if ($PSBoundParameters.ContainsKey($name)) { $paramArgs += @('--param', "$name=$value") }
}

Write-IbaRunHeader -WorkPackage 'open-item' -Step $stepId -RunId $runId
$json = python -m iba.app.run open-item --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code
exit $code
