<#
.SYNOPSIS
    Validated partial UPDATE of one `wa_obs_question_catalogue` row (bible_research.db), keyed by
    obs_id. Escalation #1007, researcher instruction 2026-08-31. No history/audit table by design —
    researcher's own call: "I dont think there is any history control on this table and I don't
    think it is necessary."

.DESCRIPTION
    Every column except obs_id is settable via -Set (a JSON object of column:value pairs); a
    column not named in -Set is left untouched. Two columns auto-fill when you don't name them —
    still overridable by naming them explicitly:
      - last_modified    -> now (UTC, ISO-8601)
      - catalogue_version -> "v2-<today>" (a judgment-call default; the column's live data has 6
                              different conventions with no single correct answer — override freely)
    Rejects: an unknown column name, obs_id present in -Set (it's the key, not settable), or a
    nonexistent obs_id.

.PARAMETER ObsId  REQUIRED. The wa_obs_question_catalogue row to update.
.PARAMETER Set    REQUIRED. JSON object of column:value pairs, e.g. '{"source":"verse_lexical.resolved_sense"}'
.PARAMETER RunId  resume/re-tag a specific run.
.PARAMETER Trace  Print every config read (IBA_TRACE).

.EXAMPLE
    .\Catalogue-Update.ps1 -ObsId 224 -Set '{"source":"verse.text + verse_lexical.resolved_sense (Partial)"}'

.EXAMPLE
    .\Catalogue-Update.ps1 -ObsId 224 -Set '{"review_note":"corrected 2026-09-01","catalogue_version":"v2.2"}'
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [int] $ObsId,
    [Parameter(Mandatory = $true)] [string] $Set,
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

$resolvedRunId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-CATALOGUE-UPDATE" }

Write-IbaRunHeader -WorkPackage 'catalogue-update' -Step 'obs_catalogue.update' -RunId $resolvedRunId

$json = python -m iba.app.run catalogue-update --step obs_catalogue.update --run-id $resolvedRunId --param "ObsId=$ObsId" --param "Set=$Set"
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'obs_catalogue.update' -Path $res.path -Message $res.message -Code $code

exit $code
