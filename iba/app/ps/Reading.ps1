<#
.SYNOPSIS
    The reading process (escalations #2228, #2273): a reading of one scope with its objective, on the
    phases of the analytic process, through four gates -- pre, observe, claims, narrate -- then published.
    Every step dispatches through run.py, work package reading.

.DESCRIPTION
    Claude reads and writes in the session; the app resolves the scope, gives everything already known,
    writes the findings as rows (one observation per finding, applied by its nodes) and checks each gate
    from the tables. One reading per scope:

      Open     -Label anger-bosom -Escalation 2172 -Home M02 -Objective "..." <scope selectors, as
               Verse-Scope.ps1>   0.C: the scope resolved (above 2,500 verses held until -Reviewed), its
               verses kept, the scope collated, and the pre-gap JSON written, one section per gap type of
               phase pre -> outputs/reading/<label>/<label>-gaps.json (and -collation.json)
      Gather   -Label <label> [-File <pre-gap JSON>]   0.GAP pre written: each item's record ({"finding"},
               {"table", "id"}, {"reason"}, a face, a response), new open items; ids written back
      Observe  -Label <label>    the observe JSON built from the tables: per verse its passage, every finding
               applied to it, the words in focus (qualifiers included), the claims, the prompts by kind
      Record   -Label <label> [-File <observe JSON>]   the findings written (a live description gains
               nodes), withdrawals with their reasons, each word's open item or reason
      Check    -Label <label>    the gate the reading is at: pre (open -> gathered), observe (gathered ->
               observed: every word in focus has a node of this reading, an open item or a reason; the
               verses are marked analysed), claims (observed -> synergised: every node disposed, every
               claim resting on a finding, every matched open item settled; the narrate JSON built), narrate
               (synergised -> narrated: every claim told or held, every cited verse recorded)
      Synergy  -Label <label>    the synergy JSON, built from the tables (never memory)
      Apply    -Label <label> [-File <synergy JSON>]   claims, each node's disposition, open items settled
      Narrate  -Label <label> [-File <narrate JSON>]   tellings, holds, blocks rewritten; nodes told
      Publish  -Label <label>    the touched chapters published, copied to the learning4comfort inbox
               and checked byte-identical
      Account  -Label <label>    the reading from the tables: its state and the gaps at its gate

    The JSON shapes are in lib/reading.py, lib/observationrecord.py and each file's "how". Write steps
    (all but Account) need -By Claude|Researcher. The escalation that anchors a reading cannot reach
    completed or closed while the reading is not published.

.EXAMPLE
    iba\app\ps\Reading.ps1 -Step Open -Label anger-bosom -Escalation 2172 -Home M02 -Objective "what the bosom shows of anger" -Strong H2436 -By Claude
.EXAMPLE
    iba\app\ps\Reading.ps1 -Step Record -Label anger-bosom -By Claude
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('Open', 'Gather', 'Observe', 'Record', 'Check', 'Synergy', 'Apply', 'Narrate', 'Publish', 'Account')]
    [string] $Step,
    [Parameter(Mandatory = $true)] [string] $Label,
    [ValidateSet('Claude', 'Researcher')] [string] $By,
    # -Home is an alias of HomeCluster: a variable named Home would be PowerShell's read-only HOME (#2248)
    [string] $Escalation, [Alias('Home')] [string] $HomeCluster, [string] $Objective, [string] $Note, [string] $File,
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
foreach ($name in @('Label', 'By', 'Escalation', 'HomeCluster', 'Objective', 'Note', 'File', 'Cluster', 'Subgroup', 'Strand', 'Word',
                    'Strong', 'Verse', 'Chapter', 'Section', 'Claim', 'Observation', 'Item', 'Thread', 'OnlyStrong',
                    'Reviewed')) {
    $value = Get-Variable -Name $name -ValueOnly
    $key = if ($name -eq 'HomeCluster') { 'Home' } else { $name }   # run.py's parameter stays Home
    if ($PSBoundParameters.ContainsKey($name)) { $paramArgs += @('--param', "$key=$value") }
}

Write-IbaRunHeader -WorkPackage 'reading' -Step $stepId -RunId $runId
$json = python -m iba.app.run reading --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code
exit $code
