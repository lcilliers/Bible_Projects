<#
.SYNOPSIS
    Module 1 of 5 of the surface cycle: corrections of the group of a surface (escalation #2361).

.DESCRIPTION
    A word of collection a (behaviour or inner_being_state) can have a base that the judge put in 'being' or 'other', judged alone without the
    sense its derived words show. This step reads the tables (surface_term, the structure of lib/surfacestructure.py, cfg_setting module group);
    no file is read.

      Status    what the rule would do (read-only)
      Repoint   bases whose derived words all agree and are inflections, with the base in an automatic group, are corrected to the group of
                their derived words; other pairs become held_pair flags for you. -Base a,b names proposed bases you accept.
                -Check previews. A second Repoint with the same inputs changes nothing.
      Judge     ask the AI (zeta-assist, through the AI client) for the group of the surfaces not yet judged; -Limit n, -Retry also asks the
                failed ones. One ai_call row per attempt; a long run is started outside the session (B:125).

    Everything is inferential until you confirm it (B:4). After a correction run Surface-Structure.ps1 -Action Match.

.EXAMPLE
    iba\app\ps\Surface-Group.ps1 -Action Repoint -Check
.EXAMPLE
    iba\app\ps\Surface-Group.ps1 -Action Repoint -Base build,redeem
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('Status', 'Repoint', 'Judge')]
    [string] $Action,
    [string] $Base,
    [switch] $Check,
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

$stepMap = @{ Status = 'group.status'; Repoint = 'group.repoint'; Judge = 'group.judge' }
$stepId = $stepMap[$Action]
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-SURFACEGROUP"

$paramArgs = @()
if ($PSBoundParameters.ContainsKey('Base')) { $paramArgs += @('--param', "Base=$Base") }
if ($PSBoundParameters.ContainsKey('Limit')) { $paramArgs += @('--param', "Limit=$Limit") }
if ($Retry) { $paramArgs += @('--param', 'Retry=true') }
if ($Check) { $paramArgs += @('--param', 'Check=true') }

Write-IbaRunHeader -WorkPackage 'surface-group' -Step $stepId -RunId $runId
$json = python -m iba.app.run surface-group --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Message $res.message -Code $code
exit $code
