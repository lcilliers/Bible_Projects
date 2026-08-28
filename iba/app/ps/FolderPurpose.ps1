<#
.SYNOPSIS
    The `folder_purpose` table editor and its two automated methods — escalation #971
    (`iba/docs/folder-purpose-governance-plan-v5-20260828.md`). One row per folder in the project
    tree, giving the researcher visibility into what every folder is for and its current status.

.DESCRIPTION
    -Action Seed        Method A — full reconciliation against the live tree: new folders inserted,
                         folders no longer on disk marked status='deleted' (soft, never removed),
                         every row's disk-derived columns (file counts, extensions, mtime)
                         refreshed. Never touches type/status(other than 'deleted')/
                         usage_description.
    -Action CrossCheck   Method B — re-derives governed_by_setting from live cfg_setting `*_dir`/
                         `*_path` values; pre-fills type='operations'/status='authoritative' for any
                         row a setting already names unambiguously; reports the invariant's
                         anomalies (a type='operations' row with no governed_by_setting, or a
                         cfg_setting pointing at a folder with no row here at all).
    -Action AutoAssess   Method D — fills type/status for every row still missing either, from
                         Methods A/B's own gathered facts only (never guesses 'mixed'/'reallocate',
                         or a category-less folder's type — those stay for -Action Set).
    -Action Set          Method C — hand-set -Type/-Status/-UsageDescription for one -FolderPath.
                         The only sanctioned way to change those three columns; every other column
                         is owned by Seed/CrossCheck and would be overwritten on the next run anyway.
    -Action List         Method C — list rows, optionally filtered by -Type/-Status/-TopLevelRoot.
    -Action Show         Method C — full detail for one -FolderPath.

.PARAMETER Action           Seed | CrossCheck | Set | List | Show
.PARAMETER FolderPath       (Set/Show) the folder_path to act on, e.g. "iba/docs"
.PARAMETER Type             (Set) archive | operations | results
.PARAMETER Status           (Set) authoritative | mixed | reallocate | stale | deleted
.PARAMETER UsageDescription (Set) free text — what this folder is actually for
.PARAMETER TopLevelRoot     (List) filter to one top-level root, e.g. "iba"
.PARAMETER RunId            resume/re-tag a specific run.
.PARAMETER Trace            Print every config read (IBA_TRACE).

.EXAMPLE
    iba/app/ps/FolderPurpose.ps1 -Action Seed
.EXAMPLE
    iba/app/ps/FolderPurpose.ps1 -Action CrossCheck
.EXAMPLE
    iba/app/ps/FolderPurpose.ps1 -Action Set -FolderPath "outputs/escalation" -Type operations `
        -Status authoritative -UsageDescription "Escalation.ps1's own auto-generated list/history exports only."
.EXAMPLE
    iba/app/ps/FolderPurpose.ps1 -Action List -Status mixed
.EXAMPLE
    iba/app/ps/FolderPurpose.ps1 -Action Show -FolderPath "docs"
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('Seed', 'CrossCheck', 'AutoAssess', 'Set', 'List', 'Show')]
    [string] $Action,
    [string] $FolderPath,
    [ValidateSet('archive', 'operations', 'results')] [string] $Type,
    [ValidateSet('authoritative', 'mixed', 'reallocate', 'stale', 'deleted')] [string] $Status,
    [string] $UsageDescription,
    [string] $TopLevelRoot,
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

$stepMap = @{ Seed = 'folderpurpose.seed'; CrossCheck = 'folderpurpose.crosscheck';
             AutoAssess = 'folderpurpose.autoassess';
             Set = 'folderpurpose.set'; List = 'folderpurpose.list'; Show = 'folderpurpose.show' }
$stepId = $stepMap[$Action]
$runId  = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-FOLDERPURPOSE" }

$paramArgs = @()
if ($Action -eq 'Set') {
    if (-not $FolderPath) {
        Write-Host "Set needs -FolderPath." -ForegroundColor Yellow
        exit 1
    }
    $paramArgs += @('--param', "FolderPath=$FolderPath")
    if ($Type)             { $paramArgs += @('--param', "Type=$Type") }
    if ($Status)            { $paramArgs += @('--param', "Status=$Status") }
    if ($UsageDescription)  { $paramArgs += @('--param', "UsageDescription=$UsageDescription") }
}
if ($Action -eq 'Show') {
    if (-not $FolderPath) {
        Write-Host "Show needs -FolderPath." -ForegroundColor Yellow
        exit 1
    }
    $paramArgs += @('--param', "FolderPath=$FolderPath")
}
if ($Action -eq 'List') {
    if ($Type)          { $paramArgs += @('--param', "Type=$Type") }
    if ($Status)         { $paramArgs += @('--param', "Status=$Status") }
    if ($TopLevelRoot)   { $paramArgs += @('--param', "TopLevelRoot=$TopLevelRoot") }
}

Write-IbaRunHeader -WorkPackage 'folder-purpose' -Step $stepId -RunId $runId

$json = python -m iba.app.run folder-purpose --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Message $res.message -Code $code

exit $code
