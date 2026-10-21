<#
.SYNOPSIS
    Structural presence check on an inner-being narrative file — confirms a "## Scope self-check"
    section exists and all three required channel labels (non-human<->human, human<->human,
    physical world<->human) are present with non-empty content. A presence check only, not a
    judgment of citation quality — see WA-inner-being-narrative-guidance-v1-2026-07-28.md section 4
    and handlers/narrative.py's module docstring.

.DESCRIPTION
    Read-only. Not part of any narrative-writing pipeline (none is registered — narrative writing
    stays unmechanized analytical work). Run this on demand against a finished narrative file
    before treating it as done.

.PARAMETER Path  the narrative markdown file to check. Mandatory.
.PARAMETER Trace  Print every config read (IBA_TRACE).

.EXAMPLE
    .\BookNarrative-Validate.ps1 -Path iba\app\verse-analysis\Daniel\WA-dan-inner-being-narrative-v3-consolidated-2026-07-28.md
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [string] $Path,
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

$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-BOOK-NARRATIVE-VALIDATE"

Write-IbaRunHeader -WorkPackage 'book-narrative-validate' -Step 'report.book_narrative_validate' -RunId $runId

$json = python -m iba.app.run book-narrative-validate --step report.book_narrative_validate --run-id $runId --param "Path=$Path"
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'report.book_narrative_validate' -Path $res.path -Message $res.message -Code $code

exit $code
