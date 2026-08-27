<#
.SYNOPSIS
    The DB-canonical prose store's operations, registered and config-governed
    (escalation #784, 2026-08-21; -Step Flag added escalation #829, 2026-08-24). Step-selection,
    not a fixed pipeline.

.DESCRIPTION
    -Step Extract        programme-prose extract (JSON/MD/DOCX) — iba/app/lib/prosestore.py
    -Step Search         FTS5 search across active prose sections
    -Step ExportChapter  export one chapter/section as an editable Markdown file
    -Step ImportChapter  turn an edited chapter file into a PROSE supersede patch (no DB write)
    -Step Flag           raise one wa_data_quality_flags instance (PROSE_QUALITY) — writes directly,
                          no prose-section reference (escalation #829 sec12.2 — sections a flag
                          touches are found by search at fix time, not stored from raise time)
    -Step FlagFixPropose search active prose for -Find, write a review report of proposed
                          -Replace text per matching section (no DB write, no patch) — angle b of
                          the flag mechanism, escalation #890 D5
    -Step FlagFixApply   after reviewing a FlagFixPropose report, generate a PROSE supersede patch
                          for the approved -SectionIds (re-checks each section fresh; no DB write —
                          apply via scripts/apply_session_patch.py, same as ImportChapter)
    -Step SetStatus      set (or reset) -Status directly on one or more -SectionIds, no body
                          touched -- the reviewer's own "I've read this" / "reopen this" action,
                          separate from an ImportChapter content edit (escalation #918, 2026-08-27,
                          superseding cfg_prose_chapter's now-removed chapter-status tracking; no
                          DB write here either — apply via scripts/apply_session_patch.py)

    CHAPTER_NAMES / BOOK_STAGE_MAP / search default limit / edit file dir are config
    (cfg_prose, escalation #829) — see Config-Maintenance.ps1 -Step Propose to change them.

.PARAMETER Step         Extract | Search | ExportChapter | ImportChapter | Flag | FlagFixPropose |
                         FlagFixApply
.PARAMETER Book         book_label (Extract/ExportChapter)
.PARAMETER Chapter      chapter number (Extract/ExportChapter, combine with -Book)
.PARAMETER TypeId       single prose_section_type.id (ExportChapter, instead of -Book/-Chapter)
.PARAMETER IncludeBody  include full prose body text in the JSON extract (Extract)
.PARAMETER AlsoMarkdown also emit a readable Markdown view (Extract)
.PARAMETER AlsoDocx     also emit a readable .docx view (Extract)
.PARAMETER Query        search text (Search)
.PARAMETER Limit        result cap (Search); default: prose.search_default_limit
.PARAMETER Fts          treat -Query as a raw SQLite FTS5 MATCH expression (Search)
.PARAMETER InputFile    path to an edited chapter Markdown file (ImportChapter). Named InputFile,
                        not Input -- $Input is a PowerShell automatic variable (the pipeline-input
                        enumerator); a same-named parameter cannot be set from the command line
                        (found live, escalation #829 build testing, 2026-08-24 -- reproduced with
                        three separate binding syntaxes, all silently failed to set it).
.PARAMETER Author       patch author, default 'researcher' (ImportChapter)
.PARAMETER FlagCode      one of the live PROSE_QUALITY flag_code values (Flag/FlagFixPropose/FlagFixApply)
.PARAMETER Description   the issue, in prose — required (Flag)
.PARAMETER Find          literal substring to search prose body for (FlagFixPropose)
.PARAMETER Replace       literal replacement text (FlagFixPropose)
.PARAMETER ProposalFile  path to a FlagFixPropose report .json (FlagFixApply)
.PARAMETER SectionIds    comma-separated prose_section.id list, approved from the report (FlagFixApply);
                         or the section(s) to change (SetStatus)
.PARAMETER Status        the new prose_section.status value — draft | in_review | approved |
                         archived, per cfg_enum prose_section_status (SetStatus)
.PARAMETER Out          output path override (all steps)
.PARAMETER Trace        Print every config read (IBA_TRACE).

.EXAMPLE
    .\Prose.ps1 -Step Extract -Book Programme -AlsoMarkdown
.EXAMPLE
    .\Prose.ps1 -Step Search -Query grace -Book Programme
.EXAMPLE
    .\Prose.ps1 -Step ExportChapter -Book Programme -Chapter 1
.EXAMPLE
    .\Prose.ps1 -Step ImportChapter -InputFile outputs/markdown/prose-edit-programme-chapter-1-20260821.md
.EXAMPLE
    .\Prose.ps1 -Step Flag -FlagCode "Terminology change" -Description "Session A/B/C/D superseded by Base_data/Analysis/Publishing"
.EXAMPLE
    .\Prose.ps1 -Step FlagFixPropose -FlagCode "Terminology change" -Find "Session A/B/C/D" -Replace "Base_data/Analysis/Publishing"
.EXAMPLE
    .\Prose.ps1 -Step FlagFixApply -ProposalFile outputs/markdown/prose-flag-fix-proposal-20260826T120000Z.json -SectionIds 12,47 -FlagCode "Terminology change"
.EXAMPLE
    .\Prose.ps1 -Step SetStatus -SectionIds 22 -Status approved
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [ValidateSet('Extract', 'Search', 'ExportChapter', 'ImportChapter', 'Flag', 'FlagFixPropose', 'FlagFixApply', 'SetStatus')] [string] $Step,
    [string] $Book,
    [int] $Chapter,
    [int] $TypeId,
    [switch] $IncludeBody,
    [switch] $AlsoMarkdown,
    [switch] $AlsoDocx,
    [string] $Query,
    [int] $Limit,
    [switch] $Fts,
    [string] $InputFile,
    [string] $Author,
    [string] $FlagCode,
    [string] $Description,
    [string] $Find,
    [string] $Replace,
    [string] $ProposalFile,
    [string] $SectionIds,
    [ValidateSet('draft', 'in_review', 'approved', 'archived')] [string] $Status,
    [string] $Out,
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

$stepMap = @{ Extract = 'prose.extract'; Search = 'prose.search'; ExportChapter = 'prose.export_chapter'; ImportChapter = 'prose.import_chapter'; Flag = 'prose.flag'; FlagFixPropose = 'prose.flag_fix_propose'; FlagFixApply = 'prose.flag_fix_apply'; SetStatus = 'prose.set_status' }
$stepId  = $stepMap[$Step]
$runId   = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-PROSE"

$paramArgs = @()
if ($Book) { $paramArgs += @('--param', "Book=$Book") }
if ($Chapter) { $paramArgs += @('--param', "Chapter=$Chapter") }
if ($TypeId) { $paramArgs += @('--param', "TypeId=$TypeId") }
if ($IncludeBody) { $paramArgs += @('--param', "IncludeBody=true") }
if ($AlsoMarkdown) { $paramArgs += @('--param', "AlsoMarkdown=true") }
if ($AlsoDocx) { $paramArgs += @('--param', "AlsoDocx=true") }
if ($Query) { $paramArgs += @('--param', "Query=$Query") }
if ($Limit) { $paramArgs += @('--param', "Limit=$Limit") }
if ($Fts) { $paramArgs += @('--param', "Fts=true") }
if ($InputFile) { $paramArgs += @('--param', "Input=$InputFile") }
if ($Author) { $paramArgs += @('--param', "Author=$Author") }
if ($FlagCode) { $paramArgs += @('--param', "FlagCode=$FlagCode") }
if ($Description) { $paramArgs += @('--param', "Description=$Description") }
if ($PSBoundParameters.ContainsKey('Find')) { $paramArgs += @('--param', "Find=$Find") }
if ($PSBoundParameters.ContainsKey('Replace')) { $paramArgs += @('--param', "Replace=$Replace") }
if ($ProposalFile) { $paramArgs += @('--param', "ProposalFile=$ProposalFile") }
if ($SectionIds) { $paramArgs += @('--param', "SectionIds=$SectionIds") }
if ($Status) { $paramArgs += @('--param', "Status=$Status") }
if ($Out) { $paramArgs += @('--param', "Out=$Out") }

if ($Step -eq 'Search' -and -not $Query) { Write-Host "Search needs -Query." -ForegroundColor Yellow; exit 1 }
if ($Step -eq 'ImportChapter' -and -not $InputFile) { Write-Host "ImportChapter needs -InputFile." -ForegroundColor Yellow; exit 1 }
if ($Step -eq 'ExportChapter' -and -not $TypeId -and -not $Book) { Write-Host "ExportChapter needs -TypeId or -Book (+ -Chapter)." -ForegroundColor Yellow; exit 1 }
if ($Step -eq 'Flag' -and (-not $FlagCode -or -not $Description)) { Write-Host "Flag needs -FlagCode and -Description." -ForegroundColor Yellow; exit 1 }
if ($Step -eq 'FlagFixPropose' -and (-not $FlagCode -or -not $PSBoundParameters.ContainsKey('Find') -or -not $PSBoundParameters.ContainsKey('Replace'))) { Write-Host "FlagFixPropose needs -FlagCode, -Find and -Replace." -ForegroundColor Yellow; exit 1 }
if ($Step -eq 'FlagFixApply' -and (-not $ProposalFile -or -not $SectionIds)) { Write-Host "FlagFixApply needs -ProposalFile and -SectionIds." -ForegroundColor Yellow; exit 1 }
if ($Step -eq 'SetStatus' -and (-not $SectionIds -or -not $Status)) { Write-Host "SetStatus needs -SectionIds and -Status." -ForegroundColor Yellow; exit 1 }

Write-IbaRunHeader -WorkPackage 'prose' -Step $stepId -RunId $runId

$json = python -m iba.app.run prose --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res  = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code
exit $code
