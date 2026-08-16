<#
.SYNOPSIS
    Lexicon-parsed layer (L2b) — parse strong_meaning_tree/strong_lexicon into strong_meaning_
    parsed/strong_lsj_parsed/strong_mounce_parsed, fetch STEP's relatedNos into strong_related, and
    check both for coverage/value-quality. Standalone work package (each step invoked
    independently), like Config-Maintenance.ps1/Candidate-Quality.ps1/Passage-Quality.ps1.

.DESCRIPTION
    -Step Parse     strong_meaning_tree + strong_lexicon -> the 3 parsed tables. No network,
                    deterministic, safe to re-run (clears and rebuilds).
    -Step Related   strong -> strong_related, one live STEP getInfo call per row. Can take a
                    couple of minutes over the full strong table.
    -Step Validate  read-only coverage + value-quality check. If there are findings, escalates
                    ONCE, then pauses. Answer with
                    `Escalation.ps1 -Action AnswerRun -RunId <run_id> -Decision <Approve|Reject|Revise|Hold|Noted>`,
                    then re-run this script with -Step Validate -RunId <run_id> to act on the answer.

.PARAMETER Step   Parse | Related | Validate
.PARAMETER RunId  resume a specific pending check (reuse the run_id from its first call).
.PARAMETER Trace  Print every config read (IBA_TRACE).

.EXAMPLE
    .\Lexicon-Parse.ps1 -Step Parse
.EXAMPLE
    .\Lexicon-Parse.ps1 -Step Related
.EXAMPLE
    .\Lexicon-Parse.ps1 -Step Validate
.EXAMPLE
    .\Lexicon-Parse.ps1 -Step Validate -RunId RUN-20260725_...-LEXICON-PARSE
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [ValidateSet('Parse', 'Related', 'Validate')] [string] $Step,
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

$stepId = @{ Parse = 'lexicon.parse'; Related = 'lexicon.related'; Validate = 'lexicon.validate' }[$Step]
$runId  = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-LEXICON-PARSE" }

Write-IbaRunHeader -WorkPackage 'lexicon-parse' -Step $stepId -RunId $runId

$json = python -m iba.app.run lexicon-parse --step $stepId --run-id $runId
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code

if ($code -eq 2) {
    Write-IbaPaused -WorkPackage 'lexicon-parse' -RunId $runId -Message $res.message
}

exit $code
