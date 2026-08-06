<#
.SYNOPSIS
    Register the debate's own input scope as a passage. Config-governed.

.DESCRIPTION
    Runs the 'build-passages' work package's passage.build step for one book+scope. Redefined
    2026-08-06 (researcher direction, following the HIB-distribution visualization across four
    chapters): a passage is no longer derived by a HIB-continuity algorithm — it IS the given
    scope, verbatim. This step reads the whole scope in light of the HIBs already identified
    (hib.set must have run first for these verses), and requires a JSON payload carrying the
    already-decided reading judgement: a high-level story synthesis, and a self-assessment of
    whether the scope can be read as a whole without quality loss. If not, the step refuses
    outright (no passage row written) with a message to narrow the scope and resubmit.

.PARAMETER Book         OSIS book code, e.g. Dan, Hos, Jon.
.PARAMETER Chapters     Whole-chapter range, e.g. 1-3 or 1. Mutually exclusive with -Range.
.PARAMETER Range        Single-chapter verse range, e.g. 8:1-27. Mutually exclusive with -Chapters.
.PARAMETER PayloadPath  Path to the JSON payload file (story_summary/feasible/feasibility_note,
                        and reconciliation_note if correcting an already-registered scope).
.PARAMETER Trace        Print every config read (IBA_TRACE).

.EXAMPLE
    .\Build-Passages.ps1 -Book Dan -Range 8:1-27 -PayloadPath iba\app\staging\passages\dan-8.json
.EXAMPLE
    .\Build-Passages.ps1 -Book Hos -Chapters 1 -PayloadPath iba\app\staging\passages\hos-1.json
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [string] $Book,
    [string] $Chapters,
    [string] $Range,
    [Parameter(Mandatory = $true)] [string] $PayloadPath,
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

if ([bool]$Chapters -eq [bool]$Range) {
    Write-Host "passage.build needs exactly one of -Chapters or -Range." -ForegroundColor Yellow
    exit 1
}
if (-not (Test-Path $PayloadPath)) {
    Write-Host "PayloadPath '$PayloadPath' does not exist." -ForegroundColor Yellow
    exit 1
}

Test-IbaWorkPackageActive -WorkPackage 'build-passages'

$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-BUILD-PASSAGES"
$scopeLabel = if ($Range) { "$Book $Range" } else { "$Book $Chapters" }
Write-IbaRunHeader -WorkPackage 'build-passages' -RunId $runId -RunsOver "scope = '$scopeLabel'"

$paramArgs = @('--param', "Book=$Book", '--param', "PayloadPath=$PayloadPath")
if ($Chapters) { $paramArgs += @('--param', "Chapters=$Chapters") }
if ($Range)    { $paramArgs += @('--param', "Range=$Range") }

$json = python -m iba.app.run build-passages --step passage.build --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'passage.build' -Path $res.path -Message $res.message -Code $code

if ($code -eq 3) { Write-IbaStopped -Message $res.message }
elseif ($code -eq 2) { Write-IbaPaused -WorkPackage 'build-passages' -RunId $runId -Message $res.message }
else { Write-IbaComplete -WorkPackage 'build-passages' -Vars @{ scope = $scopeLabel } }

exit $code
