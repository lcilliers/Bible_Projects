<#
.SYNOPSIS
    Migrate the legacy registry word list into the IBA app by running the new-word
    operation for each word, in series.

.DESCRIPTION
    Reads the OLD study database (database/bible_research.db, READ-ONLY) and takes every
    word_registry word EXCEPT those marked deleted or excluded (phase1_status). For each,
    it runs New-Word.ps1 and drives the run to completion:

      - a registry-approval pause is auto-answered YES (this list is the researcher's own
        curated, already-approved registry — that is the point of the migration),
      - any OTHER pause (e.g. a word that maps to no strongs) is NOT auto-resolved; it is
        logged as NEEDS-REVIEW and the batch moves on,
      - a word already built in the app is skipped (so the batch is resumable — re-run it
        any time and it continues where it stopped).

    A markdown transcript is written to iba/app/reports/. Nothing in the old DB is touched.

.PARAMETER Source   Override the Source recorded per word. Default: "legacy registry: <source_list>".
.PARAMETER Limit    Process only the first N words (0 = all). Use for a trial.
.PARAMETER DryRun   List the words that would be processed; make no changes, no STEP calls.
.PARAMETER SkipStartup  Do not run Start-Iba first (assume the app is already initialised).

.EXAMPLE
    .\Import-LegacyRegistry.ps1 -DryRun
    .\Import-LegacyRegistry.ps1 -Limit 5
    .\Import-LegacyRegistry.ps1
#>

[CmdletBinding()]
param(
    [string] $Source = "",
    [int]    $Limit = 0,
    [switch] $DryRun,
    [switch] $SkipStartup
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot
$NewWord = Join-Path $PSScriptRoot 'New-Word.ps1'
$StartIba = Join-Path $PSScriptRoot 'Start-Iba.ps1'

# 1. app must be ready (config loaded, tables built, STEP up) — unless told to skip
if (-not $DryRun -and -not $SkipStartup) {
    & $StartIba | Out-Host
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Startup did not reach ready (STEP down?). Aborting import." -ForegroundColor Red
        exit 1
    }
}

# 2. the word list from the OLD DB (read-only), excluding deleted/excluded
$words = (python -m iba.app.tools.legacy_import words | ConvertFrom-Json)
if ($Limit -gt 0) { $words = $words | Select-Object -First $Limit }
$total = ($words | Measure-Object).Count
Write-Host ""
Write-Host "legacy import — $total word(s) to process (deleted/excluded already filtered out)" -ForegroundColor Cyan

# 3. transcript
$stamp = Get-Date -Format 'yyyyMMdd_HHmmss'
$log = Join-Path $RepoRoot "iba/app/reports/legacy-import-$stamp.md"
$lines = @("# Legacy registry import — $stamp", "",
           "Source DB: ``database/bible_research.db`` (read-only). $total word(s).", "",
           "| # | word | result | detail |", "| --- | --- | --- | --- |")
$tally = @{ DONE = 0; SKIPPED = 0; 'NEEDS-REVIEW' = 0; ERROR = 0 }

$i = 0
foreach ($w in $words) {
    $i++
    $word = $w.word
    $src = if ($Source) { $Source } elseif ($w.source_list) { "legacy registry: $($w.source_list)" } else { "legacy registry migration" }

    if ($DryRun) {
        Write-Host ("  [{0}/{1}] would import '{2}'" -f $i, $total, $word)
        $lines += "| $i | $word | (dry-run) | $src |"
        continue
    }

    Write-Host ("  [{0}/{1}] {2}" -f $i, $total, $word) -ForegroundColor White

    # first attempt
    & $NewWord -Word $word -Source $src | Out-Host
    $code = $LASTEXITCODE
    $result = "?"; $detail = ""

    if ($code -eq 0) {
        $result = "DONE"
    }
    elseif ($code -eq 3) {
        $result = "SKIPPED"; $detail = "already built / stopped"
    }
    elseif ($code -eq 2) {
        # what is it paused on? only a registry-approval pause is auto-answered
        $at = (python -m iba.app.tools.legacy_import pending $word).Trim()
        if ($at -eq 'registry.create') {
            python -m iba.app.lib.escalation answer $word yes | Out-Null
            & $NewWord -Word $word -Source $src | Out-Host       # resume
            $code2 = $LASTEXITCODE
            if     ($code2 -eq 0) { $result = "DONE" }
            elseif ($code2 -eq 3) { $result = "SKIPPED"; $detail = "stopped after approval" }
            else                  { $result = "NEEDS-REVIEW"; $detail = "paused again after approval (at ${at})" }
        }
        else {
            $result = "NEEDS-REVIEW"; $detail = "paused at '${at}' (not an approval) — left for you"
        }
    }
    else {
        $result = "ERROR"; $detail = "exit $code"
    }

    if (-not $tally.ContainsKey($result)) { $tally[$result] = 0 }
    $tally[$result]++
    $lines += "| $i | $word | $result | $detail |"
    Write-Host ("       -> {0} {1}" -f $result, $detail) -ForegroundColor Gray
}

# 4. summary
$summary = "DONE $($tally['DONE']) · SKIPPED $($tally['SKIPPED']) · NEEDS-REVIEW $($tally['NEEDS-REVIEW']) · ERROR $($tally['ERROR'])"
$lines += @("", "## Summary", "", $summary)
$lines | Set-Content -Path $log -Encoding utf8

Write-Host ""
Write-Host $summary -ForegroundColor Cyan
Write-Host "transcript: $log"
