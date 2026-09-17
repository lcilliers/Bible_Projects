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

    A live (non-preview) call always resolves and processes the WHOLE cluster's verse list -- there
    is no partial/manual verse selector on this step, by design (the handler's own comment: this is
    what lets it check verse-reading completeness and advance `cluster.status` to
    `ready_for_subgroup_allocation` the moment the full cluster is done).

.PARAMETER ClusterCode  The M-code or T-code to read, e.g. M67. Mandatory.
.PARAMETER Live         Actually call the API and write results. Omit for a preview (cost estimate
                      per batch, no API call, nothing written) -- always preview first.
.PARAMETER RunId        resume/re-tag a specific run.
.PARAMETER Trace        Print every config read (IBA_TRACE).

.EXAMPLE
    .\VerseReading.ps1 -ClusterCode M67
    # -> preview only: batch plan + estimated cost, no API call, nothing written.
.EXAMPLE
    .\VerseReading.ps1 -ClusterCode M67 -Live
    # -> real run: LLM call per batch, recorded via recordingpass.py, cluster.status advanced if
    #    every member strong now has verse-reading coverage.
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [string] $ClusterCode,
    [switch] $Live,
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

Write-IbaRunHeader -WorkPackage 'verse-lexical' -Step $stepId -RunId $runId -RunsOver "cluster_code = '$ClusterCode'"

$paramArgs = @('--param', "ClusterCode=$ClusterCode")
$paramArgs += @('--param', "Preview=$(if ($Live) { 'false' } else { 'true' })")

$json = python -m iba.app.run verse-lexical --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code

exit $code
