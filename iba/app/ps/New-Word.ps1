<#
.SYNOPSIS
    The new-word work package. PowerShell is the orchestrator; Python does the work.

.DESCRIPTION
    Loads the sequence from iba/app/config/run.json and walks it, calling
    `python -m iba.app.run` once per step. It owns NO process logic — the order of
    work is config, the work of each step is a Python handler. Changing the sequence
    is a run.json edit, not a script edit.

    Branches on the step's exit code:
        0  ok        -> next step
        2  paused    -> a researcher escalation was raised; stop, resumable later
        3  stop      -> a red failure; stop

.PARAMETER Word
    The English word to register and build.

.PARAMETER Source
    Why it is being registered.

.PARAMETER Fresh
    Rebuild the DB from schema.json before running (a clean slice).

.EXAMPLE
    .\New-Word.ps1 -Word hypocrisy -Source "gap scan 2026-07-17" -Fresh
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [string] $Word,
    [Parameter(Mandatory = $true)] [string] $Source,
    [switch] $Fresh
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot

$runCfg  = Get-Content "iba/app/config/run.json" -Raw | ConvertFrom-Json
$package = $runCfg.work_packages.'new-word'
# millisecond precision — two runs in the same second must not share a run_id
$runId   = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-NEW-WORD"

Write-Host ""
Write-Host "work package : new-word — $($package.name)"
Write-Host "run_id       : $runId"
Write-Host "runs over    : word = '$Word'"
Write-Host "sequence     : $($package.sequence.Count) steps, loaded from run.json"
Write-Host ""

if ($Fresh) {
    Write-Host "[db] rebuilding from schema.json (fresh slice)" -ForegroundColor DarkCyan
    python -m iba.app.lib.db --reset | Out-Null
}

$halt = $false
foreach ($entry in $package.sequence) {
    $json = python -m iba.app.run new-word `
        --step $entry.step --run-id $runId `
        --param "Word=$Word" --param "Source=$Source"
    $code = $LASTEXITCODE
    $res  = $json | ConvertFrom-Json

    $colour = @{ 0 = 'Green'; 2 = 'Yellow'; 3 = 'Red' }[$code]
    Write-Host ("  {0,-18} {1,-6} {2}" -f $entry.step, $res.path, $res.message) -ForegroundColor $colour

    if ($code -eq 2) {
        Write-Host ""
        Write-Host "PAUSED — a researcher escalation was raised. The run is resumable:" -ForegroundColor Yellow
        Write-Host "  answer the escalation, then re-run this package; it resumes at the paused step." -ForegroundColor Yellow
        $halt = $true; break
    }
    if ($code -eq 3) {
        Write-Host ""
        Write-Host "STOPPED — $($res.message)" -ForegroundColor Red
        $halt = $true; break
    }
}

Write-Host ""
if (-not $halt) {
    Write-Host "COMPLETE — raw layer built for '$Word'." -ForegroundColor Green
    Write-Host "  report: python -m iba.app.report --word $Word"
}
