# The new-word run — v7 · the raw design built in

> **v7 · 2026-07-17.** Rebuilds v4 (the hop-by-hop run) with the **settled raw column design** from
> the prototype work built into the raw hops. v4 marked the raw hops "wrong/missing"; here they are
> designed. **All the work is in this document. No config created or loaded.**
>
> Registry and signoff hops are the frame — they are the researcher's and are not designed here.
> **The raw hops (4–8) are the substance**, and they are complete to column level.

---

## 1. The model (settled, from v2–v6)

- A **work package** starts with a PS script named in `run.json`, moves through a **sequence** of
  sub-processes cross-referenced to their configs, and ends in validation.
- **Scope comes from the run**, not the module. This package runs over **one word**.
- Every rule has an **`on_fail` path**, not a severity: `report-continue · pause-continue ·
  report-stop · self-heal`.
- **Researcher interaction is one utility** (`escalation`) — a pause, not a fork; the run resumes.
- **An add-rule is three configs meeting:** the schema says *where* (column + use + expectation);
  the method says *when*; the source config says *what/how*. Every schema column must have at least
  one method that feeds it.

**The tables this run produces** (see §3 for columns):

```
word ──< word_strong >── strong ──< strong_verse >── verse ──< span ──1:1── span_analysis
  registry   L1           L2 MEANING    m:m           L3         L4a SOURCE   L4b DERIVED
```

---

## 2. What changed since v4

| v4 said | v7 says | why |
|---|---|---|
| raw has 7 steps | **5 steps** — discover · detail · verses · write · validate | relatedNos excluded, morphology folded |
| `get-related-terms` | **retired** | relatedNos is root-family noise (`H2519` → "to divide", "Mount Halak") |
| `get-morphology` (getBibleText, canon-wide) | **folded into verses** | call 3's `preview` IS the interlinear |
| `ent.raw.lexicon` holds gloss+sub-glosses | **`strong` holds the full meaning** | `mediumDef`, the sense head, at last stored where analytics reads it |
| the span master carries the overlay | **`span` (source) + `span_analysis` (derived)** | the old master is the named `no-analytical-values` violation |
| "get-strongs-by-word" uses masterSearch.text | **`meanings=`** | text-search is forbidden (`may_source: []`) and wrong |

---

## 3. The tables — column design

### L1 · `word_strong` — the link
one row per (word, strong) · the m:m junction

`id` · `word_fk` · `strong_fk` · `deleted`

### L2 · `strong` — the meaning
one row per strong · **unique, global** · from call 2 `vocabInfos[]`

`id` · **`strongNumber`** (key) · `accentedUnicode` · `stepGloss` · `stepTransliteration` ·
**`mediumDef`** (the meaning) · `lsjDefs` · `shortDefMounce` · `count` · `freqList` · `_step_Type` ·
`_vi/_es/_zh` · `deleted`
— `relatedNos` and `rawRelatedNumbers` **excluded**

### `strong_verse` — the m:m index
one per (strong, verse) · the source's assertion "this strong is in this verse"

`id` · `strong_fk` · `verse_fk` · `deleted`

### L3 · `verse`
one per verse · **unique** · does not belong to a strong · from call 3 `results[]`

`id` · **`osisId`** (key) · `key` · `preview` (verbatim, source of L4a) · `step_version` · `deleted`

### L4a · `span` — SOURCE, immutable
one per (verse, position) · a parse of `verse.preview`

`id` · `verse_fk` · **`position`** (key) · `strong_variant` (→ L2) · `surface` · **`morph_code`** ·
`particles` · `built_at` · `deleted`
— `language`/`stem`/`pos`/`person` derive from `morph_code`; `gloss`/`transliteration` read from L2

### L4b · `span_analysis` — DERIVED, mutable · 1:1 with span
filled after later stages, never by raw

`span_fk` · `candidate_char` · `char_candidate_tag` (seeding) · `role` · `role_provenance` ·
`role_set_at` · `role_source_ve_id` · `characteristic` · `ib_char_id` · `cluster` (analytics) ·
`deleted`

---

## 4. The run, hop by hop

Each hop: **from/to · what · where · how · when · why · who · what-if · validate**, and its
**config home**.

---

### Hop 0 — pre-flight
**from** a researcher request · **to** a run that may proceed, pinned to a config version

- **how** `check.step.up` (STEP up AND tagged) · `gate.cfgmaint.no-reconcile-in-scope`
- **what-if** STEP down → `report-stop`, warn the researcher · contested rule in scope → refuse
- **who** `util.run` · `util.step` · `util.config-maintenance`
- **validate** the run record exists, pinned, before any work
- **config** `run.json` (the work package) · `step.json` (check.step.up)

---

### Hops 1–3 — registry: the word enters
**from** an approved run · **to** a registered, approved word · scope **word** · `process/registry.json`

1. **exists?** — `word_registry.word`; if it exists → `report-stop` (a separate *refresh* run handles that)
2. **approve** — a new word needs researcher approval → `util.escalation` type A (prompted, with preset details: term count, verse count, which terms already held)
3. **create** — write the word, status `proposed → approved`

**Frame only.** Registry CRUD, the growth rule, and `enum.word_status` are the researcher's, taken
separately. This run *consumes* them.

---

### Hop 4 — RAW · discover
**from** a registered word · **to** the seed strongs (L1) · scope **word**

| | |
|---|---|
| **what** | find the strongs the word maps to |
| **where** | `word_strong` (L1) · and `verse`+`span` from this call's own `results[]` |
| **how** | **CALL 1** `masterSearch version=<v>\|meanings=<word>` → `definitions[].strongNumber` |
| **when** | first raw step |
| **why** | the word is the way in; the strongs are what the study holds |
| **who** | `module.raw` · `util.step` |
| **what-if** | **zero strongs** → `pause-continue` (a registered word mapping to nothing is a researcher question) |
| **validate** | `check.step.api-fit` — `meanings=` may source `word_strong`; **`text=` may not** (forbidden) |

⚠ `relatedNos` is **not followed.** Discovery ends at the seed strongs.

**config** — `step.json` `apis.meanings.may_source: [word_strong]` · `raw.json` records: `word_strong`
written here, one row per (word, seed strong).

---

### Hop 5 — RAW · detail (the meaning)
**from** each L1 strong · **to** the strong's meaning (L2) · scope **strong**

| | |
|---|---|
| **what** | the strong's full lexical detail |
| **where** | `strong` (L2) — **unique per strong, global** |
| **how** | **CALL 2** `getInfo/<v>//<strong>//` → `vocabInfos[0]` |
| **when** | per L1 strong |
| **why** | **★ this is the meaning the study has never stored where analytics reads it.** Old `D101` used the ESV surface word instead (88% of rows); the sub-gloss head is the span's true sense |
| **who** | `module.raw` · `util.step` |
| **what-if** | no vocab → recorded STEP gap, `report-continue` · **already in `strong`** (another word found it first) → **skip**, do not re-fetch (global dedup) |
| **validate** | `strong.mediumDef` non-empty — a strong with no meaning fails |

**config** — `step.json` `apis.getInfo.may_source: [strong]` · `raw.json` records: every L2 column,
from which `vocabInfos` field; `relatedNos`/`rawRelatedNumbers` explicitly not recorded.

---

### Hop 6 — RAW · verses + spans
**from** each L1 strong · **to** `strong_verse` · `verse` · `span` · scope **strong**

| | |
|---|---|
| **what** | every verse the strong occurs in, and each verse decomposed into its words |
| **where** | `strong_verse` (m:m) · `verse` (new only) · `span` (new verses only) |
| **how** | **CALL 3** `masterSearch strong=<strong>\|version=<v>` → `results[]`; **the span is a PARSE of each `result.preview`** — no separate morphology call |
| **when** | per L1 strong |
| **why** | the evidence, and its grammar. `preview` is the whole interlinear — every word with strong + morph |
| **who** | `module.raw` · `util.step` |
| **what-if** | rows < STEP's `total` → `report-stop` (a short count must never bank) · **verse/span already built** by a prior word's run → `strong_verse` gets a new row, `verse`/`span` do **not** (global dedup) |
| **validate** | `check.step.cap-exhausted` — rows == total, by arithmetic |

⚠ `Gal.2.13` proved the dedup inside one word: returned by both `G5272` and `G4942`, it is one
`verse` row and two `strong_verse` rows. **The verse does not belong to a strong.**

**config** — `step.json` `apis.masterSearch_strong.may_source: [strong_verse, verse, span]` ·
`raw.json` records: `strong_verse` (strong, verse); `verse` (osisId, preview…); `span` (position,
strong_variant, surface, morph_code, particles) parsed from `preview`.

---

### Hop 7 — RAW · write
**from** everything fetched · **to** committed rows · scope **word**

| | |
|---|---|
| **what** | commit L1/L2/L3/strong_verse/L4a; **create L4b (`span_analysis`) rows empty** |
| **where** | all six tables |
| **how** | each table's add-rules (the `records` node) |
| **when** | after the fetches |
| **why** | where the word's raw layer becomes real |
| **who** | `module.raw` |
| **what-if** | **a new strong's `word_strong` has no cluster** → its add-rule cannot be satisfied → **`self-heal` → `base.cluster-assignment`** (the trigger — a rule that names its own resolver) |
| **validate** | `no-null` · `fk-integrity` · `strongs-format` · `raw.immutable` (span is write-once) |

**config** — `raw.json` records node (all six tables) · `raw.immutable` on `span` · the cluster
add-rule on the strong (`on_fail: self-heal → base.cluster-assignment`).

---

### Hop 8 — RAW · validate
**from** committed rows · **to** a proven raw layer · scope **word**

| | |
|---|---|
| **what** | prove the layer |
| **how** | **the parse-check**: `span` (what we parsed) vs `strong_verse` (what STEP asserted) must agree — measured 35/35 senses, 0 missed, 0 invented · plus `no-null`, `fk-integrity` |
| **what-if** | mismatch → `report-stop` |
| **who** | `module.validation` (the gate every module calls) |

**config** — `validation.json` (pending) · `raw.json` validation node.

---

### Hop 9 — base: assign the cluster (called, not passed through)
**from** a new strong with no cluster · **to** a strong with a cluster, or an escalation

Already designed: `base.cluster-assignment` — has-cluster? → compare against the terms in each
cluster → assign on loose relationship → none fits → **escalate** (`util.escalation`, pause-resume).
Axis **C**, no API. `process/base.json`.

---

### Hops 10–11 — registry: validate, then sign off
**from** a proven raw layer · **to** a signed-off word

10. **validate** — every strong of the word has a cluster (read `gate.base.cluster-assigned`)
11. **sign off** — status → `signed-off`

**Frame only.** The registry signoff step and record are the researcher's. The check they read
(`gate.base.cluster-assigned`) exists.

---

## 5. What gets authored, and where

| # | config | change |
|---|---|---|
| A | **schema** (new-DB `DBSchema`) | the 6 tables, every column with `use` + `expectation` (§3) |
| B | **`step.json`** | `apis[].may_source` bound per §4; the `records` node; retire the text-search-as-source path |
| C | **`raw.json`** | replace `ent.raw.verse/verse-morphology/lexicon` with the 6 tables; add the **`records` node** (add-rules: column ← source field, when); the cluster add-rule (`on_fail: self-heal`); `raw.immutable` on `span` |
| D | **`pipeline.json`** | `module.raw`: retire `get-related-terms`, fold `get-morphology`; the 5 steps of §4 |
| E | **`run.json`** | the `new-word` sequence updated to the 5 raw steps |
| F | **`enums`** | `enum.on_fail` (report-continue · pause-continue · report-stop · self-heal); `enum.word_status` |
| G | **`escalation.json`** (new) | type A/B, pause-resume, the request/answer entities |
| H | **envelope** | `on_fail {path, resolves_by, defined_in}` replacing `severity` |

**Order:** A (the tables) → B/C (the records that feed them) → D/E (the steps that run the records)
→ then F–H, which the whole run depends on but which are cross-cutting.

---

## 6. Open before the design layer

| # | question |
|---|---|
| O1 | **L1 key** — word↔strong junction (key = the pair), unique strong in L2. Confirm. |
| O2 | `word_strong` carries only the link, not the call-1 definition fields. Confirm. |
| O3 | `particles` on `span` — a list column (keeps (verse, position) as key) or their own rows. |
| O4 | the meaning **tree** (not the head) — structured into its own table, or `mediumDef` on L2 is enough. |
| O5 | `enum.word_status` values, and whether `clustered` is a status or a derived read of the gate. |
| O6 | the escalation channel — how the researcher is actually reached (email precedent: NAS backup). |
| O7 | resumability — `run.json` must pause and resume for `pause-continue`; it cannot yet. |

researcher comments

I will answer you open items below.

Generally speaking this buildout is still light on detail, and we must make a choice to continue to add individual items to create, or to proceed with the actual build and think through what is missing at that stage. Currently the buildout talks about some stuff, and mainly focus on things that was in focus, but it definitely not have all the items that will have to be included in the config files and resolve all the questions that may come from thinking through it.

O1 + O2 - L1 only purpose is to show which strongs were returned from the STEP word search. these strongs are the basis for L2.
O3 - use the same custom we used on the master list, e.g. particles have there own row, each span have a row. Simplies the parsing.
O4 - the meaning block for each strong is complex and large, if we use different parts of it during the study, then it definely need to be be normalised into a separate table or tables, we defintely do not want to scan the whole block every time some element of the meaning block need to be used.
05 - word status need to reflect the processing stages of the registry - simplied. clustering complete is achieved on a term level, not word level.
06 - I am likely to use the VS code interface for the app user interface, so a message to the terminal could work.  I image I am going to use the chat to capture feedback, but if it is easy to create a message window then that is also good.
O7 what would be best practice for resumeability. the app is moving away from the chat being the continuity interface, so I assume the resumeability is because the interaction is in a loop in the program with conditions for exit and continue.

