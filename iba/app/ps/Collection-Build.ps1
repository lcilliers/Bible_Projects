<#
.SYNOPSIS
    Module 5 of 5 of the surface cycle: the members of each collection, decided from the AI judgements (escalation #2361).

.DESCRIPTION
    A collection has a core word. The AI judged each candidate word against it (synonym, opposite or distinct), and the words that are neither
    for association by meaning. This step turns those judgements in the tables into the members of each collection: core, synonym, opposite,
    possible_opposite (a lead, never a member), set_aside and associated. Reads and writes tables only; no file is an input.

      Status    how the stored members stand against what the judgements decide (read-only)
      Links     write the difference; -Check previews. A pair whose link was removed is not linked again. A second Links changes nothing.
      Show      -Collection <name>   one collection with its members by tier
      Export    a CSV of the collections to the exports folder (a view of the tables)
      ExportMembers   a CSV of the member surfaces of the collections, one row for each verse, cluster and tier, with the verse text (the #2379 members-verses view)
      ExportSurfaces  a CSV of the surfaces of the behaviour and inner-being-state groups, one row for each verse and cluster, with the collection and tier (the #2379 surfaces view)
                The three exports take no name: the file name is cfg_setting collection.export_names and the version is the next one by the filing rule;
                the previous live version is moved to the archive folder (#2413).
      Set       -Collection <name> -Status indicative|confirmed|retired -Reason <text>   on your instruction
      Merge     -From <name> -Into <name> -Reason <text>   fold one collection into another, on your instruction
      Gather    -Name <name> -Surface <a,b,c> -Reason <text> [-Check]   one collection of the surfaces you name, tier gathered, without the AI; for words in no collection
                that you want assessed together (#2388)
      Seed      -Word <word>   make a collection of a core word: the AI names its pole (a real word? reciprocal?) and lists synonyms and opposites
      Ask       -Collection <name> [-Limit n]   judge the candidates (the words nearest the core by embedding, and the listed words) through the
                AI client; then run Links. A run of more than a few minutes is started outside the session (B:125).

    Everything is inferential until you confirm it (B:4).

.EXAMPLE
    iba\app\ps\Collection-Build.ps1 -Action Links -Check
.EXAMPLE
    iba\app\ps\Collection-Build.ps1 -Action Show -Collection love
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('Status', 'Links', 'Show', 'Export', 'ExportMembers', 'ExportSurfaces', 'Set', 'Merge', 'Seed', 'Ask', 'Gather')]
    [string] $Action,
    [string] $Collection,
    [string] $Word,
    [string] $Name,
    [string] $Surface,
    [string] $Limit,
    [string] $Status,
    [string] $Reason,
    [string] $From,
    [string] $Into,
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

$stepMap = @{ Status = 'collection.status'; Links = 'collection.links'; Show = 'collection.show'; Export = 'collection.export'; ExportMembers = 'collection.export_members'; ExportSurfaces = 'collection.export_surfaces'; Set = 'collection.set'; Merge = 'collection.merge'; Seed = 'collection.seed'; Ask = 'collection.ask'; Gather = 'collection.gather' }
$stepId = $stepMap[$Action]
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-COLLECTIONBUILD"

$paramArgs = @()
foreach ($p in @('Collection', 'Word', 'Name', 'Surface', 'Limit', 'Status', 'Reason', 'From', 'Into')) {
    if ($PSBoundParameters.ContainsKey($p)) { $paramArgs += @('--param', "$p=$($PSBoundParameters[$p])") }
}
if ($Check) { $paramArgs += @('--param', 'Check=true') }

Write-IbaRunHeader -WorkPackage 'collection-build' -Step $stepId -RunId $runId
$json = python -m iba.app.run collection-build --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Message $res.message -Code $code
exit $code
