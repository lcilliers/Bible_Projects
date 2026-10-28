<#
.SYNOPSIS
    The reading process (escalations #2228, #2273): a reading of one scope with its objective, on the
    phases of the analytic process, through four gates -- pre, observe, claims, narrate -- then published.
    Every step dispatches through run.py, work package reading.

.DESCRIPTION
    Claude reads and writes in the session; the app resolves the scope, gives everything already known for a verse when the
    verse is worked, writes the findings as rows (one observation per finding, applied by its nodes) and checks each gate.
    One reading per scope. Analysis_phase_1 (the verse understanding, #2320) is steps 1 to 3:

      Open     -Label m21-asking -Escalation 2320 -Objective "..." -Subgroup M21_asking [-Surface asks,asked | -Verse "Mat 7:8"]
               0.C: ONE subgroup, or a segment of it; the home is the subgroup. Writes <the home cluster's folder under _analytics/Clusters>/<label>/<label>.json,
               the index of the verses (reference, route, progress). No observation is written.
      Observe  -Label <label> [-Count n] [-Verse ref]   the next verses in hand: each verse's sheet is read from the tables
               NOW (surfaces, existing observations and nodes, ledger faces) and set in the JSON to be filled
      Record   -Label <label>   the filled sheets checked whole, then written in one transaction: each surface evaluated
               (kept in the JSON), each existing observation and node accepted, modified in place or soft deleted, new
               findings written; the verses become done
      Check    -Label <label>   the gate the reading is at. At open: the Observe gate (every verse done, the evaluations agree
               with the live nodes); open -> observed; the verses marked analysed
      (Gather is retired: its pull is the first move on each verse in Observe.)

    The claims steps are unchanged:
      Synergy  -Label <label>    the synergy JSON, built from the tables (never memory)
      Apply    -Label <label> [-File <synergy JSON>]   claims, each node's disposition, open items settled
      Narrate  -Label <label> [-File <narrate JSON>]   tellings, holds, blocks rewritten; nodes told
      Publish  -Label <label>    the touched chapters published, copied to the learning4comfort inbox
      Account  -Label <label>    the reading from the tables: its state and the gaps at its gate

    The JSON shapes are in lib/reading.py and lib/observationrecord.py and each file's "how". Write steps (all but Account)
    need -By Claude|Researcher.

.EXAMPLE
    iba\app\ps\Reading.ps1 -Step Open -Label m21-asking -Escalation 2320 -Objective "the asking words in their verses" -Subgroup M21_asking -By Claude
.EXAMPLE
    iba\app\ps\Reading.ps1 -Step Record -Label m21-asking -By Claude
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('Open', 'Observe', 'Record', 'Check', 'Synergy', 'Apply', 'Narrate', 'Publish', 'Account')]
    [string] $Step,
    [Parameter(Mandatory = $true)] [string] $Label,
    [ValidateSet('Claude', 'Researcher')] [string] $By,
    # -Home is an alias of HomeCluster: a variable named Home would be PowerShell's read-only HOME (#2248)
    [string] $Escalation, [Alias('Home')] [string] $HomeCluster, [string] $Objective, [string] $Note, [string] $File,
    [string] $Cluster, [string] $Subgroup, [string] $Strand, [string] $Word, [string] $Strong,
    [string] $Verse, [string] $Chapter, [string] $Section, [string] $Claim, [string] $Observation,
    [string] $Item, [string] $Thread, [string] $OnlyStrong, [string] $Reviewed, [string] $Surface, [string] $Count,
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
                    'Reviewed', 'Surface', 'Count')) {
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
