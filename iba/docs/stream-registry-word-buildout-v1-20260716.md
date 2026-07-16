# The registry-word build-out stream — narrated through the configs

> **v1 · 2026-07-16.** Walks the researcher's run, hop by hop, through every config that
> governs it — and records what each hop needs that the config does not have.
>
> **The run, as the researcher describes it:**
>
> ```
> PS run → update registry word → pipeline (get all the modules involved)
>        → raw → STEP → validate all DB tables
>        → base → validate cluster
>        → registry → sign off
> ```
>
> **It starts and ends at registry.** That is not a detail — the pipeline's dependencies are
> linear (`registry → raw → base`), and this run is a **loop**. Nothing in the config expresses
> the return leg.
>
> Config state as narrated: `config_version` **0.1.7** · 138 LIVE · 91 INACTIVE (parked) ·
> 16 RECONCILE.

---

## Hop 0 — PS run

**What happens:** the researcher invokes a run from PowerShell with parameters — which word,
which entry point, what scope.

**What governs it:** `util.run` → **`run.json` is PENDING. It does not exist.**

The only two items mentioning `util.run` are borrowed from the config-maintenance utility:
`cfgmaint.version-pinning` (a run pins to a config version) and
`gate.cfgmaint.no-reconcile-in-scope` (a run refuses to start on a contested rule).

### ✗ MISSING — Hop 0

| # | missing | why it bites |
|---|---|---|
| M1 | **the run entity** | nothing declares what a run IS: its id, its scope, its params, its config pin, its outcome. `cfgmaint.version-pinning` says a run pins to a config version — there is no run to pin |
| M2 | **the parameter set** | the researcher's design is "the PS Run call will set a parameter for using a specific API, that will trigger the API, and the output, and what to do with the output". No component declares any parameter, for any entry point |
| M3 | **the entry points** | two are described — (a) via `module.registry` when a new/revised word is entered, (b) direct PS call for a single term or all related terms. Neither is declared anywhere |
| M4 | **the run record / audit** | `engine_run_log`, `word_run_state` and `term_fetch_log` exist in the live DB. No entity declares them |

---

## Hop 1 — update registry word

**What happens:** an English word is entered or revised.

**What governs it:** `process/registry.json` · `module.registry` (scope `registry`) ·
3 LIVE steps — `create-new-item → update-tables → validate`.

**`ent.registry.word`** — one row per English word, holding *the word · **its terms (via
Strong's)** · source_list/origin · the reason it was registered · status*.

**Rules:** `registry.definition` (the entry point) · `registry.is-scaffolding` (red guardrail —
the word list is not the study's object) · `registry.path` (every characteristic traces back to
a registered term) · `registry.growth` — **RECONCILE**.

### ✗ MISSING — Hop 1

| # | missing | why it bites |
|---|---|---|
| M5 | **★ the TERM as an entity** | the term is a *property* of the word here ("its terms (via Strong's)"). The code has a rich term model — `mti_terms`, `wa_term_inventory`, `wa_term_related_words`, `wa_term_root_family` — and the config has none of it. **The cluster edge and all the meaning data hang off the term, not the word.** Nothing in this stream can be wired until the term is a declared thing |
| M6 | **the word ↔ term association** | one Strong's can serve more than one word — the live DB carries ~5,500 OWNER + ~1,500 XREF for exactly this. A term-as-property cannot express it |
| M7 | **the "new word in analysis" path** | the researcher: *"the term identified will either be added to an existing word term group, or a new word is created."* `registry.growth` is RECONCILE and `step.registry.gap-scan` is RECONCILE. `gap-scan` surfaces candidates; **nothing routes them** to existing-word vs new-word |

---

## Hop 2 — pipeline: get all the modules involved

**What happens:** the pipeline resolves which modules this run needs, and in what order.

**What governs it:** `wide/pipeline.json`. Three LIVE modules with ordinals and scopes:

```
0. module.registry   scope: registry
1. module.raw        scope: term | book
2. module.base       scope: book
```

Two dependencies, **both `activation: auto`**:
`dep.raw-needs-registry` · `dep.base-needs-raw`.

### ✗ MISSING — Hop 2

| # | missing | why it bites |
|---|---|---|
| M8 | **★ module resolution** | *"get all the modules involved"* has no method. Modules carry `ordinal` and `scope`; **nothing maps a run request to a module set.** "New word" vs "single term" vs "all related terms" must select different modules and different steps — the config cannot express which |
| M9 | **★ the return leg** | dependencies are one-directional (`base ← raw ← registry`). This run **ends at registry**. No dependency says registry's signoff depends on base's clustering |
| M10 | **the handler contract** | **all 40 steps declare `handler: null`.** Nothing states what a handler is, what it receives, or what it returns. This is the single thing blocking "build the scripts" |
| M11 | **scope reconciliation** | registry is word-scoped · raw is term\|book · base is book · cluster assignment is term-collection. A run for one word touches all four. Nothing declares how a word-scoped run drives a book-scoped module |

---

## Hop 3 — raw

**What happens:** from the word, discover all terms; fetch every verse for each term; add all
term-based meaning data.

**What governs it:** `process/raw.json` · `module.raw` · 7 LIVE steps — exactly the researcher's
sentence:

| | step | does |
|---|---|---|
| 1 | `get-strongs-by-word` | word → Strong's |
| 2 | `get-term-by-strongs` | the term **and its meaning** — gloss, sub-glosses, definition |
| 3 | `get-related-terms` | related words + root family |
| 4 | `get-verses` | every verse where the original-language word occurs |
| 5 | `get-morphology` | the interlinear per verse |
| 6 | `update-tables` | write verse · morphology · lexicon |
| 7 | `validate` | parity, completeness, no-null, FK |

**Entities:** `ent.raw.verse` · `ent.raw.verse-morphology` · `ent.raw.lexicon`.

**Rules that work:** `raw.immutable` · `raw.source-is-step` (every row names which API produced
it) · `raw.step-precedence` (a re-pull is a *validation event*) · `raw.no-duplication` ·
`raw.include-related` (default off) · `raw.omission-is-recorded-not-assumed`.

### ✗ MISSING / WRONG — Hop 3

| # | issue | why it bites |
|---|---|---|
| M12 | **★ `ent.raw.lexicon` holds only `["gloss", "sub-glosses"]`** | the researcher: *"all the term based meaning data is added to the DB"*. No `mediumDef`, no LSJ, no Mounce declared. **Measured consequence: `wa_term_inventory.meaning` is EMPTY on 7,052 of 7,131 live terms (99%)** while STEP returns it on request. The definition is neither declared nor stored |
| M13 | **no meaning-extraction step** | `wa_meaning_parsed` / `wa_meaning_sense` / `wa_meaning_stem` / `wa_lsj_parsed` exist and are written by `engine/meaning_parser.py`. **No step, no entity, no rule.** The sub-gloss is D101's sense authority and its parse is undeclared |
| M14 | **step 1 cites a FORBIDDEN method** | `get-strongs-by-word` names `get_strongs_for_word` = `masterSearch.**text**`. step.json gives that route `may_source: []` and `check.step.api-fit` makes it **red**. The code actually uses `meanings=`. The pipeline names a method that is both wrong and prohibited |
| M15 | **step 5 has the wrong unit** | `get-morphology` cites `_apply_ingest_verse_morphology.py` — a **canon-wide** bulk ingest of all 25,634 verses. `module.raw` is term\|book scoped. A per-term run cannot invoke a whole-canon ingest |
| M16 | **no term/related-term entity** | steps 2 and 3 produce terms and related terms. `wa_term_related_words` and `wa_term_root_family` receive them. No entity declares either |

---

## Hop 4 — STEP

**What happens:** the actual calls.

**What governs it:** `utility/step.json` — connection (localhost, ESV_th, 30s), five verbatim
routes, the 60-cap, the forward-walk, and four checks. Implemented by
`scripts/analytics/step_client.py`, which takes all of it from the config and reads nothing from
the environment.

**Gates:** `mgate.raw-pre-available → check.step.up` (up **and tagged**, else halt and warn) ·
`mgate.raw-post-oracle → check.step.cap-exhausted` (rows == STEP's reported total).

### ✗ MISSING / WRONG — Hop 4

| # | issue | why it bites |
|---|---|---|
| M17 | **`bible.getBibleText` is declared NOT IMPLEMENTED — and that is false** | it built the entire 325,507-row `verse_morphology` layer via `_apply_ingest_verse_morphology.py:32`. It is the **no-cap** route and step 5 depends on it. **The config denies the existence of a route in production use** |
| M18 | **step.json's checks carry no envelope** | stripped to `id/when/severity/on_fail`. They have **no `status`** — so `mgate.raw-pre-available` and `mgate.raw-post-oracle` point at statusless items |
| M19 | **step.json is missing meta / script / output nodes** | no `out.step.fetch-log` (→ `term_fetch_log`), no pull artefact declaration (`research/discovery/{word}_step_data_{date}.json`, 278 exist) |
| M20 | **`include_related` is misfiled in step.json** | it is a *what to fetch* decision → belongs to `config.raw` (which already declares `raw.include-related` — so it is declared **twice**) |

---

## Hop 5 — validate all DB tables

**What happens:** after raw writes, prove the DB is sound.

**What governs it:** `util.validation` → **`validation.json` is PENDING.**
`util.db` → **`db.json` is PENDING.**
And **I parked `module.validation` and its three steps** on 2026-07-16 — a mis-park: it governs
`util.validation`, which fell outside the mechanical stream filter, but the researcher's sequence
needs it at exactly this hop. `module.validation`'s own spec calls it *"BOTH a standalone module
AND the gate every other module calls."*

What exists instead: per-entity gates in raw — `gate.raw.no-null`, `gate.raw.fk-integrity`,
`gate.raw.strongs-format`, `gate.raw.completeness`, `gate.raw.immutability`.

### ✗ MISSING — Hop 5

| # | missing | why it bites |
|---|---|---|
| M21 | **★ the DB validation utility** | `db.json` PENDING. No declared DB access layer — connection, transaction, backup |
| M22 | **★ the validation utility** | `validation.json` PENDING. The gate battery every module calls is undeclared |
| M23 | **"validate all DB tables" as a step** | raw's gates are **per entity**. A whole-DB table validation after raw is not declared. `gate.dbschema.counts-match` exists but is INACTIVE and scoped to the register |
| M24 | **UNPARK `module.validation`** | my error, listed here so it is not lost |

---

## Hop 6 — base

**What happens:** derive the span master, the seed, the passages.

**What governs it:** `process/base.json` · `module.base` (scope `book`) · LIVE steps
`build-span-master` (1) → `build-char-seed` (3) → `build-passages` (4) → `update-tables` (5) →
`validate` (6) → `review-pack` (7) → `assign-cluster` (9). Ordinals 2 (stem-master) and
8 (signoff) are RECONCILE.

`base.definition` was corrected 2026-07-16: base **judges under a stated rule**, and is
regenerable *because* the rules are documented.

### ✗ MISSING / WRONG — Hop 6

| # | issue | why it bites |
|---|---|---|
| M25 | **`mgate.base-post-candidate → gate.char.candidate-verse-record` is now INACTIVE** | my park. It governs `characteristics` but it **guards base**. It is the *"a char_candidate span with no verse-record = DB integrity violation"* invariant. A LIVE module gate now points at a parked target |
| M26 | **`step.base.build-stem-master` is RECONCILE** | `open.base.stem-master-shape` — no stem-master table exists; persisted vs derived undecided |
| M27 | **base is book-scoped; this run is word-scoped** | see M11. A word's terms scatter across books |

---

## Hop 7 — validate cluster

**What happens:** every term of the word is in an analysis group.

**What governs it:** `base.cluster-assignment` (LIVE, authored 2026-07-16) —
has-cluster? → compare against the terms in each cluster → loose relationship → assign →
**escalate to the researcher** if none fits. Axis **C**, not re-run, no API.
`ent.base.cluster` · `gate.base.cluster-assigned` (red: cluster **or** recorded escalation) ·
`step.base.assign-cluster` (scope `term-collection`).

### ✗ MISSING — Hop 7

| # | missing | why it bites |
|---|---|---|
| M28 | **★ the escalation channel** | the rule says *escalate to the researcher*. **How?** No component declares an escalation mechanism, a queue, or a record. The only precedent is a note in step.json pointing at the NAS-backup email path. An escalation with no channel is a silent drop |
| M29 | **the escalation as an entity** | `gate.base.cluster-assigned` passes on "a recorded escalation". Nothing declares what a recorded escalation IS |
| M30 | **`open.base.cluster-regenerability`** | assignment is declared not-re-run; `gate.base.regenerable` demands base reproduce exactly. Unresolved |

---

## Hop 8 — registry: sign off

**What happens:** *"the registry cannot be signed off for a word until all its terms are
connected with a cluster."*

**What governs it:** **nothing.**

`step.base.signoff` exists but is RECONCILE, is **book**-scoped, and holds **lexical** — not
registry. `dep.lexical-needs-base-signoff` is RECONCILE.

### ✗ MISSING — Hop 8

| # | missing | why it bites |
|---|---|---|
| M31 | **★ the registry signoff** | no step, no gate, no entity. The check it would read exists (`gate.base.cluster-assigned`); the signoff does not |
| M32 | **★ the signoff record** | who signed, when, against which config version, covering which word, and **what voids it**. `open.base.signoff-mechanism` recommends a hash of the covered outputs so invalidation is mechanical — undecided |
| M33 | **the registry ← base dependency** | the return leg (M9), stated as a rule |
| M34 | **word status vocabulary** | a word moves seeded → fetched → clustered → signed off. `ent.registry.word` holds `status`; **no enum declares its values** |

---

## The missing configs, consolidated

**Whole components that do not exist** (9 of 12 utilities are PENDING; these three are on the
critical path of this stream):

| component | needed at | for |
|---|---|---|
| `utility/run.json` | Hop 0 | the run, its params, its entry points, its record |
| `utility/db.json` | Hop 5 | the DB access layer |
| `utility/validation.json` | Hop 5 | the gate battery every module calls |

**Entities that do not exist:**

`ent.*.term` (M5) · word↔term association (M6) · related-term (M16) · the meaning parse (M13) ·
`ent.run.*` (M1) · the escalation (M29) · the signoff record (M32)

**Methods that do not exist:**

module resolution (M8) · the return leg (M9) · the handler contract (M10) · new-word-vs-existing
routing (M7) · whole-DB table validation (M23) · the escalation channel (M28) · the registry
signoff (M31)

**Wrong, and live:**

M14 (forbidden discovery route) · M15 + M17 (`getBibleText` — unit wrong, and denied by the
config that owns it) · M12 (lexicon entity too thin — 99% of meanings unstored) · M20
(`include_related` declared twice)

**My errors, to repair:**

M24 (`module.validation` mis-parked) · M25 (`gate.char.candidate-verse-record` mis-parked) ·
M18 (step.json checks have no status)

**The structural one, which no entry can paper over:**

M11 / M27 — **registry is word-scoped · raw is term|book · base is book · cluster assignment is
term-collection.** One run for one word crosses all four. A per-word signoff cannot be satisfied
by a per-book module completing, because a word's terms scatter across books and a book holds
terms from many words. **The unit model has to be settled before the handlers can be written.**
