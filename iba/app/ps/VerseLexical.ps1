<#
.SYNOPSIS
    The verse-lexical work package — replaces VerseSpanMeaning-Report.ps1 (retired). Chains
    lexical.build (the mechanical T1-T3 engine) then report.verse_lexical (a pure render off
    the DB) under one run_id, for one book/chapter-range.

.DESCRIPTION
    lexical.build resolves, per code within every span, role (content lexical entry vs.
    grammatical formative) and — for content codes — a morph-selected sense (not the whole
    stem/voice paradigm), writing version-aware rows to verse_lexical (soft-deletes the superseded
    row, never overwrites in place). report.verse_lexical then renders an MD extract purely from
    that table — it does not re-derive anything from span/strong/strong_meaning_parsed itself.
    Runs independent of report.passage_debate/T4-T9; see
    iba/app/reports/t1-t3-design-decisions-20260805.md for the full design record.

    STEP-dependent for lexical.build only (step.required_for_runs, default true) — a
    content-role code with no strong row yet needs a live STEP call to resolve. report.verse_lexical
    itself has no STEP dependency.

.PARAMETER Book       OSIS book code as stored in verse.osisId, e.g. Dan. Mandatory.
.PARAMETER Chapters   whole-chapter range, e.g. 1-3 or 1. Mutually exclusive with -Range.
.PARAMETER Range      single-chapter verse range, e.g. 8:1-27. Mutually exclusive with -Chapters.
.PARAMETER BookLabel  subfolder-name OVERRIDE, used verbatim -- exists for the rare case the
                      folder must differ from -Book. Defaults to -Book if omitted, and that
                      default is almost always what you want: _analytics/Bible_Books subfolders
                      must be named EXACTLY as cfg_book_order.book (the OSIS code, e.g. Dan, not
                      a full name like "Daniel") -- passing -BookLabel with anything else creates
                      a second, wrong, non-compliant folder next to the real one (found live
                      2026-08-29, escalation #1007 thread). Omit this parameter unless you have a
                      specific, confirmed reason not to.
.PARAMETER Step       Run only this one step (lexical.build | lexical.enrich | report.
                      verse_lexical | report.lexical_exceptions | report.lexical_extract)
                      instead of the full chained sequence -- e.g. report.verse_lexical alone,
                      to VIEW already-built results for a range without re-running the build
                      (which may make live STEP calls). Omit to run the full sequence, unchanged
                      default except it now also runs lexical.enrich + report.lexical_exceptions
                      (escalation #1383).
.PARAMETER PayloadPath  Path to the JSON payload file for lexical.enrich (notes/remove/genre) --
                      REQUIRED when -Step lexical.enrich is given, or when running the full
                      sequence (which now includes lexical.enrich) -- same convention as
                      Operations-Ingest.ps1's own -PayloadPath.
.PARAMETER SkipBuild  Only meaningful with `-Step lexical.enrich`. By default, `-Step
                      lexical.enrich` auto-detects whether Layer 1 already has live rows for this
                      exact range (same Book/Chapters or Range/BookLabel) and, if it does, skips
                      the rebuild automatically -- see -ForceRebuild below for why that auto-detect
                      exists and is NOT a bare "always build first." Pass -SkipBuild to skip the
                      detection query too and go straight to enrich unconditionally (fails fast if
                      Layer 1 turns out to be missing, rather than silently building it). Has no
                      effect on any other -Step value or on the full default sequence. Mutually
                      exclusive with -ForceRebuild.
.PARAMETER ForceRebuild  Only meaningful with `-Step lexical.enrich`. Forces `lexical.build` to
                      run even though Layer 1 is already present for this range. Found live,
                      escalation #1451 review session 2026-09-05, on Rom.9.14: `lexical.build`'s
                      version-aware write always mints fresh `verse_lexical` row ids on every run
                      -- even when the new content is byte-identical to what's already there (the
                      original test plan's own documented B4 case) -- and nothing in the design
                      re-points `verse_lexical_note.verse_lexical_id` when that happens. An
                      unconditional "always rebuild" default therefore silently ORPHANS every
                      existing Layer 2 note on that verse (their FK now points at a soft-deleted
                      row) the moment a verse that already has notes gets enriched again -- exactly
                      what happened testing this flag's first version. The safe default is now
                      "build only if Layer 1 is missing." Use -ForceRebuild only when you deliberately
                      want Layer 1 re-minted despite that risk; if Layer 2 notes already exist for
                      the range, the script prints a loud warning before proceeding and you will
                      need to re-run lexical.enrich with the same payload afterward (or delete the
                      stale notes first) to reattach them to the new ids. Mutually exclusive with
                      -SkipBuild.
.PARAMETER PassageFilter  (report.lexical_extract only) comma-list of passage ids.
.PARAMETER VerseFilter    (report.lexical_extract only) comma-list of OSIS verses, or a same-book
                      range, e.g. `Rom.9.14` or `Gen.1.1-Gen.1.10`. NOT the same syntax as -Range
                      (which is chapter:verse against -Book) -- this is the handler's own
                      independent filter set and ignores -Book/-Chapters/-Range entirely.
.PARAMETER SurfaceFilter  (report.lexical_extract only) comma-list of exact surface-text values.
.PARAMETER StrongFilter   (report.lexical_extract only) comma-list of Strong's codes.
                      report.lexical_extract takes none of -Book/-Chapters/-Range/-BookLabel --
                      it is a filter-driven extract over the whole corpus, not a range render --
                      but -Book and one of -Chapters/-Range are still required by THIS script (see
                      Errors and fixes, escalation #1520 follow-up 2026-09-05: found live, this
                      step was reachable in -Step's own ValidateSet with no way to actually supply
                      its real parameters until these four were added) -- pass any values for
                      them, e.g. -Book Rom -Range 1:1, they are accepted but unused by this step.
                      At least one of the four filters is required when -Step report.lexical_extract
                      is given, checked the same way -PayloadPath is required for lexical.enrich.
.PARAMETER RunId      resume/re-tag a specific run.
.PARAMETER Trace      Print every config read (IBA_TRACE).

.EXAMPLE
    .\VerseLexical.ps1 -Book Dan -Range 8:1-27
.EXAMPLE
    .\VerseLexical.ps1 -Book Dan -Range 8:1-27 -Step report.verse_lexical
.EXAMPLE
    .\VerseLexical.ps1 -Book Dan -Range 1:1-8 -Step lexical.enrich -PayloadPath iba\app\staging\lexical\dan-1-1-8.json
    # -> auto-detects: builds Layer 1 first only if Dan 1:1-8 doesn't already have it, then enriches.
.EXAMPLE
    .\VerseLexical.ps1 -Book Dan -Range 1:1-8 -Step lexical.enrich -PayloadPath iba\app\staging\lexical\dan-1-1-8.json -SkipBuild
    # -> lexical.enrich only, no detection query -- fails fast if Layer 1 is missing.
.EXAMPLE
    .\VerseLexical.ps1 -Book Dan -Range 1:1-8 -Step lexical.enrich -PayloadPath iba\app\staging\lexical\dan-1-1-8.json -ForceRebuild
    # -> rebuilds Layer 1 even though present; warns if Layer 2 notes already exist (they'll be orphaned).
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [string] $Book,
    [string] $Chapters,
    [string] $Range,
    [string] $BookLabel,
    [ValidateSet('lexical.build', 'lexical.enrich', 'report.verse_lexical',
                 'report.lexical_exceptions', 'report.lexical_extract')] [string] $Step,
    [string] $PayloadPath,
    [switch] $SkipBuild,
    [switch] $ForceRebuild,
    [string] $PassageFilter,
    [string] $VerseFilter,
    [string] $SurfaceFilter,
    [string] $StrongFilter,
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

if ([bool]$Chapters -eq [bool]$Range) {
    Write-Host "Give exactly one of -Chapters or -Range." -ForegroundColor Yellow
    exit 1
}

Test-IbaWorkPackageActive -WorkPackage 'verse-lexical'

if ($SkipBuild -and $ForceRebuild) {
    Write-Host "-SkipBuild and -ForceRebuild are mutually exclusive." -ForegroundColor Yellow
    exit 1
}

$seq   = python -c "import json; from iba.app.lib.cfg import Cfg; c=Cfg(); print(json.dumps([dict(r) for r in c.sequence('verse-lexical')])); c.close()" | ConvertFrom-Json
if ($Step -eq 'lexical.enrich' -and $SkipBuild) {
    # Explicit skip -- no detection query, straight to enrich (fails fast if Layer 1 is missing).
    $seq = $seq | Where-Object { $_.step -eq $Step }
} elseif ($Step -eq 'lexical.enrich') {
    # Auto-detect whether Layer 1 already has live rows for this exact range -- see -SkipBuild/
    # -ForceRebuild's own help text for why this is NOT a bare "always build first": lexical.build
    # mints fresh verse_lexical ids on every run, even for identical content, which orphans any
    # verse_lexical_note already attached. Default: build only if genuinely missing.
    $precheck = @'
import json, sys
from iba.app.lib.cfg import Cfg
from iba.app.lib.versespanmeaningreport import fetch_verses, parse_chapters, parse_range
from iba.app.lib.lexicalenrich import layer1_state
book, range_spec, chapters_spec = sys.argv[1], sys.argv[2], sys.argv[3]
c = Cfg()
if range_spec:
    ch, vlo, vhi = parse_range(range_spec)
    lo = hi = ch
else:
    lo, hi = parse_chapters(chapters_spec)
    vlo = vhi = None
verses = fetch_verses(c.conn, book, lo, hi, vlo, vhi)
print(json.dumps(layer1_state(c.conn, [v['id'] for v in verses])))
c.close()
'@
    $rangeArg    = if ($Range) { $Range } else { '' }
    $chaptersArg = if ($Chapters) { $Chapters } else { '' }
    $state = python -c $precheck $Book $rangeArg $chaptersArg | ConvertFrom-Json

    if (-not $state.has_layer1) {
        # Genuinely missing -- safe to auto-build, nothing to orphan yet.
        $seq = $seq | Where-Object { $_.step -in @('lexical.build', 'lexical.enrich') } | Sort-Object ordinal
    } elseif ($ForceRebuild) {
        if ($state.has_notes) {
            Write-Host ("WARNING: this range already has Layer 2 notes attached to the current " +
                "Layer 1 rows. lexical.build always mints fresh row ids (even for identical " +
                "content) -- forcing a rebuild will ORPHAN every existing note (its " +
                "verse_lexical_id will point at a soft-deleted row). Re-run lexical.enrich with " +
                "the same payload afterward to reattach them, or delete the stale notes first if " +
                "they're being replaced anyway.") -ForegroundColor Red
        }
        $seq = $seq | Where-Object { $_.step -in @('lexical.build', 'lexical.enrich') } | Sort-Object ordinal
    } else {
        # Layer 1 already present -- skip the no-op rebuild by default (safe: nothing to gain from
        # re-minting identical rows, and it avoids orphaning any existing notes).
        Write-Host "Layer 1 already present for this range -- skipping rebuild (pass -ForceRebuild to rebuild anyway)." -ForegroundColor DarkGray
        $seq = $seq | Where-Object { $_.step -eq $Step }
    }
} elseif ($Step) {
    $seq = $seq | Where-Object { $_.step -eq $Step }
}
$runId = if ($RunId) { $RunId } else { "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-VERSE-LEXICAL" }

# lexical.enrich without -PayloadPath fails fast (bad-payload) rather than silently skipping
# itself -- a full run genuinely needs the JSON prepared first (escalation #1383, build spec §F.1).
if (($seq | Where-Object { $_.step -eq 'lexical.enrich' }) -and -not $PayloadPath) {
    Write-Host "lexical.enrich is in this run's sequence but -PayloadPath was not given." -ForegroundColor Yellow
    exit 1
}

# report.lexical_extract without any filter fails fast the same way, same reason -- the handler
# itself refuses an unbounded extract (no-filter), and until these four params existed there was
# no way to reach it from this script at all (found live, escalation #1520 follow-up 2026-09-05).
if (($seq | Where-Object { $_.step -eq 'report.lexical_extract' }) -and
    -not ($PassageFilter -or $VerseFilter -or $SurfaceFilter -or $StrongFilter)) {
    Write-Host ("report.lexical_extract is in this run's sequence but none of -PassageFilter/" +
        "-VerseFilter/-SurfaceFilter/-StrongFilter was given.") -ForegroundColor Yellow
    exit 1
}

Write-IbaRunHeader -WorkPackage 'verse-lexical' -RunId $runId -RunsOver "book = '$Book'"
Write-Host "sequence     : $($seq.Count) steps, loaded from the DB config store (cfg_step)"
Write-Host ""

$paramArgs = @('--param', "Book=$Book")
if ($Chapters)      { $paramArgs += @('--param', "Chapters=$Chapters") }
if ($Range)         { $paramArgs += @('--param', "Range=$Range") }
if ($BookLabel)     { $paramArgs += @('--param', "BookLabel=$BookLabel") }
if ($PayloadPath)   { $paramArgs += @('--param', "PayloadPath=$PayloadPath") }
if ($PassageFilter) { $paramArgs += @('--param', "PassageFilter=$PassageFilter") }
if ($VerseFilter)   { $paramArgs += @('--param', "VerseFilter=$VerseFilter") }
if ($SurfaceFilter) { $paramArgs += @('--param', "SurfaceFilter=$SurfaceFilter") }
if ($StrongFilter)  { $paramArgs += @('--param', "StrongFilter=$StrongFilter") }

$halt = $false
$exitCode = 0
foreach ($entry in $seq) {
    $json = python -m iba.app.run verse-lexical --step $entry.step --run-id $runId @paramArgs
    $code = $LASTEXITCODE
    $res  = $json | ConvertFrom-Json

    Write-IbaStepResult -Step $entry.step -Path $res.path -Message $res.message -Code $code

    if ($code -eq 2) {
        Write-IbaPaused -WorkPackage 'verse-lexical' -RunId $runId -Message $res.message
        $halt = $true; $exitCode = 2; break
    }
    if ($code -eq 3) {
        Write-IbaStopped -Message $res.message
        $halt = $true; $exitCode = 3; break
    }
}

if (-not $halt) {
    Write-IbaComplete -WorkPackage 'verse-lexical' -Vars @{ book = $Book }
}
exit $exitCode
