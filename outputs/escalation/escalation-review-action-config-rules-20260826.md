# What config actually governs a `next_action=review` escalation — live extract

> Extracted directly from `iba.db` (`cfg_escalation`, `cfg_escalation_transition`,
> `cfg_escalation_requirement`, `cfg_enum`, `cfg_behaviour_rule`, `cfg_setting`), 2026-08-26 —
> per `governance.iba_config_first_not_doc_archaeology`: config queried live, not reasoned from
> `Escalation.ps1`'s help text or from docs. Bottom line up front: **there is no dedicated
> `cfg_escalation_transition`/`cfg_escalation_requirement` row for `next_action='review'`
> specifically** — that part of this extract stands. **§3 below does not** — see the
> **2026-08-26 CORRECTION** box before reading it; it checked the wrong `cfg_enum` name and its
> "the whole enum is inactive" conclusion is wrong. The corrected picture: `review` is a live,
> validated, active enum value that simply has no mapped *transition outcome* — a much narrower
> and more likely-intentional gap than originally reported.
>
> **★ 2026-08-26 CORRECTION (found while tracing `iba/app/lib/escalation.py`'s own config-read
> path for escalation #857, filed as `escalation-scripts-config-paths-20260826.md`):** §3 below
> checked `cfg_enum` for `name='escalation_next_action'` and found it entirely inactive — true,
> but that is a **retired, superseded enum name**, confirmed by the module's own docstring
> ("`escalation_next_action` (the old merged cfg_enum) is retired"). The code actually validates
> `next_action` against **two split, fully active groups**: `escalation_next_action_manual`
> (includes `review`, ordinal 5, `inactive=0`) and `escalation_next_action_dispatcher`. **`review`
> IS a live, active, validated enum member right now.** §3's "no live, enforced vocabulary check"
> conclusion, and the §5 Answer's echo of it, are both wrong as originally stated — corrected
> versions of both appear below, left struck through rather than deleted so the error is visible,
> not hidden.

## 1. `cfg_escalation_transition` — `review` has no matching row

The full active table (8 rows) was dumped. Every `manual`-shape `next_action` value that
resolves to something is matched by name — `approved`, `reject`, `revise`, `noted`,
`ready_for_approval`. `review` is **not** one of them. It falls through to the generic
priority-6/7/8 rows, and priority 6's own note says so explicitly:

> priority 6, condition `explicit_state_given` → `resulting_status_key='__unchanged__'`: *"Only
> 'review' or no next_action can still reach this priority (approved/reject/revise/noted/
> ready_for_approval are all already intercepted by priorities 1-5 above)."*

So when an item sits at `next_action=review`, the config's own transition table treats it as: no
mapped outcome → state stays whatever the caller's `-State` says, or carries forward unchanged,
or derives to `re-assigned` if only `-AssignedTo` changed (priority 7). **`review` is a hold
marker, not a controlled action with its own rule** — it means "read this and respond," nothing
more specific is encoded.

## 2. `cfg_escalation_requirement` — no field is mandated *because* next_action is review

Full active table (13 rows) checked for any row keyed `action='review'` — none exists. The
requirement rows that *do* apply to any reply (via `-Action Update`, which is how a `review` item
is normally answered) are action-level, not review-specific:

- `update` / `from_id` (`exists`, `not_self`) — if `-FromId` is touched, it must resolve and not
  self-reference.
- `update` / `related_activity` (`field_required`, condition `from_id_set`) — must be paired with
  `from_id` when that's set.
- `update` / `state` (`check_kind='not_raised_with_content'`, condition `has_content`) — **the one
  requirement that actually bites on most `review` replies**: an Update carrying
  comment/context/tried cannot leave the item at `state='raised'` — it must move off `raised`
  first (D26).

Nothing in this table requires a resolution, a decision, or any specific field just because the
item's `next_action` happens to be `review`.

## 3. `cfg_enum` — ~~`escalation_next_action` (including `review`) is currently INACTIVE~~ CORRECTED: `review` is live and active, via a different (split) enum group

~~Checked live: `cfg_enum` has no active row for `name='escalation_next_action'` at all — every
value sits in the 29-row "UNATTRIBUTED inactive" bucket surfaced by `configmaint.validate`'s own
§1 report. So `review` isn't just unmatched in the transition table — the whole enum family it
belongs to has no live, enforced vocabulary check right now.~~ **Wrong as stated — see the
correction box above.** `escalation_next_action` is real and really is fully inactive, but it is a
*retired predecessor*, not the enum the code reads. `iba/app/lib/escalation.py` actually validates
`next_action` against two split groups: **`escalation_next_action_manual`** — `ready_for_approval`,
`approved`, `reject`, `revise`, `noted`, **`review`** (ordinal 5) — **all 6 active** — and
**`escalation_next_action_dispatcher`** — `approve`, `reject`, `revise`, `hold`, `noted` — **all 5
active**. `review` is a live, validated enum member right now. This is unrelated to escalation
**#851** ("`noted` has no authority check unlike `approved`"), which is about the *authority*
check on `next_action=approved`, not enum validity — the earlier sentence linking them was also
mistaken.

## 4. The rules that DO actually bind a reply — general, not review-specific

Nothing in the three escalation-specific config tables singles out `review`. What actually
governs how Claude must respond is the general-purpose behaviour rules in `cfg_escalation`
(rule_key) and `cfg_behaviour_rule` (class), all still active:

| Rule | Governs |
|---|---|
| `cfg_escalation.resolution_precedence` (id 4) | Open items with `next_action_assigned_to='Claude'` — which a `review`-to-Claude item is — take precedence over other work. *Not mechanically enforced — session practice.* |
| `cfg_escalation.chat_routing` (id 5) | Any judgement call surfaced while replying that isn't a closed, fully-reasoned decision must get its own escalation in the same turn, not be left in chat prose — applies symmetrically to Claude's own findings and to researcher feedback given in chat. |
| `cfg_behaviour_rule` id 21 (`chat.chat-items-become-escalations`) | Pointer restating the same rule at the `chat` behaviour-class level. |
| `cfg_behaviour_rule` id 40 (`development.open-items-route-through-escalation`) | Same principle, non-chat form — any open item found doing the review (a data-quality gap, a stale doc, etc.) goes into `escalation`, not a silent fix or a buried report mention. |
| `cfg_escalation.full_path_file_references` (id 7) | Any file named in the reply's text fields must be a full repo-relative path. |
| `cfg_escalation.document_reference_grouping` (id 6) | If the reply is one of several related rows, `context` carries the reference doc and `related_activity` is shared across the group. *Not currently mechanically enforced.* |
| `cfg_escalation.issue_decisions_produce_documentation_tasks` (id 12) | If the reply closes an issue whose resolution states a new/changed rule, or changes user-facing behaviour, a companion task to update `GOVERNANCE.md`/`USER-GUIDE.md` must be raised in the same turn. |
| `cfg_escalation.chat_start_work_moves_to_in_progress` (id 13) | If the researcher's message effectively says "start work," the reply's Update call must carry `-State in-progress` — and this half **is** mechanically enforced, via the `update`/`state`/`not_raised_with_content` requirement row in §2 above. |

## 5. Answer (corrected)

**No, there is no dedicated `cfg_escalation_transition` or `cfg_escalation_requirement` row that
specifically governs a `next_action=review` reply.** That part stands. `review` is the
fall-through, unmapped value in the transition table (explicitly documented as such at priority
6) — but it is a **legally validated, active enum value** (§3, corrected), not an unvalidated
dangling one. What actually constrains how Claude replies is the general escalation
behaviour-rule set (§4 above) plus the two generic `update`-action requirements (§2). The
remaining, narrower, real question is a design one: `review` currently produces no state change
and no requirement at all — is that the intended shape (a pure "FYI, read this" marker with no
side effects), or should it map to something in `cfg_escalation_transition`? That's a much smaller
question than "an unvalidated value in active use," which is what this report originally,
incorrectly, claimed.
