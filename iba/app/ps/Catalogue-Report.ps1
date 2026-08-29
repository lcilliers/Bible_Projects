<#
.SYNOPSIS
    Structural review of `wa_obs_question_catalogue` (bible_research.db) on its own — no findings,
    no joins. Escalation #1007, second half: "evaluate and augment the questions and structure
    around it — all in the one table." Read-only. Built 2026-08-29.

.DESCRIPTION
    Writes report.obs_catalogue_path (default Workflow/Catalogue/obs-catalogue.md — corrected
    2026-08-29, researcher: "iba/app/reports is not an approved or valid destination"). No CSV
    alongside it — a verbatim wa_obs_question_catalogue dump already exists via the governed
    table.export mechanism (table_export.output_dir -> Workflow/schema/bible_research/). Sections:
    overview (status/deleted lifecycle breakdown), lifecycle conflicts (the exact rows where status
    and deleted disagree), naming schemes (section/tier/question_code/catalogue_version/date_added
    inconsistencies), tier structure (the live tiered question set, grouped for review),
    unclassified (live questions with no tier — integration candidates).

.PARAMETER RunId  resume/re-tag a specific run.
.PARAMETER Trace  Print every config read (IBA_TRACE).

.EXAMPLE
    .\Catalogue-Report.ps1
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

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-CATALOGUE-REPORT" }

Write-IbaRunHeader -WorkPackage 'catalogue-report' -RunId $runId

$json = python -m iba.app.run catalogue-report --step report.obs_catalogue --run-id $runId
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'report.obs_catalogue' -Path $res.path -Message $res.message -Code $code

exit $code
