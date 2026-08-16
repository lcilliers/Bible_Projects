<#
.SYNOPSIS
    Search the project-wide file manifest (filename/path metadata) — field:value or free-text path
    match.

.DESCRIPTION
    Queries the file_manifest table (built/refreshed by Manifest-Rebuild.ps1) and writes results as
    a one-off report (governance.oneoff_* naming/archiving). Field queries: registry:68,
    type:iba-migration, category:iba, currency:archived, cluster:c17, word:grace, date:2026-08,
    archived:true, ext:.md. Anything else is a free-text substring match against the file path.

.PARAMETER Query  the search term — required.
.PARAMETER RunId  resume/re-tag a specific run.
.PARAMETER Trace  Print every config read (IBA_TRACE).

.EXAMPLE
    iba/app/ps/Manifest-Search.ps1 -Query "type:iba-verse-analysis"
.EXAMPLE
    iba/app/ps/Manifest-Search.ps1 -Query "category:archived"
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string] $Query,
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

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-MANIFEST-SEARCH" }

Write-IbaRunHeader -WorkPackage 'file-manifest-search' -RunId $runId

$json = python -m iba.app.run file-manifest-search --step manifest.search --run-id $runId --param "Query=$Query"
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'manifest.search' -Path $res.path -Message $res.message -Code $code

exit $code
