<#
.SYNOPSIS
    The operations-ingest work package — the writer mechanism for the debate analytic process's
    core schema (BUILD.md §61/§63; `hib`/`phenomenon`/`operation` and their children). Standalone,
    not chained — each step invoked independently, own run_id, same shape as
    Config-Maintenance.ps1.

.DESCRIPTION
    -Step hib.set          Step 1: HIB register for the given scope (hib/hib_referent_option/
                            verse_hib). REVISED 2026-08-08 (researcher direction,
                            PLAN-revise-hib-set-scope-and-crud-v1-20260808.md): scoped by
                            -Chapters/-Range like every other step, not book-wide — "the entire
                            pipeline will only concern itself with the chapter." A payload's
                            `verses` may only reference verses inside that scope. Matching against
                            an existing HIB (so e.g. "Daniel" extending from Dan 1 into Dan 2
                            resolves to the SAME row) is still book-wide by label — only the
                            completeness check ("every pre-existing item must be addressed or
                            removed") and the verse_hib writes are scope-limited.
    -Step phenomenon.set   Step 3: phenomena register for one already-tracked passage. Sets
                            passage.phenomena_complete_at itself once the register is complete
                            against verse_hib -- the phase gate operation.set checks.
    -Step operation.set    Step 4-5: operations + parties for the same passage. REFUSES
                            (phenomena-incomplete) if the phase gate above isn't set yet.
    -Step closing.set      Step 7: linkages/insufficiencies/emergent_questions/validation_notes +
                            open_decisions_note for the same passage. REFUSES (operations-
                            incomplete) until every live phenomenon has a live operation. Was
                            registered in cfg_step and reachable via Debate-Run.ps1 (which calls
                            the dispatcher directly) but missing from THIS wrapper's own
                            -ValidateSet -- fixed 2026-08-08, found auditing the debate writers'
                            CRUD (PLAN-revise-hib-set-scope-and-crud-v1-20260808.md).

    Every step takes -PayloadPath, a JSON file holding the actual analytical content (payload
    shape documented on each handler function in handlers/operations.py) -- the analysis itself is
    still an AI/researcher reading pass against the method docs; this step only validates and
    commits its ALREADY-DECIDED findings, exactly the boundary every other step in this app draws.

.PARAMETER Step         hib.set | phenomenon.set | operation.set | closing.set
.PARAMETER Book         OSIS book code, e.g. Dan.
.PARAMETER Chapters     whole-chapter range (every step, incl. hib.set as of 2026-08-08). Mutually
                        exclusive with -Range.
.PARAMETER Range        single-chapter verse range (every step, incl. hib.set as of 2026-08-08).
                        Mutually exclusive with -Chapters.
.PARAMETER PayloadPath  path to the JSON payload file.
.PARAMETER RunId        resume/re-tag a specific run.
.PARAMETER Trace        Print every config read (IBA_TRACE).

.EXAMPLE
    .\Operations-Ingest.ps1 -Step hib.set -Book Dan -Chapters 2 -PayloadPath iba\app\staging\operations\dan-2-hib.set.json
.EXAMPLE
    .\Operations-Ingest.ps1 -Step phenomenon.set -Book Dan -Range 8:1-27 -PayloadPath iba\app\staging\operations\dan-8-phenomena.json
.EXAMPLE
    .\Operations-Ingest.ps1 -Step operation.set -Book Dan -Range 8:1-27 -PayloadPath iba\app\staging\operations\dan-8-operations.json
.EXAMPLE
    .\Operations-Ingest.ps1 -Step closing.set -Book Dan -Range 8:1-27 -PayloadPath iba\app\staging\operations\dan-8-closing.json
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('hib.set', 'phenomenon.set', 'operation.set', 'closing.set')] [string] $Step,
    [Parameter(Mandatory = $true)] [string] $Book,
    [string] $Chapters,
    [string] $Range,
    [Parameter(Mandatory = $true)] [string] $PayloadPath,
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

# Every step, incl. hib.set (as of 2026-08-08 -- was book-scoped-only until now, see .DESCRIPTION),
# needs exactly one of -Chapters/-Range: the debate's own input scope, never book-wide.
if ([bool]$Chapters -eq [bool]$Range) {
    Write-Host "$Step needs exactly one of -Chapters or -Range." -ForegroundColor Yellow
    exit 1
}

if (-not (Test-Path $PayloadPath)) {
    Write-Host "PayloadPath '$PayloadPath' does not exist." -ForegroundColor Yellow
    exit 1
}

Test-IbaWorkPackageActive -WorkPackage 'operations-ingest'

$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-OPERATIONS-INGEST" }

$paramArgs = @('--param', "Book=$Book", '--param', "PayloadPath=$PayloadPath")
if ($Chapters) { $paramArgs += @('--param', "Chapters=$Chapters") }
if ($Range)    { $paramArgs += @('--param', "Range=$Range") }

Write-IbaRunHeader -WorkPackage 'operations-ingest' -Step $Step -RunId $runId

$json = python -m iba.app.run operations-ingest --step $Step --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step $Step -Path $res.path -Message $res.message -Code $code

if ($code -eq 2) {
    Write-IbaPaused -WorkPackage 'operations-ingest' -RunId $runId -Message $res.message
}

exit $code
