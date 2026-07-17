# The new-word run — the data layer, element by element

> **v5 · 2026-07-17.** Continues v4 (the hops). **All the work is in this document. No config has
> been created or loaded.**
>
> **Method:** *"decide / question each data element / column / output / input and tease it out in
> terms of config entries that govern it in all the different supporting configs also. if you
> unclear (e.g. span / morphology) then mark and bypass, do what you can. Use the current database
> as a guide."*
>
> **Every element carries a verdict:** **DECIDED** · **QUESTION** (needs the researcher) ·
> **BYPASS** (marked, not worked).
>
> **Every element names the configs that govern it**, per the three-config model:
> **WHERE** = schema (use + expectation) · **WHEN** = method config · **WHAT/HOW** = source config
> · plus **IBA-wide** where the rule is shared, and its **`on_fail`** path.

---

## 1. ★ What the live DB says before we design anything

Four measurements, taken today. Each one changes a decision below.

### 1.1 The meaning is not missing — it is held at the wrong grain

```
lexicon.medium_def          11,666 / 11,666  populated   ← but 0 rows end in a letter: BASE CODES ONLY
wa_term_inventory.meaning        87 /  7,844 populated   ← the SUB-GLOSS codes the study actually uses
```

**The base code has the definition and no verses. The sub-gloss has the verses and no definition.**
`H7307` → `medium_def` present, **0 verses**. `H7307G` → 194 verses, `meaning` empty.

v4 called this "two columns for one fact". It is worse and more interesting: **two columns at two
different grains, and the study reads the one that is empty.**

### 1.2 The term table is at the wrong grain

```
wa_term_inventory   7,844 rows / 4,155 distinct Strong's
                    H3588A appears 18×, H5921A 16×, H0226G 15×
```

One row per **(word, term)** — so a term used by 18 words has 18 rows. And it holds the term's
**meaning, gloss, LSJ, Mounce, occurrence_count** — all facts about the *term*, stored once per
*word*. **A term's definition would be written 18 times, and could disagree 18 ways.**

**This is the root of the meaning mess**: the definition has no single home to be written to.

### 1.3 There is no word status — there are four legacy stage-trackers

```
phase1_status         Complete 176 · Excluded 42 · Pending 2 · In Progress 2
session_b_status      Verse Context Reset 160 · NULL 45 · Analysis Complete 12 · Ready for Analysis 5
verse_context_status  Complete 172 · NULL 49 · In Progress 1
dim_review_status     NULL 170 · Complete 52
```

Four columns, each tracking a stage that no longer exists. **None of them is "where is this word
in its build-out".** The new-word run needs one status; the live DB has four wrong ones.

### 1.4 The word is not unique

222 rows / 218 distinct — *deadness, resentment, transformation, vulnerability* twice each.

---

## 2. The grain, decided

Everything below rests on this. **DECIDED** (subject to review — it follows from 1.1/1.2, not from
a ruling):

| thing | grain | why |
|---|---|---|
| **word** | one row per English word | the entry point |
| **term** | **one row per Strong's code** — sub-gloss codes included | a term's facts are the term's, written once |
| **word↔term** | one row per (word, term) | a Strong's serves several words; the study already has ~1,500 XREF copies proving it |
| **term meaning** | on the **term** | 1.1 — it is a fact about the term, not about the word that found it |

**What this retires:** `wa_term_inventory` as it stands. It is a word×term junction wearing a
term table's clothes. Split it: term facts → term; the (word, term) edge → the junction.

⚠ **QUESTION:** is `lexicon` then the term table, extended to sub-glosses — or is `lexicon` the
raw STEP capture and `term` the study's object built from it? The live split (`lexicon` = base
codes bulk-harvested; `mti_terms`/`wa_term_inventory` = the study's terms) suggests two things
exist for a reason, but it may just be accretion.

---

## 3. The data layer, element by element

### 3.1 `word` — from Hop 3

| element | verdict | WHERE — use · expectation | WHAT/HOW — source | WHEN — method | on_fail |
|---|---|---|---|---|---|
| `word` | **DECIDED** | the English inner-being word; the entry point · **required · unique** | the researcher, `-Word` | Hop 1 checks, Hop 3 creates | exists → `report-stop` (7.6) |
| `source` | **DECIDED** | why it was registered — the growth trigger · required, free text | the researcher, `-Source` | Hop 3 | absent → `report-stop` |
| `origin` | **QUESTION** | live values: `original_list` 185 · `programme_addition` 27 · NULL 10 | — | — | — |
| `status` | **DECIDED** | where the word is in its build-out · required · **`enum.word_status`** | the run | Hops 3, 11, 14 | — |
| `approved_by` · `approved_at` | **DECIDED** | the researcher's approval — 7.4 · required before create | `util.escalation` type A | Hop 2 | no answer → stays paused |
| `signed_off_by` · `_at` · `_config_version` | **DECIDED** | the signoff, and what voids it | the researcher | Hop 14 | — |

**`origin` — the QUESTION:** is it *how the word arrived* (original list vs programme addition)?
If so it is **the same fact as `source`**, one coded and one free text. **Two columns, one fact —
exactly what §1.2 of v4 says to catch.** One should own it.

**`enum.word_status` — proposed**, from the run's own shape (⚠ review):

```
proposed    → the word is asked for, not yet approved      (Hop 2 raised)
approved    → the researcher said yes                      (Hop 2 answered)
built       → terms, verses, meaning are in                (Hop 10)
clustered   → every term has a cluster or an escalation    (Hop 11)
signed-off  → the researcher signed it                     (Hop 14)
rejected    → the researcher said no                       (Hop 2)
```

**Retired from the live table:** `phase1_status`, `session_b_status`, `verse_context_status`,
`dim_review_status`, `carry_forward`, `no` (identical to `id` on all 222 rows),
`phase2_datasets` (declared REAL, holds 4 filenames), `last_automation_run` (holds the literal
`'AUDITED'` on 193 rows), `word_synopsis` (100% NULL), `dimensions`, `sb_classification*`,
`dim_review_*`, `term_sharing_ratio` / `unique_term_count` / `shared_term_count` (derivable).
**~20 of 32 columns do not serve this run.**

⚠ **BYPASS:** `description` and `inference_note` are researcher-authored prose (212 and 32
populated). They serve a study purpose this run does not touch. Not designed here.

---

### 3.2 `term` — from Hop 5, the core of the run

| element | verdict | WHERE — use · expectation | WHAT/HOW — source | WHEN | on_fail |
|---|---|---|---|---|---|
| `strongs` | **DECIDED** | the term's identity · required · **`[HG]\d{4}[A-Z]?`, zero-padded** · **unique** | STEP `strongNumber` | Hop 5 | malformed → `report-stop` |
| `language` | **DECIDED** | Hebrew · Greek · Aramaic · required | ⚠ see below | Hop 5 | — |
| `script_form` | **DECIDED** | **the actual Hebrew/Greek word** · required | STEP `accentedUnicode` (`getInfo`) **or** `matchingForm` (`masterSearch.strong`) | Hop 5 | absent → `report-continue` + STEP gap |
| `transliteration` | **DECIDED** | a reading aid · required · **never shown without the gloss** | STEP `stepTransliteration` | Hop 5 | — |
| `gloss` | **DECIDED** | the term's short sense · required | STEP `stepGloss` | Hop 5 | absent → `report-stop` |
| `meaning` | **DECIDED** | **the definition** · **required** · one home only (§1.1) | STEP `mediumDef` | Hop 5 | absent → `report-stop` |
| `lsj_entry` | **DECIDED** | LSJ text · Greek only | STEP `lsjDefs` | Hop 5 | — |
| `short_def_mounce` | **DECIDED** | Mounce short def · Greek only | STEP `shortDefMounce` | Hop 5 | — |
| `occurrence_count` | **DECIDED** | corpus frequency · **⚠ CAPPED AT 10000 — not exact** | STEP `count` | Hop 5 | — |
| `is_sense_of` | **BYPASS** | the base code this is a sub-gloss of | derivable from the code | Hop 5 | — |
| `cluster` | **DECIDED** | the analysis group · **required** | `base.cluster-assignment` | Hop 11 | absent → **`self-heal`** → Hop 11 |
| `source_api` | **DECIDED** | which STEP route produced this row · required | the fetch | Hop 10 | absent → `report-stop` |
| `step_version` | **DECIDED** | **provenance** — which module the text came from · required | **IBA-wide** (§1.3) | Hop 10 | absent → `report-stop` |

**`language` — the trap.** `wa_meaning_parsed.language` reads Hebrew on 7,739 rows because a
caller passed one field of four. And `project_morph_is_source_of_truth` says language derives from
`morph_code`. **But a term has no morph** — morph is a property of a *span*, not of a lemma. So
for the term, language derives from the **code prefix** (`H`/`G`), and Aramaic is invisible there.
⚠ **QUESTION:** is the term's `language` the code prefix, or is it `BYPASS` until spans are
designed? The live `lexicon` has Hebrew 7,027 · Greek 4,638 · **Aramaic 1** — which is not
credible for the OT.

**`occurrence_count` — the expectation must state the cap.** Five entries sit at exactly 10000.
Any frequency arithmetic over the common words is wrong, and the column looks fine.

**`meaning` — one home.** Per §2 the term owns it. That means:
- `lexicon.medium_def` (11,666, base codes) and `wa_term_inventory.meaning` (87, sub-glosses)
  **collapse into one column on `term`**;
- the bulk harvest must extend to sub-gloss codes, or the sense has no definition.

⚠ **QUESTION:** is `lexicon` retained as the raw STEP capture (raw layer, immutable, per
`ent.raw.lexicon`) with `term` derived from it — or is `lexicon` retired into `term`? The
three-config model says raw holds what STEP said; the term is arguably that plus the study's
additions (cluster, owning word). **This is the biggest open structural question in the data
layer.**

---

### 3.3 `word_term` — the junction, from Hop 10

| element | verdict | WHERE — use · expectation | WHEN | on_fail |
|---|---|---|---|---|
| `word` | **DECIDED** | the registry word · required | Hop 10 | — |
| `term` | **DECIDED** | the Strong's · required | Hop 10 | — |
| *(pair)* | **DECIDED** | **unique** — one edge per (word, term) | Hop 10 | duplicate → `report-continue`, ignore |
| `decision_group` | **QUESTION** | why this term is attached — F0–F5 | Hop 6 | — |
| `decision_reason` | **QUESTION** | the human-readable why | Hop 6 | — |
| `is_owner` | **QUESTION** | the live model has OWNER vs XREF: one word is the term's canonical home | Hop 10 | — |

**`is_owner` — the QUESTION that matters.** The live DB carries ~5,500 OWNER + ~1,500 XREF. If a
term's facts now live on `term` (§2), **XREF may be obsolete** — it existed to say "this copy is a
duplicate of the real one", and there are no copies any more. But *ownership* may still be needed
for a different reason: which word's build-out is responsible for the term, and whose signoff
covers it. ⚠ **Not decided.**

**`decision_group` / `decision_reason`** are Hop 6's output, and Hop 6 is undeclared — F0–F5, the
particle ceiling (1000), the proper-noun heuristic all live in code. **QUESTION:** does the
decision belong on the edge (this word includes this term because…) or on the term?

---

### 3.4 `term_related` — from Hop 4/5

| element | verdict | WHERE — use · expectation | WHAT/HOW | WHEN | on_fail |
|---|---|---|---|---|---|
| `term` | **DECIDED** | the term this relates from · required | — | Hop 5 | — |
| `related_strongs` | **DECIDED** | the related code · required | STEP `relatedNos[].strongNumber` **or** `definitions[].strongNumber` | Hop 5 | — |
| `gloss` | **DECIDED** | the relative's sense | STEP `gloss` | Hop 5 | — |
| `script_form` | **DECIDED** | the relative's word | STEP `matchingForm` — **⚠ not even captured today** | Hop 5 | — |
| `transliteration` | **DECIDED** | reading aid | STEP `stepTransliteration` | Hop 5 | — |
| `popularity` | **QUESTION** | the relative's frequency — **`definitions[].popularity` == `getInfo.count`** | STEP | Hop 5 | — |

**★ This table is what cluster assignment compares against** (Hop 11). It is the signal for
"does this term relate to that cluster's terms". **So its completeness is not cosmetic — it is
the cluster rule's evidence base.** Today: `wa_term_related_words` holds 103,944 rows with
`strongs_number · gloss · transliteration` and **drops `matchingForm`**.

⚠ **QUESTION — one source or two?** `relatedNos` (from `getInfo`) and `definitions[]` (free on
the verse call) both give the relatives. Are they the same set? **The dumps are on disk; the
comparison costs nothing.** If they agree, Hop 5's per-relative `getInfo` calls are redundant.

**`root_family` — BYPASS.** `wa_term_root_family` (2,861) is **2,188 rows backfilled by clustering
`wa_term_related_words`** — i.e. derived from the relatives, not from etymology. Whether the new
DB needs it as a stored thing, or whether it *is* the relatives read another way, is not clear.
Marked.

---

### 3.5 `term_meaning` (the parse) — from Hop 9

| element | verdict | WHERE — use · expectation | WHAT/HOW | WHEN | on_fail |
|---|---|---|---|---|---|
| `term` | **DECIDED** | required | — | Hop 9 | — |
| `sense_code` | **DECIDED** | `1)`, `1a)`, `1b1)` — the position in the tree | parsed from `mediumDef` | Hop 9 | — |
| `sense_text` | **DECIDED** | the sense itself | parsed | Hop 9 | — |
| `parent_sense` | **DECIDED** | the tree edge | parsed | Hop 9 | — |
| `stem_label` | **BYPASS** | Hiphil / Piel etc. | parsed | Hop 9 | — |
| `language` | **DECIDED** | **which parser to use** · required | **the term's language, passed in** | Hop 9 | absent → **`report-stop`, never default** |
| `parse_version` | **DECIDED** | which parser produced this | the run | Hop 9 | — |

**`language` here is the 7,739-row defect, and the fix is an expectation, not a code change.**
`parse_term` reads `vocab.get("language", "Hebrew")` — **a default**. If the schema's expectation
says *required, no default*, the caller cannot silently pass nothing. **The rule is what makes the
bug impossible, not the patch.**

⚠ **BYPASS — `stem_label`:** stems are a morphology concept and morphology is a span property. A
stem on a *lexicon definition* is STEP describing the lemma's forms, not this occurrence's form.
Whether that belongs on the term's meaning at all is unclear. Marked.

**⚠ QUESTION — is the parse raw or base?** It reads text STEP gave (raw) and produces structure by
a stated rule (base's definition exactly: *"reproducible by following a rule stated in this
config, without reading what the text means"*). **I think it is base, not raw** — v4 put it in
raw's hops because that is where the code runs it.

---

### 3.6 `verse` — from Hop 7

| element | verdict | WHERE — use · expectation | WHAT/HOW | WHEN | on_fail |
|---|---|---|---|---|---|
| `osis_id` | **DECIDED** | the addressable verse · required · **unique** | STEP `osisId` | Hop 7 | — |
| `reference` | **DECIDED** | human-readable | STEP `key` | Hop 7 | — |
| `book` · `chapter` · `verse_num` | **DECIDED** | parsed from `osis_id` | derived | Hop 7 | — |
| `testament` | **DECIDED** | OT · NT | derived from book | Hop 7 | — |
| `text` | **DECIDED** | the verse text · required | STEP `preview`, HTML stripped | Hop 7 | — |
| `translation` | **DECIDED** | **provenance** | **IBA-wide (R22)** — hard-coded `'ESV'` today | Hop 7 | — |
| `step_version` | **DECIDED** | which module · required | **IBA-wide** | Hop 7 | — |

⚠ `verse.verse_text` in the live DB **includes the reference as a prefix** ("1Ch 10:1 Now the
Philistines…") and `wa_verse_records.verse_text` is inconsistent about it. **The expectation must
say which.**

---

### 3.7 `span` / `morphology` — **BYPASS**

**Marked and bypassed, per instruction, for a reason that is not vagueness:**

**B4 / R21 decides what a term is.** If the sub-gloss codes are **four disjoint senses** (which is
what the data says: `H7307G/H/I/J`, 366 occurrences partitioned, zero overlap), then a span's
term is a *sense* and the span table joins to the sense. If they are **unioned into one lemma**,
the span joins to the lemma and the sense is lost. **The span's identity depends on that ruling.**

The researcher: *"this is likely to branch out into a multi layered decision making tree based on
how the source STEP data is parsed into the destination data… I expect a much more detail analysis
of this section before I can respond."*

**What is known and can be recorded now:**
- the interlinear is complete and canon-wide: `verse_morphology` 325,507 rows, one per word of
  every verse; `verse_morphology_raw` 25,634 — the raw HTML kept, so it is re-parseable
- a span carries **multiple** Strong's: `strongs='H7307G H9002'` — the word **and its attached
  particles**, aligned positionally with `morph='HNcfsc HC'`
- `morph_code` is an opaque token holding gender, number, **state** (construct vs absolute),
  person and stem. `HNcfsc` = construct = *"Spirit **of** God"*. Only `pos` and `stem` are pulled
  out. **Decomposition is undesigned.**
- ⚠ **Hop 7's backtrack reads `verse_span_index` mid-fetch** — raw reading base — **and returns
  nothing for a new word**, so the siblings are dropped for exactly this run.

---

### 3.8 `cluster` edge — from Hop 11

| element | verdict | WHERE — use · expectation | WHEN | on_fail |
|---|---|---|---|---|
| `term` | **DECIDED** | required · **one cluster per term** | Hop 11 | — |
| `cluster` | **DECIDED** | the analysis group · required | Hop 11 | none fits → `pause-continue` |
| `assigned_by` | **DECIDED** | the rule, or the researcher · required | Hop 11 | — |
| `assignment_reason` | **DECIDED** | **which terms it matched, and how** — this is what makes it regenerable | Hop 11 | — |
| `escalation_id` | **DECIDED** | when the researcher decided it | Hop 11 | — |
| `subgroup` | **BYPASS** | placement within a cluster — a second, finer question | — | — |

**`assignment_reason` is not decoration.** `base.definition` now says base is regenerable
*because* the rules are documented. An assignment that does not record **what it matched** cannot
be re-derived and compared — which is `open.base.cluster-regenerability`.

---

### 3.9 `escalation` — from Hops 2 and 11

| element | verdict | WHERE — use · expectation |
|---|---|---|
| `escalation_id` · `run_id` | **DECIDED** | which run paused · required |
| `at_step` | **DECIDED** | **where to resume** · required — this is what makes it a pause, not a fork |
| `type` | **DECIDED** | `prompted` · `interactive` (§1.5 v4) · required |
| `question` | **DECIDED** | required |
| `preset_details` | **DECIDED** | **the context that lets it be answered** · required for `prompted` |
| `options` | **DECIDED** | the closed answer set · required for `prompted` |
| `tried` | **DECIDED** | what the app attempted first · **required** — an escalation that skipped the attempt is a defect |
| `state` | **DECIDED** | raised · answered · resumed · `enum.escalation_state` |
| `answer` · `answered_by` · `answered_at` | **DECIDED** | the decision · **data, not a chat message** |

⚠ **`at_step` is the whole design.** Without it there is no resume, and without resume an
escalation is the fork the researcher forbade.

---

### 3.10 `run` — from Hop 0

| element | verdict | WHERE — use · expectation | WHEN |
|---|---|---|---|
| `run_id` | **DECIDED** | required · unique | Hop 0 |
| `work_package` | **DECIDED** | which package · required | Hop 0 |
| `params` | **DECIDED** | what it was asked to do · required | Hop 0 |
| `runs_over` | **DECIDED** | the scope — here, the word | Hop 0 |
| `config_version` | **DECIDED** | **the config that ran** · required **before any work** | Hop 0 |
| `state` | **QUESTION** | running · paused · done · failed — **`paused` is new** (B3) | throughout |
| `resume_point` | **DECIDED** | which sequence entry to resume at | on pause |
| `outcome` · `started_at` · `ended_at` | **DECIDED** | | Hop 0, end |

⚠ **QUESTION:** does this replace `engine_run_log` / `word_run_state` / `term_fetch_log`, or wrap
them? `word_run_state` shows the approval workflow **never operated**: `researcher_approved`=0 on
all 539 rows, `approved_at` 100% NULL, `approved_by` only ever `'PROVISIONAL'`. **The mechanism
this run needs was declared before and never worked** — worth knowing why before rebuilding it.

**The fetch log** (per STEP call: api · query · version · rows · **reported total** · cap verdict)
is the only evidence a fetch was complete. **DECIDED** it exists; ⚠ **QUESTION** whether it is
part of the run record or its own thing.

---

## 4. Marked and bypassed

| # | thing | why |
|---|---|---|
| BY1 | **span / morphology** | R21 decides what a term is; the span's identity depends on it (§3.7) |
| BY2 | `morph_code` decomposition | state/gender/number/person are in an opaque token; undesigned |
| BY3 | `root_family` | 2,188/2,234 backfilled from the relatives — may not be a thing of its own (§3.4) |
| BY4 | `stem_label` on the meaning parse | a morphology concept on a lexicon definition (§3.5) |
| BY5 | `term.is_sense_of` | R21 |
| BY6 | `cluster.subgroup` | a finer question than membership |
| BY7 | `word.description` / `inference_note` | researcher prose; this run does not touch it |

---

## 5. Questions

| # | question | why it matters |
|---|---|---|
| Q1 | **★ Is `lexicon` retained as the raw STEP capture with `term` derived from it, or retired into `term`?** | §3.2. The biggest structural question in the data layer. Today the definition sits in `lexicon` at base-code grain and the study reads `wa_term_inventory` at sub-gloss grain — which is why 99% is empty |
| Q2 | **The grain** (§2) — term facts on the term, (word, term) as a junction | follows from the data; not a ruling. It retires `wa_term_inventory` as it stands |
| Q3 | **`is_owner` / XREF** — obsolete once terms are single-rowed, or still needed for responsibility? | §3.3 |
| Q4 | **`origin` vs `source`** — two columns, one fact? | §3.1 |
| Q5 | **`term.language`** — from the code prefix? Aramaic is invisible there, and the live `lexicon` claims **1** Aramaic row | §3.2 |
| Q6 | **Is the meaning parse raw or base?** | §3.5 — it reads raw text and derives by a stated rule. I think base |
| Q7 | **`relatedNos` vs `definitions[]`** — same set? | §3.4. **Free to answer — the dumps are on disk.** If they agree, Hop 5's per-relative calls are redundant |
| Q8 | **Hop 6's decision layer** — F0–F5 are code constants | §3.3. A judgement layer with no rule |
| Q9 | **The run record** — replace or wrap `engine_run_log`/`word_run_state`? | §3.10. The approval mechanism was declared before and never operated |
| Q10 | **`enum.word_status`** — proposed from the run's shape | §3.1 |

---

## 6. What this settles

**The 99% empty `meaning` column is a grain error, not a wiring error.** I have reported it three
ways in two days — "a column nobody feeds", "two columns for one fact", and now the truth: **the
definition is stored against the base code, which has no verses; the study reads the sub-gloss,
which has the verses.** Both columns are behaving exactly as built. The design is what is wrong.

And it follows the researcher's rule precisely: *the feeder defines what must be pushed based on
the source or the task, then confirms the column exists, is coherent, is not duplicated
elsewhere.* Run that on `meaning` and every clause fails — **coherent** (wrong grain),
**not duplicated** (two of them), **not recorded differently** (base vs sub-gloss). The check
would have caught this on day one.
