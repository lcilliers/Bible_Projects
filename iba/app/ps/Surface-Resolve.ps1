<#
.SYNOPSIS
    Module 4 of 5 of the surface cycle: the base of every surface, chosen from the evidence (escalation #2361).

.DESCRIPTION
    Reads the evidence in the tables (surface_derivation from the structure module, ai_call from the AI base step), the structure of
    lib/surfacestructure.py and cfg_setting module resolve; no file is read. For every surface of collection a it decides the base and its
    state: matched_structure, base_ambiguous (the structure found more than one base: left for the AI step or you), matched_sibling,
    ai_answered, ai_none, ai_failed, unmatched (no AI call yet), resolved_own, phrase_not_tested. A base you confirmed is never touched.

      Status   how far the stored bases are from what the evidence decides (read-only)
      Run      write the difference; -Check previews. A second Run with the same evidence changes nothing.
      Show     -Surface <text>   one surface: stored state, decision, evidence rows

.EXAMPLE
    iba\app\ps\Surface-Resolve.ps1 -Action Run -Check
.EXAMPLE
    iba\app\ps\Surface-Resolve.ps1 -Action Show -Surface hides
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('Status', 'Run', 'Show')]
    [string] $Action,
    [string] $Surface,
    [switch] $Check,
    [switch] $Trace
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'
if ($Trace) { $env:IBA_TRACE = '1' }

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot
. $PSScriptRoot\_lib\Notify.ps1

$stepMap = @{ Status = 'resolve.status'; Run = 'resolve.run'; Show = 'resolve.show' }
$stepId = $stepMap[$Action]
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-SURFACERESOLVE"

$paramArgs = @()
if ($PSBoundParameters.ContainsKey('Surface')) { $paramArgs += @('--param', "Surface=$Surface") }
if ($Check) { $paramArgs += @('--param', 'Check=true') }

Write-IbaRunHeader -WorkPackage 'surface-resolve' -Step $stepId -RunId $runId
$json = python -m iba.app.run surface-resolve --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Message $res.message -Code $code
exit $code
