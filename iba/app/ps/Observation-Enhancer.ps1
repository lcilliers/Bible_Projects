<#
.SYNOPSIS
    The observation_enhancer utility (escalation #1778) -- applies a researcher-confirmed rule to
    `ib_observation`, without re-running the LLM pipeline.

.DESCRIPTION
    Rules live in `cfg_observation_enhancer_rule`, added/edited via the standard
    `Config-Maintenance.ps1 -Step Propose` cycle (a rule is just another cfg_* row -- there is no
    separate add/confirm command here). Each rule pairs a `selector_sql` (a SELECT identifying
    target ib_observation rows) with an `update_json` (the field(s) to change and to what).

    -Action Preview   read-only. Runs the rule's selector_sql against live data and shows the
                       match count, a sample of matched rows, and the update that would be
                       applied. Works on a rule in any status.
    -Action Apply      refuses unless the rule's own status is 'confirmed' or 'active' -- the
                       per-rule confirmation gate: run -Action Preview, look at the real matches,
                       THEN confirm via Config-Maintenance.ps1 -Step Propose -Table
                       cfg_observation_enhancer_rule -Op update -Where '{"rule_key":"..."}' -Set
                       '{"status":"confirmed"}', THEN apply. A first-time confirmed rule is
                       promoted to 'active' automatically on a successful apply. Every field
                       actually changed is logged to `ib_observation_enhancer_log`.

.PARAMETER Action   Preview | Apply
.PARAMETER RuleKey  the cfg_observation_enhancer_rule.rule_key to run
.PARAMETER RunId    resume a specific run (reuse the run_id from its first call).
.PARAMETER Trace    Print every config read (IBA_TRACE).

.EXAMPLE
    .\Observation-Enhancer.ps1 -Action Preview -RuleKey 1769-placeholder-filler
.EXAMPLE
    .\Observation-Enhancer.ps1 -Action Apply -RuleKey 1769-placeholder-filler
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [ValidateSet('Preview', 'Apply')] [string] $Action,
    [Parameter(Mandatory = $true)] [string] $RuleKey,
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

$stepId = if ($Action -eq 'Preview') { 'observation_enhancer.preview' } else { 'observation_enhancer.apply' }
$runId  = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-OBSERVATION-ENHANCER" }

Write-IbaRunHeader -WorkPackage 'observation-enhancer' -Step $stepId -RunId $runId

$json = python -m iba.app.run observation-enhancer --step $stepId --run-id $runId --param "RuleKey=$RuleKey"
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code

if ($code -eq 2) {
    Write-IbaPaused -WorkPackage 'observation-enhancer' -RunId $runId -Message $res.message
}

exit $code
