<#
.SYNOPSIS
    Meaning-parse layer coverage — strong/strong_sense/strong_meaning_tree/strong_lexicon gap
    list, sense-count distribution, lexicon completeness. Read-only.

.DESCRIPTION
    Writes report.strong_meaning_path (default iba/app/reports/strong-meaning.md) + a CSV pairing
    (strong_sense, strong_meaning_tree, both joined to strong.stepGloss) to its export/ subfolder.
    First-cut content per PLAN-reports-config-governance-v1-20260722.md §3.2 — expected to be
    expanded once built.

.PARAMETER RunId  resume/re-tag a specific run.
.PARAMETER Trace  Print every config read (IBA_TRACE).

.EXAMPLE
    .\StrongMeaning-Report.ps1
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

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-STRONG-MEANING" }

Write-IbaRunHeader -WorkPackage 'strong-meaning-report' -RunId $runId

$json = python -m iba.app.run strong-meaning-report --step report.strong_meaning --run-id $runId
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'report.strong_meaning' -Path $res.path -Message $res.message -Code $code

exit $code
