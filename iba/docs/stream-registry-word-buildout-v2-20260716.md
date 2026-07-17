# The new-word work package — the run described in detail through the configs

> **v2 · 2026-07-16.** Supersedes v1 (same day). v1's narration is kept there; this is
> corrected and continued.
>
> **Method, per researcher instruction:** *"work step by step, document the missing configs and
> their missing entries; if unsure mark the config for review; create stubs for the powershell
> and method scripts (without building anything out) — cross reference these so you have the
> handles — and describe the entire process for this run through the configs — in detail."*
>
> **Nothing in this document has been loaded into a config.** Per instruction: *"do not create or
> load any configs, it is all first done in the md."* It is a specification to review, not a
> change to apply.
>
> ⚠ **One exception, and it predates the instruction:** `utility/run.json` and
> `iba/ps/New-Word.ps1` were written and committed before it (config 0.1.8). They are described
> in §6 and are subject to the same review. Nothing has been added to a config since.

---

## 1. What I had wrong in v1

Three corrections. All are the researcher's; all change the model rather than a detail.

### 1.1 A module does not own a scope

> *"raw is never book scoped, it is word or term scoped. base is not one integrated process, it
> is a collection of different processes with various scopes, it is likely to be called by
> another process. A per book validation will be associated with a PS run that is per book.
> module scope will be determined by the context of the run."*

v1 called the scope mismatch **structural** — *"the one thing no entry can paper over"*. It was
not structural. It was my mis-model. The **work package** says what it runs over; every
sub-process inherits that. `module.raw scope: ["term","book"]` and `module.base scope: ["book"]`
were simply wrong entries, now removed.

**A per-book validation is a per-book work package — not a book-shaped module.**

### 1.2 Base is a collection of routines, not a stage

`module.base` is not a thing that "runs" between raw and lexical. It is a set of routines with
different scopes, **called by whatever needs them**. `step.base.assign-cluster` is called by the
new-word package; it is not a stage the package passes through.

### 1.3 ★ There is no trigger mechanism — there are entity add-rules

This is the important one, and I asked a question that showed I had not understood it:

> *"the config will include rules for adding DB values for all entities, and this will pick up
> that there is a possibility that when you add a term, that you are missing a cluster — that is
> the trigger."*

I had modelled `trigger.new-term-needs-cluster` as an **event** fired from a step, and asked
*which* step fires it. Wrong question. Nothing fires it.

**The config declares, for every entity, the rules for adding its DB values.** Adding a term
applies the term's add-rules. One of those rules says a term must have a cluster. A term arriving
without one **fails its own add-rule** — and the rule names what supplies the missing value. That
is the trigger, and it is a consequence of the entity's rules, not a message anyone sends.

This generalises, and it is the layer this whole stream has been missing. See §4.

---

## 2. The model

```
WORK PACKAGE                       one unit of work the researcher asks for
  ├─ starts with   a PS script     named in run.json
  ├─ takes         params          Word, Source, Anchors, IncludeRelated, DryRun
  ├─ runs over     a scope         this package: ONE WORD
  ├─ moves through a SEQUENCE LIST loaded from run.json into memory
  │                                each entry: step · config · module · scope · what it does
  └─ ends with     a validation    the package is done when this passes,
                                   not when its last task returns
```

Each sub-process in the sequence is **cross-referenced** to three things: the **step** that
defines it (`pipeline.json`), the **config** that holds its rules (a process file), and the
**module** it belongs to. The order of work lives in `run.json`. **Changing the order is a config
change, never a code change.**

---

## 3. The run, in detail

Parameters: `-Word "anger" -Source "gap scan 2026-07-16" [-Anchors H2734] [-IncludeRelated] [-DryRun]`

**The handler is given a word.** (Researcher: *"what the handler is given will be determined as we
go, in this case, I guess it is a word."*) Sub-processes scoped `term` receive one term; the
package fans out to them.

### Before anything — pre-flight

| gate | config | what it does |
|---|---|---|
| `check.step.up` | `utility/step.json` | STEP is up **and answering with the tagged module**. On fail: **stop and warn the researcher.** Not a retry, not a degrade |
| `gate.cfgmaint.no-reconcile-in-scope` | `utility/config-maintenance.json` | the run refuses to start if a rule it depends on is contested |

Then `ent.run.record` is written — run id, package, params, **the config version this run is
pinned to** — *before* any work. "The config that ran" must be a record.

### 3.1 · 3.2 — Registry: create the word

`step.registry.create-new-item` → `step.registry.update-tables` · scope **word** · rules in
`process/registry.json`.

The word enters. `registry.growth` requires the addition to carry its **trigger and reason** —
that is what `-Source` is for. `registry.is-scaffolding` is a red guardrail: the word list is not
the study's object, it is the way in.

**What must be in place, and is not:**

- **The add-rules for `ent.registry.word`** (§4). What must be set when a word is created?
  `word`, `source_list`/`origin`, the reason, `status` — and which of them are required, which are
  derived, which the researcher supplies.
- **The word status vocabulary.** A word moves *created → fetched → clustered → signed off*.
  `ent.registry.word` holds `status`; **no enum declares its values.** The package cannot advance
  a word through states that do not exist.
- **`registry.growth` is RECONCILE**, so it is contested, and `gate.cfgmaint.no-reconcile-in-scope`
  would refuse this run at pre-flight. **This package cannot legally start today.**

### 3.3 — Raw: get the list of terms

`step.raw.get-strongs-by-word` · scope **word** · rules in `process/raw.json`.

From the English word, discover the terms. STEP's `meanings=` route returns curated terms whose
*meaning* relates to the concept — including terms the ESV never renders with that English word.

**Wrong, and live:** the step cites `get_strongs_for_word`, which is `masterSearch.text` — the
English-text search. `step.json` gives that route `may_source: []` and `check.step.api-fit` makes
it **red**: an English-text hit is not an original-language occurrence. The code actually uses
`meanings=`. **The config names a method that is both wrong and forbidden.**

If `-Anchors` is given, this sub-process is skipped and the terms are taken as supplied.

### 3.4 — Raw: get each term and its meaning

`step.raw.get-term-by-strongs` · scope **term** · route `module.getInfo`.

Per term: gloss, sub-glosses, transliteration, the script form, the definition, LSJ, Mounce,
occurrence count.

**★ The largest hole in the stream.** `ent.raw.lexicon` declares `holds: ["gloss",
"sub-glosses"]`. The researcher's requirement is *"all the term based meaning data is added to the
DB"*. **The definition is not declared** — no `mediumDef`, no LSJ, no Mounce.

Measured consequence, live DB: **`wa_term_inventory.meaning` is empty on 7,052 of 7,131 live
terms — 99%** — while STEP returns it on request. The config never asked for it, so nothing
stores it.

**And the sub-gloss is the sense.** `H7307G` spirit · `H7307H` spirit: breath · `H7307I` spirit:
side · `H7307J` spirit: temper — four disjoint senses, 366 occurrences partitioned between them,
each tagged per occurrence at the source. This is D101's authority arriving in the pull.

### 3.5 — Raw: related terms and root family

`step.raw.get-related-terms` · scope **term**.

**One call already has this.** `masterSearch.strong` returns `definitions[]` alongside the verses
— every sibling and relative with its gloss and count — and `searchTokens[].enhancedTokenInfo`
carries the term's own script form, transliteration and gloss. The client reads `total` and
`results` and discards both. So this sub-process may not need a call of its own.

**Not declared:** no entity for related terms or the root family, though
`wa_term_related_words` (103,944 rows) and `wa_term_root_family` (2,861) receive them.

### 3.6 — Raw: get the verses

`step.raw.get-verses` · scope **term** · route `masterSearch.strong`.

Every verse where the original-language term occurs — **regardless of how the ESV renders it**.
Gen 26:35 carries `H7307G` and the ESV never says "spirit".

The 60-cap is real and pagination is not offered: STEP reports `pageSize: 60` / `pageNumber: 1`
and honours neither. The forward-walk handles it. `check.step.cap-exhausted` proves the fetch by
**arithmetic** — rows == STEP's reported total — never by having applied a strategy.

⚠ **A base code returns 0 verses, silently.** `H7307 → 0`, `H7307G → 194`. No error either way.

### 3.7 — Raw: get the morphology

`step.raw.get-morphology` · scope **term** · route `bible.getBibleText`.

The per-word interlinear for each verse: every word with its Strong's and its morph.

**Two problems.** The step cites `_apply_ingest_verse_morphology.py` — a **canon-wide** bulk
ingest of all 25,634 verses. This package runs over one word. **And `step.json` declares
`bible.getBibleText` "NOT IMPLEMENTED — do not use until probed"**, which is false: it is the
no-cap route and it built the entire 325,507-row `verse_morphology` layer.

### 3.8 — Raw: update the tables

`step.raw.update-tables` · scope **word**.

Writes: the terms, the related terms, the meaning, the verses, the morphology.

**★ This is where the entity add-rules fire** (§4). Each row written applies its entity's
add-rules. Adding a **new term** applies the term's rules — and one of them requires a cluster. A
new term has none. **That is the trigger.** Not an event: a rule that cannot be satisfied, naming
what satisfies it.

### 3.9 — Base: assign the cluster (called, not passed through)

`step.base.assign-cluster` · scope **term-collection** · rules in `process/base.json`.

Called because the term's add-rule could not be satisfied. The method:

1. Does the term already have a cluster? → done. Membership is not re-decided.
2. Compare the term against **the terms in each cluster**. Where it relates loosely to a cluster's
   members, it joins. A cluster has no definition apart from its members.
3. No cluster found → **escalate to the researcher.** Do not guess, do not create a cluster, do
   not leave it silently null.

**Axis C. No Claude API.** The relatedness is already in hand — `relatedNos`,
`rawRelatedNumbers`, `definitions[]` and the root family all arrived with the term. "Does this
term relate to that cluster's terms" is set overlap over data the study already holds.

**Missing: the escalation channel.** The rule says escalate. **Nothing declares how** — no
channel, no queue, no record. `gate.base.cluster-assigned` passes on "a recorded escalation" and
nothing declares what one is. An escalation with no channel is a silent drop.

### 3.10 — Back to raw: validate everything

`step.raw.validate` · scope **word**.

Raw's gates: `no-null`, `fk-integrity`, `strongs-format`, `completeness`, `immutability`,
`source-parity` (RECONCILE — STEP keeps no cache, so there is no baseline to compare against).

**Missing: "validate all DB tables".** Raw's gates are **per entity**. A whole-DB validation is
not declared, and both utilities it would need are PENDING: `validation.json` and `db.json`.

### 3.11 — Back to registry: validate

`step.registry.validate` · scope **word**.

Validate the word — **including that every one of its terms has a cluster**.

The check exists: `gate.base.cluster-assigned` (red — cluster or recorded escalation). **The rule
that registry validation must read it does not.**

### 3.12 — Registry: sign off

`step.registry.signoff` · scope **word**.

**Governed by nothing. The step does not exist.**

`step.base.signoff` exists but is RECONCILE, is book-scoped, and holds *lexical*. Also missing:
the **signoff record** — who signed, when, against which config version, covering which word, and
**what voids it**. `open.base.signoff-mechanism` recommends hashing the covered outputs so
invalidation is mechanical rather than remembered. Registry is the researcher's to take.

---

## 4. ★ The entity add-rules — the missing layer

The correction in §1.3 is not a detail about one trigger. It names a layer that does not exist,
and it is the layer this stream runs on.

**Today an entity declares `holds: [...]` — a list of field names.** That is a description. It
cannot say what must be set when a row is added, what supplies it, or what happens when it is
absent. So:

- `ent.raw.lexicon` holds `["gloss","sub-glosses"]` → nothing requires the definition → 99% of
  meanings are unstored.
- The term has no cluster rule → nothing notices a term without one → membership was done "by
  hook or by crook, by chatting".

**What is needed: per entity, per field, the rule for adding it.** Roughly:

| field | required | supplied by | on absent |
|---|---|---|---|
| `term.strongs` | yes | STEP `module.getInfo` | reject |
| `term.gloss` | yes | STEP `stepGloss` | reject |
| `term.meaning` | yes | STEP `mediumDef` | reject — *this is the rule that would have caught the 99%* |
| `term.cluster` | yes | `base.cluster-assignment` | **run it** ← the trigger |
| `term.owning_word` | yes | the work package's word | reject |

**"On absent → run it"** is the whole trigger mechanism. No events, no messages. A required value
with a named supplier: if it is missing, the supplier runs. If the supplier cannot decide, it
escalates.

**This is also the join to `DBSchema.json`.** The schema register says which tables and columns
exist (110 tables, 1177 columns, observed). The add-rules say **what must be populated, by what,
and what to do when it is not.** The register is the shape; the add-rules are the obligations. The
two have never been connected — which is why the DBSchema file reads as a report rather than a
configurator element.

⚠ **MARKED FOR REVIEW.** The table above is my reading of the researcher's sentence, not his
words. The field list, the vocabulary (`required` / `supplied by` / `on absent`), and whether
add-rules live on the entity or in a component of their own are all undecided.

---

## 5. The missing configs

Renumbered against v1; scope items dissolved by §1.1.

### Whole components that do not exist

| component | needed at | for |
|---|---|---|
| `utility/db.json` | 3.10 | the DB access layer — connection, transaction, backup |
| `utility/validation.json` | 3.10 | the gate battery every module calls |

*(`utility/run.json` existed as a gap in v1 and has since been authored — see §6.)*

### The layer that does not exist

**Entity add-rules (§4)** — for every entity. Nothing in this stream can be wired without them:
they are the trigger, they are the 99% meaning gap, they are the join to the schema register.

### Entities that do not exist

| # | entity | note |
|---|---|---|
| E1 | **the TERM** | a *property* of the word in config (`"its terms (via Strong's)"`); a rich model in the code (`mti_terms`, `wa_term_inventory`, `wa_term_related_words`, `wa_term_root_family`). Everything hangs off it |
| E2 | word ↔ term | one Strong's serves several words — the live DB carries ~5,500 OWNER + ~1,500 XREF |
| E3 | related term / root family | `wa_term_related_words` 103,944 rows, `wa_term_root_family` 2,861 |
| E4 | the meaning parse | `wa_meaning_parsed` / `_sense` / `_stem` / `wa_lsj_parsed`, written by `engine/meaning_parser.py` — no step, no entity, no rule |
| E5 | the escalation | §3.9 |
| E6 | the signoff record | §3.12 |

### Methods that do not exist

| # | method | note |
|---|---|---|
| F1 | **the registry signoff** | §3.12 — the check it reads exists; the signoff does not |
| F2 | **the handler contract** | all 40 steps are `handler: null`. Given a word, for this package — the rest as we go |
| F3 | new-word-vs-existing routing | *"the term identified will either be added to an existing word term group, or a new word is created"*. `step.registry.gap-scan` is RECONCILE and routes nothing |
| F4 | whole-DB validation | §3.10 |
| F5 | the escalation channel | §3.9 |
| F6 | registry validation reads the cluster gate | §3.11 |
| F7 | the word status vocabulary | §3.1 |

### Wrong, and live

| # | what | where |
|---|---|---|
| W1 | discovery cites `masterSearch.text` — forbidden by a red gate, and not what the code does | §3.3 |
| W2 | `bible.getBibleText` declared NOT IMPLEMENTED — it built the 325k-row morphology layer | §3.7 |
| W3 | `get-morphology` cites a canon-wide script for a per-word package | §3.7 |
| W4 | `ent.raw.lexicon` too thin — 99% of meanings unstored | §3.4 |
| W5 | `include_related` declared in both `step.json` and `raw.json` | step.json |
| W6 | step.json's checks carry no `status` — raw's two gates point at statusless items | step.json |
| W7 | step.json missing its meta / script / output nodes | step.json |
| W8 | `registry.growth` RECONCILE → pre-flight would refuse this run today | §3.1 |

---

## 6. The stubs and their handles

Written before the no-configs instruction; listed for review.

**`iba/config/utility/run.json`** — 11 items. `ent.run.work-package` holds the `new-word` package:
PS script, params, `runs_over: word`, and the 12-entry sequence. `ent.run.record` pins a run to a
config version. Four rules: `run.work-package-is-the-unit`, `run.sequence-is-loaded`,
`run.scope-from-context`, `run.ends-in-validation`.

**`iba/ps/New-Word.ps1`** — runs; loads all 12 sub-processes from `run.json`; walks them; executes
nothing. Owns no process logic. Verified output shows the sequence read from config, the trigger,
and both REVIEW marks.

```
work package : new-word — Create a new registry word and build it out
runs over    : word = 'anger'
sequence     : 12 sub-process(es), loaded from run.json
STUB — 12 sub-process(es) walked, 0 executed.
```

**Python method stubs: not written.** They would be shaped entirely by the handler contract (F2)
and by the add-rules (§4). Writing them now would mean inventing both.

**Cross-reference, so the handles exist:**

```
iba/ps/New-Word.ps1
   └─ run.json · ent.run.work-package · new-word
        └─ sequence[n] ─┬─ step   → wide/pipeline.json      what it IS
                        ├─ config → process/*.json          its RULES
                        ├─ module → wide/pipeline.json      what it belongs to
                        └─ scope  → from the work package
```

---

## 7. What I need from you

1. **§4 — the add-rules.** The shape of the vocabulary, and whether they live on the entity or in
   their own component. Everything else waits on this.
2. **The trigger, confirmed.** My reading: a required value with a named supplier; absent → the
   supplier runs; the supplier cannot decide → it escalates. Is that it?
3. **The escalation channel** (F5) — how does a term reach you when no cluster fits?
4. **`registry.growth` is RECONCILE** (W8) and would block this package at pre-flight. It is
   yours, with registry.
5. **run.json and New-Word.ps1** — written before you said md-first. Keep, revise, or revert?

researcher comments:
this time round you saw the light, and are starting to work with the light shining on your work. that is good.  We are a long way from having teased out all the elements. our single run example (adding new word)  is a solid work package to dig into each and every layer of this work package.  you are using the md as a record of your thinking - that is good. I want to encourage you to continue doing it, because you make your thinking visible to me so I can steer it. This process has demonstrated how critical it is that I steer it. I also don't want to take over your work, you have a lot to contribute and you are good at it, if you stay focussed.  We need another round of thinking , this time going several layers down in thinking detail.  first let me answer your questions.

7.1 - the add-rule is likely to be a combination of configs:a) the schema: defines the table, its columns, the use of the columns, and the expectation. The schema defines the where. b) the method config defines the when. There must be a cross correlation to ensure that every method thinks about what must be added when it is prosessing, and the schema must be ready to receive it and comply with the schema rules for the tables and columns. ultimately after all the methods is designed every schema entity must have at least one method that feeds it.  Several methods could feed a column in a table, they should not be in conflict.  c) we still miss the how and what - this is likely to be in the configs that govern the source e.g. run.config for run updates to the engine tables, or step.config where the step data is defined and generated. every config is likely to have a section that deals with what data is recorded where, when, and how.

7.2 Triggers. yes, the concept of triggers creating diversions in the flow is everywhere.  That is what the role of the rule is, if the rule does not comply, what happens, where does it go to, can it resolve itself, where is that defined.

7.3 escalation - I guess there is a utility that will deal with researcher interaction. this config will define the rules. the principle is that the app must first try to resolve it, and the rules must guide it, and if not, then need to pause the workflow, communicate with the researcher, get the feedback and return to the process - without venturing into to a whole new branch and never returning to finish the job.

7.4 registry.growth. The short anwer is yes, the app should not add a new word without researcher approval.  this points to the escalation utility, this is all it is - a controlled researcher interaction.

7.5 we are a long way off starting to write ps or python scripts, but you may create the stub, so you get the naming and purpose of the script in place.

next actions:  build out all the missing configs in the .md; build out all the missing rules in the existing configs in the .md work through each hop, each branch, describe, think through it: test its completeness, check if the hop answers all the questions: what, where, how, when, why, who, what if, and validate.  this is a detail task, and must be thought through step by step, iterative, and at multiple levels.  all the work is in the .md
