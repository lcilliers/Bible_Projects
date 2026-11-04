<#
.SYNOPSIS
    The base form of a surface word, asked of the Ollama server (escalation #2359).

.DESCRIPTION
    The list is a JSON file of English words, <surface_judge.batch_dir>/<Batch><surface_judge.base_input_suffix>
    ({"words": [...]}). Each word goes to the server on its own (no verse, no Hebrew or Greek code); the answer is a
    base word and the relation of the word to it: inflection, derivation, or none (no base of the same root
    meaning). Every answer is inferential until the researcher confirms it. Nothing is written to iba.db: the
    answers are appended, one JSON line per word as it finishes, to <surface_judge.batch_dir>/<Batch>.jsonl.

      Status   -Batch <name>   how far the batch file has got against the input list
      Run      -Batch <name> [-Limit n]   ask for the words not yet answered; -Limit stops after n words (a pilot is a
               Run with a small -Limit). Resumable: run it again with the same -Batch and it carries on. A run of
               hours is started outside the Claude session (USER-GUIDE.md section 8.8).

    -Batch is lower-case words joined by hyphens, then -v and a number, then -yyyymmdd.
    The server, the model, the question and the answer shape are cfg_setting rows (modules ollama, surface_judge).

.EXAMPLE
    iba\app\ps\Surface-Base.ps1 -Action Run -Batch base-form-pilot-v1-20261104 -Limit 20
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('Status', 'Run')]
    [string] $Action,
    [Parameter(Mandatory = $true)] [string] $Batch,
    [string] $Limit,
    [switch] $Trace
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'
if ($Trace) { $env:IBA_TRACE = '1' }

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot
. $PSScriptRoot\_lib\Notify.ps1

$stepMap = @{ Status = 'surface_base.status'; Run = 'surface_base.run' }
$stepId = $stepMap[$Action]
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-SURFACEBASE"

$paramArgs = @()
foreach ($p in @('Batch', 'Limit')) {
    if ($PSBoundParameters.ContainsKey($p)) { $paramArgs += @('--param', "$p=$($PSBoundParameters[$p])") }
}

Write-IbaRunHeader -WorkPackage 'surface-base' -Step $stepId -RunId $runId
$json = python -m iba.app.run surface-base --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Message $res.message -Code $code
exit $code
