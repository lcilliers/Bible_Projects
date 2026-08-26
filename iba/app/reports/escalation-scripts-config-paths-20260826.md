# Escalation scripts (from `cfg_utility`) → the config each one reads to operate

> Extracted 2026-08-26 for escalation #857. Two-step method: (1) query `cfg_utility` for scripts
> genuinely associated with escalation (file path names it, not merely a "found via escalation
> #NNN" citation — the same distinction this thread already applied to governance rules and
> enums); (2) for each one found, grep its actual source for `cfg.*`/`cfg_*` read call sites — the
> real runtime path from script to config, not an inference from its `cfg_utility.purpose` text.
>
> **A correction surfaces along the way — flagged prominently, not buried: my earlier finding in
> this same escalation (v1/v5, "the whole `escalation_next_action` enum is inactive, `review` is
> unvalidated") checked the wrong enum name and is WRONG as stated. See §4.**

## 1. What `cfg_utility` actually says — literally one row

```sql
SELECT module, file_path FROM cfg_utility WHERE file_path LIKE '%escalation%'
```

Returns **exactly one row**: `module='escalation'`, `file_path='iba/app/lib/escalation.py'`. That
is the entire registered-in-config list.

## 2. What actually exists and operates — 18 more files, zero of them registered

Grepped the whole `iba/app` tree for real functional escalation integration (`import escalation`,
`lib.escalation`, `escalation.raise_`, `esc_raise`, etc.) — **27 files** genuinely touch the
escalation module at the code level. Cross-checked every one against `cfg_utility`:

- **`iba/app/lib/escalation.py`** — registered (the one row above).
- **4 other genuinely escalation-adjacent files that ARE registered** (for different, broader
  reasons — not because they're escalation-specific): `iba/app/lib/prosestore.py`,
  `iba/app/lib/cfgquality.py`, `iba/app/migration/flag_management_build_v1_20260823.py`,
  `iba/app/migration/fix_from_id_closed_items_20260821.py`.
- **16 escalation-NAMED migration scripts on disk, NONE registered in `cfg_utility`**:
  `add_escalation_state_in_progress.py`, `escalation_crash_review_rollout_20260821.py`,
  `escalation_explicit_state_priority_fix_20260821.py`, `escalation_redesign_v1_20260819.py` (+ its
  `_ROLLBACK` sibling), `escalation_redesign_v2_20260820.py`,
  `escalation_register_v9_build_20260821.py`, `escalation_reset_v1_20260816.py`,
  `escalation_v1_load_20260821.py`, `escalation_v1_snapshot_20260821.py`,
  `fix_escalation_history_write_grant_20260820.py`,
  `fix_escalation_short_description_and_columns_20260820.py`, `fix_escalation_titles_v2_20260820.py`,
  `rebuild_escalation_from_export_20260821.py`, `rebuild_escalation_rules_config_20260820.py`,
  `reset_escalation_tables_20260820.py`.
- **`iba/app/handlers/reports.py`** (serves `escalation.list`/`escalation.history`) and
  **`iba/app/run.py`** (the dispatcher — raises escalations directly on crash/report-stop, runs
  the `module_blocking` gate) — also unregistered, but this matches the project-wide pattern
  already found for the whole `handlers/` directory (zero files registered there) — not
  escalation-specific.

**This is a real, total gap against `governance.new_utility_registration_timing`** ("any new
script or routine... must be registered in `cfg_utility`... in the same unit of work it is
created") for one specific, clean category: every escalation-system migration script ever
written, 16 for 16, is missing from the registry that's supposed to catalogue exactly this.

## 3. The one registered script's real config path — `iba/app/lib/escalation.py`

Every `cfg.*`/raw `cfg_*` read call site found in the file, grouped by target table:

| Config table | What it's read for | Call site (paraphrased) |
|---|---|---|
| `cfg_write_grant` | Which tables this module may write | `cfg.may_write("escalation")` |
| `cfg_enum` (`escalation_state`) | Validates any `state` value being written | `db.cfg.enum("escalation_state")` |
| `cfg_enum` (`escalation_type`) | Validates any `type` value at Raise | `db.cfg.enum("escalation_type")` |
| `cfg_enum` (`resolution_kind`) | Validates `decision_required`/`self_correctable` | `db.cfg.enum("resolution_kind")` |
| `cfg_enum` (`escalation_next_action_manual`) | Validates a manual-shape `next_action` | `db.cfg.enum("escalation_next_action_manual")` |
| `cfg_enum` (`escalation_next_action_dispatcher`) | Validates a dispatcher-shape `decision` | `db.cfg.enum("escalation_next_action_dispatcher")` |
| `cfg_enum` (`escalation_assignee`) | Validates `next_action_assigned_to`/`originator` | `db.cfg.enum("escalation_assignee")` |
| `cfg_status_flow` (`entity='escalation'`) | Looks up a status by `set_by` pattern | raw SQL, `SELECT status FROM cfg_status_flow WHERE entity='escalation' AND set_by LIKE ?` |
| `cfg_escalation_transition` | The state-derivation engine — priority-ordered rule match | raw SQL, `... WHERE shape=? AND active=1 ORDER BY priority` |
| `cfg_escalation_requirement` | Field-requirement checks per action | raw SQL, `SELECT field, condition_key, check_kind, message FROM cfg_escalation_requirement ...` |
| `cfg_setting` (`escalation.control_objectives`) | Text shown in the List report header | `cfg.setting("escalation.control_objectives", "")` |
| `cfg_setting` (`escalation.control_process`) | Text shown in the List report header | `cfg.setting("escalation.control_process", "")` |
| `cfg_setting` (`escalation.list_report_path`) | Output path for the List report | `cfg.setting("escalation.list_report_path", "iba/app/reports/escalation-list.md")` |
| `cfg_setting` (`escalation.history_report_dir`) | Output directory for History reports | `cfg.setting("escalation.history_report_dir", "iba/app/reports")` |

**6 distinct tables** (`cfg_write_grant`, `cfg_enum`, `cfg_status_flow`,
`cfg_escalation_transition`, `cfg_escalation_requirement`, `cfg_setting`), **14 distinct read call
sites** counting each of `cfg_enum`'s 6 groups and `cfg_setting`'s 4 keys separately (corrected on
self-review — originally miscounted as "7 tables, 13 sites"). `cfg_escalation` itself (the 10-row
governance-rule table from the earlier extract) is **not** read anywhere in this file — it is
pure documentation, matching the "8 of 10 rows are session-practice, not mechanically enforced"
finding already on this item: the code has literally no code path that queries `cfg_escalation`
at all.

## 4. ★ CORRECTION to this item's own earlier findings (v1, v5)

Grepping this file surfaced the exact enum names the code actually validates against —
**`escalation_next_action_manual`** and **`escalation_next_action_dispatcher`** — not the single
merged `escalation_next_action` group I checked in the earlier extracts. Checked live, just now:

- `escalation_next_action_manual`: 6 values, **ALL ACTIVE** — `ready_for_approval`, `approved`,
  `reject`, `revise`, `noted`, **`review`** (ordinal 5, `inactive=0`).
- `escalation_next_action_dispatcher`: 5 values, **ALL ACTIVE** — `approve`, `reject`, `revise`,
  `hold`, `noted`.

**This means my earlier claim was wrong: `review` IS a live, active, correctly-validated enum
member right now.** The old merged `escalation_next_action` group (all 8 values inactive, found
in the v5 extract) is a genuinely **retired predecessor** — the module's own docstring says so
outright ("`escalation_next_action` (the old merged cfg_enum) is retired; the dispatcher and
manual [vocabularies are validated separately]") — the same shape as `escalation_answer`'s own
retirement, not a live gap. I did not check the code before drawing that conclusion the first
time; I should have.

**What survives the correction, unaffected:** `cfg_escalation_transition` genuinely has no
priority row matching `next_action='review'` to a resulting state (§1 of the original `review`
extract, re-verified — this part was checked against the transition table directly, not the enum,
and stands). But recast in light of §3-4 here, that reads much more like **an intentional
no-op** — `review` is a legally validated value whose entire semantic content the config engine
correctly says is "no state change, no requirement, just a marker for the current reader" — not
an unvalidated, dangling value the way the earlier framing implied. Whether that's still worth a
design decision (should `review` produce some resulting status?) is a much smaller, more precise
question than "the vocabulary is dead while in majority-share use," which was overstated.

## Summary

- `cfg_utility` names exactly **one** escalation script. **16 more exist, none registered** — a
  clean, total `governance.new_utility_registration_timing` gap.
- The one registered script's operation is governed by **6 config tables, 14 read call sites** —
  fully enumerated above.
- **A real error in this item's own earlier work is corrected here**: `next_action`/`review`
  validation is live and active via the correctly-split `escalation_next_action_manual`/
  `_dispatcher` enums; the "entire enum inactive" claim was based on checking a retired,
  superseded enum name instead of the two the code actually reads.
