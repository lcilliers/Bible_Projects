<#
.SYNOPSIS
    Build passages for a book from HIB continuity. Config-governed. Run AFTER HIB identification
    (debate digest Step 1) has populated verse_hib for the book.

.DESCRIPTION
    Runs the 'build-passages' work package over a book: passage.build recomputes the book's
    passages from verse_hib (a passage is a maximal run of consecutive verses tracking the same
    Human Inner Being(s) -- debate-analytic-process-digest-20260805.md Step 2, redefined 2026-08-05
    from the retired char-continuity/candidate-stamp rule). Passages depend on verse_hib, so
    re-run this whenever HIB identification changes for the book.

.PARAMETER Book  OSIS book code, e.g. Dan, Hos, Jon.
.PARAMETER Rule  Boundary rule: hib-continuity (default) or maximal.
.PARAMETER Trace Print every config read (IBA_TRACE).

.EXAMPLE
    .\Build-Passages.ps1 -Book Dan
    .\Build-Passages.ps1 -Book Dan -Rule maximal
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [string] $Book,
    [ValidateSet('hib-continuity', 'maximal')] [string] $Rule = 'hib-continuity',
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

Test-IbaWorkPackageActive -WorkPackage 'build-passages'

$seq   = python -c "import json; from iba.app.lib.cfg import Cfg; c=Cfg(); print(json.dumps([dict(r) for r in c.sequence('build-passages')])); c.close()" | ConvertFrom-Json
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-BUILD-PASSAGES"

Write-IbaRunHeader -WorkPackage 'build-passages' -RunId $runId -RunsOver "book = '$Book'  (rule: $Rule)"

$exitCode = 0
foreach ($entry in $seq) {
    $json = python -m iba.app.run build-passages --step $entry.step --run-id $runId --param "Book=$Book" --param "Rule=$Rule"
    $code = $LASTEXITCODE
    $res  = $json | ConvertFrom-Json
    Write-IbaStepResult -Step $entry.step -Path $res.path -Message $res.message -Code $code
    if ($code -eq 3) { Write-IbaStopped -Message $res.message; $exitCode = 3; break }
    if ($code -eq 2) { Write-IbaPaused -WorkPackage 'build-passages' -RunId $runId -Message $res.message; $exitCode = 2; break }
}

if ($exitCode -eq 0) {
    Write-IbaComplete -WorkPackage 'build-passages' -Vars @{ book = $Book }
}
exit $exitCode
