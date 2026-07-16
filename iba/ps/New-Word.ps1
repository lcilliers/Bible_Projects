<#
.SYNOPSIS
    Create a new registry word and build it out.  STUB — nothing is built out.

.DESCRIPTION
    This is the PowerShell script that starts the `new-word` WORK PACKAGE.

    It owns NO process logic.  The order of work lives in the config:
        iba/config/utility/run.json
          -> ent.run.work-package
             -> work_packages[code = "new-word"].sequence

    The script loads that sequence into memory and walks it.  Each entry names
    the step, the config that holds its rules, the module it belongs to, and
    what it runs over.  To change the order of work, change run.json — not this
    file (run.sequence-is-loaded).

    SCOPE COMES FROM HERE, NOT FROM THE MODULE.  This package runs over ONE
    WORD.  Every sub-process in the sequence inherits that unless its entry says
    otherwise (run.scope-from-context).

.PARAMETER Word
    The English inner-being word to register.

.PARAMETER Source
    Why it is being registered.  Feeds registry.growth, which requires every
    addition to carry its trigger and reason.

.PARAMETER Anchors
    Optional.  Explicit Strong's codes.  When given, term discovery is skipped.

.PARAMETER IncludeRelated
    Optional, default off.  Pull verses and meaning for related terms too.
    See raw.include-related.

.PARAMETER DryRun
    Plan and validate; write nothing.

.EXAMPLE
    .\New-Word.ps1 -Word "anger" -Source "gap scan 2026-07-16" -DryRun

.NOTES
    ⚠ STUB.  Every Invoke-Step call below is a HANDLE, not an implementation.
    ⚠ The handler contract is NOT agreed — see run.json open.run.handler-contract.
       Until it is, nothing can be called.  All 40 steps in pipeline.json declare
       handler: null.
    ⚠ step.registry.signoff DOES NOT EXIST.  The sequence names it because the
       work package needs it; the researcher is taking registry separately.
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [string] $Word,
    [Parameter(Mandatory = $true)] [string] $Source,
    [string] $Anchors,
    [switch] $IncludeRelated,
    [switch] $DryRun
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$RepoRoot   = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$ConfigRoot = Join-Path $RepoRoot 'iba\config'
$PackageCode = 'new-word'


function Get-WorkPackage {
    <#  Load the work package from run.json.  The sequence is config, not code. #>
    param([string] $Code)

    $runCfg = Get-Content (Join-Path $ConfigRoot 'utility\run.json') -Raw | ConvertFrom-Json
    $entity = $runCfg.entities | Where-Object { $_.id -eq 'ent.run.work-package' }
    $pkg    = $entity.spec.work_packages | Where-Object { $_.code -eq $Code }
    if (-not $pkg) { throw "Work package '$Code' is not declared in run.json." }
    return $pkg
}


function New-RunRecord {
    <#  ent.run.record — pin the run to a config version BEFORE any work.
        'The config that ran' must be a record, not an assumption. #>
    param([string] $Package, [hashtable] $Params, [string] $RunsOver)

    $manifest = Get-Content (Join-Path $ConfigRoot '_manifest.json') -Raw | ConvertFrom-Json
    # STUB — writes nothing yet.
    return [pscustomobject]@{
        run_id         = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss')-$($Package.ToUpper())"
        work_package   = $Package
        params         = $Params
        runs_over      = $RunsOver
        config_version = $manifest.config_version
        started_at     = (Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ')
    }
}


function Invoke-Step {
    <#  ⚠ THE HANDLE.  Calls one sub-process.

        BLOCKED: open.run.handler-contract.  Nothing states what a handler is
        given or what it returns, and every step declares handler: null.  This
        function exists so the cross-reference from run.json -> pipeline.json ->
        a callable thing is in place.  It calls nothing. #>
    param(
        [Parameter(Mandatory)] $Entry,     # one sequence entry from run.json
        [Parameter(Mandatory)] $Run,       # the run record
        [string] $Scope                    # inherited from the package unless overridden
    )

    $effectiveScope = if ($Entry.PSObject.Properties['scope']) { $Entry.scope } else { $Scope }

    Write-Host ("  {0,-34} {1,-16} scope={2}" -f $Entry.step, $Entry.module, $effectiveScope)
    Write-Host ("      rules : {0}" -f $Entry.config)
    Write-Host ("      does  : {0}" -f $Entry.does)

    if ($Entry.PSObject.Properties['raises']) {
        Write-Host ("      raises: {0}   ⚠ trigger mechanism not agreed (open.run.trigger-mechanism)" -f $Entry.raises) -ForegroundColor DarkYellow
    }
    if ($Entry.PSObject.Properties['triggered_by']) {
        Write-Host ("      called by trigger: {0}" -f $Entry.triggered_by) -ForegroundColor DarkYellow
    }
    if ($Entry.PSObject.Properties['⚠ REVIEW']) {
        Write-Host ("      ⚠ REVIEW: {0}" -f $Entry.'⚠ REVIEW') -ForegroundColor Yellow
    }

    # ⚠ STUB — no handler is called.  See open.run.handler-contract.
    return [pscustomobject]@{ step = $Entry.step; outcome = 'NOT-IMPLEMENTED' }
}


function Invoke-PreFlight {
    <#  Gates that must pass before the package starts.
        - check.step.up          (utility/step.json)  STEP is up AND tagged, else halt and warn
        - gate.cfgmaint.no-reconcile-in-scope         a run refuses to start on a contested rule
        ⚠ STUB. #>
    param($Run)
    Write-Host "[pre-flight] check.step.up · gate.cfgmaint.no-reconcile-in-scope   ⚠ STUB" -ForegroundColor DarkGray
}


# ── the work package ─────────────────────────────────────────────────────────

$pkg = Get-WorkPackage -Code $PackageCode

$params = @{
    Word           = $Word
    Source         = $Source
    Anchors        = $Anchors
    IncludeRelated = [bool]$IncludeRelated
    DryRun         = [bool]$DryRun
}
$run = New-RunRecord -Package $PackageCode -Params $params -RunsOver $pkg.runs_over

Write-Host ""
Write-Host "work package : $($pkg.code) — $($pkg.name)"
Write-Host "run_id       : $($run.run_id)"
Write-Host "config       : $($run.config_version)"
Write-Host "runs over    : $($pkg.runs_over) = '$Word'"
Write-Host "sequence     : $($pkg.sequence.Count) sub-process(es), loaded from run.json"
if ($DryRun) { Write-Host "mode         : DRY RUN — nothing will be written" -ForegroundColor Cyan }
Write-Host ""

Invoke-PreFlight -Run $run

Write-Host ""
Write-Host "[sequence]"
$results = foreach ($entry in $pkg.sequence) {
    Invoke-Step -Entry $entry -Run $run -Scope $pkg.runs_over
}

Write-Host ""
Write-Host "[end validation]  run.ends-in-validation — a package is done when its end validation" -ForegroundColor DarkGray
Write-Host "                  passes, not when its last task returns.   ⚠ STUB" -ForegroundColor DarkGray
Write-Host ""
Write-Host "STUB — $($results.Count) sub-process(es) walked, 0 executed." -ForegroundColor Yellow
Write-Host "Blocked on: open.run.handler-contract (what a handler is given and returns)." -ForegroundColor Yellow
