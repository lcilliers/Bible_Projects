# IBA configurator — file layout and the schema boundary (v2)

> **Status: rulings recorded 2026-07-15.** v1 (proposal) → `archive/iba-configurator-layout-v1-20260715.md`. This version records the researcher's rulings in series and carries the residual opens forward.
>
> Authority: researcher le Roux Cilliers, 2026-07-15. Supersedes plan `moonlit-launching-cocke.md` §A.12 `File layout`; the rule envelope (A.10) is amended by §1.1 below.

## 1. The two configurators — RULED

**The boundary stands** (§1 agreed): the DB schema owns *what structures exist*; the IBA configurator owns *what the data means and how it operates together*. The configurator points at schema objects, never declares them.

### 1.1 Enforcement — RULED (supersedes v1's A/B choice)

Neither "schema silent" nor "schema generated". The ruling:

> **The schema must continue to use DB technology to regulate compliance** — CHECK constraints, FK definitions, indexing, required/NOT NULL. **But DB controls are subservient to the data-definition requirements, which are defined in the IBA configurator.** A change to the configurator *may trigger a DB change requirement*; effecting that is a function of the **configurator-maintenance utility**. The configurator carries **a node signalling that a particular control is governed by a DB constraint**.

Consequences:

1. **`validation.enforcement` is added to the envelope** — declares *where* the control is enforced (`db:check` · `db:fk` · `db:not-null` · `db:index` · `gate` · `db+gate`). This is the signalling node.
2. **One home is preserved.** A DB CHECK is not a second definition — it is a *projection* of the config rule, emitted and maintained by the utility. The config remains the source; the DB is a downstream enforcer.
3. **`recon.vocab-home` (C.13 #6) is substantially resolved**: the REF doc, `wa_vocab_*` and synced patch copies all lose their claim; the SQL-CHECK store survives *as a projection, not a definition*. The residue for that reconciliation is narrowed to seeding member values from the live DB.
4. **A config change is a schema-change trigger.** The maintenance utility must diff config against the live schema and raise the required migration — never a hand-applied one (plan 3.4.2 "no implicit supersession").

### 1.2 db-governance — RULED

Agreed as a Tier A section. **The "grey zone" is dismissed:**

> It is not grey. The IBA configurator sets the rule. If the rule is used in the DB, then the rule governing the configurator-maintenance utility — itself an IBA-wide configuration — triggers an update of the schema.

So `open.invariant-split` is **closed, not split**: there is no negotiation over which invariants belong to schema vs config. **All rules are config.** Those expressible in DB technology are marked `enforcement: db:*` and propagated by the utility. The invariant set (I1–I13) is authored once, in `db-governance`, with each invariant declaring its enforcement location.

## 2. The layout — RULED

### 2.1 Tier A — IBA-wide

**Definition of Tier A (ruled):** *the same rule applies in all situations* — even if in practice it is only used in some places. Universality is the criterion; breadth of use is not. `governs` still records where it is actually used (see §5).

| file | holds | change |
|---|---|---|
| `enums.json` | the controlled-vocabulary register — **definitional only** (see §3) | stripped |
| `pipeline.json` | modules · order · dependency graph · module-gates | |
| `patterns.json` | naming / label / patch / versioning rules | |
| `governance.json` | GR-* · FLAG-* · interaction protocols | |
| `settings.json` | model tier · DB path · STEP · thresholds · budget caps · debug | |
| `db-governance.json` | data layers · raw immutability · provenance · I1–I13 · soft-delete · replayable patches · field-authority | new |
| `principles.json` | the nine principles · focus-point · infer-don't-extract · convergence · STATED/INFERRED · behavioural guardrails | |
| `filing.json` | **filing · folders · file-manifest maintenance · the process index** | new (§2.1, §5) |
| `git.json` | git usage | new (§2.1) |
| `reconciliations.json` | the decision register | |
| `_manifest.json` | config version · the rule envelope | |

`process-index.json` **is deleted as a standalone file** — it is part of the file/folder configuration (`filing.json`), backed by a utility that documents and indexes the processes (§5).

### 2.1a Tier A — utilities (new)

> **Add a json for each IBA utility** (e.g. configuration maintenance, process run utility, discovery utility, etc.).

Utilities are a distinct population from processes: a process transforms study data; a utility provides a capability. Candidate set, from plan 3.3.1/3.3.3 (**to confirm** → `open.utility-set`):

`config-maintenance` · `run` (orchestrator + run manager + interface) · `discovery` · `db` · `step` · `morphology` · `validation` · `api` (Claude adapter) · `git` · `filing` · `auth`

⚠ **`git.json` and `filing.json` appear in both lists.** Under §2.3 (one rule, one home) they cannot exist twice. Proposed: they are **utility files**, and the wide list points at them — the git rules *are* the git utility's configuration; the filing rules *are* the filing utility's. → `open.utility-vs-wide`.

### 2.2 Tier B — per process — RULED

**Seven files, one per process, facets as nodes** (not 42 facet files):

`registry · fetch · raw · verses-passages · lexical · characteristics · findings`

Nodes in each: `process` · `entities` · `output` · `validation` · `naming` · `filing`.

> **"When the jsons are all consolidated into the DB, then these will all become one table (perhaps)."**

This is the load-bearing observation. **The file layout is authoring ergonomics, not architecture.** At runtime every rule is a row carrying `kind` + `governs`, queryable on both axes regardless of which file authored it. It also supports the rule-centric schema of A.10 (one `cfg_rule` core + kind-specific sub-tables) over the table-per-kind sketch of A.3. → `open.rule-table`.

### 2.3 One rule, one home — RULED (replaces v1's "instantiation rule")

> **The same rule must not be defined in multiple places. As far as possible, the entire rule for an entity must be defined in one place.**

v1 proposed splitting a rule across tiers (wide owns the rule, process owns the parameter). **That is withdrawn** — it *is* a rule in two places. The corrected rule:

- **A rule is atomic.** It has exactly one home and is defined there *in full*.
- **Cross-reference by id; never restate, never extend.** A process rule may cite `pattern.version-bump`; it may not paraphrase, qualify, or partially override it.
- **Home is decided by the entity, not the tier.** "Where lexical outputs are filed" is a rule about the lexical entity → the lexical file, entire. "Same-name → version bump" is a rule about naming as such → `patterns.json`, entire.

⚠ This leaves a real ambiguity between wide `filing.json`/`patterns.json` and the per-process `naming`/`filing` nodes — the exact seam where drift starts. → `open.filing-seam`.

## 3. Enums are definitional — RULED

> **Enums define the item, its options, and where it is used. How it is applied is process configuration.**

The authored `enums.json` violates this. To be stripped out and repurposed:

| currently in enums.json | verdict | goes to |
|---|---|---|
| `validation` block (`check: value-in-domain`, `severity: red`) | **application** — the domain *check* is a gate belonging to the field's process | that process's `validation` node, citing the enum id |
| `spec.default` (device → `literal`) | **application** — "write `literal` when the read finds nothing" is a read rule | `lexical.process` |
| `spec.rule` (resolution: `none` ≠ `unknown`, never conflate) | **application** | `lexical.process` |
| `spec.note` (type: the faculty-ontology data failed; locus: the Ps 1-25 blanket convention) | **data-state provenance**, not vocabulary | the scoreboard / `db-governance` provenance |
| `spec.values` · `canonical` · `variants` · `alias_map` · `labels` | **definitional — stays** | |

**Residual shape of an enum item:** `id · governs · kind · status · version · authority · reference · intent · spec{values, canonical, reconcile?, variants?, alias_map?}` — no `validation`, no `default`, no `rule`.

⚠ **This forces an envelope change:** `validation` is currently *required* on every item, and a definitional item has none. → `open.definitional-kinds`.

### 3.1 The question this raises — does it extend to dimensions?

The principle is not about enums; it is about **definitional vs enforcement rules**. `dimensions.json` has the same conflation, and worse: every item carries a `validation` block, plus `spec.rule` (D3 driver-vs-restraint, D5 bearer≠God), `spec.default` (D117 literal) and `spec.genre_note` — all of which are *how it is applied*.

Read consistently, a dimension defines `ve_nr · label · shape · pair endpoints · mandatory · derivation · enum`, and **every check on it becomes a gate in `lexical.validation`**. That is ~18 gates created and 18 validation blocks removed.

**Recommendation: yes, it extends** — the ruling names a cause, not an instance, and leaving dimensions conflated would reintroduce it. **But the blast radius is large enough to confirm before acting.** → `open.definitional-extends`.

## 4. Where the current sections land

| section | lands |
|---|---|
| `enums.json` | wide/ — stripped to definitional |
| `dimensions.json` | `process/lexical.json` → `entities` node |
| `ledgers.json` | `process/lexical.json` → `process` node (`open.ledger-home` ruled: process) |
| `gates.json` | **dissolves** → each process's `validation` node; I1–I13 → `db-governance.json` |
| `screen-role.json` | `process/characteristics.json` → `process` node |
| `read-quality.json` | `wide/principles.json` |
| `provenance.json` | `wide/db-governance.json` |
| `process-index.json` | **deleted** → `wide/filing.json` + a utility |

## 5. §5 rulings

| id | ruling |
|---|---|
| `open.check-constraints` | **CLOSED** — see §1.1. DB enforces, subservient; config carries the enforcement node; the maintenance utility propagates. |
| `open.invariant-split` | **CLOSED** — see §1.2. No split. All rules are config; enforcement location is declared. |
| `open.ledger-home` | **CLOSED** — `process`. The ledger defines what the read must produce; validation checks it did. |
| `open.facet-granularity` | **CLOSED** — 7 files, facets as nodes. |
| `open.index-derived` | **CLOSED** — the process index is part of the file/folder configuration, with a utility that documents and indexes the processes. Not a standalone seed file. |
| `open.governs-tier-a` | **CLOSED** — Tier A items *do* carry `governs`. Tier A means *the rule applies universally*; `governs` records where it is actually used, and may name **utilities** as well as processes. `governs` therefore extends beyond the 7 study processes. |
| `open.id-convention` | **CLOSED with a caveat** — labelled ids are kept ("easier to read and use") but carry disadvantages, uniqueness among them. See `open.id-uniqueness`. |

## 6. Open — carried forward

| id | question | recommendation |
|---|---|---|
| `open.definitional-extends` | **Does §3's definitional/enforcement split extend to dimensions?** ~18 validation blocks removed, ~18 gates created. | **Yes** — the ruling names a cause. Confirm before acting; largest blast radius of the opens. |
| `open.definitional-kinds` | `validation` is a required envelope field, but definitional items have none. | Make `validation` required only for enforcement kinds (`gate`, and whatever survives on `dimension`); `not-applicable` for definitional kinds (`enum`). |
| `open.utility-vs-wide` | `git` and `filing` appear as both wide files and utilities — forbidden by §2.3. | They are **utility files**; the wide layer cites them. One home. |
| `open.utility-set` | Which utilities get a json? | The plan's 3.3.1/3.3.3 set (11 candidates, §2.1a). Confirm the list before authoring. |
| `open.filing-seam` | Wide `filing.json`/`patterns.json` vs per-process `naming`/`filing` nodes — where does one end? | Wide owns rules about *naming/filing as such*; a process owns rules about *its own entity's* outputs. Different entities, one home each. Needs a worked example to be safe. |
| `open.id-uniqueness` | Labelled ids rot when the label changes — `dim.114.reading` was relabelled from "discovery" on 2026-07-14; had the id been minted then, it would now mislead. | **Id is frozen at mint; `spec.label` is authority for display.** The label inside an id is a mnemonic, never a fact. Loader enforces global uniqueness. |
| `open.rule-table` | Does the DB hold one `cfg_rule` table (A.10 rule-centric) or table-per-kind (A.3)? | **One rule core + kind-specific sub-tables** — matches "these will all become one table" and the envelope's shape. Defer to Appendix B. |
| `open.value-metadata` | *(carried from `enums.json`)* Enum values are bare strings — no per-value description/ordinal/alias. Independent of layout; **gates expansion of the register.** | Values become objects `{value, description, ordinal?, aliases?}`. Cheapest now, at 11 items. |
| `open.check-vocabulary` · `open.axis-vs-derivation` · `open.self-hosting` · `open.legacy-scope` · `open.source-of-members` | *(carried from the file metas, unchanged)* | as filed |

## 7. Next

Per §6 of the researcher's direction: **create all the jsons with their meta section and a few example records, for evaluation.**

Blocking first, because the envelope is the shape every file inherits and reworking 20 files afterwards is the expensive order:

1. **`open.definitional-extends`** — decides whether dimensions keep their validation blocks. Changes `process/lexical.json` materially.
2. **`open.utility-set` + `open.utility-vs-wide`** — decides how many files exist.

`open.value-metadata` also still gates enum expansion, though not the meta scaffold.
