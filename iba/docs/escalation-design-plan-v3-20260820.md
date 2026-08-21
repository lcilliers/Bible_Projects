# Escalation design plan (v3, 2026-08-20)

Supersedes [`escalation-design-plan-v2-20260820.md`](escalation-design-plan-v2-20260820.md).
Incorporates every correction from the review since v2: the relationship mechanism (`from_id` +
`related_activity`, not a typed link table), validation rules moved into config, the report content
(missing-link/incoherent-link exceptions), and the report registration itself (the existing
`cfg_report`/`cfg_report_section`/`cfg_report_csv_table` mechanism, not a new table). v2's
type-of-entries model (task/issue/notice/run_error/config, each a distinct shape of life) stands
unchanged — nothing since has touched it. Sections below are marked **unchanged from v2** where
that's true, so this reads as one coherent document rather than a diff to reconstruct by hand.

---

## Resources

Unchanged from v1/v2, plus this round's own source: the four review turns since v2 (the `from_id`
correction, its mutability/validation refinement, the missing-link/incoherent-link addition, and the
`cfg_report` correction) — all captured live in escalation `#6`, not reconstructed from chat memory
for this document.

---

## Purpose

**Unchanged from v2.** The utility exists to hold three genuinely different kinds of activity
(deciding, doing, recording) plus two automatic ones, in a shape that matches what each actually is,
connected well enough that "how did we get here" is answerable without re-reading prose. v2's three
gaps stand as stated; this round closes gap 2 (nothing links an item to what it came from) with a
simpler mechanism than v2 proposed, and adds real content to gap 3's report side.

---

## Type of entries

**Unchanged from v2** — `task` (do something, get it confirmed), `issue` (work out what should be
done, through rounds, before anything is built — its own `open`/`decided`/`abandoned` vocabulary),
`notice` (for the record, closes itself at raise, never enters the decision machinery), `run_error`
(a defect exists, task-shaped, tagged for provenance), `config` (a `configmaint.propose` pause,
narrowest and most specific). Full reasoning for each: v2 §Type of entries, not repeated here.

**What changes: how one item relates to another.** v2 proposed a typed many-to-many
`cfg_escalation_link` table. Wrong on two counts, corrected: `cfg_` is reserved for configuration —
rules that govern how *any* item behaves — never for data about *specific* items, which is exactly
what a link between two particular escalation rows is. And a typed many-to-many table solved a
problem that, checked against every real case found this session (the `#648` series, the `#712`
cascade, the supersede pattern), never actually occurred — every real chain is single-parent.

**The corrected mechanism:**

- `escalation.from_id INTEGER NULL` — the id this item builds on. One column, not a link table.
- `related_activity` (existing column, kept) — free text describing the relationship when paired
  with `from_id` (*"replaces previous," "follow-up on the config-review finding," etc."*). This
  single free-text field now does the job v2's whole enum (`produces`/`supersedes`/`duplicate_of`/
  `blocks`) was trying to pre-name — an issue "producing" a task is just `task.from_id = issue.id`,
  `task.related_activity = "implements the decision in #X"`. No fixed vocabulary needed; the
  researcher's own words carry it.
- **Both fields are optional, and available on Raise and Update alike** — not immutable-after-raise
  the way `short_description` is. A chain link can be corrected, added, or re-pointed later, which
  also means legacy messy chains (the `#712` cascade landing under the wrong label) can be retrofitted
  after the fact once the real relationship is understood.
- **Paired presence**: `from_id` and `related_activity` are set together or neither is — never one
  without the other, checked after merging this transaction's deltas onto whatever the row already
  holds (not just what's supplied this one call, since either could already be set from an earlier
  transaction).
- **Validation, narrow and specific**: `from_id` must reference an existing `escalation.id` (a live
  lookup — this app runs with FKs off everywhere, confirmed, so this is an explicit check, not a
  database constraint) and must not equal the item's own id. **The referenced item's state is
  explicitly irrelevant** — raised, in-progress, closed, completed, withdrawn are all valid targets.

**A real `escalation_tree` link table remains the fallback if many-to-many is ever actually needed**
— explicitly postponed, not built, per the researcher's own framing: *"I think we can get away with
a downward cascade only."*

---

## transaction types

**Unchanged in shape from v2** — Raise and Update remain the only two transaction types, still
branching by `type` as v2 described (task/run_error/config unchanged; issue validates against its
own three-value vocabulary; notice closes itself). **What's removed: v2's third transaction, `Link`.**
There's no separate operation any more — `from_id`/`related_activity` are just two more optional
fields on the same Raise/Update calls every other field goes through, validated by the same
paired-presence/existence/not-self rules regardless of which transaction sets them.

---

## tables and columns

**Carried forward, unresolved, not re-argued here:** the `escalation`/`escalation_history` stale
`cfg_table.use` text (`#4`); the id-sequence collision with `escalations_old` (`#5`) — **now more
urgent than before**, since `from_id` depends entirely on `id` being unambiguous; building a chain
mechanism on top of a colliding id sequence just relocates the same problem one column over.

**New this round:**

- `escalation.from_id INTEGER NULL` — the only new column anywhere in this design. No new table.
- `cfg_escalation_requirement` gains a `check_kind` column alongside its existing `condition_key`
  (see §configs) — reused, not duplicated.
- `escalation.next_action`'s `cfg_column.use` still needs the third vocabulary named (v2 finding,
  unchanged, unbuilt).
- `cfg_report`/`cfg_report_section`/`cfg_report_csv_table` gain rows for `escalation.list`/
  `escalation.history` (see §report) — using the tables that already exist, not new ones. **This
  requires a `cfg_step` row for each, which — checked live this round, not assumed — means both
  reports become real `run.py`-dispatched steps** (every live `cfg_report` row without exception is
  tied to a dispatcher-invoked `cfg_step`, confirmed against `retention.report`, `configmaint.report`,
  and every other active example; there is no precedent anywhere in the app for a `cfg_report`
  registration on an operation invoked outside `run.py`). This is bigger than "register two reports"
  — `Escalation.ps1 -Action List`/`-Action History` change from calling
  `python -m iba.app.lib.escalation` directly to dispatching through `run.py`, the same as every
  other governed script does. Directly related to `#8` (found this session: 8 of 45 PS scripts bypass
  `run.py` entirely, with no record of their own execution as a result) — closing this for
  escalation's own reports is one concrete instance of closing that wider gap, not a separate fix.

---

## Governance

**Unchanged rows from v2 stand** (not re-copied here — see v2 §Governance for the full
requirement/response/still-broken table). **What changes or adds this round:**

| Rule | This round's development |
|---|---|
| `governance.rules_must_be_config_driven` | `from_id`'s validation rules now genuinely go into config (`cfg_escalation_requirement`, extended) rather than living only in code — the actual fix v2 gestured at but didn't design correctly |
| *(new candidate)* — no `cfg_` naming discipline currently stated anywhere as a rule | This round's own mistake (`cfg_escalation_link`, a data table wrongly prefixed) is itself evidence a rule is missing: `cfg_` names configuration only, never a table holding rows about specific instances of the thing it governs. Worth a `governance.cfg_prefix_is_configuration_only` setting — the same treatment already given to `governance.escalation.type_is_structural` in v2, for the same reason: this exact mistake could recur anywhere else in the app that hasn't been checked (candidate work for `#9`, currently on hold) |
| `governance.reports_must_persist` | Unaffected in substance — still true both reports persist to a config-defined path. What's now clearer: persisting to a path and being *registered* (`cfg_report`) are different compliance questions, and only the first has ever been true for these two reports |

---

## control items

**Unchanged from v2** for task/issue/notice/run_error/config's own state combinations (v2 §control
items, not repeated). **New: the `from_id`/`related_activity` pair as its own control combination**,
orthogonal to `type`/`state`/`next_action` — it can be set (or not) on an item of any type, at any
point in its life:

| Combination | Meaning | Illegal |
|---|---|---|
| `from_id` NULL, `related_activity` NULL | Standalone item, no claimed relationship | — |
| `from_id` set, `related_activity` set, `from_id` references a real, distinct escalation | A real, described chain link | — |
| `from_id` set, `related_activity` NULL (or reverse) | Half-formed link | Rejected — paired-presence check |
| `from_id` = own id | Self-reference | Rejected — not-self check |
| `from_id` references a non-existent id | Dangling from the moment of write | Rejected at write time going forward; may still exist in older data (hence the report's "Dangling reference" exception, §report) |

---

## automation

**Unchanged from v2** except: no auto-linking logic to design (there was never going to be any — v2
already chose explicit-only), and the traversal automation is simpler than v2's graph walk — a
downward recursive walk over a single `from_id` column (children, grandchildren, ...), the same
queue-with-seen-set pattern `write_history_report()` already uses today (already cycle-safe by
construction — the existing `if eid in seen: continue` guard carries over unchanged; a cycle can't
infinite-loop the report even before the write-time guard below exists).

---

## configs

**Corrected mechanism, not a new table.** `cfg_escalation_requirement` (existing) gains a
`check_kind` column: today's rows are all implicitly `presence` (is the field non-empty). New kinds,
new rows, same table, same `_check_requirements()` call site generalised to read `check_kind`:

| action | field | check_kind | condition_key | message |
|---|---|---|---|---|
| raise / update | `from_id` | `exists` | `from_id_set` (fires only when `from_id` is actually being supplied) | `from_id` must reference an existing escalation |
| raise / update | `from_id` | `not_self` | `from_id_set` | an item cannot build on itself |
| raise / update | `related_activity` | `paired` | `from_id_set` | `related_activity` must describe the relationship whenever `from_id` is set |
| raise / update | `from_id` | `paired` | `related_activity_set` | `from_id` must be given whenever `related_activity` is being used to describe a chain link (the reverse pairing check) |

**No new enum.** `escalation_link_type` (v2) is retired with the table it belonged to — there is
nothing left to enumerate; the relationship's *nature* is free text, its *structure* is one integer
column.

**Report-side exception categories are `cfg_report_section` rows, not a bespoke config table** — see
§report. Same reasoning as the validation rules above: use what already exists rather than add
alongside it.

---

## validation

**Write-time (blocks the write, config-driven via the extended `cfg_escalation_requirement` above):**
`from_id` exists · `from_id` ≠ self · paired presence, both directions.

**Report-time (does not block anything — advisory, surfaced as named exceptions, per the
researcher's explicit framing: *"these are not errors, they are exceptions highlighted in the
report"*):**

| Exception | What it detects | Why it can exist despite write-time validation |
|---|---|---|
| Cycle | A builds on B builds on ... builds on A | Write-time validation only checks the single new link being written, not the whole graph it would complete — a cycle can form across two separate, individually-valid writes |
| Dangling reference | `from_id` points at an id that doesn't exist | Legacy data, written before this rule existed, or an item that only ever lived in `escalations_old` |
| Mismatched pairing | One of `from_id`/`related_activity` set, not both | Same — legacy data predating the pairing rule |
| **Missing link** *(new, researcher this round)* | An item with no `from_id`, and nothing else's `from_id` points at it either — fully isolated | Not a write-time violation (a standalone item is always legal) — a report-time visibility signal only. Every plain, one-off item will trip this; that's accepted, not a false-positive to suppress |
| **Incoherent link** *(new, researcher this round)* | An item's `from_id` points into an emergent cluster of related work, but its own `related_activity` text doesn't match what that cluster otherwise uses | The softest check here — proposed detection: compare against the *dominant* `related_activity` text already used by the other members of the cluster the `from_id` target belongs to. A structural proxy for "does this actually belong here," not a semantic judgement — flagged as a proposal, not yet confirmed as the right mechanism |

---

## scripts

**Carried forward from v2's inventory** (`escalation.py`, `Escalation.ps1`, `run.py`, the 8 handlers,
etc. — unchanged). **What's added/changed this round, as a plan, nothing built:**

- `escalation.py`: `_check_requirements()` generalised to read `check_kind`, not just presence; a
  new `_downward()` traversal function (queue/seen-set, `WHERE from_id=?`, recursive); the five
  report-time exception checks as their own small functions, each producing the rows one
  `cfg_report_section` row will render.
- `Escalation.ps1`: `-FromId`/`-RelatedActivity` (already exists) available on both `Raise` and
  `Update`. **If the `cfg_report` registration is actually built this round** (§tables and columns):
  `-Action List`/`-Action History` change from calling `python -m iba.app.lib.escalation` directly to
  dispatching through `run.py`, gaining a `run_id`, matching every other governed script.
- New: `handlers/escalation.py` (or equivalent) wrapping `write_list_report()`/`write_history_report()`
  as real dispatched handlers, if the `run.py` re-plumbing is approved — this is the concrete,
  scoped piece of work `#8` implies for this module specifically.

---

## report

**Corrected mechanism — the existing `cfg_report`/`cfg_report_section`/`cfg_report_csv_table`
tables, checked live this round, not a new table:**

| Config table | What it holds for `escalation.list`/`escalation.history` |
|---|---|
| `cfg_report` | `title`, `output_kind='md+csv'` (a CSV of flagged exceptions, matching every other report's offering), `naming_scheme`, `archive_dir`, `show_toc` |
| `cfg_report_section` | One row per section, ordered, headed, individually includable: the open-items table, the recently-resolved table, **and each of the five exception categories** (Cycle / Dangling reference / Mismatched pairing / Missing link / Incoherent link) as their own section — this is literally "what should be included in the report," the mechanism already built for exactly this |
| `cfg_report_csv_table` | The flagged-exception rows, exportable for the researcher to work through outside the report itself |

**Traversal**: the deep-history report's downward walk (§automation) replaces v2's link-table join —
simpler, since there's only one column to follow, not a typed graph.

**Still open, not resolved by this round**: whether the `run.py` re-plumbing this registration
implies (§tables and columns) actually gets built now, or stays a confirmed-correct-but-not-yet-built
design — a scope decision for the Summary below, not assumed here.

---

## Summary — decisions for this round

1. **`from_id` + `related_activity`, replacing the typed link table** — confirm this is now right, or
   still needs adjustment.
2. **The five report-time exception categories** — Cycle / Dangling reference / Mismatched pairing /
   Missing link / Incoherent link — confirm the set, and specifically whether the Incoherent-link
   detection proposal (dominant-label comparison within a cluster) is an acceptable starting mechanism.
3. **The `run.py` re-plumbing this round's report-registration correction implies** — build it now as
   part of this design, or register the config rows and leave the actual dispatch-wiring for later.
4. **Everything still carried unresolved from v1/v2** — the id collision (`#5`, now more load-bearing
   than before), the stale table text (`#4`), `GOVERNANCE.md` never updated, `cfg_utility.escalation.
   purpose` still the narrow one-liner.

Nothing built. Ready for the next section whenever you are.
