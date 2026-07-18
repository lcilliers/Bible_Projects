<#
.SYNOPSIS
    Build passages for a book from the candidate stamp. Config-governed. Run AFTER Set-Candidates.

.DESCRIPTION
    Runs the 'build-passages' work package over a book: passage.build recomputes the book's
    passages from span_candidate (a passage extends a char's context to adjacent verses).
    Passages depend on the candidate stamp, so re-run this whenever the candidates change.

.PARAMETER Book  OSIS book code, e.g. Prov, Ps, Gen.
.PARAMETER Rule  Boundary rule: char-continuity (default) or maximal.
.PARAMETER Trace Print every config read (IBA_TRACE).

.EXAMPLE
    .\Build-Passages.ps1 -Book Prov
    .\Build-Passages.ps1 -Book Ps -Rule maximal
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [string] $Book,
    [ValidateSet('char-continuity', 'maximal')] [string] $Rule = 'char-continuity',
    [switch] $Trace
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'
if ($Trace) { $env:IBA_TRACE = '1' }

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot

$ready = python -c "from iba.app.init import _config_loaded, _data_tables_exist; from iba.app.lib.cfg import Cfg; print('1' if (_config_loaded() and _data_tables_exist(Cfg())) else '0')" 2>$null
if ($ready -ne '1') {
    Write-Host "The app is not initialised. Run first:  iba\app\ps\Start-Iba.ps1" -ForegroundColor Yellow
    exit 1
}

$seq   = python -c "import json; from iba.app.lib.cfg import Cfg; c=Cfg(); print(json.dumps([dict(r) for r in c.sequence('build-passages')])); c.close()" | ConvertFrom-Json
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-BUILD-PASSAGES"

Write-Host ""
Write-Host "work package : build-passages"
Write-Host "run_id       : $runId"
Write-Host "runs over    : book = '$Book'  (rule: $Rule)"
Write-Host ""

$exitCode = 0
foreach ($entry in $seq) {
    $json = python -m iba.app.run build-passages --step $entry.step --run-id $runId --param "Book=$Book" --param "Rule=$Rule"
    $code = $LASTEXITCODE
    $res  = $json | ConvertFrom-Json
    $colour = @{ 0 = 'Green'; 2 = 'Yellow'; 3 = 'Red' }[$code]
    Write-Host ("  {0,-16} {1,-14} {2}" -f $entry.step, $res.path, $res.message) -ForegroundColor $colour
    if ($code -eq 3) { Write-Host "`nSTOPPED — $($res.message)" -ForegroundColor Red; $exitCode = 3; break }
    if ($code -eq 2) { Write-Host "`nPAUSED — $($res.message)" -ForegroundColor Yellow; $exitCode = 2; break }
}

Write-Host ""
if ($exitCode -eq 0) {
    Write-Host "COMPLETE — passages built for '$Book'." -ForegroundColor Green
}
exit $exitCode
