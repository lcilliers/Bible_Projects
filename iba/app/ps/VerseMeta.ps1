<#
.SYNOPSIS
    verse_meta.status maintenance -- escalation #1661. Dispatched through run.py (work package
    `verse-meta`, step `verse_meta.set_status`, #2207).

.DESCRIPTION
    -Step SetStatus   set `verse_meta.status` for one or more verses, given as a comma-delimited
                       list of references (either osisId, e.g. 'Rom.1.1', or the display form,
                       e.g. 'Rom 1:2' — either is accepted per reference, tried in that order).
                       `status_changed_at` is stamped ONLY when the status actually changes value;
                       re-setting the same status again leaves it untouched. `status` must be a
                       live value of `cfg_enum verse_meta_status` (exclude / citated / analysed —
                       'anchor' is deliberately NOT part of this domain: that's already
                       `verse_meta.is_passage_anchor`, set elsewhere). Exits 1 if the status is not
                       valid or any reference is not found.

.PARAMETER Step         SetStatus
.PARAMETER References   comma-delimited verse references (SetStatus)
.PARAMETER Status       exclude | citated | analysed, per cfg_enum verse_meta_status (SetStatus)
.PARAMETER Trace        Print every config read (IBA_TRACE).

.EXAMPLE
    .\VerseMeta.ps1 -Step SetStatus -References "Gen.1.1,Gen.1.2,Rom 1:3" -Status analysed
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [ValidateSet('SetStatus')] [string] $Step,
    [string] $References,
    [string] $Status,
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

if ($Step -eq 'SetStatus') {
    if (-not $References -or -not $Status) {
        Write-Host "SetStatus needs -References and -Status." -ForegroundColor Yellow
        exit 1
    }
    $runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-VERSE-META"
    Write-IbaRunHeader -WorkPackage 'verse-meta' -RunId $runId

    $json = python -m iba.app.run verse-meta --step verse_meta.set_status --run-id $runId `
        --param "References=$References" --param "Status=$Status"
    $code = $LASTEXITCODE
    $res  = $json | ConvertFrom-Json
    Write-IbaStepResult -Step 'verse_meta.set_status' -Path '' -Message $res.message -Code $code
    if ($res.counts) {
        if ($res.counts.updated)     { Write-Host "  updated: $($res.counts.updated)" }
        if ($res.counts.already_set) { Write-Host "  already set: $($res.counts.already_set)" }
        if ($res.counts.not_found)   { Write-Host "  NOT FOUND: $($res.counts.not_found)" -ForegroundColor Yellow }
    }
    if ($code -eq 0 -and $res.condition -ne 'ok') { exit 1 }
    exit $code
}
