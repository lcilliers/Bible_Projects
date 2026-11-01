<#
.SYNOPSIS
    Edit the concept grouping: descriptions, new domains, a domain's delete flag (escalation #2355).

.DESCRIPTION
    The concept grouping is the tables concept_domain (a chapter of the narrative), concept (a sub-chapter
    in a domain) and concept_subgroup (the link table, not touched here).

      List        the domains and concepts with their descriptions: -Level Domain|Concept (both when
                  left off), -DomainId n (the concepts of one domain), -IncludeDeleted
      Describe    -Level Domain|Concept -Id n -Description "<text>"   set one description (the wording it
                  replaces is shown); or -File <list.json>, a JSON list of
                  {"level": "Concept", "id": 12, "description": "..."} set as one unit
      AddDomain   -Name "<name>" [-Ordinal n] [-Description "<text>"]   a new domain, last in order
                  unless -Ordinal is given
      SetDeleted  -Id n -Deleted 1|0   set or clear the delete flag of a domain (a soft delete; the row
                  stays). A domain that still holds live concepts is not deleted: the refusal names them

    A refusal writes nothing. Every change is stamped with the run id and the time; -By names who
    made it (Claude by default, or Researcher).

.EXAMPLE
    iba\app\ps\Concept-Edit.ps1 -Action List -Level Domain
.EXAMPLE
    iba\app\ps\Concept-Edit.ps1 -Action Describe -Level Domain -Id 3 -Description "Fear, dread and awe before God and danger."
.EXAMPLE
    iba\app\ps\Concept-Edit.ps1 -Action AddDomain -Name "Rest and peace" -Description "Quietness of the inner being."
.EXAMPLE
    iba\app\ps\Concept-Edit.ps1 -Action SetDeleted -Id 15 -Deleted 1
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('List', 'Describe', 'AddDomain', 'SetDeleted')]
    [string] $Action,
    [ValidateSet('Domain', 'Concept')] [string] $Level,
    [string] $Id, [string] $DomainId, [string] $Description, [string] $Name, [string] $Ordinal,
    [ValidateSet('0', '1')] [string] $Deleted, [string] $File,
    [ValidateSet('Claude', 'Researcher')] [string] $By,
    [switch] $IncludeDeleted,
    [switch] $Trace
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'
if ($Trace) { $env:IBA_TRACE = '1' }

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot
. $PSScriptRoot\_lib\Notify.ps1

$stepMap = @{ List = 'concept_edit.list'; Describe = 'concept_edit.describe';
              AddDomain = 'concept_edit.add_domain'; SetDeleted = 'concept_edit.set_deleted' }
$stepId = $stepMap[$Action]
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-CONCEPTEDIT"

$paramArgs = @()
foreach ($p in @('Level', 'Id', 'DomainId', 'Description', 'Name', 'Ordinal', 'Deleted', 'File', 'By')) {
    if ($PSBoundParameters.ContainsKey($p)) { $paramArgs += @('--param', "$p=$($PSBoundParameters[$p])") }
}
if ($IncludeDeleted) { $paramArgs += @('--param', 'IncludeDeleted=1') }

Write-IbaRunHeader -WorkPackage 'concept-edit' -Step $stepId -RunId $runId
$json = python -m iba.app.run concept-edit --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Message $res.message -Code $code
exit $code
