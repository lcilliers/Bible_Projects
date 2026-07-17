# The new-word work package — every hop, every branch, tested

> **v3 · 2026-07-17.** Supersedes v2 (2026-07-16); v2's narration and the researcher's comments
> are kept there.
>
> **All the work is in this document. No config has been created or loaded.**
>
> **Method:** *"build out all the missing configs in the .md; build out all the missing rules in
> the existing configs in the .md; work through each hop, each branch, describe, think through
> it: test its completeness, check if the hop answers all the questions: what, where, how, when,
> why, who, what if, and validate."*

---

## 1. The model, as it now stands

### 1.1 ★ An add-rule is three configs meeting

The researcher's answer to *"where do add-rules live"* is that they do not live in one place.
Three configs each own one part, and they must agree:

| part | lives in | says |
|---|---|---|
| **WHERE** | the **schema** | the table, its columns, **the use of each column, and the expectation** |
| **WHEN** | the **method config** | at what point in its processing a method must add this value |
| **WHAT + HOW** | the **source config** | what data is recorded, and how it is produced — `step.json` for STEP data, `run.json` for run/engine data |

> *"every config is likely to have a section that deals with what data is recorded where, when,
> and how."*

So **every component gains a `records` node.** Not a new file — a new section in each.

**This settles two things that have been open since yesterday.**

*It settles what `DBSchema.json` is for.* The researcher's verdict on it was *"more of a
structured report than a configurator item… very difficult to work with the items that really
matter."* Now the items that really matter are named: a column's **use** and its **expectation**.
The register today carries a description derived from profiling — which is *observation*. What it
must carry is the **obligation**: what this column is for, and what must be true of it. Structure
and profile are the evidence; use and expectation are the configuration.

*It settles the 99% empty `meaning` column.* Not a pipeline bug — an add-rule that never existed.
No schema entry said `wa_term_inventory.meaning` **expects** STEP's `mediumDef`; no method config
said **when** it is written; `step.json` never declared `mediumDef` as data it records. Three
configs, three silences, one empty column.

### 1.2 ★ The cross-correlation invariant

> *"ultimately after all the methods is designed every schema entity must have at least one method
> that feeds it. Several methods could feed a column in a table, they should not be in conflict."*

Two checks fall out, and they are mechanical:

| check | asks | catches |
|---|---|---|
| **every column has a feeder** | for each column the schema expects, does at least one method declare it writes it? | `wa_term_inventory.meaning` — expected, fed by nobody |
| **feeders do not conflict** | where several methods write one column, do they agree on what it means and when? | `causative_form_present` in `wa_term_inventory` **and** `has_causative_stem` in `wa_meaning_parsed` — one fact, two columns, two feeders, no agreement |

The first is the direction nothing has ever run: **from the schema outward, asking who fills
this.** Every audit this study has done ran the other way — from the method, asking what it
wrote. That is why a column can sit empty for six months and look fine from every method's point
of view.

⚠ It also means a column that **no** method feeds is either a missing method or a column that
should not exist. Both are findings.

### 1.3 ★ A rule is a fork, not a test

> *"the concept of triggers creating diversions in the flow is everywhere. That is what the role
> of the rule is: if the rule does not comply, what happens, where does it go to, can it resolve
> itself, where is that defined."*

Today a rule declares `validation: {axis, check, severity, enforcement}` — it can say *this
failed, red*. It cannot say **what happens next**. So every rule needs a non-compliance path:

```
rule
 ├─ complies      → carry on
 └─ does not comply
      ├─ can it resolve itself?   → WHO resolves it (a named method)
      │                              e.g. term has no cluster → base.cluster-assignment
      ├─ cannot resolve itself    → escalate (util.escalation)
      └─ must not proceed         → halt
```

**The proposed envelope addition** — `on_fail`, on every rule:

| field | means |
|---|---|
| `resolves_by` | the method that can supply/repair the missing thing. Null if none |
| `then` | `retry` · `escalate` · `halt` · `record-and-continue` |
| `defined_in` | the config that owns the resolving method |

*The cluster case reads:* `term.cluster` absent → `resolves_by: base.cluster-assignment` → that
method cannot decide → `then: escalate`.

⚠ **MARKED FOR REVIEW.** `severity` (red/amber) and `on_fail` overlap. Red-and-resolvable is not
the same as red-and-halt, and today both are just "red".

### 1.4 ★ The escalation utility — `utility/escalation.json` (does not exist)

> *"there is a utility that will deal with researcher interaction. The principle is that the app
> must first try to resolve it, and the rules must guide it, and if not, then need to pause the
> workflow, communicate with the researcher, get the feedback and return to the process — without
> venturing into a whole new branch and never returning to finish the job."*

This is a bigger thing than "escalation". It is **the only sanctioned way the app talks to the
researcher**, and it covers approvals as much as failures — `registry.growth` (7.4: *"the app
should not add a new word without researcher approval"*) routes through it too.

**The shape, which is the whole point:**

```
try to resolve  →  cannot  →  PAUSE the work package (do not abandon it)
                              →  ask the researcher
                              →  wait
                              →  take the answer
                              →  RESUME at the point it paused
```

> *"without venturing into a whole new branch and never returning to finish the job."*

That sentence is the design constraint. An escalation is **a pause, not a fork**. The work package
survives it and finishes. Which means the run must be **resumable** — and that is new: nothing in
`run.json` can pause and resume.

**What it must declare** (my proposal; ⚠ review):

| node | holds |
|---|---|
| `ent.escalation.request` | id · run_id · the sub-process that paused · what was tried · the question · options · raised_at |
| `ent.escalation.answer` | the researcher's decision · who · when · free text |
| `escalation.try-first` | the app must attempt resolution under the rules **before** asking. An escalation that skipped the attempt is a defect |
| `escalation.pause-not-fork` | the package pauses and resumes at the same point. It never abandons the job |
| `escalation.channel` | **how** the researcher is reached. Precedent: the NAS-backup email alert |
| `escalation.answer-is-recorded` | the answer is data, not a chat message. It must survive the session |
| `gate.escalation.no-silent-drop` | red — a raised escalation with no answer blocks the package. It cannot quietly pass |

**The two escalations this one package raises:**

1. **A new word needs approval** — `registry.growth` (7.4). Before the word is created.
2. **A term fits no cluster** — `base.cluster-assignment` step 3.

⚠ **Open:** an approval is asked **before** the work; a cluster decision **during** it. Same
mechanism, different moment. Whether that is one kind or two is not decided.

---

## 2. The test — eight questions per hop

| question | what it asks of the hop |
|---|---|
| **what** | what does it do; what data does it record |
| **where** | which table and columns (the schema) |
| **how** | which route/method produces the value (the source config) |
| **when** | at what point in the method it is written |
| **why** | what it is for — the use |
| **who** | which module owns it; who supplies it; who is told |
| **what if** | it does not comply — resolve, escalate, or halt |
| **validate** | how we know it was done |

A hop that cannot answer all eight is not specified.

---

## 3. The run, hop by hop

Package `new-word` · `-Word "anger" -Source "gap scan" [-Anchors] [-IncludeRelated] [-DryRun]` ·
runs over **one word**.

---

### Hop 0 — pre-flight

| | |
|---|---|
| **what** | prove the run may start; write the run record |
| **where** | `ent.run.record` → *no table declared* ⚠ |
| **how** | `check.step.up` (STEP up **and tagged**); `gate.cfgmaint.no-reconcile-in-scope` |
| **when** | before any work |
| **why** | a raw process without its source is not a slow run, it is a wrong one |
| **who** | `util.run` · `util.step` · `util.config-maintenance` |
| **what if** | STEP down → **halt and warn** (not retry, not degrade). Contested rule in scope → refuse to start |
| **validate** | the run record exists and is pinned to a config version |

**★ FAILS TODAY.** `registry.growth` is RECONCILE, so `gate.cfgmaint.no-reconcile-in-scope`
refuses this package at pre-flight. **The package cannot legally start.** 7.4 resolves the
substance (growth requires researcher approval, via `util.escalation`) — the rule still has to
stop being contested.

**Missing rules:**
- `run.records` node — where the run record lives (`engine_run_log`? a new table? ⚠)
- `gate.run.record-before-work` — red; no work before the pin
- **resumability** (§1.4) — nothing can pause and resume

---

### Hop 1 — registry: create the word

| | |
|---|---|
| **what** | create the registry entry |
| **where** | `word_registry` — `word`, `source_list`, `origin`, `notes`, `status` |
| **how** | researcher-supplied via `-Word` / `-Source` |
| **when** | first sub-process |
| **why** | the study's entry point; everything downstream is reachable only from here |
| **who** | `module.registry` · rules in `process/registry.json` |
| **what if** | **the word is new → the researcher must approve it (7.4)** → `resolves_by: null` → `then: escalate` → `util.escalation` → resume |
| **validate** | `gate.registry.growth-recorded` — the addition carries its trigger and reason |

**Missing rules:**

| # | rule | says |
|---|---|---|
| R1 | `registry.growth` **resolved** | growth requires researcher approval through `util.escalation`. Currently RECONCILE and blocking |
| R2 | `enum.word_status` | **does not exist.** A word moves *proposed → approved → fetched → clustered → signed off*. `word_registry.status` has no declared vocabulary. ⚠ the live column's values are unknown to the config |
| R3 | `registry.records` node | which columns this method feeds, and when |
| R4 | add-rules for `ent.registry.word` | `word` required · `source_list` required (feeds growth) · `status` required, from `enum.word_status` · `origin` required |
| R5 | **duplicate check** | `word_registry.word` is **222 rows / 218 distinct** — deadness, resentment, transformation, vulnerability each appear twice. No rule forbids it. What if the word exists → escalate or reject? **Not decided** |

---

### Hop 2 — raw: get the list of terms

| | |
|---|---|
| **what** | discover the terms the English word maps to |
| **where** | nothing written yet — discovery only |
| **how** | STEP `masterSearch.meanings` — curated terms whose **meaning** relates to the concept, including ones the ESV never renders with that word |
| **when** | after the word exists |
| **why** | the word is a way in; the terms are what the study actually holds |
| **who** | `module.raw` · `util.step` |
| **what if** | **zero terms → the word maps to nothing.** Escalate: a registered word with no terms is a researcher question, not a failure. ⚠ not declared |
| **validate** | `check.step.api-fit` — the sourcing route may produce what it is producing |

**Wrong, and live (W1):** the step cites `get_strongs_for_word` = `masterSearch.**text**`, which
`step.json` forbids from sourcing raw (`may_source: []`, red). The code uses `meanings=`. **The
config names a method that is both wrong and prohibited.**

**Missing rules:**

| # | rule | says |
|---|---|---|
| R6 | fix `step.raw.get-strongs-by-word` | route = `masterSearch.meanings`, not `.text` |
| R7 | `raw.term-discovery` | what counts as a term for this word; the particle filter (`^[HG]9`); the vocab-count ceiling |
| R8 | `-Anchors` branch | when anchors are given, discovery is **skipped**. Not declared anywhere |
| R9 | **the F0 fork** | with `-Anchors`, `definition_codes` is empty so filter F0 never fires — **the same term can be included via a word entry and excluded via a term entry.** Undeclared, and a real behavioural difference between the two entry points |

---

### Hop 3 — raw: term + meaning

| | |
|---|---|
| **what** | per term: gloss, sub-glosses, script form, transliteration, **the definition**, LSJ, Mounce, count |
| **where** | `mti_terms`, `wa_term_inventory`, `lexicon` |
| **how** | STEP `module.getInfo` |
| **when** | per term, after discovery |
| **why** | **the sub-gloss is D101's sense authority.** `H7307G` spirit · `H7307H` breath · `H7307I` side · `H7307J` temper — four disjoint senses, tagged per occurrence at the source |
| **who** | `module.raw` · `util.step` |
| **what if** | no vocab for a code → record as a STEP gap, never as "the term does not exist" (`step.is-a-source-not-the-truth`) |
| **validate** | `check.step.response-components` — term · meaning · related · verses all present |

**★ The largest hole. `ent.raw.lexicon` declares `holds: ["gloss", "sub-glosses"]`.**

Against *"all the term based meaning data is added to the DB"*, run the §1.2 check — **which
method feeds this column?**

| column | expects | fed by | reality |
|---|---|---|---|
| `wa_term_inventory.meaning` | STEP `mediumDef` | **nobody declares it** | **EMPTY on 7,052 / 7,131 (99%)** |
| `wa_term_inventory.lsj_entry` | STEP `lsjDefs` | undeclared, but written | populated 2,060/2,061 Greek |
| `wa_term_inventory.causative_form_present` | derived from `mediumDef` | **nobody** | column exists, INSERT omits it |
| *(script form)* | STEP `accentedUnicode` | **no column at all** in either term table | lost |
| `lexicon.original_unicode` | STEP `accentedUnicode` | bulk harvest 2026-06-16 | **base codes only — 0 of 11,666 rows end in a letter**, so no sub-gloss, so **no sense** |

**Missing rules:**

| # | rule | says |
|---|---|---|
| R10 | `ent.raw.lexicon` add-rules | `mediumDef` **required** · `lsjDefs` (Greek) · `shortDefMounce` (Greek) · `accentedUnicode` **required** — *R10 alone is the 99%* |
| R11 | `raw.records` node | which columns raw feeds, from which STEP field, when |
| R12 | `step.records` node | what STEP data is recorded — the field list, per route (7.1c) |
| R13 | the **script form** needs a column | `accentedUnicode` is the actual Hebrew/Greek word and has no home on the term |
| R14 | `lexicon` covers sub-glosses | it holds `H7307` (0 verses) and none of the four codes carrying the senses |
| R15 | **the meaning parse** | `wa_meaning_parsed` / `_sense` / `_stem` / `wa_lsj_parsed` — no step, no entity, no rule. `parse_term` needs `language` · `medium_def` · `lsj_entry` · `strong_number`; its caller passes one, so **7,739 rows defaulted to "Hebrew"** and every Greek sense tree was built by the Hebrew parser |

---

### Hop 4 — raw: related terms + root family

| | |
|---|---|
| **what** | the term's relatives and its root family |
| **where** | `wa_term_related_words` (103,944) · `wa_term_root_family` (2,861) |
| **how** | STEP `relatedNos` — **or free with the verses**, see below |
| **when** | per term |
| **why** | **this is what cluster assignment compares against** (§Hop 7). Without it the cluster rule has no signal |
| **who** | `module.raw` |
| **what if** | `related_words[]` **absent** ≠ empty. Empty is a fact about the term; absent is a fact about the fetch |
| **validate** | `check.step.response-components` — the field must have been assessed |

**Free, and discarded:** `masterSearch.strong` returns `definitions[]` — every sibling and
relative with gloss and count — **on the same call that fetches the verses**. The client reads
`total` and `results` only. `popularity` == `getInfo`'s `count`; `popularityList` == `freqList`.
The A–Z suffix probe (up to 26 `getInfo` calls/term) re-discovers what `definitions[]` already
listed.

**Missing rules:**

| # | rule | says |
|---|---|---|
| R16 | related-term + root-family entities | neither is declared |
| R17 | `relatedNos.matchingForm` | the script form of the relative — **not even in the pull artefact** |
| R18 | prefer `definitions[]` | take relatives from the verse call rather than a second call. ⚠ needs the `relatedNos` vs `definitions[]` comparison — **cheap, the dumps are on disk** |
| R19 | `raw.include-related` declared twice | in `raw.json` **and** `step.json` (W5). It is a *what to fetch* decision → `raw.json` |

---

### Hop 5 — raw: verses

| | |
|---|---|
| **what** | every verse where the term occurs |
| **where** | `wa_verse_records` · `wa_verse_term_links` |
| **how** | STEP `masterSearch.strong`, forward-walk over the 60-cap |
| **when** | per term |
| **why** | the evidentiary floor. Gen 26:35 carries `H7307G` and the ESV never says "spirit" — a text search would never find it |
| **who** | `module.raw` · `util.step` |
| **what if** | rows < STEP's reported total → **halt.** A short count must never bank. Missing total → also a failure |
| **validate** | `check.step.cap-exhausted` — proof by arithmetic, never by having applied a strategy |

⚠ **A base code returns 0 verses, silently** — `H7307 → 0`, `H7307G → 194`. No error. Very likely
the cause of "different results every time".

**Missing rules:**

| # | rule | says |
|---|---|---|
| R20 | resolve before searching | search the **resolved** code. Undeclared, and the reason a base code silently returns nothing |
| R21 | **the multi-code fork** | union the siblings or keep them as senses? They are **disjoint senses**, 366 occurrences partitioned. For a study whose object is meaning, unioning collapses what STEP already decided. **RECONCILE since 2026-07-13** |
| R22 | `wa_verse_records.translation` | hard-coded `'ESV'` in the INSERT. No rule, no config |

---

### Hop 6 — raw: morphology

| | |
|---|---|
| **what** | the per-word interlinear of each verse |
| **where** | `verse_morphology` (325,507) · `verse_morphology_raw` (25,634 — raw HTML kept) |
| **how** | STEP `bible.getBibleText` — **no cap**, addressed by reference |
| **when** | per verse fetched |
| **why** | the linguistic source of truth. Language, stem, pos all derive from it |
| **who** | `module.raw` |
| **what if** | the master attests a Strong's STEP does not tag → **a recorded STEP gap**, not an absence |
| **validate** | `gate.raw.fk-integrity` — every morphology row resolves to a real verse |

**Wrong, and live:**
- **W2** — `step.json` declares `bible.getBibleText` *"NOT IMPLEMENTED — do not use until probed"*. **It built this entire layer** (`_apply_ingest_verse_morphology.py:32`), bypassing `StepClient` with raw `requests`.
- **W3** — the step cites that canon-wide script (all 25,634 verses) for a **per-word** package.

**Missing rules:**

| # | rule | says |
|---|---|---|
| R23 | correct `bible.getBibleText` | it is live, it is the no-cap route, it is how the interlinear arrives |
| R24 | per-word morphology | this package needs the interlinear **for its verses**, not the canon |
| R25 | `morph_code` decomposition | `HNcfsc` = Hebrew · Noun · common · feminine · singular · **construct**. Construct-vs-absolute is *"Spirit **of** God"* vs *"a spirit"*. Stored as an opaque token; only `pos` and `stem` are pulled out |

---

### Hop 7 — raw: update the tables · **and the fork**

| | |
|---|---|
| **what** | write the terms, related terms, meaning, verses, morphology |
| **where** | every table above |
| **how** | the add-rules of each entity (§1.1) |
| **when** | after the fetches, before validation |
| **why** | this is where a term first **exists** |
| **who** | `module.raw` |
| **what if** | **★ the term's add-rule requires a cluster. A new term has none. THAT IS THE TRIGGER** — `resolves_by: base.cluster-assignment` |
| **validate** | `gate.raw.no-null` · `fk-integrity` · `strongs-format` · `immutability` |

**No event is fired.** The rule cannot be satisfied, and it names who satisfies it. §1.3.

---

### Hop 8 — base: assign the cluster (called, not passed through)

| | |
|---|---|
| **what** | put each new term in an analysis group |
| **where** | `mti_terms.cluster_code` (49 clusters) |
| **how** | 1. has a cluster? → done. 2. compare against **the terms in each cluster** → loose relationship → join. 3. none → **escalate** |
| **when** | called when a term's cluster add-rule cannot be satisfied |
| **why** | a term no group owns is a term the study never reads |
| **who** | `module.base`, **called by** the package. Escalates to **the researcher**, never the model |
| **what if** | no cluster fits → `util.escalation` → **pause → ask → answer → resume** |
| **validate** | `gate.base.cluster-assigned` — red: a cluster **or** a recorded escalation |

**Axis C. No API.** The relatedness arrived with the term (Hop 4): `relatedNos`,
`rawRelatedNumbers`, `definitions[]`, root family. "Does this term relate to that cluster's terms"
is set overlap over data already held.

**Missing rules:**

| # | rule | says |
|---|---|---|
| R26 | the comparison, stated | which signal, what threshold. *Rule-governed* is what makes it regenerable — an unstated threshold is a judgement nobody can reproduce |
| R27 | `cluster_subgroup` | placement **within** a cluster is a second, finer question. Not decided |
| R28 | `open.base.cluster-regenerability` | never re-run vs `gate.base.regenerable`. My proposal: re-derive and **report divergence**, never silently reassign |
| R29 | escalation carries a proposal | *"the app must first try to resolve it"* — so the escalation should say what it tried and what it nearly chose |

---

### Hop 9 — back to raw: validate everything

| | |
|---|---|
| **what** | prove the raw layer is sound |
| **where** | every table written |
| **how** | the gate battery |
| **when** | after the tables are written and clusters assigned |
| **why** | *"then back to raw the validate everything"* |
| **who** | `module.validation` — **the gate every other module calls** |
| **what if** | red → halt. Amber → record and continue |
| **validate** | this **is** the validation |

**Missing:** `utility/validation.json` and `utility/db.json` — **both PENDING**. Raw's gates are
**per entity**; a whole-DB validation is not declared. And §1.2's *every column has a feeder*
belongs here — it is the check that would have caught the 99%.

---

### Hop 10 — back to registry: validate

| | |
|---|---|
| **what** | validate the word, **including that every one of its terms has a cluster** |
| **where** | `word_registry` · `mti_terms.cluster_code` |
| **how** | read `gate.base.cluster-assigned` for every term of the word |
| **when** | after raw validates |
| **why** | *"then back to register to validate (including rule that terms must have a cluster)"* |
| **who** | `module.registry` |
| **what if** | a term has no cluster and no escalation → the word is not ready. **Do not sign off** |
| **validate** | ⚠ **F6 — no rule says registry validation reads the cluster gate.** The check exists; the reading does not |

---

### Hop 11 — registry: sign off

| | |
|---|---|
| **what** | sign the word off |
| **where** | `word_registry.status` + a signoff record |
| **how** | a researcher act |
| **when** | last |
| **why** | *"the registry cannot be signed off for a word until all its terms are connected with a cluster"* |
| **who** | **the researcher** — through `util.escalation`? ⚠ or is a signoff a different kind of interaction? |
| **what if** | a term is unclustered → refuse |
| **validate** | — |

**Governed by nothing. `step.registry.signoff` does not exist.** Nor does the signoff record —
who signed, when, against which config version, over which word, **and what voids it**.
`open.base.signoff-mechanism` recommends hashing the covered outputs so invalidation is
mechanical rather than remembered.

⚠ **Open:** is a signoff an escalation (pause → ask → answer → resume) or its own thing? It has
the same shape. Registry is the researcher's.

---

## 4. What must be authored

### 4.1 New components

| component | why |
|---|---|
| **`utility/escalation.json`** | §1.4. The only sanctioned researcher interaction. **Two of this package's hops need it** (word approval, cluster decision) and neither can run without it |
| **`utility/validation.json`** | Hop 9. The gate battery every module calls |
| **`utility/db.json`** | Hop 9. The DB access layer |

### 4.2 A new node in every component

**`records`** — what data this config's methods record, where, when, how (7.1c). Needed at
minimum in `raw.json`, `step.json`, `run.json`, `registry.json`, `base.json`.

### 4.3 The schema must carry use + expectation

`DBSchema.json` currently holds structure + a profile-derived description. It must hold, per
column: **the use** and **the expectation** — and, by cross-correlation, **which method feeds
it**. That is the answer to *"I dont yet know what rules would be needed"*.

### 4.4 New entities

`ent.raw.term` · word↔term · related-term · root-family · the meaning parse ·
`ent.escalation.request` · `ent.escalation.answer` · the signoff record · the run record's table

### 4.5 New enums

`enum.word_status` (R2) · `enum.escalation_state` (raised · answered · resumed) ·
`enum.on_fail` (retry · escalate · halt · record-and-continue)

### 4.6 Envelope change

`on_fail: {resolves_by, then, defined_in}` on every rule (§1.3). ⚠ overlaps `severity`.

---

## 5. Blocked

| # | blocker | blocks |
|---|---|---|
| B1 | **`registry.growth` is RECONCILE** | pre-flight refuses the package. 7.4 gives the substance; the rule must be resolved |
| B2 | **the handler contract** | all 40 steps are `handler: null`. Given a word, for this package — the rest as we go |
| B3 | **resumability** | §1.4 requires pause-and-resume. `run.json` has no concept of it |
| B4 | **the multi-code fork** (R21) | RECONCILE since 2026-07-13; decides whether a "term" is a lemma or a sense |

---

## 6. Stubs

`iba/config/utility/run.json` + `iba/ps/New-Word.ps1` — written 2026-07-16, **before** the
md-first instruction. The stub runs, loads all 12 sub-processes from config, walks them, executes
nothing.

**Not written:** Python method stubs. Per 7.5 the naming and purpose can be stubbed — but their
shape is decided by the handler contract (B2) and the add-rules (§1.1), so I would be inventing
both. Proposed naming only, for review:

```
iba/modules/registry/create_word.py     step.registry.create-new-item
iba/modules/raw/get_terms.py            step.raw.get-strongs-by-word
iba/modules/raw/get_term_meaning.py     step.raw.get-term-by-strongs
iba/modules/raw/get_related_terms.py    step.raw.get-related-terms
iba/modules/raw/get_verses.py           step.raw.get-verses
iba/modules/raw/get_morphology.py       step.raw.get-morphology
iba/modules/raw/update_tables.py        step.raw.update-tables
iba/modules/base/assign_cluster.py      step.base.assign-cluster
```

---

## 7. For review

1. **§1.1 — the three-config add-rule.** My reading of 7.1. Does `records` belong as a node in
   every component, or as its own thing?
2. **§1.2 — every column has a feeder.** The check runs *from the schema outward*. Nothing has
   ever run that direction. Confirm it is a gate.
3. **§1.3 — `on_fail` on the envelope.** Overlaps `severity`. One field or two?
4. **§1.4 — `utility/escalation.json`.** Naming, and: is an **approval** (before) the same kind
   as a **decision** (during)? Is a **signoff** a third?
5. **R21 — the multi-code fork.** Disjoint senses vs union. It decides what a "term" is, and
   everything above it.
6. **R5 — duplicate words.** 222 rows / 218 distinct, today. What if the word exists?
