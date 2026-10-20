<#
.SYNOPSIS
    The session compliance file (escalation #2173 P2): the governance settings, behaviour rules
    and escalation rules, restated at start and proved at close.

.DESCRIPTION
    Researcher, 2026-10-20 (verbatim): "You print the config report, but you ignore the content.
    What step can I take as part of the behaviour section to ensure that you read and understood
    the governance and config rules and acknowledge that you will comply with it."

    -Action Template
        Writes this session's compliance file (compliance.dir, COMPLIANCE-<date>-<session>.md)
        with one row per active rule (G:<governance key>, B:<behaviour id>, E:<escalation id>).
        Never overwrites an existing file. Claude then fills it: per rule, what it requires in this
        session in Claude's own words, or "not engaged" with the reason; the acknowledgement
        sentence; every conflict or rule not followed, by id.
    -Action Check -Phase Start
        Checks the file (lib/compliance.check_start): every active rule has a row, none is blank,
        none copies the rule text, the statuses are known, the acknowledgement is present, and
        every rule naming a retired table/step/setting/file is named in the conflicts section.
        Exits 3 while any finding is open: start-project does not end until it passes.
    The close check (evidence for every engaged rule) runs inside Session-Close.ps1 (SC6).

.EXAMPLE
    .\Compliance.ps1 -Action Template
.EXAMPLE
    .\Compliance.ps1 -Action Check -Phase Start
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('Template', 'Check')]
    [string] $Action,
    [ValidateSet('Start')]
    [string] $Phase,
    [switch] $Trace
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'
if ($Trace) { $env:IBA_TRACE = '1' }

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot
. $PSScriptRoot\_lib\Notify.ps1

if ($Action -eq 'Check' -and -not $Phase) {
    Write-Host "Check needs -Phase Start (the close check runs inside Session-Close.ps1)." -ForegroundColor Yellow
    exit 1
}
$stepId = if ($Action -eq 'Template') { 'compliance.template' } else { 'compliance.check_start' }
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-COMPLIANCE"

Write-IbaRunHeader -WorkPackage 'session-compliance' -Step $stepId -RunId $runId
$json = python -m iba.app.run session-compliance --step $stepId --run-id $runId
$code = $LASTEXITCODE
$res = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code
if ($res.condition -eq 'findings-open') {
    Write-Host "  NOT PASSED: fix the compliance file and re-run." -ForegroundColor Red
    exit 3
}
exit $code
