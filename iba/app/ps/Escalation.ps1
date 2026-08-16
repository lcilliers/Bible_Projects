<#
.SYNOPSIS
    The researcher's side of every escalation — list open ones, answer a word approval, or
    answer a run-scoped (config proposal / quality-check) escalation. The one PS front door for
    lib/escalation.py, which every other governed operation already has and this one didn't.

.DESCRIPTION
    Escalation-reset 2026-08-16 (see USER-GUIDE.md §4, GOVERNANCE.md §39): `next_action` replaces
    `answer` (adds Hold/Noted — not every escalation is a decision gate), `resolution` records what
    was actually done, `-By`/`-AnsweredBy` attributes who answered (Claude|Researcher, defaults to
    Researcher since this script IS the researcher's own terminal).

    -Action List        writes every open (unanswered) escalation to escalation.list_report_path
                        (default iba/app/reports/escalation-list.md; archived on regenerate, same
                        convention as every other report) and prints a one-line pointer + count —
                        fixed 2026-07-23, it used to dump the full list to the terminal only.
    -Action Answer       answer a WORD-scoped escalation (new-word approval). Needs -Word and
                         -Decision (Approve|Reject; Yes|No still accepted as aliases).
    -Action AnswerRun    answer a RUN-scoped escalation (a config proposal, or a quality-check
                         finding from Candidate-Quality.ps1 / Passage-Quality.ps1 / Config-
                         Maintenance.ps1). Needs -RunId and -Decision (Approve|Reject|Revise|Hold|
                         Noted); -Comment is required with Revise, optional otherwise. -Resolution
                         optional — what was actually done, if anything.
    -Action Raise        add your OWN item to the escalation table — a researcher-initiated
                         flag/note, not raised by a running step. Needs -Question. Prints the
                         synthetic run_id to answer it with later (AnswerRun, same as any other).
                         -AssignedTo (Claude|Researcher, default Researcher) and -Type
                         (task|run_error|issue|notice|config, default task) optional.

    Added 2026-07-23 — for working the escalation table as a backlog of items for Claude, not only
    design decisions awaiting approval. Run-scoped/manual only (same boundary AnswerRun already
    draws against word-scoped Answer):
    -Action Edit         replace a still-open (raised or on-hold) escalation's question wording.
                         Needs -RunId and -Question. The old wording is preserved (not lost) in
                         the row's `tried` field with a timestamp.
    -Action Pause        set a raised escalation aside without answering it — excluded from the
                         active queue a real dispatcher run would resume against, but still shown
                         in -Action List, flagged. Needs -RunId; -Comment optional.
    -Action Resume       bring an on-hold escalation back into the active (raised) queue. Needs -RunId.
    -Action Retract      withdraw an open escalation — "never mind", not a reviewed decision.
                         Terminal, like a completed answer, but distinguishable from one in the
                         record. Needs -RunId; -Comment optional.

.EXAMPLE
    .\Escalation.ps1 -Action List
.EXAMPLE
    .\Escalation.ps1 -Action Answer -Word hypocrisy -Decision Approve
.EXAMPLE
    .\Escalation.ps1 -Action AnswerRun -RunId RUN-20260721_163604_125-CANDIDATE-QUALITY -Decision Approve
.EXAMPLE
    .\Escalation.ps1 -Action AnswerRun -RunId RUN-... -Decision Revise -Comment "check the H0430 cluster first"
.EXAMPLE
    .\Escalation.ps1 -Action AnswerRun -RunId RUN-... -Decision Noted -Resolution "acknowledged, no action needed"
.EXAMPLE
    .\Escalation.ps1 -Action Raise -Question "Revisit the anger/spirit dual-characteristic overlap in candidate_seed"
.EXAMPLE
    .\Escalation.ps1 -Action Edit -RunId MANUAL-20260723_055356_776621 -Question "Corrected wording..."
.EXAMPLE
    .\Escalation.ps1 -Action Pause -RunId MANUAL-20260723_060301_575459 -Comment "waiting on the STEP schema question first"
.EXAMPLE
    .\Escalation.ps1 -Action Resume -RunId MANUAL-20260723_060301_575459
.EXAMPLE
    .\Escalation.ps1 -Action Retract -RunId MANUAL-20260723_061922_821483 -Comment "superseded by #274's rework"
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('List', 'Answer', 'AnswerRun', 'Raise', 'Edit', 'Pause', 'Resume', 'Retract')]
    [string] $Action,
    [string] $Word,
    [string] $RunId,
    [ValidateSet('Yes', 'No', 'Approve', 'Reject', 'Revise', 'Hold', 'Noted')] [string] $Decision,
    [string] $Comment,
    [string] $Question,
    [string] $Resolution,
    [ValidateSet('Claude', 'Researcher')] [string] $AnsweredBy = 'Researcher',
    [ValidateSet('Claude', 'Researcher')] [string] $AssignedTo = 'Researcher',
    [ValidateSet('task', 'run_error', 'issue', 'notice', 'config')] [string] $Type = 'task'
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
    'Answer' {
        if (-not $Word -or -not $Decision) {
            Write-Host "Answer needs -Word and -Decision (Approve|Reject; Yes|No accepted as aliases)." -ForegroundColor Yellow
            exit 1
        }
        if ($Decision -notin @('Yes', 'No', 'Approve', 'Reject')) {
            Write-Host "Answer's -Decision must be Approve or Reject (word-scoped approval)." -ForegroundColor Yellow
            exit 1
        }
        python -m iba.app.lib.escalation answer $Word $Decision.ToLower() "--by=$AnsweredBy"
    }
    'AnswerRun' {
        if (-not $RunId -or -not $Decision) {
            Write-Host "AnswerRun needs -RunId and -Decision (Approve|Reject|Revise|Hold|Noted)." -ForegroundColor Yellow
            exit 1
        }
        if ($Decision -notin @('Approve', 'Reject', 'Revise', 'Hold', 'Noted')) {
            Write-Host "AnswerRun's -Decision must be Approve, Reject, Revise, Hold, or Noted." -ForegroundColor Yellow
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
        if (-not $Question) {
            Write-Host "Raise needs -Question." -ForegroundColor Yellow
            exit 1
        }
        python -m iba.app.lib.escalation raise "--source=researcher" "--assigned-to=$AssignedTo" "--type=$Type" $Question
    }
    'Edit' {
        if (-not $RunId -or -not $Question) {
            Write-Host "Edit needs -RunId and -Question." -ForegroundColor Yellow
            exit 1
        }
        python -m iba.app.lib.escalation edit $RunId $Question
    }
    'Pause' {
        if (-not $RunId) {
            Write-Host "Pause needs -RunId." -ForegroundColor Yellow
            exit 1
        }
        if ($Comment) {
            python -m iba.app.lib.escalation pause $RunId $Comment
        } else {
            python -m iba.app.lib.escalation pause $RunId
        }
    }
    'Resume' {
        if (-not $RunId) {
            Write-Host "Resume needs -RunId." -ForegroundColor Yellow
            exit 1
        }
        python -m iba.app.lib.escalation resume $RunId
    }
    'Retract' {
        if (-not $RunId) {
            Write-Host "Retract needs -RunId." -ForegroundColor Yellow
            exit 1
        }
        if ($Comment) {
            python -m iba.app.lib.escalation retract $RunId "--by=$AnsweredBy" $Comment
        } else {
            python -m iba.app.lib.escalation retract $RunId "--by=$AnsweredBy"
        }
    }
}
