<#
.SYNOPSIS
    Bootstrap the Bible_Projects local development environment.

.DESCRIPTION
    This script:
      1. Verifies required tools (Python, Git, PowerShell version).
      2. Creates a Python virtual environment in analytics\venv\.
      3. Installs Python dependencies from analytics\requirements.txt.
      4. Creates a .env template if one does not already exist.
      5. Confirms that all output directories are present.

.NOTES
    Run from the repository root:
        .\scripts\env_setup.ps1
#>

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$RepoRoot = Split-Path -Parent $PSScriptRoot

Write-Host "`n=== Bible_Projects Environment Setup ===" -ForegroundColor Cyan

# ── 1. Check PowerShell version ──────────────────────────────────────────────
if ($PSVersionTable.PSVersion.Major -lt 7) {
    Write-Warning "PowerShell 7+ is recommended. Current version: $($PSVersionTable.PSVersion)"
}

# ── 2. Check Python ───────────────────────────────────────────────────────────
$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) {
    Write-Error "Python was not found on PATH. Install Python 3.10+ and retry."
}
$pythonVersion = & python --version 2>&1
Write-Host "Python found: $pythonVersion" -ForegroundColor Green

# ── 3. Check Git ──────────────────────────────────────────────────────────────
$gitCmd = Get-Command git -ErrorAction SilentlyContinue
if (-not $gitCmd) {
    Write-Error "Git was not found on PATH. Install Git and retry."
}
$gitVersion = & git --version
Write-Host "Git found: $gitVersion" -ForegroundColor Green

# ── 4. Create Python virtual environment ─────────────────────────────────────
$venvPath = Join-Path $RepoRoot 'analytics\venv'
if (-not (Test-Path $venvPath)) {
    Write-Host "`nCreating Python virtual environment at: $venvPath" -ForegroundColor Yellow
    & python -m venv $venvPath
} else {
    Write-Host "`nVirtual environment already exists: $venvPath" -ForegroundColor Green
}

# ── 5. Install Python dependencies ───────────────────────────────────────────
$requirementsPath = Join-Path $RepoRoot 'analytics\requirements.txt'
$pipExe = Join-Path $venvPath 'Scripts\pip.exe'

Write-Host "`nInstalling Python dependencies..." -ForegroundColor Yellow
& $pipExe install --upgrade pip --quiet
& $pipExe install -r $requirementsPath
Write-Host "Dependencies installed." -ForegroundColor Green

# ── 6. Create .env template if missing ───────────────────────────────────────
$envFile = Join-Path $RepoRoot '.env'
if (-not (Test-Path $envFile)) {
    Write-Host "`nCreating .env template at: $envFile" -ForegroundColor Yellow
    @"
# Bible_Projects environment variables
# Fill in your credentials and NEVER commit this file.

# ── Zotero ──────────────────────────────────────────────────────────────────
ZOTERO_API_KEY=your_zotero_api_key_here
ZOTERO_USER_ID=your_zotero_user_id_here
ZOTERO_LIBRARY_TYPE=user

# ── STEP Bible ──────────────────────────────────────────────────────────────
# Base URL for the STEP Bible public API (no key required for standard access)
STEP_API_BASE_URL=https://www.stepbible.org/api
# Default Bible translation (e.g. ESV, NIV, KJV, NASB, NET)
STEP_DEFAULT_VERSION=ESV
# Optional: API key placeholder — leave blank unless STEP issues a key
# STEP_API_KEY=
# HTTP request timeout in seconds
STEP_REQUEST_TIMEOUT=10

# ── SQLite Database ──────────────────────────────────────────────────────────
# Path to the SQLite database file (relative to project root)
DB_PATH=data/bible_research.db
"@ | Set-Content $envFile
    Write-Host ".env template created. Edit it to add your credentials." -ForegroundColor Yellow
} else {
    Write-Host "`n.env file already exists." -ForegroundColor Green
}

# ── 7. Ensure output directories exist ───────────────────────────────────────
$dirs = @(
    'research',
    'research\projects',
    'research\notes',
    'research\templates',
    'docs',
    'data',
    'data\schema',
    'data\imports',
    'data\exports',
    'outputs\markdown',
    'outputs\docx',
    'outputs\pdf',
    'scripts',
    'analytics'
)

Write-Host "`nVerifying directory structure..." -ForegroundColor Yellow
foreach ($dir in $dirs) {
    $fullPath = Join-Path $RepoRoot $dir
    if (-not (Test-Path $fullPath)) {
        New-Item -ItemType Directory -Path $fullPath | Out-Null
        Write-Host "  Created: $dir" -ForegroundColor Yellow
    } else {
        Write-Host "  OK:      $dir" -ForegroundColor Green
    }
}

Write-Host "`n=== Setup complete! ===" -ForegroundColor Cyan
Write-Host "Next steps:" -ForegroundColor White
Write-Host "  1. Edit .env with your Zotero credentials" -ForegroundColor White
Write-Host "  2. See docs\file_organization.md for the two-tier storage guide (Git + Google Drive)" -ForegroundColor White
Write-Host "  3. See docs\zotero_setup.md for Zotero API instructions" -ForegroundColor White
Write-Host "  4. See docs\step_setup.md for STEP Bible API instructions" -ForegroundColor White
Write-Host "  5. See docs\data_setup.md for SQLite data platform instructions" -ForegroundColor White
Write-Host "  6. Initialise the database schema:" -ForegroundColor White
Write-Host "     python analytics\bible_analytics.py --init-db" -ForegroundColor White
Write-Host "  7. Activate the virtual environment:" -ForegroundColor White
Write-Host "     .\analytics\venv\Scripts\Activate.ps1" -ForegroundColor White
