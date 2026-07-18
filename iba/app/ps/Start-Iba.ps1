<#
.SYNOPSIS
    Start the IBA app: prepare the environment and report ready.

.DESCRIPTION
    The session startup. Run this once when you begin, before any word run. It:
      - checks Python and the one dependency (requests) are available,
      - validates + loads the config into the DB (idempotent),
      - builds the data tables if missing,
      - pre-flights STEP (up and answering with the tagged module),
      - prints READY.

    The app needs NO .env and NO secrets: STEP is the local server named in config,
    with no key. The only external requirement is the local STEP server running.

.PARAMETER Reload   Reseed the config from the JSON into the DB.
.PARAMETER Reset    Rebuild the data tables (DROPS data). Config is kept.

.EXAMPLE
    .\Start-Iba.ps1
    .\Start-Iba.ps1 -Reset        # start clean (drops the data, keeps config)
#>

[CmdletBinding()]
param([switch] $Reload, [switch] $Reset)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot

# 0. Python + dependency
try {
    python -c "import requests" 2>$null
    if ($LASTEXITCODE -ne 0) { throw }
} catch {
    Write-Host "Python or 'requests' not available. Install: python -m pip install requests" -ForegroundColor Red
    exit 1
}

# 1-4. bootstrap (config, DB, STEP)
$flags = @()
if ($Reload) { $flags += '--reload' }
if ($Reset)  { $flags += '--reset' }
python -m iba.app.init @flags
exit $LASTEXITCODE
