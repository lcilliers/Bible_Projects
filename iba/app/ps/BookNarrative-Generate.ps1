<#
.SYNOPSIS
    Assembles a book's filled passage debates + the two governing narrative docs (hard constraints
    + three-channel guidance), submits the package to the Anthropic Messages API, and files the
    returned narrative — a real API call, real money, not a subscription. See
    lib/narrativegenerate.py's module docstring for the full design.

.DESCRIPTION
    First run for a book: assembles the package, estimates tokens/cost, and PAUSES for researcher
    approval (report.book_narrative_generate/needs-approval) — no API call is made yet. Answer the
    escalation (Escalation.ps1 -Action AnswerRun -Decision Approve|Reject|Revise|Hold|Noted), then re-run this
    EXACT command with the SAME -RunId to make the live call and write the narrative.

    Requires ANTHROPIC_API_KEY in the environment or the repo-root .env. Requires at least one
    debate_status='filled' passage row for the book (run PassageDebate-Report.ps1 first).

.PARAMETER Book       OSIS book code as stored in verse.osisId, e.g. Dan. Mandatory.
.PARAMETER BookLabel  human-facing subfolder name (e.g. "Daniel"). Defaults to -Book if omitted —
                      same convention every other verse-analysis script uses.
.PARAMETER RunId      resume the SAME run after answering its approval escalation. Mandatory to
                      resume; a fresh run without -RunId always starts a new estimate+pause.
.PARAMETER Trace      Print every config read (IBA_TRACE).

.EXAMPLE
    .\BookNarrative-Generate.ps1 -Book Dan -BookLabel Daniel
    # PAUSED — read the estimate, then:
    .\Escalation.ps1 -Action AnswerRun -RunId RUN-...-NARRATIVE-GENERATE -Decision Approve
    .\BookNarrative-Generate.ps1 -Book Dan -BookLabel Daniel -RunId RUN-...-NARRATIVE-GENERATE
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [string] $Book,
    [string] $BookLabel,
    [string] $RunId,
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

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-NARRATIVE-GENERATE" }

$paramArgs = @('--param', "Book=$Book")
if ($BookLabel) { $paramArgs += @('--param', "BookLabel=$BookLabel") }

Write-IbaRunHeader -WorkPackage 'book-narrative-generate' -Step 'report.book_narrative_generate' -RunId $runId

$json = python -m iba.app.run book-narrative-generate --step report.book_narrative_generate --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'report.book_narrative_generate' -Path $res.path -Message $res.message -Code $code

if ($code -eq 2) {
    Write-Host "`nPAUSED — no API call made yet. Read the estimate above, then:" -ForegroundColor Yellow
    Write-Host "  iba\app\ps\Escalation.ps1 -Action AnswerRun -RunId $runId -Decision Approve|Reject|Revise|Hold|Noted" -ForegroundColor Yellow
    Write-Host "  iba\app\ps\BookNarrative-Generate.ps1 -Book $Book -BookLabel $BookLabel -RunId $runId   # re-run to resume" -ForegroundColor Yellow
} elseif ($code -eq 0) {
    Write-Host "`nNarrative written — run BookNarrative-Validate.ps1 on it next." -ForegroundColor DarkGray
}

exit $code
