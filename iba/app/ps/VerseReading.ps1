<#
.SYNOPSIS
    The `verse-reading` stage (`lexical.meaning`, escalation #1706 Phase C pipeline stage 1) --
    per-cluster, pre-subgroup Layer 2 lexical-observation + lexical-question-answering pass.
    Standalone single-step entry point onto the `verse-lexical` work package's `lexical.meaning`
    step (ordinal 6) -- this step didn't have a PS entry point until now, found live building this
    (`cfg_behaviour_rule` `every-interactive-module-needs-ps-script`).

.DESCRIPTION
    Resolves the cluster's full member-strong list, then every verse those strongs occur in, then
    calls the LLM in `passage.max_verses`-sized batches (never the whole cluster in one call) --
    always previews cost first (default: `-Live` is NOT given, so nothing is called and nothing is
    written) per `lib/handlers/lexical.py:meaning`'s own safe-default discipline for a newly-built,
    never-yet-run-at-scale mechanism. Every live batch's result is written by `lib/recordingpass.py`
    in the same unit of work it's returned in -- no deferred/batched pickup.

    A live (non-preview) call with no -VerseList resolves and processes the WHOLE cluster's verse
    list. -VerseList (2026-09-22) narrows a run to an explicit, small OSIS-reference subset of that
    same cluster -- for a cheap, disposable live test rather than a full-cluster run; -ClusterCode
    is still required alongside it since member-strong context and prompt framing are the cluster's
    own. cluster.status completeness is still checked after every live call regardless (it's a
    fresh read of the WHOLE cluster's live coverage, not dependent on what this call touched), so a
    -VerseList run cannot falsely advance a cluster that isn't actually complete.

.PARAMETER ClusterCode  The M-code or T-code to read, e.g. M67. Mandatory.
.PARAMETER VerseList    Optional comma-separated OSIS references (e.g. "2Cor.8.8,Rom.12.8") to
                      restrict this run to, instead of the cluster's full remaining-work list.
.PARAMETER Live         Actually call the API and write results. Omit for a preview (cost estimate
                      per batch, no API call, nothing written) -- always preview first.
.PARAMETER Force        (#1824 v10/v11, Fix 3) Bypass the permanent already-committed skip for an
                      explicit, deliberate reconciliation rerun -- every batch in scope gets a
                      genuine fresh LLM call even if identical content was committed before.
                      Never implied by -Live alone; always opt-in. This is the only lever that
                      triggers any correction to existing ib_observation rows -- the update
                      routine (recordingpass.py) only ever reconciles old data as a byproduct of
                      a real rerun's fresh output, never via an offline script.
.PARAMETER RunId        resume/re-tag a specific run.
.PARAMETER Trace        Print every config read (IBA_TRACE).

.EXAMPLE
    .\VerseReading.ps1 -ClusterCode M67
    # -> preview only: batch plan + estimated cost, no API call, nothing written.
.EXAMPLE
    .\VerseReading.ps1 -ClusterCode M67 -Live
    # -> real run: LLM call per batch, recorded via recordingpass.py, cluster.status advanced if
    #    every member strong now has verse-reading coverage.
.EXAMPLE
    .\VerseReading.ps1 -ClusterCode M67 -VerseList "2Cor.8.8,Rom.12.8" -Live
    # -> real run restricted to just those 2 verses.
.EXAMPLE
    .\VerseReading.ps1 -ClusterCode M67 -VerseList "2Cor.8.8,Rom.12.8" -Live -Force
    # -> real, forced rerun of those 2 verses even though they were already committed before --
    #    a genuine reconciliation pass.
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

$stepId = 'lexical.meaning'
$runId  = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-VERSE-READING" }

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
