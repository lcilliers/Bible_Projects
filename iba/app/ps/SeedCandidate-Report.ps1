<#
.SYNOPSIS
    Whole-seed candidate_seed analysis — counts by decision/layer/role, tag/lemma distribution,
    busiest lemmas, open-vs-resolved over time. Broader than Candidate-Quality.ps1 (which is
    error/exception-focused). Read-only.

.DESCRIPTION
    Writes report.seed_candidate_path (default iba/app/reports/seed-candidate.md) + a CSV pairing
    (candidate_seed joined to lemma_inventory.gloss) to report.seed_candidate_path's export/
    subfolder. First-cut content per PLAN-reports-config-governance-v1-20260722.md §3.1 — expected
    to be expanded once built.

.PARAMETER RunId  resume/re-tag a specific run.
.PARAMETER Trace  Print every config read (IBA_TRACE).

.EXAMPLE
    .\SeedCandidate-Report.ps1
#>

[CmdletBinding()]
param(
    [string] $RunId,
    [switch] $Trace
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'
if ($Trace) { $env:IBA_TRACE = '1' }

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot
. $PSScriptRoot\_lib\Notify.ps1

$ready = python -c "from iba.app.init import _config_loaded, _data_tables_exist; from iba.app.lib.cfg import Cfg; print('1' if (_config_loaded() and _data_tables_exist(Cfg())) else '0')" 2>$null
if ($ready -ne '1') {
    Write-IbaNotInitialised
    exit 1
}

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-SEED-CANDIDATE" }

Write-IbaRunHeader -WorkPackage 'seed-candidate-report' -RunId $runId

$json = python -m iba.app.run seed-candidate-report --step report.seed_candidate --run-id $runId
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'report.seed_candidate' -Path $res.path -Message $res.message -Code $code

exit $code
