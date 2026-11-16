<#
.SYNOPSIS
    The `verse-reading` stage's RELATIONAL half (`lexical.relational`, escalation #1860 word-level/
    relational split, 2026-09-23) -- per-cluster, pre-subgroup Layer 2 pass answering M0.6.5/M0.6.6/
    D7.7.1/M0.7.1-16/M0.8.1. Standalone single-step entry point onto the `verse-lexical` work
    package's `lexical.relational` step (ordinal 7), mirroring `VerseReading.ps1` (`lexical.meaning`,
    the word-level half) exactly.

.DESCRIPTION
    Run AFTER `VerseReading.ps1` (`lexical.meaning`) has covered the same verses -- a hard readiness
    gate refuses to run against any verse whose M-code words don't already have a committed
    word-level observation (relational reading grounds on those committed findings, alongside the
    raw lexicon, per the researcher's own #1860 v3 approval: "the base data must in any case be
    included for relational phase to be successful"). Resolves the cluster's full member-strong
    list, then every verse those strongs occur in, then calls the LLM in
    `lexical.relational_max_verses_per_batch`-sized batches (never the whole cluster in one call) --
    always previews cost first (default: `-Live` is NOT given, so nothing is called and nothing is
    written).

    A live (non-preview) call with no -VerseList resolves and processes the WHOLE cluster's verse
    list. -VerseList narrows a run to an explicit, small OSIS-reference subset of that same cluster
    -- for a cheap, disposable live test rather than a full-cluster run; -ClusterCode is still
    required alongside it since member-strong context and prompt framing are the cluster's own.
    cluster.status completeness (the true final transition of verse-reading, moved here from
    `lexical.meaning` by the split) is checked after every live call regardless.

.PARAMETER ClusterCode  The M-code or T-code to read, e.g. M67. Mandatory.
.PARAMETER VerseList    Optional comma-separated OSIS references (e.g. "2Cor.8.8,Rom.12.8") to
                      restrict this run to, instead of the cluster's full remaining-work list.
.PARAMETER Live         Actually call the API and write results. Omit for a preview (cost estimate
                      per batch, no API call, nothing written) -- always preview first.
.PARAMETER Force        Bypass the permanent already-committed skip AND the whole-verse fully-
                      covered exclusion for an explicit, deliberate reconciliation rerun -- every
                      batch in scope gets a genuine fresh LLM call even if identical content was
                      committed before. Does NOT bypass the readiness gate (that is a correctness
                      precondition, not a reconciliation-skip mechanism) -- a verse with genuinely
                      missing word-level coverage still blocks even with -Force.
.PARAMETER RunId        resume/re-tag a specific run.
.PARAMETER Trace        Print every config read (IBA_TRACE).

.EXAMPLE
    .\RelationalReading.ps1 -ClusterCode M67
    # -> preview only: batch plan + estimated cost, no API call, nothing written.
.EXAMPLE
    .\RelationalReading.ps1 -ClusterCode M67 -Live
    # -> real run: LLM call per batch, recorded via recordingpass.py, cluster.status advanced if
    #    every member strong now has verse-reading coverage.
.EXAMPLE
    .\RelationalReading.ps1 -ClusterCode M67 -VerseList "2Cor.8.8,Rom.12.8" -Live
    # -> real run restricted to just those 2 verses (must already have word-level coverage).
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [string] $ClusterCode,
    [string] $VerseList,
    [switch] $Live,
    [switch] $Force,
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

Test-IbaWorkPackageActive -WorkPackage 'verse-lexical'

$stepId = 'lexical.relational'
$runId  = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-RELATIONAL-READING" }

$runsOver = if ($VerseList) { "cluster_code = '$ClusterCode', verses = '$VerseList'" } else { "cluster_code = '$ClusterCode'" }
Write-IbaRunHeader -WorkPackage 'verse-lexical' -Step $stepId -RunId $runId -RunsOver $runsOver

$paramArgs = @('--param', "ClusterCode=$ClusterCode")
$paramArgs += @('--param', "Preview=$(if ($Live) { 'false' } else { 'true' })")
if ($VerseList) { $paramArgs += @('--param', "VerseList=$VerseList") }
if ($Force) { $paramArgs += @('--param', "Force=true") }

$json = python -m iba.app.run verse-lexical --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code

exit $code
