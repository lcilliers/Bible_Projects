# term → sense → span — the structure, confirmed

> **v6 · 2026-07-17.** Answers the researcher's comments on v5 (1.1, 1.2, 1.3, 2, 3.2, 3.3) before
> anything downstream moves. **All the work is in this document. No config created or loaded.**
>
> **The headline:** the structure the researcher described is right, the data proves it, and it
> dissolves R21, OWNER/XREF and the "missing meaning" in one move.

---

## 1. ★ The structure, confirmed against STEP

> *"word - find terms and related terms - find verses for all - get span of verses - find meaning
> of span. Each verse will have multiple span, span is backtracked to the term via the meaning.
> confirming this structure is fundamental on how the hops would work."*

**Confirmed. Measured today, live:**

```
H7307G  gloss 'spirit'          head ': spirit'         tree '1) wind, breath, mind, spirit  1a) breath  1b) wind…'
H7307H  gloss 'spirit: breath'  head ': breath/wind'    tree  ← BYTE-IDENTICAL
H7307I  gloss 'spirit: side'    head ': side'           tree  ← BYTE-IDENTICAL
H7307J  gloss 'spirit: temper'  head ': temper'         tree  ← BYTE-IDENTICAL
```

**Every sub-gloss carries the same definition tree and its own head.** That is not a coincidence
of formatting — it is the data model showing itself:

| layer | is | STEP gives it as |
|---|---|---|
| **TERM** | the lemma — `H7307` *ruach* | the **shared tree**: `1) wind, breath, mind, spirit 1a) breath 1b) wind…` |
| **SENSE** | one meaning of the lemma — `H7307G` | the **head** (`': spirit'`) + the gloss (`'spirit'`) + its own verse set |
| **SPAN** | one occurrence in one verse | `strongs='H7307G H9002'` — **it names its sense** |

**So the chain is exactly the researcher's:**

```
word → terms (+ related terms) → verses for all → spans of verses → meaning of span
                                                        │
                                    span names its SENSE ─┴─→ sense belongs to a TERM
                                        ↑ the backtrack, VIA THE MEANING
```

**A span does not carry a term. It carries a sense.** The term is reached *through* the sense.
That is what *"span is backtracked to the term via the meaning"* means, and it is true in the
data.

### 1.1 The span's meaning is available at ingest, in digestible form

> *"it sounds like you can get the span meaning and save it in digestable format right from the
> start… the other meaning elements are also relevant in the study, but only to understand the
> verse application of the meaning in a broader context."*

**Yes — and it is one field.** Gen 1:2's span carries `H7307G`; `H7307G`'s head is `': spirit'`
and its gloss is `'spirit'`. **That is the span's meaning, decided at the source, per occurrence.**

And the researcher's second clause is exactly the tree: `1) wind, breath, mind, spirit 1a) breath
1b) wind…` is the **term's** full range — relevant for understanding the verse application in a
broader context, and **not** the span's meaning.

**The study has had this backwards.** It read the tree looking for the span's meaning, when the
head already said it. That is `ve_lexical_verification`'s recurring diagnosis in one line:
*"the stored sense states an inferred inner state or the verse's effect rather than what the word
means."* The word's meaning was one field away.

### 1.2 ★ This resolves R21 — and there is no fork

R21 asked: union the sibling codes into one lemma, or keep them separate?

**Neither. They are the term's senses.**

- Union them → *spirit* + *breath* + *side* + *temper* collapse into one bucket. The sense STEP
  decided per occurrence is destroyed.
- Keep them as separate *terms* → `H7307` has four "terms" that are one word.

**They are one term with four senses, and every occurrence already names which.** 366 occurrences,
partitioned, zero overlap.

**So the "multi-code bug" is not a resolver bug — it is a model error.** `_resolved_strong`
returns `vocabInfos[0]` and the study calls it "the term". It is **one sense of the term**.
Fetching `H7307G` and calling it *ruach* is fetching *spirit* and calling it *ruach*: 194 verses
of 366, and the 137 *breath* verses are not "lost data" — they are **a sense the study never knew
existed**.

⚠ **B4/R21 can be closed on this**, subject to the researcher. The researcher expected *"a multi
layered decision making tree based on how the source STEP data is parsed into the destination
data"* — the tree turns out to be two layers: **term (tree) → sense (head)**.

### 1.3 ★ What `lexicon` actually is — Q1 answered, and it is not good

`lexicon` holds 11,666 rows keyed on **base codes**, `medium_def` populated on **all** of them.
I called that "the term's meaning, complete". **It is not.**

```
lexicon['H7307'] →  gloss 'spirit'   medium_def ': spirit  1) wind, breath, mind, spirit…'
```

**That is `H7307G`'s payload, stored under the key `H7307`.** The harvest asked STEP for `H7307`;
STEP resolved it to `H7307G` and answered with the *spirit* sense; the row was filed under the
base code.

So `lexicon` is:
- **not the term table** — its `gloss` is one sense's gloss
- **not the sense table** — it is keyed on the base, and **0 of 11,666 rows end in a letter**
- **a mislabelled sense table holding one arbitrary sense per lemma** — whichever STEP happened to
  resolve to — with *breath*, *side* and *temper* **absent entirely**

**Q1 answered:** `lexicon` is neither raw capture nor term. It is a harvest that ran before anyone
knew the sub-gloss was a sense. Its `medium_def` is genuinely useful — it is the **tree** — but
its key is wrong and its `gloss` belongs to a sense that is not named.

---

## 2. 3.3 answered — OWNER / XREF has no purpose in the new model

> *"can you explain to me what is the value/purpose of the 'owner' status of a term. what is the
> basis of deciding it? is there really a place for XREF."*

**Measured:**

```
OWNER   3,996 rows / 3,979 distinct   → ~one per Strong's
XREF    3,380 rows / 1,762 distinct   → ~1.9 per Strong's
NULL      468 rows

H0226G:  1 OWNER + 13 XREF = 14 word-copies of one term
```

**The purpose:** the term row is duplicated once per word that uses it. `OWNER` marks *which copy
is the real one*; `XREF` marks *this is a duplicate — do not process it, take the owner's answers*.
It is why XREF verses are `delete_flagged` and XREF verse-context is "derived from OWNER".

**The basis of deciding it:** whichever word onboarded the term first became its owner. **Not a
study judgement — an accident of processing order.**

**Is there a place for XREF? No.**

**XREF is a workaround for the grain error.** It exists to manage duplicate term rows. Store the
term **once** (§3) and there are no duplicates, so there is nothing for XREF to mark. The whole
OWNER/XREF apparatus — the `term_owner_type` column, the delete-flagged XREF verses, the
"VC derived from OWNER" rule, the ~1,500 XREF copies — **is scaffolding around a table shape that
should not exist.**

**And it never worked anyway:** `has_meaning` is 27/3,996 on OWNER rows and 44/3,380 on XREF. The
"canonical copy" does not carry the definition either.

⚠ **What might survive, and it is a different question:** *which word's build-out is responsible
for a term, and whose signoff covers it.* That is a property of the **word↔term edge**, not of the
term, and it is not ownership — it is **provenance**: which word first brought this term in. It
answers a different question and needs a different name.

---

## 3. The relationship design — what data at what level

> *"I would like to see the relationship table design for this — this is not a single row. this
> would sort out what data you are saving at what level (e.g. language is at span level)"*

Five levels. **Each fact sits at exactly one.**

```
  WORD                     "anger"                    the researcher's entry point
    │  (word_term)          many-to-many
  TERM                     H7307   ruach              the lemma · THE TREE
    │  (one term, many senses)
  SENSE                    H7307G 'spirit'            the head · its own verse set · THE SPAN'S MEANING
    │  (one sense, many occurrences)
  SPAN                     Gen 1:2 word 8             morph · surface · the attached particles
    │  (many spans per verse)
  VERSE                    Gen 1:2                    the text
```

| level | holds | why here | from |
|---|---|---|---|
| **word** | the English word · source · status · approval | the entry point | the researcher |
| **word_term** | the (word, term) edge · why this term was attached (F0–F5) · **which word introduced it** | a term serves several words | Hop 6/10 |
| **term** | base Strong's · **the definition tree** · related terms · root family | one lemma, one row, written once | `getInfo` |
| **sense** | sub-gloss code · **head** · gloss · occurrence count | **the sense is the unit the span names** | `getInfo` per sub-gloss |
| **span** | verse · word_index · surface · **morph_code** · **language** · the attached particles (`H9002`) · **its sense** | ⚠ **the researcher: language is at SPAN level** | `getBibleText` |
| **verse** | osis_id · reference · text · translation · step_version | the addressable unit | `masterSearch.strong` / `getBibleText` |

**`language` at span level — why the researcher is right.** Language is a property of *this
occurrence's morphology* (`morph_code` starts `H`/`G`), and `project_morph_is_source_of_truth`
says exactly that. A **term** has no morph — a lemma is not inflected. So `term.language` was
always a derived convenience from the code prefix, and that is precisely how
`wa_meaning_parsed.language` read `Hebrew` on 7,739 rows: **a span-level fact stored at term
level, defaulted.**

⚠ **QUESTION:** the term still needs *which lexicon it is in* (Hebrew vs Greek Strong's). That is
the code prefix, and it is not the same fact as the span's language. **Two facts, currently one
word.** Aramaic makes it visible: the live `lexicon` claims **1** Aramaic row, which is not
credible — Aramaic spans exist and carry `H`-prefixed codes.

### 3.1 The span carries more than one code

```
'Spirit'   strongs='H7307G H9002'   morph='HNcfsc HC'
'earth'    strongs='H0776G H9002 H9009'  morph='HNcfsa HC HTd'
```

Positionally aligned: the word **plus its attached particles** (waw, article). So the span→sense
edge is **the head code**, and the particles are a separate fact about the span. ⚠ The study
filters `^[HG]9` as "grammar particles" and drops them — but *"and the Spirit"* vs *"the Spirit"*
is `H9002`, and that is meaning.

---

## 4. Tables that become redundant, and why

> *"lets redesign the terms table(s) to fit (this may mean some tables becomes redundant.
> investigate it properly and name the tables that becomes redundant and why)"*

| table | rows | verdict | why |
|---|---|---|---|
| **`wa_term_inventory`** | 7,844 | **REDUNDANT — split** | a word×term junction holding term facts (`H3588A` × 18). Term facts → `term`/`sense`; the edge → `word_term` |
| **`mti_terms`** | 7,861 | **REDUNDANT — merge** | **also** a word×term junction (`owning_registry_fk`; `H3487` × 15). **Two tables doing one job.** Its real content — `cluster_code` — is the term↔cluster edge |
| **`lexicon`** | 11,666 | **REDUNDANT — rebuild** | a mislabelled sense table: one arbitrary sense per lemma, keyed on the base (§1.3). Its `medium_def` (the tree) is worth keeping; its key and its `gloss` are wrong |
| **`wa_term_related_words`** | 103,944 | **REDESIGN** | correct idea, wrong grain — hangs off `term_inv_id` (per word×term), so relatives are duplicated per word. Belongs on `term` |
| **`wa_term_root_family`** | 2,861 | **QUESTION** | 2,188/2,234 backfilled by clustering the relatives — derived from `wa_term_related_words`, not etymology. May not be a thing of its own |
| **`verse_term_index`** | 275,593 | **REDUNDANT — derived** | `(verse_id, primary_strong)`. `verse_span_index` already holds 293,133 distinct such pairs — **more than the index has**, so it is a stale materialised view of the span master |
| **`wa_verse_term_links`** | 237,531 | **REDUNDANT — derived** | verse×term with `step_subgloss_code` — i.e. the span→sense edge, which the span master already carries |
| **`wa_meaning_parsed` / `_sense` / `_stem`** | 7,748 / 17,125 / 13 | **REDESIGN** | the parse is of the **tree**, which is the **term's** — so it belongs once per term, not once per word×term. Currently keyed on `term_inv_id` |
| **`wa_lsj_parsed`** | 9 | **REDESIGN** | same; and it was never fed |
| **`mti_term_cross_refs`** | 462 | **QUESTION** | likely the XREF apparatus (§2) |
| **`wa_term_phase2_flags`** | 1,570 | **QUESTION** | 1,092 bulk_patch with no per-term justification |

⚠ **`verse_span_index` — the researcher's point 2.** *"factor in the use/existence of the
span.term.verse master index table. maybe the new structure replaces this index, it should not
duplicate it."*

`verse_span_index` (325,474) is **the span master + an analytical overlay stamped onto it**
(`role`, `char_candidate`, `characteristic`, `ib_char_id`, `cluster`). The overlay is exactly what
`gate.base.no-judgement` was written to keep out, and what the migration strips.

**So: the new span table replaces it, minus the overlay.** And once the span master exists,
`verse_term_index` and `wa_verse_term_links` are both derivable from it and should not exist.
**Three tables, one fact.**

---

## 5. Registry columns — the researcher's 1.3

> *"origin - drop it; status and signoff has the same value. keep status drop signoff. signoff is
> achieved when the process is completed, validated and status is updated."*
> *"the list does not show all current registry columns, the registry config must deal with all of
> them (or set to drop on migration)"*
> *"status enums: you need to have a config that sets each of these statuses, else drop the enum."*

**`origin` — DROPPED.** **`signed_off_by/_at/_config_version` — DROPPED**; signoff **is** a status
value, reached when the process completes and validates.

**`enum.word_status` — every value must be set by a config, or it goes.** Applying that test:

| value | set by | verdict |
|---|---|---|
| `proposed` | Hop 2 raises the approval escalation | **keep** |
| `approved` | Hop 2's answer | **keep** |
| `built` | Hop 10 writes the tables | **keep** |
| `clustered` | Hop 11 | **⚠ DROP?** — no config *sets* it; it is a **derived** fact (every term has a cluster). A status that restates a gate's answer is a second copy of it |
| `signed-off` | Hop 13 validates → Hop 14 | **keep** — this is the signoff |
| `rejected` | Hop 2's answer | **keep** |

**All 32 registry columns** — the config must rule on every one. ⚠ **Not done here.** It needs the
full list against this run, and `description`/`inference_note` are researcher prose whose purpose
this run does not touch.

---

## 6. What this changes upstream

**The hops change shape**, because the fetch does:

| hop | was | becomes |
|---|---|---|
| Hop 5 expand | "find the term's family" — A–Z probe for siblings | **find the term's SENSES.** The probe is not discovering siblings, it is enumerating senses |
| Hop 7 verses | fetch verses "for the term" | **fetch verses PER SENSE.** `H7307G` 194 + `H7307H` 137 + `H7307I` 7 + `H7307J` 10 = 366. Fetching only `H7307G` fetches one sense |
| Hop 7 backtrack | reads `verse_span_index` to find variants | **unnecessary.** The senses come from `getInfo`'s sub-gloss enumeration at Hop 5 — before any verse is fetched. **The raw→base cycle dissolves** |
| Hop 9 parse | parse `mediumDef` per term | **parse the TREE once per term**; the **head** per sense is not parsed, it is read |

**★ The backtrack disappears.** v4 found `fetch_verses` reading `verse_span_index` mid-fetch to
find sibling codes — raw reading base, and returning nothing for a new word. **Under this model
the senses are known at Hop 5 from STEP itself.** There is nothing to backtrack for.

---

## 7. For review

1. **★ §1 — the structure.** term (tree) → sense (head) → span (names its sense). Confirm and
   everything below follows.
2. **★ §1.2 — R21 closes.** Not union vs separate: **one term, four senses**, each occurrence
   naming its own. Confirm and B4 lifts.
3. **§1.3 — `lexicon` holds one arbitrary sense per lemma, mislabelled as the base.** Rebuild.
4. **§2 — XREF has no place.** OWNER survives only as *which word introduced the term*, on the
   edge, and that is provenance, not ownership.
5. **§3 — `language`.** Span-level, per your ruling. But the term needs *which lexicon* (H/G) —
   is that the same fact? Aramaic says no.
6. **§4 — three tables hold one fact** (`verse_span_index`, `verse_term_index`,
   `wa_verse_term_links`). The new span master replaces all three, minus the overlay.
7. **§3.1 — the attached particles.** `H9002` is *"and"*. The study filters `^[HG]9` away. *"And
   the Spirit"* is not *"the Spirit"*.
8. **§5 — `clustered` as a status.** It restates a gate. Drop?
