<#
.SYNOPSIS
    The step before narration: what each surface of a collection does for the inner being (escalation #2406).

.DESCRIPTION
    A surface is assessed in each verse it occurs in, with the role it takes there (a characteristic or a qualifier of an inner-being
    operation, a word that bears on one, or no bearing); the surface-level group follows from the roles and replaces the draft group.
    Claude reads and writes in the session from a working file; the app pulls the file, checks the filled assessment whole and writes it.
    Everything assessed is inferential until you confirm it (B:4).

      Pull     -Collection <name> [-Batch n]   write the working file of one collection (-Batch n: only batch n of the verses, engagement.batch_size items a batch, #2388) (its member surfaces, their verses with the ESV text, and the
                                    observations already on those verses); a view of the tables, never overwritten
      Record   -File <assessment.json> [-Check]   check the filled assessment against its pull, whole, and write it in one transaction;
                                    -Check previews; nothing is written when anything is wrong
      Group    -Collection <name> [-Check]   set the surface-level group of each member surface from its assessments (refused for a surface
                                    not assessed in every verse; a group you confirmed is held); a surface that leaves the study group is
                                    raised as one escalation for the collection, never unlinked
      Review   -Collection <name>   write the review file: the verses where every member surface was assessed with no bearing (ruling B, #2411),
                                    the items still to be read again
      Close    -File <review-assessment.json> [-Check]   check the decisions on a review file (confirm no bearing, or reopen with a role) and write
                                    them in one transaction; a verse is set aside only when all its surfaces are confirmed
      Check    -Collection <name>   a report of every member surface against its verses

.EXAMPLE
    iba\app\ps\Engagement.ps1 -Action Pull -Collection aloud
.EXAMPLE
    iba\app\ps\Engagement.ps1 -Action Record -File _analytics\surfaces\working_files\engagement\engagement-aloud-assess-20261109.json -Check
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('Pull', 'Record', 'Group', 'Review', 'Close', 'Check')]
    [string] $Action,
    [string] $Collection,
    [string] $Batch,
    [string] $File,
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

$stepMap = @{ Pull = 'engagement.pull'; Record = 'engagement.record'; Group = 'engagement.group'; Review = 'engagement.review'; Close = 'engagement.close'; Check = 'engagement.check' }
$stepId = $stepMap[$Action]
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-ENGAGEMENT"

$paramArgs = @()
foreach ($p in @('Collection', 'File', 'Batch')) {
    if ($PSBoundParameters.ContainsKey($p)) { $paramArgs += @('--param', "$p=$($PSBoundParameters[$p])") }
}
if ($Check -and $Action -ne 'Check') { $paramArgs += @('--param', 'Check=true') }

Write-IbaRunHeader -WorkPackage 'engagement' -Step $stepId -RunId $runId
$json = python -m iba.app.run engagement --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Message $res.message -Code $code
exit $code
