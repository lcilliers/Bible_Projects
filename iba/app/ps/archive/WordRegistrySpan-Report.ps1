<#
.SYNOPSIS
    word_registry -> word_strong -> strong -> parse-meaning -> unique span analysis, for one
    registry word. Read-only.

.DESCRIPTION
    For every Strong's linked to the given word (word_registry -> word_strong), shows its gloss/
    transliteration/count, its parse-meaning breakdown (strong_meaning_parsed, falling back to the
    base lemma for suffixed sub-entries like H3372G), and its unique surface-span applications —
    the distinct `span.surface` text forms tagged with that Strong's in `verse_lexical`, each with
    an example verse reference + text.

    Writes report.word_registry_span_output_dir (default iba/app/verse-analysis/word_registry/) —
    one file per word, dated/versioned naming (cfg_report.naming_scheme='dated'), prior versions
    auto-archived. Content/section shape governed by cfg_report/cfg_report_section — see
    CONFIG-REPORT.md or Config-Maintenance.ps1 -Step Propose to change them.

.PARAMETER Word    the registry word, e.g. fear. Mandatory.
.PARAMETER RunId    resume/re-tag a specific run.
.PARAMETER Trace    Print every config read (IBA_TRACE).

.EXAMPLE
    .\WordRegistrySpan-Report.ps1 -Word fear
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [string] $Word,
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

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-WORD-REGISTRY-SPAN" }

Write-IbaRunHeader -WorkPackage 'word-registry-span-report' -RunId $runId -RunsOver "word = '$Word'"

$json = python -m iba.app.run word-registry-span-report --step report.word_registry_span --run-id $runId --param "Word=$Word"
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'report.word_registry_span' -Path $res.path -Message $res.message -Code $code

exit $code
