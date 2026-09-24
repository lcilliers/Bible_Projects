---
description: Session-close validation — escalation update coverage, governance/config/doc drift, BUILD.md tracking-id coverage (escalation #1875)
---

# Session Close — Close-Out Validation

Run this at the end of a session, before handing off. It checks three things the researcher asked
for directly (escalation #1875, 2026-09-24): (a) every escalation touched this session actually
got a proper update recorded, (b) governance/config/doc text that this session's chat decided
should change actually changed, with superseded text properly marked, and (c) any build/update
activity this session is recorded in `iba/app/BUILD.md` with a proper tracking id. This command
does the DETECTION mechanically, then has you (Claude) do the REMEDIATION using the actual
conversation content — the detection script cannot write the sentence that fixes a gap, only find
it.

Do not skip steps. This command ends by re-confirming the checks are clean (or explaining what's
deliberately deferred), not by stopping at "found some gaps."

## 1. Run the detection script

Run `iba/app/ps/Session-Close.ps1` via the PowerShell tool. It re-reads this session's own JSONL
transcript (harness-native, already recorded automatically — no separate tracker needed), diffs
git state since session start, cross-references `escalation_history` and `BUILD.md`, and persists
a report. It never blocks — always exits 0/continue. Read the report path it prints.

## 2. Read the report

Read the full report (`iba/app/reports/session-close.md`, or the versioned path the script just
printed). It has three sections: escalation update coverage, governance/config/doc drift, BUILD.md
coverage.

## 3. Remediate (a) — escalation update gaps

For every escalation id the report lists under "GAPS" (touched in the transcript, `escalation_history`
behind it): re-read this session's own conversation for what was actually said/decided about that
item, then call `Escalation.ps1 -Action Update` (or `-Action Correction` if the item is already
closed) to add the missing entry. Per the researcher's exact instruction, the entry must capture —
not just a general summary:

- **researcher update verbatim** — their own words, quoted, not paraphrased
- **design debates** — the back-and-forth, options considered, objections raised
- **design decisions** — what was actually decided and why
- **anything skipped, postponed, or ignored** — named explicitly, not silently dropped

This is filing paperwork for something that already happened in this same session — do this
directly, no approval cycle needed.

## 4. Remediate (b) — governance/config/doc drift

The report lists which of `GOVERNANCE.md`/`CLAUDE.md`/`USER-GUIDE.md` changed in this session's
git diff window — but whether they changed ENOUGH is not mechanically checkable, so do this by
hand: re-read the session's own decisions (the conversation, and this session's `SESSION-LOG-*.md`
if one exists) and check each one against those three files plus any relevant `cfg_*` row:

- If a decision should have updated governance/config and didn't, make that edit now (or file the
  `cfg_*` change via `Config-Maintenance.ps1 -Step Propose` if it's a config value, not just a doc).
- If new chat content conflicts with existing GOVERNANCE.md/CLAUDE.md/USER-GUIDE.md/config text,
  confirm the old text is marked superseded/retired (dated, pointing to what replaced it) — not
  left silently stale.
- This is also paperwork for an already-approved in-session decision — auto-remediate, no fresh
  approval cycle.
- **Exception**: if you find a genuinely NEW unresolved conflict — chat decided X, but it's
  ambiguous whether some existing doc/config still asserts incompatible Y, and it's not obvious
  which should win — that is not a documentation gap, it's a fresh judgement call. Do not silently
  pick a winner. Raise it as its own new `decision_required` escalation instead.

## 5. Remediate (c) — BUILD.md coverage

For every file the report lists under "GAPS" in the BUILD.md coverage section, add a proper
`iba/app/BUILD.md` entry (next sequential `## N.` id after the current highest, matching the
existing entry shape: title line with date/attribution/escalation refs, a verbatim researcher
quote where applicable, a **Build** paragraph naming the actual files/functions, a **Test plan
run** paragraph, a **Not done here** paragraph if anything was deliberately deferred, and a closing
**Files:** line). If several gap files belong to the same piece of work, one entry covering all of
them is correct — don't force one entry per file.

## 6. Re-confirm clean

Re-run `Session-Close.ps1`. Confirm 0 escalation-update gaps and 0 BUILD.md gaps. A remaining
governance/doc item is acceptable only if you've explicitly judged it doesn't need a change (say
why); anything you fixed should no longer show as changed-without-BUILD.md-entry.

## 7. Commit and push

Completing a `/session-close` cycle is a standing pre-authorization to commit
(`governance.session_log_triggers_commit`, `CLAUDE.md` §12, widened 2026-09-24 to cover this
command specifically, escalation #1876) — the same trigger a completed `SESSION-LOG-*.md` already
is. Do the full cycle in this same unit of work, not a separate pass:

1. `git status` — see everything outstanding, not just what this session's own remediation touched
   (CLAUDE.md §12's "default scope" rule: stage the full outstanding diff, not session-own changes
   only — but still read anything unfamiliar before staging it, and still exclude
   `database/bible_research.db`/`backups/`).
2. Stage it, write a proper commit message (`session YYYYMMDD: brief description`, per CLAUDE.md
   §12), commit.
3. Push.
4. Confirm `git status` is clean and the push succeeded — don't assert it, show the actual output.

## 8. Report

Summarise in chat: what the checks found, what was fixed, whether anything was escalated as a
fresh decision_required item under the exception in step 4, and the commit/push confirmation from
step 7. Do not present this as a `.md` deliverable — a brief chat summary plus the report path is
enough, per the standard interaction protocol for a status check.
