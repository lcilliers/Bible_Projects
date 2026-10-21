# Configuration seed — Inner Being Analysis Programme application (DESIGNED, not yet loadable)

> **This is not the app's entry point.** To run the IBA app, start at
> [`iba/app/USER-GUIDE.md`](../app/USER-GUIDE.md). That app runs on its own **lightweight `cfg_*` DB
> config**, seeded from `iba/app/config/*.json` and loaded by `iba/app/lib/cfgload.py` — proven
> working today. This folder (`iba/config/`) is a **separate, more elaborate configurator design**
> (plan `moonlit-launching-cocke.md` Appendix A + the 2026-07-15 layout-v2 ruling): a full rule-anatomy
> model meant to eventually govern the study's interpretive stages (lexical, characteristics,
> findings). **It has no loader and writes to no DB yet** — nothing in the running app reads these
> files. Whether/how the two configurators converge is an **open, undecided question**, named in
> `iba/app/GOVERNANCE.md` §6 and tracked in
> [`iba-app-design-precedence-and-structure-v1-20260721.md`](../docs/iba-app-design-precedence-and-structure-v1-20260721.md)
> §2 item 5 / §3. Don't assume this folder is live until that convergence is actually decided.
>
> The JSON files here ARE the seed of record for this design (git is their change history), and the
> **sole write path is `iba/scripts/cfg_apply.py`** — hand-editing a section file bypasses its own
> validation and is the failure this configurator exists to prevent (see `_manifest.md` "how this
> config is maintained"). This `README.md` is prose orientation, not a seed file — it's fine to
> hand-edit.

## The rule envelope (every item)

Every configuration item is a **rule** with a fixed anatomy (plan A.10). Common envelope + a kind-specific `spec`:

| field | meaning |
|---|---|
| `id` | stable unique id, minted on first DB load not first seed appearance (dotted, e.g. `dim.116.locus`) |
| `governs` | the process(es)/utility(ies) it applies to — `all` permitted for genuinely cross-cutting rules |
| `kind` | selects the spec-schema `spec` validates against — **no longer 1:1 with a file** (layout is process-primary; see below) |
| `subject` | what the rule is about, named plainly (`bearer`, `sense`, `role`, `raw-immutability`, `seed-breadth`, …) |
| `status` | `LIVE · LEGACY · RECONCILE` (RECONCILE = value contested; see `wide/reconciliations.json`) |
| `version` | integer, bumped on every change; a run pins to the config version it used |
| `authority` | the decision/document it derives from (rule provenance) |
| `reference` | doc §/`[current]` pointer where it is stated |
| `intent` | what it means / why it exists |
| `satisfaction` | the pass condition — when data/process complies |
| `validation` | how enforced: `{ "axis": "C or I", "check": "...", "severity": "red or amber" }` — not required on purely definitional items (e.g. an enum) per the 2026-07-15 ruling; enforcement of its domain lives in a separate gate rule instead |
| `spec` | kind-specific body (the loader validates each kind against its own spec-schema) |

## The layout — two tiers (ruling: `iba/docs/iba-configurator-layout-v2-20260715.md`)

**Tier A (`wide/`)** = rules that apply the same way in every situation, plus **one file per utility**
(`utility/`). **Tier B (`process/`)** = one file per study-process stage, facets as nodes within it, not
separate files. Stage chain: `REGISTRY → RAW → BASE → [SIGNOFF] → LEXICAL → CHARACTERISTICS → FINDINGS`,
each its own file/module/`governs` value.

| dir | files (authored) | files (pending) |
|---|---|---|
| `wide/` | `enums.json` · `reconciliations.json` · `pipeline.json` | `patterns.json` · `governance.json` · `settings.json` · `db-governance.json` · `principles.json` |
| `utility/` | `config-maintenance.json` · `step.json` · `run.json` · `DBSchema_maintenance.json` | `filing.json` · `git.json` · `validation.json` · `api.json` · `db.json` · `morphology.json` · `discovery.json` · `auth.json` |
| `process/` | `registry.json` · `raw.json` · `base.json` · `lexical.json` · `characteristics.json` | `findings.json` |
| `DBSchema/` | `DBSchema.json` — **captured data**, not authored: an observation of the live app DB written by `build_dbschema.py`, no rule envelope | |
| root | `_manifest.json` — config version + the canonical envelope | |

**Don't hand-maintain a file list here** — the per-component and overall index is generated fresh from
the JSON every time it changes: **[`_manifest.md`](_manifest.md)** (overall index, envelope, open
questions) and each file's own `*.md` sibling (e.g. `process/lexical.md`). Read those for the current,
exact state; this README only orients you to where to look.

## Status discipline

Two independent axes — don't conflate them:

- **Rule `status`** (per-item, inside a file): **LIVE** — current, authoritative. **LEGACY** — superseded,
  kept for provenance. **RECONCILE** — divergent definitions across sources, canonical value **not yet
  decided** (tracked in `wide/reconciliations.json`); a loader would refuse to run study modules on a
  RECONCILE rule until resolved.
- **File `status`** (per-file, in `_manifest.json`/`_manifest.md`): **authored** vs **pending** (not yet
  written) — see the table above. Neither status implies the file is loaded anywhere; see the banner at
  the top of this document.
