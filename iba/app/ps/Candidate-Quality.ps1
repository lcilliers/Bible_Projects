<#
.SYNOPSIS
    Standalone quality check for span_candidate — candidate_tag null/format, lemma_key/strong
    resolution. NOT part of Set-Candidates.ps1's seed/set sequence (deliberately — see
    handlers/candidate.py:validate's docstring): run this on demand, not on every book build.

.DESCRIPTION
    Read-only. If findings exist, escalates ONCE with a summary + samples, then pauses. Answer
    with `Escalation.ps1 -Action AnswerRun -RunId <run_id> -Decision <Approve|Reject|Revise>`,
    then re-run this script with -RunId to act on the answer.

.PARAMETER RunId  resume a specific pending check (reuse the run_id from its first call).
.PARAMETER Trace  Print every config read (IBA_TRACE).

.EXAMPLE
    .\Candidate-Quality.ps1
.EXAMPLE
    .\Candidate-Quality.ps1 -RunId RUN-20260721_...-CANDIDATE-QUALITY
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

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-CANDIDATE-QUALITY" }

Write-IbaRunHeader -WorkPackage 'candidate-quality' -RunId $runId

$json = python -m iba.app.run candidate-quality --step candidate.validate --run-id $runId
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'candidate.validate' -Path $res.path -Message $res.message -Code $code

if ($code -eq 2) {
    Write-IbaPaused -WorkPackage 'candidate-quality' -RunId $runId -Message $res.message
}

exit $code
