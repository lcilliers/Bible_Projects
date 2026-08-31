# Session log — 2026-08-31 — Developer Mode built, escalation CLI friction found+fixed, backlog cleared

**Scope:** Direct continuation of the prior same-day session
(`SESSION-LOG-20260831-escalation-system-bugs-and-developer-app-mode-established.md`), whose own
"open items for next session" list named this session's actual work almost verbatim. Researcher
explicitly opened this session NOT via `start-project`, to establish a real Developer Mode
protocol first. Built the `/developer-mode` entry point, then used it to investigate and fix real
operational friction in the escalation CLI itself (found live, not assumed), then worked through
the prior session's stuck backlog, then built a mechanical Stop-hook check so backlog items
assigned to Claude can't silently go stale again the way #1312/#1314 just had.

## What was built

- **`.claude/commands/developer-mode.md`** / **`exit-developer-mode.md`** — session-level mode
  declaration commands (not a per-table/per-file self-classification — that mechanism was already
  rejected in the prior session). Loads live `cfg_behaviour_rule` class=`development` rows, states
  the harness permission boundary honestly rather than asserting a check that can't actually run,
  requires a backlog check (`Escalation.ps1 -Action List`) as part of entry — added mid-session
  after that omission let #1312/#1314 go unnoticed for one full turn.
- **Visual indicator** — `.claude/.developer-mode-active` marker file (gitignored) drives both a
  mandatory chat banner on every reply while active, and a statusline warning
  (`.claude/statusline-devmode.ps1` + `.claude/settings.json` `statusLine`), built via the
  `statusline-setup` agent, tested live (both branches) before trusting it.
- **`.claude/hooks/stop_check_escalation_backlog.py`** + `settings.json` `hooks.Stop` — queries
  `next_action_assigned_to='Claude'` live, every turn, blocks once (never loops —
  `stop_hook_active` respected) with the open list. Deliberately not filtered by type/age (no
  clean field distinguishes "forgotten" from "legitimately still in progress" — checked against
  real data before deciding this). Built via the `update-config` skill; all branches tested with
  real synthetic payloads before wiring in.
- **`iba/app/lib/escalation.py`** — three real fixes, each found live and verified live, not
  assumed:
  1. `main()`'s blanket `except Exception` treated every deliberate validation `ValueError`
     (title too long, missing `-Resolution`, wrong assignee) identically to a genuine crash,
     auto-filing a `run_error` escalation for each — seven such noise-rows existed from earlier
     today alone. Now: `ValueError` gets a clean stderr message and exit 1, no escalation write;
     genuine bugs still auto-file exactly as before.
  2. `requires_prior_ready_for_approval_if_decision_required` only checked that `ready_for_approval`
     existed *somewhere* in history, ever — not that it's where the item currently sits, so
     `ready_for_approval → revise → in-progress → approved` would have passed. Renamed to
     `requires_current_ready_for_approval_if_decision_required`, now checks the live row directly.
     Found while re-verifying an earlier, incomplete chat claim about this exact check — researcher
     caught it.
  3. `update()`'s status message showed only `state=`, hiding `next_action` — `state='re-assigned'`
     looked identical whether it meant "approved, routed back to Claude" or an ordinary
     reassignment. Now reports `state`, `next_action`, `assigned_to` together (`update()` and
     `correction()`; `resolve_self_correctable()` is always unambiguous, untouched).
  4. `update()` never forced the assignee to Claude on `approved`+`needs_claude_followup` — it just
     carried forward whatever `-AssignedTo` was passed. Now forced, overriding an explicit
     different value, since the flag's whole meaning is "Claude still has to act."
- **`iba/docs/escalation-operational-friction-review-v1-20260831.md`** — the living record of all
  of the above, four addenda, kept current in place rather than superseded by new files.
- **`cfg_behaviour_rule` id 63** (`claude-held-item-must-progress-or-bounce-back`) — an item
  assigned to Claude in an open working state has exactly two legitimate outcomes each time
  touched: complete and move it forward, or comment and bounce it back — never silent inaction.
  Researcher's own diagnosis after #1316 and #1327 both stuck; the Stop hook's reason text was
  sharpened to match after Claude initially just *mentioned* the backlog instead of acting on it.

## `actor_must_be_assignee` — built same day (prior session), removed same day (this session)

Prior session built a blanket guard: whoever currently holds an item is the only party who may act
on it *at all*, for every action. Researcher, hours later, reversed it in full: *"the objective of
the actor_must_be_assignee is to prevent you to do what you like. but I also see that it is now
preventing you from acting on a chat, and requires me to put all notes through the difficult to
use escalation excel tool... escalation activities are now consuming 80% of time spent on the
project... My conclusion is just drop this requirement."* Concrete trigger: it blocked Claude from
leaving the Researcher a clarifying note on #1337, and blocked the Researcher from giving Claude
feedback on #1306 — control with no matching benefit. Dropped via `cfg_escalation_requirement`
deactivation (reversible), not code deletion. The narrower D25 approval-authority check (who may
`approved`/`noted` a `decision_required` item) is untouched — that one gates a real decision.

## Escalations touched, by id and outcome

| id | outcome |
|---|---|
| 1309, 1310, 1312, 1315, 1321–1325, 1329 | **completed** — pre-existing stuck-approved records (assignee left at Researcher after approval, before today's forced-reassignment fix existed). Each individually verified against live reality before closing (grant revocations live, `cfg_escalation_requirement` rows present, corrupted row actually deleted) — not bulk-flipped. |
| 1330 | pre-existing fix from the prior session, confirmed still correctly completed. |
| 1338, 1339, 1341, 1344 | **completed** — CLI-crash noise from before this session's `actor_must_be_assignee` removal, closed as non-defects. |
| 1340 | **completed** — the `followup_cleared_was_approved` transition row (approved by researcher this session), applied live, the full approve-before-build-with-followup loop proven end to end. |
| 1345, 1346, 1348 | **completed** — this session's own three escalation-CLI fixes, self-correctable, each recorded with live verification evidence. |
| 1347, 1349 | **closed** — throwaway test items, explicitly labelled, verification purpose served. |
| 1316 | **re-assigned, `ready_for_approval`, assigned Researcher** — reset for review per researcher's own instruction ("if you are unsure, reset the item for my review") rather than guessed at: approved, but Claude's own prior note says it's superseded and should be rejected. Awaiting your decision. |
| 1327 | **re-assigned, `review`, assigned Researcher** — a proposed new guard (`ready_for_approval_not_assignable_to_claude`), commented and bounced back: the "proceed" authorizing it predates this session's `actor_must_be_assignee` reversal, and it's explicitly self-described as redundant belt-and-suspenders alongside a still-active guard. Genuinely unsure, not a guess to make. Awaiting your decision. |
| 1306, 1331–1335, 1337 | **re-assigned/in-progress, assigned Claude, deliberately deferred** — a reporting fix (bible_research.db schema-overview report + its 6 config registrations). Started work in this Developer Mode session before checking it against the researcher's own stated scope ("developer mode... normal work such as reporting... will all be in standard mode"); a raw config-write attempt was also independently blocked by the Claude Code harness's own permission classifier, confirming this session never had elevated write permissions beyond the app-level gate Developer Mode explicitly bypasses. Comment recorded on each record explaining the deferral. **Resume in a standard-mode session** — no config applied, script left unused at `[scratchpad]/register_schema_overview_bible_research.py` (not committed, session-local). |

## Decisions — whose

**Researcher's own decisions, this session:**
- Scoped Developer Mode explicitly: app-control-layer work only, not reporting/data/prototyping —
  stated once, applied by Claude late (the #1306 miss), corrected on the spot.
- Reversed `actor_must_be_assignee` in full, with reasoning (see above).
- Caught an incomplete claim about the approval-sequencing check — led directly to the real fix
  (#1348).
- Approved #1340 (the approve-before-build transition row) live, through the real mechanism.
- Directed the #1316/#1327 handling explicitly: reset-for-review when genuinely unsure; complete-
  or-bounce-back as the standing two-outcome cycle for anything Claude holds.
- Asked for the Stop hook — a mechanical check, specifically because a written/memory rule had
  already failed once at exactly this (#1312/#1314).

**Self-correctable — Claude found, fixed, and closed directly:** the three escalation.py fixes
(#1345/#1348, and the message-format fix, undocumented as its own escalation but covered by
#1348's record); the seven pre-existing stuck-approved records, each verified before closing.

**Claude's own process mistakes, corrected mid-session (not silently absorbed):**
- Claimed the D25 approval check "gates an actual decision" without having verified it fully —
  the researcher's direct question exposed the real gap (#1348).
- Let #1306's reporting work drift into Developer Mode without checking it against the
  researcher's own stated scope boundary, stated at the very start of this session.
- After building the Stop hook, twice just *mentioned* the surfaced backlog instead of doing the
  progress-or-bounce-back cycle on it — the researcher had to point this out explicitly before the
  actual routing work (#1316, #1327, the 7 stuck items) got done.

## Open items for next session

1. **#1316, #1327** — pending your review/decision, both reset to a state you can actually act on.
2. **#1306 + #1331–1335, #1337** — resume in a **standard-mode** session, not Developer Mode.
   Registration values are already fully specified (context field on each escalation); the code/PS
   script side is already built and confirmed present.
3. **#737, #738, #770, #784, #1006, #1007, #1022** — older backlog, assigned to Researcher,
   untouched this session, unrelated to today's work. The new Stop hook only checks items assigned
   to **Claude** — it will never surface these. Flagged, not fixed; whether a symmetric check is
   wanted is an open question, not decided.
4. Real code/doc changes are uncommitted going into this close — see Git state below for what
   actually got committed at session end.

## Git state
