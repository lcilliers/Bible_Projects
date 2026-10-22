<#
.SYNOPSIS
    The reading process (escalation #2172): a strand read, recorded, mapped to the claims register
    and written into the narrative, in seven steps. Every step dispatches through run.py, work
    package strand-reading.

.DESCRIPTION
    Claude reads and writes in the session; the app gives everything already known, records the
    results as rows and checks facts. One strand at a time:

      Define   -Strand flesh-body -Title "Flesh and body" -Cluster M48 -Escalation 2162 -Strongs "H1320,G4561"
               (an open strand: -Strand -Strongs adds words)
      Context  -Strand <code>      every hit with its text and lexical data, the observations already
                                   on those words and verses, the open thread items that match, each
                                   verse's coverage -> outputs/strand-reading/<code>/<code>-context-vN.md
      Record   -Strand <code> -File <reading.json>   observations, and a face or a reason per hit read
      Gather   -Strand <code>      every narrative block related to the strand, with its text and tellings
      Map      -Strand <code> -File <map.json>       each related block's statements to the claims register
      Derive   -Strand <code> -File <derive.json>    new, adjusted and withdrawn claims; observation dispositions
      Rewrite  -Strand <code> -File <rewrite.json>   blocks written anew, whole; chapters published
      Account  -Strand <code>      the strand from the tables, gaps as text

    The JSON shapes are in lib/strandreading.py (each step's docstring). Write steps (Define,
    Context, Record, Map, Derive, Rewrite) need -By Claude|Researcher. The strand's escalation cannot
    reach completed or closed while a hit has no face or reason or an observation has no disposition.

.EXAMPLE
    iba\app\ps\Strand-Reading.ps1 -Step Context -Strand flesh-body -By Claude
.EXAMPLE
    iba\app\ps\Strand-Reading.ps1 -Step Record -Strand flesh-body -File "outputs/strand-reading/flesh-body/reading-1.json" -By Claude
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('Define', 'Context', 'Record', 'Gather', 'Map', 'Derive', 'Rewrite', 'Account')]
    [string] $Step,
    [Parameter(Mandatory = $true)] [string] $Strand,
    [ValidateSet('Claude', 'Researcher')] [string] $By,
    [string] $Title, [string] $Cluster, [string] $Escalation, [string] $Strongs, [string] $Note,
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

$stepId = "strand_reading.$($Step.ToLower())"
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-STRANDREAD"

$paramArgs = @()
foreach ($name in @('Strand', 'By', 'Title', 'Cluster', 'Escalation', 'Strongs', 'Note', 'File')) {
    $value = Get-Variable -Name $name -ValueOnly
    if ($PSBoundParameters.ContainsKey($name)) { $paramArgs += @('--param', "$name=$value") }
}

Write-IbaRunHeader -WorkPackage 'strand-reading' -Step $stepId -RunId $runId
$json = python -m iba.app.run strand-reading --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code
exit $code
