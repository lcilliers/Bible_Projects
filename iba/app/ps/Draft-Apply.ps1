<#
.SYNOPSIS
    The processing of prepared re-read drafts into the observation record (escalation #2498; design
    outputs/escalation/2498-prior-reread-by-collection-design-v3-20261113.md section 5; method rules DA-01 to DA-04).

.DESCRIPTION
      Check -File <load file>   applies the load inside a savepoint and rolls it back: what a run would do and every problem.
                                Writes nothing to any table.
      Apply -File <load file>   the same, kept, in one transaction; the whole file refused on any problem. Existing
                                observations are changed in place (text only), nodes and roles are added, new observations are
                                written in stage prior-reread; every change is kept with its reason in ib_observation_change.

    Test on a copy first (python -m iba.app.lib.dbsnapshot --copy-to PATH; python -m iba.app.lib.draftapply --db PATH --file FILE
    [--apply]) and take a named snapshot (python -m iba.app.lib.dbsnapshot --reason X --named) before Apply.

.EXAMPLE
    iba\app\ps\Draft-Apply.ps1 -Step Check -File outputs\escalation\2498-pilot-load-v1-20261113.json
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [ValidateSet('Check', 'Apply')] [string] $Step,
    [Parameter(Mandatory = $true)] [string] $File,
    [switch] $Trace
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'
if ($Trace) { $env:IBA_TRACE = '1' }

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot
. $PSScriptRoot\_lib\Notify.ps1

$stepId = @{ Check = 'draft_apply.check'; Apply = 'draft_apply.apply' }[$Step]
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-DRAFTAPPLY"

Write-IbaRunHeader -WorkPackage 'draft-apply' -Step $stepId -RunId $runId
$json = python -m iba.app.run draft-apply --step $stepId --run-id $runId --param "File=$File"
$code = $LASTEXITCODE
$res = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code
exit $code
