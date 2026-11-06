<#
.SYNOPSIS
    Module 2 of 5 of the surface cycle: match a surface to a base by the shape of the word (escalation #2361).

.DESCRIPTION
    Reads the surfaces of collection a from surface_term, the construct rules from cfg_base_construct and the thresholds from
    cfg_setting (module structure); no file is read. A surface is matched to a base when removing an ending (sins to sin), restoring an e
    (abased to abase), undoubling a letter (begged to beg) or removing a prefix gives another surface of the list; negating affixes and
    other prefixes are kept as leads, never as bases. Unmatched words get starts-with leads, outside-list bases and sibling groups.
    Everything it finds is evidence about shape, not meaning (B:4): the AI base and the researcher decide the meaning.

      Status   how the structure stands, and how far the evidence rows in surface_derivation are from it (read-only)
      Match    write the difference: new evidence rows added, rows no longer produced set to deleted; -Check previews. A second Match with
               the same inputs changes nothing.
      Show     -Surface <text>   one surface's record and its evidence rows

.EXAMPLE
    iba\app\ps\Surface-Structure.ps1 -Action Match -Check
.EXAMPLE
    iba\app\ps\Surface-Structure.ps1 -Action Show -Surface hides
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('Status', 'Match', 'Show')]
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

$stepMap = @{ Status = 'structure.status'; Match = 'structure.match'; Show = 'structure.show' }
$stepId = $stepMap[$Action]
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-SURFACESTRUCTURE"

$paramArgs = @()
if ($PSBoundParameters.ContainsKey('Surface')) { $paramArgs += @('--param', "Surface=$Surface") }
if ($Check) { $paramArgs += @('--param', 'Check=true') }

Write-IbaRunHeader -WorkPackage 'surface-structure' -Step $stepId -RunId $runId
$json = python -m iba.app.run surface-structure --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Message $res.message -Code $code
exit $code
