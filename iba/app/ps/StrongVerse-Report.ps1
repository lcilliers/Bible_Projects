<#
.SYNOPSIS
    On-demand verse restatement for ONE Strong's reference, in the context of a registry word.
    Read-only.

.DESCRIPTION
    Every verse `verse_lexical` matches this exact Strong's code (whole Bible), with only that
    occurrence annotated inline (`**surface** [strong: senses]`) — the rest of each verse is
    untouched. Senses are exact `strong_variant` matches only (no sibling/base fallback). A
    combined-code span (STEP tags more than one Strong's on one rendering unit) is labelled as
    such; an empty-surface occurrence (the other half of a combined tag, no independent English
    text) is noted as a structured aside rather than forced into the running text; a surface that
    doesn't match this verse's text exactly once is flagged UNRESOLVED rather than guessed.

    Formalises iba/app/reports/g2128-verse-lexical-by-strong-sample-20260810.md and
    g2127-verse-lexical-by-strong-sample-20260810.md (BUILD.md — the session that built this).

    Writes report.strong_verse_output_dir (default iba/app/verse-analysis/word_registry/)
    /<word>/<word>-<strong>-verse-lexical.md — filed directly under the word's own folder, dated/
    versioned naming, prior versions auto-archived. Content/section shape governed by
    cfg_report/cfg_report_section — see CONFIG-REPORT.md or Config-Maintenance.ps1 -Step Propose
    to change them.

.PARAMETER Word    the registry word this Strong's is being viewed under, e.g. blessing.
                    Mandatory — also the filing folder. The Strong's must be linked to this word
                    (word_strong); the run refuses otherwise.
.PARAMETER Strong   the Strong's code, e.g. G2127. Mandatory.
.PARAMETER RunId    resume/re-tag a specific run.
.PARAMETER Trace    Print every config read (IBA_TRACE).

.EXAMPLE
    C:\Bible_study_projects\iba\app\ps\StrongVerse-Report.ps1 -Word blessing -Strong G2127
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [string] $Word,
    [Parameter(Mandatory = $true)] [string] $Strong,
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

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-STRONG-VERSE" }

Write-IbaRunHeader -WorkPackage 'strong-verse-report' -RunId $runId -RunsOver "word = '$Word', strong = '$Strong'"

$json = python -m iba.app.run strong-verse-report --step report.strong_verse --run-id $runId --param "Word=$Word" --param "Strong=$Strong"
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'report.strong_verse' -Path $res.path -Message $res.message -Code $code

exit $code
