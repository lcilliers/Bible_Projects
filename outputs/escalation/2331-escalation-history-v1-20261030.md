# Escalation deep history

## #2331 — Reading: no way to put a done verse back in hand
type=issue source=researcher

**v1** (2026-10-30T05:13:58Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Reading: no way to put a done verse back in hand
> **comment (set this version):** Found 2026-10-30 in the #2329 trial, standard session 698fb0d0. The trial redoes the 39 done m21-asking verses under the new parts, but Reading.ps1 -Step Observe puts only waiting verses in hand: run for Gen 37:15 it answered 'no verse waiting or in hand (39 done)'; Record only writes verses in hand (iba/app/lib/reading.py, observe at line 542, record at line 808). No step returns a done verse to waiting. Nothing was changed on the live database; a named snapshot iba/app/db/snapshots/kept/iba-20261030T051301Z-2329-trial-before-redo.db was taken before the attempt. Options: (A, recommended) build a re-open action in Reading.ps1 that returns named done verses to waiting with a logged reason, so Observe and Record redo them by modifying in place (RS-04) and RW-01 holds; built in a Developer Mode session, then the trial resumes in standard mode. (B) Set the 39 verses to waiting by editing _analytics/Clusters/M21 - fasting-piety/m21-asking/m21-asking.json by hand: quick, but a change to the scope index outside the app (governance.project_change_rule) with no logged reason; not recommended. Decision sought: approve A, or B, or another route. Related: #2329, #2320.
> **context (set this version):** iba/app/lib/reading.py; _analytics/Clusters/M21 - fasting-piety/m21-asking/m21-asking.json; outputs/escalation/2329-phase-1-fit-for-purpose-design-v1-20261030.md

**v2** (2026-10-30T05:15:30Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Decision with options, as in the item's first comment.
> **resolution (set this version):** Approval sought: option A, a re-open action in Reading.ps1 that returns named done verses to waiting with a logged reason, so Observe and Record redo them by modifying in place (RS-04); option B (hand edit of the scope JSON) not recommended.

**v3** (2026-10-30T05:15:30Z, Researcher) state=re-assigned next_action=approved assigned_to=Claude
> **comment (set this version):** Researcher, chat 2026-10-30 (verbatim): 'Approve A'.
> **resolution (set this version):** Approved option A: build a re-open action in Reading.ps1 that returns named done verses to waiting with a logged reason, so Observe and Record redo them by modifying in place (RS-04). Built in a Developer Mode session (config first, then code, spec, USER-GUIDE, BUILD); then the #2329 trial resumes in a standard session.
