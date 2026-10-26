<#
.SYNOPSIS
    The capture of prior study documents into the observation record (escalation #2305; design
    outputs/escalation/2305-prior-work-capture-design-v2-20261026.md; method rules CP-01 to CP-10).

.DESCRIPTION
    A migration, not part of the standard analytic process. Per document, in a chat session on the Sonnet model:

      Prepare -File <document>   the document's JSON: every line that names a verse, the verses resolved, the
                                 M- and T-coded words of each verse, the October ids already recorded. Reads only.
              (Claude reads the document and fills "findings" and the "answer" of every line)
      Record  -File <JSON>       checks the filled JSON and writes it whole, or refuses it whole: the observations
                                 (stage prior-capture), their nodes, the answer to every line, the document's
                                 capture_status. Writes a report of the run.
      Report                     where the capture stands: documents by status, observations by tag, line answers.
                                 Reads only.

    <document> is the repo-relative path of a study document in the reading index (reading_file), or its id.
    Files go to prior_capture.output_dir (outputs/prior-capture), versioned per day.

.EXAMPLE
    iba\app\ps\Prior-Capture.ps1 -Step Prepare -File "_analytics/Clusters/M18 - desire-longing/m18-group-D-reading-v1-20261009.md"
.EXAMPLE
    iba\app\ps\Prior-Capture.ps1 -Step Record -File outputs\prior-capture\capture-086-20261026.json
.EXAMPLE
    iba\app\ps\Prior-Capture.ps1 -Step Report
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [ValidateSet('Prepare', 'Record', 'Report')] [string] $Step,
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

$stepId = @{ Prepare = 'prior_capture.prepare'; Record = 'prior_capture.record'; Report = 'prior_capture.report' }[$Step]
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-PRIORCAPTURE"

$paramArgs = @()
if ($File) { $paramArgs += @('--param', "File=$File") }

Write-IbaRunHeader -WorkPackage 'prior-capture' -Step $stepId -RunId $runId
$json = python -m iba.app.run prior-capture --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code
exit $code
