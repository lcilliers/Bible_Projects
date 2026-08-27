# What config actually governs `comment`/`context`/`resolution` — live extract

> Extracted directly from `iba.db` (`cfg_column`, `cfg_escalation_requirement`, `cfg_escalation`,
> `cfg_behaviour_rule`), 2026-08-26, for escalation #857. Same method as the `next_action=review`
> extract (`escalation-review-action-config-rules-20260826.md`): queried live, not reasoned from
> `Escalation.ps1`'s help text. Bottom line up front: **the only config that defines what these
> three columns mean, or how they differ, is their own `cfg_column.use` text.** No
> `cfg_escalation` row and no `cfg_behaviour_rule` row addresses them at all. Exactly one of the
> three (`comment`) has a presence requirement, and exactly one (`resolution`) has a
> content-conditional requirement; `context` has none.

## 1. `cfg_column.use` — the column definitions themselves (the only place the semantics live)

**`escalation.comment`** — *"additional information for the assigned party. Cumulative, same
rule as context."*

**`escalation.context`** — *"what must be done or the error message, plus links to external
documents. Cumulative: an Update's input is the increment, appended onto the current value (plan
v3 §2)."*

**`escalation.resolution`** — *"what was actually done -- REQUIRED when next_action=approved
(validity check, plan v3 §3)."*

That third definition is the only one of the three that states a requirement inline — and it's a
partial statement (see §2, it's also required at `ready_for_approval`, not just `approved`).

These three `use` strings are the **entire** live definition of what belongs where. In
particular: **`context`'s own definition is the one that says file links go there** ("plus links
to external documents") — this is not stated anywhere else in config. It is the source of the
researcher correction captured as `feedback_escalation_links_go_in_context_not_resolution`
(escalation #784, 2026-08-22) — that correction restates this exact `cfg_column.use` text, it does
not add a new rule on top of it.

**`escalation_history`'s versions of the same three columns carry a real asymmetry**, also stated
only in `cfg_column.use`:

- `escalation_history.comment` — *"delta: the raw increment THIS version added, NULL if this
  version didn't touch it — was wrongly 'full cumulative text' under the retired full-snapshot
  design ... 'the cumulative is only in escalation'."*
- `escalation_history.context` — *"delta: ... same correction as comment, above."*
- `escalation_history.resolution` — *"snapshot of escalation.resolution at this version"* — **not**
  a delta. `resolution` is a single terminal value set once (at `approved`), so each history row
  just carries what `escalation.resolution` held at that point; `comment`/`context` accumulate
  across many versions, so their history rows correctly store only that version's increment, not
  the running total.

## 2. `cfg_escalation_requirement` — which of the three is actually enforced

Checked against the full active table (13 rows, same set as the `review` extract):

| Field | Rows found | What's enforced |
|---|---|---|
| `comment` | 1 (`action='raise'`, `condition='always'`) | Required **only at Raise** — *"comment is required at Raise -- minimum: what the item is about."* No requirement row for `comment` on Update, Correction, or any other action. |
| `context` | **0** | **No requirement row exists for `context` at all**, on any action. Nothing mechanically forces it to be filled, ever — including at Raise, where a new item could in principle be raised with no context and no check would catch it. |
| `resolution` | 2 (`action='approved'`, `action='ready_for_approval'`, both `condition='always'`) | Required when the item is being moved to `ready_for_approval` (the readiness check) and re-confirmed required at `approved` (D25 — checked twice, once at each stage of the two-stage handshake). No requirement row for any other action. |

So: `comment` has a one-time presence check, `resolution` has a two-time presence check tied to
the approval handshake, and `context` has **none** — its entire governance is the `cfg_column.use`
sentence in §1, honoured by convention only.

## 3. `cfg_escalation` and `cfg_behaviour_rule` — searched, nothing found

Both tables were searched for any row mentioning `comment`, `context`, or `resolution` by name or
in free text. **Zero rows in either table address these three columns** — not their meaning, not
their cumulative-vs-snapshot behaviour, not which one a link or a decision belongs in. The
7-row `cfg_escalation` rule set (source classification, duplicate suppression, module blocking,
resolution precedence, chat routing, document reference grouping, full-path file references) and
the active `cfg_behaviour_rule` rows (decision-required-answered-via-update-not-answerrun,
test-plan-per-module-utility, and the escalation-adjacent chat/development pointers already
surfaced in the `review` extract) are all silent on this specific question.

## 4. What this means, concretely

- **`context` is the least governed of the three fields in this table.** It carries real
  operational weight (per its own `use` text, it's where "what must be done," error messages, and
  every external document link belong — the exact place the researcher has twice had to correct
  Claude for putting links in `resolution` instead, #784) but has zero presence check, zero
  content-shape check, and no `cfg_escalation`/`cfg_behaviour_rule` row backing its definition —
  only the one `cfg_column.use` sentence.
- **`resolution`'s requirement is asymmetric with its own `use` text** — the `use` string only
  names `approved`; the actual enforcement (§2) also fires at `ready_for_approval`. The full rule
  lives correctly in `cfg_escalation_requirement`, but `cfg_column.use` under-states it — a minor
  documentation gap in the config's own self-description, found live while extracting this.
- **Nothing anywhere validates the cumulative-append behaviour actually happens** — `comment` and
  `context` being append-only (rather than overwritten) is asserted in `cfg_column.use` and in the
  `escalation_history` columns' own `use` text, but there is no `cfg_escalation_requirement` row
  or `check_kind` that verifies an Update's increment was appended rather than replacing the prior
  text. It is a code-level guarantee (`escalation.update`, per `filled_by`), not a config-enforced
  one.
