<#
.SYNOPSIS
    The ongoing candidate_seed add/correct/split/remove utility. Two modes:
    -Mode Curate (default) — single-row, APPROVAL-GATED correct/split/delete on a row that
      already exists. configmaint.propose deliberately never touches data tables (only cfg_*),
      so candidate_seed needs its own governed correction path.
    -Mode Load — JSON-batch create/update/validate (candidate.load). Takes a batch of English
      WORDS (no lemma_key — the tool derives it), auto-loads whatever passes every config-driven
      check, and writes anything that doesn't as an inspectable candidate_seed row
      (decision='exception') rather than a per-item approval gate. One escalation for the whole
      run, only if unresolved exceptions remain. Omitting -InputFile (or an empty items array)
      just revalidates the existing seed. See iba/docs plan "melodic-foraging-bunny" (approved
      2026-07-22) for the full design.

.DESCRIPTION
    -Mode Curate:
    -Field tag       correct a wrong tag on the row for (LemmaKey, StrongVariant or the base row
                     if StrongVariant is omitted).
    -Field decision  reject a lemma/variant (decision -> rejected), same row-targeting.
    -Field split     ADD a new row for a specific sub-strong variant (StrongVariant REQUIRED,
                     Value = its own clean, single-concept tag) — many base lemmas have multiple
                     sub-lettered strong variants with genuinely different senses (e.g. H0639G
                     "anger" vs H0639H "nose"); the base lemma_key alone can't hold both as one
                     clean tag. Copies layer/registry_match from the base row.
    -Field delete    soft-delete the row for (LemmaKey, StrongVariant or the base row) — e.g. the
                     researcher's 2026-07-22 rule that a candidate with no tag and no registry
                     match at all is an invalid row.

    First call escalates and pauses (exit code 2) — answer it with:
        Escalation.ps1 -Action AnswerRun -RunId <run_id> -Decision <Approve|Reject|Revise|Hold|Noted>
    then re-run this SAME command (pass -RunId to resume the same proposal).

    -Mode Load:
    -InputFile   path to a JSON file: { "items": [ { "word": "...", "reason": "..." }, ... ] }.

    Adding a BRAND-NEW candidate LEMMA (not yet in candidate_seed at all) via -Mode Curate is
    still the existing cfg_candidate_rule 'accept' route via Config-Maintenance.ps1 -Step Propose
    -Table cfg_candidate_rule -Op insert, followed by a candidate.seed re-run (Set-Candidates.ps1)
    — see the curation method doc. -Mode Curate corrects/splits/removes rows that already exist;
    -Mode Load is the batch add-from-outside-the-app path.

.PARAMETER Mode           Curate (default) | Load
.PARAMETER LemmaKey       (Curate) the base lemma, e.g. H0639
.PARAMETER Field          (Curate) tag | decision | split | delete
.PARAMETER StrongVariant  (Curate) the specific sub-lettered strong (e.g. H0639G) — omit to target
                         the base row (strong_variant = LemmaKey). REQUIRED for -Field split.
.PARAMETER Value          (Curate) the new value (tag text; decision: candidate|rejected|undecided;
                         the new tag for split). Not needed for -Field delete.
.PARAMETER InputFile      (Load) path to the JSON batch. Omit to revalidate the existing seed only.
.PARAMETER Question       plain-text description shown to the researcher — make this REPRESENTATIVE.
.PARAMETER RunId           resume a specific pending proposal (Curate only — Load has no gate on
                         clean items, only its own unresolved-exceptions escalation).
.PARAMETER Trace           Print every config read (IBA_TRACE).

.EXAMPLE
    .\Candidate-Curate.ps1 -LemmaKey H8085 -Field tag -Value "hearing" `
        -Question "Replace the raw dual-gloss 'to hear: hear' with a clean IB label."
    # -> PAUSED, run_id printed. Answer it, then:
    .\Candidate-Curate.ps1 -RunId <the run_id> -LemmaKey H8085 -Field tag -Value "hearing"

.EXAMPLE
    .\Candidate-Curate.ps1 -LemmaKey H2000 -Field decision -Value rejected `
        -Question "H2000 was seeded read-emergent but on review does not belong — reject it."

.EXAMPLE
    .\Candidate-Curate.ps1 -LemmaKey H0639 -StrongVariant H0639G -Field split -Value "anger" `
        -Question "H0639 covers three distinct senses (anger/nose/face) across its sub-strongs -- split H0639G off as its own clean-tag row."

.EXAMPLE
    .\Candidate-Curate.ps1 -LemmaKey G0112 -Field delete `
        -Question "No tag, no registry_match, ib-judgement layer only -- an invalid row per the researcher's 2026-07-22 rule."

.EXAMPLE
    .\Candidate-Curate.ps1 -Mode Load -InputFile iba\app\config\seed-batch-20260722.json

.EXAMPLE
    .\Candidate-Curate.ps1 -Mode Load
    # no -InputFile: revalidates the whole existing seed, no new items.
#>

[CmdletBinding()]
param(
    [ValidateSet('Curate', 'Load')] [string] $Mode = 'Curate',
    [string] $LemmaKey,
    [ValidateSet('tag', 'decision', 'split', 'delete')] [string] $Field,
    [string] $StrongVariant,
    [string] $Value,
    [string] $InputFile,
    [string] $Question,
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

if ($Mode -eq 'Curate') {
    if (-not $LemmaKey -or -not $Field) {
        Write-Host "-Mode Curate needs -LemmaKey and -Field." -ForegroundColor Yellow
        exit 1
    }
    if ($Field -ne 'delete' -and -not $Value) {
        Write-Host "-Field $Field needs -Value." -ForegroundColor Yellow
        exit 1
    }
    if ($Field -eq 'split' -and -not $StrongVariant) {
        Write-Host "-Field split needs -StrongVariant (the specific sub-lettered strong this new row is for)." -ForegroundColor Yellow
        exit 1
    }
}

$ready = python -c "from iba.app.init import _config_loaded, _data_tables_exist; from iba.app.lib.cfg import Cfg; print('1' if (_config_loaded() and _data_tables_exist(Cfg())) else '0')" 2>$null
if ($ready -ne '1') {
    Write-IbaNotInitialised
    exit 1
}

if ($Mode -eq 'Load') {
    $runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-CANDIDATE-LOAD" }
    $paramArgs = @()
    if ($InputFile) { $paramArgs += @('--param', "InputFile=$InputFile") }

    Write-IbaRunHeader -WorkPackage 'candidate-curation' -RunId $runId

    $json = python -m iba.app.run candidate-curation --step candidate.load --run-id $runId @paramArgs
    $code = $LASTEXITCODE
    $res  = $json | ConvertFrom-Json
    Write-IbaStepResult -Step 'candidate.load' -Path $res.path -Message $res.message -Code $code

    # NOTE: this banner's wording deliberately differs from the shared guided template (missing
    # the "then re-run..." line) — a pre-existing inconsistency found 2026-07-22, preserved as-is
    # per Phase 0's "no visible change" rule rather than silently normalised. Flagged for the
    # researcher to decide on in a follow-up, not decided here.
    if ($code -eq 2) {
        Write-Host ""
        Write-Host "PAUSED — unresolved exceptions in candidate_seed. Answer with:" -ForegroundColor Yellow
        Write-Host "  .\Escalation.ps1 -Action AnswerRun -RunId $runId -Decision <Approve|Reject|Revise|Hold|Noted> [-Comment ...]"
    }
    exit $code
}

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-CANDIDATE-CURATE" }

$paramArgs = @('--param', "LemmaKey=$LemmaKey", '--param', "Field=$Field")
if ($StrongVariant) { $paramArgs += @('--param', "StrongVariant=$StrongVariant") }
if ($Value)         { $paramArgs += @('--param', "Value=$Value") }
if ($Question)      { $paramArgs += @('--param', "Question=$Question") }

Write-IbaRunHeader -WorkPackage 'candidate-curation' -RunId $runId

$json = python -m iba.app.run candidate-curation --step candidate.curate --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'candidate.curate' -Path $res.path -Message $res.message -Code $code

if ($code -eq 2) {
    Write-IbaPaused -WorkPackage 'candidate-curation' -RunId $runId -Message $res.message
}

exit $code
