# IBA configurator — file layout and the schema boundary (v1)

> **Status: PROPOSAL for researcher review.** Restructures the flat, kind-organised file layout of plan `moonlit-launching-cocke.md` §A.12 to the researcher's two-tier grouping (2026-07-15), and fixes the boundary between the DB schema and the IBA configurator. **No config files have been moved** — this is the design to agree first.
>
> Authority: researcher le Roux Cilliers, 2026-07-15. Supersedes the A.12 `File layout` block only; the rule envelope (A.10) and the configurator's principles (A.1–A.7) are unaffected.

## 1. The two configurators, and the line between them

The researcher's framing: **the database schema is itself a configurator.** There are therefore two, and they must not overlap.

| | **DB schema** (`Appendix B` → `schema-design.md`) | **IBA configurator** (`iba/config/`) |
|---|---|---|
| owns | tables · columns · types · keys · FKs · indexes · layer separation · migrations | the domains those columns may hold · how values are produced and checked · which process touches what, in what order, under which gates |
| answers | **what structures exist** | **what the data means and how it operates together** |

**The test.** *If the DB were dropped and rebuilt from the schema document alone, would the fact survive?* Yes → schema. If the fact only matters once data flows → configurator.

**The rule.** The configurator **never redefines the schema**. It may *point at* a schema object (`ve_lexical.pair_kind`, `verse.genre`) as the home of a fact it governs; it may not declare that object's existence, type, or structure.

### 1.1 The consequence that matters

If enums are the one home for controlled vocabularies, then **the schema must not carry independent CHECK constraints on config-governed domains.** A `CHECK (role IN (...))` written by hand in the schema is a *second definition* of `enum.role` — the precise defect this register exists to end, re-imported through the back door.

Two permissible resolutions (researcher decision, → `open.check-constraints`):

- **A — schema stays silent**: config gates enforce every domain. Simple; the DB alone won't reject bad data.
- **B — schema is generated**: CHECK constraints are emitted *from* config at migration time. Stronger (the DB enforces too), and still one home, because the config remains the source.

This is not a new problem — it is `recon.vocab-home` (C.13 #6, four competing stores) meeting the schema boundary. **The boundary rule resolves most of it**: the REF doc, `wa_vocab_*`, and synced patch copies all lose their claim; only the SQL-CHECK store needs this ruling.

### 1.2 Where `db governance` sits

`db-governance` (IBA-wide) is the **bridge**: it holds how the DB is *operated*, not what it contains — the four data layers, raw immutability, provenance columns, soft-delete discipline, replayable-patch discipline, the integrity invariants, field-authority. This is exactly the configurator's side of the boundary and is why the researcher's grouping needs it as a distinct section.

⚠ **Grey zone — integrity invariants (I1–I13).** The plan says the candidate⇒verse-record invariant and FK integrity are enforced "by the schema + gates" — *both*. Proposed split: where an invariant is expressible as a schema constraint it is **declared** in the schema and **not restated** here; where it is not (multi-table, conditional, arithmetic), it is a gate in `db-governance`. → `open.invariant-split`.

## 2. The layout

### 2.1 Tier A — IBA-wide

Rules that are not owned by any one process.

| file | holds |
|---|---|
| `enums.json` | **the whole controlled-vocabulary register.** Wide even though most individual enums govern one process: the register is one lookup table, and `governs` says where each is used. |
| `pipeline.json` | overall pipeline — modules, order, the dependency graph, module-gates |
| `process-index.json` | the by-process index (⚠ see `open.index-derived`) |
| `patterns.json` | naming / label / patch / versioning **rules** |
| `governance.json` | GR-* · FLAG-* · interaction protocols |
| `settings.json` | model tier · DB path · STEP · thresholds · budget caps · debug |
| `db-governance.json` | data layers · raw immutability · provenance · integrity invariants · soft-delete · replayable patches · field-authority |
| `principles.json` | the nine principles · focus-point · infer-don't-extract · convergence · STATED/INFERRED · the behavioural guardrails |
| `reconciliations.json` | the decision register (contested values) |
| `_manifest.json` | config version · the canonical rule envelope |

### 2.2 Tier B — per process

One folder per process, from the 7 `vocab.governs` values: `registry · fetch · raw · verses-passages · lexical · characteristics · findings`.

Each carries the same six facets:

| facet | holds |
|---|---|
| `process.json` | how the process works — its own rules, staging, routing, internal order |
| `entities.json` | the data it owns and how that data operates together |
| `output.json` | what it emits — projections, extracts, reports, formats |
| `validation.json` | its gates and measures |
| `naming.json` | its naming **parameters** (label prefixes, id conventions) |
| `filing.json` | its filing **parameters** (output-tree home, archiving triggers) |

```text
iba/config/
  _manifest.json
  wide/     enums · pipeline · process-index · patterns · governance
            settings · db-governance · principles · reconciliations
  process/  registry/ fetch/ raw/ verses-passages/ lexical/
            characteristics/ findings/
              └─ process · entities · output · validation · naming · filing
```

**Facet files are created on demand.** 7 × 6 = 42 possible files, many of which have no content (`fetch` has no filing rules). The manifest declares which facets are *expected* vs *authored* per process; an unauthored facet simply does not exist as a file. → `open.facet-granularity` offers the alternative.

### 2.3 The instantiation rule (prevents the obvious drift)

`patterns.json` (wide) and a process's `naming.json`/`filing.json` are the same concept at two levels — the classic two-homes trap.

> **Wide owns the RULE; a process owns only its PARAMETERS.** A process file *instantiates* a wide pattern (naming its own prefix, its own output tree). It never restates the rule. `same-name → version bump` is written once, in `patterns.json`, forever.

The same discipline applies to `principles.json` vs any process's `process.json`: the principle is wide, its process-specific application is a parameter or a gate — never a restatement.

## 3. Where the current sections land

| current / planned section | lands |
|---|---|
| `enums.json` | **wide/** — unchanged |
| `dimensions.json` | **process/lexical/entities.json** — the ve_nr dimensions *are* the lexical layer's data entities |
| `ledgers.json` | **process/lexical/** — ⚠ `process` or `validation`? → `open.ledger-home` |
| `gates.json` | **dissolves** — each gate goes to its process's `validation.json`; cross-DB invariants → `wide/db-governance.json` |
| `pipeline.json` | **wide/** — unchanged |
| `screen-role.json` | **process/characteristics/process.json** |
| `read-quality.json` | **wide/principles.json** — guardrails are behavioural and span processes |
| `provenance.json` | **wide/db-governance.json** |
| `patterns.json` · `governance.json` · `settings.json` · `process-index.json` · `reconciliations.json` | **wide/** — unchanged |

**Net:** `gates.json` dissolves into seven process `validation.json` files plus `db-governance`; `dimensions.json` becomes a process entity file; `read-quality`/`provenance` fold into wide files; `db-governance.json` is new. The four authored files move but their *content* survives intact.

## 4. What this costs

- **Authored content survives.** The rule envelope, the four metas, the 11 enums and the 18 dimensions are all layout-independent — items carry `governs` and `kind` already. This is a move, not a rewrite.
- **`_manifest.json` `sections[]` is rebuilt** — it currently lists the flat A.12 layout.
- **Two meta claims are corrected**: "kind and section are 1:1" (no longer true — kind selects the spec-schema, the folder selects the process) and `vocab.kind`'s `section` field per value.
- **`meta.open.governs-application` (manifest) is resolved by this structure**: Tier A *is* the home for rules that govern no study process. `governs` needs a wide/application value, or becomes optional for Tier A items. → folded into `open.governs-tier-a`.

## 5. Open — needs a researcher ruling

| id | question | recommendation |
|---|---|---|
| `open.check-constraints` | Schema silent (A) or CHECKs generated from config (B)? | **B** — the DB enforces too, and one home is preserved because config remains the source. Costs a generator at migration time. |
| `open.invariant-split` | Which integrity invariants are schema constraints vs `db-governance` gates? | Expressible-as-constraint → schema, declared once, not restated. The rest → gates. Needs an I1–I13 pass. |
| `open.ledger-home` | Is the genre × role mandatory ledger a `process` rule or a `validation` rule? | **`process`** — it defines what the read must *produce*; `validation` then checks it was produced. Keeps "the rule" and "the check" distinct. |
| `open.facet-granularity` | Six facet files per process (created on demand), or one file per process with six sections? | **Six files on demand** — `lexical` alone would otherwise be a very large single file; and per-facet files let the manifest track authored-vs-expected per facet. |
| `open.index-derived` | Is `process-index.json` authored, or generated from `governs`? | **Generated.** Every item already carries `governs`; an authored index is a third home that can drift from the items it indexes. Make it a loader output, not a seed file. |
| `open.governs-tier-a` | Do Tier A items carry `governs`? | Add a wide value (`application`) **and** allow `all` for genuinely cross-cutting rules (provenance). Supersedes `meta.open.governs-application`. |
| `open.id-convention` | Do ids stay kind-prefixed (`gate.*`) now that files are process-cut? | **Yes** — ids must be unique programme-wide and independent of where a rule is authored. A rule that moves file must not change id. |

## 6. Recommended order

The researcher's own build order (plan §2.3) is *framework before modules*, and the same logic applies here: **agree the layout before authoring into it.** Concretely:

1. **Rule §1's boundary + §5's opens** — these decide the shape.
2. **Restructure the four authored files** into the layout (mechanical; content survives).
3. **Rule the 8 reconciliations** — still the critical path; `recon.mandatory-ledger` blocks `lexical/` regardless of layout.
4. **Then author outward**, wide-first (`db-governance` and `patterns` set the discipline every process file instantiates).

⚠ **Order note:** the enum value-shape question (`enums.json` → `meta.open.value-metadata`, bare strings vs objects) is *independent of this layout* and still gates expansion of the register. It is cheaper to settle before the register grows past its current 11 items.
