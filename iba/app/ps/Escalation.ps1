<#
.SYNOPSIS
    The researcher's side of every escalation — list open ones, answer a dispatcher-tied (config
    write / quality-check) pause, or raise/update a manual item. The one PS front door for
    lib/escalation.py.

.DESCRIPTION
    Full rebuild, 2026-08-20 (`iba/docs/escalation-rebuild-design-v1-20260820.md`) — the
    2026-08-19/20 redesign fixed the loss-of-history bug (#715) but shipped with no config
    representation for its own validate/complete rules and stored full CUMULATIVE snapshots in
    `escalation_history` instead of per-version deltas; both reset and rebuilt 2026-08-20. Now:
    `escalation` is current-state (cumulative, unchanged), `escalation_history` is a true delta —
    each row shows only what THAT version actually changed, envelope fields (state/next_action/
    assigned_to/originator/when) always present, content fields blank unless this version touched
    them. State-derivation and field-requirement rules are config-driven
    (`cfg_escalation_transition`/`cfg_escalation_requirement`), not hardcoded.

    **`-AnsweredBy` is REQUIRED on every write action (AnswerRun/Raise/Update/Correction) — no
    default.** A silent `'Researcher'` default previously misattributed >=39 history rows to the
    wrong party in one session; there is no safe default for "who is actually running this
    command."

    **Two shapes, two vocabularies, one mechanism** (deliberately not unified — they answer
    different questions):
      - DISPATCHER-TIED (a real run.py pause — configmaint.propose/validate, a quality-check
        finding, a crash, a report-stop): vocabulary UNCHANGED — approve/reject/revise/hold/noted.
        Answered with -Action AnswerRun, same as always. These are development/design controls
        (changes to the app's own behaviour) and correctly keep a real, gated approval.
      - MANUAL (the researcher/Claude backlog-of-work-and-issues workflow): vocabulary
        ready_for_approval/approved/reject/revise/noted/review — a two-stage approval handshake
        (ready_for_approval -> approved -> system-validated completed). Raised/updated with
        -Action Raise / -Action Update — REPLACING the six single-purpose actions
        (Edit/Pause/Resume/Retract/Reassign/Complete) the pre-redesign script had: "in principle
        there are only two transaction types... the resulting state is determined by the values
        in the fields" (researcher, plan v3 §5). A standard operational routine (registry.create
        and similar) no longer escalates at all — logged by the engine, errors only (`BUILD.md`
        §153) — word-scoped -Action Answer is RETIRED, not replaced.

    **Decision-vs-defect axis, 2026-08-22** (`iba/docs/escalation-decision-vs-defect-axis-proposal-v5-20260822.md`,
    escalation #798/#799 — `cfg_behaviour_rule` 'decision-points-are-terminal-not-inline'): every
    item now carries `resolution_kind` — `decision_required` (a genuine judgement call; the ONLY
    thing this vocabulary answers) or `self_correctable` (a code/config execution slip against an
    already-approved design; Claude fixes it directly, no approval needed). `-Action Raise` now
    REQUIRES `-ResolutionKind DecisionRequired|SelfCorrectable` — no default, mirroring
    `-AnsweredBy`'s own no-silent-default rule. `-Type` is respected as given regardless of
    `-ResolutionKind` — it no longer forces `issue` under `decision_required` (removed 2026-08-26,
    escalation #872: `task`/`note` must be usable types too, researcher's explicit instruction);
    `type` is still immutable after Raise, same as `run_id`/`source`/`at_step`/`raised_at`. Two new
    actions close
    the loop a self-correctable item can still take: `-Action ResolveSelfCorrectable` (fixed it,
    done — needs `-Id`/`-Resolution`/`-AnsweredBy`) or `-Action EscalateToDecision` (the fix, once
    attempted, turned out to need a real judgement call after all — needs `-Id`/`-Tried`/
    `-AnsweredBy`; this was `-Tried`'s original purpose). A dispatcher-tied item whose
    `resolution_kind` is `self_correctable` is answered the same way as before (report-stop/
    pause-continue via run.py); one recorded as `decision_required` always routes to a terminal
    report-stop, never resumes inline — per the researcher's own framing: "when a build has
    validation or other stoppages for clarification it should be terminal."

    **D14/D15 RETIRED 2026-08-27, escalation #909.** `from_id` and `related_activity` — the
    "which item this one was spawned from" column and its free-text pairing/graph companion — are
    both gone: not deprecated, removed. Two live audits this session found the mechanism
    unreliable and never actually used
    (`iba/app/reports/related-activity-summary-mockup-20260826.md`,
    `iba/app/reports/from-id-data-quality-audit-20260826.md`), on top of escalation #768's own
    10-round closure (`GOVERNANCE.md` §56). Researcher, verbatim: *"the related-activity and
    fromid columns in the table is unreliable, and does not serve a purpose, and is very confusing
    and distracting in the history report... so scrap it."* `-RelatedActivity`/`-FromId` no longer
    exist as parameters anywhere below; the List report's D15 exception sections (cycle/dangling/
    mismatched pairing/missing link/incoherent link) and the History report's relationship-walk
    are both gone too. Full record: `GOVERNANCE.md` §57.

    **Register v9 build, 2026-08-21** (`escalation-design-plan-v5-20260821.md` +
    `escalation-design-decision-register-v9-20260821.md`): List/History now dispatch through
    run.py (work package 'escalation-reporting') instead of calling the module directly, matching
    every other report script (D4/D16/D23). `-NextAction ready_for_approval` now resolves explicitly
    (D27) rather than depending on -AssignedTo happening to change. Two-stage approval (`approved`)
    is now an AUTHORITY check, not identity (D25) — the party ready_for_approval assigned it to may
    approve, even if that's the same party who set ready_for_approval. `-Type notice` closes on
    arrival (D12) — no review/decision cycle. An Update carrying -Comment/-Context/-Tried is
    refused if the resulting state would still be 'raised' (D26) — move it off raised first.

    -Action List        writes every open escalation, WITH FULL HISTORY INLINE (plan v3 §5a — the
                        old report only ever showed current state), to escalation.list_report_path
                        (default iba/app/reports/escalation-list.md; archived on regenerate).
    -Action History      deep-history report for ONE item (plan v3 §5b) — its own full history.
                        Needs -Id.
    -Action AnswerRun    answer a DISPATCHER-TIED escalation (config proposal, quality-check
                        finding, crash, report-stop). Needs -RunId and -Decision (Approve|Reject|
                        Revise|Hold|Noted); -Comment required with Revise, optional otherwise.
                        -Resolution optional. UNCHANGED from pre-redesign.
    -Action Raise        raise a new MANUAL item — an error/issue/task, not raised by a running
                        step. Needs -Question (becomes short_description), -Comment (required —
                        minimum: what this is about, plan v3 §6), and -ResolutionKind
                        DecisionRequired|SelfCorrectable (required — no default, escalation
                        #798/#799). -Type is respected as given, no longer forced to issue under
                        decision_required (escalation #872, 2026-08-26). -Source (default
                        'researcher'), -Type (default task; 'notice' closes on arrival, D12; 'note'
                        added 2026-08-26 for searchability, no special close behaviour, #872),
                        -AssignedTo (default Claude). Prints the new id — update it
                        with -Action Update.
    -Action ResolveSelfCorrectable
                        close out a `self_correctable` item you already fixed — no approval step,
                        this IS the approval (the design was already approved; only the execution
                        slipped). Needs -Id, -Resolution (what was wrong, what changed), and
                        -AnsweredBy. Refuses items whose resolution_kind is decision_required —
                        those close via -Action Update / -Action AnswerRun instead.
    -Action EscalateToDecision
                        convert a `self_correctable` item into `decision_required` mid-fix — the
                        attempted self-correction surfaced a genuine judgement call the original
                        design didn't anticipate. Needs -Id, -Tried (what was attempted and what it
                        revealed), and -AnsweredBy. Sets type=issue and routes the item to a
                        terminal stop, same as any other decision_required item.
    -Action Update        every subsequent change to a MANUAL item — comments, decisions,
                        reassignment, state changes, all through this one action; the resulting
                        state is DERIVED from what you set via cfg_escalation_transition, not
                        chosen directly:
                          next_action=approved (+ resolution present)      -> completed
                          next_action=reject (+ -State withdraw|supersede, -Comment required) -> that state
                          next_action=revise                        -> in-progress
                          next_action=noted                         -> closed
                          your own explicit -State                 -> that state (D-fix, #762 —
                                                                        outranks the -AssignedTo
                                                                        row above; previously an
                                                                        explicit -State silently
                                                                        lost to a same-call
                                                                        reassignment)
                          -AssignedTo changed, nothing else matches -> re-assigned
                        Needs -Id. -Comment/-Context are CUMULATIVE in
                        `escalation` — what you pass
                        is the increment, appended onto the existing text — but `escalation_history`
                        now stores only that increment for this version, not the running total.
                        `next_action=approved` is REJECTED if you are NOT the party
                        `ready_for_approval` most recently assigned this item to — an AUTHORITY
                        check (D25, register v9), not identity: the same party is fine when it
                        holds the authority (e.g. Claude self-authorising an item within its own
                        remit). An Update carrying -Comment/-Context/-Tried is refused outright if
                        the resulting state would still be 'raised' (D26) — -State in-progress (or
                        similar) first.
    -Action Correction   ★ ERROR CORRECTION ONLY (escalation #774, 2026-08-21) — NOT a normal
                        workflow action, do not use for ordinary changes (use -Action Update for
                        those; a runtime warning prints on every call as a reminder). A copy of
                        Update that works on an item in ANY state, including closed/completed
                        (Update structurally refuses those), and can set -ShortDescription (Update
                        has no such parameter — the title is otherwise immutable after Raise,
                        §4.7/below). state/next_action are taken EXACTLY as given, never
                        auto-derived via cfg_escalation_transition — omit them and the item's
                        current state/assignment carry forward unchanged, the normal case (most
                        corrections fix content, not workflow position).

.EXAMPLE
    .\Escalation.ps1 -Action List
.EXAMPLE
    .\Escalation.ps1 -Action History -Id 741
.EXAMPLE
    .\Escalation.ps1 -Action AnswerRun -RunId RUN-20260721_163604_125-CANDIDATE-QUALITY -Decision Approve -AnsweredBy Researcher
.EXAMPLE
    .\Escalation.ps1 -Action AnswerRun -RunId RUN-... -Decision Revise -AnsweredBy Researcher -Comment "check the H0430 cluster first"
.EXAMPLE
    .\Escalation.ps1 -Action Raise -Question "word_full_extract.py throws on H1234" -Comment "ValueError at line 210, traceback in context" -Type run_error -ResolutionKind SelfCorrectable -AnsweredBy Claude
.EXAMPLE
    .\Escalation.ps1 -Action ResolveSelfCorrectable -Id 812 -Resolution "off-by-one in the span index, fixed and re-ran clean" -AnsweredBy Claude
.EXAMPLE
    .\Escalation.ps1 -Action EscalateToDecision -Id 812 -Tried "widened the retry window but the underlying limit is a design choice, not a bug -- needs a researcher call" -AnsweredBy Claude
.EXAMPLE
    .\Escalation.ps1 -Action Update -Id 741 -NextAction revise -AssignedTo Researcher -AnsweredBy Claude -Comment "can you confirm the verse span is intact?"
.EXAMPLE
    .\Escalation.ps1 -Action Update -Id 741 -NextAction approved -AnsweredBy Researcher -Resolution "confirmed and fixed; re-ran clean"
.EXAMPLE
    .\Escalation.ps1 -Action Update -Id 741 -NextAction reject -State withdraw -AnsweredBy Researcher -Comment "superseded by #900"
.EXAMPLE
    .\Escalation.ps1 -Action Correction -Id 741 -ShortDescription "corrected title" -AnsweredBy Researcher -Comment "original title had a typo"
#>

[CmdletBinding(PositionalBinding = $false)]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('List', 'History', 'AnswerRun', 'Raise', 'Update', 'Correction',
                 'ResolveSelfCorrectable', 'EscalateToDecision')]
    [string] $Action,
    [int] $Id,
    [string] $RunId,
    [ValidateSet('Approve', 'Reject', 'Revise', 'Hold', 'Noted')] [string] $Decision,
    [ValidateSet('ready_for_approval', 'approved', 'reject', 'revise', 'noted', 'review')] [string] $NextAction,
    [string] $Comment,
    [string] $Context,
    [string] $Question,
    [string] $Resolution,
    [string] $Tried,
    [ValidateSet('Claude', 'Researcher')] [string] $AnsweredBy,
    [ValidateSet('Claude', 'Researcher')] [string] $AssignedTo,
    [ValidateSet('task', 'run_error', 'issue', 'notice', 'config', 'note')] [string] $Type = 'task',
    [string] $Source = 'researcher',
    # -Action Correction (escalation #774) can set state to ANY value, not just the 5 Update
    # allows explicitly (raised/re-assigned/completed are normally system-derived for Update, but
    # a Correction has to be able to fix any of them directly) -- widened here rather than a
    # parallel duplicate parameter, since Update's own explicit-state precedence (D-fix #762) is
    # unaffected either way.
    [ValidateSet('raised', 'in-progress', 'on-hold', 're-assigned', 'closed', 'withdraw', 'supersede', 'completed')] [string] $State,
    [string] $ShortDescription,
    # escalation #798/#799: required on Raise (cfg_behaviour_rule
    # 'decision-points-are-terminal-not-inline'). DecisionRequired/SelfCorrectable map to the
    # lowercase cfg_enum values the Python side expects.
    [ValidateSet('DecisionRequired', 'SelfCorrectable')] [string] $ResolutionKind,
    # escalation #1075, 2026-08-30: set on Raise, or set/cleared on Update, when finishing this
    # item needs a further Claude action AFTER the researcher approves it (a config apply, a build
    # step) -- approved then routes back to Claude instead of straight to completed. '1' sets it,
    # '0' clears it; omitted on Update carries the item's current value forward unchanged, omitted
    # on Raise defaults to not set.
    [ValidateSet('1', '0')] [string] $NeedsFollowup
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot

# -AnsweredBy auto-attribution (researcher, 2026-08-21): the 2026-08-20 rebuild made -AnsweredBy
# mandatory everywhere with NO default, deliberately -- a silent 'Researcher' default previously
# misattributed >=39 history rows in one session when CLAUDE was the one actually running the
# command. That risk is real specifically when Claude Code is driving this script (it always sets
# $env:CLAUDECODE=1 in every shell it runs -- confirmed live, not assumed). A human typing this
# command in their OWN terminal window never has that variable set, and in this single-researcher
# project nothing else plausibly runs it -- so THAT case can safely auto-attribute to Researcher
# without reintroducing the original bug, closing the friction of typing -AnsweredBy Researcher
# by hand every time. Claude's own invocations still get the hard stop below, unchanged.
if (-not $AnsweredBy -and -not $env:CLAUDECODE) {
    $AnsweredBy = 'Researcher'
    Write-Host "  (-AnsweredBy not given, not running under Claude Code -- defaulting to Researcher)" -ForegroundColor DarkGray
}

switch ($Action) {
    'List' {
        # D4/D16/D23 (register v9): report-producing steps go through the dispatcher like every
        # other report in the app (Reports.ps1/Manifest-Rebuild.ps1 pattern), not a direct module
        # invocation — registered as work package 'escalation-reporting', step 'escalation.list'.
        $runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-ESCALATION-LIST"
        $json = python -m iba.app.run escalation-reporting --step escalation.list --run-id $runId
        $code = $LASTEXITCODE
        $res = $json | ConvertFrom-Json
        Write-Host "  $($res.message)"
        exit $code
    }
    'History' {
        if (-not $Id) {
            Write-Host "History needs -Id." -ForegroundColor Yellow
            exit 1
        }
        $runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-ESCALATION-HISTORY"
        $json = python -m iba.app.run escalation-reporting --step escalation.history --run-id $runId --param "Id=$Id"
        $code = $LASTEXITCODE
        $res = $json | ConvertFrom-Json
        Write-Host "  $($res.message)"
        exit $code
    }
    'AnswerRun' {
        if (-not $RunId -or -not $Decision) {
            Write-Host "AnswerRun needs -RunId and -Decision (Approve|Reject|Revise|Hold|Noted)." -ForegroundColor Yellow
            exit 1
        }
        if (-not $AnsweredBy) {
            Write-Host "AnswerRun needs -AnsweredBy Claude|Researcher -- no default (escalation rebuild 2026-08-20: a silent 'Researcher' default previously misattributed >=39 history rows in one session)." -ForegroundColor Yellow
            exit 1
        }
        if ($Decision -eq 'Revise' -and -not $Comment) {
            Write-Host "Revise needs -Comment — what should be checked/changed." -ForegroundColor Yellow
            exit 1
        }
        $flags = @("--by=$AnsweredBy")
        if ($Resolution) { $flags += "--resolution=$Resolution" }
        if ($Comment) {
            python -m iba.app.lib.escalation answer-run $RunId $Decision.ToLower() @flags $Comment
        } else {
            python -m iba.app.lib.escalation answer-run $RunId $Decision.ToLower() @flags
        }
    }
    'Raise' {
        if (-not $Question -or -not $Comment) {
            Write-Host "Raise needs -Question and -Comment (minimum: what this item is about)." -ForegroundColor Yellow
            exit 1
        }
        if (-not $AnsweredBy) {
            Write-Host "Raise needs -AnsweredBy Claude|Researcher -- no default (escalation rebuild 2026-08-20: a silent 'Researcher' default previously misattributed >=39 history rows in one session)." -ForegroundColor Yellow
            exit 1
        }
        if (-not $ResolutionKind) {
            Write-Host "Raise needs -ResolutionKind DecisionRequired|SelfCorrectable (escalation #798/#799, cfg_behaviour_rule 'decision-points-are-terminal-not-inline')." -ForegroundColor Yellow
            exit 1
        }
        $kindMap = @{ DecisionRequired = 'decision_required'; SelfCorrectable = 'self_correctable' }
        # .ToLower() -- escalation #872, 2026-08-26: ValidateSet matches case-INsensitively, so
        # e.g. -Type Task passes PS validation, but Python's cfg_enum check is exact-match and
        # crashed on it uncaught. Every ValidateSet value in this script is already lowercase, so
        # folding case here is enough (unlike -ResolutionKind, which needs an actual word mapping,
        # not just case-folding).
        $flags = @("--source=$Source", "--type=$($Type.ToLower())", "--comment=$Comment",
                  "--originator=$AnsweredBy", "--resolution-kind=$($kindMap[$ResolutionKind])")
        if ($AssignedTo) { $flags += "--assigned-to=$AssignedTo" }
        if ($Context) { $flags += "--context=$Context" }
        if ($NeedsFollowup) { $flags += "--needs-followup=$NeedsFollowup" }
        python -m iba.app.lib.escalation raise @flags $Question
    }
    'ResolveSelfCorrectable' {
        if (-not $Id -or -not $Resolution) {
            Write-Host "ResolveSelfCorrectable needs -Id and -Resolution (what was wrong, what changed)." -ForegroundColor Yellow
            exit 1
        }
        if (-not $AnsweredBy) {
            Write-Host "ResolveSelfCorrectable needs -AnsweredBy Claude|Researcher -- no default." -ForegroundColor Yellow
            exit 1
        }
        python -m iba.app.lib.escalation resolve-self-correctable $Id --originator=$AnsweredBy --resolution=$Resolution
    }
    'EscalateToDecision' {
        if (-not $Id -or -not $Tried) {
            Write-Host "EscalateToDecision needs -Id and -Tried (what was attempted before converting)." -ForegroundColor Yellow
            exit 1
        }
        if (-not $AnsweredBy) {
            Write-Host "EscalateToDecision needs -AnsweredBy Claude|Researcher -- no default." -ForegroundColor Yellow
            exit 1
        }
        python -m iba.app.lib.escalation escalate-to-decision $Id --originator=$AnsweredBy --tried=$Tried
    }
    'Update' {
        if (-not $Id) {
            Write-Host "Update needs -Id." -ForegroundColor Yellow
            exit 1
        }
        if (-not $AnsweredBy) {
            Write-Host "Update needs -AnsweredBy Claude|Researcher -- no default (escalation rebuild 2026-08-20: a silent 'Researcher' default previously misattributed >=39 history rows in one session)." -ForegroundColor Yellow
            exit 1
        }
        if ($NextAction -eq 'reject' -and (-not $State -or -not $Comment)) {
            Write-Host "-NextAction reject needs -State (withdraw|supersede) and -Comment (the reason)." -ForegroundColor Yellow
            exit 1
        }
        # -NextAction approved with no -Resolution here is NOT rejected client-side -- a resolution
        # may already be on the row from an earlier ready_for_approval update; update() itself
        # makes that call against the real current row, not guessed here from a second query.
        # .ToLower() -- escalation #872, 2026-08-26: same case-fold as -Type (see 'Raise' above).
        # -NextAction/-State's ValidateSet values are already lowercase, so this is enough.
        $flags = @("--originator=$AnsweredBy")
        if ($NextAction) { $flags += "--next-action=$($NextAction.ToLower())" }
        if ($AssignedTo) { $flags += "--assigned-to=$AssignedTo" }
        if ($State) { $flags += "--state=$($State.ToLower())" }
        if ($Resolution) { $flags += "--resolution=$Resolution" }
        if ($Tried) { $flags += "--tried=$Tried" }
        if ($Context) { $flags += "--context=$Context" }
        if ($NeedsFollowup) { $flags += "--needs-followup=$NeedsFollowup" }
        if ($Comment) {
            python -m iba.app.lib.escalation update $Id @flags $Comment
        } else {
            python -m iba.app.lib.escalation update $Id @flags
        }
    }
    'Correction' {
        if (-not $Id) {
            Write-Host "Correction needs -Id." -ForegroundColor Yellow
            exit 1
        }
        if (-not $AnsweredBy) {
            Write-Host "Correction needs -AnsweredBy Claude|Researcher -- no default." -ForegroundColor Yellow
            exit 1
        }
        Write-Host "  ** Correction is for ERROR CORRECTION ONLY (escalation #774) -- fixing something already recorded wrong, not normal workflow. Use -Action Update for ordinary changes. **" -ForegroundColor Yellow
        $flags = @("--originator=$AnsweredBy")
        if ($ShortDescription) { $flags += "--short-description=$ShortDescription" }
        if ($NextAction) { $flags += "--next-action=$($NextAction.ToLower())" }
        if ($AssignedTo) { $flags += "--assigned-to=$AssignedTo" }
        if ($State) { $flags += "--state=$($State.ToLower())" }
        if ($Resolution) { $flags += "--resolution=$Resolution" }
        if ($Tried) { $flags += "--tried=$Tried" }
        if ($Context) { $flags += "--context=$Context" }
        if ($Comment) {
            python -m iba.app.lib.escalation correction $Id @flags $Comment
        } else {
            python -m iba.app.lib.escalation correction $Id @flags
        }
    }
}
