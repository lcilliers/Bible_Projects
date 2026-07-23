<#
.SYNOPSIS
    The researcher's side of every escalation — list open ones, answer a word approval, or
    answer a run-scoped (config proposal / quality-check) escalation. The one PS front door for
    lib/escalation.py, which every other governed operation already has and this one didn't.

.DESCRIPTION
    -Action List        show every open (unanswered) escalation.
    -Action Answer       answer a WORD-scoped escalation (new-word approval). Needs -Word and
                         -Decision (Yes|No).
    -Action AnswerRun    answer a RUN-scoped escalation (a config proposal, or a quality-check
                         finding from Candidate-Quality.ps1 / Passage-Quality.ps1 / Config-
                         Maintenance.ps1). Needs -RunId and -Decision (Approve|Reject|Revise);
                         -Comment is required with Revise, optional otherwise.
    -Action Raise        add your OWN item to the escalation table — a researcher-initiated
                         flag/note, not raised by a running step. Needs -Question. Prints the
                         synthetic run_id to answer it with later (AnswerRun, same as any other).

.EXAMPLE
    .\Escalation.ps1 -Action List
.EXAMPLE
    .\Escalation.ps1 -Action Answer -Word hypocrisy -Decision Yes
.EXAMPLE
    .\Escalation.ps1 -Action AnswerRun -RunId RUN-20260721_163604_125-CANDIDATE-QUALITY -Decision Approve
.EXAMPLE
    .\Escalation.ps1 -Action AnswerRun -RunId RUN-... -Decision Revise -Comment "check the H0430 cluster first"
.EXAMPLE
    .\Escalation.ps1 -Action Raise -Question "Revisit the anger/spirit dual-characteristic overlap in candidate_seed"
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [ValidateSet('List', 'Answer', 'AnswerRun', 'Raise')] [string] $Action,
    [string] $Word,
    [string] $RunId,
    [ValidateSet('Yes', 'No', 'Approve', 'Reject', 'Revise')] [string] $Decision,
    [string] $Comment,
    [string] $Question
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
            Write-Host "Answer needs -Word and -Decision (Yes|No)." -ForegroundColor Yellow
            exit 1
        }
        if ($Decision -notin @('Yes', 'No')) {
            Write-Host "Answer's -Decision must be Yes or No (word-scoped approval)." -ForegroundColor Yellow
            exit 1
        }
        python -m iba.app.lib.escalation answer $Word $Decision.ToLower()
    }
    'AnswerRun' {
        if (-not $RunId -or -not $Decision) {
            Write-Host "AnswerRun needs -RunId and -Decision (Approve|Reject|Revise)." -ForegroundColor Yellow
            exit 1
        }
        if ($Decision -notin @('Approve', 'Reject', 'Revise')) {
            Write-Host "AnswerRun's -Decision must be Approve, Reject, or Revise." -ForegroundColor Yellow
            exit 1
        }
        if ($Decision -eq 'Revise' -and -not $Comment) {
            Write-Host "Revise needs -Comment — what should be checked/changed." -ForegroundColor Yellow
            exit 1
        }
        if ($Comment) {
            python -m iba.app.lib.escalation answer-run $RunId $Decision.ToLower() $Comment
        } else {
            python -m iba.app.lib.escalation answer-run $RunId $Decision.ToLower()
        }
    }
    'Raise' {
        if (-not $Question) {
            Write-Host "Raise needs -Question." -ForegroundColor Yellow
            exit 1
        }
        python -m iba.app.lib.escalation raise $Question
    }
}
