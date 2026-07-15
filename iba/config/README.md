# Configuration seed — Inner Being Analysis Programme application

> This folder is the **human-editable JSON seed** for the application's configurator. At build time a loader
> **self-validates** these files and writes them into the new DB, which is **authoritative at runtime**.
> The JSON is the input; the DB is the source of truth. Git is the change history.
> Design reference: the plan `C:\Users\lerouxc\.claude\plans\moonlit-launching-cocke.md` — Appendix A (configurator),
> Appendix C (content inventory). *(App folder name `iba/` is provisional.)*

## The rule envelope (every item)

Every configuration item is a **rule** with a fixed anatomy (plan A.10). Common envelope + a kind-specific `spec`:

| field | meaning |
|---|---|
| `id` | stable unique id (dotted, e.g. `dim.116.locus`) |
| `governs` | the process(es) it governs — `registry · fetch · raw · verses-passages · lexicon · characteristics · findings` |
| `kind` | `enum · dimension · ledger · gate · module · dependency · principle · pattern · setting · provenance · guardrail` |
| `status` | `LIVE · LEGACY · RECONCILE` (RECONCILE = value contested; see `reconciliations.json`) |
| `version` | integer, bumped on change |
| `authority` | the decision/document it derives from (rule provenance) |
| `reference` | doc §/`[current]` pointer where it is stated |
| `intent` | what it means / why it exists |
| `satisfaction` | the pass condition — when data/process complies |
| `validation` | how enforced: `{ "axis": "C"|"I", "check": "...", "severity": "red"|"amber" }` |
| `spec` | kind-specific body (the loader validates each kind against its own spec-schema) |

## The section files

| file | section | notes |
|---|---|---|
| `enums.json` | controlled vocabularies | live lexical enums first; status/flag vocabularies later |
| `dimensions.json` | ve_nr 101–118 | shape · pair-direction · mandatory · derivability |
| `ledgers.json` | genre × role mandatory sets | *(pending)* |
| `gates.json` | validation gates & measures | *(pending)* |
| `pipeline.json` | modules · order · dependencies · module-gates | *(pending)* |
| `screen-role.json` · `read-quality.json` · `principles.json` · `provenance.json` | study rules | *(pending)* |
| `patterns.json` · `governance.json` · `settings.json` | ops & governance | *(pending)* |
| `reconciliations.json` | canonical-value decisions + LIVE/LEGACY | the C.13 open decisions |
| `process-index.json` | by-process rule-set index | references rule ids |
| `_manifest.json` | config version + files | |

## Status discipline

- **LIVE** — the current, authoritative rule.
- **LEGACY** — a superseded rule kept for provenance (marked, not deleted).
- **RECONCILE** — the same concept has divergent definitions across sources; the canonical value is **not yet decided** (a researcher decision, tracked in `reconciliations.json`). The loader will refuse to run study modules on a RECONCILE rule until it is resolved.
