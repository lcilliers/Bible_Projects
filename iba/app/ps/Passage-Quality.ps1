<#
.SYNOPSIS
    Standalone quality check for passage — the verse_count distribution (how fragmented passages
    are, or — book-scoped — how sized a completed book's debate ranges came out). NOT part of
    Build-Passages.ps1's sequence (deliberately — see handlers/passage.py:validate's docstring):
    run this on demand, not on every book build.

.DESCRIPTION
    Read-only. If there are passages to review, escalates ONCE with the distribution, then
    pauses. Answer with
    `Escalation.ps1 -Action AnswerRun -RunId <run_id> -Decision <Approve|Reject|Revise|Hold|Noted>`,
    then re-run this script with -RunId to act on the answer.

.PARAMETER Book   Optional OSIS book code (e.g. Dan). Scopes the distribution to that book's live
                  passages — for a book whose passage-debate work is complete, this is the min/max/
                  avg verse-count spot-check on the debate-range sizes actually chosen (e.g. "was
                  a 45-verse range the right call?"), not the raw char-continuity fragmentation
                  the unscoped, corpus-wide run checks. Omit for the original corpus-wide check.
.PARAMETER RunId  resume a specific pending check (reuse the run_id from its first call).
.PARAMETER Trace  Print every config read (IBA_TRACE).

.EXAMPLE
    .\Passage-Quality.ps1
.EXAMPLE
    .\Passage-Quality.ps1 -Book Dan
.EXAMPLE
    .\Passage-Quality.ps1 -RunId RUN-20260721_...-PASSAGE-QUALITY
#>

[CmdletBinding()]
param(
    [string] $Book,
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

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-PASSAGE-QUALITY" }

Write-IbaRunHeader -WorkPackage 'passage-quality' -RunId $runId

$paramArgs = @()
if ($Book) { $paramArgs += @('--param', "Book=$Book") }

$json = python -m iba.app.run passage-quality --step passage.validate --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'passage.validate' -Path $res.path -Message $res.message -Code $code

if ($code -eq 2) {
    Write-IbaPaused -WorkPackage 'passage-quality' -RunId $runId -Message $res.message
}

exit $code
