<#
.SYNOPSIS
    What is known, and what is missing, for a scope (escalation #2228).

.DESCRIPTION
    Resolves the scope as Verse-Scope.ps1 does (same selectors, same guard), then for every verse in it
    collates its text, its inner-being words, the observations on it, the strand hits, the claims resting
    on it and the blocks telling them, the blocks citing it, the matching open thread items, and the lines
    of the cluster files that name it (only those lines are read); the lexicon once per strong; and the
    gaps per verse. Reads only.

      -Cluster -Subgroup -Strand -Word -Strong -Verse -Chapter [-Section] -Claim -Observation -Item
      -Thread -File -OnlyStrong     the scope, as in Verse-Scope.ps1
      -Reviewed "<the review>"      a scope over verse_scope.max_verses (2500), after the researcher's review
      -Label <name>                 names the output files

    -> verse_collate.output_dir/<label>-<YYYYMMDD>.json (the record) and .md (the summary). The design
    is outputs/escalation/2228-verse-collate-design-v1-20261023.md.

.EXAMPLE
    iba\app\ps\Verse-Collate.ps1 -Label anger-bosom -Cluster M02 -OnlyStrong H3708A
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

$stepId = 'verse_collate.collate'
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-VERSECOLLATE"

$paramArgs = @()
foreach ($name in @('Label', 'Cluster', 'Subgroup', 'Strand', 'Word', 'Strong', 'Verse', 'Chapter', 'Section',
                    'Claim', 'Observation', 'Item', 'Thread', 'File', 'OnlyStrong', 'Reviewed')) {
    $value = Get-Variable -Name $name -ValueOnly
    if ($PSBoundParameters.ContainsKey($name)) { $paramArgs += @('--param', "$name=$value") }
}

Write-IbaRunHeader -WorkPackage 'verse-collate' -Step $stepId -RunId $runId
$json = python -m iba.app.run verse-collate --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code
exit $code
