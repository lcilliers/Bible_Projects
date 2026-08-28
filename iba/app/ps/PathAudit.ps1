<#
.SYNOPSIS
    Project-wide scan for hardcoded folder/file-path string literals that should be
    `cfg_setting`/`cfg.module_setting()`-driven instead — escalation #971/#976. The automated
    successor to the one-off manual sweep (escalation #648) for the location subset specifically.

.DESCRIPTION
    Scans every `.py` file project-wide EXCEPT one whose `cfg_utility` row is `inactive=1` (the
    researcher's own scope, 2026-08-28: "the only scripts to not include, are scripts that is
    marked as inactive"). A file with no `cfg_utility` row at all IS included — not being
    registered is `configmaint.validate`'s own `unregistered_project_scripts` finding, not a reason
    to skip it here too. See `iba/app/lib/pathaudit.py`'s own docstring for the exact method and
    its honest limits — ADVISORY, every finding needs a look, not an auto-fix.

.PARAMETER RunId  resume/re-tag a specific run.
.PARAMETER Trace  Print every config read (IBA_TRACE).

.EXAMPLE
    iba/app/ps/PathAudit.ps1 -Action Scan
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('Scan')]
    [string] $Action,
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

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-PATHAUDIT" }

Write-IbaRunHeader -WorkPackage 'path-audit' -Step 'pathaudit.scan' -RunId $runId

$json = python -m iba.app.run path-audit --step pathaudit.scan --run-id $runId
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step 'pathaudit.scan' -Path $res.path -Message $res.message -Code $code

exit $code
