<#
.SYNOPSIS
    The researcher's side of every escalation — list open ones, answer a dispatcher-tied (config
    write / quality-check) pause, or raise/update a manual item. The one PS front door for
    lib/escalation.py.

.DESCRIPTION
    Escalation redesign, 2026-08-19/20 (`iba/docs/escalation-redesign-plan-v3-20260819.md`,
    `BUILD.md` §152-154) — root cause: escalation #715's updates were silently overwritten with no
    trace. Fixed: `escalation` is current-state only, `escalation_history` is a real append-only
    table, one full snapshot per update, never lost again.

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

    -Action List        writes every open escalation, WITH FULL HISTORY INLINE (plan v3 §5a — the
                        old report only ever showed current state), to escalation.list_report_path
                        (default iba/app/reports/escalation-list.md; archived on regenerate).
    -Action History      deep-history report for ONE item (plan v3 §5b) — its full history, plus
                        the same for every item its related_activity text names or is named by.
                        Needs -Id.
    -Action AnswerRun    answer a DISPATCHER-TIED escalation (config proposal, quality-check
                        finding, crash, report-stop). Needs -RunId and -Decision (Approve|Reject|
                        Revise|Hold|Noted); -Comment required with Revise, optional otherwise.
                        -Resolution optional. UNCHANGED from pre-redesign.
    -Action Raise        raise a new MANUAL item — an error/issue/task, not raised by a running
                        step. Needs -Question (becomes short_description) and -Comment (required —
                        minimum: what this is about, plan v3 §6). -Source (default 'researcher'),
                        -Type (default task), -AssignedTo (default Claude), -RelatedActivity
                        (free text, optional) optional. Prints the new id — update it with
                        -Action Update.
    -Action Update        every subsequent change to a MANUAL item — comments, decisions,
                        reassignment, state changes, all through this one action; the resulting
                        state is DERIVED from what you set, not chosen directly (plan v3 §3):
                          next_action=approved (+ -Resolution)      -> completed
                          next_action=reject (+ -State withdraw|supersede, -Comment required) -> that state
                          next_action=revise                        -> in-progress
                          next_action=noted                         -> closed
                          -AssignedTo changed, nothing else matches -> re-assigned
                        Needs -Id. -Comment/-Context are CUMULATIVE — what you pass is the
                        increment, appended onto the existing text, not a replacement.

.EXAMPLE
    .\Escalation.ps1 -Action List
.EXAMPLE
    .\Escalation.ps1 -Action History -Id 741
.EXAMPLE
    .\Escalation.ps1 -Action AnswerRun -RunId RUN-20260721_163604_125-CANDIDATE-QUALITY -Decision Approve
.EXAMPLE
    .\Escalation.ps1 -Action AnswerRun -RunId RUN-... -Decision Revise -Comment "check the H0430 cluster first"
.EXAMPLE
    .\Escalation.ps1 -Action Raise -Question "word_full_extract.py throws on H1234" -Comment "ValueError at line 210, traceback in context" -Type run_error
.EXAMPLE
    .\Escalation.ps1 -Action Update -Id 741 -NextAction revise -AssignedTo Researcher -Comment "can you confirm the verse span is intact?"
.EXAMPLE
    .\Escalation.ps1 -Action Update -Id 741 -NextAction approved -Resolution "confirmed and fixed; re-ran clean"
.EXAMPLE
    .\Escalation.ps1 -Action Update -Id 741 -NextAction reject -State withdraw -Comment "superseded by #900"
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('List', 'History', 'AnswerRun', 'Raise', 'Update')]
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
    [ValidateSet('Claude', 'Researcher')] [string] $AnsweredBy = 'Researcher',
    [ValidateSet('Claude', 'Researcher')] [string] $AssignedTo,
    [ValidateSet('task', 'run_error', 'issue', 'notice', 'config')] [string] $Type = 'task',
    [string] $Source = 'researcher',
    [ValidateSet('on-hold', 'in-progress', 'closed', 'withdraw', 'supersede')] [string] $State,
    [string] $RelatedActivity
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot

switch ($Action) {
    'List' {
        python -m iba.app.lib.escalation list
    }
    'History' {
        if (-not $Id) {
            Write-Host "History needs -Id." -ForegroundColor Yellow
            exit 1
        }
        python -m iba.app.lib.escalation history $Id
    }
    'AnswerRun' {
        if (-not $RunId -or -not $Decision) {
            Write-Host "AnswerRun needs -RunId and -Decision (Approve|Reject|Revise|Hold|Noted)." -ForegroundColor Yellow
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
        $flags = @("--source=$Source", "--type=$Type", "--comment=$Comment", "--originator=$AnsweredBy")
        if ($AssignedTo) { $flags += "--assigned-to=$AssignedTo" }
        if ($RelatedActivity) { $flags += "--related-activity=$RelatedActivity" }
        if ($Context) { $flags += "--context=$Context" }
        python -m iba.app.lib.escalation raise @flags $Question
    }
    'Update' {
        if (-not $Id) {
            Write-Host "Update needs -Id." -ForegroundColor Yellow
            exit 1
        }
        if ($NextAction -eq 'reject' -and (-not $State -or -not $Comment)) {
            Write-Host "-NextAction reject needs -State (withdraw|supersede) and -Comment (the reason)." -ForegroundColor Yellow
            exit 1
        }
        # -NextAction approved with no -Resolution here is NOT rejected client-side -- a resolution
        # may already be on the row from an earlier ready_for_approval update; update() itself
        # makes that call against the real current row, not guessed here from a second query.
        $flags = @("--originator=$AnsweredBy")
        if ($NextAction) { $flags += "--next-action=$NextAction" }
        if ($AssignedTo) { $flags += "--assigned-to=$AssignedTo" }
        if ($State) { $flags += "--state=$State" }
        if ($Resolution) { $flags += "--resolution=$Resolution" }
        if ($RelatedActivity) { $flags += "--related-activity=$RelatedActivity" }
        if ($Tried) { $flags += "--tried=$Tried" }
        if ($Context) { $flags += "--context=$Context" }
        if ($Comment) {
            python -m iba.app.lib.escalation update $Id @flags $Comment
        } else {
            python -m iba.app.lib.escalation update $Id @flags
        }
    }
}
