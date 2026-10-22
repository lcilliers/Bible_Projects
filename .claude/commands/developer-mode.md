---
description: Enter a Developer Mode session — building/fixing the IBA app itself, exempt from configmaint.propose's approval gate (cfg_behaviour_rule developer-mode-scope-and-conduct)
---

# Developer Mode — Session Declaration

For a session that builds or fixes the IBA app itself. The scope of the mode and the conduct
inside it are `cfg_behaviour_rule` `developer-mode-scope-and-conduct`; the two modes are
`iba/app/CHARTER.md` §4.

This command runs only as the first prompt of a fresh session. The hook
`.claude/hooks/gate_developer_mode_entry.py` refuses it otherwise. If it ran anyway, check
`.claude/.session-boundary-state.json`: unless `start_source` is `startup` or `clear`, stop and
say so. It does not bootstrap the IBA app (`iba/app/ps/Start-Iba.ps1`); that is a separate ask.

## 1. Permission boundary

State in chat what permission mode the session appears to run under, from what is observable
(`.claude/settings.json`, approval prompts so far). This command cannot grant permissions. If
nothing shows elevated permissions, say so and ask the researcher to confirm before treating the
approval gate as bypassed.

## 2. Load the rules

Write and fill this session's compliance file with the rules that apply in Developer Mode
(the general rules, `cfg_rule_scope`, with `deliver_when` `always` and `developer_mode`, plus
`study_active` while the study is active; the rest come at their point of use):

```powershell
.\iba\app\ps\Compliance.ps1 -Action Template -Mode Developer
.\iba\app\ps\Compliance.ps1 -Action Check -Phase Start
```

Fill it as `/start-project` step 3 describes; the declaration is not complete until Check passes.
Read `iba/app/CHARTER.md` §4.

Run the backlog check:

```powershell
.\iba\app\ps\Escalation.ps1 -Action List
```

Note every open item with `next_action_assigned_to='Claude'`, however old.

## 3. Set the signal

- Write the current UTC timestamp to `.claude/.developer-mode-active`.
- The statusline (`.claude/statusline-devmode.ps1`, `statusLine` in `.claude/settings.json`) reads
  that file. Say whether it is wired up; don't claim it if it isn't.

## 4. Report and stop

State in chat:
- the permission finding
- that the compliance file passes, and the rules named in its conflicts section
- that Developer Mode is the declared basis and the marker file is set
- whether the statusline is wired up
- every item assigned to Claude, by id and short description

Then ask what to build or fix. Start nothing on your own initiative.

## 5. For the rest of the session

While `.claude/.developer-mode-active` exists, every reply starts with this line:

> 🛠️ **DEVELOPER MODE ACTIVE** — `configmaint.propose` gate bypassed; every other rule still
> applies.

`/exit-developer-mode` removes the marker and ends the banner.
