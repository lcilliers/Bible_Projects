<#
.SYNOPSIS
    Live progress monitor over `run_batch` (escalation #1756) -- see how far a long-running batch
    step has gotten, mid-run, without waiting for it to finish or reading a background process's
    raw stdout.

.DESCRIPTION
    Read-only. `-FilterRunId`/`-Step`/`-SelectorKey` are all optional and combine with AND:
    `-FilterRunId` narrows to one specific run, `-Step`/`-SelectorKey` narrow to one step/selector
    (e.g. every M49 batch across every run_id that has ever touched it, live or historical). No
    filters at all reports every `run_batch` row currently `status='running'` DB-wide -- the
    live-right-now view -- plus a short recent-activity tail.

.PARAMETER FilterRunId  Narrow to one run_id (the run BEING inspected, not this monitor's own).
.PARAMETER Step         Narrow to one step, e.g. lexical.meaning, cluster.answer.
.PARAMETER SelectorKey  Narrow to one selector, e.g. a cluster_code or cluster_code|subgroup_code.
.PARAMETER RunId        resume/re-tag THIS monitor's own run.
.PARAMETER Trace        Print every config read (IBA_TRACE).

.EXAMPLE
    .\BatchProgress.ps1
    # -> every batch currently running, DB-wide.
.EXAMPLE
    .\BatchProgress.ps1 -Step lexical.meaning -SelectorKey M49
    # -> M49's own verse-reading batch history, every run_id that ever touched it.
#>

[CmdletBinding()]
param(
    [string] $FilterRunId,
    [string] $Step,
    [string] $SelectorKey,
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

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-BATCH-PROGRESS" }

Write-IbaRunHeader -WorkPackage 'batch-progress-report' -Step 'report.batch_progress' -RunId $runId

$paramArgs = @()
if ($FilterRunId) { $paramArgs += @('--param', "FilterRunId=$FilterRunId") }
if ($Step) { $paramArgs += @('--param', "Step=$Step") }
if ($SelectorKey) { $paramArgs += @('--param', "SelectorKey=$SelectorKey") }

$json = python -m iba.app.run batch-progress-report --step report.batch_progress --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'report.batch_progress' -Path $res.path -Message $res.message -Code $code

exit $code
