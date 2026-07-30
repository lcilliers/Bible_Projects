# `configmaint.validate` vs. the researcher's expected coverage (a-g) — gap analysis

> Requested 2026-07-29, against the researcher's stated expectations for what config-maintenance
> validation should do. Read-only. Every claim below is checked against live code
> (`handlers/configmaint.py`, `lib/cfgquality.py`, `lib/valuequality.py`, `run.py`, `lib/cfg.py`,
> `lib/stepapi.py`, `handlers/passage.py`) and/or a live query against `iba.db` — not asserted from
> memory or docs. Builds on `configmaint-validate-coverage-20260729.md` (the full 16-check
> enumeration) and the two passage config reports.

## (a) Every active config is being used in a routine

**Covered, partially, for 2 of 19 `cfg_*` tables.** The orphan check (`find_orphan_configs`) tests
only `cfg_setting` and `cfg_enum` — and even there, "used" means the key/name text co-occurs with a
`.setting()`/`.enum()` call *in source*, not that the calling code is ever actually reached.

**Not covered at all** for `cfg_column`, `cfg_report`, `cfg_report_section`, `cfg_report_csv_table`,
`cfg_write_grant`, `cfg_on_fail`, `cfg_candidate_rule`, `cfg_book_order`, `cfg_api`, `cfg_connection`,
`cfg_unique`, `cfg_status_flow` — no check asks "is this row ever consulted at runtime."

**Concrete live gap — the sharpest version of this problem isn't orphan settings, it's the
opposite: a *retired* config that's still fully live at runtime.** `lib/cfg.py:121-125`:

```python
def step(self, work_package: str, step: str) -> sqlite3.Row:
    r = self.conn.execute("SELECT * FROM cfg_step WHERE work_package=? AND step=?",
                          (work_package, step)).fetchone()
    return r
```

No `inactive` filter. `run.py:85` (`run_step`) calls this directly and dispatches to whatever
handler comes back — **`cfg_step.inactive`/`cfg_work_package.inactive` are metadata read only by
`configmaint.validate`'s own coherence report; nothing in the actual dispatch path checks them.**
This is exactly what open escalation #334 already flagged (2026-07-29, `MANUAL-20260729_122829_764060`)
— confirmed again here from a different angle.

## (b) No hardcoded logic in any method that is not config-driven

**Not covered at all.** No check anywhere scans for hardcoded logic. Concrete live examples that
would fail such a check:

- `run.py:28` — `PATH_EXIT = {"ok": 0, "report-continue": 0, "self-heal": 0, "pause-continue": 2, "report-stop": 3}` — a hardcoded Python dict mapping path→exit-code, never sourced from `cfg_enum`/`cfg_setting`, even though `enum.on_fail` already models the valid path vocabulary in config.
- `handlers/passage.py:41-44` — four `cfg.setting(key, <literal default>)` calls; one default
  (`review_over` code-side fallback = `5`) **disagrees with its own DB row's value (`10`)** —
  harmless today only because the row is inactive.
- **The validator's own definition of "what should be configured" is itself hardcoded.**
  `lib/cfgquality.py`'s `QUALITY_CHECK_REPORT_PATH`, `REPORT_STEPS`, and `MODULE_DEDICATED_TABLE`
  are Python dicts/tuples — the code says so itself ("a hardcoded list... disconnected from
  `cfg_step.inactive`" — the module's own docstring, escalation #310). The tool that checks for
  config-completeness is not itself config-driven for the one thing it's checking.

## (c) Every module routine that updates tables has the full standard config bundle (column controls, processing rules, validations, error handling/notifications, reporting)

**Not covered as a bundle at all** — only two narrow slices exist (`REPORT_STEPS`/
`QUALITY_CHECK_REPORT_PATH`, both hardcoded per (b)), and neither checks column controls or
processing-rule completeness.

**Live counts, queried directly:**

- **11 active steps have zero `cfg_on_fail` rows** — no configured error-handling/notification
  path at all: `raw.write`, `configmaint.report`, `validation.word`, `validation.book`,
  `retention.report`, `table.export`, `report.strong_meaning`, `report.span_analysis`,
  `report.schema_overview`, `report.registry`, `lexicon.parse`. If any of these fail in a way that
  returns a non-`ok` condition, `run.py` falls back to `path = "report-stop"` — a default, not a
  configured decision.
- **6 active steps that write data tables (`cfg_write_grant`) have no `cfg_report` row**:
  `configmaint.propose`, `lexicon.parse`, `lexicon.related`, `raw.validate`, `raw.write`,
  `registry.create`. Some of these may genuinely not need one — but nothing in the schema records
  *that decision*, so "doesn't need a report" and "was missed" are indistinguishable today.
- No check exists that every column a writer's `db.write`/`UPDATE` actually touches has a matching
  `cfg_column` row (the reverse direction — `cfg_column` completeness against real code — was not
  tested here but is the same shape of gap).

## (d) Every utility routine has configs that govern it, and is complete

**No mechanism exists to even enumerate "utility routines."** `cfg_step` is the only registry of
governed routines, and it only covers *steps* (things `run.py` dispatches to). Library code
(`lib/stepapi.py`, `lib/words.py`, `lib/reportkit.py`, `lib/cfgquality.py` itself, etc.) reads
`cfg.setting()` ad hoc with no equivalent of `cfg_step`/`REPORT_STEPS` to check completeness
against. There are 19 `cfg_*` tables; none is a utility registry. This expectation currently has
**no config category to be checked against at all** — it isn't a check that's weak, it's a check
that has nowhere to attach.

## (e) Configs are structurally complete, not duplicated, not conflicting

**Structural duplication is prevented by PK constraints** (a `cfg_setting.key` or
`(work_package, step)` pair literally cannot repeat). **Semantic conflict is not checked at all.**
Concrete live conflicts found by direct comparison of code-side literal defaults against their own
DB row's stored value:

| setting | code default | DB value | DB `inactive` | verdict |
|---|---|---|---|---|
| `passage.review_over` | `5` | `10` | 1 | **disagree** — masked only because inactive |
| `step.expect_min_verses` | `1` | `1000` | **0 (active)** | **disagree, live** |

`step.expect_min_verses` is the STEP-health-probe threshold (`lib/stepapi.py:69`) — the same probe
that ran at this session's `Start-Iba.ps1` startup ("2088 verses" for H0430, which clears 1000).
Today the DB value (1000) is what actually governs the probe, so it works — but if that row were
ever deleted, the probe would silently fall back to accepting as few as **1** verse, and nothing
would catch the regression: no check compares a setting's code-side fallback default against its
own stored value for drift.

## (f) Configs that refer to each other are not broken or incoherent

**Only one cross-reference is checked**: `cfg_on_fail.step` must name a known step (check #8 in
the coverage report). Queried live against every other cross-reference:

- `cfg_write_grant.writer` — **never validated against `cfg_step`.** Of 13 distinct active
  writers, 6 (`call1_meanings`, `call2_getInfo`, `call3_strong`, `escalation`, `migration`, `run`)
  are not `cfg_step` rows at all — by convention these are special internal writer-identities, not
  steps, which is fine — but the validator cannot tell "intentional non-step writer" from "typo/
  orphan reference," because it checks nothing here.
- `cfg_column.filled_by` — **never validated against `cfg_step.inactive`.** This is precisely the
  passage-table finding: `passage.rule`/`passage.source`/etc. all declare `filled_by:
  'passage.build'`, a step that is `inactive=1` and never runs. Nothing flags the contradiction.
- `cfg_report_section.step` / `cfg_report_csv_table.step` — checked live here (not by the
  validator): all values **do** resolve to real steps. Clean today, but only incidentally — no
  standing check enforces it.

## (g) The config text is actually active — changing it would change processing

**Not checked at all**, and this is the hardest category to check mechanically (it requires either
a semantic read of code, or literally mutating a value and re-running to observe a behavior
difference). Two live illustrations of exactly why this matters:

- `step.expect_min_verses` (above) — today the DB value genuinely drives the probe threshold, so
  changing it *would* change processing. But this is true by luck of current wiring, not by any
  verified guarantee — see (e).
- `passage.cross_chapter` — the code's own comment (`handlers/passage.py:70-77`) states the
  setting *is* read and folded into a boolean, but **also states outright that a true
  chapter-boundary crossing "still can't be recognised here even with cross_chapter=True"** because
  "adjacent" is computed purely from verse numbers, which reset each chapter. This is a
  self-documented case of a config whose text ("passages do not cross a chapter boundary") promises
  more than changing its value can actually deliver — it's read, so it isn't an *orphan* by the
  current check's definition, but it is not fully *live* either.

## Summary

| requirement | current coverage |
|---|---|
| (a) active config used in a routine | 2 of 19 tables checked, and only by source co-occurrence — the sharper live risk (inactive step still dispatchable) is unchecked |
| (b) no hardcoded non-config logic | not checked; found in `run.py`, `passage.py`, and the validator's own hardcoded completeness lists |
| (c) full standard config bundle per table-writing routine | not checked as a bundle; 11 active steps have no error-handling config, 6 have no report config |
| (d) utility routines fully governed | no registry of utility routines exists to check against |
| (e) structurally complete / no conflicts | DB prevents literal duplicates; semantic conflicts (code default vs. DB value) not checked — 2 found live, one active |
| (f) cross-references coherent | 1 of at least 4 cross-reference types checked (`on_fail.step`); `write_grant.writer` and `column.filled_by` unchecked, the latter is the exact passage-table defect |
| (g) config text is behaviourally live | not checked at all; one illustration where it holds by luck, one self-documented case where it demonstrably doesn't fully hold |

Every one of the seven expectations names a real, currently-unfilled gap — not a matter of
adjusting an existing check's threshold, but categories of check that don't exist yet. No fix
proposed here; this is the assessment requested before any design decision.
