<#
.SYNOPSIS
    Report every .md file in the manifest by size, largest first — file name, folder, size — for
    visual review before deciding what to add to cfg_content_index_exclude.

.DESCRIPTION
    Read-only. Run this BEFORE ContentIndex-Rebuild.ps1 if you haven't decided exclusions yet — a
    live finding 2026-08-17 showed some generated dumps (large prose/verse-analysis .md files)
    produce pathological hit density during indexing. No exclusions are applied by this report; it
    shows everything so you can decide.

.PARAMETER RunId  resume/re-tag a specific run.
.PARAMETER Trace  Print every config read (IBA_TRACE).

.EXAMPLE
    .\ContentIndex-SizeProfile.ps1
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

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-CONTENTINDEX-SIZEPROFILE" }

Write-IbaRunHeader -WorkPackage 'content-index-size-profile' -RunId $runId

$json = python -m iba.app.run content-index-size-profile --step content_index.size_profile --run-id $runId
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'content_index.size_profile' -Path $res.path -Message $res.message -Code $code

exit $code
