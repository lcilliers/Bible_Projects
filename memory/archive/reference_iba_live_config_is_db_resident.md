---
name: reference_iba_live_config_is_db_resident
description: "The IBA app's LIVE config is DB-resident (iba/app/db/iba.db, cfg_* tables) seeded from iba/app/config/cfg_*.csv — NOT the aspirational governance docs in iba/config/*.json."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 17d30e5a-09c0-4950-83c7-4ab98c83ccd4
  modified: 2026-07-21T12:51:04.034Z
---

When investigating IBA app behaviour (candidate seeding, spans, etc.), the config that actually governs
runtime is in **`iba/app/db/iba.db`**, tables `cfg_*` (`cfg_candidate_rule`, `cfg_table`, `cfg_column`,
`cfg_write_grant`, `cfg_change_log`, `cfg_enum`, `cfg_setting`, `cfg_step`, `cfg_status_flow`,
`cfg_work_package`, `cfg_on_fail`, `cfg_unique`, `cfg_api`, `cfg_connection`, `cfg_book_order`, `cfg_meta`).
The human-editable seed source for each is a CSV in **`iba/app/config/*.csv`** (index at
`iba/app/config/cfg-table-csv-index.md`); a load stamps a row into `cfg_change_log`.

**Do NOT treat `iba/config/process/*.json` + `iba/config/_manifest.md` (the "envelope"/rule-store
documentation with `id/governs/kind/subject/status/authority/reference/intent/satisfaction/validation/spec`
and `cfg_apply.py`/`cfg_helper.py`/`cfg_kernel.py`) as the live config** — that is a separate, more
elaborate governance-design layer (aspirational rule store, `ent.cfg.rule`) that, as of 2026-07-21, has
no matching table in either `database/bible_research.db` or `iba/app/db/iba.db`. It documents an intended
richer envelope (open questions, RECONCILE status, audited sole-write-path) that the actual running app
config (the thin `cfg_*` tables above) does not yet implement.

**Why:** On 2026-07-21 I read `iba/config/process/base.json`/`base.md` as "the config" governing
candidate seeding and proposed filing an `open.*` question there. The researcher corrected me: wrong file
— the real config is in the DB. Tracing it found `iba/app/db/iba.db.cfg_candidate_rule` (schema
`kind,value` only, seeded from `iba/app/config/cfg_candidate_rule.csv`) is what actually drives the
`ib-judgement` accept-list read by `iba/app/handlers/candidate.py` — and its missing `tag` column is the
real cause of 281/489 blank `candidate_seed.tag` rows (which propagate to `span_candidate.candidate_tag`
in `iba/app/db/iba.db`, exported as `outputs/csv/span_candidate-iba-*.csv`).

**How to apply:** When told "check the config" for IBA app behaviour, look first at `iba/app/db/iba.db`
cfg_* tables and their `iba/app/config/*.csv` seeds. Only reach for `iba/config/*.json` when the
discussion is explicitly about the governance/design layer itself, not about why the running app is
doing something. Ties to [[project_iba_analytic_phase_blocked_on_data_layer_stability]].
