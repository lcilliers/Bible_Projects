<#
.SYNOPSIS
    Read-only front door for the operational-behaviour cfg layer (`cfg_behaviour_class` +
    `cfg_behaviour_rule`, escalations #715/#732/#733). Content is written by migrations through
    configmaint, never by this script. Dispatched through run.py (work package `behaviour`, step
    `behaviour.list`, #2207).

.DESCRIPTION
    -Action List [-Class <class>]
        Writes every active rule (optionally scoped to one class) to `behaviour.list_report_path`
        (archived on regenerate) and prints a one-line pointer and count.

.EXAMPLE
    .\Behaviour.ps1 -Action List
.EXAMPLE
    .\Behaviour.ps1 -Action List -Class chat
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('List')]
    [string] $Action,
    [ValidateSet('chat', 'terminal', 'sqlite', 'documentation', 'llm_output', 'development', 'filing', 'study_method')]
    [string] $Class
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot
. $PSScriptRoot\_lib\Notify.ps1

$ready = python -c "from iba.app.init import _config_loaded, _data_tables_exist; from iba.app.lib.cfg import Cfg; print('1' if (_config_loaded() and _data_tables_exist(Cfg())) else '0')" 2>$null
if ($ready -ne '1') {
    Write-IbaNotInitialised
    exit 1
}

$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-BEHAVIOUR"
$paramArgs = @()
if ($Class) { $paramArgs += @('--param', "Class=$Class") }

Write-IbaRunHeader -WorkPackage 'behaviour' -RunId $runId

$json = python -m iba.app.run behaviour --step behaviour.list --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'behaviour.list' -Path $res.path -Message $res.message -Code $code

exit $code
