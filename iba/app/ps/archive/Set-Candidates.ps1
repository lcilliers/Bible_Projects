<#
.SYNOPSIS
    Seed + stamp candidate characteristics (span L4b) for a book. Config-governed.

.DESCRIPTION
    Runs the 'set-candidates' work package over a book: candidate.seed refreshes the
    independent candidate_seed assessment (and the registry-completeness double-control),
    then candidate.set stamps span_candidate on the book's spans. The sequence and every
    rule come from the config store in the DB. Run the seed migration once before the first
    use: python -m iba.app.migration.import_seed

.PARAMETER Book  OSIS book code, e.g. Prov, Ps, Gen.
.PARAMETER Trace Print every config read (IBA_TRACE).

.EXAMPLE
    .\Set-Candidates.ps1 -Book Prov
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [string] $Book,
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

Test-IbaWorkPackageActive -WorkPackage 'set-candidates'

$seq   = python -c "import json; from iba.app.lib.cfg import Cfg; c=Cfg(); print(json.dumps([dict(r) for r in c.sequence('set-candidates')])); c.close()" | ConvertFrom-Json
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-SET-CANDIDATES"

Write-IbaRunHeader -WorkPackage 'set-candidates' -RunId $runId -RunsOver "book = '$Book'"

$exitCode = 0
foreach ($entry in $seq) {
    $json = python -m iba.app.run set-candidates --step $entry.step --run-id $runId --param "Book=$Book"
    $code = $LASTEXITCODE
    $res  = $json | ConvertFrom-Json
    Write-IbaStepResult -Step $entry.step -Path $res.path -Message $res.message -Code $code
    if ($code -eq 3) { Write-IbaStopped -Message $res.message; $exitCode = 3; break }
    if ($code -eq 2) { Write-IbaPaused -WorkPackage 'set-candidates' -RunId $runId -Message $res.message; $exitCode = 2; break }
}

if ($exitCode -eq 0) {
    Write-IbaComplete -WorkPackage 'set-candidates' -Vars @{ book = $Book }
}
exit $exitCode
