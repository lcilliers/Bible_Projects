# Module config completeness audit + schema question (v1)

> Grounded in direct queries against the live `iba.db`, not assumption. Two things: (1) confirms your
> load-lifecycle observation is accurate — there is no app-wide-vs-module-activation load distinction
> today; (2) the actual per-module rule-sextet gaps, which is the real evidence behind "configs for
> individual modules seems incomplete."

---

## 1. Load lifecycle — your observation is correct, nothing exists today

Checked `Start-Iba.ps1`/`init.py` and all four work-package PS scripts. Today: `Start-Iba.ps1` loads
**everything** once (`cfgload` writes all `cfg_*` tables from the seed in one pass); after that, every
work-package script (`New-Word.ps1`, `Set-Candidates.ps1`, `Build-Passages.ps1`,
`Config-Maintenance.ps1`) just checks the app is already initialised and dispatches straight into
`run.py`. **There is no per-module load step anywhere** — `Cfg` opens one connection that can query any
`cfg_*` row at any time, with no distinction between "loaded at app-open" and "loaded on module
activation." Your description (app-wide settings load on open; module settings load on activating that
module) is not what's built — it's a real design gap, not something I'm aware of a reason to defend.

**Open question back to you:** is this a runtime/architecture change you want built now (an actual
load-phase distinction, e.g. each work package's first step explicitly loading/validating just its own
config slice), or is it more a description of how config *should be organised conceptually* (which the
completeness/audit work in §2–3 addresses without needing a runtime load-phase change)? These are
different amounts of work and I don't want to guess which you mean.

---

## 2. Per-module rule-sextet audit — concrete, not abstract

Every module's steps, `cfg_on_fail` rows, and `cfg_write_grant` counts, queried directly:

| module (handler file) | create/update/delete | data (settings) | relationships (write-grant) | output | validity (on_fail) | quality |
|---|---|---|---|---|---|---|
| `registry.py` | ✓ (`registry.create`) | `registry.strip_ends_pattern` (1) | ✓ (2 grants) | **none** — `report.py`'s settings aren't registry-specific | ✓ 3 rules | **none** |
| `raw.py` | ✓ (`raw.write`) | 4 settings (`discovery.*`, `meaning.*`, `language.*`) + `step.*` (8, owned by `stepapi.py`) | ✓ (6 grants across call1/2/3 + validate/write) | shared `report.*` (5) | ✓ 4 rules + 3 STEP preflight settings | **hard-coded only** — the forward-walk completeness check has no tunable threshold in config |
| `candidate.py` | ✓ (seed/set writes) | `candidate.lemma_base_pattern` (1) + `cfg_candidate_rule` (289 rows, **0 reject, 0 synonym** — flagged earlier) | ✓ (3 grants) | **none** | ✓ 2 rules | **none** — no reject-kind in active use, no quality threshold |
| `passage.py` | ✓ (`passage.build`, wholesale rebuild) | 4 settings, **1 dead** (`passage.cross_chapter` — found last session, code never reads it) | ✓ (2 grants); `verse_passage` uniqueness is schema-enforced (`cfg_unique`), not a named rule | `vw_passages_by_book` VIEW exists but **is not registered in `cfg_table`/`cfg_column` at all** — unlike every real table | ✓ 1 rule | **asymmetric** — `passage.review_over` catches too-long passages; nothing catches too-short/fragmented (the 1.56-avg problem) |
| `configmaint.py` | ✓ (`propose`) | 3 settings (`report_path` bug fixed last session) | ✓ (17 grants — every `cfg_*` table) | ✓ (`report` → `CONFIG-REPORT.md`) | ✓ 5 rules — the most complete of all five | present but **hard-coded, not config-tunable** (the step-dup + orphan checks) |

**The pattern, not just isolated gaps:** *quality* is missing or hard-coded-only in **every single
module** — never a setting the researcher can actually tune. *Output* is missing for two of five
modules. This is exactly the "comparative rules" problem you named: with the rule-sextet scattered
across `cfg_setting`/`cfg_on_fail`/`cfg_write_grant`/schema constraints, there was no single place that
would have shown this pattern — I had to hand-build the table above from five separate queries to see it.

---

## 3. The schema question — two ways to get "one list per module," fairly weighed

Your proposal: one table, with a "table indicator" column, so a module's full config is one query.

**Option 1 — your proposal, literally.** Merge `cfg_setting`/`cfg_on_fail`/`cfg_write_grant`/
`cfg_status_flow`/`cfg_candidate_rule` into one table, with a `kind` column (`setting`/`on_fail`/
`write_grant`/...) and a `module` column. `SELECT * FROM cfg_all WHERE module='passage'` returns
everything in one shot — directly solves the stated goal.
**Real cost:** each kind's fields differ (`on_fail` needs `condition`/`path`/`resolver`/`message`;
`write_grant` needs `writer`/`table_name`; `setting` needs `key`/`value`/`use`). One shared table means
either a wide, mostly-null column set, or a JSON blob for "the rest," which loses the exact-column
type-checking `configmaint.validate`'s coherence checks currently rely on (e.g. checking `cfg_on_fail.path`
is a real enum value is a clean single-column check today; inside a JSON blob it's not).

**Option 2 — add a `module` column to each existing typed table, and build a per-module completeness
report/view that unions across them.** Same end result (one list per module) via a query or a new
`configmaint` report section, e.g. "## Module: passage" listing its settings, grants, on_fail rules, and
which of the 6 rule-sextet categories are present — literally the table in §2, generated instead of
hand-built. Keeps every table's own proper typed columns; `configmaint.validate`'s existing per-kind
checks don't change at all — they'd just gain a `module` filter.

**My recommendation is Option 2** — it solves the actual problem (a single, complete, comparable view per
module) without giving up the typing that makes `validate()`'s coherence checks precise, and it's a much
smaller change (one column added to ~4 existing tables + a new report/query, vs. collapsing five
differently-shaped tables into one). But this is a real architecture call and you may have reasons to
prefer a single unified store regardless (e.g. if you expect to query/edit configs by module far more
often than by kind) — which do you want built?
