<#
.SYNOPSIS
    The base form of a surface word, asked of the AI through the AI client (escalation #2359, #2361).

.DESCRIPTION
    Module 3 of 5 of the surface cycle. For the surfaces the resolve module leaves unmatched (the shape of the word found no base), the AI is asked
    on its own for the base word and its relation: inflection, derivation, or none (no base of the same root meaning). Each word goes to zeta-assist
    on its own (no verse, no Hebrew or Greek code); every attempt is a row in ai_call. Every answer is inferential until you confirm it. Reads and
    writes tables only. Then run Surface-Resolve.ps1 -Action Run, which reads the answers and decides the bases.

      Ask   [-Limit n] [-Retry]   ask for the words waiting; -Limit stops after n words (a pilot is Ask with a small -Limit); -Retry also asks
            the words that failed. A run of hours is started outside the Claude session (USER-GUIDE.md section 8.8, B:125).

    The earlier file route (-Action Status and Run with a batch file) was retired in stage 6 of escalation #2361.
    The server, the model, the prompt (base.word) and the answer shape are in the registers and cfg_setting modules ollama, ai and surface_judge.

.EXAMPLE
    iba\app\ps\Surface-Base.ps1 -Action Ask -Limit 20
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('Ask')]
    [string] $Action,
    [string] $Limit,
    [switch] $Retry,
    [switch] $Trace
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'
if ($Trace) { $env:IBA_TRACE = '1' }

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot
. $PSScriptRoot\_lib\Notify.ps1

$stepId = 'surface_base.ask'
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-SURFACEBASE"

$paramArgs = @()
if ($PSBoundParameters.ContainsKey('Limit')) { $paramArgs += @('--param', "Limit=$Limit") }
if ($Retry) { $paramArgs += @('--param', 'Retry=true') }

Write-IbaRunHeader -WorkPackage 'surface-base' -Step $stepId -RunId $runId
$json = python -m iba.app.run surface-base --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Message $res.message -Code $code
exit $code
