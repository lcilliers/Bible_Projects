# What `configmaint.validate` actually checks — and why it passed the passage hodgepodge clean

> Requested 2026-07-29 after the passage config extract showed stale/contradictory rows
> (`passage-rules-audit-20260729.md`, `passage-config-full-extract-20260729.md`) that no
> escalation ever caught. Read live code (`handlers/configmaint.py`, `lib/cfgquality.py`,
> `lib/valuequality.py`), then ran the check live against today's DB to confirm. Read-only.

## Confirmed live: it passes clean today

```
HARD ERRORS: 0
ORPHANS: 0
NEEDING JUSTIFICATION: 0
```

Run directly against `iba.db` as it stands right now — the exact state documented in the two
passage config reports. `configmaint.validate` would report **"cfg_* tables are coherent... no
orphans, no settings needing justification"** if invoked today. No escalation would fire.

## Every check it runs (`handlers/configmaint.py:_validate_live`, 14 checks)

**Hard structural checks — fail outright, no escalation, no judgement call:**

1. No `cfg_table` has more than one PK column.
2. Every `cfg_column.fk` points at a real table and a real column.
3. Every `cfg_unique.col` names a real column.
4. Every *active* `cfg_api` route contains a `{version}` placeholder.
5. Every *active* `cfg_write_grant.table_name` is a real table.
6. No step name is registered under more than one *active* work package (steps must be globally
   unique — `cfg_on_fail`/escalation match by step name alone).
7. Every *active* step's `handler` resolves to a real `module:function` that actually exists.
8. Every *active* `cfg_on_fail.path` is a member of `enum.on_fail`; its `step` is a known step.
9. Every *active* `cfg_status_flow` (entity='word') status is a member of `enum.word_status`.
10. Every *active* `cfg_setting` whose key contains "pattern" is a valid compiled regex;
    `report.span_fields`/`report.strong_fields` name real columns.
11. Every *active* `cfg_setting` has a non-null `module`, and that module is a member of
    `enum.config_module`.
12. **governance.reports_must_persist** — every *active* step in the hardcoded
    `QUALITY_CHECK_REPORT_PATH` dict (`configmaint.validate`, `candidate.validate`,
    `passage.validate`, `lexicon.validate`) has an active, non-null report-path setting.
13. **report-governance** — every *active* step in the hardcoded `REPORT_STEPS` tuple has an
    active `cfg_report` row; every *active* chained work package has a `complete_message`.
14. **value-quality** (`valuequality.find_enum_violations`) — for every `cfg_column` declaring
    `expectation = enum.<name>`, every **non-null** live value in that column is a member of the
    declared enum.

**Advisory checks — escalate if found, don't fail:**

15. **Orphan configs** (`find_orphan_configs`) — an *active* `cfg_setting`/`cfg_enum` whose key/
    name doesn't co-occur with a real `.setting(`/`.enum(` call in the same source file.
16. **Settings needing justification** (`find_settings_needing_justification`) — an *active*
    `cfg_setting` whose module already has a dedicated table (currently only `candidate` →
    `cfg_candidate_rule` is registered this way).

## Why none of the 16 catch the passage hodgepodge

The stale/contradictory rows found in the passage audit are, specifically:

- `cfg_column` rows on `passage` (`rule`, `source`, `filled_by='passage.build'`) describing a
  retired mechanism, with every live value **NULL**.
- `cfg_table` descriptions for `passage`/`verse_passage` still describing the pre-2026-07-26
  candidate-driven grain, not the current completion-tracking use.
- `cfg_enum` groups `passage_rule`/`passage_source` still `inactive=0` though nothing populates
  the columns they'd validate.
- `cfg_on_fail`'s `findings-rejected` message text ("...needing the rule revisited") referring to
  a rule that no longer exists.

Mapped against the 16 checks above:

- **Checks 1-11, 12-13** are pure structural/plumbing checks (PK/FK counts, enum-membership of a
  *few specific* columns, handler resolvability, report-path/row presence). None of them read or
  reason about a `use`/`does`/free-text description field at all — there is no mechanism anywhere
  in the validator that compares a description to whether the thing it describes is still active.
- **Check 14 (value-quality)** only flags a value **outside** the enum. `passage.rule`/
  `passage.source` are `NULL` on every live row — `NULL` is explicitly excluded
  (`if r2["v"] is not None`), so an all-NULL column after its populating step went inactive
  produces **zero** findings. This is a structural blind spot: "nothing was ever written" and
  "everything written conforms" look identical to this check.
- **Check 15 (orphans)** only scans whether a config's *name* still appears in source code
  together with a `.setting(`/`.enum(` call — it does not check whether that *code path is ever
  reached*. `handlers/passage.py:build()` still exists and still calls
  `ctx.cfg.setting("passage.default_rule", ...)` etc. in its source text, so those settings and
  the `passage_rule`/`passage_source` enums all read as "used" even though the step that uses them
  is `inactive=1` and never runs. Dead-but-present code masks the orphan check completely.
- **The retired `passage.*` settings themselves (`inactive=1`) are excluded from every "active-
  only" check (1-15 all filter `WHERE inactive=0` or equivalent)** — by the standing rule
  (escalation #310, 2026-07-23) that a deactivated config shouldn't keep tripping validation. That
  rule is reasonable on its own terms, but it means **nothing ever re-checks whether the *other*,
  still-active rows that describe or depend on a now-inactive row (a `cfg_column.filled_by`
  naming an inactive step, a `cfg_table` description of a retired mechanism, an `cfg_on_fail`
  message written for a retired rule) get updated to match.** Retiring a row is checked structurally
  (nothing points at a *deleted* table/column); it is not checked *narratively* — no rule enforces
  "if you retire mechanism X, every other config that describes X in prose must also be revisited."

## The gap, stated plainly

`configmaint.validate` checks that the config **is internally wired correctly** (FKs resolve,
enums are well-formed, handlers exist, reports have somewhere to write). It has **no check for
whether the config is a coherent, current, non-contradictory *story*** — i.e., whether free-text
descriptions, enum vocabularies, and on-fail messages that reference a mechanism still agree with
whether that mechanism is active. A whole module can be retired correctly by every structural
measure this validator applies, while five or six *other* rows scattered across `cfg_column`,
`cfg_table`, `cfg_enum`, and `cfg_on_fail` keep describing it as if it still ran — and the
validator will report "coherent" throughout.

No fix proposed or applied here — this is the requested explanation of current behaviour only.
