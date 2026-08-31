<#
.SYNOPSIS
    bible_research.db's own data-schema snapshot — every table, columns, types, PK/FK, indexes,
    row counts. Read-only. Introspects the live DB directly, no separately-maintained register.
    The bible_research.db counterpart to SchemaOverview-Report.ps1 (the IBA-side equivalent) —
    escalation #1306, 2026-08-31.

.DESCRIPTION
    Writes report.schema_overview_bible_research_path (default
    workflow/schema/schema-overview-bible-research.md -- a sibling of report.schema_overview_path's
    own workflow/schema/schema-overview.md, NOT inside workflow/schema/bible_research/, which is
    table_export.output_dir's CSV-dump folder, a different purpose entirely). No curated table
    allowlist -- shows every
    real table in bible_research.db (no cfg_*-style config/data split there to filter). For
    per-column descriptions and data profiles, see iba/config/DBSchema/DBSchema.json
    (iba/scripts/build_dbschema.py --db bible_research) -- that stays the separate, heavier,
    profiled register; this is the lightweight, always-current structural report.

.PARAMETER RunId  resume/re-tag a specific run.
.PARAMETER Trace  Print every config read (IBA_TRACE).

.EXAMPLE
    .\SchemaOverview-BibleResearch-Report.ps1
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

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-SCHEMA-OVERVIEW-BR" }

Write-IbaRunHeader -WorkPackage 'schema-overview-report-bible-research' -RunId $runId

$json = python -m iba.app.run schema-overview-report-bible-research --step report.schema_overview_bible_research --run-id $runId
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'report.schema_overview_bible_research' -Path $res.path -Message $res.message -Code $code

exit $code
