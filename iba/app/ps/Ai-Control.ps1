<#
.SYNOPSIS
    Control and view of the AI use on zeta-assist: the registers of models and prompts, the calls made (escalation #2361).

.DESCRIPTION
    Every AI call of the project goes through the AI client (lib/aiclient.py): the model is the active one of its role (cfg_ai_model), the prompt is
    the active version of its key (cfg_ai_prompt), the options are within cfg_setting ai.allowed_options, and every attempt is a row in ai_call.

      Status      the registers and the calls by module, step and outcome; -Live also asks the server which models it holds
      Prompts     every version of every prompt, or of -Key
      PromptAdd   -Key -Text -Note [-Role] [-Activate]   a NEW version of a prompt (a version's text never changes); -Activate retires the
                  active version and uses the new one from the next call
      Replay      -Call <ai_call id>   send a stored request again and say whether the answer is the same
      Compare     -Step <step>   per prompt version and model: answered, refused, failed, seconds, tokens

.EXAMPLE
    iba\app\ps\Ai-Control.ps1 -Action Status -Live
.EXAMPLE
    iba\app\ps\Ai-Control.ps1 -Action Compare -Step base
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('Status', 'Prompts', 'PromptAdd', 'Replay', 'Compare')]
    [string] $Action,
    [string] $Key,
    [string] $Text,
    [string] $Note,
    [string] $Role,
    [string] $Call,
    [string] $Step,
    [switch] $Activate,
    [switch] $Live,
    [switch] $Trace
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'
if ($Trace) { $env:IBA_TRACE = '1' }

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot
. $PSScriptRoot\_lib\Notify.ps1

$stepMap = @{ Status = 'ai.status'; Prompts = 'ai.prompts'; PromptAdd = 'ai.prompt_add'; Replay = 'ai.replay'; Compare = 'ai.compare' }
$stepId = $stepMap[$Action]
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-AICONTROL"

$paramArgs = @()
foreach ($p in @('Key', 'Text', 'Note', 'Role', 'Call', 'Step')) {
    if ($PSBoundParameters.ContainsKey($p)) { $paramArgs += @('--param', "$p=$($PSBoundParameters[$p])") }
}
if ($Activate) { $paramArgs += @('--param', 'Activate=true') }
if ($Live) { $paramArgs += @('--param', 'Live=true') }

Write-IbaRunHeader -WorkPackage 'ai-control' -Step $stepId -RunId $runId
$json = python -m iba.app.run ai-control --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Message $res.message -Code $code
exit $code
