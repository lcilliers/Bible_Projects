<#
.SYNOPSIS
    The base-data spine check — verse/span/strong sync (FATAL per governance.base_data_spine,
    escalation #1613, researcher ruling 2026-09-10). Standalone, single-step work package, like
    Lexicon-Parse.ps1/Candidate-Quality.ps1.

    The strong-extended-meaning-parse completeness check + its discoverability pass were REMOVED
    2026-09-11 (escalation #1681/#1684/#1686) — they checked coverage against
    strong_meaning_parsed/strong_lsj_parsed/strong_mounce_parsed, which were retired/frozen on
    2026-09-10 and are no longer maintained. See handlers/spine.py module docstring.

.DESCRIPTION
    Read-only. Always persists a report (spine.quality_report_path). If there are FATAL findings,
    escalates ONCE, then pauses. Answer with
    `Escalation.ps1 -Action AnswerRun -RunId <run_id> -Decision <Approve|Reject|Revise|Hold|Noted>`,
    then re-run this script with -RunId <run_id> to act on the answer.

.PARAMETER RunId   resume a specific pending check (reuse the run_id from its first call).
.PARAMETER Trace   Print every config read (IBA_TRACE).

.EXAMPLE
    .\Spine-Check.ps1
.EXAMPLE
    .\Spine-Check.ps1 -RunId RUN-20260910_...-SPINE-CHECK
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

$stepId = 'spine.check'
$runId  = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-SPINE-CHECK" }

Write-IbaRunHeader -WorkPackage 'spine-check' -Step $stepId -RunId $runId

$json = python -m iba.app.run spine-check --step $stepId --run-id $runId
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code

if ($code -eq 2) {
    Write-IbaPaused -WorkPackage 'spine-check' -RunId $runId -Message $res.message
}

exit $code
