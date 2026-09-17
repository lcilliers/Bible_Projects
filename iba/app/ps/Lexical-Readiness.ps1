<#
.SYNOPSIS
    The 3-leg lexical base-data readiness check (#1606, Phase A item 1 of the lexical-stack rebuild,
    escalation #1706/#1711, built 2026-09-16). Standalone, single-step work package, like
    Spine-Check.ps1/Lexicon-Parse.ps1.

.DESCRIPTION
    Read-only. Always persists a report (lexical.readiness_report_path). Leg1: every live verse has
    >=1 live span. Leg2: every live span's strong_variant code resolves to a live `strong` row
    (duplicates spine.check's own desync check deliberately -- #1606's own framing is one cohesive
    3-leg check). Leg3: every live `strong` that actually occurs in a live span has >=1 live
    `cluster_strong` allocation -- the precondition Layer 1's redesigned `role` column (a JSON array
    of cluster_strong.cluster_code) depends on directly. Run this before every Layer 1
    build/rebuild, per governance.base_data_spine's own sibling principle.

.PARAMETER Trace   Print every config read (IBA_TRACE).

.EXAMPLE
    .\Lexical-Readiness.ps1
#>

[CmdletBinding()]
param(
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

$stepId = 'lexical.readiness'
$runId  = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-LEXICAL-READINESS"

Write-IbaRunHeader -WorkPackage 'verse-lexical' -Step $stepId -RunId $runId

$json = python -m iba.app.run verse-lexical --step $stepId --run-id $runId
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code

exit $code
