# Escalation #1778 — observation-enhancer rule utility — build proposal

**Not built.** Proposal per your direction, verbatim: *"this audit functionality is based on a set
of rules (to be define) that will run the observations and nodes to improve the alignment of the
data after the completion of the llm work. The rules will progressively be defined and added, as
gaps are discovered in the data. the aim is for you to create a untility that can use input to
update the related table. the input will be generated follow user driven exploration to identify
actions to be taken."*

Reading this precisely: you don't want me inventing rules — you want the **mechanism** (a utility
that takes a rule as input and applies it), while the rules themselves come from you/us finding
real gaps in the data over time (exactly what tonight's #1769/#1770 investigations already were).
This proposal is for that mechanism only.

**Naming correction (this round):** the utility is **`observation_enhancer`**, not "correction" —
your correction, this chat turn. Every name below (work package, handler, PS script, log table)
is updated to match; nothing has been built under the old name.

## Decisions this round (your answers, this chat turn)

### 1. Rule storage — governance, not a file

You asked directly: *what would governance say about rule storage, and why was I deviating from
it?* Checking straight: `governance.rules_must_be_config_driven` — "no operational or process rule
may exist only in ... without a referenced `cfg_*` row recording it as the evidence that the
configuration control is in operation" — plus `governance.utility.config` ("each utility must have
its own config table in the `cfg_*` series") and `governance.config_control` (every `cfg_*` entry
is governed by `cfg.configmaint`). A rule that lives only in a hand-authored JSON file checked into
`iba/docs/` or `iba/app/rules/` is exactly the thing that first governance rule prohibits — it
can't be queried, validated, or coherence-checked by `configmaint`, and nothing records it as
config-controlled. Offering that as an equally-valid option alongside a table was the deviation;
there wasn't a good reason for it, just a lapse in checking governance first. Corrected:

- **New table `cfg_observation_enhancer_rule`** — the enhancer's own rule store, `cfg_table`/
  `cfg_column`-registered like every other config table, queryable and listable the same way
  `cfg_method_rule` already is. Columns: `id`, `rule_key`, `description`, `selector_sql` (§2),
  `update_json` (field/value pairs to apply), `status` (`draft` / `confirmed` / `active` /
  `retired` — a rule is `draft` until you confirm it, matching §2's per-rule confirmation step),
  `confirmed_at`, `created_at`, `ordinal`, `active`.

### 2. Selector scope — a DB query, confirmed per rule before it runs

Your answer replaces the narrow column=value grammar this proposal originally suggested: **the
selector is a real DB query** (a `SELECT` against `ib_observation`, joined to `ib_node` where a
rule needs it) — full expressive power, not a restricted mini-language. The safety mechanism isn't
a grammar limit, it's process: **every query is refined and confirmed with you before it's applied
to real rows** — the utility's `-Preview` step shows the query, its row count, and a sample of what
it would match; nothing runs live until you've looked at that specific query and said go. This
removes the need I flagged for "name a real rule in advance so the grammar doesn't need
redesigning" — a real SQL `SELECT` already covers any selector shape a future rule needs.

### 3. `ib_observation.status` — real bug, now tracked separately

Confirmed: yes, this utility will use `status` as one of its update targets (a rule can set
`status='needs-corroboration'` instead of touching `obs_text`). You asked for the underlying bug —
`status` was designed but never wired up — to be escalated on its own, not folded silently into
this proposal. Raised as **#1782**: `iba/app/lib/recordingpass.py:213`
(`_insert_observation`) hardcodes `status='resolved'` on every insert; all 7,046 live rows carry
that one value; the other 3 `cfg_enum` values (`needs-corroboration`, `open`, `silent`) have never
been written by any code path. That's a `DecisionRequired` item assigned to you (deciding the
write-time default and which status transitions belong to the LLM pipeline vs. this enhancer) —
this proposal doesn't block on it resolving first, since the enhancer can start writing
`needs-corroboration`/`open`/`silent` via its own `update_json` regardless of what recordingpass.py
defaults to at insert time.

### 4. Manual first, pipeline later

Confirmed: v1 runs manual/on-demand, matching every other one-off audit tool built this session.
As rules stabilise and the same rule gets applied repeatedly across runs, it graduates to a
pipeline step that runs automatically (a `cfg_step` addition at that point, not built now) — no
change needed to the mechanism itself for that later step, since `active`/`status='active'` rules
are already what a future automatic sweep would iterate over.

## What a rule contains

Two parts, both required:

1. **Selector** — a `SELECT` query against `ib_observation` (optionally joined to `ib_node`)
   identifying the target rows. Reviewed and confirmed by you, per rule, before it is ever run live
   (§2) — the query's own text plus a preview run (row count + sample) is what you're confirming.
2. **Update** — which field(s) on the matched `ib_observation` row(s) change, and to what. Direct
   `UPDATE`, matching your own word ("update the related table") — NOT a new superseding row via
   `supersedes_observation_id` (that chain is the LLM's own same/broaden/new decision at write
   time, a different mechanism with a different meaning; reusing it here would conflate "the model
   decided this observation broadens an earlier one" with "a human rule corrected a mistake after
   the fact").

## Proposed shape

- **Rule storage:** `cfg_observation_enhancer_rule` (§1) — not a file.
- **A new `ib_observation_enhancer_log` table** (this app's own established discipline —
  `governance.reports_must_persist`/every other write path logs what it did): one row per
  observation actually changed, recording `rule_id`, `observation_id`, the field(s) changed,
  before/after values, and timestamp. This is the audit trail that lets you (or me) answer "which
  rule touched this row, and what did it change" months later — the same kind of traceability
  `ib_node`'s own `traced_observation_id`/`source_stage` already gives the write-time pipeline.
- **Preview-then-live, same discipline as every other write script in this app**: `-Preview`
  default true, runs the rule's `selector_sql` and shows exactly which rows match and what would
  change, with counts, before anything is written; `-Preview:$false` applies for real, only once
  the rule's own `status` has been moved to `confirmed`.
- **A PS wrapper + registered handler**: `handlers/observationenhancer.py`
  (`preview(ctx)`/`apply(ctx)`), `ps/Observation-Enhancer.ps1`, work package
  `observation-enhancer`, `cfg_step`, `cfg_utility`, report path — registered the same way as
  tonight's `Purge-SoftDeletes.ps1`, not an ad hoc script.
- **First real rule**, once the table exists: #1769's `placeholder` row (id 4655) — the actual case
  that started this — as `cfg_observation_enhancer_rule` row 1, `status='draft'` until you confirm
  its selector and intended update (correct the text, or flag it via `status='needs-corroboration'`
  per #1782's status fix — your call once both exist).

## What I'd build, once you say go

1. `cfg_observation_enhancer_rule` + `ib_observation_enhancer_log` tables; `cfg_table`/`cfg_column`
   registration for both.
2. `handlers/observationenhancer.py` — `preview(ctx)`/`apply(ctx)`, running a rule's stored
   `selector_sql`, applying `update_json`, writing the log.
3. `ps/Observation-Enhancer.ps1`, registered in the ps tools worksheet.
4. `cfg_step`/`cfg_utility` registration, work package `observation-enhancer`.
5. First real rule (#1769's id 4655) entered as a `draft` row, confirmed with you, then applied —
   closing that loose end for real rather than leaving it as a one-off manual fix.

All four of the original open questions are answered above. Nothing built yet — say go and I'll
build items 1–4 in one pass, then bring you the first real rule for confirmation before it runs
live.
