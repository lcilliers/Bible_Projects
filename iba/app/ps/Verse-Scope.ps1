<#
.SYNOPSIS
    The scope resolver (escalation #2228): any request -> the collection of verses, as a JSON file.

.DESCRIPTION
    Selectors add verses and are combined as a union; -OnlyStrong narrows the result to the verses
    holding one of the given codes. A bare Strong's code is decomposed to its derivatives
    (cfg_behaviour_rule bare-strong-decomposed-to-derivatives). Every verse carries the route that
    brought it in; what does not resolve is listed with its reason. Reads only.

      -Cluster M02[,M01]            -Subgroup <subgroup_code>     -Strand <code>      -Word <word>
      -Strong "H0430,G3563G"        -Verse "Psa 10:2; Luk 14:12-14; Rom 8"
      -Chapter 13 [-Section "<heading>"]                         -Claim C-330
      -Observation 12478            -Item OT-108.3                -Thread OT-108
      -File <request.json>          the same keys as lists (a batch or a kept group)
      -OnlyStrong "H3708A"          filter
      -Reviewed "<the review>"      a result over verse_scope.max_verses (2500) is held for review;
                                    given after the researcher's review, it proceeds and is recorded
      -Label <name>                 names the output file

    -> outputs/verse-scope/<label>-<YYYYMMDD>.json (setting verse_scope.output_dir; a same-day
    re-run writes -v2 and archives the earlier file). The design is
    outputs/escalation/2228-scope-resolver-design-v1-20261022.md.

.EXAMPLE
    iba\app\ps\Verse-Scope.ps1 -Label anger-bosom -Cluster M02 -OnlyStrong H3708A
.EXAMPLE
    iba\app\ps\Verse-Scope.ps1 -Label ot108 -Thread OT-108
#>

[CmdletBinding()]
param(
    [string] $Label,
    [string] $Cluster, [string] $Subgroup, [string] $Strand, [string] $Word, [string] $Strong,
    [string] $Verse, [string] $Chapter, [string] $Section, [string] $Claim, [string] $Observation,
    [string] $Item, [string] $Thread, [string] $File, [string] $OnlyStrong, [string] $Reviewed,
    [switch] $Trace
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'
if ($Trace) { $env:IBA_TRACE = '1' }

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot
. $PSScriptRoot\_lib\Notify.ps1

$stepId = 'verse_scope.resolve'
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-VERSESCOPE"

$paramArgs = @()
foreach ($name in @('Label', 'Cluster', 'Subgroup', 'Strand', 'Word', 'Strong', 'Verse', 'Chapter', 'Section',
                    'Claim', 'Observation', 'Item', 'Thread', 'File', 'OnlyStrong', 'Reviewed')) {
    $value = Get-Variable -Name $name -ValueOnly
    if ($PSBoundParameters.ContainsKey($name)) { $paramArgs += @('--param', "$name=$value") }
}

Write-IbaRunHeader -WorkPackage 'verse-scope' -Step $stepId -RunId $runId
$json = python -m iba.app.run verse-scope --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code
exit $code
