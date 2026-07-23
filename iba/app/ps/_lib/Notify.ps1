<#
.SYNOPSIS
    Shared terminal-notification rendering — dot-sourced by every work-package PS script instead
    of each hardcoding its own Write-Host strings. Reads wording from `notification.*` settings and
    `cfg_work_package.complete_message/next_step_hint/paused_message` (added 2026-07-22,
    PLAN-reports-config-governance-v1-20260722.md Phase 0d) — the English text lives in config, not
    in this file or the 12 wrapper scripts.

.DESCRIPTION
    Dot-source this file, then call:
      Write-IbaNotInitialised
      Write-IbaRunHeader -WorkPackage <name> [-Step <id>] -RunId <id> [-RunsOver <text>]
      Write-IbaStepResult -Step <id> -Path <path> -Message <msg> -Code <exitcode>
      Write-IbaPaused -WorkPackage <name> -RunId <id> [-Message <msg>]
      Write-IbaStopped -Message <msg>
      Write-IbaComplete -WorkPackage <name> [-Vars <hashtable>]
    Templates are fetched once per process (memoized) via a single `python -c` call — the same
    "one python round trip" pattern the readiness guard already uses.
#>

$script:_ibaNotif = $null
$script:_ibaWpCache = @{}

function _IbaLoadNotifications {
    if ($null -ne $script:_ibaNotif) { return }
    $json = python -c @'
import json
from iba.app.lib.cfg import Cfg
c = Cfg()
keys = ["notification.not_initialised", "notification.header_work_package",
        "notification.header_step", "notification.header_run_id",
        "notification.header_runs_over", "notification.step_result_line",
        "notification.paused_banner_guided", "notification.paused_banner_passthrough",
        "notification.stopped_banner"]
print(json.dumps({k: c.setting(k) for k in keys}))
c.close()
'@
    $script:_ibaNotif = $json | ConvertFrom-Json
}

function _IbaWorkPackageRow([string] $WorkPackage) {
    if ($script:_ibaWpCache.ContainsKey($WorkPackage)) { return $script:_ibaWpCache[$WorkPackage] }
    $json = python -c @"
import json
from iba.app.lib.cfg import Cfg
c = Cfg()
r = c.conn.execute('SELECT chained, complete_message, next_step_hint, paused_message FROM cfg_work_package WHERE name=?', ('$WorkPackage',)).fetchone()
print(json.dumps(dict(r) if r else {}))
c.close()
"@
    $row = $json | ConvertFrom-Json
    $script:_ibaWpCache[$WorkPackage] = $row
    return $row
}

function _IbaFormat([string] $Template, [hashtable] $Vars) {
    $out = $Template
    foreach ($k in $Vars.Keys) { $out = $out.Replace("{$k}", [string]$Vars[$k]) }
    return $out
}

function Write-IbaNotInitialised {
    # can fire before cfg_setting even exists (a truly fresh clone) — falls back to the literal
    # text rather than crashing on the very guard meant to catch "not initialised".
    try {
        _IbaLoadNotifications
        $msg = $script:_ibaNotif.'notification.not_initialised'
    } catch {
        $msg = $null
    }
    if (-not $msg) { $msg = "The app is not initialised. Run first:  iba\app\ps\Start-Iba.ps1" }
    Write-Host $msg -ForegroundColor Yellow
}

function Write-IbaRunHeader {
    param(
        [Parameter(Mandatory)] [string] $WorkPackage,
        [string] $Step,
        [Parameter(Mandatory)] [string] $RunId,
        [string] $RunsOver
    )
    _IbaLoadNotifications
    Write-Host ""
    Write-Host (_IbaFormat $script:_ibaNotif.'notification.header_work_package' @{ work_package = $WorkPackage })
    if ($Step) {
        Write-Host (_IbaFormat $script:_ibaNotif.'notification.header_step' @{ step = $Step })
    }
    Write-Host (_IbaFormat $script:_ibaNotif.'notification.header_run_id' @{ run_id = $RunId })
    if ($RunsOver) {
        Write-Host (_IbaFormat $script:_ibaNotif.'notification.header_runs_over' @{ runs_over = $RunsOver })
    }
    Write-Host ""
}

function Write-IbaStepResult {
    param(
        [Parameter(Mandatory)] [string] $Step,
        [string] $Path,
        [string] $Message,
        [Parameter(Mandatory)] [int] $Code
    )
    _IbaLoadNotifications
    $colour = @{ 0 = 'Green'; 2 = 'Yellow'; 3 = 'Red' }[$Code]
    Write-Host ($script:_ibaNotif.'notification.step_result_line' -f $Step, $Path, $Message) -ForegroundColor $colour
}

function Write-IbaPaused {
    param(
        [Parameter(Mandatory)] [string] $WorkPackage,
        [Parameter(Mandatory)] [string] $RunId,
        [string] $Message
    )
    _IbaLoadNotifications
    $wp = _IbaWorkPackageRow $WorkPackage
    Write-Host ""
    if ($wp.chained) {
        $text = if ($wp.paused_message) { $wp.paused_message } else {
            _IbaFormat $script:_ibaNotif.'notification.paused_banner_passthrough' @{ message = $Message }
        }
        Write-Host "PAUSED — $text" -ForegroundColor Yellow
    } else {
        $text = _IbaFormat $script:_ibaNotif.'notification.paused_banner_guided' @{ run_id = $RunId }
        foreach ($line in ($text -split "`n")) { Write-Host $line -ForegroundColor Yellow }
    }
}

function Write-IbaStopped {
    param([Parameter(Mandatory)] [string] $Message)
    _IbaLoadNotifications
    Write-Host (_IbaFormat $script:_ibaNotif.'notification.stopped_banner' @{ message = $Message }) -ForegroundColor Red
}

function Write-IbaComplete {
    param(
        [Parameter(Mandatory)] [string] $WorkPackage,
        [hashtable] $Vars = @{}
    )
    $wp = _IbaWorkPackageRow $WorkPackage
    Write-Host ""
    if ($wp.complete_message) {
        Write-Host ("COMPLETE — " + (_IbaFormat $wp.complete_message $Vars)) -ForegroundColor Green
    }
    if ($wp.next_step_hint) {
        Write-Host ("  " + (_IbaFormat $wp.next_step_hint $Vars))
    }
}
