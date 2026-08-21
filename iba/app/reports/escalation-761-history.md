# Escalation deep history

## #761 — -AnsweredBy required friction in researcher's own terminal
type=issue source=researcher related_activity=escalation-module-rebuild-20260820 from_id=

**v1** (2026-08-21T12:13:52Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** -AnsweredBy required friction in researcher's own terminal
> **comment (set this version):** Researcher, verbatim: "got this error. Update needs -AnsweredBy Claude|Researcher -- no default (escalation rebuild 2026-08-20: a silent 'Researcher' default previously misattributed >=39 history rows in one session). AnsweredBy should be fully automated. Are there any others you also missed". This should have become an escalation the moment it was reported (cfg_escalation.chat_routing) -- went straight to investigate-and-fix in chat instead, a real miss caught only when the researcher asked directly whether one had been raised.
> **context (set this version):** Root cause: -AnsweredBy has no default in lib/escalation.py (deliberate, since the 2026-08-20 rebuild -- a silent 'Researcher' default previously misattributed >=39 history rows to the wrong party). That fix never distinguished WHO was actually running the PS front door -- the researcher, typing it by hand in their own terminal, hit the exact same hard stop Claude is meant to hit.
> **related activity (set this version):** escalation-module-rebuild-20260820

**v2** (2026-08-21T12:13:52Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **resolution (set this version):** Fixed same session: $env:CLAUDECODE (set in every shell Claude Code drives, confirmed live; never set in a terminal the researcher opens themselves) used as the safe signal. Escalation.ps1 now auto-defaults -AnsweredBy to Researcher when omitted AND not running under Claude Code -- covers AnswerRun/Raise/Update at once, one shared check before the switch. Claude's own invocations are unaffected (CLAUDECODE=1 always present), so the original hard stop still fires exactly as the 2026-08-20 rebuild intended -- the misattribution risk this rule exists to prevent is not reopened. Checked every OTHER mandatory parameter across AnswerRun/Raise/Update (-RunId/-Decision, -Question/-Comment, -Id, -State+-Comment on reject) for the same class of gap -- all are genuine per-call data, not attribution gaps; no others found. Tested both branches in isolation (no DB writes) before touching the real script, then a real -Action List end-to-end. USER-GUIDE.md updated in the same pass. Committed: 48590f83. Awaiting your confirmation the auto-attribution is what you wanted.

**v3** (2026-08-21T13:36:28Z, Researcher) state=completed next_action=approved assigned_to=Researcher
