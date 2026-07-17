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
    Write-Host "[config] seeding cfg_* from the JSON into the DB, rebuilding data tables" -ForegroundColor DarkCyan
    python -m iba.app.lib.cfgload | Out-Null
    python -m iba.app.lib.db --reset | Out-Null
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
        $halt = $true; break
    }
    if ($code -eq 3) {
        Write-Host "`nSTOPPED — $($res.message)" -ForegroundColor Red
        $halt = $true; break
    }
}

Write-Host ""
if (-not $halt) {
    Write-Host "COMPLETE — raw layer built for '$Word'." -ForegroundColor Green
    Write-Host "  report: python -m iba.app.report --word $Word"
}
