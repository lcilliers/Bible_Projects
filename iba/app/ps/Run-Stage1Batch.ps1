<#
.SYNOPSIS
    Batch controller for `lexical.meaning` (Stage 1 verse-reading) -- runs an explicit list of
    clusters sequentially, unattended, so a multi-cluster pass can run in the background while
    progress is watched separately with `BatchProgress.ps1` (escalation #1756's own monitor, read-
    only over `run_batch` -- `lexical.meaning` already writes there via `batchcontrol.py`, so no
    new monitoring mechanism was needed, only this orchestration layer).

.DESCRIPTION
    A thin PS-level loop over the SAME single-cluster step `VerseReading.ps1` already dispatches
    (`python -m iba.app.run verse-lexical --step lexical.meaning`) -- no new Python step, no
    duplicated pipeline logic. Per cluster, in the given order: run the step, parse its own result,
    accumulate real spend, and stop immediately on the first real failure (never silently continue
    past an error to the next cluster) or once `-MaxTotalCostUsd` would be exceeded (checked BEFORE
    each cluster starts, using that cluster's own preview estimate -- never mid-cluster). Always
    previews the whole list first (default, no `-Live`) so the full plan and total estimated cost
    are visible before any API spend; `-Live` executes for real.

    Every cluster's own result (and the running total) is printed as it completes, and the full
    batch's own summary is persisted to `outputs/stage1-batch-{run_id}.csv` (one row per cluster)
    so the run is auditable after the fact even if nobody watched it live.

    Deliberately does NOT auto-resolve which clusters need running -- `-ClusterCodes` is always an
    explicit list the caller decided. Auto-selecting "every incomplete M-code cluster" is a policy
    decision (which clusters, what order, what counts as "needs running") not made here; this
    controller only executes a given plan, it doesn't build one.

.PARAMETER ClusterCodes    Comma-separated list of cluster codes to run, in order, e.g.
                         "M35,M51,M61". Mandatory.
.PARAMETER Live            Actually call the API and write results, per cluster. Omit for a
                         preview across the whole list (every cluster's own cost estimate, a
                         running total, no API calls, nothing written).
.PARAMETER MaxTotalCostUsd Cumulative safety cap across the WHOLE batch (not per-cluster --
                         `lexical.llm_max_cost_per_batch` already caps that). Checked before each
                         cluster starts using its own preview estimate; if starting it would push
                         the running total over the cap, the batch stops there and reports which
                         clusters were never attempted. Optional -- omit for no cap (still bounded
                         by each individual cluster's own existing per-batch cap).
.PARAMETER RunId           resume/re-tag a specific run.
.PARAMETER Trace           Print every config read (IBA_TRACE).

.EXAMPLE
    .\Run-Stage1Batch.ps1 -ClusterCodes "M35,M51,M61"
    # -> preview only: every cluster's own estimated cost + a running total, no API calls.
.EXAMPLE
    .\Run-Stage1Batch.ps1 -ClusterCodes "M35,M51,M61" -Live -MaxTotalCostUsd 15.00
    # -> real run, all 3 clusters, stops before starting any cluster that would push the running
    #    total over $15.
.EXAMPLE
    # in a second terminal, while the above runs:
    .\BatchProgress.ps1 -Step lexical.meaning
    # -> live progress on whichever cluster is currently running.
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [string] $ClusterCodes,
    [switch] $Live,
    [double] $MaxTotalCostUsd,
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

$batchRunId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-STAGE1-BATCH" }
# @(...) forces an array even for a single cluster code -- PowerShell unwraps a single-item
# pipeline result to a bare scalar otherwise, and a scalar has no .Count, found live testing a
# one-cluster call ("The property 'Count' cannot be found on this object").
$clusters = @(($ClusterCodes -split ',') | ForEach-Object { $_.Trim() } | Where-Object { $_ })
if ($clusters.Count -eq 0) {
    Write-Host "No cluster codes given." -ForegroundColor Yellow
    exit 1
}

Write-Host "Stage 1 batch controller -- run_id $batchRunId"
Write-Host "  clusters ($($clusters.Count)): $($clusters -join ', ')"
Write-Host "  mode: $(if ($Live) { 'LIVE' } else { 'PREVIEW (no API calls, nothing written)' })"
if ($MaxTotalCostUsd) { Write-Host "  cumulative cost cap: `$$MaxTotalCostUsd" }
Write-Host ""

$rows = @()
$runningTotal = 0.0
$stoppedEarly = $false
$stopReason = $null

for ($i = 0; $i -lt $clusters.Count; $i++) {
    $cc = $clusters[$i]
    $subRunId = "$batchRunId-$cc"

    # Always preview first, regardless of -Live, so the cap check below has a real estimate to
    # weigh BEFORE spending anything on this cluster.
    $previewArgs = @('--param', "ClusterCode=$cc", '--param', 'Preview=true')
    $previewJson = python -m iba.app.run verse-lexical --step lexical.meaning --run-id "$subRunId-preview" @previewArgs
    $previewCode = $LASTEXITCODE
    if ($previewCode -ne 0) {
        Write-Host "[$($i+1)/$($clusters.Count)] $cc -- PREVIEW FAILED, stopping batch: $previewJson" -ForegroundColor Red
        $stoppedEarly = $true
        $stopReason = "preview failed for $cc"
        $rows += [pscustomobject]@{ cluster_code = $cc; status = 'preview-failed'; est_cost_usd = 0
                                    actual_cost_usd = 0; message = "$previewJson" }
        break
    }
    $preview = $previewJson | ConvertFrom-Json
    # Only batches NOT already committed actually cost anything (matches lexical.meaning's own
    # "remaining work" semantics exactly -- summing every batch regardless double-counted already-
    # committed ones here, found live testing a single-cluster call: reported $9.82 when the
    # step's own message said $2.03). `counts.batches` is also absent entirely when the whole
    # cluster is already fully covered (the newer "nothing to do" preview shape) -- guard for that.
    $estCost = 0.0
    if ($preview.counts.batches) {
        $remaining = @($preview.counts.batches | Where-Object { -not $_.already_committed })
        if ($remaining.Count -gt 0) {
            $estCost = [double]($remaining | Measure-Object -Property est_cost_usd -Sum).Sum
        }
    }

    if ($MaxTotalCostUsd -and ($runningTotal + $estCost) -gt $MaxTotalCostUsd) {
        Write-Host "[$($i+1)/$($clusters.Count)] $cc -- SKIPPED, estimated `$$([math]::Round($estCost,4)) would push the running total (`$$([math]::Round($runningTotal,4))) over the `$$MaxTotalCostUsd cap" -ForegroundColor Yellow
        $stoppedEarly = $true
        $stopReason = "cost cap reached before $cc"
        $rows += [pscustomobject]@{ cluster_code = $cc; status = 'skipped-cost-cap'; est_cost_usd = $estCost
                                    actual_cost_usd = 0; message = 'not attempted -- would exceed -MaxTotalCostUsd' }
        break
    }

    if (-not $Live) {
        Write-Host "[$($i+1)/$($clusters.Count)] $cc -- PREVIEW: $($preview.message)"
        $rows += [pscustomobject]@{ cluster_code = $cc; status = 'previewed'; est_cost_usd = $estCost
                                    actual_cost_usd = 0; message = $preview.message }
        $runningTotal += $estCost
        continue
    }

    $liveArgs = @('--param', "ClusterCode=$cc", '--param', 'Preview=false')
    $liveJson = python -m iba.app.run verse-lexical --step lexical.meaning --run-id $subRunId @liveArgs
    $liveCode = $LASTEXITCODE
    # NOT named $live -- PowerShell variable names are case-insensitive, so $live and the script's
    # own [switch] $Live parameter are THE SAME VARIABLE. Assigning the parsed JSON into $live
    # silently failed every single time ("Cannot convert value ... PSCustomObject ... to type ...
    # SwitchParameter", caught and swallowed by the try/catch below) because it was really trying
    # to overwrite -Live's own bound switch value -- every live run was misreported as FAILED even
    # when the underlying step succeeded and real work was committed. Found live: a $0-cost rerun
    # of an already-fully-committed cluster still "failed" the same way, isolating the bug to this
    # variable collision, not anything about the API call itself.
    $liveResult = $null
    try { $liveResult = $liveJson | ConvertFrom-Json } catch { }

    if ($liveCode -ne 0 -or -not $liveResult) {
        Write-Host "[$($i+1)/$($clusters.Count)] $cc -- FAILED, stopping batch (never silently continue past a real error): $liveJson" -ForegroundColor Red
        $stoppedEarly = $true
        $stopReason = "$cc failed"
        $rows += [pscustomobject]@{ cluster_code = $cc; status = 'failed'; est_cost_usd = $estCost
                                    actual_cost_usd = 0; message = "$liveJson" }
        break
    }

    $actualCost = 0.0
    if ($liveResult.counts.llm_calls) {
        $actualCost = [double]($liveResult.counts.llm_calls | Measure-Object -Property cost_usd -Sum).Sum
    }
    $runningTotal += $actualCost
    Write-Host "[$($i+1)/$($clusters.Count)] $cc -- `$$([math]::Round($actualCost,4)) spent (running total `$$([math]::Round($runningTotal,4))): $($liveResult.message)"
    $rows += [pscustomobject]@{ cluster_code = $cc; status = 'completed'; est_cost_usd = $estCost
                                actual_cost_usd = $actualCost; message = $liveResult.message }
}

$reportPath = "outputs/stage1-batch-$batchRunId.csv"
$rows | Export-Csv -Path $reportPath -NoTypeInformation -Encoding UTF8

$attempted = @($rows | Where-Object { $_.status -in @('completed', 'previewed') }).Count
$skipped = @($rows | Where-Object { $_.status -notin @('completed', 'previewed') }).Count
Write-Host ""
Write-Host "Batch $(if ($stoppedEarly) { "STOPPED EARLY ($stopReason)" } else { 'complete' }) -- $attempted of $($clusters.Count) cluster(s) attempted$(if ($skipped) { ", $skipped not attempted" }), running total `$$([math]::Round($runningTotal,4))"
Write-Host "Report: $reportPath"
if ($Live) {
    Write-Host "Monitor a still-running batch from another terminal with: .\BatchProgress.ps1 -Step lexical.meaning"
}

exit $(if ($stoppedEarly -and $stopReason -like '*failed*') { 1 } else { 0 })
