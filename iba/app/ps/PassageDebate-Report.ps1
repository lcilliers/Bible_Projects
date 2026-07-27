<#
.SYNOPSIS
    Passage-debate SCAFFOLD generator — writes the front-matter, per-verse Subject/Operation/
    Source/Target + Q1-Q10 interrogative blocks, and standard closing sections for a passage
    debate, resolved against the CURRENT method docs (config-driven, not memory). Read-only
    against the DB; does not generate the interpretive content itself — see
    lib/passagedebatereport.py's module docstring for the mechanised/analytical boundary.

.DESCRIPTION
    Writes to report.verse_analysis_output_dir/<BookLabel>/<pattern> — the SAME book folder the
    range's `report.verse_span_meaning` extract already lives in (config-governed, not
    hardcoded — see CONFIG-REPORT.md, modules 'report' and 'method'). Requires that extract to
    already exist for this exact book/range (exit code from cfg_on_fail
    report.passage_debate/base-extract-missing if not — run VerseSpanMeaning-Report.ps1 first).
    Also requires method.passage_read_guidance_path / method.interpretation_questions_path to
    resolve to real files on disk (report.passage_debate/guidance-doc-missing otherwise).

.PARAMETER Book       OSIS book code as stored in verse.osisId, e.g. Dan. Mandatory.
.PARAMETER Chapters   whole-chapter range, e.g. 1-3 or 1. Mutually exclusive with -Range.
.PARAMETER Range      single-chapter verse range, e.g. 2:17-30. Mutually exclusive with -Chapters.
.PARAMETER BookLabel  human-facing subfolder name (e.g. "Daniel"). Defaults to -Book if omitted —
                      a per-call parameter, not a setting, same boundary as
                      VerseSpanMeaning-Report.ps1's -BookLabel.
.PARAMETER RunId      resume/re-tag a specific run.
.PARAMETER Trace      Print every config read (IBA_TRACE).

.EXAMPLE
    .\PassageDebate-Report.ps1 -Book Dan -Range 3:1-7 -BookLabel Daniel
.EXAMPLE
    .\PassageDebate-Report.ps1 -Book Dan -Chapters 3 -BookLabel Daniel
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [string] $Book,
    [string] $Chapters,
    [string] $Range,
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

if ([bool]$Chapters -eq [bool]$Range) {
    Write-Host "Give exactly one of -Chapters or -Range." -ForegroundColor Yellow
    exit 1
}

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-PASSAGE-DEBATE" }

$paramArgs = @('--param', "Book=$Book")
if ($Chapters) { $paramArgs += @('--param', "Chapters=$Chapters") }
if ($Range)    { $paramArgs += @('--param', "Range=$Range") }
if ($BookLabel) { $paramArgs += @('--param', "BookLabel=$BookLabel") }

Write-IbaRunHeader -WorkPackage 'passage-debate-report' -Step 'report.passage_debate' -RunId $runId

$json = python -m iba.app.run passage-debate-report --step report.passage_debate --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'report.passage_debate' -Path $res.path -Message $res.message -Code $code

if ($code -eq 0) {
    Write-Host "`nScaffold written — fill in every <!-- fill in --> placeholder by applying:" -ForegroundColor DarkGray
    $guidance = python -c "from iba.app.lib.cfg import Cfg; c=Cfg(); print(c.setting('method.passage_read_guidance_path')); c.close()"
    $interrogative = python -c "from iba.app.lib.cfg import Cfg; c=Cfg(); print(c.setting('method.interpretation_questions_path')); c.close()"
    Write-Host "  method:        $guidance" -ForegroundColor DarkGray
    Write-Host "  interrogative: $interrogative" -ForegroundColor DarkGray
}

exit $code
