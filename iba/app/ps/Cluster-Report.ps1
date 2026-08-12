<#
.SYNOPSIS
    Evaluate/review the cluster taxonomy and cluster_strong assignment coverage, scoped to
    strong.origin='word'. Read-only. Built 2026-08-11, replacing an ad hoc script that wrote CSVs
    outside the app's own reporting mechanism.

.DESCRIPTION
    Writes report.cluster_path (default iba/app/reports/cluster.md) + CSV pairing (cluster,
    cluster_strong joined, strong_without_cluster) to report.cluster_path's export/ subfolder.

.PARAMETER RunId  resume/re-tag a specific run.
.PARAMETER Trace  Print every config read (IBA_TRACE).

.EXAMPLE
    .\Cluster-Report.ps1
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

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-CLUSTER-REPORT" }

Write-IbaRunHeader -WorkPackage 'cluster-report' -RunId $runId

$json = python -m iba.app.run cluster-report --step report.cluster --run-id $runId
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'report.cluster' -Path $res.path -Message $res.message -Code $code

exit $code
