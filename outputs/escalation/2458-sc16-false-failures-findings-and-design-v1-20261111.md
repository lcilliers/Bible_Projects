# #2458 SC16 counts designed refusals and misattributes failures: findings and design (for decision, B:105)

Session 8ca87189, 2026-11-11. Read-only investigation; nothing changed. SC16 is `_sc16` in `iba/app/handlers/session_close.py`, fed by `failed_calls` and `_operation` in `iba/app/lib/sessionwindow.py`.

## How SC16 works

Every tool result with `is_error` is a "failure". The first-use rules refusal (`Rules for this operation (`) and results carrying a text of `session_close.sc16_designed_stops` (COMMIT BLOCKED, NOT PASSED, a config change needs researcher approval) are skipped. The rest are grouped by an operation key; a key with two or more failures is a finding. The key is a PS script name (plus -Action or -Step) when the command text contains `<name>.ps1`, else the tool and the command's first word.

## Tested on two real transcripts (`failed_calls` run over the session transcripts)

| Session | Failures counted | Of which not a failure of the thing named |
|---|---|---|
| 8ca87189 (this one) | 12 | the retired-script hook denial twice (`Bash: python`, `Bash: mv`, "Retired script, not approved for use (#2200)", a hook refusing by design, not skipped); a Bash call whose text only names `Collection-Build.ps1` blamed on it; a multi-command PowerShell call whose last command failed, blamed on the first script named (`Collection-Build.ps1 -Action Evidence | === neither`, `Escalation.ps1 -Action Update | escalation ## v# -> ... ready_for_approval` whose own text is a success line); `Config-Maintenance.ps1 -Step Validate` exit 3 twice (a stated hard stop that decision B of #2220 keeps counted) |
| 77a059b4 (the #2458 session) | 13 | `Collection-Build.ps1` twice: a Bash call with `for lid, sh in pl["reshare"]:` (code text) and a shell syntax slip, both only naming the script |

## Causes (three, separable)

1. **A hook refusal is a failure unless it is the rules display.** `_RULES_SHOWN` skips one hook's text. The retired-script gate (`gate_retired_script.py`, "Retired script, not approved for use") denies by design and is counted; the other gates (such as the Developer Mode entry gate) are expected to be the same but were not seen refusing in these transcripts.
2. **A command that only names a script is attributed to it.** `_operation` searches the whole command text for `\w+.ps1`, so a Bash or Python heredoc that mentions a script, or a call chaining several commands, is keyed to the script and not to what failed. `gate_retired_script.py` already has the right reading (`_ps1_targets`: the script is run only when it is the first word of a command segment, follows `-File`, or follows a Python launcher).
3. **The error text is not the script's.** A call with several commands fails as a whole; the finding quotes the first error line, which may be another command's.

## Design (for your decision)

**A (recommended): fix causes 1 and 2, leave 3.**
- Cause 1, config only: add the text `hook error: ` (the text in every PreToolUse denial seen in this session, "PreToolUse:Bash hook error: ...") to `session_close.sc16_designed_stops`, through `apply_logged`. One row; no code. A genuinely crashed hook is a different text and stays counted (to confirm on a real crash before relying on it).
- Cause 2, code: in `_operation`, attribute a PS script only when the command runs it, reusing `gate_retired_script._ps1_targets`; otherwise key on the tool and first word as for any other call.
- Cause 3 stays: stated in USER-GUIDE and in the finding text ("the call may chain several commands").
- Test: re-run `failed_calls` and `_sc16` over the two transcripts above and over a built transcript with a refusal, a heredoc naming a script, a chained call and a real script failure; each must come out as intended; report the counts before and after.

**B: A plus splitting a chained call into its commands** so each error is attributed to the command that produced it. More code; the transcript does not say which command of a chain failed, so it can only be guessed from the error text (inferential, B:4). Not recommended.

**C: leave as is.** The finding stays noisy: a "fixed:" disposition is needed for each false repeat.

## What the researcher is asked

Approve A (config row plus the `_operation` change), choose B or C, or name another approach.
