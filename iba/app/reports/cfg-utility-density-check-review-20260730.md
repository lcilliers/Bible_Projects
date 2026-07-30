# Review: `find_utility_config_density` findings (escalation #380 and the newer duplicate run)

> Generated 2026-07-30T06:23:03Z by hand (Claude Code), reviewing `escalation-list.md` before
> answering the open `configmaint.validate` escalation(s). Read-only investigation — no cfg_*
> write, no escalation answered. Covers the "low config-density utilities" category only.
>
> **Correction (2026-07-30, later same session):** the note below originally called the
> stale-governance-docs finding a "clock-skew artifact." That was wrong, and was reached without
> actually checking `cfg_change_detail` — the real cause: GOVERNANCE.md §28 was written right
> after escalation #384 (`report-stop`) was applied, but escalation #385 (`crash`) was applied
> *afterward* (`cfg_change_detail.applied_at` 2026-07-30T05:14:23Z) and §28 was never updated to
> match — it said crash was "not yet approved" when it already had been. A real content-currency
> gap, exactly what the check exists to catch. Fixed in GOVERNANCE.md §28 directly; the check
> itself was correct the whole time. See `BUILD.md` (the follow-up entry logging this correction).

## Why this needed a look before just approving/rejecting

The escalation bundles all 13 flagged modules into **one** decision (approve/reject/revise covers
the whole `low_config_density_utilities` category at once — `handlers/configmaint.py`'s `validate`
has no per-item granularity). Before answering it, I read all 14 originally-flagged files
(`cfg_utility` rows with zero `cfg.setting()`/`cfg.enum()` call sites per
`lib/cfgquality.find_utility_config_density`) to check whether the flag is actually meaningful in
each case — and found the check itself has **three distinct ways to be wrong**, not just the one
(legitimate zero vs. real gap) its own docstring already names.

## What I found, per file

| module | verdict | why |
|---|---|---|
| `cfg.py` | legitimate zero | this file **defines** `.setting()`/`.enum()` — it is the callee, not a caller. Cannot flag itself. |
| `cfgcheck.py` | legitimate zero | validates the raw seed **dict**, before any DB/Cfg object exists — structurally cannot call `.setting()`/`.enum()`. |
| `cfgload.py` | legitimate zero | **writes** the seed into the cfg_* tables (drops + recreates them) — same class as `migration/` scripts, already excluded from `find_orphan_configs` for the identical reason. |
| `cfgreport.py` | legitimate zero — **and a false negative I introduced, then fixed** | takes `out_path`/`db_path` as arguments; the *caller* (`configmaint.report`) resolves `configmaint.report_path` via `cfg.setting()`, not this module. Separately: my earlier edit today (adding the 7th finding-category description) accidentally wrote the literal substrings `cfg.setting(` / `cfg.enum(` into this file's own source as descriptive prose, which silently satisfied the check's naive text-scan and dropped `cfgreport` off the flagged list (14→13). Caught by re-diffing after the edit; reworded to avoid the collision (see `BUILD.md`, this session). |
| `db.py` | **check false negative — genuinely config-driven, the check's definition is just too narrow** | its own docstring: *"the code enforces, it does not decide"* — every table/column/dedup-key decision comes from `cfg.tables()`, `cfg.columns()`, `cfg.unique_key()`. Zero `.setting()`/`.enum()` calls, but that's because this module consumes the **schema-shape** side of `Cfg`, not the settings/enum side — a real gap in what the check counts as "usage," not a real gap in the module. |
| `dbsnapshot.py` | **check false negative — a literal pattern-matching miss** | line 84: `keep = int(c.setting("retention.snapshot_keep_count", 20))` — this **is** a real `cfg.setting()`-equivalent call, reading a real setting. Missed only because the check's substring search is hardcoded to the literal text `cfg.setting(` / `cfg.enum(` and this file binds its `Cfg` instance to a local named `c`, not `cfg`. Any other variable name defeats the check the same way. |
| `lexiconparse.py` | **real gap — the one already named** | zero reference to `Cfg`/`cfg` at all. Six regexes and a hardcoded tag-set deciding a real parse — exactly the case `find_utility_config_density`'s own docstring calls out as the actual reason this check exists. |
| `passagetrack.py` | legitimate zero | takes an already-open `cfg`/`cfg.conn` from its caller; only reads `cfg.may_write(...)` (a write-grant check, not a setting/enum). |
| `registryreport.py` | legitimate zero | same — `cfg.conn` passed in by caller, no settings/enums of its own. |
| `retention.py` | legitimate zero | same — `cfg.conn` passed in; its OWN setting (`retention.snapshot_keep_count`) is read by `dbsnapshot.py` (above), not here. |
| `schemareport.py` | legitimate zero | same pattern (`cfg.conn` from caller). |
| `seedreport.py` | legitimate zero | same pattern — already named as legitimate in the check's own docstring. |
| `spanreport.py` | legitimate zero | same pattern. |
| `strongreport.py` | legitimate zero | same pattern. |

## Bottom line

Of the 13 currently flagged: **11 are legitimate zeros** (structurally can't/needn't call
`.setting()`/`.enum()` themselves — caller resolves it, or the module IS the config layer), **1 is
a real, already-known gap** (`lexiconparse.py`), and **2 are false negatives in the check itself**
(`db.py`, `dbsnapshot.py` — both genuinely config-driven, missed by the check's own narrow
definition: literal `cfg.setting(`/`cfg.enum(` text only, hardcoded to the variable name `cfg`).

**This means the check's raw finding ("13 utility modules with zero usage") overstates the
problem roughly 13-to-1** — only one module actually lacks config it should have. Answering the
current escalation `approve`/`reject` as one bundle either (a) waves off the one real gap
(`lexiconparse.py`) along with the legitimate zeros, or (b) manufactures "needs action" busywork
for 11 modules that are already fine.

## The actual question

Two separate decisions, not one:

1. **Should `find_utility_config_density` be fixed** (broaden to other `Cfg` methods like
   `.tables()`/`.columns()`/`.on_fail()`/`.may_write()` as valid "usage," and stop hardcoding the
   variable name `cfg` — e.g. detect any `<name> = Cfg(...)` binding and check `<name>.setting(`)
   before its findings are treated as reliable? Until then, every future run of this check carries
   the same class of false negative dbsnapshot.py/db.py just exposed.
2. **What to do about `lexiconparse.py`** specifically — its six regexes/hardcoded tag-set genuinely
   look like they should be `cfg.setting()`-driven (a future tag-set change means a code edit, not
   a config change). Confirm that's wanted as a real fix, or that it's deliberately hardcoded (e.g.
   performance, or the tag-set is considered code-stable) and the escalation should just be
   dismissed for this item.

Not answering `Escalation.ps1` for run `RUN-20260730_044143_606-CONFIGMAINT` (#380) or the newer
duplicate (`RUN-20260730_061454_014-CONFIGMAINT`, raised this session) pending your call on the
above — a silent approve/reject here would either bury the one real gap or manufacture false work
for eleven files that don't need any.
