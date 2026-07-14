# WA — Projection Spec: Flattened Reading View

**File:** WA-projection-spec-1.2-2026-07-13.md
**Date:** 2026-07-13
**Version:** 1.2
**Author:** le Roux Cilliers
**Built from:** `psalms__grace-mercy-compassion.json` (16 readings). Worked examples attached.
**Prior output:** `WA-assess-raw-source-json-1.0-2026-07-13.md`

---

## 0. What actually determines the limit — corrected in v1.1

**v1.0 asked the wrong question, and so did I.** There is no "maximum CSV size." File size is not a constraint, because **I do not have to read the file.** I have a Python environment: a 5 MB CSV, or the full 4.7 MB raw JSON set, is trivially processed on disk. Format is close to irrelevant — JSON parses as easily as CSV.

**Only what is read *verbatim into context* costs anything.** There are two separate budgets, and I conflated them:

| Budget | Limit | What it constrains |
|---|---|---|
| **Compute (on disk)** | effectively unbounded at this scale | nothing. Any format, any size. |
| **Context (read verbatim)** | ~200 k token window, shared with the system prompt, the conversation, prior outputs, reasoning and the response being written — realistically **100–130 k for one ingested artefact** | only the columns whose *meaning* I must read. |

### The rule that actually governs it

| Column class | Must be read? | Why |
|---|---|---|
| **Coded / controlled** — `lemma`, `verse_ref`, `seat`, `source`, `type`, `locus`, `role`, `intensity`, `effect`, `prohibition`, `NONE`/`ABSENT` flags | **No — never.** | Counted mechanically, 100% reliably. These are the machine's own invariant strings. Counting them is exactly the operation that *is* trustworthy (session log B.4). |
| **Free text** — `sense`, `operation`, `discovery`, `coupling`, `target`, `bearer` | **Yes — always.** | Meaning cannot be counted. Every attempt to regex prose in this session produced garbage and was disowned. |

### Measured, from the real file

| | bytes/row | tokens/row | across 2,048 readings |
|---|---|---|---|
| Coded columns | 175 | 44 | ~359 KB / **~90 k tokens — and I need to read none of it** |
| **Free-text columns** | **243** | **61** | **~498 KB / ~124 k tokens — the real constraint** |
| Everything | 418 | 105 | ~856 KB / ~214 k tokens |

**And the free-text budget does not have to be paid in one pass.**

- One family at a time (avg 45 readings): **~2.7 k tokens.** Trivial.
- The largest theme (`praise-extol-sing`, 167 readings): **~10 k tokens.** Comfortable.

### Consequence: the two-tier split in v1.0 was solving a problem that does not exist

**One flat file. Read columns selectively.**

- Coded columns → computed over on disk, corpus-wide, any time, at zero context cost. Every check in §1 below runs on these.
- Free-text columns → read family by family, as each exploration reaches it.

**Format:** CSV, JSONL or JSON are all acceptable. CSV is ~30–40 % smaller than indented JSON and easiest to slice by column; JSONL preserves types. **The gain is not the format — it is (i) flattening the 16 dimensions from 176 verbose row-objects into 16 rows × 16 columns, and (ii) dropping `passage_text`.** Those two changes do the work. The choice of serialisation does not.

**One caveat worth noting:** `discovery` alone is **145 of the 243 free-text bytes per row — 60 % of the entire read budget.** If it has indeed been repurposed as a sense-seed rather than the discovery-lookout (assessment §2.7), then the single largest thing I would be reading is not doing the job its name claims. That should be settled before the projection is generated.

---
## 1. The flat file (v1.1: single tier)

**One row per `reading_id`. All 16 dimensions as columns. `passage_text` dropped.**

`reading_id, lemma, span_id, morph, hebrew_form, translit, char_key, ib_char, family, cluster, verse_ref, anchor, same_as, sense, type, source, seat, bearer, operation, target, object_kind, direction, manner, intensity, specifier, effect, coupling, prohibition, discovery, role, locus`

**Four of these are new in v1.2 and they are the point of the exercise:**

| Column | Why |
|---|---|
| **`span_id`** | The STEP span. **This is the actual discriminator between readings of the same lemma** (H2603 → four readings, four spans). It currently appears only inside `to_span` on some dimension rows, ambiguously. It must be explicit and at the lexical level. |
| **`morph`** | The morphological parse the study reads. Exists upstream; **does not travel with the emitted data at all.** |
| **`hebrew_form`** | The surface form in the verse. Absent everywhere. |
| **`translit`** | Currently buried inside the free text of `sense` and `discovery` (`pity (chanan)`). Promote it to a column — it is *data*, not prose. |

`direction` and `object_kind` remain as specified in v1.1 §4.

**Without `span_id` and `morph`, the artefact shows only `H2603:generou` vs `H2603:pity` — lemma plus English label — and every reader of it will conclude the split is gloss-driven. It is not. But the evidence must travel with the data.**

**Measured (v1.1 column set): 418 bytes/row → ~856 KB → ~214 k tokens for all 2,048 readings.** The four new columns are short coded values and add negligibly — and `span_id`, `morph`, `hebrew_form` are **coded columns**, so they cost **zero read budget** (§0). It does not need to fit in one pass, and it does not need to. See §0.

**Two state codes, and the distinction is the whole point:**

| Code | Source | Meaning |
|---|---|---|
| `NONE` | `value: "none"` | **The reader looked and found none.** This *is* evidence of silence. |
| `ABSENT` | `present: false` | **No row was recorded.** This is *not* evidence of silence — it is absence of reading. |

Everything else is the recorded value.

Collapsing these two into a blank cell would destroy the single most important distinction in the dataset — and it is exactly the distinction the narrative layer already lost, which is how the intensity/effect silence came to be asserted without evidence.

**Live example, verbatim from the attached file:**

```
reading_id,lemma,ib_char,family,cluster,verse_ref,anchor,type,source,seat,bearer,target,manner,intensity,effect,coupling,prohibition,role,locus
H2603:generou#1,H2603,generous,grace-mercy-compassion,Blessing,Psa 37:21,True,volition,ABSENT,NONE,the righteous,generosity,NONE,ABSENT,ABSENT,generous-and-gives,ABSENT,characteristic,internal:ib-state
H2580:grac#1,H2580,grace,grace-mercy-compassion,Blessing,Psa 45:2,True,status,ABSENT,NONE,the king,NONE,poured on his lips,ABSENT,ABSENT,the graciousness for which God blessed him,ABSENT,characteristic,internal:ib-state
H8467:mercy#1,H8467,mercy,grace-mercy-compassion,Prayer,Psa 55:1,True,action,ABSENT,NONE,the psalmist,to God,NONE,ABSENT,ABSENT,twinned with the prayer,ABSENT,characteristic,external:god
```

Note what is already visible in three rows: **`seat` is `NONE` on all three** (reader determination — E1 confirmed); **`source`, `intensity`, `effect`, `prohibition` are `ABSENT` on all three** (never read); `type` carries a small controlled vocabulary (`volition` / `status` / `action`); and `target` on row 3 holds **`to God`** — a *direction*, sitting in the target field because there is nowhere else for it to go.

### What Tier 1 alone would settle, in one pass

These are the checks currently blocked, and each is a single query once the file exists:

1. **Is `seat: NONE` universal across all 46 families?** Currently the strongest finding of the session, resting on one family and one theme.
2. **Are `source` / `intensity` / `effect` `ABSENT` everywhere, or only here?** This determines whether E1's declared-silence closers are evidenced *anywhere in the corpus*.
3. **How many lemmas are fragmented by English gloss** (H2603 → pity / generous / deals generously)?
4. **Is `coupling` ↔ `locus` swapped in other families,** and how widely? (10 of 16 here.)
5. **What is the controlled vocabulary of `type`,** and is it a faculty bin under another name?
6. **Every observation in every exploration to date can be re-bound to a verse and a lemma.**

---

## 2. How it is worked — superseded tiering

v1.0 proposed two files. v1.1 proposes **one file, two modes of access**:

- **Corpus-wide, on disk, zero context cost:** every coded column. All six checks in §1 run here, across all 46 families, at any time.
- **Family by family, read into context (~2.7 k tokens each):** the free-text columns, when an exploration reaches that family.

This lets an exploration cite *what the reader actually determined* rather than what the narrative said about it — which, on the evidence of the assessment, are not always the same thing.

---

## 3. What is deliberately dropped

| Dropped | Why |
|---|---|
| `passage_text` | ~2,800 words per family, the single largest component. I can read the Psalm. |
| `ve_lexical_ids` (the 11-per-lexical arrays) | Backtracking keys. Not needed in the working view; recoverable from the DB on demand. |
| `passage_ref` | Superseded by `verse_ref`. Retain in Tier 2 only if the passage boundary is itself analytically meaningful. |
| Per-dimension `from_span` / `to_span` / `provenance` / `notes` | `notes` is populated **0 times**; `from_span` **4 times of 176**; `provenance` is a constant. Retain `resolution` if the `inferred` vs recorded distinction matters — it is populated on 82 of 176 rows and I would want it if it is cheap. |

---

## 4. Two fields I would add at generation, not after

1. **`direction`** — the slot already exists on every `ve_lexical` row and is **null in all 176**. E4's preliminary finding is that direction may be the edge that *constitutes* the movement. Populating it costs nothing structurally.
2. **`object_kind`** — a small controlled vocabulary beside `target`: `god / person / self / thing / abstraction / null`. Row 3 above shows why: `target: "to God"` is currently doing the job of both, badly.

---

## 5. Deliverables attached

| File | Rows | Size | Note |
|---|---|---|---|
| `WA-projection-tier2-example-1.0-2026-07-13.csv` | 16 | 6,942 B | **This is now the target shape** — all columns, one row per reading. |
| `WA-projection-tier1-example-1.0-2026-07-13.csv` | 16 | 3,601 B | Retained only as an illustration of the coded-column subset. Not a separate deliverable. |

Both are the **real projection of the real file**, not mock-ups.

---

## Change control

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-07-13 | First issue. Corrects the "entirely tractable" estimate. Specifies a two-tier projection. |
| 1.2 | 2026-07-13 | **Adds `span_id`, `morph`, `hebrew_form`, `translit` as lexical-level columns.** The study reads morphology via the STEP span; the emitted data carries neither. `span_id` is the true discriminator between readings of one lemma and must be explicit. All four are coded columns — zero read cost. |
| 1.1 | 2026-07-13 | **Corrects §0 and collapses the tiering.** File size is not the constraint — compute on disk is unbounded and format is near-irrelevant. The constraint is **free-text volume read into context (~124 k tokens corpus-wide, ~2.7 k per family)**, and it need not be paid in one pass. Coded columns never need reading at all. **One flat file, columns read selectively.** The gain is flattening + dropping `passage_text`, not CSV as such. |
