---
description: Session close — detection (SC1-SC12) of what the session did, decided or left open against its record; remediation; session log; commit blocked until clean; two commits
---

# Session Close

Rebuilt 2026-10-20 (escalation #2173; proposal
`outputs/markdown/session-routines-session-close-change-proposal-v1-20261020.md`). Purpose: end
the session so that nothing done, decided or left open in it exists only in the chat or in an
unrecorded file, and the base data and the narrative are sound. **Detection is code
(`Session-Close.ps1`); remediation is Claude's.** Do not skip steps. **Nothing is committed while
`Session-Close.ps1` exits 3** (`cfg_behaviour_rule` session-close-blocks-commit-on-open-findings).

## 1. Detect: `iba\app\ps\Session-Close.ps1`

`handlers/session_close.py` writes `session_close.report_path` (versioned). Each finding has a
stable key. The checks:

| step | finds |
|---|---|
| SC1 | no session id or no boundary record (the close fails: the window is unknown) |
| SC2 | spine FATAL (`handlers/spine.compute`): span -> strong, verse <-> span, strong -> cluster, strong -> meaning against STEP |
| SC3 | a researcher message in the transcript that is in no escalation comment written this session |
| SC4 | (a) an `Open items` line in a changed file with no open OT-nn.n / #nnnn; (b) a researcher message with a holding word (`session_close.held_words`) |
| SC5 | (a) a chapter file changed with no recorded weave; (b) a quotation in a chapter's added lines not in the ESV text; (c) a register-check finding new since the last close, or standing on a chapter changed now (rule 77); (d) a verse a changed reading file names with no placement, or placed `told` and not told |
| SC6 | an engaged rule in the compliance file with no evidence, or evidence that does not check |
| SC8 | no session log naming this session, or a missing/empty section |
| SC9 | a decision line in the log naming no target that changed this session |
| SC10 | a code/config file changed (`session_close.build_scope`) not named in what BUILD.md gained |
| SC12 | whether the narrative copy and the threads export are needed |

Read the whole report.

## 2. Remediate (SC7)

Fix each finding. Where a fix is not made now, disposition it. Dispositions go in the compliance
file's `## Close dispositions` section, one line each: `- <finding key> :: <disposition>`. The check
verifies every disposition; an unchecked one leaves the finding open.

- **SC3:** write the missing `Escalation.ps1 -Action Update` (the researcher's words verbatim, the
  debate, the decisions, anything skipped), then the finding clears itself; or
  `:: recorded in #n vN` / `:: no record needed: <reason>` (e.g. a bare "proceed" recorded in the
  context of the item it answers).
- **SC4:** raise the item the same turn (rule 21) and name it: `:: in register OT-nn.n` /
  `:: in register #nnnn`; or `:: not held: <reason>`. Fix an `Open items` line by naming its
  handle.
- **SC5:** record the weave (`Narrative-Register.ps1 -Action Record`); correct a misquote (or
  `:: not scripture: <reason>` for a quoted gloss or statement); reconcile register findings under
  rule 77; add the missing placements.
- **SC6:** add the evidence for each engaged rule in the compliance file.
- **SC2, and anything not fixed now:** `:: carried OT-nn.n` or `:: carried #nnnn` (an open item;
  raise it if needed).
- **SC10:** a BUILD.md entry (`## N.`, matching the existing shape) that names each file.

## 3. Session log (SC8, SC9)

Write `Logs/SESSION-LOG-<date>-<topic>.md` (`governance.session_log_dir`), naming the session id,
with the six sections headed exactly as `session_close.log_sections`: `## 1. Scope`,
`## 2. Escalations`, `## 3. Files`, `## 4. Decisions`, `## 5. Open items`, `## 6. Git`
(`governance.session_log_required_content`). In **4. Decisions** each line names where the
decision was recorded: a file path, a `cfg_*` table, or `#nnnn vN`. Leave **6. Git** to step 6.

## 4. Re-run (SC11)

Re-run `Session-Close.ps1` until it exits 0 (no open finding). Repeat steps 2-3 as needed.

## 5. Publish only what changed (SC12)

The script prints `publish (SC12)`. Only if it says NEEDED:

- narrative copy: `iba\app\ps\Copy-NarrativeToLearning4Comfort.ps1` (report what it copied);
- threads export: `iba\app\ps\Escalation.ps1 -Action Export -Type thread`.

Never publish to GitHub (`governance.no_direct_github_publish`).

## 6. Commit and push, twice (SC13)

Standing pre-authorisation: `governance.session_log_triggers_commit`, CLAUDE.md section 12.

1. `git status`; stage every outstanding change (read anything unfamiliar first; never
   `database/bible_research.db`, `backups/`); commit `session YYYYMMDD: ...`; push.
2. Write **6. Git** into the session log: branch, the commit hash and the push output, from the
   actual git output. Commit it alone with the message
   `session YYYYMMDD: session log git confirmation` (`session_close.final_commit_marker`; the
   next start checks for it) and push.
3. Show `git status` clean and the push output.

## 7. Report (SC14)

The close report (`session_close.report_path`) is the persisted record. In chat: the findings
carried rather than fixed (with their items), and the two commits with the push confirmation.
