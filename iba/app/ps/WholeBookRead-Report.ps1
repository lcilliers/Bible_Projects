<#
.SYNOPSIS
    Whole-book-read gathering report — pulls every filled `report.passage_debate` output for a
    book, in reading order, and lays out each one's Emergent-questions / Passage-level-linkages
    content together with an empty Resolution slot. Read-only against the DB; does not decide how
    any emergent question actually resolves itself — see lib/wholebookread.py's module docstring
    for the mechanised/analytical boundary.

.DESCRIPTION
    Writes to report.verse_analysis_output_dir/<BookLabel>/<pattern> — the SAME book folder the
    book's individual passage debates already live in. Requires at least one
    debate_status='filled' passage row for the book (exit code from cfg_on_fail
    report.whole_book_read/no-debates-found if not — run PassageDebate-Report.ps1 first and fill
    in at least one range).

.PARAMETER Book       OSIS book code as stored in verse.osisId, e.g. Dan. Mandatory.
.PARAMETER BookLabel  human-facing subfolder name (e.g. "Daniel"). Defaults to -Book if omitted —
                      same convention PassageDebate-Report.ps1's -BookLabel uses.
.PARAMETER RunId      resume/re-tag a specific run.
.PARAMETER Trace      Print every config read (IBA_TRACE).

.EXAMPLE
    .\WholeBookRead-Report.ps1 -Book Dan -BookLabel Daniel
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

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-WHOLE-BOOK-READ" }

$paramArgs = @('--param', "Book=$Book")
if ($BookLabel) { $paramArgs += @('--param', "BookLabel=$BookLabel") }

Write-IbaRunHeader -WorkPackage 'whole-book-read' -Step 'report.whole_book_read' -RunId $runId

$json = python -m iba.app.run whole-book-read --step report.whole_book_read --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'report.whole_book_read' -Path $res.path -Message $res.message -Code $code

if ($code -eq 0) {
    Write-Host "`nScaffold written — for each item under 'Carried forward per passage,' fill in " -ForegroundColor DarkGray -NoNewline
    Write-Host "whether/how a later passage in this book resolves it." -ForegroundColor DarkGray
}

exit $code
