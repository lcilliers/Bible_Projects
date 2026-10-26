<#
.SYNOPSIS
    The scope resolver (escalation #2228; occurrence-shaped, #2295): any request -> the collection of
    verses with their occurrences, as a JSON file.

.DESCRIPTION
    Selectors add verses and are combined as a union; -OnlyStrong narrows the result to the verses
    holding one of the given codes. A bare Strong's code is decomposed to its derivatives
    (cfg_behaviour_rule bare-strong-decomposed-to-derivatives). Every verse carries the route that
    brought it in; what does not resolve is listed with its reason. Reads only.

    Each verse lists its occurrences (one verse_lexical row each): an M-coded word with its subgroup,
    cluster, two-sense flag, whether it brought the verse in and whether it is in the home; other
    words as context. A mapped M cluster and a subgroup enter through their (code, surface) pairs; a
    word enters through its surface, never word_strong (cfg_behaviour_rule 119). The home is -Home,
    else the subgroups and M clusters named; a qualifier group or a T cluster is never a home
    (cfg_behaviour_rule 120). A thread item of kind scope gives its stored verses.

      -Cluster M02[,M01]            -Subgroup <subgroup_code>     -Strand <code>      -Word <word>
      -Strong "H0430,G3563G"        -Verse "Psa 10:2; Luk 14:12-14; Rom 8"
      -Chapter 13 [-Section "<heading>"]                         -Claim C-330
      -Observation 12478            -Item OT-108.3                -Thread OT-108
      -Home M18_desire[,M18]        the home (a subgroup or an M cluster), when not the ones named
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
    # -Home is an alias of HomeScope: a variable named Home would be PowerShell's read-only HOME (#2248)
    [string] $Item, [string] $Thread, [Alias('Home')] [string] $HomeScope, [string] $File, [string] $OnlyStrong,
    [string] $Reviewed,
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
                    'Claim', 'Observation', 'Item', 'Thread', 'HomeScope', 'File', 'OnlyStrong', 'Reviewed')) {
    $value = Get-Variable -Name $name -ValueOnly
    $key = if ($name -eq 'HomeScope') { 'Home' } else { $name }   # run.py's parameter is Home
    if ($PSBoundParameters.ContainsKey($name)) { $paramArgs += @('--param', "$key=$value") }
}

Write-IbaRunHeader -WorkPackage 'verse-scope' -Step $stepId -RunId $runId
$json = python -m iba.app.run verse-scope --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code
exit $code
