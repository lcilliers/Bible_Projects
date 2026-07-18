<#
.SYNOPSIS
    The new-word work package. PowerShell orchestrates; Python works; CONFIG (in the DB) governs.

.DESCRIPTION
    The sequence of steps is read from the CONFIG STORE IN THE DATABASE (cfg_step),
    not from a JSON file and not from this script. This script owns no process logic:
    it loads the sequence, calls `python -m iba.app.run` per step, and branches on the
    step's exit code (which the config's on_fail rules decide).

    -Fresh reseeds the config from the JSON into the DB and rebuilds the data tables.
    After that, everything — including this sequence — is read from the DB.

.PARAMETER Word
.PARAMETER Source
.PARAMETER Fresh   Reseed config + rebuild data tables first (a clean slice).
.PARAMETER Trace   Print every config read (IBA_TRACE) — see the governance chain.

.EXAMPLE
    .\New-Word.ps1 -Word hypocrisy -Source "gap scan" -Fresh
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [string] $Word,
    [Parameter(Mandatory = $true)] [string] $Source,
    [switch] $Fresh,
    [switch] $Trace
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'
if ($Trace) { $env:IBA_TRACE = '1' }

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot

if ($Fresh) {
    # convenience: rebuild the data tables before this run (keeps config)
    python -m iba.app.init --reset | Out-Null
}

# The app must be initialised (config loaded, tables built). If not, point to Start-Iba.
$ready = python -c "import sys; from iba.app.init import _config_loaded, _data_tables_exist; from iba.app.lib.cfg import Cfg; print('1' if (_config_loaded() and _data_tables_exist(Cfg())) else '0')" 2>$null
if ($ready -ne '1') {
    Write-Host "The app is not initialised. Run first:  iba\app\ps\Start-Iba.ps1" -ForegroundColor Yellow
    exit 1
}

# The sequence comes from the CONFIG STORE IN THE DB.
$seq   = python -c "import json; from iba.app.lib.cfg import Cfg; c=Cfg(); print(json.dumps([dict(r) for r in c.sequence('new-word')])); c.close()" | ConvertFrom-Json
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-NEW-WORD"

Write-Host ""
Write-Host "work package : new-word"
Write-Host "run_id       : $runId"
Write-Host "runs over    : word = '$Word'"
Write-Host "sequence     : $($seq.Count) steps, loaded from the DB config store (cfg_step)"
Write-Host ""

$halt = $false
$exitCode = 0                       # 0 done · 2 paused · 3 stopped — so the script is composable
foreach ($entry in $seq) {
    $json = python -m iba.app.run new-word `
        --step $entry.step --run-id $runId `
        --param "Word=$Word" --param "Source=$Source"
    $code = $LASTEXITCODE
    $res  = $json | ConvertFrom-Json

    $colour = @{ 0 = 'Green'; 2 = 'Yellow'; 3 = 'Red' }[$code]
    Write-Host ("  {0,-18} {1,-14} {2}" -f $entry.step, $res.path, $res.message) -ForegroundColor $colour

    if ($code -eq 2) {
        Write-Host "`nPAUSED — a researcher escalation was raised; the run is resumable." -ForegroundColor Yellow
        $halt = $true; $exitCode = 2; break
    }
    if ($code -eq 3) {
        Write-Host "`nSTOPPED — $($res.message)" -ForegroundColor Red
        $halt = $true; $exitCode = 3; break
    }
}

Write-Host ""
if (-not $halt) {
    Write-Host "COMPLETE — raw layer built for '$Word'." -ForegroundColor Green
    Write-Host "  report: python -m iba.app.report --word $Word"
}
exit $exitCode
