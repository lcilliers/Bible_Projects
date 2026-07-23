<#
.SYNOPSIS
    Every output/report generator in the app, registered and config-governed. Step-selection,
    not a fixed pipeline — these three are independent, not a sequence.

.DESCRIPTION
    -Step ReportWord        the word-raw report (report.py). Needs -Word.
    -Step ValidationWord    the raw-layer validation report (validation.py). Needs -Word.
    -Step ValidationBook    the base-layer validation report (validation.py). Needs -Book.

    Output location and content (which sections/fields appear) are config — see
    CONFIG-REPORT.md's Settings section (module = report / validation) or
    Config-Maintenance.ps1 -Step Propose to change them.

.PARAMETER Step  ReportWord | ValidationWord | ValidationBook
.PARAMETER Word  the word (for ReportWord / ValidationWord)
.PARAMETER Book  the OSIS book code (for ValidationBook)
.PARAMETER Trace Print every config read (IBA_TRACE).

.EXAMPLE
    .\Reports.ps1 -Step ReportWord -Word hypocrisy
.EXAMPLE
    .\Reports.ps1 -Step ValidationBook -Book Prov
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [ValidateSet('ReportWord', 'ValidationWord', 'ValidationBook')] [string] $Step,
    [string] $Word,
    [string] $Book,
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

$stepMap = @{ ReportWord = 'report.word'; ValidationWord = 'validation.word'; ValidationBook = 'validation.book' }
$stepId  = $stepMap[$Step]
$runId   = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-REPORTS"

$paramArgs = @()
if ($Step -in @('ReportWord', 'ValidationWord')) {
    if (-not $Word) { Write-Host "$Step needs -Word." -ForegroundColor Yellow; exit 1 }
    $paramArgs += @('--param', "Word=$Word")
} else {
    if (-not $Book) { Write-Host "$Step needs -Book." -ForegroundColor Yellow; exit 1 }
    $paramArgs += @('--param', "Book=$Book")
}

Write-IbaRunHeader -WorkPackage 'reports' -Step $stepId -RunId $runId

$json = python -m iba.app.run reports --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code
exit $code
