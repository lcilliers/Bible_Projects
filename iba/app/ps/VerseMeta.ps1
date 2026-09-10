<#
.SYNOPSIS
    verse_meta.status maintenance — escalation #1661. Standalone utility (like Escalation.ps1),
    not a run.py dispatcher step, since this is a direct researcher-driven maintenance action, not
    a repeatable pipeline stage.

.DESCRIPTION
    -Step SetStatus   set `verse_meta.status` for one or more verses, given as a comma-delimited
                       list of references (either osisId, e.g. 'Rom.1.1', or the display form,
                       e.g. 'Rom 1:2' — either is accepted per reference, tried in that order).
                       `status_changed_at` is stamped ONLY when the status actually changes value;
                       re-setting the same status again leaves it untouched. `status` must be a
                       live value of `cfg_enum verse_meta_status` (exclude / citated / analysed —
                       'anchor' is deliberately NOT part of this domain: that's already
                       `verse_meta.is_passage_anchor`, set elsewhere).

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
    python -m iba.app.lib.versemeta set-status --references $References --status $Status
    exit $LASTEXITCODE
}
