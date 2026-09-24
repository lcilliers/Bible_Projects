<#
.SYNOPSIS
    The soft-delete purge audit + execute + database retirement -- app-wide, both databases
    (escalation #1766/#1868/#1872/#1873). Standalone work package (chained=0 -- each action is an
    independent step you invoke separately, not a pipeline).

.DESCRIPTION
    -Action Audit (default)  read-only. For every table with a registered soft-delete column,
                             counts soft-deleted rows and flags any table over
                             purge.unsafe_check_min_soft_deleted as UNSAFE if a live row elsewhere
                             still references one of its soft-deleted PKs. Always persists a
                             report (purge.audit_report_path). Removes nothing.
    -Action Execute          recomputes the same safe/unsafe split fresh (never trusts a cached
                             audit) and intersects it with cfg_write_grant, so only explicitly
                             allow-listed tables are ever touched. Default is preview (no -Live):
                             counts only, nothing written. -Live actually deletes every
                             soft-deleted row in each granted-and-currently-safe table, one
                             transaction per database, and verifies each table reads back 0
                             afterward. A table that is UNSAFE or ungranted is always skipped and
                             reported, never silently included. Always persists a report
                             (purge.execute_report_path).
    -Action Retire           physically clears EVERY row (not just soft-deleted) from every table
                             cfg_table marks inactive=1 for -Database (default bible_research) --
                             scope read live from cfg_table every run, never a hardcoded list. Also
                             nulls known FK columns on RETAINED active tables that point into the
                             cleared set, so no kept row is left dangling. Default is preview (no
                             -Live): counts only, nothing written. Always persists a report
                             (purge.retire_database_report_path).

    bible_research.db is in scope for all three actions -- cfg_behaviour_rule
    'bible-research-db-excluded-from-iba-results' explicitly exempts registered DB-hygiene/
    maintenance utilities from the general exclusion (amended 2026-09-24, escalation #1868/#1870).

.PARAMETER Action    Audit (default) | Execute | Retire
.PARAMETER Live      (Execute/Retire only) actually delete. Omit for a preview -- always preview first.
.PARAMETER Database  (Retire only) which database to retire inactive tables from. Default bible_research.
.PARAMETER RunId     resume a specific pending run (reuse the run_id from its first call).
.PARAMETER Trace     Print every config read (IBA_TRACE).

.EXAMPLE
    .\Purge-SoftDeletes.ps1
    # -> Audit (default): read-only report.
.EXAMPLE
    .\Purge-SoftDeletes.ps1 -Action Execute
    # -> preview only: counts of what would be purged, nothing written.
.EXAMPLE
    .\Purge-SoftDeletes.ps1 -Action Execute -Live
    # -> real run: soft-deleted rows physically removed from every granted-and-safe table.
.EXAMPLE
    .\Purge-SoftDeletes.ps1 -Action Retire
    # -> preview only: counts of every row that would be cleared from inactive bible_research.db tables.
.EXAMPLE
    .\Purge-SoftDeletes.ps1 -Action Retire -Live
    # -> real run: every row cleared from every cfg_table.inactive=1 bible_research.db table.
#>

[CmdletBinding()]
param(
    [ValidateSet('Audit', 'Execute', 'Retire')] [string] $Action = 'Audit',
    [switch] $Live,
    [string] $Database = 'bible_research',
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

$stepId = switch ($Action) {
    'Audit'   { 'purge.audit' }
    'Execute' { 'purge.execute' }
    'Retire'  { 'purge.retire_database' }
}
$runId  = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-PURGE-$($Action.ToUpper())" }

Write-IbaRunHeader -WorkPackage 'purge-audit' -Step $stepId -RunId $runId

$paramArgs = @()
if ($Action -eq 'Execute' -or $Action -eq 'Retire') {
    $paramArgs += @('--param', "Preview=$(if ($Live) { 'false' } else { 'true' })")
}
if ($Action -eq 'Retire') {
    $paramArgs += @('--param', "Database=$Database")
}

$json = python -m iba.app.run purge-audit --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code

if ($code -eq 2) {
    Write-IbaPaused -WorkPackage 'purge-audit' -RunId $runId -Message $res.message
}

exit $code
