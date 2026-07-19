# The new-word work package — v4

> **v4 · 2026-07-17.** Supersedes v3 (same day); v3 and the researcher's comments are kept there.
> **All the work is in this document. No config has been created or loaded.**
>
> This round: the model corrected where I had it backwards · **pre-hop / post-hop** on every hop ·
> the exists/fails cycles · **what the engine records** · the schema entries this run expects ·
> the stubs re-partitioned by the task rather than by data type.

---

## 1. The model

### 1.1 Every method answers: what is the output?

> *"every method must answer the question: what is the output — this could be a file (which then
> needs its own config rules) or DB rows (taking full CRUD into account) — it could also be
> different files at different stages, and different table updates at different points."*

So the node is **`output`**, not `records`, and it is richer than I had it:

| output kind | needs |
|---|---|
| **a file** | its own config rules — path, naming, format, when written, what supersedes it |
| **DB rows** | **full CRUD** — not just "add". What creates, what updates, what soft-deletes, what may never change |
| **staged** | different files at different stages, different tables at different points **within one method** |

**CRUD is the correction.** v3 said "add-rules". Wrong scope. `raw.immutable` already says raw is
write-once but a re-pull is the source speaking again — that is C and U with a rule between them.
`raw.no-duplication` is a U-not-C rule. Soft-delete is the D. **Every one is a different rule and
v3 collapsed them into "add".**

### 1.2 ★ The feeder is driven by the task, not by the column list — I had this backwards

> *"The feeder does not decide on what it pushes by seeing what columns it have. It defines what
> need to be pushed based on the source or the task, and then confirms the column exists, is
> coherent, is not duplicated elsewhere, is not recorded slightly different in another method."*

v3 §1.2 said the check runs "from the schema outward, asking who fills this". **That is the wrong
direction and it would design the study around the table it happens to have.**

The right direction:

```
the SOURCE or the TASK  →  says what must be pushed
                        →  then CONFIRM against the schema:
                              · the column exists
                              · it is coherent (it means what we are pushing)
                              · it is not duplicated elsewhere
                              · it is not recorded slightly differently by another method
```

The task leads. The schema receives. A column that nothing pushes to is not a gap to fill — it is
**a column with no purpose**, which is exactly what the researcher says the live DB is full of.

*The 99% empty `meaning` column re-read:* STEP's `mediumDef` **is** term meaning data, so the task
says push it. Then confirm: does a column exist? Yes — `wa_term_inventory.meaning`. Is it
coherent? Yes. Is it duplicated? **Yes — `lexicon.medium_def` holds the same thing.** Recorded
differently elsewhere? **Yes — one is base-codes-only, the other per-term.** So the failure was
never "a column nobody fed". It was **two columns for one fact, and no method owning either.**

### 1.3 Where the rule is the same, it does not live in every config

> *"Where ever the rules across the configs are the same, it should not be repeated in every
> config — it should be considered to be a IBA wide config rule, or a utility. cross referencing
> configs, and cross resolving nodes need to be thought through very carefully as it is critical
> for efficient operation."*

**Candidates surfaced by this one run:**

| shared thing | today | belongs |
|---|---|---|
| **ESV** | hard-coded `'ESV'` in the INSERT; `ESV_th` in step.json; `masterVersion: ESV` from STEP | **IBA-wide.** The version is *provenance of every verse row* — R22 |
| Strong's format | `gate.raw.strongs-format` (raw only) | IBA-wide — every layer joins on it |
| soft-delete | `delete_flagged` on ~everything | IBA-wide |
| provenance stamp | `raw.source-is-step` (raw only) | IBA-wide — every row should know where it came from |
| ISO-8601 UTC timestamps | assumed everywhere, declared nowhere; live DB has **three formats** | IBA-wide |
| the escalation path | would otherwise be restated in registry + base | **a utility** (§1.5) |

⚠ **Cross-resolution is unsolved and the researcher flags it as critical.** Today the kernel
resolves `spec.cites` and `spec.implements` — and nothing else. `gate_code` in pipeline was
dangling for a day and no check saw it. **Before more cross-references are authored, the
resolution rule needs to be decided**, or every new reference is another silent edge.

### 1.4 `on_fail` — four paths, not a severity

> *"in my view there are several types of paths rather than severity: report in engine, continue;
> pause for input, continue; report to chat, stop; self heal - take action to resolve"*

**This replaces `severity`, it does not sit beside it.** Red/amber was always an impoverished way
of saying one of these four:

| path | means | who is told | run |
|---|---|---|---|
| `report-continue` | record it in the engine and carry on | the engine log | continues |
| `pause-continue` | pause, get input, resume **at the same point** | the researcher | continues |
| `report-stop` | report and stop | the chat / the researcher | **stops** |
| `self-heal` | take a named action to resolve it | nobody, unless it fails | continues |

**Read against this run:**

| rule | path | why |
|---|---|---|
| term has no cluster | **`self-heal`** → `base.cluster-assignment` | the rule names who resolves it. This is the trigger |
| ...and no cluster fits | **`pause-continue`** → the researcher | the app tried first |
| the word already exists (add-new-word) | **`report-stop`** | 7.6 — *"if so fail, report stop"* |
| rows < STEP's reported total | **`report-stop`** | a short count must never bank |
| STEP is down | **`report-stop`** | not a slow run, a wrong one |
| a related term named but not pulled | **`report-continue`** | expected under the default; the omission is recorded |
| a STEP gap the morphology master contradicts | **`report-continue`** | a recorded STEP gap, not an absence |

Every one of those is "red" today. **The path is the information; the colour never was.**

### 1.5 Researcher interaction — two types, one hard

> *"pre-prompted yes/no, or a specific input such as a new word — this must accompany preset
> details to share to facilitate the response; and, interactive response where the result is
> derived from research or debate around a topic — this is a much more tricky one to build out,
> because the question is why is the response validated to continue."*

| type | shape | this run |
|---|---|---|
| **A · prompted** | a closed question + **the preset details that let it be answered** | *"Register 'anger'? It resolves to 14 terms, 3 already held under M02."* → yes/no · *"Which cluster for H2734?"* → a choice + why each |
| **B · interactive** | the answer emerges from research or debate | *"This term fits no cluster — should there be a new one?"* |

**Type A is buildable now.** Its whole design is the **preset details**: an interaction with no
context is a chat, and a chat does not survive the session.

**Type B is the hard one, and the researcher names why: *why is the response validated to
continue?*** Type A validates trivially — the answer is in the option set. Type B has no option
set, so nothing bounds the answer. ⚠ **Not designed. It emerges per situation.** But the
distinction must exist in the config from the start, because A and B behave differently and a
package that pauses on B may never resume.

---

## 2. The test

Eight questions — **what · where · how · when · why · who · what if · validate** — plus, per the
researcher: **every hop has a pre-hop and a post-hop. From / to.**

Pre-hop and post-hop are what make the sequence checkable: a hop's *from* must be some earlier
hop's *to*. A hop whose `from` nothing produces is unreachable; a hop whose `to` nothing consumes
is dead.

---

## 3. The hops

Package `new-word` · runs over **one word** · `-Word "anger" -Source "gap scan"`.

---

### Hop 0 — pre-flight

**from:** a researcher request · **to:** a run that may legally proceed, pinned to a config version

| | |
|---|---|
| **what** | prove the run may start; write the run record |
| **where** | the run record — ⚠ **no table designed** (live DB has `engine_run_log`, `word_run_state`, `term_fetch_log`; 7.2 says the new schema is not settled) |
| **how** | `check.step.up` · `gate.cfgmaint.no-reconcile-in-scope` |
| **when** | before any work |
| **why** | a raw process without its source is not a slow run, it is a wrong one |
| **who** | `util.run` · `util.step` · `util.config-maintenance` |
| **validate** | the run record exists and names its config version |

**Branches:**

| condition | path | to |
|---|---|---|
| STEP unreachable | `report-stop` | halt + warn the researcher |
| STEP up but **untagged** | `report-stop` | the dangerous case: it answers, with no Strong's |
| a rule in scope is RECONCILE | `report-stop` | refuse to start |
| config hash mismatch | `report-stop` | the config that ran is not the config on disk |

**Engine records:** `run_id` · work package · params · **config_version** · started_at · the
pre-flight gate results. **Before any work** — a pin written after the fact is a label.

---

### Hop 1 — registry: does the word exist?

**from:** an approved run · **to:** a decision — proceed, or stop

| | |
|---|---|
| **what** | check whether the word is already registered |
| **where** | `word_registry.word` |
| **how** | exact match, case-insensitive |
| **when** | before creating anything |
| **why** | 7.6 — *"if the run is add new word — then the check is, does it exist, if so fail, report stop"* |
| **who** | `module.registry` |
| **what if** | **it exists → `report-stop`, via the escalation config.** Not an update. **A separate run is configured for refresh-existing-word** |
| **validate** | one word, one row |

⚠ **The live registry violates this today:** 222 rows / **218 distinct** — *deadness, resentment,
transformation, vulnerability* each appear twice. The rule does not exist, so nothing stopped it.

**This is also the answer to B1.** Registry grows **through the new-word run and no other
process** (researcher). So `registry.growth` is not a contested philosophy — it is this run.

---

### Hop 2 — registry: approve the word

**from:** a word that does not exist · **to:** a researcher decision

| | |
|---|---|
| **what** | ask the researcher to approve the new word |
| **where** | the escalation request/answer |
| **how** | **type A — prompted** (§1.5), with preset details |
| **when** | before the word is created |
| **why** | 7.4 — *"the app should not add a new word without researcher approval"* |
| **who** | `util.escalation` → the researcher |
| **what if** | no → `report-stop`, run ends clean. Yes → proceed. **No answer → the package stays paused. It does not time out into a guess** |
| **validate** | the answer is recorded and survives the session |

**The preset details this question needs** — this is the design, not decoration:

- the word, and the `-Source` (why it is proposed)
- **what it will pull**: term count from `meanings=`, verse count from the oracle — *the cost of
  saying yes*
- **which of those terms the study already holds**, and under which clusters
- whether any resolves to an existing word's term group

⚠ Several of those need a **dry probe before approval** — STEP calls before the word exists.
Is that Hop 2 or an earlier Hop 1.5? **Not decided.**

---

### Hop 3 — registry: create the word

**from:** an approved word · **to:** a registry row, status `approved`

| | |
|---|---|
| **what** | create the entry |
| **where** | the registry table |
| **how** | **C** of CRUD. Researcher-supplied |
| **when** | after approval |
| **why** | the entry point — everything downstream is reachable only from here |
| **who** | `module.registry` |
| **what if** | write fails → `report-stop` |
| **validate** | the row exists and carries its trigger and reason |

**⚠ The registry CRUD methods are outstanding** (researcher) — added later. This hop names C only.

**Engine records:** the word created, by which run.

---

### Hop 4 — raw: discover the terms

**from:** a registered word · **to:** a candidate term list

| | |
|---|---|
| **what** | find the terms the word maps to |
| **where** | nothing written — discovery |
| **how** | STEP `masterSearch.meanings` — curated by meaning, **not** by ESV wording |
| **when** | first raw sub-process |
| **why** | the word is a way in; the terms are what the study holds |
| **who** | `module.raw` · `util.step` |
| **what if** | **zero terms** → `pause-continue`: a registered word that maps to nothing is a researcher question. ⚠ undeclared |
| **validate** | `check.step.api-fit` — the route may source what it is sourcing |

**W1 stands:** the step cites `get_strongs_for_word` = `masterSearch.**text**`, which `step.json`
forbids from sourcing raw. The code uses `meanings=`. **Wrong and prohibited.**

**Branch:** `-Anchors` given → discovery skipped, terms taken as supplied. ⚠ And **filter F0 never
fires** on that path, so the same term can be included via a word entry and excluded via a term
entry. Undeclared.

---

### Hop 5 — raw: expand each term's family

**from:** candidate codes · **to:** the full code set (primary · sub-glosses · relatives)

| | |
|---|---|
| **what** | find every code in the term's family |
| **where** | nothing written yet |
| **how** | `getInfo` → `relatedNos`; then **probe A–Z** for siblings; then `getInfo` + a verse-count search **per relative** |
| **when** | per candidate |
| **why** | **the sub-gloss IS the sense.** `H7307G` spirit · `H7307H` breath · `H7307I` side · `H7307J` temper |
| **who** | `module.raw` |
| **what if** | a code returns no vocab → a recorded STEP gap, `report-continue` |
| **validate** | every sibling found is a real code STEP confirms |

**★ This hop is where the cost is, and most of it is waste.** The A–Z probe costs up to 26
`getInfo` calls per term to find what `definitions[]` already lists — and `definitions[]` arrives
free on the verse call at Hop 7. Measured: `H0430` names **46** relatives; each costs a `getInfo`
+ a search.

---

### Hop 6 — raw: decide which terms to keep

**from:** the full code set · **to:** include / exclude, each with a reason

| | |
|---|---|
| **what** | filter |
| **where** | nothing written — a decision |
| **how** | F0–F5: meanings-confirmed · proper-noun · particle ceiling · section type · root confirmation |
| **when** | before any verse is fetched |
| **why** | fetching everything is a scope explosion; the registry never chose those terms |
| **who** | `module.raw` |
| **what if** | everything excluded → `pause-continue` |
| **validate** | every term carries its decision **and its reason** |

⚠ **Undeclared entirely.** F0–F5 live in `word_study_extract.py` and in no config. The
particle ceiling (1000), the proper-noun heuristic, the confirmed-root set — all code constants.
**This is a judgement layer with no rule.**

---

### Hop 7 — raw: fetch the verses · **and the backtrack**

**from:** included terms · **to:** verses with spans

| | |
|---|---|
| **what** | every verse where each term occurs |
| **where** | the verse + span tables |
| **how** | `masterSearch.strong` + forward-walk |
| **when** | per included term |
| **why** | the evidentiary floor. Gen 26:35 carries `H7307G`; the ESV never says "spirit" |
| **who** | `module.raw` · `util.step` |
| **what if** | rows < total → `report-stop`. Missing total → `report-stop` |
| **validate** | `check.step.cap-exhausted` — proof by arithmetic |

**★ THE BACKTRACK, AND IT BREAKS FOR THIS PACKAGE.**

`fetch_verses` calls `_morphology_variant_codes(conn, code)`, which reads **`verse_span_index`** —
a **base** artefact — to find which sibling codes to also pull. So:

- **raw reads base's output mid-fetch.** A layering cycle: raw → base → raw.
- **For a NEW word there are no spans yet.** The lookup returns `[code]` — the primary only —
  and **every sibling is silently dropped.** `H7307G` 194 verses; `H7307H` 137 and `H7307I` 7
  lost.

**The multi-code repair only works for terms already in the DB. This package is exactly the case
it does not cover.** That is a finding, not a design choice.

⚠ **R21 (7.5)** — the researcher expects *"a multi layered decision making tree based on how the
source STEP data is parsed into the destination data, ready for the columns"* before ruling.
Deferred to its own analysis; it decides what a "term" *is*.

---

### Hop 8 — raw: fetch the morphology

**from:** verses · **to:** the per-word interlinear

| | |
|---|---|
| **what** | every word of each verse with its Strong's and morph |
| **where** | the morphology tables (+ raw HTML kept for re-parse) |
| **how** | `bible.getBibleText` — **no cap**, by reference |
| **when** | per verse fetched |
| **why** | the linguistic source of truth |
| **who** | `module.raw` |
| **what if** | the master attests a Strong's STEP does not tag → recorded STEP gap, `report-continue` |
| **validate** | every morphology row resolves to a real verse |

**W2/W3 stand:** `step.json` says this route is "NOT IMPLEMENTED" — it built the whole 325k-row
layer. And the step cites a **canon-wide** script for a **per-word** package.

---

### Hop 9 — raw: parse the meaning

**from:** the raw definition text · **to:** structured senses

| | |
|---|---|
| **what** | turn `mediumDef` into a sense tree; `lsjDefs` into LSJ structure |
| **where** | the meaning-parse tables |
| **how** | **no STEP call** — re-reads text already pulled |
| **when** | after the term detail is held |
| **why** | D101's sense authority |
| **who** | `module.raw` |
| **what if** | no structured senses → prose-only, `report-continue` |
| **validate** | every parsed meaning names its term and its language |

⚠ **v3 missed this as a hop.** It is where the caller passes one field of four, so `language`
defaults to `"Hebrew"` **7,739 times** and every Greek sense tree was built by the Hebrew parser.
**Undeclared: no step, no entity, no rule.**

---

### Hop 10 — raw: write the tables

**from:** everything fetched · **to:** rows, and a term with no cluster

| | |
|---|---|
| **what** | write terms, relatives, meaning, verses, morphology |
| **where** | §4.3 |
| **how** | each entity's CRUD rules |
| **when** | after the fetches |
| **why** | where a term first exists |
| **who** | `module.raw` |
| **what if** | **a term's cluster rule cannot be satisfied → `self-heal` → `base.cluster-assignment`.** The trigger |
| **validate** | no-null · fk-integrity · strongs-format · immutability |

**Engine records:** rows written per table · the STEP calls made (api, query, version, rows,
reported total, cap verdict) · what was **deliberately not pulled**.

---

### Hop 11 — base: assign the cluster (called)

**from:** a term with no cluster · **to:** a term with a cluster, or an escalation

| | |
|---|---|
| **what** | put the term in an analysis group |
| **where** | the term's cluster edge |
| **how** | has one? → done. Compare against **the terms in each cluster** → loose relationship → join. None → escalate |
| **when** | called when the cluster rule cannot be satisfied |
| **why** | a term no group owns is a term the study never reads |
| **who** | `module.base`, **called by** the package |
| **what if** | no cluster fits → `pause-continue` → **type A prompted**, with the candidate clusters and why each nearly fits |
| **validate** | a cluster **or** a recorded escalation |

**Axis C. No API.** The relatedness arrived at Hop 5.

---

### Hop 12 — back to raw: validate everything

**from:** written rows · **to:** a proven raw layer

Needs `utility/validation.json` and `utility/db.json` — **both PENDING**. Raw's gates are per
entity; **a whole-DB validation is not declared.**

Per 7.2: the column↔method correlation is **a design-stage test and report, not a runtime gate** —
the new schema does not exist until every run type is defined.

---

### Hop 13 — back to registry: validate

**from:** a proven raw layer · **to:** a word ready to sign off

| | |
|---|---|
| **what** | validate the word, **including that every one of its terms has a cluster** |
| **how** | read the cluster gate for every term of the word |
| **what if** | a term has no cluster and no escalation → not ready → do not sign off |
| **validate** | ⚠ **no rule says registry validation reads the cluster gate.** The check exists; the reading does not |

---

### Hop 14 — registry: sign off

**from:** a validated word · **to:** a signed-off word

**Governed by nothing.** No step, no signoff record — who signed, when, against which config
version, over which word, **and what voids it**.

---

## 4. What must be authored

### 4.1 New components

| component | holds |
|---|---|
| **`utility/escalation.json`** | type A / type B · the preset-details rule · pause-not-fork · the channel · the request + answer entities · no-silent-drop. **Two hops of this run need it** |
| **`utility/validation.json`** | the gate battery every module calls |
| **`utility/db.json`** | the DB access layer — connection, transaction, CRUD semantics, soft-delete |
| **`wide/iba-wide.json`** ⚠ | §1.3 — ESV, Strong's format, soft-delete, provenance, timestamps. **Naming for review** |

### 4.2 The `output` node — in every component

Per method: **what is the output** — file(s) and/or DB rows, with **full CRUD**, at which stage.

### 4.3 The schema entries this run expects

Per 7.6, *"lots of the columns are completely redundant"* — so this is what **this run** needs,
not the live columns. `use` and `expectation` are the config; `fed by` is the cross-correlation.

**word** *(registry)*

| column | use | expectation | fed by |
|---|---|---|---|
| `word` | the English inner-being word; the entry point | required · **unique** (violated today: 218/222) | Hop 3 |
| `source` | why it was registered — the growth trigger | required | Hop 3, from `-Source` |
| `status` | where the word is in its build-out | required · `enum.word_status` — **does not exist** | Hops 3, 14 |
| `approved_by` / `approved_at` | the researcher's approval | required before create | Hop 2 |
| `signed_off_by` / `_at` / `_config_version` | the signoff, and what voids it | — | Hop 14 |

**term**

| column | use | expectation | fed by |
|---|---|---|---|
| `strongs` | the term's identity | required · zero-padded 4-digit · `[HG]\d{4}[A-Z]?` | Hop 5 |
| `owning_word` | which word owns it | required · **⚠ one Strong's can serve several words** | Hop 10 |
| `gloss` | the term's short sense | required · STEP `stepGloss` | Hop 5 |
| `script_form` | **the actual Hebrew/Greek word** | required · STEP `accentedUnicode` / `matchingForm` — **no column exists today** | Hop 5 |
| `transliteration` | a reading aid | required · never shown without the gloss | Hop 5 |
| `meaning` | **the definition** | **required** · STEP `mediumDef` · ⚠ duplicated by `lexicon.medium_def` — **one must own it** | Hop 5 |
| `lsj_entry` | LSJ text (Greek) | Greek only · STEP `lsjDefs` | Hop 5 |
| `short_def_mounce` | Mounce (Greek) | Greek only | Hop 5 |
| `occurrence_count` | corpus frequency | **⚠ capped at 10000 by STEP — not exact.** The expectation must say so | Hop 5 |
| `cluster` | the analysis group | **required** · `self-heal` → Hop 11 | Hop 11 |
| `is_sense_of` | the base code this is a sub-gloss of | ⚠ **R21 decides this** | Hop 5 |
| `source_api` | which STEP route produced it | required — "it came from STEP" is not an answer | Hop 5 |
| `step_version` | **provenance** — which module the text is from | required · IBA-wide (§1.3) | Hop 5 |

**verse · span · morphology · meaning-parse · cluster edge · escalation · run** — same shape;
deferred until R21 settles what a term is, since the span's identity depends on it.

### 4.4 Entities

term · word↔term · related-term · root-family · meaning-parse · escalation request · escalation
answer · signoff record · run record

### 4.5 Enums

`enum.word_status` · `enum.on_fail` (report-continue · pause-continue · report-stop · self-heal) ·
`enum.escalation_type` (prompted · interactive) · `enum.escalation_state`

### 4.6 Envelope

**`on_fail` replaces `severity`** (§1.4) — `{path, resolves_by, defined_in}`.

---

## 5. Blocked

| # | blocker | state |
|---|---|---|
| ~~B1~~ | ~~registry.growth RECONCILE~~ | **RESOLVED** — registry grows through the new-word run and no other process |
| ~~R5~~ | ~~duplicate words~~ | **RESOLVED** — exists → `report-stop`; a separate refresh run |
| B2 | the handler contract | given a word here; the rest as we go |
| B3 | **resumability** | `pause-continue` requires it. `run.json` has no concept of it |
| B4 | **R21 — the multi-code fork** | needs its own layered analysis (7.5). **It decides what a term is**, so §4.3's span rows wait on it |
| B5 | **cross-resolution** (§1.3) | the kernel resolves `cites`/`implements` only. Every new cross-reference is another silent edge until the rule is decided |

---

## 6. Stubs — partitioned by the task

> *"the stubs must not dictate the flow of the task, the task must dictate the partitioning."*

v3 partitioned by **data type** — `get_terms · get_verses · get_morphology`. That is the file
layout deciding the flow. **The actual task, read out of the code:**

```
discover      meanings=            → candidate codes
expand        getInfo + A–Z probe  → the family        ← iterative: fetch, parse, fetch more
enrich        getInfo per code     → full vocab
decide        F0–F5                → include/exclude   ← no fetch
fetch verses  masterSearch.strong  → verses + spans
BACKTRACK     read verse_span_index → more codes to pull  ← reads the DB mid-fetch
fetch more    masterSearch.strong  → the siblings' verses
parse         mediumDef, lsjDefs   → senses            ← no fetch
write         everything
```

So the partition follows the **task's own shape** — fetch/parse/fetch-more/backtrack:

```
iba/modules/raw/discover_terms.py      Hop 4      fetch + parse
iba/modules/raw/expand_family.py       Hop 5      fetch/parse loop — owns the A-Z probe
iba/modules/raw/decide_terms.py        Hop 6      no fetch; owns F0-F5
iba/modules/raw/fetch_verses.py        Hop 7      fetch + BACKTRACK + fetch more
iba/modules/raw/fetch_morphology.py    Hop 8      fetch
iba/modules/raw/parse_meaning.py       Hop 9      no fetch
iba/modules/raw/write_tables.py        Hop 10     CRUD
iba/modules/registry/word_exists.py    Hop 1
iba/modules/registry/create_word.py    Hop 3
iba/modules/base/assign_cluster.py     Hop 11
```

**Naming and purpose only** (7.5). Not written — their shape depends on B2 and §4.2.

⚠ `expand_family` and `fetch_verses` are the two that are **iterative**, and `fetch_verses` is the
one that **backtracks into the DB**. A partition by data type hides both. That is the researcher's
point, demonstrated.

---

## 7. For review

1. **§1.2** — corrected direction. Confirm.
2. **§1.4** — `on_fail` **replaces** `severity`. Four paths. Is `self-heal` distinct from
   `report-continue` *after* it heals?
3. **§1.3 / B5 — cross-resolution.** Flagged as critical and unsolved. **Nothing should be
   cross-referenced further until the resolution rule exists.**
4. **Hop 2's preset details** need STEP probes *before* the word exists. Own hop, or part of the
   ask?
5. **§4.3 — `meaning` is duplicated** (`wa_term_inventory` and `lexicon`). One must own it.
6. **Hop 7's backtrack** — raw reads base mid-fetch, and it **silently drops siblings for a new
   word**. Architecture, not a bug fix.
7. **Hop 6 is undeclared** — F0–F5, the particle ceiling, the proper-noun heuristic are all code
   constants. A judgement layer with no rule.
