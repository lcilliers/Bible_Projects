# Escalation #1017 — dispatcher-tied vs. manual transactions, explained

You asked (v4): *"I need more help to fully understand what the options are for dispatcher-tied
transactions in the escalation actions worksheet. I definitely do not have a proper handle on this
transaction usage."* Grounded directly in your own worksheet's actual content and `escalation.py`
— not reasoned from memory.

## The core distinction

**Manual** ("Decision-tied-Manual" — your worksheet's top section, rows 3–19): an escalation you
or Claude create or edit by hand, addressing it by its **id** (a permanent row in the `escalation`
table). `Raise`, `Update`, and `Correction` all work this way.

**Dispatcher-tied**: an escalation that a PS *tool run* raised automatically because it hit an
approval gate mid-execution (e.g. `Config-Maintenance.ps1 -Step Propose` pausing for your
decision). It's addressed by its **run id** (`RUN-...`), not its escalation id — because the whole
point is to resume *that specific paused run* once you've decided, not just edit a record. Three
actions: `AnswerRun`, `ResolveSelfCorrectable`, `EscalateToDecision`.

## Your worksheet's "Despatcher-tied" section is a stub, not a bug in your understanding

Rows 26–29 have header labels (`-action`, `-Id`, `-Decision`, `-AssignedTo`, `-Comment`,
`-Context`) but — unlike every row in the "Decision-tied-Manual" section above it — **no working
compiled-command formula**, and the headers don't actually match what these 3 actions need
(`-Id` isn't used by any of them; `-RunId` is, and it's missing entirely). That's why this felt
ungraspable — the sheet itself doesn't yet describe these three actions correctly.

## The three dispatcher-tied actions

**`AnswerRun`** — answer a run that's currently paused waiting for your decision (e.g. a
`Config-Maintenance Propose` pause). Flags: `-RunId <the paused run's id>` `-Decision
<Approve|Reject|Revise|Hold|Noted>` `-AnsweredBy <Claude|Researcher>` `[-Comment ...]`.
```
Escalation.ps1 -Action AnswerRun -RunId RUN-20260829_063456_930-CONFIGMAINT -Decision Approve -AnsweredBy Researcher
```

**`ResolveSelfCorrectable`** — close out a `self_correctable`-type escalation (Claude's own coding
mistake, already fixed — no decision needed from you at all, per `cfg_behaviour_rule
'decision-points-are-terminal-not-inline'`). Flags: `-Id <escalation id>` `-Resolution <what was
wrong and what changed, required>` `-AnsweredBy <usually Claude>`.
```
Escalation.ps1 -Action ResolveSelfCorrectable -Id 1010 -Resolution "off-by-one, fixed and re-ran clean" -AnsweredBy Claude
```

**`EscalateToDecision`** — converts a `self_correctable` item into a real `decision_required` one,
when attempting the fix reveals it's actually a genuine judgement call, not just a slip. Flags:
`-Id <escalation id>` `-Tried <what was attempted, required>` `-AnsweredBy <usually Claude>`.
```
Escalation.ps1 -Action EscalateToDecision -Id 812 -Tried "widened the retry window, but the limit is a design choice" -AnsweredBy Claude
```

## The 5 flags missing from BOTH worksheet sections (the actual `#1017` finding)

The worksheet-drift check (built earlier today, escalations #1012–#1014) found these `Escalation.ps1`
parameters used nowhere in your sheet at all:

| flag | used by | for |
|---|---|---|
| `-RunId` | `AnswerRun` | which paused run this answers (see above) |
| `-AnsweredBy` | `AnswerRun`, `ResolveSelfCorrectable`, `EscalateToDecision`, `Update` | who's recording the decision — `Claude` or `Researcher`. **Required, no default** — this is the field that determines whether the system will let a `ready_for_approval` item actually close (only `Researcher` may). |
| `-Tried` | `EscalateToDecision` (required), optionally `Raise` | what was attempted already |
| `-ShortDescription` | `Correction` (row 19 is *also* a stub — a header with no formula) | fixing a wrongly-worded title on an existing escalation, without it counting as a new decision |
| `-Source` | `Raise` | who/what originated it — defaults to `'researcher'`, essentially never needs setting by hand |

## What I'd suggest for the worksheet

Two real gaps, same shape as the working "Decision-tied-Manual" section above them:

1. **"Despatcher-tied" (rows 26–29):** replace the `-Id` column with `-RunId`, add `-AnsweredBy`
   and `-Resolution`/`-Tried` (used by 2 of the 3 actions, not the `-Decision` one), and give it a
   working compiled-command formula per row, one row per action (`AnswerRun`/
   `ResolveSelfCorrectable`/`EscalateToDecision`) — matching how each `Decision-tied-Manual` row is
   its own concrete example, not one shared row for three different action shapes.
2. **"Correction" (row 19):** currently a bare label with no header row or formula at all —
   needs the same treatment (`-Id`, `-ShortDescription`, `-AnsweredBy`, `-Comment`).

I can build both sections properly, matching your existing formula style exactly, once you
confirm — this is your model sheet, so I want your go-ahead on the shape before touching it, not
just my own guess at how you'd want the columns laid out.
