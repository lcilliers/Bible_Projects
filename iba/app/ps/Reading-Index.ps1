<#
.SYNOPSIS
    The cluster reading index (escalation #2228): where the study files name each verse.

.DESCRIPTION
    Build reads the .md files under the folders in reading_index.roots (archive/ folders skipped) and
    records every verse reference with its file, heading section and line (reading_file,
    reading_section, reading_ref). Only new and changed files are read; a build stops between files
    after reading_index.max_seconds and the next build carries on. Report writes the coverage report.

      Build      index new and changed files, mark removed ones
      Report     -> reading_index.output_dir/reading-index-coverage-vN.md

    The design is outputs/escalation/2228-cluster-reading-index-design-v1-20261023.md.

.EXAMPLE
    iba\app\ps\Reading-Index.ps1 -Step Build
.EXAMPLE
    iba\app\ps\Reading-Index.ps1 -Step Report
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('Build', 'Report')]
    [string] $Step,
    [switch] $Trace
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'
if ($Trace) { $env:IBA_TRACE = '1' }

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot
. $PSScriptRoot\_lib\Notify.ps1

$stepId = "reading_index.$($Step.ToLower())"
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-READINDEX"

Write-IbaRunHeader -WorkPackage 'reading-index' -Step $stepId -RunId $runId
$json = python -m iba.app.run reading-index --step $stepId --run-id $runId
$code = $LASTEXITCODE
$res = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code
exit $code
