<#
.SYNOPSIS
    The reading process (escalation #2228): a reading of one scope through three gates -- recorded,
    synergised, published. Every step dispatches through run.py, work package reading.

.DESCRIPTION
    Claude reads and writes in the session; the app resolves the scope, gives everything already known,
    writes the records as rows and checks each gate from the tables. One reading per scope:

      Open     -Label anger-bosom -Escalation 2172 -Home M02 <scope selectors, as Verse-Scope.ps1>
               the scope resolved (a selection above 2,500 verses is held until -Reviewed), its verses
               kept, the scope collated, and the gap JSON written: one section per gap type, each with
               its guide -> outputs/reading/<label>/<label>-gaps.json (and -collation.json)
      Record   -Label <label> [-File <gap JSON>]   each item's record written: {"new": ...},
               {"table", "id"} or {"reason"}; the ids written back into the file; new open items
               (new_items, the Open-Item.ps1 add shape)
      Check    -Label <label>    gate 1 at state open (every item has an id that exists or a reason;
               the verses are marked analysed), gate 2 at state recorded (every observation carried or
               disposed, every claim told or held, every matched open item settled)
      Synergy  -Label <label>    the synergy JSON, built from the tables for the scope (never memory)
      Apply    -Label <label> [-File <synergy JSON>]   claims, dispositions, tellings, blocks rewritten,
               open items settled or carried forward
      Publish  -Label <label>    the touched chapters published, copied to the learning4comfort inbox
               and checked byte-identical
      Account  -Label <label>    the reading from the tables: its state and the gaps at its gate

    The JSON shapes are in lib/reading.py and in each file's "how". Write steps (all but Account) need
    -By Claude|Researcher. The escalation that anchors a reading cannot reach completed or closed while
    the reading is not published.

.EXAMPLE
    iba\app\ps\Reading.ps1 -Step Open -Label anger-bosom -Escalation 2172 -Home M02 -Strong H2436 -By Claude
.EXAMPLE
    iba\app\ps\Reading.ps1 -Step Record -Label anger-bosom -By Claude
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('Open', 'Record', 'Check', 'Synergy', 'Apply', 'Publish', 'Account')]
    [string] $Step,
    [Parameter(Mandatory = $true)] [string] $Label,
    [ValidateSet('Claude', 'Researcher')] [string] $By,
    [string] $Escalation, [string] $Home, [string] $Note, [string] $File,
    [string] $Cluster, [string] $Subgroup, [string] $Strand, [string] $Word, [string] $Strong,
    [string] $Verse, [string] $Chapter, [string] $Section, [string] $Claim, [string] $Observation,
    [string] $Item, [string] $Thread, [string] $OnlyStrong, [string] $Reviewed,
    [switch] $Trace
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'
if ($Trace) { $env:IBA_TRACE = '1' }

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot
. $PSScriptRoot\_lib\Notify.ps1

$stepId = "reading.$($Step.ToLower())"
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-READING"

$paramArgs = @()
foreach ($name in @('Label', 'By', 'Escalation', 'Home', 'Note', 'File', 'Cluster', 'Subgroup', 'Strand', 'Word',
                    'Strong', 'Verse', 'Chapter', 'Section', 'Claim', 'Observation', 'Item', 'Thread', 'OnlyStrong',
                    'Reviewed')) {
    $value = Get-Variable -Name $name -ValueOnly
    if ($PSBoundParameters.ContainsKey($name)) { $paramArgs += @('--param', "$name=$value") }
}

Write-IbaRunHeader -WorkPackage 'reading' -Step $stepId -RunId $runId
$json = python -m iba.app.run reading --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code
exit $code
