<#
.SYNOPSIS
    The relations between the single-word surfaces, linked by WordNet 3.0, held in iba.db (escalation #2548).

.DESCRIPTION
    An outside source (WordNet, through NLTK) links the single-word surfaces of the relation study; the scope of the study, the pair types and
    weight and the WordNet folder are cfg_setting rows (surfaces.relation_scope, surfaces.relation_pair_rules, surfaces.wordnet_data_dir).
    WordNet is modern general English: its links are candidate relations to read, not study findings. Nothing is written to surface_term.

      Status     how far the stored pairs, groups and flags are from what WordNet gives (read-only)
      Load       write the pairs into surface_relation; a changed pair or a pair no longer linked is flipped to deleted; -Check previews
      Groups     write the connected groups of the live pairs into surface_network_group; the earlier grouping is kept (deleted); -Check previews
      Flag       -File <workbook>   one surface_flag (kind wordnet_no_pair) for each surface of the reviewed list; the list must be exactly the
                 surfaces with no pair; -Escalation <id> (default 2545); -Check previews
      Validate   compare the WordNet same_base pairs and groups with surface_term.base_id; writes a report under the exports folder, nothing to base_id

    Run Load, then Groups, then Flag. A second run with nothing changed writes nothing.

.EXAMPLE
    iba\app\ps\Surface-Relation.ps1 -Action Load -Check
.EXAMPLE
    iba\app\ps\Surface-Relation.ps1 -Action Flag -File _analytics/surfaces/exports/wordnet-no-pair-review-v2-20261123.xlsx -Check
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('Status', 'Load', 'Groups', 'Flag', 'Validate')]
    [string] $Action,
    [string] $File,
    [string] $Escalation,
    [switch] $Check,
    [switch] $Trace
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'
if ($Trace) { $env:IBA_TRACE = '1' }

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot
. $PSScriptRoot\_lib\Notify.ps1

$stepMap = @{ Status = 'relation.status'; Load = 'relation.load'; Groups = 'relation.groups'; Flag = 'relation.flag'; Validate = 'relation.validate' }
$stepId = $stepMap[$Action]
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-SURFACERELATION"

$paramArgs = @()
if ($PSBoundParameters.ContainsKey('File')) { $paramArgs += @('--param', "File=$File") }
if ($PSBoundParameters.ContainsKey('Escalation')) { $paramArgs += @('--param', "Escalation=$Escalation") }
if ($Check) { $paramArgs += @('--param', 'Check=true') }

Write-IbaRunHeader -WorkPackage 'surface-relation' -Step $stepId -RunId $runId
$json = python -m iba.app.run surface-relation --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Message $res.message -Code $code
exit $code
