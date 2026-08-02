<#
.SYNOPSIS
    The book-narrative work package — entry point (c) of the book-by-book pipeline's 3-way split
    (chapter generation / book overview / book narrative, per the researcher's 2026-08-02
    instruction). PowerShell orchestrates; Python works; CONFIG (in the DB) governs.

.DESCRIPTION
    Chains report.book_narrative_generate then report.book_narrative_validate under one run_id,
    for one book. Unlike Chapter-Generate.ps1/New-Word.ps1's generic sequence-loop (same fixed
    params passed to every step), this is bespoke orchestration: validate needs the -Path
    generate just wrote, which isn't known until generate's own result comes back — so this
    script reads generate's result.path and feeds it into validate automatically. No need to
    re-invoke BookNarrative-Validate.ps1 by hand with a copy-pasted path afterward.

    Cost is real money, not a subscription (report.book_narrative_generate calls the live
    Anthropic Messages API). First run for a book: estimates tokens/cost and PAUSES for
    researcher approval — no API call is made yet, and validate does not run either. Answer the
    escalation, then re-run this EXACT command with the SAME -RunId to make the live call and
    continue automatically to validation.

    Requires ANTHROPIC_API_KEY in the environment or the repo-root .env. Requires at least one
    debate_status='filled' passage row for the book (Chapter-Generate.ps1 + manual fill +
    PassageDebate-Sync.ps1, per chapter, first).

.PARAMETER Book       OSIS book code as stored in verse.osisId, e.g. Hos. Mandatory.
.PARAMETER BookLabel  human-facing subfolder name (e.g. "Hosea"). Defaults to -Book if omitted.
.PARAMETER RunId      resume the SAME run after answering its approval escalation. Mandatory to
                      resume; a fresh run without -RunId always starts a new estimate+pause.
.PARAMETER Trace      Print every config read (IBA_TRACE).

.EXAMPLE
    .\Book-Narrative.ps1 -Book Amos -BookLabel Amos
    # PAUSED — read the estimate, then:
    .\Escalation.ps1 -Action AnswerRun -RunId RUN-...-BOOK-NARRATIVE -Decision Approve
    .\Book-Narrative.ps1 -Book Amos -BookLabel Amos -RunId RUN-...-BOOK-NARRATIVE
    # makes the live call, writes the narrative, THEN validates it automatically
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

Test-IbaWorkPackageActive -WorkPackage 'book-narrative'

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-BOOK-NARRATIVE" }

$paramArgs = @('--param', "Book=$Book")
if ($BookLabel) { $paramArgs += @('--param', "BookLabel=$BookLabel") }

Write-IbaRunHeader -WorkPackage 'book-narrative' -RunId $runId -RunsOver "book = '$Book'"

# ordinal 0 — generate (real API spend, approval-gated)
$json = python -m iba.app.run book-narrative --step report.book_narrative_generate --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'report.book_narrative_generate' -Path $res.path -Message $res.message -Code $code

if ($code -eq 2) {
    Write-IbaPaused -WorkPackage 'book-narrative' -RunId $runId -Message $res.message
    exit 2
}
if ($code -eq 3) {
    Write-IbaStopped -Message $res.message
    exit 3
}

# ordinal 1 — validate, fed generate's own output path automatically
$json2 = python -m iba.app.run book-narrative --step report.book_narrative_validate --run-id $runId --param "Path=$($res.path)"
$code2 = $LASTEXITCODE
$res2  = $json2 | ConvertFrom-Json
Write-IbaStepResult -Step 'report.book_narrative_validate' -Path $res2.path -Message $res2.message -Code $code2

if ($code2 -eq 3) {
    Write-IbaStopped -Message $res2.message
    exit 3
}

Write-IbaComplete -WorkPackage 'book-narrative' -Vars @{ book = $Book }
exit $code2
